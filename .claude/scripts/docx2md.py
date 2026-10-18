#!/usr/bin/env python3
"""
Converte un file Word (.docx) in Markdown pensato per Obsidian.

Uso:
    python3 -I .claude/scripts/docx2md.py "percorso/file.docx" [cartella-di-uscita]

Produce `nome-del-file.md` (e una cartella `img/` con le immagini, se ce ne
sono) nella cartella di uscita (default: la stessa cartella del docx).

Non ha dipendenze esterne: legge direttamente l'XML dentro il .docx.
Gestisce titoli (Heading 1-3 / Titolo 1-3), elenchi puntati e numerati,
grassetto, corsivo, tabelle semplici, immagini e formule (Word OMML -> LaTeX
approssimato, da ricontrollare a mano).

Se e' installato `pandoc`, preferiscilo:
    pandoc "file.docx" -t gfm --wrap=none --extract-media=. -o "file.md"
"""

import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"

HEADING_RE = re.compile(r"^(heading|titolo|berschrift|titre)\s*(\d)$", re.I)


def slugify(name):
    s = name.lower()
    s = re.sub(r"[àáâä]", "a", s)
    s = re.sub(r"[èéêë]", "e", s)
    s = re.sub(r"[ìíîï]", "i", s)
    s = re.sub(r"[òóôö]", "o", s)
    s = re.sub(r"[ùúûü]", "u", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "documento"


def load_styles(z):
    """Mappa styleId -> nome leggibile (es. 'Titolo1' -> 'heading 1')."""
    styles = {}
    try:
        root = ET.fromstring(z.read("word/styles.xml"))
    except KeyError:
        return styles
    for st in root.iter(f"{W}style"):
        sid = st.get(f"{W}styleId")
        name_el = st.find(f"{W}name")
        name = name_el.get(f"{W}val") if name_el is not None else sid
        styles[sid] = (name or sid).lower()
    return styles


def load_rels(z):
    rels = {}
    try:
        root = ET.fromstring(z.read("word/_rels/document.xml.rels"))
    except KeyError:
        return rels
    for rel in root.iter(f"{REL}Relationship"):
        rels[rel.get("Id")] = rel.get("Target")
    return rels


def load_numbering(z):
    """numId -> {ilvl: 'bullet'|'decimal'}."""
    out = {}
    try:
        root = ET.fromstring(z.read("word/numbering.xml"))
    except KeyError:
        return out
    abstract = {}
    for an in root.iter(f"{W}abstractNum"):
        aid = an.get(f"{W}abstractNumId")
        levels = {}
        for lvl in an.iter(f"{W}lvl"):
            fmt = lvl.find(f"{W}numFmt")
            levels[lvl.get(f"{W}ilvl")] = fmt.get(f"{W}val") if fmt is not None else "bullet"
        abstract[aid] = levels
    for num in root.iter(f"{W}num"):
        nid = num.get(f"{W}numId")
        ref = num.find(f"{W}abstractNumId")
        out[nid] = abstract.get(ref.get(f"{W}val") if ref is not None else "", {})
    return out


def heading_level(style_name, style_id):
    for candidate in (style_name or "", style_id or ""):
        m = HEADING_RE.match(candidate.strip())
        if m:
            return int(m.group(2))
    return 0


def omath_to_latex(el):
    """Traduzione approssimata di Office Math (OMML) in LaTeX."""
    tag = el.tag
    if tag == f"{M}r":
        return "".join(t.text or "" for t in el.iter(f"{M}t"))
    if tag == f"{M}f":
        num = el.find(f"{M}num")
        den = el.find(f"{M}den")
        return "\\frac{%s}{%s}" % (omath_children(num), omath_children(den))
    if tag == f"{M}sSup":
        return "%s^{%s}" % (omath_children(el.find(f"{M}e")), omath_children(el.find(f"{M}sup")))
    if tag == f"{M}sSub":
        return "%s_{%s}" % (omath_children(el.find(f"{M}e")), omath_children(el.find(f"{M}sub")))
    if tag == f"{M}sSubSup":
        return "%s_{%s}^{%s}" % (
            omath_children(el.find(f"{M}e")),
            omath_children(el.find(f"{M}sub")),
            omath_children(el.find(f"{M}sup")),
        )
    if tag == f"{M}rad":
        deg = el.find(f"{M}deg")
        d = omath_children(deg) if deg is not None else ""
        body = omath_children(el.find(f"{M}e"))
        return "\\sqrt[%s]{%s}" % (d, body) if d else "\\sqrt{%s}" % body
    if tag == f"{M}d":  # delimitatori (parentesi)
        return "\\left(%s\\right)" % " , ".join(omath_children(e) for e in el.findall(f"{M}e"))
    if tag == f"{M}nary":  # sommatorie, integrali
        chr_el = el.find(f"{M}naryPr/{M}chr")
        sym = chr_el.get(f"{M}val") if chr_el is not None else "∫"
        ops = {"∑": "\\sum", "∏": "\\prod", "∫": "\\int"}
        return "%s_{%s}^{%s} %s" % (
            ops.get(sym, sym),
            omath_children(el.find(f"{M}sub")),
            omath_children(el.find(f"{M}sup")),
            omath_children(el.find(f"{M}e")),
        )
    return omath_children(el)


def omath_children(el):
    if el is None:
        return ""
    return "".join(omath_to_latex(c) for c in el)


def run_text(run):
    """Testo di un <w:r>, con grassetto/corsivo e immagini."""
    pieces = []
    rpr = run.find(f"{W}rPr")
    bold = rpr is not None and rpr.find(f"{W}b") is not None and rpr.find(f"{W}b").get(f"{W}val") != "0"
    italic = rpr is not None and rpr.find(f"{W}i") is not None and rpr.find(f"{W}i").get(f"{W}val") != "0"
    for child in run:
        if child.tag == f"{W}t":
            pieces.append(child.text or "")
        elif child.tag == f"{W}tab":
            pieces.append(" ")
        elif child.tag in (f"{W}br", f"{W}cr"):
            pieces.append("\n")
        elif child.tag == f"{W}drawing":
            for blip in child.iter(f"{A}blip"):
                rid = blip.get(f"{R}embed")
                pieces.append(f"\x00IMG:{rid}\x00")
    text = "".join(pieces)
    if not text.strip():
        return text
    if bold and italic:
        return f"***{text}***"
    if bold:
        return f"**{text}**"
    if italic:
        return f"*{text}*"
    return text


def paragraph_text(p):
    out = []
    for child in p:
        if child.tag == f"{W}r":
            out.append(run_text(child))
        elif child.tag == f"{W}hyperlink":
            out.append("".join(run_text(r) for r in child.iter(f"{W}r")))
        elif child.tag == f"{M}oMathPara":
            for om in child.findall(f"{M}oMath"):
                out.append("\n$$\n" + omath_children(om).strip() + "\n$$\n")
        elif child.tag == f"{M}oMath":
            out.append("$" + omath_children(child).strip() + "$")
    text = "".join(out)
    # unisce grassetti/corsivi spezzati su piu' run contigui
    text = re.sub(r"\*\*(\s*)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*(\s*)\*(?!\*)", r"\1", text)
    return text


def table_to_md(tbl):
    rows = []
    for tr in tbl.findall(f"{W}tr"):
        cells = []
        for tc in tr.findall(f"{W}tc"):
            cell = " ".join(paragraph_text(p).strip() for p in tc.findall(f"{W}p"))
            cells.append(cell.replace("|", "\\|").replace("\n", " "))
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def convert(docx_path, out_dir=None):
    docx_path = os.path.abspath(docx_path)
    base = slugify(os.path.splitext(os.path.basename(docx_path))[0])
    out_dir = os.path.abspath(out_dir or os.path.dirname(docx_path))
    os.makedirs(out_dir, exist_ok=True)

    z = zipfile.ZipFile(docx_path)
    styles = load_styles(z)
    rels = load_rels(z)
    numbering = load_numbering(z)
    body = ET.fromstring(z.read("word/document.xml")).find(f"{W}body")

    img_dir = os.path.join(out_dir, "img")
    images = {}  # rId -> nome file salvato
    counter = [0]

    def save_image(rid):
        if rid in images:
            return images[rid]
        target = rels.get(rid)
        if not target:
            return None
        member = "word/" + target.lstrip("/") if not target.startswith("word/") else target
        try:
            data = z.read(member)
        except KeyError:
            return None
        counter[0] += 1
        ext = os.path.splitext(member)[1].lower() or ".png"
        name = f"{base}-{counter[0]:02d}{ext}"
        os.makedirs(img_dir, exist_ok=True)
        with open(os.path.join(img_dir, name), "wb") as fh:
            fh.write(data)
        images[rid] = name
        return name

    def resolve_images(text):
        def repl(m):
            name = save_image(m.group(1))
            return f"\n![[img/{name}]]\n" if name else ""
        return re.sub("\x00IMG:([^\x00]+)\x00", repl, text)

    lines = []
    counters = {}
    for el in body:
        if el.tag == f"{W}tbl":
            lines.append(table_to_md(el))
            lines.append("")
            continue
        if el.tag != f"{W}p":
            continue
        ppr = el.find(f"{W}pPr")
        style_id = None
        num_id = ilvl = None
        if ppr is not None:
            ps = ppr.find(f"{W}pStyle")
            style_id = ps.get(f"{W}val") if ps is not None else None
            numpr = ppr.find(f"{W}numPr")
            if numpr is not None:
                ni = numpr.find(f"{W}numId")
                il = numpr.find(f"{W}ilvl")
                num_id = ni.get(f"{W}val") if ni is not None else None
                ilvl = il.get(f"{W}val") if il is not None else "0"
        text = resolve_images(paragraph_text(el)).strip()
        if not text:
            continue

        level = heading_level(styles.get(style_id, ""), style_id)
        if level:
            lines.append("")
            lines.append("#" * min(level, 6) + " " + re.sub(r"\*+", "", text))
            lines.append("")
            continue
        if num_id is not None and num_id != "0":
            fmt = numbering.get(num_id, {}).get(ilvl, "bullet")
            indent = "  " * int(ilvl or 0)
            if fmt == "bullet":
                lines.append(f"{indent}- {text}")
            else:
                key = (num_id, ilvl)
                counters[key] = counters.get(key, 0) + 1
                lines.append(f"{indent}{counters[key]}. {text}")
            continue
        # paragrafo normale: una riga vuota di separazione se prima c'era un elenco
        if lines and lines[-1].lstrip().startswith(("- ", "1", "2", "3", "4", "5", "6", "7", "8", "9")) and lines[-1] != "":
            lines.append("")
        lines.append(text)
        lines.append("")

    md = "\n".join(lines)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    out_path = os.path.join(out_dir, base + ".md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(out_path)
    if images:
        print(f"{len(images)} immagini salvate in {img_dir}")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
