#!/usr/bin/env python3
"""Converte una nota Obsidian del vault in una pagina HTML pronta da stampare in PDF.

Uso (serve il pacchetto markdown, installato nell'ambiente di sbobine-whisper):
  "$HOME/Library/Application Support/sbobine-whisper/.venv/bin/python" \
      .claude/scripts/md2html.py NOTA.md USCITA.html PERCORSO/tex-svg.js

Gestisce: proprieta' iniziali (tolte), callout > [!tipo] (anche richiudibili: nel PDF
restano aperti), wikilink (diventano testo), immagini ![[nome.svg|larghezza]] cercate
nel vault, formule $...$ e $$...$$ (scritte poi da MathJax). Il PDF si crea con
.claude/scripts/html2pdf.js.
"""
import html
import os
import re
import sys

import markdown

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
COLORI = {
    'note': '#4a7bd0', 'info': '#4a7bd0', 'abstract': '#1fa2a8', 'summary': '#1fa2a8',
    'tip': '#1fa26b', 'success': '#2e9e44', 'question': '#d08a1e', 'warning': '#d0711e',
    'danger': '#c9453b', 'example': '#7b57c9', 'quote': '#888888',
}
TITOLI = {'note': 'Nota', 'info': 'Info', 'abstract': 'Da ricordare', 'tip': 'Consiglio',
          'success': 'Soluzione', 'question': 'Domanda', 'warning': 'Attenzione',
          'danger': 'Pericolo', 'example': 'Esempio', 'quote': 'Citazione'}

_indice_file = None


def trova(nome):
    global _indice_file
    if _indice_file is None:
        _indice_file = {}
        for radice, cartelle, file in os.walk(VAULT):
            cartelle[:] = [c for c in cartelle if not c.startswith('.')]
            for f in file:
                _indice_file.setdefault(f, os.path.join(radice, f))
    return _indice_file.get(nome)


def proteggi_formule(testo, deposito):
    def metti(m):
        # dentro i callout le righe delle formule cominciano con "> ": il simbolo va tolto
        deposito.append(re.sub(r'(^|\n)[ \t]*>[ \t]?', r'\1', m.group(0)))
        return f'@@F{len(deposito) - 1}@@'
    testo = re.sub(r'\$\$.+?\$\$', metti, testo, flags=re.S)
    testo = re.sub(r'(?<![\\$])\$(?!\s)[^$\n]+?(?<!\s)\$', metti, testo)
    return testo


def wikilink(testo):
    def immagine(m):
        nome, _, larg = m.group(1).partition('|')
        p = trova(nome.strip())
        if not p:
            return f'[immagine mancante: {html.escape(nome)}]'
        stile = f' style="width:{int(larg)}px;max-width:100%"' if larg.strip().isdigit() else ''
        return f'<img class="fig" src="file://{p}"{stile}>'
    testo = re.sub(r'!\[\[([^\]]+)\]\]', immagine, testo)

    def link(m):
        dest, _, alias = m.group(1).partition('|')
        if alias:
            return alias
        dest = dest.split('#')[-1] if dest.startswith('#') else dest.split('#')[0]
        return re.sub(r'^\d+-', '', dest).replace('-', ' ')
    return re.sub(r'\[\[([^\]]+)\]\]', link, testo)


def righe_vuote_prima_degli_elenchi(testo):
    # in Obsidian un elenco puo' seguire subito un paragrafo; in Python-Markdown no
    out, prec = [], ''
    for riga in testo.split('\n'):
        elenco = re.match(r'\s*([-*+]|\d+\.)\s', riga)
        if elenco and prec.strip() and not re.match(r'\s*([-*+]|\d+\.)\s', prec) and not prec.startswith('|'):
            out.append('')
        if riga.startswith('|') and prec.strip() and not prec.startswith('|'):
            out.append('')
        out.append(riga)
        prec = riga
    return '\n'.join(out)


def callout(testo):
    righe = testo.split('\n')
    out, i = [], 0
    while i < len(righe):
        m = re.match(r'^>\s*\[!(\w+)\]([-+]?)\s*(.*)$', righe[i])
        if m:
            tipo, titolo = m.group(1).lower(), m.group(3).strip()
            corpo = []
            i += 1
            while i < len(righe) and righe[i].startswith('>'):
                corpo.append(re.sub(r'^> ?', '', righe[i]))
                i += 1
            colore = COLORI.get(tipo, '#4a7bd0')
            interno = rendi('\n'.join(corpo), formule=False).replace('\n', ' ')
            out.append(f'<div class="callout" style="border-color:{colore}">'
                       f'<div class="ctitolo" style="color:{colore}">{html.escape(titolo or TITOLI.get(tipo, tipo.capitalize()))}</div>'
                       f'<div class="ccorpo">{interno}</div></div>')
            continue
        out.append(righe[i])
        i += 1
    return '\n'.join(out)


def rendi(testo, formule=True):
    # le formule si proteggono una volta sola, sul testo intero (i callout sono annidati)
    deposito = []
    if formule:
        testo = proteggi_formule(testo, deposito)
    testo = callout(testo)
    testo = wikilink(testo)
    testo = righe_vuote_prima_degli_elenchi(testo)
    h = markdown.markdown(testo, extensions=['tables', 'sane_lists', 'fenced_code', 'md_in_html'])
    if not formule:
        return h
    return re.sub(r'@@F(\d+)@@', lambda m: html.escape(deposito[int(m.group(1))]), h)


CSS = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm; }
body { font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #222; }
h1 { font-size: 20pt; margin: 0 0 4pt; } .sotto { color: #777; font-size: 9pt; margin-bottom: 14pt; }
h2 { font-size: 14pt; margin: 18pt 0 6pt; border-bottom: 1px solid #ccc; padding-bottom: 2pt; page-break-after: avoid; }
h3 { font-size: 12pt; margin: 14pt 0 4pt; page-break-after: avoid; } h4 { font-size: 11pt; margin: 10pt 0 3pt; page-break-after: avoid; }
p { margin: 4pt 0 6pt; } ul, ol { margin: 3pt 0 6pt; padding-left: 20pt; } li { margin: 1pt 0; }
.callout { border-left: 4px solid; background: #f7f7f9; border-radius: 3px; padding: 5pt 9pt; margin: 8pt 0; page-break-inside: avoid; }
.ctitolo { font-weight: 600; margin-bottom: 2pt; } .ccorpo > :first-child { margin-top: 0; } .ccorpo > :last-child { margin-bottom: 0; }
table { border-collapse: collapse; margin: 6pt 0; font-size: 9.5pt; } th, td { border: 1px solid #ccc; padding: 3pt 6pt; } th { background: #f0f0f0; } tr { page-break-inside: avoid; }
img.fig { display: block; margin: 8pt auto; max-width: 100%; page-break-inside: avoid; }
code { background: #f0f0f0; padding: 0 3px; border-radius: 2px; font-size: 9pt; }
mjx-container[display="true"] { margin: 6pt 0 !important; } mjx-container { page-break-inside: avoid; }
"""


def main():
    nota, uscita, mathjax = sys.argv[1], sys.argv[2], sys.argv[3]
    testo = open(nota, encoding='utf-8').read()
    corso = re.search(r'^corso:\s*(.+)$', testo, re.M)
    testo = re.sub(r'\A---\n.*?\n---\n', '', testo, flags=re.S)
    corpo = rendi(testo)
    sotto = f'{corso.group(1).strip() if corso else ""} · Second brain di Nadia'
    corpo = re.sub(r'(</h1>)', r'\1<div class="sotto">' + html.escape(sotto) + '</div>', corpo, count=1)
    pagina = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style>
<script>window.MathJax = {{ tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']] }}, svg: {{ fontCache: 'global' }},
startup: {{ pageReady: () => MathJax.startup.defaultPageReady().then(() => {{ document.title = 'PRONTO'; }}) }} }};</script>
<script src="file://{mathjax}"></script></head><body>{corpo}</body></html>"""
    open(uscita, 'w', encoding='utf-8').write(pagina)


if __name__ == '__main__':
    main()
