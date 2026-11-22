"""Esercizio 4 (Muuratsalo): tante disposizioni semplici della casa (solo le stanze).

La casa e' fatta di "ali" appoggiate al recinto (nord ed est, perche' graticcio e apertura sud
devono restare sul patio). Ogni ala e' una fila di pezzi: stanze a tutta profondita', tratti con
il corridoio e le stanze accanto, oppure tratti doppi (stanze - corridoio - stanze). Lo spessore
di ogni ala si calcola in modo che le stanze tengano esattamente la superficie di Aalto.
Il programma prova molte combinazioni, scarta quelle che non rispettano le regole e ne tiene
un gruppo il piu' vario possibile.
Uso: python3 composizione-muuratsalo-disposizioni.py USCITA.html [quante]
"""
import itertools
import sys

LATO, R = 14.40, 0.40
A, B_ = R, LATO - R
L0 = B_ - A
AREA = {"SP": 9.35 * 4.35, "K": 4.25 * 3.05, "I": 4.25 * 1.25, "B": 3.25 * 1.50,
        "G": 3.25 * 1.95, "L2": 3.25 * 2.80, "L1": 4.25 * 3.05}
C_AREA = 1.00 * 6.25
NOME = {"SP": "Soggiorno e pranzo", "K": "Cucina", "I": "Ingresso", "C": "Corridoio", "B": "Bagno",
        "G": "Guardaroba", "L2": "Camera", "L1": "Camera grande"}
CORTO = dict(NOME, SP="Soggiorno", G="Guard.", L1="Camera gr.")
ZONA = {"SP": "giorno", "K": "giorno", "I": "distr", "C": "distr", "B": "servizi", "G": "notte",
        "L2": "notte", "L1": "notte"}
COL = {"giorno": "#f6d5cf", "notte": "#d3e0f3", "servizi": "#e3d5ef", "distr": "#fbecb3"}
PATIO_AALTO = L0 ** 2 - sum(AREA.values()) - C_AREA


# --- calcolo di un'ala ----------------------------------------------------------------------
def lunghezza(slots, T, wc):
    tot = 0
    for s in slots:
        if s[0] == "pieno":
            tot += AREA[s[1]] / T
        elif s[0] == "corr":
            tot += sum(AREA[k] for k in s[2]) / (T - wc)
        else:                                   # doppio
            tot += (sum(AREA[k] for k in s[1]) + sum(AREA[k] for k in s[2])) / (T - wc)
    return tot


def spessore(slots, L, wc):
    a, b = wc + 1.0, 12.0
    if lunghezza(slots, a, wc) < L:
        return None
    for _ in range(60):
        m = (a + b) / 2
        if lunghezza(slots, m, wc) > L:
            a = m
        else:
            b = m
    return (a + b) / 2


def posa(slots, T, wc, ala, inizio):
    """Rettangoli (x0, y0, x1, y1) delle stanze di un'ala.
    ala "N": lungo x da `inizio`, profondita' verso sud da y=A; "E": lungo y, profondita' verso ovest da x=B_."""
    out, corr = [], []
    t = inizio

    def rett(t0, t1, d0, d1):            # t lungo l'ala, d in profondita' dal recinto
        if ala == "N":
            return (t0, A + d0, t1, A + d1)
        return (B_ - d1, t0, B_ - d0, t1)
    for s in slots:
        if s[0] == "pieno":
            l = AREA[s[1]] / T
            out.append((s[1], rett(t, t + l, 0, T)))
            t += l
        elif s[0] == "corr":
            lato, ids = s[1], s[2]
            d = T - wc
            t0 = t
            for k in ids:
                l = AREA[k] / d
                out.append((k, rett(t, t + l, wc, T) if lato == "fuori" else rett(t, t + l, 0, d)))
                t += l
            corr.append(rett(t0, t, 0, wc) if lato == "fuori" else rett(t0, t, d, T))
        else:
            top, bot = s[1], s[2]
            st, sb = sum(AREA[k] for k in top), sum(AREA[k] for k in bot)
            l_tot = (st + sb) / (T - wc)
            a = st / l_tot
            t0, tt = t, t
            for k in top:
                l = AREA[k] / a
                out.append((k, rett(tt, tt + l, 0, a)))
                tt += l
            tt = t0
            for k in bot:
                l = AREA[k] / (T - wc - a)
                out.append((k, rett(tt, tt + l, a + wc, T)))
                tt += l
            corr.append(rett(t0, t0 + l_tot, a, a + wc))
            t += l_tot
    return out, corr


def costruisci(n_slots, e_slots, angolo):
    """angolo = "N": l'ala nord prende l'angolo nord-est; "E": lo prende l'ala est."""
    wc = 1.0                     # corridoio largo 1 m, come quello di Aalto
    for _ in range(1):
        if e_slots:
            if angolo == "N":
                TN = spessore(n_slots, L0, wc)
                if TN is None:
                    return None
                TE = spessore(e_slots, L0 - TN, wc)
            else:
                TE = spessore(e_slots, L0, wc)
                if TE is None:
                    return None
                TN = spessore(n_slots, L0 - TE, wc) if n_slots else 0
        else:
            TN, TE = spessore(n_slots, L0, wc), 0
        if TN is None or TE is None:
            return None
        stanze, corr = [], []
        if n_slots:
            s, c = posa(n_slots, TN, wc, "N", A)
            stanze += s
            corr += c
        if e_slots:
            s, c = posa(e_slots, TE, wc, "E", A + TN if angolo == "N" else A)
            stanze += s
            corr += c
        if not corr:
            return None
    for i, q in enumerate(corr):
        stanze.append(("C" if i == 0 else f"C{i+1}", q))
    return {k: q for k, q in stanze}, (TN, TE, wc)


# --- regole -----------------------------------------------------------------------------
def tocca(p, q, minimo=0.8):
    e = 1e-6
    if abs(p[2] - q[0]) < e or abs(q[2] - p[0]) < e:
        return min(p[3], q[3]) - max(p[1], q[1]) >= minimo
    if abs(p[3] - q[1]) < e or abs(q[3] - p[1]) < e:
        return min(p[2], q[2]) - max(p[0], q[0]) >= minimo
    return False


def valida(st):
    distr = [k for k in st if k == "I" or k.startswith("C")]
    # il distributivo e' un pezzo solo
    vis, coda = {"I"}, ["I"]
    while coda:
        n = coda.pop()
        for k in distr:
            if k not in vis and tocca(st[n], st[k], 0.85):
                vis.add(k)
                coda.append(k)
    if len(vis) != len(distr):
        return False
    serve = lambda k: any(tocca(st[k], st[d]) for d in distr)
    if not all(serve(k) for k in ("B", "G", "L2", "L1", "SP")):
        return False
    if not tocca(st["K"], st["SP"], 1.0):
        return False
    # l'ingresso tocca il recinto (ci si entra da fuori)
    q = st["I"]
    lato = max((q[2] - q[0]) if abs(q[1] - A) < 1e-6 or abs(q[3] - B_) < 1e-6 else 0,
               (q[3] - q[1]) if abs(q[0] - A) < 1e-6 or abs(q[2] - B_) < 1e-6 else 0)
    if lato < 1.0:
        return False
    # proporzioni ragionevoli
    lim = {"SP": (3.6, 3.4), "K": (2.2, 2.6), "L1": (2.6, 2.0), "L2": (2.4, 2.0), "G": (1.3, 3.6),
           "B": (1.3, 3.2), "I": (1.1, 6.0)}
    for k, (mn, asp) in lim.items():
        q = st[k]
        a, b = sorted((q[2] - q[0], q[3] - q[1]))
        if a < mn - 1e-6 or b / a > asp + 1e-6:
            return False
    # graticcio (ovest, y 7,70-12,60) e apertura sud (x 2,45-6,95) restano sul patio
    for q in st.values():
        if q[0] < A + 0.5 and q[3] > 7.80 and q[1] < 12.60:   # il primo montante e' a 7,85
            return False
        if q[3] > B_ - 0.5 and q[0] < 6.95 and q[2] > 2.45:
            return False
    # il patio: superficie e un solo pezzo (non deve restare chiuso tra le stanze)
    patio = L0 ** 2 - sum((q[2] - q[0]) * (q[3] - q[1]) for q in st.values())
    return abs(patio / PATIO_AALTO - 1) <= 0.05


# --- le combinazioni ----------------------------------------------------------------------
def notte_corr(ordine, lato, l1_fuori):
    ids = [k for k in ordine if not (l1_fuori and k == "L1")]
    s = [("corr", lato, ids)]
    return s + ([("pieno", "L1")] if l1_fuori else [])


def candidati():
    notti = list(itertools.permutations(["B", "G", "L2", "L1"]))
    out = []
    # 1) L: giorno a nord, notte a est (e viceversa), ingresso all'incrocio
    for giorno_n in (True, False):
        for ord_g in (["K", "SP"], ["SP", "K"]):
            for ordine in notti:
                for lato in ("fuori", "patio"):
                    for l1f in (False, True):
                        notte = notte_corr(ordine, lato, l1f)
                        for pos_i in ("giorno", "notte"):
                            for angolo in ("N", "E"):
                                g = [("pieno", k) for k in ord_g]
                                if giorno_n:
                                    n = g + ([("pieno", "I")] if pos_i == "giorno" else [])
                                    e = ([("pieno", "I")] if pos_i == "notte" else []) + notte
                                    titolo = "Giorno a nord, notte a est"
                                else:
                                    # la notte a nord si legge da ovest verso l'angolo
                                    n = list(reversed(notte)) + ([("pieno", "I")] if pos_i == "notte" else [])
                                    n = [(s[0], s[1], list(reversed(s[2]))) if s[0] == "corr" else s for s in n]
                                    e = ([("pieno", "I")] if pos_i == "giorno" else []) + \
                                        [("pieno", k) for k in reversed(ord_g)]
                                    titolo = "Notte a nord, giorno a est"
                                out.append((titolo, n, e, angolo,
                                            f"corridoio {'sul recinto' if lato == 'fuori' else 'sul patio'}"))
    # 2) barra a nord: soggiorno a un'estremita', il resto a corridoio centrale
    resto = ["K", "B", "I", "G", "L2", "L1"]
    for sp_ovest in (True, False):
        for k in (2, 3, 4):
            for sopra in itertools.combinations(resto, k):
                sotto = [x for x in resto if x not in sopra]
                for top in itertools.permutations(sopra):
                    for bot in itertools.permutations(sotto):
                        d = ("doppio", list(top), list(bot))
                        n = [("pieno", "SP"), d] if sp_ovest else [d, ("pieno", "SP")]
                        camere_sud = sum(x in sotto for x in ("G", "L2", "L1"))
                        nota = (f"soggiorno a {'ovest' if sp_ovest else 'est'}, "
                                f"{'camere sul patio' if camere_sud >= 2 else 'camere verso nord'}")
                        out.append(("Barra a nord, patio a sud", n, [], "N", nota))
    # 3) L con la zona notte a corridoio centrale (doppio) nell'ala est o nord
    for giorno_n in (True, False):
        for ord_g in (["K", "SP"], ["SP", "K"]):
            for a in itertools.permutations(["B", "G"]):
                for b in itertools.permutations(["L2", "L1"]):
                    for angolo in ("N", "E"):
                        g = [("pieno", k) for k in ord_g]
                        d = ("doppio", list(a), list(b))
                        if giorno_n:
                            out.append(("Giorno a nord, notte a est", g + [("pieno", "I")], [d], angolo,
                                        "camere ai due lati del corridoio"))
                        else:
                            out.append(("Notte a nord, giorno a est", [d, ("pieno", "I")],
                                        [("pieno", k) for k in reversed(ord_g)], angolo,
                                        "camere ai due lati del corridoio"))
    return out


def scegli(quante):
    validi = []
    for titolo, n, e, angolo, nota in candidati():
        r = costruisci(n, e, angolo)
        if r is None:
            continue
        st, par = r
        if valida(st):
            validi.append((titolo, nota, st, par))
    # varieta': si sceglie ogni volta la disposizione piu' diversa da quelle gia' prese
    def firma(st):
        return {k: ((q[0] + q[2]) / 2, (q[1] + q[3]) / 2) for k, q in st.items() if not k.startswith("C")}

    def distanza(a, b):
        fa, fb = firma(a), firma(b)
        return sum(AREA[k] ** 0.5 * (abs(fa[k][0] - fb[k][0]) + abs(fa[k][1] - fb[k][1])) for k in fa)
    gruppo = lambda v: (v[0], v[1].split(",")[0])
    conta = {}
    scelti = [validi[0]]
    conta[gruppo(validi[0])] = 1
    while len(scelti) < min(quante, len(validi)):
        resto_v = [v for v in validi if v not in scelti and conta.get(gruppo(v), 0) < 6]
        if not resto_v:
            break
        v = max(resto_v, key=lambda v: min(distanza(v[2], s[2]) for s in scelti))
        scelti.append(v)
        conta[gruppo(v)] = conta.get(gruppo(v), 0) + 1
    ordine = {"Giorno a nord, notte a est": 0, "Notte a nord, giorno a est": 1, "Barra a nord, patio a sud": 2}
    scelti.sort(key=lambda v: (ordine[v[0]], v[1]))
    return scelti, len(validi)


# --- disegno ------------------------------------------------------------------------------
def num(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",")


def svg(st, s=19):
    x0, y0 = -0.3, -0.3
    W = H = (LATO + 0.6) * s
    X = lambda x: (x - x0) * s
    Y = lambda y: (y - y0) * s
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="100%" '
         f'font-family="Helvetica, Arial, sans-serif">',
         f'<rect x="{X(A)}" y="{Y(A)}" width="{L0*s}" height="{L0*s}" fill="#e9f2e1"/>']
    for k, q in st.items():
        z = "distr" if k.startswith("C") else ZONA[k]
        o.append(f'<rect x="{X(q[0])}" y="{Y(q[1])}" width="{(q[2]-q[0])*s}" height="{(q[3]-q[1])*s}" '
                 f'fill="{COL[z]}" stroke="#333" stroke-width="1.3"/>')
    o.append(f'<path d="M{X(0)} {Y(0)}H{X(LATO)}V{Y(LATO)}H{X(0)}Z M{X(A)} {Y(A)}V{Y(B_)}H{X(B_)}V{Y(A)}Z" '
             f'fill="#555" fill-rule="evenodd"/>')
    o.append(f'<rect x="{X(0)}" y="{Y(7.70)}" width="{R*s}" height="{4.9*s}" fill="#fff" stroke="#555"/>')
    o.append(f'<rect x="{X(2.45)}" y="{Y(B_)-0.5}" width="{4.5*s}" height="{R*s+1}" fill="#e9f2e1"/>')
    for k, q in st.items():
        w, h = q[2] - q[0], q[3] - q[1]
        cx, cy = X((q[0] + q[2]) / 2), Y((q[1] + q[3]) / 2)
        base = "C" if k.startswith("C") else k
        vert = h > w and w < 2.4
        lungo, corto = (h, w) if vert else (w, h)
        rot = f' transform="rotate(-90 {cx} {cy})"' if vert else ""
        nome = CORTO[base]
        dim = f"{num(w)} × {num(h)}"
        if corto < 1.5:
            riga = f"{nome} {dim}"
            fs = min(8.5, (lungo * s - 4) / (len(riga) * 0.52))
            o.append(f'<text x="{cx}" y="{cy + 3}" font-size="{fs:.1f}" text-anchor="middle"{rot}>'
                     f'<tspan font-weight="bold">{nome}</tspan> {dim}</text>')
        else:
            fs = min(9, (lungo * s - 4) / (max(len(nome), len(dim)) * 0.55))
            o.append(f'<text x="{cx}" y="{cy - 1}" font-size="{fs:.1f}" font-weight="bold" text-anchor="middle"'
                     f'{rot}>{nome}<tspan x="{cx}" dy="{fs+1:.1f}" font-weight="normal">{dim}</tspan></text>')
    patio = L0 ** 2 - sum((q[2] - q[0]) * (q[3] - q[1]) for q in st.values())
    o.append(f'<text x="{X(4.0)}" y="{Y(11.0)}" font-size="11" font-weight="bold" text-anchor="middle" '
             f'fill="#4c7a34">PATIO<tspan x="{X(4.0)}" dy="13" font-size="9" font-weight="normal">'
             f'{num(patio,1)} m²</tspan></text></svg>')
    return "".join(o)


CSS = """
@page { size: A4; margin: 11mm 12mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; color: #222; margin: 0; }
h1 { font-size: 16pt; margin: 0 0 3pt; } p { margin: 2pt 0 6pt; }
.griglia { display: grid; grid-template-columns: 1fr 1fr; gap: 6pt 14pt; }
.nuova { page-break-before: always; }
.card { page-break-inside: avoid; height: 84mm; } .card svg { width: 70mm; display: block; margin: 0 auto; }
.card h3 { height: 9mm; line-height: 1.2; } .card h3 { font-size: 10pt; margin: 4pt 0 2pt; }
.card h3 span { font-weight: normal; color: #666; }
.leg span { display: inline-block; width: 10pt; height: 8pt; border: 1px solid #333; vertical-align: -1pt; margin: 0 3pt 0 8pt; }
"""


def html(quante):
    scelti, tot = scegli(quante)
    r = ["<h1>Esercizio 4 · Disposizioni della casa</h1>",
         f"<p>{len(scelti)} piante, scelte tra {tot} combinazioni che rispettano le regole: recinto "
         "intatto, graticcio e apertura sud sul patio, ogni stanza con la superficie di Aalto, patio "
         "di circa 86,5 m², camere e bagno sul corridoio, soggiorno sul distributivo, cucina accanto "
         "al pranzo. Misure in metri, dentro le stanze; senza annesso, porte e finestre.</p>",
         '<p class="leg"><span style="background:#f6d5cf"></span>zona giorno<span style="background:#d3e0f3">'
         '</span>zona notte<span style="background:#e3d5ef"></span>bagno<span style="background:#fbecb3">'
         '</span>ingresso e corridoio<span style="background:#e9f2e1"></span>patio</p>']
    per_pagina = [4] + [6] * 10
    i, pag = 0, 0
    while i < len(scelti):
        n = per_pagina[pag]
        r.append(f'<div class="griglia{" nuova" if pag else ""}">')
        for titolo, nota, st, par in scelti[i:i + n]:
            i += 1
            r.append(f'<div class="card"><h3>{i}. {titolo}<br><span>{nota}</span></h3>{svg(st)}</div>')
        r.append("</div>")
        pag += 1
    return (f"<!doctype html><html lang='it'><head><meta charset='utf-8'><title>caricamento</title>"
            f"<style>{CSS}</style></head><body>{''.join(r)}"
            f"<script>window.onload=function(){{document.title='PRONTO'}}</script></body></html>")


if __name__ == "__main__":
    quante = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    if len(sys.argv) > 1:
        open(sys.argv[1], "w", encoding="utf-8").write(html(quante))
    else:
        scelti, tot = scegli(quante)
        print("valide:", tot)
        for t, n, st, par in scelti:
            print(t, "|", n, "| spessori", [round(v, 2) for v in par])
