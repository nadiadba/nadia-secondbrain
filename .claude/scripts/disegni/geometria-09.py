"""Schemi per la sbobina di geometria descrittiva del 29 ottobre (09-...): il ribaltamento
del piano generico, in forma canonica (con la prima traccia) e in forma tecnica (con
un'orizzontale del piano, senza linea di terra).

Usa disegni_monge.py senza modificarlo. Ogni punto ribaltato viene calcolato due volte:
con la costruzione della docente (piano gamma perpendicolare, ribaltamento laterale,
triangolo di rotazione, affinita') e con la rotazione vera nello spazio; lo script
controlla che i due risultati coincidano e che la figura ribaltata abbia le misure vere.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


# ---------- funzioni di servizio (come in geometria-07.py) ----------

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
    """Piede della perpendicolare da p alla retta ab (coordinate di disegno)."""
    d = unit((b[0] - a[0], b[1] - a[1]))
    t = (p[0] - a[0]) * d[0] + (p[1] - a[1]) * d[1]
    return (a[0] + d[0] * t, a[1] + d[1] * t)


def lato(p, a, b):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def ribalta_3d(P, a, b, quota_asse, verso):
    """Ribaltamento vero: il punto P (3D) ruota intorno all'orizzontale del piano che ha
    prima proiezione ab (coordinate di disegno) e quota quota_asse, fino al piano
    orizzontale a quella quota. verso = segno del lato di ab dove deve cadere P*.
    Restituisce P* in coordinate di disegno (sul foglio della prima proiezione)."""
    p1 = P1(P)
    H = piede(p1, a, b)
    r = math.sqrt(math.dist(p1, H) ** 2 + (P[2] - quota_asse) ** 2)
    n = unit((-(b[1] - a[1]), b[0] - a[0]))
    if lato(lungo(H, n, 1), a, b) * verso < 0:
        n = (-n[0], -n[1])
    return lungo(H, n, r)


def costruzione_docente(P, a, b, quota_asse, verso):
    """La costruzione della docente, passo per passo, in coordinate di disegno:
    gamma1 perpendicolare ad ab per P1; P barrato (ribaltamento laterale di gamma, con la
    quota di P misurata dal piano dell'asse); centro H = gamma1 ∩ asse; raggio H-Pbarrato
    riportato su gamma1 dalla parte 'verso'."""
    p1 = P1(P)
    H = piede(p1, a, b)
    dasse = unit((b[0] - a[0], b[1] - a[1]))
    q = P[2] - quota_asse
    Pbar = lungo(p1, dasse, q)               # ribaltamento laterale: perpendicolare a gamma1
    r = math.dist(H, Pbar)                  # raggio di rotazione (ipotenusa)
    g = unit((p1[0] - H[0], p1[1] - H[1]))
    if lato(lungo(H, g, 1), a, b) * verso < 0:
        g = (-g[0], -g[1])
    Pstar = lungo(H, g, r)
    return p1, H, Pbar, r, Pstar


def affine(Q1, asse_a, asse_b, P1p, Pstar):
    """Affinita' ortogonale di asse ab: corrispondente di Q1 sapendo P1 -> P*."""
    U = interseca(P1p, Q1, asse_a, asse_b)          # la retta P1Q1 incontra l'asse in U
    H = piede(Q1, asse_a, asse_b)
    return interseca(U, Pstar, Q1, H), U


def controlla(nome, veri, trovati):
    for i in range(3):
        a, b = math.dist(veri[i], veri[(i + 1) % 3]), math.dist(trovati[i], trovati[(i + 1) % 3])
        assert abs(a - b) < 1e-6, (nome, a, b)
    print(f"{nome}: misure vere ok")


# ---------- il piano generico alfa ----------
K3 = (40, 0, 0)
n_a, d_a = piano(K3, (440, 220, 0), (440, 0, 200))


def su_alfa(x, y):
    return (x, y, (d_a - n_a[0] * x - n_a[1] * y) / n_a[2])


_dt = (400 / math.hypot(400, 220), 220 / math.hypot(400, 220), 0)      # direzione di t1alfa
_w = (n_a[1] * _dt[2] - n_a[2] * _dt[1], n_a[2] * _dt[0] - n_a[0] * _dt[2], n_a[0] * _dt[1] - n_a[1] * _dt[0])
_lw = math.sqrt(sum(x * x for x in _w))
_w = tuple(x / _lw for x in _w)
if _w[2] < 0:
    _w = tuple(-x for x in _w)


def in_alfa(s, h):
    """Punto di alfa a distanza s da K lungo t1alfa e h da t1alfa (misure vere nel piano)."""
    return tuple(K3[i] + s * _dt[i] + h * _w[i] for i in range(3))


K = (40, 0)
T1A = (440, -220)          # fine di t1alfa nel disegno
T2A = (440, 200)           # fine di t2alfa nel disegno

# =========================================================================================
# 1. Le orizzontali del piano scendono fino alla prima traccia
# =========================================================================================
f = Figura(620, 500, 225, "Le orizzontali di α: più scendono, più o₁ si avvicina a t₁α", x0=40)
f.lt(-20, 560)
f.traccia(K, T2A); f.testo(T2A, "t_2α", 4, 4)
f.traccia(K, T1A); f.testo(T1A, "t_1α ≡ o₁ a quota 0", 10, 4)
d1 = unit((T1A[0] - K[0], T1A[1] - K[1]))
for (h, col) in [(160, "verde"), (120, "arancio"), (60, "viola")]:
    x2 = interseca(K, T2A, (0, h), (1, h))[0]     # T2o sulla seconda traccia
    f.retta((x2, h), (540, h), col)
    f.testo((540, h), "o₂", -4, -8, col)
    fine = lungo((x2, 0), d1, min(330, (530 - x2) / d1[0]))
    f.retta((x2, 0), fine, col)
    f.richiamo(x2, h, 0)
    f.punto((x2, h), None)
    f.punto((x2, 0), None)
    f.testo(fine, "o₁", 8, 4, col)
    f.testo((x2, h), f"quota {h}", -70, -6, col, 12, False)
nota_righe(f, 472, ["Ogni orizzontale ha o₂ parallela alla LT e o₁ parallela a t₁α. Quando la quota arriva a zero",
                    "l'orizzontale sta su π₁ e coincide con la prima traccia: t₁α è l'orizzontale a quota zero."])
f.salva(OUT + "09-orizzontali-fino-alla-traccia.svg")


# =========================================================================================
# 2. Nello spazio: le orizzontali del piano generico
# =========================================================================================
def triedro(titolo, h=500, w=620, origine=(270, 200), scala=0.75):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, origine, X3=400, U=360, Y=230, Z=220, scala=scala)
    t.piani()
    return f, t


f, t = triedro("Nello spazio: le orizzontali di α, fino a quella a quota zero (t₁α)")
t.piano(n_a, d_a, "blu", 0.14)
t.tracce(n_a, d_a, "nero", "α")
for h, col in [(160, "verde"), (120, "arancio"), (60, "viola")]:
    # orizzontale a quota h: da t2alfa (y=0) a t3alfa (x=400)
    xa = 40 + h * 400 / 200
    a = (xa, 0, h)
    yb = (d_a - n_a[0] * 400 - n_a[2] * h) / n_a[1]
    b = (400, yb, h)
    t.segmento(a, b, col, 2)
    t.richiamo(a, (a[0], a[1], 0)); t.richiamo(b, (b[0], b[1], 0))
    t.segmento((a[0], a[1], 0), (b[0], b[1], 0), col, 1, "4,3")
nota_righe(f, 470, ["Le orizzontali sono parallele tra loro e a π₁; le loro prime proiezioni (tratteggiate)",
                    "sono parallele a t₁α. Scendendo, l'ultima orizzontale è la prima traccia stessa."])
f.salva(OUT + "09-spazio-orizzontali-del-piano.svg")

# =========================================================================================
# 3. Il triangolo con C su pi1: la prima traccia del piano dalle tracce delle rette
# =========================================================================================
A = in_alfa(260, 30)
B = in_alfa(330, 140)
C = in_alfa(110, 0)
assert abs(C[2]) < 1e-9
print("quote: A", round(A[2], 1), "B", round(B[2], 1), "C", round(C[2], 1))
f = Figura(640, 500, 215, "Triangolo ABC con C su π₁: la prima traccia del piano", x0=30)
f.lt(-10, 590)
f.figura([P2(A), P2(B), P2(C)], "blu")
f.figura([P1(A), P1(B), P1(C)], "blu")
for p in (A, B, C):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
# retta s = AB: prima traccia
s2a, s2b = P2(A), P2(B)
Ts2 = interseca(s2a, s2b, (0, 0), (1, 0))      # (T1s)2 sulla LT
Ts1 = interseca(P1(A), P1(B), (Ts2[0], 0), (Ts2[0], -1))
f.retta(P2(B), Ts2, "arancio", 1.2)
f.retta(P1(B), Ts1, "arancio", 1.2)
f.richiamo(Ts2[0], 0, Ts1[1])
f.punto(Ts2, "(T_{1s})₂", -62, 20, "arancio")
f.punto(Ts1, "T_{1s}", -34, 14, "arancio")
f.testo(lungo(P2(A), unit((s2b[0]-s2a[0], s2b[1]-s2a[1])), 60), "s₂", -4, -10, "arancio")
f.testo(lungo(P1(A), unit((P1(B)[0]-P1(A)[0], P1(B)[1]-P1(A)[1])), 60), "s₁", 0, 16, "arancio")
# la prima traccia: per C1 (= T1r) e T1s
f.traccia(K, lungo(K, d1, 430)); f.testo(lungo(K, d1, 430), "t_1α", 6, 10)
assert abs(lato(Ts1, K, T1A)) < 1e-6
for p, n_, e2, e1 in [(A, "A", (-10, -10), (-10, 20)), (B, "B", (8, -6), (8, 6)), (C, "C", (-6, 20), (-18, 22))]:
    f.punto(P2(p), n_ + "₂", *e2, "blu")
    f.punto(P1(p), n_ + "₁", *e1, "blu")
f.testo(P1(C), "≡ T_{1r}", 2, 22, "rosso", 13)
f.testo(P2(C), "r₂ ≡ B₂C₂", 110, -78, "grigio", 12, False)
nota_righe(f, 460, ["C sta su π₁: C₂ è sulla LT e C₁ è già la prima traccia della retta r = BC.",
                    "Con la prima traccia di un'altra retta (s = AB) si hanno i due punti che bastano per t₁α.",
                    "La seconda traccia del piano non serve."])
f.salva(OUT + "09-triangolo-prima-traccia.svg")

# =========================================================================================
# 4. Ribaltamento in forma canonica: piano gamma, B barrato, raggio di rotazione, affinita'
# =========================================================================================
verso = -lato(P1(B), K, T1A)            # P* dalla parte opposta alla prima proiezione
b1, H, Bbar, r, Bst = costruzione_docente(B, K, T1A, 0, verso)
assert math.dist(Bst, ribalta_3d(B, K, T1A, 0, verso)) < 1e-6
Ast, U = affine(P1(A), K, T1A, P1(B), Bst)
assert math.dist(Ast, ribalta_3d(A, K, T1A, 0, verso)) < 1e-6
Cst = P1(C)
controlla("ribaltamento forma canonica", [A, B, C], [Ast, Bst, Cst])

f = Figura(680, 610, 165, "Ribaltamento del piano generico α su π₁ (forma canonica, con t₁α)", x0=20)
f.lt(0, 660)
f.traccia(K, lungo(K, d1, 620)); f.testo(lungo(K, d1, 620), "t_1α", -36, 4)
f.figura([P2(A), P2(B), P2(C)], "blu")
f.figura([P1(A), P1(B), P1(C)], "blu")
for p in (A, B, C):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
# gamma: t1gamma perpendicolare a t1alfa per B1
g = unit((Bst[0] - H[0], Bst[1] - H[1]))
fine_g = lungo(H, g, r + 40)
inizio_g = lungo(b1, g, -45)
f.traccia(inizio_g, fine_g, "verde")
f.testo(inizio_g, "t_1γ", 4, -6, "verde")
f.angolo_retto(H, d1, g)
# ribaltamento laterale: quota di B riportata da B1, perpendicolare a t1gamma
f.costruzione(b1, Bbar)
tacche(f, (B[0], 0), P2(B), 2)
tacche(f, b1, Bbar, 2)
f.angolo_retto(b1, d1, (-g[0], -g[1]))
f.retta(H, Bbar, "verde", 1.4)              # raggio di rotazione
arco(f, H, r, angolo(H, Bbar), angolo(H, Bst) + (360 if angolo(H, Bst) < angolo(H, Bbar) - 180 else 0), "grigio", 1, "4,3")
# affinita': retta A1B1 fino all'asse in U, poi U-B*; perpendicolare all'asse da A1
f.costruzione(P1(B), U)
f.costruzione(U, Ast)
f.costruzione(P1(A), Ast)
f.figura([Ast, Bst, Cst], "rosso")
for p, n_, e2, e1 in [(A, "A", (-10, -10), (8, 4)), (B, "B", (8, -6), (8, 0)), (C, "C", (-6, 20), (6, -10))]:
    f.punto(P2(p), n_ + "₂", *e2, "blu")
    f.punto(P1(p), n_ + "₁", *e1, "blu")
f.punto(Bbar, "B̄", 6, -4, "verde")
f.punto(H, "H", 8, -4)
f.punto(U, "U", -6, 18)
f.punto(Ast, "A*", -28, 6, "rosso")
f.punto(Bst, "B*", 8, 10, "rosso")
f.testo(Cst, "≡ C*", -40, 30, "rosso", 13)
nota_righe(f, 520, ["1. t₁γ ⊥ t₁α per B₁ (γ è proiettante in prima e perpendicolare ad α); H = t₁γ ∩ t₁α.",
                    "2. Ribaltamento laterale di γ: da B₁, perpendicolare a t₁γ, la quota di B (due lineette): B̄.",
                    "3. HB̄ è il raggio di rotazione: centro in H, lo si riporta su t₁γ e si trova B*.",
                    "4. Affinità di asse t₁α: la retta A₁B₁ incontra l'asse in U; U-B* incontra in A* la",
                    "    perpendicolare all'asse condotta da A₁. C sta sull'asse e non si muove: C* ≡ C₁."])
f.salva(OUT + "09-ribaltamento-piano-generico-tracce.svg")

# =========================================================================================
# 5. Nello spazio: il ribaltamento del piano generico intorno a t1alfa
# =========================================================================================
f, t = triedro("Nello spazio: il piano γ ⊥ α per B e la rotazione di B intorno a t₁α",
               h=520, origine=(300, 190), scala=0.72)
t.piano(n_a, d_a, "blu", 0.12)
t.tracce(n_a, d_a, "nero", "α")
# gamma: piano verticale per B, perpendicolare a t1alfa
Hs = (H[0], -H[1], 0)
dir_t1 = (d1[0], -d1[1], 0)                      # direzione di t1alfa nello spazio
n_g = dir_t1
d_g = sum(n_g[i] * B[i] for i in range(3))
t.piano(n_g, d_g, "verde", 0.12)
# punti ribaltati nello spazio (su pi1)
def S1(p):
    return (p[0], -p[1], 0)
Ast3, Bst3, Cst3 = S1(Ast), S1(Bst), S1(Cst)
# arco di B in gamma: da B a B*, centro Hs
e1 = [B[i] - Hs[i] for i in range(3)]
r3 = math.sqrt(sum(x * x for x in e1))
e1 = [x / r3 for x in e1]
v = [Bst3[i] - Hs[i] for i in range(3)]
dot = sum(v[i] * e1[i] for i in range(3))
e2 = [v[i] - dot * e1[i] for i in range(3)]
l2 = math.sqrt(sum(x * x for x in e2)); e2 = [x / l2 for x in e2]
amax = math.degrees(math.atan2(sum(v[i] * e2[i] for i in range(3)), dot))
pts = []
for i in range(41):
    a = math.radians(amax * i / 40)
    pts.append(t._p(tuple(Hs[j] + r3 * (math.cos(a) * e1[j] + math.sin(a) * e2[j]) for j in range(3))))
f.parti.append('<path d="M ' + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) +
               f'" fill="none" stroke="{COLORI["rosso"]}" stroke-width="1.4" stroke-dasharray="5,3"/>')
t.segmento(Hs, B, "verde", 1.4)
t.segmento(Hs, S1(b1), "verde", 1.2)
t.richiamo(B, S1(b1))
t.richiamo(A, S1(P1(A)))
t._poligono([A, B, C], "blu", 0.35, "blu")
t._poligono([S1(P1(A)), S1(P1(B)), S1(P1(C))], "blu", 0.10, "blu")
t._poligono([Ast3, Bst3, Cst3], "rosso", 0.2, "rosso")
t.punto(A, "A", -16, -6, "blu"); t.punto(B, "B", 6, -6, "blu"); t.punto(C, "C ≡ C*", -30, 26, "blu")
t.punto(S1(b1), "B₁", 6, 14); t.punto(Hs, "H", -18, 4)
t.punto(Ast3, "A*", -24, 14, "rosso"); t.punto(Bst3, "B*", -10, 18, "rosso")
t.testo((400, 230, 40), "γ", -40, 0, "verde")
nota_righe(f, 490, ["B ruota intorno a t₁α lungo un arco che sta sul piano γ, perpendicolare ad α e a t₁α:",
                    "il centro è H e il raggio è HB. C sta su π₁ e non si muove. A*B*C* è la vera forma."])
f.salva(OUT + "09-spazio-ribaltamento-piano-generico.svg")

# =========================================================================================
# 6. Forma tecnica: ribaltamento intorno a un'orizzontale per C, senza linea di terra
# =========================================================================================
A6 = in_alfa(300, 90)
B6 = in_alfa(360, 200)
C6 = in_alfa(150, 50)
qo = C6[2]
print("forma tecnica: quote A", round(A6[2], 1), "B", round(B6[2], 1), "C", round(C6[2], 1))
f = Figura(640, 620, 200, "Forma tecnica: ribaltamento intorno all'orizzontale o per C (senza LT)", x0=-80)
f.figura([P2(A6), P2(B6), P2(C6)], "blu")
f.figura([P1(A6), P1(B6), P1(C6)], "blu")
for p in (A6, B6, C6):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
# o2 per C2, parallela alla "LT" (orizzontale nel foglio)
o2a, o2b = (P2(C6)[0] - 60, qo), (P2(B6)[0] + 80, qo)
f.retta(o2a, o2b, "arancio", 1.8); f.testo(o2b, "o₂", 4, 4, "arancio")
# r = AB: M2 = r2 ∩ o2
M2 = interseca(P2(A6), P2(B6), o2a, o2b)
f.retta(P2(A6), M2, "grigio", 1)
M1 = interseca(P1(A6), P1(B6), (M2[0], 0), (M2[0], -1))
f.retta(P1(A6), M1, "grigio", 1)
f.richiamo(M2[0], M2[1], M1[1])
# o1 per C1 e M1
do = unit((M1[0] - P1(C6)[0], M1[1] - P1(C6)[1]))
oa, ob = lungo(P1(C6), do, -70), lungo(P1(C6), do, 430)
f.retta(oa, ob, "arancio", 1.8); f.testo(ob, "o₁", -6, 18, "arancio")
assert abs(do[0] * d1[1] - do[1] * d1[0]) < 1e-9
if do[0] < 0:
    do = (-do[0], -do[1])
    # o1 parallela a t1alfa
verso6 = -lato(P1(B6), oa, ob)
b1, H6, Bbar6, r6, Bst6 = costruzione_docente(B6, oa, ob, qo, verso6)
assert math.dist(Bst6, ribalta_3d(B6, oa, ob, qo, verso6)) < 1e-6
Ast6, U6 = affine(P1(A6), oa, ob, P1(B6), Bst6)
assert math.dist(Ast6, ribalta_3d(A6, oa, ob, qo, verso6)) < 1e-6
Cst6 = P1(C6)
controlla("ribaltamento forma tecnica", [A6, B6, C6], [Ast6, Bst6, Cst6])
g6 = unit((Bst6[0] - H6[0], Bst6[1] - H6[1]))
f.retta(lungo(b1, g6, -40), lungo(H6, g6, r6 + 35), "verde", 1.8)
f.testo(lungo(b1, g6, -40), "γ₁", 6, -2, "verde")
f.angolo_retto(H6, do, g6)
f.costruzione(b1, Bbar6)
f.costruzione(P2(B6), (P2(B6)[0], qo))
tacche(f, (P2(B6)[0], qo), P2(B6), 2)
tacche(f, b1, Bbar6, 2)
f.retta(H6, Bbar6, "verde", 1.4)
a0, a1 = angolo(H6, Bbar6), angolo(H6, Bst6)
if a1 < a0 - 180:
    a1 += 360
arco(f, H6, r6, a0, a1, "grigio", 1, "4,3")
f.costruzione(P1(B6), U6); f.costruzione(U6, Ast6); f.costruzione(P1(A6), Ast6)
f.figura([Ast6, Bst6, Cst6], "rosso")
for p, n_, e2, e1 in [(A6, "A", (-8, -10), (8, 4)), (B6, "B", (8, -6), (8, 0)), (C6, "C", (-24, -8), (-10, -10))]:
    f.punto(P2(p), n_ + "₂", *e2, "blu")
    f.punto(P1(p), n_ + "₁", *e1, "blu")
f.punto(M2, "M₂", -8, 18, "grigio"); f.punto(M1, "M₁", -30, -6, "nero")
mA2 = ((P2(A6)[0] + P2(B6)[0]) / 2, (P2(A6)[1] + P2(B6)[1]) / 2)
mA1 = ((P1(A6)[0] + P1(B6)[0]) / 2, (P1(A6)[1] + P1(B6)[1]) / 2)
f.testo(mA2, "r₂", 8, 8, "grigio", 13)
f.testo(mA1, "r₁", 0, 18, "grigio", 13)
assert math.dist(U6, M1) < 1e-6          # M1 e' proprio il punto in cui r1 incontra l'asse
f.punto(Bbar6, "B̄", 6, -4, "verde"); f.punto(H6, "H", 6, -6)
f.punto(Ast6, "A*", -28, 6, "rosso"); f.punto(Bst6, "B*", 8, 12, "rosso")
f.testo(Cst6, "≡ C*", -36, 28, "rosso", 13)
nota_righe(f, 535, ["1. o₂ per C₂, orizzontale; r = AB: r₂ incontra o₂ in M₂; M₁ sta su r₁, sulla linea di richiamo.",
                    "2. o₁ passa per C₁ e M₁: è l'asse di rotazione (parallela a t₁α, ma la traccia non serve).",
                    "3. γ₁ ⊥ o₁ per B₁; B̄: da B₁ si riporta la distanza di B₂ da o₂ (non dalla LT).",
                    "4. Centro H, raggio HB̄: B* su γ₁. Affinità di asse o₁: r₁ incontra l'asse in M₁; M₁-B* incontra",
                    "    in A* la perpendicolare a o₁ da A₁. C sta sull'asse e non si muove: C* ≡ C₁."])
f.salva(OUT + "09-ribaltamento-intorno-a-orizzontale.svg")

# =========================================================================================
# 7. La squadretta da 60 appoggiata con un lato su pi1: l'asse e' il lato stesso
# =========================================================================================
# A e B su t1alfa; la vera forma e' un triangolo 30-60-90 (la squadretta)
sA, sB = 90.0, 250.0                  # distanze lungo t1alfa da K
L = sB - sA
A7 = (K3[0] + d1[0] * sA, -d1[1] * sA, 0)
B7 = (K3[0] + d1[0] * sB, -d1[1] * sB, 0)
# C: angolo retto in A, cateto AC = L*tan(30) nel piano alfa, perpendicolare a t1alfa
# direzione in alfa perpendicolare a t1alfa, verso l'alto
n_ = n_a
dt = (d1[0], -d1[1], 0)
w = (n_[1] * dt[2] - n_[2] * dt[1], n_[2] * dt[0] - n_[0] * dt[2], n_[0] * dt[1] - n_[1] * dt[0])
lw = math.sqrt(sum(x * x for x in w)); w = tuple(x / lw for x in w)
if w[2] < 0:
    w = tuple(-x for x in w)
AC = L * math.tan(math.radians(30))
C7 = tuple(A7[i] + AC * w[i] for i in range(3))
verso7 = -lato(P1(C7), K, T1A)
c1, H7, Cbar7, r7, Cst7 = costruzione_docente(C7, K, T1A, 0, verso7)
assert math.dist(Cst7, ribalta_3d(C7, K, T1A, 0, verso7)) < 1e-6
controlla("squadretta", [A7, B7, C7], [P1(A7), P1(B7), Cst7])
ang = math.degrees(math.acos(((P1(B7)[0]-P1(A7)[0])*(Cst7[0]-P1(A7)[0]) + (P1(B7)[1]-P1(A7)[1])*(Cst7[1]-P1(A7)[1])) /
                             (math.dist(P1(A7), P1(B7)) * math.dist(P1(A7), Cst7))))
print("angolo in A* =", round(ang, 3))
f = Figura(620, 500, 175, "La squadretta appoggiata con il lato AB su π₁: l'asse è il lato stesso", x0=30)
f.lt(-10, 570)
f.traccia(K, lungo(K, d1, 500)); f.testo(lungo(K, d1, 500), "t_1α", -36, 4)
f.figura([P2(A7), P2(B7), P2(C7)], "blu")
f.figura([P1(A7), P1(B7), P1(C7)], "blu")
for p in (A7, B7, C7):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
g7 = unit((Cst7[0] - H7[0], Cst7[1] - H7[1]))
f.retta(lungo(c1, g7, -30), lungo(H7, g7, r7 + 30), "verde", 1.8)
f.testo(lungo(H7, g7, r7 + 30), "t_1γ", -30, 4, "verde")
f.costruzione(c1, Cbar7)
tacche(f, (C7[0], 0), P2(C7), 2)
tacche(f, c1, Cbar7, 2)
f.retta(H7, Cbar7, "verde", 1.4)
a0, a1 = angolo(H7, Cbar7), angolo(H7, Cst7)
if a1 < a0 - 180:
    a1 += 360
if a1 > a0 + 180:
    a1 -= 360
arco(f, H7, r7, a0, a1, "grigio", 1, "4,3")
f.figura([P1(A7), P1(B7), Cst7], "rosso")
f.punto(P2(A7), "A₂", -10, 18, "blu"); f.punto(P2(B7), "B₂", 0, 18, "blu"); f.punto(P2(C7), "C₂", -6, -8, "blu")
f.punto(P1(A7), "A₁ ≡ A* ≡ H", -104, -2, "blu"); f.punto(P1(B7), "B₁ ≡ B*", 10, -2, "blu"); f.punto(P1(C7), "C₁", 8, -6, "blu")
f.punto(Cbar7, "C̄", 6, -4, "verde")
assert math.dist(H7, P1(A7)) < 1e-6      # l'angolo retto in A: il centro della rotazione e' A1
f.punto(Cst7, "C*", -28, 6, "rosso")
nota_righe(f, 450, ["A e B stanno su π₁: A₂ e B₂ sono sulla LT, A₁B₁ sta sulla prima traccia ed è l'asse di rotazione.",
                    "Si ribalta solo C (stessa costruzione: γ, C̄ con la quota di C, raggio HC̄): A*B*C* è la",
                    "squadretta in vera forma: angolo retto in A, 30° in B, 60° in C."])
f.salva(OUT + "09-squadretta-con-un-lato-su-pi1.svg")
print("ok")
