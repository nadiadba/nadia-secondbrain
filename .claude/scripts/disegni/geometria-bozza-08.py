"""Schemi per la bozza di geometria descrittiva del 27 ottobre (08-...): le tracce del piano
o un'orizzontale per lavorare con una figura piana, il ribaltamento del punto P di un piano
generico, e perche' conviene ribaltare il punto piu' lontano dall'asse.

Usa disegni_monge.py senza modificarlo. Ogni punto ribaltato si calcola due volte: con la
costruzione della docente (piano gamma perpendicolare, ribaltamento laterale della quota,
raggio di rotazione) e con la rotazione vera nello spazio; lo script controlla che i
risultati coincidano e che la figura ribaltata abbia le misure vere.
Immagini in geometria-descrittiva/bozze/img/ con prefisso b08-.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, interseca, tracce_retta, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"


# ---------- funzioni di servizio (come in geometria-09.py) ----------

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


def arco_tra(f, c, p, q, colore="grigio"):
    a0, a1 = angolo(c, p), angolo(c, q)
    if a1 < a0 - 180:
        a1 += 360
    if a1 > a0 + 180:
        a1 -= 360
    arco(f, c, math.dist(c, p), a0, a1, colore, 1, "4,3")


def tacche(f, a, b, n, colore="nero", t=0.5):
    L = math.dist(a, b)
    d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    q = (-d[1], d[0])
    m = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        c = lungo(m, d, o)
        f._linea(lungo(c, q, -5), lungo(c, q, 5), colore, 1.3)


def nota_righe(f, y, righe, x=20):
    for i, r in enumerate(righe):
        f.nota(x, y + 17 * i, r)


def piede(p, a, b):
    d = unit((b[0] - a[0], b[1] - a[1]))
    t = (p[0] - a[0]) * d[0] + (p[1] - a[1]) * d[1]
    return (a[0] + d[0] * t, a[1] + d[1] * t)


def lato(p, a, b):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def ribalta_3d(P, a, b, verso):
    """Rotazione vera di P (3D) intorno alla prima traccia (prima proiezione ab, quota 0)."""
    p1 = P1(P)
    H = piede(p1, a, b)
    r = math.sqrt(math.dist(p1, H) ** 2 + P[2] ** 2)
    n = unit((-(b[1] - a[1]), b[0] - a[0]))
    if lato(lungo(H, n, 1), a, b) * verso < 0:
        n = (-n[0], -n[1])
    return lungo(H, n, r)


def costruzione_docente(P, a, b, verso):
    """t1gamma perpendicolare ad ab per P1; P barrato = ribaltamento laterale di gamma (la quota
    di P riportata da P1 perpendicolarmente a t1gamma); centro H; raggio H-Pbarrato su t1gamma."""
    p1 = P1(P)
    H = piede(p1, a, b)
    dasse = unit((b[0] - a[0], b[1] - a[1]))
    Pbar = lungo(p1, dasse, P[2])
    r = math.dist(H, Pbar)
    g = unit((p1[0] - H[0], p1[1] - H[1]))
    if lato(lungo(H, g, 1), a, b) * verso < 0:
        g = (-g[0], -g[1])
    return p1, H, Pbar, r, lungo(H, g, r)


def affine(Q1, asse_a, asse_b, P1p, Pstar):
    """Affinita' ortogonale di asse ab: corrispondente di Q1 sapendo P1 -> P*."""
    U = interseca(P1p, Q1, asse_a, asse_b)
    H = piede(Q1, asse_a, asse_b)
    return interseca(U, Pstar, Q1, H), U


def controlla(nome, veri, trovati):
    for i in range(3):
        a, b = math.dist(veri[i], veri[(i + 1) % 3]), math.dist(trovati[i], trovati[(i + 1) % 3])
        assert abs(a - b) < 1e-6, (nome, a, b)
    print(f"{nome}: misure vere ok")


# ---------- il piano generico alfa (lo stesso di geometria-09.py) ----------
K3 = (40, 0, 0)
n_a, d_a = piano(K3, (440, 220, 0), (440, 0, 200))
_dt = (400 / math.hypot(400, 220), 220 / math.hypot(400, 220), 0)
_w = (n_a[1] * _dt[2] - n_a[2] * _dt[1], n_a[2] * _dt[0] - n_a[0] * _dt[2], n_a[0] * _dt[1] - n_a[1] * _dt[0])
_lw = math.sqrt(sum(x * x for x in _w))
_w = tuple(x / _lw for x in _w)
if _w[2] < 0:
    _w = tuple(-x for x in _w)


def in_alfa(s, h):
    """Punto di alfa a distanza s da K lungo t1alfa e h da t1alfa (misure vere nel piano)."""
    return tuple(K3[i] + s * _dt[i] + h * _w[i] for i in range(3))


def su_alfa(p):
    return abs(sum(n_a[i] * p[i] for i in range(3)) - d_a) < 1e-6


K = (40, 0)
d1 = unit((400, -220))          # direzione di t1alfa nel disegno
T2A = (440, 200)


def triedro(titolo, h=500, w=620, origine=(270, 200), scala=0.75, Y=230):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, origine, X3=400, U=360, Y=Y, Z=220, scala=scala)
    t.piani()
    return f, t


def S1(p):
    """Punto del foglio della prima proiezione -> punto 3D su pi1."""
    return (p[0], -p[1], 0)


# il triangolo del disegno 1 (nello spazio, dentro il triedro)
A3, B3, C3 = in_alfa(380, 55), in_alfa(330, 185), in_alfa(200, 70)
for p in (A3, B3, C3):
    assert su_alfa(p) and p[2] > 0 and p[1] > 0 and p[0] < 400

# il triangolo dei disegni 2 e 5 (sul foglio)
A = in_alfa(470, 40)
B = in_alfa(300, 190)
C = in_alfa(170, 75)
for p in (A, B, C):
    assert su_alfa(p) and p[2] > 0 and p[1] > 0
print("triangolo: quote", [round(p[2], 1) for p in (A, B, C)], "aggetti", [round(p[1], 1) for p in (A, B, C)])

# =========================================================================================
# 1. Nello spazio: il piano che contiene la figura, la prima traccia e un'orizzontale
# =========================================================================================
f, t = triedro("Nello spazio: il triangolo ABC, il suo piano α, t₁α e l'orizzontale o per C", h=510)
t.piano(n_a, d_a, "blu", 0.12)
t.tracce(n_a, d_a, "nero", "α")
# orizzontale per C: da t2alfa (y=0) a t3alfa (x=400)
qC = C3[2]
oa = (40 + qC * 400 / 200, 0, qC)
ob = (400, (d_a - n_a[0] * 400 - n_a[2] * qC) / n_a[1], qC)
assert su_alfa(oa) and su_alfa(ob)
t.segmento(oa, ob, "arancio", 2.2)
t.segmento((oa[0], oa[1], 0), (ob[0], ob[1], 0), "arancio", 1.2, "5,3")
t.richiamo(oa, (oa[0], oa[1], 0)); t.richiamo(ob, (ob[0], ob[1], 0))
t._poligono([A3, B3, C3], "blu", 0.4, "blu")
t._poligono([S1(P1(A3)), S1(P1(B3)), S1(P1(C3))], "blu", 0.08, "blu")
for p in (A3, B3, C3):
    t.richiamo(p, (p[0], p[1], 0))
t.punto(A3, "A", 10, 6, "blu"); t.punto(B3, "B", -4, -10, "blu"); t.punto(C3, "C", -16, -6, "blu")
t.testo(ob, "o", 8, -10, "arancio")
t.testo((ob[0], ob[1], 0), "o₁", 6, 12, "arancio")
nota_righe(f, 470, ["Il piano α è esteso, la figura è solo una sua parte. L'orizzontale o sta in α alla quota di C;",
                    "la sua prima proiezione o₁ (tratteggiata) è parallela a t₁α, che è l'orizzontale a quota zero."])
f.salva(OUT + "b08-spazio-figura-orizzontale-e-traccia.svg")

# =========================================================================================
# 2. Sul foglio: le tracce del piano dalle rette dei lati, oppure un'orizzontale
# =========================================================================================
f = Figura(640, 560, 200, "Dalle due proiezioni del triangolo: t₁α con le tracce, oppure o₁", x0=10)
f.lt(10, 620)
f.figura([P2(A), P2(B), P2(C)], "blu")
f.figura([P1(A), P1(B), P1(C)], "blu")
for p in (A, B, C):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
# r = AB e s = BC: prime tracce
T1r, _ = tracce_retta(A, B)
T1s, _ = tracce_retta(B, C)
for T, a, b, nome, e2, e1 in [(T1r, A, B, "r", (-8, 20), (-40, 4)), (T1s, B, C, "s", (-36, 20), (-30, 18))]:
    t2 = (T[0], 0)
    t1 = P1(T)
    assert abs(lato(t1, K, lungo(K, d1, 100))) < 1e-6        # la traccia della retta sta su t1alfa
    vicino2 = min((P2(a), P2(b)), key=lambda q: math.dist(q, t2))
    vicino1 = min((P1(a), P1(b)), key=lambda q: math.dist(q, t1))
    f.retta(vicino2, t2, "verde", 1.2)
    f.retta(vicino1, t1, "verde", 1.2)
    f.richiamo(t2[0], 0, t1[1])
    f.punto(t2, f"(T_{{1{nome}}})₂", *e2, "verde")
    f.punto(t1, f"T_{{1{nome}}}", *e1, "verde")
fine_t1 = lungo(K, d1, 560)
f.traccia(K, fine_t1); f.testo(lungo(K, d1, 200), "t_1α", -36, 22)
# orizzontale per C: o2 parallela alla LT, M2 = o2 ∩ A2B2, M1 su A1B1
o2a, o2b = (P2(C)[0] - 50, C[2]), (P2(A)[0] + 60, C[2])
M2 = interseca(P2(A), P2(B), o2a, o2b)
M1 = interseca(P1(A), P1(B), (M2[0], 0), (M2[0], -1))
do = unit((M1[0] - P1(C)[0], M1[1] - P1(C)[1]))
assert abs(do[0] * d1[1] - do[1] * d1[0]) < 1e-9         # o1 parallela a t1alfa
f.retta(o2a, o2b, "arancio", 1.8); f.testo(o2b, "o₂", 4, 4, "arancio")
oa1, ob1 = lungo(P1(C), do, -60), lungo(P1(C), do, 340)
f.retta(oa1, ob1, "arancio", 1.8); f.testo(ob1, "o₁", 6, 6, "arancio")
f.richiamo(M2[0], M2[1], M1[1])
f.punto(M2, "M₂", 8, -8, "arancio"); f.punto(M1, "M₁", -32, 16, "arancio")
for p, n_, e2, e1 in [(A, "A", (8, 4), (8, 4)), (B, "B", (6, -6), (-24, -6)), (C, "C", (-22, -6), (-22, 14))]:
    f.punto(P2(p), n_ + "₂", *e2, "blu")
    f.punto(P1(p), n_ + "₁", *e1, "blu")
nota_righe(f, 495, ["Con le tracce: le prime tracce delle rette r = AB e s = BC stanno su t₁α, e due punti bastano.",
                    "Con l'orizzontale: o₂ per C₂ parallela alla LT incontra A₂B₂ in M₂; M₁ sta su A₁B₁;",
                    "o₁ passa per C₁ e M₁ ed è parallela a t₁α. La traccia del piano non serve."])
f.salva(OUT + "b08-tracce-o-orizzontale.svg")

# =========================================================================================
# 3. Il punto P: nello spazio
# =========================================================================================
P = in_alfa(300, 150)
assert P[1] > 0 and P[2] > 0
verso = -lato(P1(P), K, lungo(K, d1, 100))
p1, H, Pbar, r, Pst = costruzione_docente(P, K, lungo(K, d1, 100), verso)
assert math.dist(Pst, ribalta_3d(P, K, lungo(K, d1, 100), verso)) < 1e-6
assert abs(r - 150) < 1e-6        # il raggio e' la distanza vera di P dalla traccia
print("P: quota", round(P[2], 1), "aggetto", round(P[1], 1), "raggio", round(r, 1))

f, t = triedro("Nello spazio: il piano γ per P, perpendicolare ad α, e la rotazione di P", h=560,
               origine=(300, 190), scala=0.7, Y=330)
t.piano(n_a, d_a, "blu", 0.10)
t.tracce(n_a, d_a, "nero", "α")
n_g = (d1[0], -d1[1], 0)                     # gamma: verticale, perpendicolare a t1alfa
d_g = sum(n_g[i] * P[i] for i in range(3))
t.piano(n_g, d_g, "verde", 0.14)
Hs, P1s, Pbs, Psts = S1(H), S1(p1), S1(Pbar), S1(Pst)
# retta di massima pendenza m = alfa ∩ gamma: da H oltre P
mfine = tuple(Hs[i] + (P[i] - Hs[i]) * 1.25 for i in range(3))
t.segmento(Hs, mfine, "viola", 1.6)
t.testo(mfine, "m", 4, -2, "viola")
# triangolo di rotazione P1 H P
t._poligono([Hs, P1s, P], "verde", 0.25, "verde")
t.richiamo(P, P1s)


def arco3d(c, a, b, colore, n=40):
    """Arco di circonferenza nello spazio, di centro c, da a a b (stessa distanza da c)."""
    e1 = [a[i] - c[i] for i in range(3)]
    r3 = math.sqrt(sum(x * x for x in e1)); e1 = [x / r3 for x in e1]
    v = [b[i] - c[i] for i in range(3)]
    dot = sum(v[i] * e1[i] for i in range(3))
    e2 = [v[i] - dot * e1[i] for i in range(3)]
    l2 = math.sqrt(sum(x * x for x in e2)); e2 = [x / l2 for x in e2]
    amax = math.degrees(math.atan2(sum(v[i] * e2[i] for i in range(3)), dot))
    pts = []
    for i in range(n + 1):
        a_ = math.radians(amax * i / n)
        pts.append(t._p(tuple(c[j] + r3 * (math.cos(a_) * e1[j] + math.sin(a_) * e2[j]) for j in range(3))))
    f.parti.append('<path d="M ' + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) +
                   f'" fill="none" stroke="{COLORI[colore]}" stroke-width="1.4" stroke-dasharray="5,3"/>')


# ribaltamento laterale di gamma intorno a t1gamma: P va in P barrato (arco intorno a P1)
assert abs(math.dist(P, P1s) - math.dist(Pbs, P1s)) < 1e-6
arco3d(P1s, P, Pbs, "arancio")
t.segmento(Hs, Pbs, "arancio", 1.4)
# rotazione di alfa intorno a t1alfa: P va in P* (arco intorno a H, su gamma)
assert abs(math.dist(P, Hs) - math.dist(Psts, Hs)) < 1e-6
arco3d(Hs, P, Psts, "rosso")
# t1gamma
g = unit((Pst[0] - H[0], Pst[1] - H[1]))
tg_a, tg_b = S1(lungo(p1, g, -60)), S1(lungo(H, g, r + 30))
t.segmento(tg_a, tg_b, "verde", 2)
t.testo(tg_b, "t_1γ", 4, 10, "verde", 13)
t.punto(P, "P", 6, -6, "blu"); t.punto(P1s, "P₁", 8, 6); t.punto(Hs, "H", -18, -4)
t.punto(Pbs, "P̄", 8, 14, "arancio"); t.punto(Psts, "P*", 10, 6, "rosso")
t.testo(P1s, "γ", -30, -60, "verde")
nota_righe(f, 500, ["γ è proiettante in prima e passa per P; t₁γ ⊥ t₁α, quindi γ ⊥ α. m = α ∩ γ, H = t₁γ ∩ t₁α.",
                    "Arancio: γ si ribalta su π₁ intorno a t₁γ e porta con sé m e la quota di P (P̄).",
                    "Rosso: α ruota intorno a t₁α; P percorre su γ un arco di centro H e raggio HP = HP̄, fino a P*."])
f.salva(OUT + "b08-spazio-ribaltamento-del-punto.svg")

# =========================================================================================
# 4. Il punto P: sul foglio
# =========================================================================================
f = Figura(640, 640, 200, "Il ribaltamento del punto P del piano generico α su π₁", x0=10)
f.lt(10, 620)
f.traccia(K, T2A); f.testo(T2A, "t_2α", 4, 4)
fine_t1 = lungo(K, d1, 560)
f.traccia(K, fine_t1); f.testo(fine_t1, "t_1α", -40, 4)
f.richiamo(P[0], P2(P)[1], P1(P)[1])
# t1gamma per P1, perpendicolare a t1alfa
f.traccia(lungo(p1, g, -50), lungo(H, g, r + 30), "verde")
f.testo(lungo(H, g, r + 30), "t_1γ", 8, 4, "verde")
f.angolo_retto(H, d1, g)
# ribaltamento laterale: la quota di P riportata da P1, perpendicolare a t1gamma
f.costruzione(p1, Pbar)
f.angolo_retto(p1, d1, (-g[0], -g[1]))
tacche(f, (P[0], 0), P2(P), 2)
tacche(f, p1, Pbar, 2)
f.retta(H, Pbar, "arancio", 1.6)       # m ribaltata lateralmente = raggio di rotazione
mid = ((H[0] + Pbar[0]) / 2, (H[1] + Pbar[1]) / 2)
f.testo(mid, "(m)", 6, -4, "arancio", 13)
arco_tra(f, H, Pbar, Pst)
f.punto(P2(P), "P₂", 8, -4, "blu")
f.punto(p1, "P₁", -24, -8, "blu")
f.punto(H, "H", 8, -6)
f.punto(Pbar, "P̄", 8, 4, "arancio")
f.punto(Pst, "P*", 8, 8, "rosso")
nota_righe(f, 560, ["1. Per P₁ si traccia t₁γ perpendicolare a t₁α: γ è il piano proiettante in prima per P, ⊥ ad α.",
                    "2. Ribaltamento laterale di γ: da P₁, perpendicolare a t₁γ, la quota di P (due lineette): P̄.",
                    "    HP̄ è la retta di massima pendenza m ribaltata, ed è il raggio di rotazione.",
                    "3. Centro del compasso in H, raggio HP̄: l'arco porta P̄ su t₁γ. Lì c'è P*."])
f.salva(OUT + "b08-ribaltamento-del-punto.svg")

# =========================================================================================
# 5. La figura: si ribalta il punto piu' lontano (B), poi l'affinita'
# =========================================================================================
asse_a, asse_b = K, lungo(K, d1, 100)
verso5 = -lato(P1(B), asse_a, asse_b)
b1, H5, Bbar, r5, Bst = costruzione_docente(B, asse_a, asse_b, verso5)
assert math.dist(Bst, ribalta_3d(B, asse_a, asse_b, verso5)) < 1e-6
Ast, U = affine(P1(A), asse_a, asse_b, P1(B), Bst)
Cst, V = affine(P1(C), asse_a, asse_b, P1(B), Bst)
assert math.dist(Ast, ribalta_3d(A, asse_a, asse_b, verso5)) < 1e-6
assert math.dist(Cst, ribalta_3d(C, asse_a, asse_b, verso5)) < 1e-6
controlla("triangolo ribaltato", [A, B, C], [Ast, Bst, Cst])
dist = {n_: abs(lato(P1(p), asse_a, asse_b)) for n_, p in (("A", A), ("B", B), ("C", C))}
assert max(dist, key=dist.get) == "B"
print("U", [round(c) for c in U], "V", [round(c) for c in V], "B*", [round(c) for c in Bst])

f = Figura(660, 640, 160, "La figura: si ribalta B, il punto più lontano da t₁α, poi l'affinità", x0=0)
f.lt(0, 650)
fine_t1 = lungo(K, d1, 600)
f.traccia(K, fine_t1); f.testo(fine_t1, "t_1α", -40, 4)
f.figura([P2(A), P2(B), P2(C)], "blu")
f.figura([P1(A), P1(B), P1(C)], "blu")
for p in (A, B, C):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
g5 = unit((Bst[0] - H5[0], Bst[1] - H5[1]))
f.traccia(lungo(b1, g5, -40), lungo(H5, g5, r5 + 30), "verde")
f.testo(lungo(b1, g5, -40), "t_1γ", 6, -4, "verde")
f.angolo_retto(H5, d1, g5)
f.costruzione(b1, Bbar)
tacche(f, (B[0], 0), P2(B), 2)
tacche(f, b1, Bbar, 2)
f.retta(H5, Bbar, "arancio", 1.4)
arco_tra(f, H5, Bbar, Bst)
for Q1, X, Qst in [(P1(A), U, Ast), (P1(C), V, Cst)]:
    f.costruzione(P1(B), X)
    f.costruzione(X, Bst)
    f.costruzione(Q1, Qst)
f.figura([Ast, Bst, Cst], "rosso")
for p, n_, e2, e1 in [(A, "A", (8, 4), (8, 6)), (B, "B", (6, -6), (6, -8)), (C, "C", (-22, -6), (-24, -4))]:
    f.punto(P2(p), n_ + "₂", *e2, "blu")
    f.punto(P1(p), n_ + "₁", *e1, "blu")
f.punto(Bbar, "B̄", 8, 4, "arancio"); f.punto(H5, "H", 8, -6)
f.punto(U, "U", 6, 16); f.punto(V, "V", -18, 16)
f.punto(Ast, "A*", 8, 6, "rosso"); f.punto(Bst, "B*", 8, 10, "rosso"); f.punto(Cst, "C*", -28, 6, "rosso")
nota_righe(f, 555, ["1. B è il vertice più lontano da t₁α: lo si ribalta come il punto P (t₁γ, B̄ con la quota, raggio HB̄): B*.",
                    "2. Affinità di asse t₁α: la retta B₁A₁ incontra l'asse in U; la retta UB* incontra in A* la",
                    "    perpendicolare all'asse condotta da A₁. Allo stesso modo, con V, si trova C*.",
                    "3. A*B*C* è la vera grandezza e forma del triangolo."])
f.salva(OUT + "b08-ribaltamento-figura-punto-lontano.svg")

# =========================================================================================
# 6. Perche' il punto lontano: lo stesso piccolo errore, ribaltando A (vicino) o B (lontano)
# =========================================================================================
# Solo prima proiezione: asse orizzontale nel foglio. Coordinate locali per ciascun riquadro.
ERR = 7.0                              # errore di disegno sul punto ribaltato (in pixel)
f = Figura(680, 430, 0, "Lo stesso piccolo errore: ribaltando il punto vicino o quello lontano")


def riquadro(ox, titolo, ribalto):
    """Riquadro con l'asse a 165 px dall'alto. A1 vicino all'asse, B1 lontano, allineati con U.
    Coordinate locali: x verso destra, y verso l'alto dall'asse."""
    def L(p):
        return (ox + p[0], -165 + p[1])
    U0, B1 = (40, 0), (215, 70)
    dirAB = unit((B1[0] - U0[0], B1[1] - U0[1]))
    A1 = (U0[0] + dirAB[0] * 80, U0[1] + dirAB[1] * 80)
    k = 2.2                                         # rapporto dell'affinita' (uguale per tutti i punti)
    Av, Bv = (A1[0], -A1[1] * k), (B1[0], -B1[1] * k)
    f.retta(L((0, 0)), L((300, 0)), "nero", 2.2)
    f.testo(L((300, 0)), "asse", -34, -8, "nero", 12, False)
    f.retta(L(U0), L(B1), "blu", 1.4)
    f.costruzione(L(A1), L((A1[0], -175)))
    f.costruzione(L(B1), L((B1[0], -190)))
    f.costruzione(L(U0), L(Bv))                     # la retta ribaltata giusta
    if ribalto == "A":
        Ae = (Av[0], Av[1] - ERR)                   # A* disegnato con un piccolo errore
        Be = interseca(U0, Ae, (B1[0], 0), (B1[0], -1))
        giusto, err = Bv, math.dist(Be, Bv)
    else:
        Be = (Bv[0], Bv[1] - ERR)
        Ae = interseca(U0, Be, (A1[0], 0), (A1[0], -1))
        giusto, err = Av, math.dist(Ae, Av)
    f.retta(L(U0), L(lungo(U0, unit((Be[0] - U0[0], Be[1] - U0[1])), math.dist(U0, Be) + 20)), "rosso", 1.4)
    f.punto(L(giusto), None, colore="grigio")
    f.punto(L(A1), "A₁", -24, -6, "blu"); f.punto(L(B1), "B₁", 6, -6, "blu")
    f.punto(L(U0), "U", -6, -10)
    f.punto(L(Ae), "A*", -28, 4, "rosso"); f.punto(L(Be), "B*", 8, 4, "rosso")
    f.nota(ox + 10, 40, titolo, 13)
    f.nota(ox + 10, 58, f"({ribalto}* è disegnato con un piccolo errore)", 12)
    return err


eA = riquadro(10, "Si ribalta A, vicino all'asse", "A")
eB = riquadro(350, "Si ribalta B, lontano dall'asse", "B")
print("errore sull'altro punto: ribaltando A", round(eA, 1), "ribaltando B", round(eB, 1), "(errore iniziale", ERR, ")")
assert eA > ERR > eB
nota_righe(f, 395, [f"In entrambi i casi il punto ribaltato è sbagliato di poco ({ERR:.0f}). Ribaltando il vicino, l'errore su B*",
                    f"diventa {eA:.0f}; ribaltando il lontano, l'errore su A* si riduce a {eB:.0f}. Il pallino grigio è la posizione giusta."], x=14)
f.salva(OUT + "b08-punto-vicino-o-lontano.svg")
print("ok")
