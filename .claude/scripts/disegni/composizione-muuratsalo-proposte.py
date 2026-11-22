"""Esercizio 4 (Muuratsalo): proposte di nuova disposizione con l'ingresso principale nell'angolo.

Ogni proposta viene controllata (superfici, patio, recinto, percorsi) e disegnata in SVG;
poi tutto finisce in una pagina HTML da stampare in PDF con .claude/scripts/html2pdf.js.
Uso: python3 composizione-muuratsalo-proposte.py USCITA.html
"""
import sys
from collections import deque

# Coordinate in metri: x verso est, y verso sud, origine nell'angolo nord-ovest del quadrato
# di 14,40. Il recinto e' spesso 0,40, quindi l'interno va da 0,40 a 14,00.
LATO, R = 14.40, 0.40
A, B_ = R, LATO - R

# superfici di Aalto (dalla pagina interattiva della nuova disposizione)
AALTO = {"SP": 9.35 * 4.35, "K": 4.25 * 3.05, "I": 4.25 * 1.25, "C": 1.00 * 6.25,
         "B": 3.25 * 1.50, "G": 3.25 * 1.95, "L2": 3.25 * 2.80, "L1": 4.25 * 3.05}
NOMI = {"SP": "Soggiorno, pranzo e atelier", "K": "Cucina", "I": "Ingresso (disimpegno)",
        "C": "Corridoio", "B": "Bagno", "G": "Guardaroba", "L2": "Camera", "L1": "Camera grande"}
CORTI = {"SP": "Soggiorno e pranzo", "K": "Cucina", "I": "Ingresso", "C": "Corridoio",
         "B": "Bagno", "G": "Guard.", "L2": "Camera", "L1": "Camera grande"}
ZONA = {"SP": "giorno", "K": "giorno", "I": "distr", "C": "distr", "B": "servizi", "G": "notte",
        "L2": "notte", "L1": "notte"}
COL = {"giorno": "#f6d5cf", "notte": "#d3e0f3", "servizi": "#e3d5ef", "distr": "#fbecb3"}
PATIO_AALTO = (B_ - A) ** 2 - sum(AALTO.values())

# aperture del recinto che devono restare sul patio
GRATICCIO = (A, 7.70, A + 0.6, 12.60)          # lato ovest
APERTURA = (2.45, B_ - 0.6, 6.95, B_)           # lato sud


def r(x0, y0, x1, y1):
    return (round(x0, 3), round(y0, 3), round(x1, 3), round(y1, 3))


# --- le proposte -------------------------------------------------------------------------
# stanze: id -> (x0, y0, x1, y1); porte: (stanza, stanza o "fuori", "v"/"h", coordinata, da, a)
# "v" = porta su un muro verticale (x fissa), "h" = su un muro orizzontale (y fissa).

def proposta_1():
    st = {"K": r(0.40, 0.40, 3.40, 4.75), "SP": r(3.40, 0.40, 12.75, 4.75),
          "I": r(12.75, 0.40, 14.00, 4.75), "C": r(13.00, 4.75, 14.00, 10.95),
          "B": r(9.75, 4.75, 13.00, 6.25), "G": r(9.75, 6.25, 13.00, 8.20),
          "L2": r(9.75, 8.20, 13.00, 10.95), "L1": r(9.75, 10.95, 14.00, 14.00)}
    porte = [("I", "fuori", "v", 14.00, 0.80, 1.80), ("I", "SP", "v", 12.75, 2.90, 3.80),
             ("SP", "K", "v", 3.40, 2.60, 3.50), ("I", "C", "h", 4.75, 13.05, 13.95),
             ("C", "B", "v", 13.00, 5.10, 5.80), ("C", "G", "v", 13.00, 7.00, 7.70),
             ("C", "L2", "v", 13.00, 9.90, 10.70), ("C", "L1", "h", 10.95, 13.05, 13.95),
             ("SP", "patio", "h", 4.75, 6.00, 6.90)]
    sopp = r(0.40, 0.40, 3.70, 4.75)
    return dict(
        titolo="La L di Aalto, con l'ingresso nell'angolo nord-est",
        idea="Tieni la forma a L della casa vera (zona giorno a nord, zona notte a est) e "
             "porti l'ingresso proprio nell'angolo. Per farlo l'ingresso diventa una stanza "
             "lunga e stretta nell'angolo, la cucina va in fondo a ovest e il corridoio corre "
             "lungo il muro est.",
        percorso="Dall'ingresso in legno si entra nel disimpegno dell'angolo. Da lì, a "
                 "sinistra, si va nel soggiorno (e attraverso il soggiorno nel pranzo e in "
                 "cucina); dritto davanti si scende nel corridoio, che porta al bagno, al "
                 "guardaroba e alle due camere senza passare dalla zona giorno.",
        pro=["Il patio resta identico a quello di Aalto (stessa forma, stessa superficie).",
             "L'ingresso in legno e l'annesso restano dove sono: non devi ridisegnarli.",
             "Il bagno è subito dopo l'ingresso, quindi vicino a tutti."],
        contro=["La cucina finisce in fondo alla casa: con la spesa attraversi il soggiorno.",
                "Le camere hanno le finestre solo sul patio, perché il corridoio occupa il "
                "lato est."],
        tetto="Il tetto può restare come quello di Aalto, alto a ovest. Il soppalco (lo "
              "studio, 3,30 × 4,35) va sopra la cucina, dove il tetto è più alto, e si "
              "affaccia sul pranzo e sul soggiorno. Sotto il soppalco la cucina è alta 2,35, "
              "come oggi la parte sotto lo studio.",
        stanze=st, porte=porte, sopp=sopp, appendice="est")


def proposta_2():
    st = {"I": r(9.65, 0.40, 14.00, 1.62), "SP": r(9.65, 1.62, 14.00, 10.97),
          "K": r(9.65, 10.97, 14.00, 14.00), "C": r(3.45, 0.40, 9.65, 1.40),
          "B": r(8.15, 1.40, 9.65, 4.65), "G": r(6.20, 1.40, 8.15, 4.65),
          "L2": r(3.45, 1.40, 6.20, 4.65), "L1": r(0.40, 0.40, 3.45, 4.65)}
    porte = [("I", "fuori", "v", 14.00, 0.55, 1.45), ("I", "SP", "h", 1.62, 12.10, 13.00),
             ("I", "C", "v", 9.65, 0.45, 1.35), ("SP", "K", "h", 10.97, 10.20, 11.10),
             ("C", "B", "h", 1.40, 8.40, 9.10), ("C", "G", "h", 1.40, 6.70, 7.40),
             ("C", "L2", "h", 1.40, 4.60, 5.40), ("C", "L1", "v", 3.45, 0.45, 1.35),
             ("SP", "patio", "v", 9.65, 6.00, 6.90)]
    sopp = r(9.65, 1.62, 14.00, 4.92)
    return dict(
        titolo="Zona giorno a est, zona notte a nord",
        idea="Giri le due ali della L: il soggiorno con il pranzo e la cucina diventano l'ala "
             "est, le camere l'ala nord. Nell'angolo nord-est, dove le due ali si incontrano, "
             "c'è l'ingresso, che distribuisce a destra e a sinistra.",
        percorso="Si entra nell'angolo. Girando a destra (verso sud) si va nel soggiorno, che "
                 "continua nel pranzo e finisce nella cucina; girando a sinistra (verso ovest) "
                 "si va nel corridoio della zona notte. Il bagno è la prima porta del "
                 "corridoio, quindi un ospite ci arriva senza passare davanti alle camere.",
        pro=["L'ingresso è il punto in cui si dividono zona giorno e zona notte: è proprio "
             "il ragionamento del prof (ingresso sul distributivo, notte separata).",
             "Il patio è un rettangolo quasi quadrato (9,25 × 9,35) che resta davanti al "
             "graticcio e alla grande apertura sud.",
             "La cucina e il pranzo guardano verso sud e verso il lago.",
             "Le camere sono le stesse di Aalto, solo ruotate: le misure non cambiano."],
        contro=["La cucina è lontana dall'ingresso (sta in fondo all'ala est).",
                "Il tetto va ripensato, perché il soppalco ora è nell'ala est."],
        tetto="Lo studio sul soppalco (4,35 × 3,30) sta in cima al soggiorno, vicino "
              "all'ingresso, e guarda il soggiorno. Il tetto deve essere alto lì: una falda "
              "che sale verso nord, alta sopra il soppalco e più bassa verso la cucina. "
              "Le camere hanno un tetto basso, come oggi.",
        stanze=st, porte=porte, sopp=sopp, appendice="est")


def barra(specchiata):
    # barra lungo il lato nord, profonda 7,24: il patio e' il rettangolo a sud, 13,60 x 6,36
    yN, yC, yS = 0.40, 3.08, 4.08          # fascia nord 2,68 / corridoio 1,00 / fascia sud 3,56
    yF = 7.64
    st = {"SP": (0.40, yN, 6.02, yF),
          "K": (6.02, yN, 10.86, yC), "B": (10.86, yN, 12.68, yC), "I": (12.68, yN, 14.00, yC),
          "C": (6.02, yC, 14.00, yS),
          "L1": (6.02, yS, 9.66, yF), "G": (9.66, yS, 11.44, yF), "L2": (11.44, yS, 14.00, yF)}
    porte = [("I", "fuori", "v", 14.00, 1.20, 2.10), ("I", "C", "h", yC, 12.90, 13.80),
             ("C", "SP", "v", 6.02, yC + 0.05, yS - 0.05), ("SP", "K", "v", 6.02, 1.40, 2.30),
             ("C", "B", "h", yC, 11.30, 12.00), ("C", "K", "h", yC, 9.60, 10.40),
             ("C", "L1", "h", yS, 8.40, 9.20), ("C", "G", "h", yS, 10.20, 10.90),
             ("C", "L2", "h", yS, 12.40, 13.20), ("SP", "patio", "h", yF, 3.00, 3.90)]
    sopp = (0.40, 0.40, 3.70, 4.75)
    if specchiata:
        m = lambda x: round(LATO - x, 3)
        st = {k: (m(x1), y0, m(x0), y1) for k, (x0, y0, x1, y1) in st.items()}
        porte = [(a, b, o, m(c) if o == "v" else c, *((m(t), m(f)) if o == "h" else (f, t)))
                 for a, b, o, c, f, t in porte]
        sopp = (m(sopp[2]), sopp[1], m(sopp[0]), sopp[3])
    return st, porte, sopp


def proposta_3():
    st, porte, sopp = barra(False)
    return dict(
        titolo="Una barra a nord e il patio tutto a sud",
        idea="Tutta la casa sta in una fascia lungo il lato nord e il patio diventa il "
             "rettangolo a sud, largo quanto la casa. A ovest c'è il soggiorno, alto e "
             "profondo; a est la zona notte, tagliata da un corridoio: a nord i servizi "
             "(cucina e bagno), a sud, sul patio, le camere.",
        percorso="Si entra nell'angolo nord-est. Subito dopo l'ingresso c'è il corridoio, che "
                 "va dritto verso ovest fino al soggiorno: lungo la strada, a destra, il bagno "
                 "e la cucina; a sinistra le camere e il guardaroba. La cucina ha una porta sul "
                 "corridoio e una direttamente sul pranzo.",
        pro=["Il patio è un unico rettangolo pieno di sole, con il graticcio e la grande "
             "apertura sud tutti e due sul patio.",
             "Le camere guardano il patio a sud; cucina e bagno, che servono meno luce, "
             "stanno sul lato nord, come nella casa vera.",
             "Il tetto e il soppalco possono restare come quelli di Aalto.",
             "Bagno subito dopo l'ingresso, a metà tra camere e soggiorno."],
        contro=["Per andare in soggiorno si passa davanti alle porte delle camere (il corridoio "
                "è in comune): è la cosa da difendere davanti al prof.",
                "Ingresso e corridoio hanno la stessa superficie di Aalto (11,6 m² in tutto), "
                "ma divisa in modo diverso: ingresso più piccolo, corridoio più lungo."],
        tetto="Il soggiorno sta a ovest, sotto la parte più alta del tetto di Aalto, e il "
              "soppalco resta nell'angolo nord-ovest, 3,30 × 4,35, proprio come oggi. Il tetto "
              "può restare la stessa falda che scende verso est.",
        stanze=st, porte=porte, sopp=sopp, appendice="est")


def proposta_4():
    st, porte, sopp = barra(True)
    return dict(
        titolo="La barra a nord specchiata, con l'ingresso nell'angolo nord-ovest",
        idea="È la proposta 3 rovesciata: il soggiorno va a est e la zona notte a ovest, "
             "così l'ingresso finisce nell'angolo nord-ovest. L'ingresso in legno e l'annesso "
             "si spostano a ovest, sempre fuori dal quadrato.",
        percorso="Si entra nell'angolo nord-ovest e si segue il corridoio verso est fino al "
                 "soggiorno. A sinistra bagno e cucina, a destra le camere e il guardaroba.",
        pro=["Stessi pregi della proposta 3: patio unico a sud, camere sul patio, servizi a "
             "nord.",
             "Il soggiorno sta a est e prende il sole del mattino; la cucina è attaccata al "
             "soggiorno e al corridoio."],
        contro=["Bisogna spostare l'ingresso in legno e l'annesso dall'altra parte (a ovest): "
                "nel disegno e nel plastico vanno rifatti.",
                "Il tetto va specchiato: alto a est, sopra il soppalco.",
                "Anche qui il corridoio verso il soggiorno passa davanti alle camere."],
        tetto="Il soppalco va nell'angolo nord-est, 3,30 × 4,35, e il tetto diventa la falda "
              "di Aalto specchiata: alta a est e bassa verso ovest.",
        stanze=st, porte=porte, sopp=sopp, appendice="ovest")


PROPOSTE = [proposta_1(), proposta_2(), proposta_3(), proposta_4()]


# --- controlli ---------------------------------------------------------------------------
def area(q):
    return (q[2] - q[0]) * (q[3] - q[1])


def sovrapp(p, q):
    return max(0, min(p[2], q[2]) - max(p[0], q[0])) * max(0, min(p[3], q[3]) - max(p[1], q[1]))


def sul_lato(q, o, c, f, t):
    """La porta (o, c, f, t) sta su un lato della stanza q?"""
    e = 1e-6
    if o == "v":
        return (abs(q[0] - c) < e or abs(q[2] - c) < e) and q[1] - e <= f and t <= q[3] + e
    return (abs(q[1] - c) < e or abs(q[3] - c) < e) and q[0] - e <= f and t <= q[2] + e


def controlla(p):
    st, errori = p["stanze"], []
    for k, q in st.items():
        if q[0] < A - 1e-6 or q[1] < A - 1e-6 or q[2] > B_ + 1e-6 or q[3] > B_ + 1e-6:
            errori.append(f"{k} esce dal recinto")
        d = area(q) / AALTO[k] - 1
        if abs(d) > 0.05 and k not in ("I", "C"):
            errori.append(f"{k}: superficie {area(q):.2f} invece di {AALTO[k]:.2f}")
        for zona, nome in ((GRATICCIO, "graticcio"), (APERTURA, "apertura sud")):
            if sovrapp(q, zona) > 1e-6:
                errori.append(f"{k} copre il {nome}")
    ks = list(st)
    for i, a in enumerate(ks):
        for b in ks[i + 1:]:
            if sovrapp(st[a], st[b]) > 1e-6:
                errori.append(f"{a} e {b} si sovrappongono")
    distr = area(st["I"]) + area(st["C"])
    if abs(distr / (AALTO["I"] + AALTO["C"]) - 1) > 0.05:
        errori.append(f"ingresso + corridoio = {distr:.2f}")
    patio = (B_ - A) ** 2 - sum(area(q) for q in st.values())
    if abs(patio / PATIO_AALTO - 1) > 0.05:
        errori.append(f"patio {patio:.2f} invece di {PATIO_AALTO:.2f}")
    # l'ingresso deve toccare l'angolo del quadrato
    qi = st["I"]
    angoli = [(A, A), (B_, A), (A, B_), (B_, B_)]
    if not any(abs(qi[0 if x == A else 2] - x) < 1e-6 and abs(qi[1 if y == A else 3] - y) < 1e-6
               for x, y in angoli):
        errori.append("l'ingresso non è nell'angolo")
    # porte sui muri giusti e percorsi
    g = {k: set() for k in st}
    for a, b, o, c, f, t in p["porte"]:
        if not sul_lato(st[a], o, c, f, t):
            errori.append(f"porta {a}-{b} non sta su un muro di {a}")
        if b in st:
            if not sul_lato(st[b], o, c, f, t):
                errori.append(f"porta {a}-{b} non sta su un muro di {b}")
            g[a].add(b)
            g[b].add(a)
    # dall'ingresso si arriva a ogni stanza; a camere e bagno solo attraverso il distributivo
    for dest in st:
        passa = {"I", "C", dest}
        if ZONA[dest] in ("notte", "servizi"):
            vis, coda = {"I"}, deque(["I"])
            while coda:
                n = coda.popleft()
                for m in g[n]:
                    if m in passa and m not in vis:
                        vis.add(m)
                        coda.append(m)
            if dest not in vis:
                errori.append(f"{dest} non si raggiunge dal corridoio")
    vis, coda = {"I"}, deque(["I"])
    while coda:
        n = coda.popleft()
        for m in g[n]:
            if m not in vis and ZONA.get(m) != "notte":
                vis.add(m)
                coda.append(m)
    for dest in ("SP", "K"):
        if dest not in vis:
            errori.append(f"{dest} si raggiunge solo passando da una camera")
    if not g["SP"] & {"I", "C"}:
        errori.append("il soggiorno non è sul distributivo")
    if "K" not in g["SP"]:
        errori.append("la cucina non comunica con il pranzo")
    return errori, patio


# --- disegno -----------------------------------------------------------------------------
def num(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",")


def appendice(lato):
    """Ingresso in legno (E) e annesso degli ospiti, fuori dal quadrato, come nella casa vera."""
    E, An = (14.40, -1.30, 16.10, 4.70), (16.10, -3.50, 23.40, 0.15)
    if lato == "ovest":
        m = lambda x: LATO - x
        E = (m(E[2]), E[1], m(E[0]), E[3])
        An = (m(An[2]), An[1], m(An[0]), An[3])
    return E, An


def svg_pianta(p, s=30):
    st = p["stanze"]
    E, An = appendice(p["appendice"])
    x0, y0 = min(0, E[0], An[0]) - 0.8, min(0, An[1]) - 0.9
    x1, y1 = max(LATO, E[2], An[2]) + 0.8, LATO + 1.6
    W, H = (x1 - x0) * s, (y1 - y0) * s
    X = lambda x: (x - x0) * s
    Y = lambda y: (y - y0) * s
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
         f'width="100%" font-family="Helvetica, Arial, sans-serif">']
    # patio
    o.append(f'<rect x="{X(A)}" y="{Y(A)}" width="{(B_-A)*s}" height="{(B_-A)*s}" fill="#e9f2e1"/>')
    # appendice
    for q, nome, sotto in ((E, "Ingresso in legno", ""),
                           (An, "Annesso degli ospiti", "(si può anche togliere)")):
        o.append(f'<rect x="{X(q[0])}" y="{Y(q[1])}" width="{(q[2]-q[0])*s}" '
                 f'height="{(q[3]-q[1])*s}" fill="#f1ece4" stroke="#8a7a66" stroke-width="2"/>')
        cx, cy = X((q[0] + q[2]) / 2), Y((q[1] + q[3]) / 2)
        if q is E:
            cy = Y((3.0 + q[3]) / 2)
        rot = f' transform="rotate(-90 {cx} {cy})"' if q[3] - q[1] > q[2] - q[0] else ""
        o.append(f'<text x="{cx}" y="{cy - 2}" font-size="11" text-anchor="middle" fill="#5d5143"'
                 f'{rot}>{nome}<tspan x="{cx}" dy="13" font-size="9.5">{sotto}</tspan></text>')
    # stanze
    for k, q in st.items():
        o.append(f'<rect x="{X(q[0])}" y="{Y(q[1])}" width="{(q[2]-q[0])*s}" '
                 f'height="{(q[3]-q[1])*s}" fill="{COL[ZONA[k]]}" stroke="#333" stroke-width="1.6"/>')
    # soppalco
    q = p["sopp"]
    o.append(f'<rect x="{X(q[0])+3}" y="{Y(q[1])+3}" width="{(q[2]-q[0])*s-6}" '
             f'height="{(q[3]-q[1])*s-6}" fill="none" stroke="#b0412f" stroke-width="1.4" '
             f'stroke-dasharray="6 4"/>')
    o.append(f'<text x="{X(q[0])+7}" y="{Y(q[1])+16}" font-size="9.5" fill="#b0412f">soppalco (studio)</text>')
    # recinto: anello spesso 0,40 con il graticcio e l'apertura sud
    o.append(f'<path d="M{X(0)} {Y(0)}H{X(LATO)}V{Y(LATO)}H{X(0)}Z M{X(A)} {Y(A)}V{Y(B_)}H{X(B_)}V{Y(A)}Z" '
             f'fill="#555" fill-rule="evenodd"/>')
    gy0, gy1 = 7.70, 12.60
    o.append(f'<rect x="{X(0)}" y="{Y(gy0)}" width="{R*s}" height="{(gy1-gy0)*s}" fill="#fff" '
             f'stroke="#555" stroke-width="1"/>')
    for i in range(9):
        yy = gy0 + 0.15 + i * 0.58
        o.append(f'<line x1="{X(0)}" y1="{Y(yy)}" x2="{X(R)}" y2="{Y(yy)}" stroke="#555" stroke-width="1.5"/>')
    o.append(f'<rect x="{X(2.45)}" y="{Y(B_)-0.5}" width="{4.5*s}" height="{R*s+1}" fill="#e9f2e1"/>')
    o.append(f'<text x="{X(4.7)}" y="{Y(LATO)+14}" font-size="10" text-anchor="middle" fill="#444">'
             f'apertura del recinto (resta)</text>')
    o.append(f'<text x="{X(-0.25)}" y="{Y(10.15)}" font-size="10" text-anchor="middle" fill="#444" '
             f'transform="rotate(-90 {X(-0.25)} {Y(10.15)})">graticcio (resta)</text>')
    # porte
    for a, b, ori, c, f, t in p["porte"]:
        lw = (t - f) * s
        esterna = b == "fuori"
        sp = (R if esterna else 0.12) * s
        if ori == "v":
            xx = X(c) - (sp / 2 if not esterna else (sp if c < LATO / 2 else 0))
            o.append(f'<rect x="{xx}" y="{Y(f)}" width="{sp}" height="{lw}" fill="#fff"/>')
        else:
            yy = Y(c) - sp / 2
            o.append(f'<rect x="{X(f)}" y="{yy}" width="{lw}" height="{sp}" fill="#fff"/>')
        col = "#c0392b" if esterna else "#333"
        if ori == "v":
            o.append(f'<line x1="{X(c)}" y1="{Y(f)}" x2="{X(c)}" y2="{Y(t)}" stroke="{col}" '
                     f'stroke-width="{3 if esterna else 1}" stroke-dasharray="{"0" if esterna else "2 2"}"/>')
        else:
            o.append(f'<line x1="{X(f)}" y1="{Y(c)}" x2="{X(t)}" y2="{Y(c)}" stroke="{col}" '
                     f'stroke-width="1" stroke-dasharray="2 2"/>')
    # ingresso dall'esterno: freccia rossa
    for a, b, ori, c, f, t in p["porte"]:
        if b != "fuori":
            continue
        ym = Y((f + t) / 2)
        dx = 1 if c > LATO / 2 else -1
        xa = X(c + dx * (R + 0.95))
        xb = X(c + dx * (R + 0.15))
        o.append(f'<line x1="{xa}" y1="{ym}" x2="{xb}" y2="{ym}" stroke="#c0392b" stroke-width="3"/>')
        o.append(f'<path d="M{xb} {ym} l{dx*9} -6 v12 Z" fill="#c0392b"/>')
    # nomi e misure delle stanze
    for k, q in st.items():
        w, h = q[2] - q[0], q[3] - q[1]
        cx, cy = X((q[0] + q[2]) / 2), Y((q[1] + q[3]) / 2)
        sp_ = p["sopp"]
        if k == "SP" and sp_[0] < (q[0]+q[2])/2 < sp_[2] and sp_[1] < (q[1]+q[3])/2 < sp_[3]:
            if q[3] - sp_[3] > 1.5:
                cy = Y((sp_[3] + q[3]) / 2)
            else:
                cx = X((sp_[2] + q[2]) / 2) if q[2] - sp_[2] > sp_[0] - q[0] else X((q[0] + sp_[0]) / 2)
        verticale = w < 1.9 and h > w
        rot = f' transform="rotate(-90 {cx} {cy})"' if verticale else ""
        lungo = max(w, h) if verticale else w
        corto = min(w, h)
        nome = CORTI[k]
        fs = 11 if lungo * s > 70 else 9.5
        riga = f"{nome} · {num(w)} × {num(h)} · {num(w*h,1)} m²"
        f1 = min(fs, (lungo * s - 8) / (len(riga) * 0.5))
        if corto < 1.4 and (not verticale or f1 >= 8.5):
            fs = f1
            o.append(f'<text x="{cx}" y="{cy + 4}" font-size="{fs:.1f}" font-weight="bold" text-anchor="middle" '
                     f'fill="#222"{rot}>{nome}<tspan font-weight="normal" font-size="{fs-1.5}"> · '
                     f'{num(w)} × {num(h)} · {num(w*h,1)} m²</tspan></text>')
            continue
        o.append(f'<text x="{cx}" y="{cy - 6}" font-size="{fs}" font-weight="bold" text-anchor="middle" '
                 f'fill="#222"{rot}>{nome}'
                 f'<tspan x="{cx}" dy="{fs+2}" font-weight="normal" font-size="{fs-1.5}">'
                 f'{num(w)} × {num(h)}</tspan>'
                 f'<tspan x="{cx}" dy="{fs+1}" font-weight="normal" font-size="{fs-1.5}">'
                 f'{num(w*h,1)} m²</tspan></text>')
    # patio: etichetta nel punto libero piu' grande (griglia grossolana)
    best, bp = 0, (7, 10)
    for i in range(14, 135, 4):
        for j in range(14, 135, 4):
            px, py = i / 10, j / 10
            if any(q[0] - 1.2 < px < q[2] + 1.2 and q[1] - 1 < py < q[3] + 1 for q in st.values()):
                continue
            d = min(px - A, B_ - px, py - A, B_ - py)
            if d > best:
                best, bp = d, (px, py)
    _, patio = controlla(p)
    o.append(f'<text x="{X(bp[0])}" y="{Y(bp[1])}" font-size="15" font-weight="bold" text-anchor="middle" '
             f'fill="#4c7a34">PATIO<tspan x="{X(bp[0])}" dy="17" font-size="11.5" font-weight="normal">'
             f'{num(patio,1)} m² (Aalto: {num(PATIO_AALTO,1)})</tspan></text>')
    # nord e scala grafica
    nx, ny = X(x1 - 0.5), Y(y0 + 0.4)
    o.append(f'<path d="M{nx} {ny} l-7 20 l7 -5 l7 5 Z" fill="#333"/><text x="{nx}" y="{ny+33}" '
             f'font-size="11" text-anchor="middle">N</text>')
    sx, sy = X(x0 + 0.5), Y(y1 - 0.45)
    for i in range(5):
        o.append(f'<rect x="{sx + i*s}" y="{sy}" width="{s}" height="5" fill="{"#333" if i % 2 == 0 else "#fff"}" '
                 f'stroke="#333" stroke-width="0.8"/>')
    o.append(f'<text x="{sx}" y="{sy-4}" font-size="9.5">0</text><text x="{sx+5*s}" y="{sy-4}" '
             f'font-size="9.5" text-anchor="middle">5 m</text>')
    o.append("</svg>")
    return "".join(o)


def svg_aalto(s=13):
    """Piccola pianta della casa vera, per confronto."""
    st = {"SP": (0.40, 0.40, 9.75, 4.75), "K": (9.75, 0.40, 14.00, 3.45), "I": (9.75, 3.45, 14.00, 4.70),
          "C": (9.75, 4.70, 10.75, 10.95), "B": (10.75, 4.70, 14.00, 6.20), "G": (10.75, 6.20, 14.00, 8.15),
          "L2": (10.75, 8.15, 14.00, 10.95), "L1": (9.75, 10.95, 14.00, 14.00)}
    E, An = appendice("est")
    x0, y0, x1, y1 = -0.4, -3.9, 23.8, 14.8
    X = lambda x: (x - x0) * s
    Y = lambda y: (y - y0) * s
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {(x1-x0)*s:.0f} {(y1-y0)*s:.0f}" '
         f'width="100%" font-family="Helvetica, Arial, sans-serif">',
         f'<rect x="{X(0)}" y="{Y(0)}" width="{LATO*s}" height="{LATO*s}" fill="#e9f2e1" stroke="#555" stroke-width="{R*s}"/>']
    for q in (E, An):
        o.append(f'<rect x="{X(q[0])}" y="{Y(q[1])}" width="{(q[2]-q[0])*s}" height="{(q[3]-q[1])*s}" '
                 f'fill="#f1ece4" stroke="#8a7a66"/>')
    for k, q in st.items():
        o.append(f'<rect x="{X(q[0])}" y="{Y(q[1])}" width="{(q[2]-q[0])*s}" height="{(q[3]-q[1])*s}" '
                 f'fill="{COL[ZONA[k]]}" stroke="#333"/>')
        if k in ("SP", "K", "L1"):
            o.append(f'<text x="{X((q[0]+q[2])/2)}" y="{Y((q[1]+q[3])/2)+3}" font-size="9" '
                     f'text-anchor="middle">{"Camera" if k == "L1" else CORTI[k]}</text>')
    o.append(f'<text x="{X(5)}" y="{Y(9.5)}" font-size="10" text-anchor="middle" fill="#4c7a34">PATIO</text>')
    ym = Y(4.05)
    o.append(f'<line x1="{X(15.4)}" y1="{ym}" x2="{X(14.5)}" y2="{ym}" stroke="#c0392b" stroke-width="2.5"/>'
             f'<circle cx="{X(14.2)}" cy="{ym}" r="4" fill="#c0392b"/>')
    o.append("</svg>")
    return "".join(o)


# --- pagina ------------------------------------------------------------------------------
CSS = """
@page { size: A4; margin: 13mm 14mm 13mm 14mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pianta { width: 84%; margin: 2pt auto 0; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 9.6pt; color: #222; line-height: 1.34; margin: 0; }
h1 { font-size: 19pt; margin: 0 0 4pt; } h2 { font-size: 14.5pt; margin: 0 0 4pt; color: #8e2f22; }
h3 { font-size: 11pt; margin: 9pt 0 3pt; } p { margin: 3pt 0 5pt; }
.pagina { page-break-after: always; } .pagina:last-child { page-break-after: auto; }
.sotto { color: #666; margin-bottom: 8pt; }
ul { margin: 2pt 0 4pt; padding-left: 15pt; } li { margin: 1.5pt 0; }
.box { border-left: 4px solid #c0392b; background: #fbf3f1; padding: 5pt 9pt; margin: 6pt 0; }
.ok { border-left-color: #4c7a34; background: #f1f7ec; }
.due { display: flex; gap: 12pt; } .due > div { flex: 1; }
table { border-collapse: collapse; font-size: 9pt; width: 100%; margin-top: 4pt; }
th, td { border: 1px solid #ccc; padding: 2.5pt 5pt; text-align: left; } th { background: #f2f2f2; }
td.n { text-align: right; }
.leg span { display: inline-block; width: 11pt; height: 9pt; border: 1px solid #333; vertical-align: -1pt; margin: 0 3pt 0 9pt; }
"""


def html():
    righe = []
    righe.append('<div class="pagina">')
    righe.append("<h1>Esercizio 4 · Ingresso nell'angolo: quattro proposte</h1>")
    righe.append('<p class="sotto">Casa sperimentale di Aalto a Muuratsalo · nuova disposizione (punto 5)</p>')
    righe.append("<p>Qui trovi quattro modi di riorganizzare la casa con <b>l'ingresso principale "
                 "in un angolo</b> del quadrato. Sono punti di partenza: puoi prenderne uno e "
                 "cambiarlo nella pagina interattiva. Tutte e quattro sono state controllate "
                 "con un programma, regola per regola.</p>")
    righe.append("<h3>Le regole del prof (lezione del 10 novembre)</h3><ul>"
                 "<li><b>Il recinto non si tocca</b>: niente fuori dal quadrato di 14,40, niente "
                 "muri abbattuti. Il graticcio a ovest e la grande apertura a sud restano, quindi "
                 "devono guardare sul patio.</li>"
                 "<li><b>Le superfici restano quelle</b>: ogni stanza può cambiare forma ma non "
                 "superficie, e il patio resta di circa 86,5 m².</li>"
                 "<li><b>L'ingresso dà sul distributivo</b> (corridoio o disimpegno), mai su una "
                 "camera: «apro la porta, scavalco il letto ed entro» è sbagliato.</li>"
                 "<li><b>La zona notte è separata</b> dalla zona giorno; al bagno si arriva dal "
                 "distributivo, senza passare dal soggiorno o da una camera. Meglio se il bagno "
                 "sta vicino all'ingresso, a metà tra giorno e notte.</li>"
                 "<li><b>La cucina sta accanto al pranzo</b>.</li>"
                 "<li><b>Il soppalco dello studio</b> resta con la stessa superficie (3,30 × 4,35); si "
                 "può spostare, ma sotto e sopra servono almeno 2,20 m: dove va lui il tetto deve "
                 "essere alto.</li>"
                 "<li><b>L'annesso degli ospiti</b> si può togliere; se lo tieni sta fuori dal "
                 "quadrato, collegato da un corridoietto (l'ingresso in legno).</li></ul>")
    righe.append('<div class="due"><div><h3>La casa di Aalto, per confronto</h3>' + svg_aalto() +
                 "<p style='font-size:9pt'>Il pallino rosso è la porta tra l'ingresso in legno e "
                 "la casa: Aalto la mette sul lato est, a metà del disimpegno, non nell'angolo.</p></div>"
                 "<div><h3>Come leggere le piante</h3>"
                 '<p class="leg"><span style="background:#f6d5cf"></span>zona giorno<br>'
                 '<span style="background:#d3e0f3"></span>zona notte<br>'
                 '<span style="background:#e3d5ef"></span>bagno<br>'
                 '<span style="background:#fbecb3"></span>ingresso e corridoio<br>'
                 '<span style="background:#e9f2e1"></span>patio</p>'
                 "<p>Le misure sono in metri, larghezza × profondità, misurate dentro le stanze "
                 "(i muri interni non sono contati, come nella pagina interattiva). La freccia "
                 "rossa è l'ingresso; le righe tratteggiate sono le porte interne; il riquadro "
                 "rosso tratteggiato è il soppalco.</p>"
                 "<p>L'ingresso in legno e l'annesso sono disegnati dove li ha messi Aalto (o "
                 "specchiati nella proposta 4): stanno già nell'angolo nord-est, quindi basta "
                 "aprire la porta dell'ingresso proprio nell'angolo della casa.</p></div></div>")
    righe.append("</div>")

    for n, p in enumerate(PROPOSTE, 1):
        err, patio = controlla(p)
        if err:
            raise SystemExit(f"Proposta {n}: " + "; ".join(err))
        righe.append('<div class="pagina">')
        righe.append(f"<h2>Proposta {n} · {p['titolo']}</h2>")
        righe.append(f"<p>{p['idea']}</p>")
        righe.append('<div class="pianta">' + svg_pianta(p) + '</div>')
        righe.append(f"<h3>Il percorso dall'ingresso</h3><p>{p['percorso']}</p>")
        righe.append('<div class="due"><div><h3>Pro</h3><ul>' +
                     "".join(f"<li>{x}</li>" for x in p["pro"]) + "</ul></div>"
                     '<div><h3>Contro</h3><ul>' + "".join(f"<li>{x}</li>" for x in p["contro"]) +
                     "</ul></div></div>")
        righe.append(f"<h3>Soppalco e tetto</h3><p>{p['tetto']}</p>")
        righe.append("</div>")

    # tabella delle superfici
    righe.append('<div class="pagina"><h2>Controllo delle superfici</h2>'
                 "<p>Superfici in m², misurate dentro le stanze. Ogni stanza resta entro il 5% "
                 "di quella di Aalto; ingresso e corridoio si controllano insieme, perché in "
                 "alcune proposte lo spazio passa dall'uno all'altro.</p>")
    righe.append("<table><tr><th>Stanza</th><th>Aalto</th>" +
                 "".join(f"<th>Prop. {n}</th>" for n in range(1, 5)) + "</tr>")
    for k in AALTO:
        righe.append(f"<tr><td>{NOMI[k]}</td><td class='n'>{num(AALTO[k],1)}</td>" +
                     "".join(f"<td class='n'>{num(area(p['stanze'][k]),1)}</td>" for p in PROPOSTE) + "</tr>")
    tot = lambda p: sum(area(q) for q in p["stanze"].values())
    righe.append(f"<tr><th>Totale costruito</th><th class='n'>{num(sum(AALTO.values()),1)}</th>" +
                 "".join(f"<th class='n'>{num(tot(p),1)}</th>" for p in PROPOSTE) + "</tr>")
    righe.append(f"<tr><th>Patio</th><th class='n'>{num(PATIO_AALTO,1)}</th>" +
                 "".join(f"<th class='n'>{num(controlla(p)[1],1)}</th>" for p in PROPOSTE) + "</tr></table>")
    righe.append('<div class="box ok"><b>Controllato in tutte e quattro:</b> nessuna stanza esce '
                 "dal recinto o si sovrappone a un'altra; graticcio e apertura sud restano sul "
                 "patio; l'ingresso è nell'angolo e dà sul distributivo; bagno, guardaroba e "
                 "camere si raggiungono dal corridoio; soggiorno e cucina si raggiungono senza "
                 "passare da una camera; la cucina comunica con il pranzo.</div>")
    righe.append("<h3>Quale scegliere?</h3>"
                 "<p>Se vuoi cambiare poco e andare sul sicuro, la <b>proposta 1</b>: il patio e "
                 "l'annesso restano quelli di Aalto. Quella che risponde meglio al ragionamento "
                 "del prof è la <b>proposta 2</b>: l'ingresso nell'angolo è esattamente il punto "
                 "dove la zona giorno e la zona notte si dividono, e nessuno passa davanti alle "
                 "camere per andare in soggiorno. Le <b>proposte 3 e 4</b> cambiano di più la "
                 "casa (il patio diventa una fascia a sud, piena di sole), ma il corridoio verso "
                 "il soggiorno passa davanti alle camere: sono le più interessanti da discutere, "
                 "ma devi saperle difendere.</p>"
                 "<p>Gli angoli a sud non funzionano: a sud-ovest c'è il graticcio, a sud la grande "
                 "apertura, e un ingresso a sud-est porterebbe dentro la zona notte oppure "
                 "costringerebbe gli ospiti ad attraversarla per arrivare al soggiorno.</p>")
    righe.append("<h3>Prima di consegnare</h3><ul>"
                 "<li>Le porte e le finestre delle piante sono solo indicative: spostale come "
                 "preferisci nella pagina interattiva, purché le porte restino sul distributivo.</li>"
                 "<li>Il tetto nuovo delle proposte 2 e 4 va disegnato anche in sezione, per "
                 "far vedere che sopra e sotto il soppalco ci sono almeno 2,20 m.</li>"
                 "<li>Se togli l'annesso, l'ingresso in legno può diventare più piccolo, ma deve "
                 "restare fuori dal quadrato.</li></ul></div>")
    corpo = "\n".join(righe)
    return (f"<!doctype html><html lang='it'><head><meta charset='utf-8'><title>caricamento</title>"
            f"<style>{CSS}</style></head><body>{corpo}"
            f"<script>window.onload=function(){{document.title='PRONTO'}}</script></body></html>")


if __name__ == "__main__":
    for n, p in enumerate(PROPOSTE, 1):
        e, pt = controlla(p)
        print(f"Proposta {n}: patio {pt:.2f}", "OK" if not e else e)
    if len(sys.argv) > 1:
        open(sys.argv[1], "w", encoding="utf-8").write(html())
