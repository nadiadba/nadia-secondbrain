"""Schemi per la prima lezione di geometria descrittiva (giovedi' 1 ottobre 2026):
formati dei fogli, squadrette, mine, scrittura, regole del segno e il primo esercizio in aula
(piante ruotate e prospetti del solido di esercit_01, come nella scheda esercit_01_esecuzione).

Usa disegni_monge.py senza modificarlo. Questi schemi non sono di Monge: si lavora in
coordinate SVG dirette (x verso destra, y verso il basso) con i piccoli aiuti qui sotto.

Il solido dell'esercizio (modulo a, ingombro 3a x 3a x 3a), ricostruito da esercit_01.jpg e
verificato sulle viste della scheda della docente. Coordinate: u verso sinistra, v verso destra
(a partire dallo spigolo davanti), w in alto; altezza del tetto H(u, v):
- cubetto      u 0-1, v 0-1: w = 1
- rampa        u 1-3, v 0-1: w = (5 - u) / 2  (da 2 a 1)
- terrazza     v 1-3, u >= v - 1: w = 3
- falda        v 1-3, u <= v - 1: w = u - v + 4 (triangolo inclinato, da 3 a 1)
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, COLORI, _etichetta, _escape

SB = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"
BZ = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"

FONT = 'font-family="Helvetica, Arial, sans-serif"'


def col(c):
    return COLORI.get(c, c)


# ---------- aiuti in coordinate SVG ----------

def L(f, a, b, c="nero", w=1.6, dash=None):
    f._linea((a[0], -a[1]), (b[0], -b[1]), c, w, dash)


def T(f, x, y, s, dim=14, c="nero", corsivo=False, ancora="start", grassetto=False):
    st = ' font-style="italic"' if corsivo else ""
    g = ' font-weight="bold"' if grassetto else ""
    f.parti.append(f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{dim}" fill="{col(c)}"'
                   f'{st}{g} text-anchor="{ancora}">{_etichetta(s)}</text>')


def POLY(f, pts, fill="none", op=1.0, stroke="nero", sw=1.6, dash=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    s = f' stroke="{col(stroke)}" stroke-width="{sw}"' if stroke else ' stroke="none"'
    d = f' stroke-dasharray="{dash}"' if dash else ""
    fl = col(fill) if fill != "none" else "none"
    f.parti.append(f'<polygon points="{p}" fill="{fl}" fill-opacity="{op}"{s}{d} stroke-linejoin="round"/>')


def ARCO(f, c, r, a0, a1, colore="grigio", w=1, dash="4,3"):
    """Arco con centro c (SVG), angoli in gradi misurati in senso orario da destra (asse y in basso)."""
    n = 40
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
            c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    f.parti.append(f'<path d="{d}" fill="none" stroke="{col(colore)}" stroke-width="{w}"{ds}/>')


def FRECCIA(f, a, b, c="nero", w=1.6, punta=9):
    L(f, a, b, c, w)
    dx, dy = b[0] - a[0], b[1] - a[1]
    l = math.hypot(dx, dy)
    ux, uy = dx / l, dy / l
    p1 = (b[0] - ux * punta - uy * punta * 0.45, b[1] - uy * punta + ux * punta * 0.45)
    p2 = (b[0] - ux * punta + uy * punta * 0.45, b[1] - uy * punta - ux * punta * 0.45)
    POLY(f, [b, p1, p2], c, 1, None)


def TRATTEGGIO(f, pts, verso="v", passo=6, c="#9a9a9a", w=0.8):
    """Campitura: linee verticali (verso='v') o orizzontali ('o') dentro il poligono pts."""
    k = 0 if verso == "v" else 1          # coordinata che varia tra una linea e l'altra
    lo, hi = min(p[k] for p in pts), max(p[k] for p in pts)
    t = lo + passo / 2
    lati = list(zip(pts, pts[1:] + pts[:1]))
    while t < hi:
        xs = []
        for a, b in lati:
            if (a[k] - t) * (b[k] - t) < 0:
                s = (t - a[k]) / (b[k] - a[k])
                xs.append(a[1 - k] + s * (b[1 - k] - a[1 - k]))
        xs.sort()
        for i in range(0, len(xs) - 1, 2):
            if k == 0:
                L(f, (t, xs[i] + 1), (t, xs[i + 1] - 1), c, w)
            else:
                L(f, (xs[i] + 1, t), (xs[i + 1] - 1, t), c, w)
        t += passo


def nuova(w, h, titolo):
    return Figura(w, h, 0, titolo)


# =====================================================================
# 1. Il rapporto dei lati del formato A4
# =====================================================================
f = nuova(640, 400, "Il formato A4: il lato maggiore è la diagonale del quadrato sul lato minore")
k = 1.1          # px per mm
O = (130, 360)
lmin, lmag = 210 * k, 297 * k
POLY(f, [O, (O[0] + lmin, O[1]), (O[0] + lmin, O[1] - lmag), (O[0], O[1] - lmag)], "blu", 0.06, "blu", 2)
# quadrato sul lato minore
L(f, (O[0], O[1] - lmin), (O[0] + lmin, O[1] - lmin), "grigio", 1, "5,4")
L(f, O, (O[0] + lmin, O[1] - lmin), "rosso", 1.8)
# arco: la diagonale ruota attorno all'angolo fino al lato verticale
ARCO(f, O, lmag, -45, -90, "rosso", 1.2, "5,4")
T(f, O[0] + lmin / 2, O[1] + 20, "l = 21 cm", 14, "nero", ancora="middle")
T(f, O[0] - 10, O[1] - lmag / 2, "d = 29,7 cm", 14, "rosso", ancora="end")
T(f, O[0] + lmin * 0.52, O[1] - lmin * 0.42, "d", 15, "rosso", True)
T(f, O[0] + lmin - 8, O[1] - 12, "quadrato l × l", 12, "grigio", ancora="end")
T(f, O[0] + lmin / 2, O[1] - lmin - 14, "A4", 18, "blu", grassetto=True, ancora="middle")
x = 410
for i, riga in enumerate(["1. Sul lato minore l si costruisce", "    un quadrato.",
                          "2. Si traccia la diagonale d del quadrato.",
                          "3. Con centro nell'angolo si ruota d",
                          "    fino al lato verticale: lì finisce",
                          "    il lato maggiore del foglio.",
                          "", "d = l · √2   (29,7 ≈ 21 × 1,414)"]):
    T(f, x - 20, 120 + i * 22, riga, 13, "#333")
f.salva(SB + "01-formato-a4-rapporto.svg")

# =====================================================================
# 2. La serie A: ogni formato e' due formati piu' piccoli accostati
# =====================================================================
f = nuova(620, 290, "La serie A: ogni formato è formato da due fogli del formato più piccolo")
k = 2.6           # px per cm
X, Y = 40, 30
W, H = 118 * k, 84 * k          # il formato piu' grande, in orizzontale
POLY(f, [(X, Y), (X + W, Y), (X + W, Y + H), (X, Y + H)], "blu", 0.04, "nero", 2)
a1 = W / 2
L(f, (X + a1, Y), (X + a1, Y + H), "nero", 1.6)                    # due A1
L(f, (X, Y + H / 2), (X + a1, Y + H / 2), "nero", 1.4)             # A1 -> due A2
L(f, (X + a1 / 2, Y + H / 2), (X + a1 / 2, Y + H), "nero", 1.2)    # A2 -> due A3
L(f, (X, Y + H * 3 / 4), (X + a1 / 2, Y + H * 3 / 4), "nero", 1)   # A3 -> due A4
POLY(f, [(X, Y + H * 3 / 4), (X + a1 / 2, Y + H * 3 / 4), (X + a1 / 2, Y + H), (X, Y + H)], "rosso", 0.12, None)
T(f, X + W * 0.75, Y + H / 2 - 8, "A1", 18, "blu", grassetto=True, ancora="middle")
T(f, X + W * 0.75, Y + H / 2 + 14, "59,4 × 84", 13, "#333", ancora="middle")
T(f, X + a1 / 2, Y + H / 4 - 6, "A2", 17, "blu", grassetto=True, ancora="middle")
T(f, X + a1 / 2, Y + H / 4 + 14, "42 × 59,4", 13, "#333", ancora="middle")
T(f, X + a1 * 0.75, Y + H * 0.75 - 6, "A3", 16, "blu", grassetto=True, ancora="middle")
T(f, X + a1 * 0.75, Y + H * 0.75 + 12, "29,7 × 42", 12, "#333", ancora="middle")
T(f, X + a1 / 4, Y + H * 0.875 - 4, "A4", 14, "rosso", grassetto=True, ancora="middle")
T(f, X + a1 / 4, Y + H * 0.875 + 14, "21 × 29,7", 11, "#333", ancora="middle")
T(f, X + a1 / 4, Y + H * 0.625 + 5, "A4", 13, "#888", ancora="middle")
for i, riga in enumerate(["Tutto il foglio è il formato", "più grande: 84 × 118 cm (A0),", "superficie circa 1 m².", "",
                          "Si dimezza ogni volta il lato", "maggiore: A0 → A1 → A2 → A3 → A4."]):
    T(f, X + W + 20, Y + 30 + i * 19, riga, 13, "#333")
f.nota(20, 282, "Misure in centimetri. Il lato minore di un formato è il lato maggiore del formato più piccolo.")
f.salva(SB + "01-formati-serie-a.svg")

# =====================================================================
# 3. Le squadrette che lavorano in coppia
# =====================================================================
f = nuova(600, 380, "Le squadrette lavorano in coppia: una sta ferma, l'altra scorre")
# squadretta ferma (30/60), lato lungo orizzontale in alto
F = [(70, 250), (450, 250), (70, 250 + 75)]
POLY(f, F, "grigio", 0.18, "grigio", 1.6)
T(f, 110, 290, "squadretta ferma", 13, "#555")
# squadretta che scorre (45 gradi), cateto sul bordo della ferma
def sq45(x0):
    return [(x0, 250), (x0 + 120, 250), (x0, 130)]
M0, M1 = sq45(120), sq45(250)
POLY(f, M1, "blu", 0.05, "blu", 1.2, "5,4")
POLY(f, M0, "blu", 0.15, "blu", 1.8)
T(f, 128, 200, "squadretta", 12, "blu")
T(f, 128, 214, "che scorre", 12, "blu")
FRECCIA(f, (180, 268), (300, 268), "blu", 1.4)
# le parallele tracciate lungo l'ipotenusa
def ipot(x0, ext=50):
    a, b = (x0 + 120, 250), (x0, 130)
    d = (-1 / math.sqrt(2), -1 / math.sqrt(2))
    return (a[0] - d[0] * 6, a[1] - d[1] * 6), (b[0] + d[0] * ext, b[1] + d[1] * ext)
for x0, n in [(120, "r"), (250, "r′")]:
    a, b = ipot(x0)
    L(f, a, b, "rosso", 2)
    T(f, b[0] - 4, b[1] - 6, n, 15, "rosso", True)
# perpendicolare: il cateto verticale
L(f, (250, 250), (250, 60), "verde", 2)
T(f, 256, 66, "s ⊥ bordo", 13, "verde", True)
L(f, (250, 240), (260, 240), "nero", 1); L(f, (260, 240), (260, 250), "nero", 1)
T(f, 420, 120, "r ∥ r′", 15, "rosso", True)
f.nota(16, 340, "Si tiene ferma una squadretta e si fa scorrere l'altra lungo il suo bordo:")
f.nota(16, 358, "l'ipotenusa traccia rette parallele (r, r′), il cateto verticale una perpendicolare (s).")
f.salva(SB + "01-squadrette-in-coppia.svg")

# =====================================================================
# 4. Le gradazioni delle mine (proposto)
# =====================================================================
f = nuova(600, 300, "Le gradazioni delle mine: dure (H) chiare, morbide (B) scure")
grad = [("2H", "#c4c4c4", 1.0), ("H", "#aaaaaa", 1.3), ("HB", "#7d7d7d", 1.7),
        ("B", "#4d4d4d", 2.2), ("2B", "#262626", 2.8)]
for i, (n, c, w) in enumerate(grad):
    y = 40 + i * 40
    T(f, 40, y + 5, n, 16, "nero", grassetto=True)
    # tratto leggermente ondulato, come a mano
    pts = [(90 + j * 10, y + 1.2 * math.sin(j * 0.9 + i)) for j in range(33)]
    d = "M " + " L ".join(f"{x:.1f} {yy:.1f}" for x, yy in pts)
    f.parti.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
FRECCIA(f, (440, 30), (440, 200), "nero", 1.2)
T(f, 452, 40, "più dura:", 13, "#333"); T(f, 452, 56, "segno grigio, leggero", 12, "#555")
T(f, 452, 180, "più morbida:", 13, "#333"); T(f, 452, 196, "segno scuro, forte", 12, "#555")
f.nota(16, 240, "Mina dura → linee di costruzione. Con la mano pesante la mina dura incide il foglio.")
f.nota(16, 260, "Nella lista del corso: portamine 2 mm con H, 2H, B; portamine 0,5 con B, 2B;")
f.nota(16, 278, "matite in legno HB, B, 2B.")
f.salva(SB + "01-gradazioni-mine.svg")

# =====================================================================
# 5. Scrivere tra due linee parallele
# =====================================================================
f = nuova(600, 250, "Scrivere tra due linee parallele: le lettere vengono tutte uguali")
for y, h, testo, dim in [(70, 22, "NOME E COGNOME", 30), (125, 22, "DATA", 30)]:
    L(f, (40, y - h), (360, y - h), "grigio", 0.9)
    L(f, (40, y), (360, y), "grigio", 0.9)
    T(f, 46, y, testo, dim, "#333")
# linee troppo distanti
L(f, (400, 45), (575, 45), "grigio", 0.9); L(f, (400, 117), (575, 117), "grigio", 0.9)
T(f, 410, 117, "MS", 100, "#999")
T(f, 485, 145, "linee lontane:", 12, "#555", ancora="middle")
T(f, 485, 160, "più difficile", 12, "#555", ancora="middle")
FRECCIA(f, (380, 52), (380, 72), "blu", 1); FRECCIA(f, (380, 64), (380, 44), "blu", 1)
T(f, 376, 92, "linee vicine", 11, "blu", ancora="end")
f.nota(16, 200, "Le due linee si tracciano a mano, leggere; le lettere toccano sia la linea sotto sia quella sopra.")
f.nota(16, 220, "Così si scrivono nome, cognome e data sul foglio (come nell'intestazione della scheda).")
f.salva(SB + "01-scrittura-tra-parallele.svg")

# =====================================================================
# 6. Le regole del segno (dalla scheda dell'esercizio)
# =====================================================================
f = nuova(640, 420, "Le regole del segno (dalla scheda dell'esercizio in aula)")
# 6a. linea unica si / linea ripassata no
def onda(f, a, b, n, amp, c, w, seme=0):
    pts = []
    for j in range(n + 1):
        t = j / n
        x = a[0] + (b[0] - a[0]) * t
        y = a[1] + (b[1] - a[1]) * t + amp * math.sin(j * 1.7 + seme)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    f.parti.append(f'<path d="{d}" fill="none" stroke="{col(c)}" stroke-width="{w}" stroke-linecap="round"/>')
onda(f, (30, 80), (280, 30), 30, 0.8, "#444", 1.6)
for p, n in [((50, 76), "A"), ((250, 36), "B")]:
    f.parti.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="3" fill="white" stroke="#444" stroke-width="1.4"/>')
    T(f, p[0] - 4, p[1] - 10, n, 13, "nero")
T(f, 290, 36, "SÌ", 15, "verde", grassetto=True)
for s, (a, b) in enumerate([((30, 140), (140, 118)), ((120, 124), (215, 104)), ((200, 108), (280, 92))]):
    onda(f, a, b, 12, 0.6, "#444", 2.6, s)
for p, n in [((50, 136), "A"), ((250, 98), "B")]:
    f.parti.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="3" fill="white" stroke="#444" stroke-width="1.4"/>')
    T(f, p[0] - 4, p[1] - 10, n, 13, "nero")
T(f, 290, 98, "NO", 15, "rosso", grassetto=True)
T(f, 30, 175, "Una linea sola, con una direzione precisa,", 12, "#333")
T(f, 30, 190, "anche se il tratto trema un po'.", 12, "#333")
# 6b. moduli e sottomoduli
base = 260
L(f, (340, base), (620, base), "#444", 1.4)
for i in range(2):
    ARCO(f, (400 + i * 120, base), 60, 180, 360, "#444", 1.2, None)
for i in range(4):
    ARCO(f, (370 + i * 60, base), 30, 180, 360, "#777", 1, None)
T(f, 340, 290, "Moduli e sottomoduli: si riportano le", 12, "#333")
T(f, 340, 305, "misure e si controllano le proporzioni.", 12, "#333")
# 6c. parallele vicine
for i in range(4):
    onda(f, (360 + i * 9, 120), (410 + i * 9, 40), 10, 0.5, "#444", 1.2, i)
onda(f, (470, 120), (520, 40), 10, 0.5, "#444", 1.2)
FRECCIA(f, (370, 135), (460, 135), "#444", 1)
T(f, 340, 160, "Prima le parallele vicine, poi", 12, "#333")
T(f, 340, 175, "quelle lontane.", 12, "#333")
# 6d. perpendicolari
cx = [70, 160, 250]
ang = [0, 35, -25]
for x0, a in zip(cx, ang):
    c0 = (x0, 300)
    r = math.radians(a)
    d1 = (math.cos(r), math.sin(r)); d2 = (-math.sin(r), math.cos(r))
    L(f, (c0[0] - d1[0] * 40, c0[1] - d1[1] * 40), (c0[0] + d1[0] * 40, c0[1] + d1[1] * 40), "#444", 1.4)
    L(f, (c0[0] - d2[0] * 10, c0[1] - d2[1] * 10), (c0[0] - d2[0] * 45, c0[1] - d2[1] * 45), "#444", 1.4)
    q = 10
    p1 = (c0[0] + d1[0] * q, c0[1] + d1[1] * q)
    p3 = (c0[0] - d2[0] * q, c0[1] - d2[1] * q)
    p2 = (p1[0] - d2[0] * q, p1[1] - d2[1] * q)
    L(f, p1, p2, "rosso", 1); L(f, p2, p3, "rosso", 1)
T(f, 30, 345, "Esercitarsi sui segmenti perpendicolari,", 12, "#333")
T(f, 30, 360, "anche inclinati; l'angolo retto si segna.", 12, "#333")
f.nota(16, 405, "Le scritte riassumono le note della scheda esercit_01_esecuzione (pagine 2-5).")
f.salva(SB + "01-regole-del-segno.svg")

# =====================================================================
# 7. Il solido dell'esercizio in assonometria
# =====================================================================
m = 46                      # modulo a
kx, ky = m * 0.707, m * 0.707


def A(p, o=(300, 350)):
    u, v, w = p
    return (o[0] - kx * u + kx * v, o[1] - ky * u - ky * v - m * w)


FACCE = [  # (punti, tinta)
    ([(0, 0, 0), (0, 3, 0), (0, 3, 1), (0, 1, 3), (0, 1, 1), (0, 0, 1)], "#dfe6ee"),   # u = 0
    ([(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)], "#c9d3de"),                         # cubetto v = 0
    ([(1, 0, 0), (3, 0, 0), (3, 0, 1), (1, 0, 2)], "#c9d3de"),                         # rampa v = 0
    ([(1, 0, 1), (1, 1, 1), (1, 1, 2), (1, 0, 2)], "#dfe6ee"),                         # rampa u = 1
    ([(0, 1, 1), (1, 1, 1), (1, 1, 2), (3, 1, 1), (3, 1, 3), (0, 1, 3)], "#c9d3de"),   # parete v = 1
    ([(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)], "#f4f1e6"),                         # cubetto sopra
    ([(1, 0, 2), (3, 0, 1), (3, 1, 1), (1, 1, 2)], "#ffffff"),                         # rampa (inclinata)
    ([(0, 1, 3), (3, 1, 3), (3, 3, 3), (2, 3, 3)], "#f4f1e6"),                         # terrazza
    ([(0, 1, 3), (2, 3, 3), (0, 3, 1)], "#ffffff"),                                    # falda (inclinata)
]


def solido(f, o, griglia=True, etichette=True):
    P = lambda p: A(p, o)
    if griglia:
        for i in range(4):     # reticolo dell'ingombro 3 x 3 x 3
            for a, b in [((i, 0, 0), (i, 3, 0)), ((0, i, 0), (3, i, 0)),
                         ((i, 0, 0), (i, 0, 3)), ((0, i, 0), (0, i, 3)),
                         ((0, 0, i), (3, 0, i)), ((0, 0, i), (0, 3, i)),
                         ((3, i, 0), (3, i, 3)), ((i, 3, 0), (i, 3, 3)),
                         ((3, 0, i), (3, 3, i)), ((0, 3, i), (3, 3, i)),
                         ((i, 0, 3), (i, 3, 3)), ((0, i, 3), (3, i, 3))]:
                L(f, P(a), P(b), "#c8c8c8", 0.7, "4,3")
    for pts, c in FACCE:
        POLY(f, [P(p) for p in pts], c, 1, "#1f1f1f", 2.2)
    if etichette:
        for a, b, dx, dy in [((0, 0, 0), (1, 0, 0), -14, 10), ((0, 0, 0), (0, 1, 0), 8, 10),
                             ((0, 0, 0), (0, 0, 1), -16, 0)]:
            pa, pb = P(a), P(b)
            T(f, (pa[0] + pb[0]) / 2 + dx, (pa[1] + pb[1]) / 2 + dy, "a", 15, "rosso", True)


f = nuova(600, 410, "Il solido dato in assonometria (esercit_01): ingombro 3a × 3a × 3a")
solido(f, (300, 360))
f.nota(16, 400, "Grigio tratteggiato: il reticolo dei moduli. In bianco le due superfici inclinate.")
f.salva(SB + "01-esercizio-solido-assonometria.svg")

# =====================================================================
# 8. Le viste: impaginazione (passo 1) e soluzione (passi 2-3)
# =====================================================================
q = 40                                  # modulo nelle viste
GX = [80, 270, 460]                     # sinistra di ogni gruppo
YLT = 175                               # linea di terra (base dei prospetti)
YP = YLT + 18                           # bordo alto delle piante


def pP(i, c, h):
    """Punto del prospetto i: colonna c, altezza h."""
    return (GX[i] + c * q, YLT - h * q)


def pT(i, c, r):
    """Punto della pianta i: colonna c, riga r (dall'alto)."""
    return (GX[i] + c * q, YP + r * q)


def reticolo(f, archi=True):
    L(f, (40, YLT), (620, YLT), "nero", 2.2)
    T(f, 600, YLT - 6, "LT", 13, "nero", True)
    for i in range(3):
        for c in range(4):
            L(f, (GX[i] + c * q, YLT - 3 * q - 12), (GX[i] + c * q, YP + 3 * q + 10), "#b5b5b5", 0.8)
        for h in range(4):
            L(f, (GX[i] - 10, YLT - h * q), (GX[i] + 3 * q + 10, YLT - h * q), "#b5b5b5", 0.8)
            L(f, (GX[i] - 10, YP + h * q), (GX[i] + 3 * q + 10, YP + h * q), "#b5b5b5", 0.8)
        if i < 2:   # le orizzontali continuano da un gruppo all'altro
            for h in range(1, 4):
                L(f, (GX[i] + 3 * q + 10, YLT - h * q), (GX[i + 1] - 10, YLT - h * q), "#c8c8c8", 0.8, "8,6")
            for h in range(0, 4):
                L(f, (GX[i] + 3 * q + 10, YP + h * q), (GX[i + 1] - 10, YP + h * q), "#c8c8c8", 0.8, "8,6")
        if archi:
            for c in range(3):
                ARCO(f, (GX[i] + c * q + q / 2, YLT - 3 * q), q / 2, 180, 360, "#9a9a9a", 0.9, None)
    if archi:   # riporto dei moduli in altezza, a sinistra
        for h in range(3):
            ARCO(f, (GX[0], YLT - h * q - q / 2), q / 2, 90, 270, "#9a9a9a", 0.9, None)
            ARCO(f, (GX[0], YP + h * q + q / 2), q / 2, 90, 270, "#9a9a9a", 0.9, None)
        ARCO(f, (GX[0], YLT - 1.5 * q), 1.5 * q, 90, 270, "#b0b0b0", 0.9, None)
        ARCO(f, (GX[0], YP + 1.5 * q), 1.5 * q, 90, 270, "#b0b0b0", 0.9, None)
    for i in range(3):
        T(f, GX[i] + 1.5 * q, 22, f"prospetto {i + 1}", 13, "#444", ancora="middle")
        T(f, GX[i] + 1.5 * q, YP + 3 * q + 30, f"pianta {i + 1}", 13, "#444", ancora="middle")


f = nuova(640, 380, "Passo 1: impaginare il foglio con il reticolo dei moduli (linee leggere)")
reticolo(f)
f.nota(16, 372, "Sopra la LT i tre prospetti, sotto le tre piante; gli archi riportano il modulo a.")
f.salva(SB + "01-esercizio-impaginazione.svg")

# --- soluzione -------------------------------------------------------
PIANTE = {
    0: dict(orizz=[[(2, 2), (3, 2), (3, 3), (2, 3)], [(3, 2), (0, 2), (0, 0), (1, 0)]],
            linee=[((0, 2), (3, 2)), ((2, 2), (2, 3)), ((1, 0), (3, 2))],
            frecce=[((1.7, 2.6), (0.25, 2.6)), ((2.0, 1.0), (2.75, 0.25))]),
    1: dict(orizz=[[(0, 2), (1, 2), (1, 3), (0, 3)], [(1, 3), (1, 0), (3, 0), (3, 1)]],
            linee=[((1, 0), (1, 3)), ((0, 2), (1, 2)), ((1, 3), (3, 1))],
            frecce=[((0.45, 1.8), (0.45, 0.2)), ((2.0, 2.0), (2.75, 2.75))]),
    2: dict(orizz=[[(2, 0), (3, 0), (3, 1), (2, 1)], [(2, 0), (2, 3), (0, 3), (0, 2)]],
            linee=[((2, 0), (2, 3)), ((2, 1), (3, 1)), ((2, 0), (0, 2))],
            frecce=[((2.55, 1.2), (2.55, 2.8)), ((1.0, 1.0), (0.25, 0.25))]),
}
PROSPETTI = {
    0: dict(contorno=[(0, 0), (3, 0), (3, 3), (0, 3)], bianco=[],
            linee=[((0, 1), (2, 2)), ((2, 2), (2, 1)), ((2, 1), (3, 1))]),
    1: dict(contorno=[(0, 0), (0, 2), (1, 2), (1, 3), (3, 3), (3, 0)], bianco=[[(1, 3), (3, 3), (3, 1)]],
            linee=[((0, 1), (1, 1)), ((1, 3), (3, 1)), ((1, 2), (1, 0))]),
    2: dict(contorno=[(0, 0), (0, 3), (2, 3), (2, 2), (3, 2), (3, 0)], bianco=[[(2, 1), (3, 1), (3, 2), (2, 2)]],
            linee=[((2, 2), (2, 1)), ((2, 1), (3, 1))]),
}


def soluzione(f, campiture=True):
    for i in range(3):
        pr, pi = PROSPETTI[i], PIANTE[i]
        cont = [pP(i, *p) for p in pr["contorno"]]
        if campiture:
            TRATTEGGIO(f, cont, "v", 5, "#8c8c8c", 0.8)
            for b in pr["bianco"]:
                POLY(f, [pP(i, *p) for p in b], "#ffffff", 1, None)
            for poly in pi["orizz"]:
                TRATTEGGIO(f, [pT(i, *p) for p in poly], "o", 5, "#b0b0b0", 0.7)
        POLY(f, cont, "none", 1, "#1f1f1f", 2.4)
        for a, b in pr["linee"]:
            L(f, pP(i, *a), pP(i, *b), "#1f1f1f", 2.4)
        POLY(f, [pT(i, 0, 0), pT(i, 3, 0), pT(i, 3, 3), pT(i, 0, 3)], "none", 1, "#1f1f1f", 2.4)
        for a, b in pi["linee"]:
            L(f, pT(i, *a), pT(i, *b), "#1f1f1f", 2.4)
        if campiture:
            for a, b in pi["frecce"]:
                FRECCIA(f, pT(i, *a), pT(i, *b), "rosso", 1.4, 8)


f = nuova(640, 380, "Passi 2-3: le tre piante ruotate e i prospetti, con le campiture")
reticolo(f)
soluzione(f)
f.nota(16, 372, "Campite le superfici orizzontali (piante) e verticali (prospetti); in bianco le inclinate.")
f.salva(SB + "01-esercizio-piante-e-prospetti.svg")

# =====================================================================
# BOZZA
# =====================================================================

# B1. Da dove si guarda: le tre rotazioni (proposto) --------------------
f = nuova(640, 330, "Il davanti dipende dalla rotazione: la freccia indica da dove si guarda")
Y0 = 50


def pt(i, c, r):
    return (GX[i] + c * q, Y0 + r * q)


for i in range(3):
    for poly in PIANTE[i]["orizz"]:
        TRATTEGGIO(f, [pt(i, *p) for p in poly], "o", 5, "#b0b0b0", 0.7)
for i, (c, r) in enumerate([(2, 2), (0, 2), (2, 0)]):
    POLY(f, [pt(i, c, r), pt(i, c + 1, r), pt(i, c + 1, r + 1), pt(i, c, r + 1)], "arancio", 0.35, None)
for i in range(3):
    POLY(f, [pt(i, 0, 0), pt(i, 3, 0), pt(i, 3, 3), pt(i, 0, 3)], "none", 1, "#1f1f1f", 2)
    for a, b in PIANTE[i]["linee"]:
        L(f, pt(i, *a), pt(i, *b), "#1f1f1f", 2)
    FRECCIA(f, pt(i, 1.5, 4.0), pt(i, 1.5, 3.25), "blu", 2, 10)
    T(f, GX[i] + 1.5 * q, Y0 + 4 * q + 22, f"pianta {i + 1}", 13, "#444", ancora="middle")
T(f, GX[1] + 1.5 * q, 30, "ruotata di 90° in senso orario", 11, "#555", ancora="middle")
T(f, GX[0] + 1.5 * q, 30, "posizione di partenza", 11, "#555", ancora="middle")
T(f, GX[2] + 1.5 * q, 30, "ruotata di 90° in senso antiorario", 11, "#555", ancora="middle")
f.nota(16, 268, "Arancio: il cubetto. È sempre lo stesso oggetto, ruotato; si guarda sempre dal basso del foglio,")
f.nota(16, 286, "quindi davanti c'è ogni volta un lato diverso:")
f.nota(16, 304, "pianta 1: cubetto e rampa · pianta 2: cubetto e falda · pianta 3: rampa e terrazza.")
f.salva(BZ + "b01-da-dove-si-guarda.svg")

# B2. Scala grafica (proposto) --------------------------------------------
f = nuova(620, 250, "La scala grafica: quanto misura sul foglio un metro vero")
def scala(f, y, cm_px, metri, passo_lab, nome, sotto):
    x0 = 50
    for j in range(metri):
        POLY(f, [(x0 + j * cm_px, y), (x0 + (j + 1) * cm_px, y), (x0 + (j + 1) * cm_px, y + 8),
                 (x0 + j * cm_px, y + 8)], "#1f1f1f" if j % 2 == 0 else "#ffffff", 1, "#1f1f1f", 1)
    for j in range(0, metri + 1, passo_lab):
        T(f, x0 + j * cm_px, y + 24, ("m " if j else "") + str(j), 12, "#333", True, "middle")
    T(f, 590, y + 4, nome, 20, "nero", True, "end")
    T(f, x0, y - 10, sotto, 12, "rosso")
scala(f, 50, 40, 10, 1, "1:100", "1 m vero = 1 cm sul foglio")
scala(f, 130, 80, 5, 1, "1:50", "1 m vero = 2 cm sul foglio")
f.nota(16, 205, "Lo schema non è in misura reale: conta il rapporto. In 1:50 tutto è il doppio che in 1:100.")
f.nota(16, 225, "La scala grafica resta giusta anche se il foglio viene ridotto o fotocopiato.")
f.salva(BZ + "b01-scala-grafica.svg")

# B3. Il solido e le tre piante affiancati (sintesi) -----------------------
f = nuova(640, 400, "Dal solido alle viste: le superfici orizzontali, verticali e inclinate")
solido(f, (170, 375), griglia=False, etichette=False)
T(f, 360, 60, "In pianta (dall'alto):", 13, "nero", grassetto=True)
T(f, 360, 80, "orizzontali → campite", 13, "#333")
T(f, 360, 98, "inclinate → bianche, con la freccia", 13, "#333")
T(f, 360, 116, "     che scende", 13, "#333")
T(f, 360, 136, "verticali → solo una linea", 13, "#333")
T(f, 360, 180, "Nel prospetto (davanti):", 13, "nero", grassetto=True)
T(f, 360, 200, "verticali → campite", 13, "#333")
T(f, 360, 218, "inclinate → bianche", 13, "#333")
T(f, 360, 236, "orizzontali → solo una linea", 13, "#333")
f.nota(16, 392, "La rampa e la falda triangolare sono le due superfici inclinate del solido.")
f.salva(BZ + "b01-superfici-e-viste.svg")
print("ok")
