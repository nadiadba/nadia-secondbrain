"""Schemi per la bozza di geometria descrittiva 09 (il ribaltamento del piano generico,
lezione del 29 ottobre).

Usa disegni_monge.py senza modificarlo; le funzioni di servizio sono copiate da
geometria-09.py (che non va toccato, perche' rigenera gli schemi della sbobina).
Stesso piano alfa e stessi triangoli della sbobina, cosi' bozza e sbobina si confrontano.
Ogni punto ribaltato e' calcolato due volte (costruzione della docente e rotazione vera
nello spazio) e lo script controlla che coincidano e che le misure siano quelle vere.

Disegni (in bozze/img/):
- b09-canonica-passo-1 ... 4         forma canonica, un passo per disegno
- b09-spazio-ribaltamento-laterale   nello spazio: gamma si abbatte su pi1 intorno a t1gamma (B -> B barrato)
- b09-tecnica-passo-1 ... 3          forma tecnica (intorno all'orizzontale o, senza LT)
- b09-spazio-ribaltamento-orizzontale nello spazio: alfa ruota intorno a o fino al piano orizzontale di C
- b09-squadretta-foglio              la squadretta con il lato AB su pi1, sul foglio
- b09-spazio-squadretta              nello spazio: la squadretta con il lato AB su pi1
- b09-spazio-piramide                proposto: una faccia della piramide si abbatte su pi1
- b09-sviluppo-piramide              proposto: lo sviluppo della piramide sul foglio
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"


# ---------- funzioni di servizio (copiate da geometria-09.py) ----------

def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def unit(v):
    l = math.hypot(*v)
    return (v[0] / l, v[1] / l)


def arco(f, c, r, a0, a1, colore="grigio", spessore=1, tratteggio="4,3", n=48):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(f._s((c[0] + r * math.cos(a), c[1] + r * math.sin(a))))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    f.parti.append(f'<path d="{d}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                   f'stroke-width="{spessore}"{dash}/>')


def arco_tra(f, c, p, q, **kw):
    """Arco di centro c da p a q (il verso piu' corto)."""
    a0, a1 = angolo(c, p), angolo(c, q)
    if a1 < a0 - 180:
        a1 += 360
    if a1 > a0 + 180:
        a1 -= 360
    arco(f, c, math.dist(c, p), a0, a1, **kw)


def angolo(c, p):
    return math.degrees(math.atan2(p[1] - c[1], p[0] - c[0]))


def tacche(f, a, b, n, colore="nero", t=0.5):
    L = math.dist(a, b)
    d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    q = (-d[1], d[0])
    m = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        c = lungo(m, d, o)
        f._linea(lungo(c, q, -5), lungo(c, q, 5), colore, 1.3)


def nota_righe(f, y, righe):
    for i, r in enumerate(righe):
        f.nota(20, y + 17 * i, r)


def piede(p, a, b):
    d = unit((b[0] - a[0], b[1] - a[1]))
    t = (p[0] - a[0]) * d[0] + (p[1] - a[1]) * d[1]
    return (a[0] + d[0] * t, a[1] + d[1] * t)


def lato(p, a, b):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def ribalta_3d(P, a, b, quota_asse, verso):
    p1 = P1(P)
    H = piede(p1, a, b)
    r = math.sqrt(math.dist(p1, H) ** 2 + (P[2] - quota_asse) ** 2)
    n = unit((-(b[1] - a[1]), b[0] - a[0]))
    if lato(lungo(H, n, 1), a, b) * verso < 0:
        n = (-n[0], -n[1])
    return lungo(H, n, r)


def costruzione_docente(P, a, b, quota_asse, verso):
    p1 = P1(P)
    H = piede(p1, a, b)
    dasse = unit((b[0] - a[0], b[1] - a[1]))
    q = P[2] - quota_asse
    Pbar = lungo(p1, dasse, q)
    r = math.dist(H, Pbar)
    g = unit((p1[0] - H[0], p1[1] - H[1]))
    if lato(lungo(H, g, 1), a, b) * verso < 0:
        g = (-g[0], -g[1])
    Pstar = lungo(H, g, r)
    return p1, H, Pbar, r, Pstar


def affine(Q1, asse_a, asse_b, P1p, Pstar):
    U = interseca(P1p, Q1, asse_a, asse_b)
    H = piede(Q1, asse_a, asse_b)
    return interseca(U, Pstar, Q1, H), U


def controlla(nome, veri, trovati):
    for i in range(len(veri)):
        j = (i + 1) % len(veri)
        a, b = math.dist(veri[i], veri[j]), math.dist(trovati[i], trovati[j])
        assert abs(a - b) < 1e-6, (nome, a, b)
    print(f"{nome}: misure vere ok")


# ---------- funzioni per lo spazio ----------

def S1(p, z=0):
    """Punto del disegno della prima proiezione -> punto 3D sul piano orizzontale di quota z."""
    return (p[0], -p[1], z)


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def norm3(v):
    l = math.sqrt(dot(v, v))
    return tuple(x / l for x in v)


def arco_spazio(t, centro, P, Q, colore="rosso", spessore=1.4, tratteggio="5,3", n=40):
    """Arco di circonferenza nello spazio, di centro 'centro', da P a Q (stesso raggio)."""
    e1 = sub(P, centro)
    r = math.sqrt(dot(e1, e1))
    e1 = tuple(x / r for x in e1)
    v = sub(Q, centro)
    c = dot(v, e1)
    e2 = norm3(tuple(v[i] - c * e1[i] for i in range(3)))
    amax = math.atan2(dot(v, e2), c)
    assert abs(math.sqrt(dot(v, v)) - r) < 1e-6, "arco: raggi diversi"
    pts = [t._p(tuple(centro[j] + r * (math.cos(amax * i / n) * e1[j] + math.sin(amax * i / n) * e2[j])
                      for j in range(3))) for i in range(n + 1)]
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    t.f.parti.append('<path d="M ' + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) +
                     f'" fill="none" stroke="{COLORI.get(colore, colore)}" stroke-width="{spessore}"{dash}/>')


# ---------- il piano generico alfa (come nella sbobina) ----------
K3 = (40, 0, 0)
n_a, d_a = piano(K3, (440, 220, 0), (440, 0, 200))
_dt = (400 / math.hypot(400, 220), 220 / math.hypot(400, 220), 0)
_w = (n_a[1] * _dt[2] - n_a[2] * _dt[1], n_a[2] * _dt[0] - n_a[0] * _dt[2], n_a[0] * _dt[1] - n_a[1] * _dt[0])
_w = norm3(_w)
if _w[2] < 0:
    _w = tuple(-x for x in _w)


def in_alfa(s, h):
    return tuple(K3[i] + s * _dt[i] + h * _w[i] for i in range(3))


K = (40, 0)
T1A = (440, -220)
d1 = unit((T1A[0] - K[0], T1A[1] - K[1]))

# =========================================================================================
# FORMA CANONICA: quattro passi
# =========================================================================================
A = in_alfa(260, 30)
B = in_alfa(330, 140)
C = in_alfa(110, 0)
verso = -lato(P1(B), K, T1A)
b1, H, Bbar, r, Bst = costruzione_docente(B, K, T1A, 0, verso)
assert math.dist(Bst, ribalta_3d(B, K, T1A, 0, verso)) < 1e-6
Ast, U = affine(P1(A), K, T1A, P1(B), Bst)
assert math.dist(Ast, ribalta_3d(A, K, T1A, 0, verso)) < 1e-6
Cst = P1(C)
controlla("forma canonica", [A, B, C], [Ast, Bst, Cst])
g = unit((Bst[0] - H[0], Bst[1] - H[1]))

TITOLI_C = {
    1: "Forma canonica · passo 1: il piano γ perpendicolare ad α, per B",
    2: "Forma canonica · passo 2: ribaltamento laterale di γ, il punto B̄",
    3: "Forma canonica · passo 3: il raggio di rotazione HB̄ porta B in B*",
    4: "Forma canonica · passo 4: l'affinità di asse t₁α dà A* (e C* ≡ C₁)",
}
NOTE_C = {
    1: ["Il punto più lontano da t₁α è B. Per B₁ si traccia t₁γ perpendicolare a t₁α:",
        "γ è proiettante in prima e perpendicolare ad α. H è il punto in cui t₁γ incontra t₁α."],
    2: ["Si prende la quota di B (distanza di B₂ dalla LT, due lineette) e la si riporta da B₁",
        "sulla perpendicolare a t₁γ: si trova B̄. Il triangolo B₁HB̄ è il triangolo di rotazione."],
    3: ["HB̄ è il raggio di rotazione (vera distanza di B da t₁α). Centro del compasso in H,",
        "raggio HB̄: l'arco porta il punto su t₁γ, dalla parte opposta alla figura. Lì c'è B*."],
    4: ["A₁B₁ prolungata incontra l'asse t₁α in U (punto unito); la retta UB* incontra in A* la",
        "perpendicolare all'asse condotta da A₁. C sta sull'asse: C* ≡ C₁. A*B*C* è la vera forma."],
}

for passo in (1, 2, 3, 4):
    f = Figura(680, 560, 165, TITOLI_C[passo], x0=20)
    f.lt(0, 660)
    f.traccia(K, lungo(K, d1, 620)); f.testo(lungo(K, d1, 620), "t_1α", -36, 4)
    f.figura([P2(A), P2(B), P2(C)], "blu")
    f.figura([P1(A), P1(B), P1(C)], "blu")
    for p in (A, B, C):
        f.richiamo(p[0], P2(p)[1], P1(p)[1])
    # passo 1
    fine_g = lungo(H, g, r + 40)
    inizio_g = lungo(b1, g, -45)
    f.traccia(inizio_g, fine_g, "verde")
    f.testo(inizio_g, "t_1γ", 4, -6, "verde")
    f.angolo_retto(H, d1, g)
    f.punto(H, "H", -8, -12)
    if passo >= 2:
        f.costruzione(b1, Bbar)
        tacche(f, (B[0], 0), P2(B), 2)
        tacche(f, b1, Bbar, 2)
        f.angolo_retto(b1, d1, (-g[0], -g[1]))
        f.retta(H, Bbar, "verde", 1.4)
        f.punto(Bbar, "B̄", 6, -4, "verde")
        if passo == 2:
            f.figura([b1, H, Bbar], "verde")
    if passo >= 3:
        arco_tra(f, H, Bbar, Bst, colore="grigio", spessore=1, tratteggio="4,3")
        f.punto(Bst, "B*", 8, 10, "rosso")
    if passo >= 4:
        f.costruzione(P1(B), U)
        f.costruzione(U, Ast)
        f.costruzione(P1(A), Ast)
        f.figura([Ast, Bst, Cst], "rosso")
        f.punto(U, "U", -6, 18)
        f.punto(Ast, "A*", -28, 6, "rosso")
        f.testo(Cst, "≡ C*", -44, 24, "rosso", 13)
    for p, n_, e2, e1 in [(A, "A", (-10, -10), (8, 4)), (B, "B", (8, -6), (-24, -10)), (C, "C", (-6, 20), (6, -10))]:
        f.punto(P2(p), n_ + "₂", *e2, "blu")
        f.punto(P1(p), n_ + "₁", *e1, "blu")
    nota_righe(f, 520, NOTE_C[passo])
    f.salva(OUT + f"b09-canonica-passo-{passo}.svg")


# =========================================================================================
# Nello spazio: il ribaltamento laterale di gamma (B -> B barrato) e la rotazione vera (B -> B*)
# =========================================================================================
def triedro(titolo, h=520, w=620, origine=(300, 190), scala=0.72, Y=230, X3=400, U=360, Z=220):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, origine, X3=X3, U=U, Y=Y, Z=Z, scala=scala)
    t.piani()
    return f, t


f, t = triedro("Nello spazio: γ si abbatte su π₁ intorno a t₁γ e porta B in B̄", h=510, Y=300)
t.piano(n_a, d_a, "blu", 0.08)
t.tracce(n_a, d_a, "grigio")
n_g = (d1[0], -d1[1], 0)
t.piano(n_g, dot(n_g, B), "verde", 0.13)
Hs, b1s, Bbars, Bsts = S1(H), S1(b1), S1(Bbar), S1(Bst)
t._poligono([A, B, C], "blu", 0.18, "blu")
# triangolo di rotazione nello spazio (verde) e ribaltato su pi1 (arancio)
t._poligono([b1s, Hs, B], "verde", 0.35, "verde")
t._poligono([b1s, Hs, Bbars], "arancio", 0.30, "arancio")
t.segmento(Hs, Bsts, "verde", 1.6)  # t1gamma fino a B*
t.segmento(b1s, S1(lungo(b1, g, -45)), "verde", 1.6)
arco_spazio(t, b1s, B, Bbars, "arancio", 1.4)          # ribaltamento laterale: intorno a t1gamma
arco_spazio(t, Hs, B, Bsts, "rosso", 1.2)              # la rotazione vera intorno a t1alfa
# su pi1 il compasso: centro H, da B barrato a B*
arco_spazio(t, Hs, Bbars, Bsts, "grigio", 1.0, "4,3")
t.punto(B, "B", 6, -6, "blu")
t.punto(b1s, "B₁", -24, 14)
t.punto(Hs, "H", -20, -4)
t.punto(Bbars, "B̄", 8, 4, "arancio")
t.punto(Bsts, "B*", -12, 20, "rosso")
t.testo(S1(lungo(H, g, r * 0.55)), "t_1γ", 8, 0, "verde", 13)
t.testo((B[0] + 40, -b1[1] - 60, 150), "γ", 0, 0, "verde")
t.testo(S1(lungo(K, d1, 330)), "t_1α", -10, 20, "nero", 13)
f.nota(20, 456, "B₁HB (verde) è il triangolo di rotazione: sta su γ, che è verticale. Abbattendo γ intorno a t₁γ")
f.nota(20, 473, "(arco arancio) il triangolo si stende su π₁ come B₁HB̄, con le stesse misure: HB̄ = HB è il raggio.")
f.nota(20, 490, "Col compasso (arco grigio) HB̄ si porta su t₁γ: è B*, lo stesso punto della rotazione vera (rosso).")
f.salva(OUT + "b09-spazio-ribaltamento-laterale.svg")

# =========================================================================================
# FORMA TECNICA: tre passi (senza linea di terra)
# =========================================================================================
A6 = in_alfa(300, 90)
B6 = in_alfa(360, 200)
C6 = in_alfa(150, 50)
qo = C6[2]
o2a, o2b = (P2(C6)[0] - 60, qo), (P2(B6)[0] + 80, qo)
M2 = interseca(P2(A6), P2(B6), o2a, o2b)
M1 = interseca(P1(A6), P1(B6), (M2[0], 0), (M2[0], -1))
do = unit((M1[0] - P1(C6)[0], M1[1] - P1(C6)[1]))
assert abs(do[0] * d1[1] - do[1] * d1[0]) < 1e-9       # o1 parallela a t1alfa
oa, ob = lungo(P1(C6), do, -70), lungo(P1(C6), do, 430)
verso6 = -lato(P1(B6), oa, ob)
b16, H6, Bbar6, r6, Bst6 = costruzione_docente(B6, oa, ob, qo, verso6)
assert math.dist(Bst6, ribalta_3d(B6, oa, ob, qo, verso6)) < 1e-6
Ast6, U6 = affine(P1(A6), oa, ob, P1(B6), Bst6)
assert math.dist(Ast6, ribalta_3d(A6, oa, ob, qo, verso6)) < 1e-6
assert math.dist(U6, M1) < 1e-6
Cst6 = P1(C6)
controlla("forma tecnica", [A6, B6, C6], [Ast6, Bst6, Cst6])
g6 = unit((Bst6[0] - H6[0], Bst6[1] - H6[1]))
print("forma tecnica: quote A", round(A6[2], 1), "B", round(B6[2], 1), "C", round(C6[2], 1))

TITOLI_T = {
    1: "Forma tecnica · passo 1: l'orizzontale o per C (o₂ e o₁), senza LT",
    2: "Forma tecnica · passo 2: γ₁ ⊥ o₁ per B₁; B̄ con la quota misurata da o₂",
    3: "Forma tecnica · passo 3: B* col compasso, poi l'affinità di asse o₁",
}
NOTE_T = {
    1: ["o₂ passa per C₂ ed è orizzontale. r = AB: r₂ prolungata incontra o₂ in M₂; M₁ sta su r₁,",
        "sulla linea di richiamo. o₁ passa per C₁ e per M₁: è l'asse di rotazione."],
    2: ["γ₁ perpendicolare a o₁ per B₁; H è l'incontro con o₁. Cambia una sola misura: da B₁ si riporta",
        "la distanza di B₂ da o₂ (due lineette), non dalla LT, perché l'asse sta alla quota di C."],
    3: ["Centro in H, raggio HB̄: B* su γ₁. r₁ incontra l'asse proprio in M₁ (punto unito): la retta",
        "M₁B* incontra in A* la perpendicolare a o₁ condotta da A₁. C sta sull'asse: C* ≡ C₁."],
}

for passo in (1, 2, 3):
    f = Figura(640, 580, 200, TITOLI_T[passo], x0=-80)
    f.figura([P2(A6), P2(B6), P2(C6)], "blu")
    f.figura([P1(A6), P1(B6), P1(C6)], "blu")
    for p in (A6, B6, C6):
        f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.retta(o2a, o2b, "arancio", 1.8); f.testo(o2b, "o₂", 4, 4, "arancio")
    f.retta(P2(A6), M2, "grigio", 1)
    f.retta(P1(A6), M1, "grigio", 1)
    f.richiamo(M2[0], M2[1], M1[1])
    f.retta(oa, ob, "arancio", 1.8); f.testo(ob, "o₁", -6, 18, "arancio")
    f.punto(M2, "M₂", -8, 18, "grigio"); f.punto(M1, "M₁", -30, -6, "nero")
    mA2 = ((P2(A6)[0] + P2(B6)[0]) / 2, (P2(A6)[1] + P2(B6)[1]) / 2)
    mA1 = ((P1(A6)[0] + P1(B6)[0]) / 2, (P1(A6)[1] + P1(B6)[1]) / 2)
    f.testo(mA2, "r₂", 8, 8, "grigio", 13)
    f.testo(mA1, "r₁", 0, 18, "grigio", 13)
    if passo >= 2:
        f.retta(lungo(b16, g6, -40), lungo(H6, g6, r6 + 35), "verde", 1.8)
        f.testo(lungo(b16, g6, -40), "γ₁", 6, -2, "verde")
        f.angolo_retto(H6, do, g6)
        f.costruzione(b16, Bbar6)
        f.costruzione(P2(B6), (P2(B6)[0], qo))
        tacche(f, (P2(B6)[0], qo), P2(B6), 2)
        tacche(f, b16, Bbar6, 2)
        f.retta(H6, Bbar6, "verde", 1.4)
        f.punto(Bbar6, "B̄", 6, -4, "verde"); f.punto(H6, "H", 6, -6)
        if passo == 2:
            f.figura([b16, H6, Bbar6], "verde")
    if passo >= 3:
        arco_tra(f, H6, Bbar6, Bst6, colore="grigio", spessore=1, tratteggio="4,3")
        f.costruzione(P1(B6), U6); f.costruzione(U6, Ast6); f.costruzione(P1(A6), Ast6)
        f.figura([Ast6, Bst6, Cst6], "rosso")
        f.punto(Ast6, "A*", -28, 6, "rosso"); f.punto(Bst6, "B*", 8, 12, "rosso")
        f.testo(Cst6, "≡ C*", -36, 28, "rosso", 13)
    for p, n_, e2, e1 in [(A6, "A", (-8, -10), (8, 4)), (B6, "B", (8, -6), (8, 0)), (C6, "C", (-24, -8), (-10, -10))]:
        f.punto(P2(p), n_ + "₂", *e2, "blu")
        f.punto(P1(p), n_ + "₁", *e1, "blu")
    nota_righe(f, 545, NOTE_T[passo])
    f.salva(OUT + f"b09-tecnica-passo-{passo}.svg")

# =========================================================================================
# Nello spazio: alfa ruota intorno all'orizzontale o fino al piano orizzontale alla quota di C
# =========================================================================================
f, t = triedro("Nello spazio: α ruota intorno a o fino al piano orizzontale di C", h=500, Y=330,
               origine=(300, 175), scala=0.66)
t.piano(n_a, d_a, "blu", 0.08)
t.tracce(n_a, d_a, "grigio")
t.piano((0, 0, 1), qo, "arancio", 0.12)
M3 = (M2[0], -M1[1], qo)
dir_o = norm3(sub(M3, C6))
o_a = tuple(C6[i] - 90 * dir_o[i] for i in range(3))
o_b = tuple(C6[i] + 330 * dir_o[i] for i in range(3))
t.segmento(o_a, o_b, "arancio", 2.2)
t.testo(o_b, "o", 6, 4, "arancio")
t._poligono([A6, B6, C6], "blu", 0.30, "blu")
H63 = S1(H6, qo)
Bst63, Ast63, Cst63 = S1(Bst6, qo), S1(Ast6, qo), S1(Cst6, qo)
piedeB = (B6[0], B6[1], qo)
t.segmento(piedeB, B6, "nero", 1.2, "3,3")
t.segmento(H63, B6, "verde", 1.4)
t.segmento(H63, piedeB, "verde", 1.0)
arco_spazio(t, H63, B6, Bst63, "rosso", 1.4)
t._poligono([Ast63, Bst63, Cst63], "rosso", 0.22, "rosso")
t.punto(A6, "A", 8, 14, "blu"); t.punto(B6, "B", 6, -6, "blu"); t.punto(C6, "C ≡ C*", -68, -10, "blu")
t.punto(H63, "H", -6, 18)
t.punto(Ast63, "A*", -26, 12, "rosso"); t.punto(Bst63, "B*", 8, 14, "rosso")
f.nota(20, 446, "L'asse è l'orizzontale o, alla quota di C: α si abbatte sul piano orizzontale (arancio) di quella quota.")
f.nota(20, 463, "La quota di B (tratteggio nero) si misura da quel piano, non da π₁. Il piano è parallelo a π₁, quindi")
f.nota(20, 480, "la prima proiezione di A*B*C* ha le stesse misure: per questo sul foglio la si disegna direttamente.")
f.salva(OUT + "b09-spazio-ribaltamento-orizzontale.svg")

# =========================================================================================
# La squadretta con il lato AB su pi1: sul foglio e nello spazio.
# Il lato AB e' piu' avanti che nella sbobina (dove C finiva dietro pi2, con C1 sopra la LT):
# cosi' tutta la squadretta sta nel primo diedro.
# =========================================================================================
sA, sB = 170.0, 330.0
L = sB - sA
A7 = (K3[0] + d1[0] * sA, -d1[1] * sA, 0)
B7 = (K3[0] + d1[0] * sB, -d1[1] * sB, 0)
C7 = tuple(A7[i] + L * math.tan(math.radians(30)) * _w[i] for i in range(3))
verso7 = -lato(P1(C7), K, T1A)
c17, H7, Cbar7, r7, Cst7 = costruzione_docente(C7, K, T1A, 0, verso7)
assert math.dist(Cst7, ribalta_3d(C7, K, T1A, 0, verso7)) < 1e-6
controlla("squadretta", [A7, B7, C7], [P1(A7), P1(B7), Cst7])
assert C7[1] > 0 and C7[2] > 0                 # C nel primo diedro
assert math.dist(H7, P1(A7)) < 1e-6            # angolo retto in A: il centro della rotazione e' A1
print("squadretta: C =", tuple(round(x, 1) for x in C7))

f = Figura(620, 470, 130, "La squadretta appoggiata con il lato AB su π₁: l'asse è il lato stesso", x0=0)
f.lt(10, 600)
f.traccia(K, lungo(K, d1, 520)); f.testo(lungo(K, d1, 520), "t_1α", -36, 4)
f.figura([P2(A7), P2(B7), P2(C7)], "blu")
f.figura([P1(A7), P1(B7), P1(C7)], "blu")
for p_ in (A7, B7, C7):
    f.richiamo(p_[0], P2(p_)[1], P1(p_)[1])
g7 = unit((Cst7[0] - H7[0], Cst7[1] - H7[1]))
f.retta(lungo(c17, g7, -35), lungo(H7, g7, r7 + 30), "verde", 1.8)
f.testo(lungo(H7, g7, r7 + 30), "t_1γ", -34, 6, "verde")
f.angolo_retto(H7, d1, (-g7[0], -g7[1]))
f.costruzione(c17, Cbar7)
tacche(f, (C7[0], 0), P2(C7), 2)
tacche(f, c17, Cbar7, 2)
f.retta(H7, Cbar7, "verde", 1.4)
arco_tra(f, H7, Cbar7, Cst7, colore="grigio", spessore=1, tratteggio="4,3")
f.figura([P1(A7), P1(B7), Cst7], "rosso")
f.punto(P2(A7), "A₂", -10, 18, "blu"); f.punto(P2(B7), "B₂", 0, 18, "blu"); f.punto(P2(C7), "C₂", -6, -8, "blu")
f.punto(P1(A7), "A₁ ≡ A* ≡ H", -104, 0, "blu"); f.punto(P1(B7), "B₁ ≡ B*", 10, -2, "blu")
f.punto(P1(C7), "C₁", 8, -6, "blu")
f.punto(Cbar7, "C̄", 6, -4, "verde")
f.punto(Cst7, "C*", -28, 6, "rosso")
nota_righe(f, 420, ["A e B stanno su π₁: A₂ e B₂ sono sulla LT e A₁B₁ sta sulla prima traccia: è l'asse di rotazione.",
                    "Si ribalta solo C: t₁γ ⊥ t₁α per C₁, C̄ con la quota di C (due lineette), centro H, raggio HC̄.",
                    "A*B*C* è la squadretta in vera forma: angolo retto in A, 30° in B, 60° in C (misure scelte qui)."])
f.salva(OUT + "b09-squadretta-foglio.svg")

f, t = triedro("Nello spazio: la squadretta appoggiata su π₁ con il lato AB", h=490, Y=220,
               X3=400, U=370, Z=150, origine=(360, 170), scala=0.9)
t.tracce(n_a, d_a, "grigio")
t._poligono([A7, B7, C7], "blu", 0.35, "blu")
t.richiamo(C7, S1(P1(C7)))
t._poligono([A7, B7, S1(Cst7)], "rosso", 0.20, "rosso")
arco_spazio(t, A7, C7, S1(Cst7), "rosso", 1.4)
t.punto(A7, "A ≡ A*", -50, 22, "blu"); t.punto(B7, "B ≡ B*", 4, 20, "blu")
t.punto(C7, "C", 6, -6, "blu"); t.punto(S1(P1(C7)), "C₁", -24, 4); t.punto(S1(Cst7), "C*", -6, 20, "rosso")
f.nota(20, 456, "Il lato AB sta già su π₁: è la cerniera. A e B non si muovono; si ribalta solo C.")
f.nota(20, 473, "C ruota intorno ad AB (arco rosso) e arriva in C*: A*B*C* è la squadretta in vera forma.")
f.salva(OUT + "b09-spazio-squadretta.svg")

# =========================================================================================
# PROPOSTO: lo sviluppo della piramide a base quadrata appoggiata su pi1
# =========================================================================================
lq, hp = 90.0, 120.0                       # lato della base, altezza della piramide
cx, cy = 250.0, 215.0                       # centro della base (x, aggetto)
rot = math.radians(25)                      # base ruotata di 25 gradi rispetto alla LT
ux, uy = (math.cos(rot), math.sin(rot)), (-math.sin(rot), math.cos(rot))
base = []
for sx, sy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:      # il lato DE e' quello davanti
    base.append((cx + (sx * ux[0] + sy * uy[0]) * lq / 2, cy + (sx * ux[1] + sy * uy[1]) * lq / 2, 0))
V = (cx, cy, hp)
NB = ["D", "E", "F", "G"]
# ribaltamento di ogni faccia intorno al suo lato di base, verso l'esterno della base
facce = []
for i in range(4):
    P, Q = base[i], base[(i + 1) % 4]
    a, b = P1(P), P1(Q)
    verso_f = -lato(P1(V), a, b)            # V* dalla parte opposta al centro della base
    v1, Hf, Vbar, rf, Vst = costruzione_docente(V, a, b, 0, verso_f)
    assert math.dist(Vst, ribalta_3d(V, a, b, 0, verso_f)) < 1e-6
    controlla(f"faccia {NB[i]}{NB[(i + 1) % 4]}V", [P, Q, V], [a, b, Vst])
    facce.append((a, b, Hf, Vbar, rf, Vst))
apot = math.hypot(lq / 2, hp)
print("apotema", round(apot, 2))

# --- sul foglio ---
f = Figura(620, 650, 150, "Proposto: lo sviluppo della piramide sul foglio", x0=60)
f.lt(-50, 550)
v2 = P2(V)
for p in base:
    f.richiamo(p[0], 0, P1(p)[1])
f.richiamo(V[0], v2[1], P1(V)[1])
# seconda proiezione: spigoli dal vertice ai quattro angoli
for p in base:
    f.retta(P2(p), v2, "blu", 1.4)
f.retta((min(p[0] for p in base), 0), (max(p[0] for p in base), 0), "blu", 2)
tacche(f, (V[0], 0), v2, 2, t=0.4)
f.punto(v2, "V₂", 6, -6, "blu")
# sviluppo: base + quattro facce ribaltate
for (a, b, Hf, Vbar, rf, Vst) in facce:
    f.figura([a, b, Vst], "rosso")
f.figura([P1(p) for p in base], "blu")
for p in base:
    f.retta(P1(p), P1(V), "blu", 1)
# costruzione completa solo per la prima faccia
a, b, Hf, Vbar, rf, Vst = facce[0]
gf = unit((Vst[0] - Hf[0], Vst[1] - Hf[1]))
f.retta(lungo(P1(V), gf, -30), lungo(Hf, gf, rf + 25), "verde", 1.6)
f.testo(lungo(Hf, gf, rf * 0.45), "t_1γ", 8, 4, "verde", 13)
f.costruzione(P1(V), Vbar)
tacche(f, P1(V), Vbar, 2)
f.retta(Hf, Vbar, "verde", 1.3)
arco_tra(f, Hf, Vbar, Vst, colore="grigio", spessore=1, tratteggio="4,3")
f.punto(Vbar, "V̄", -18, -6, "verde")
de = unit((b[0] - a[0], b[1] - a[1]))
f.punto(Hf, "H", 14 * de[0] - 4, -14 * de[1] + 14)
f.punto(P1(V), "V₁", 6, 14, "blu")
def fuori(p, c, k=16):
    d = unit((p[0] - c[0], p[1] - c[1]))
    return (k * d[0] - 8, -k * d[1] + 5)


for (a_, b_, Hf_, Vbar_, rf_, Vst_) in facce:
    f.punto(Vst_, "V*", *fuori(Vst_, P1(V)), "rosso")
for i, p in enumerate(base):
    f.punto(P1(p), NB[i] + "₁", *fuori(P1(p), P1(V), 18), "blu")
nota_righe(f, 585, ["Ogni faccia ha il lato di base su π₁, come la squadretta: si ribalta solo V, intorno a quel lato.",
                    "Per la faccia DE: t₁γ ⊥ DE per V₁; V̄ con l'altezza h (due lineette); centro H, raggio HV̄: V*.",
                    "Facendo lo stesso per le altre facce, verso l'esterno, si ottiene lo sviluppo: base + 4 facce.",
                    "(Schema proposto: le misure della piramide sono scelte qui.)"])
f.salva(OUT + "b09-sviluppo-piramide.svg")

# --- nello spazio: la faccia DEV si abbatte su pi1 ---
f, t = triedro("Proposto, nello spazio: la faccia DEV si abbatte su π₁ intorno a DE", h=480, Y=420, Z=150,
               X3=340, U=220, origine=(230, 150), scala=0.85)
a, b, Hf, Vbar, rf, Vst = facce[0]
for i in range(4):
    t.segmento(base[i], base[(i + 1) % 4], "blu", 1.6)
    t.segmento(base[i], V, "blu", 1.2)
t._poligono([base[0], base[1], V], "blu", 0.30, "blu")
t._poligono([base[0], base[1], S1(Vst)], "rosso", 0.22, "rosso")
Hf3 = S1(Hf)
arco_spazio(t, Hf3, V, S1(Vst), "rosso", 1.4)
t.richiamo(V, S1(P1(V)))
t.segmento(Hf3, V, "verde", 1.2)
t.segmento(Hf3, S1(P1(V)), "verde", 1.0)
t.punto(V, "V", 6, -6, "blu"); t.punto(S1(P1(V)), "V₁", 8, 4)
t.punto(base[0], "D", 8, 6, "blu"); t.punto(base[1], "E", -16, 16, "blu")
t.punto(Hf3, "H", -4, 18); t.punto(S1(Vst), "V*", 6, 14, "rosso")
f.nota(20, 446, "La faccia DEV ruota intorno al lato DE, che sta su π₁: V descrive un arco su un piano verticale")
f.nota(20, 463, "perpendicolare a DE, con centro H. Il triangolo HV₁V è il triangolo di rotazione.")
f.salva(OUT + "b09-spazio-piramide.svg")
print("ok")
