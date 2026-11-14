"""Schemi per la bozza di geometria descrittiva 10 (lezione del 5 novembre): l'intersezione
tra una retta e un piano, la distanza punto-piano, il segmento perpendicolare a una figura
costruito a ritroso, la scala in pianta.

Usa disegni_monge.py senza modificarlo. Ogni costruzione viene controllata con la geometria
vera nello spazio (assert): il punto trovato sul foglio deve essere quello vero, le misure
ribaltate devono essere le misure vere.

Disegni (tutti in bozze/img/):
- b10-intersezione-retta-piano-tracce / b10-spazio-intersezione-retta-piano-tracce
- b10-distanza-punto-piano-tracce / b10-spazio-distanza-punto-piano
- b10-es1-perpendicolare-dalla-figura / b10-es1-distanza-vera-grandezza
- b10-es2-segmento-3-cm / b10-spazio-es2-segmento-3-cm
- b10-scala-uno-o-due-segni
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"


# ---------- funzioni di servizio ----------

def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def unit(v):
    l = math.sqrt(sum(x * x for x in v))
    return tuple(x / l for x in v)


def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(len(a)))


def add(a, b, k=1.0):
    return tuple(a[i] + k * b[i] for i in range(len(a)))


def dot(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


def tacche(f, a, b, n, colore="nero", t=0.5):
    L = math.dist(a, b)
    d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    q = (-d[1], d[0])
    m = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        c = lungo(m, d, o)
        f._linea(lungo(c, q, -5), lungo(c, q, 5), colore, 1.3)


def angolo_retto3d(t, v, d1, d2, lato=12):
    a = add(v, d1, lato)
    c = add(v, d2, lato)
    b = add(a, d2, lato)
    t.segmento(a, b, "nero", 1); t.segmento(b, c, "nero", 1)


def righe(f, y, testi):
    for i, r in enumerate(testi):
        f.nota(16, y + 17 * i, r)


def segmento_spesso(f, a, b, colore="nero", spessore=3):
    f._linea(a, b, colore, spessore)


def su_lati(proj, tri, p, q):
    """Punti 3D sui lati del triangolo tri la cui proiezione proj cade sulla retta pq (disegno)."""
    out = []
    for i in range(3):
        a, b = tri[i], tri[(i + 1) % 3]
        pa, pb = proj(a), proj(b)
        x = interseca(p, q, pa, pb)
        if x is None:
            continue
        L = math.dist(pa, pb)
        s = math.dist(pa, x) / L
        if abs(math.dist(pa, x) + math.dist(x, pb) - L) < 1e-6:
            pt = lerp(a, b, s)
            if all(math.dist(pt, o) > 1e-6 for o in out):
                out.append(pt)
    return out


def ribalta(P, u):
    """Ribaltamento su pi1 del piano proiettante in prima che contiene P, intorno alla prima
    traccia: P* sta sulla perpendicolare alla traccia condotta da P1, a distanza = quota di P."""
    return lungo(P1(P), u, P[2])


# =========================================================================================
# Il piano generico alfa (stesso piano per i disegni 1 e 2): passa per K = (40, 0, 0)
# =========================================================================================
KA = (40, 0, 0)
n_a, d_a = piano(KA, (440, 220, 0), (440, 0, 200))


def z_alfa(x, y):
    return (d_a - n_a[0] * x - n_a[1] * y) / n_a[2]


def t1a(x):   # prima traccia nel disegno (y = -aggetto)
    return (x, -(d_a - n_a[0] * x) / n_a[1])


def t2a(x):   # seconda traccia nel disegno
    return (x, (d_a - n_a[0] * x) / n_a[2])


def tracce_alfa(f, x2):
    f.traccia((40, 0), t2a(x2)); f.testo(t2a(x2), "t_2α", 4, 4)
    f.traccia((40, 0), t1a(x2)); f.testo(t1a(x2), "t_1α", 4, 12)


# =========================================================================================
# 1. Forma canonica: intersezione tra la retta r e il piano alfa dato con le tracce
# =========================================================================================
P = (260, 40, z_alfa(260, 40))
D = (150, -30, -50)
R0, R1 = add(P, D, -0.8), add(P, D, 0.8)
assert R0[1] > 0 and R0[2] > 0 and R1[1] > 0 and R1[2] > 0

# gamma: proiettante in prima per r. t1gamma = r1 prolungata fino alla LT; t2gamma verticale
xg = interseca(P1(R0), P1(R1), (0, 0), (1, 0))[0]
T1n_d = interseca(P1(R0), P1(R1), t1a(0), t1a(400))          # T1n = t1alfa ∩ t1gamma (disegno)
T1n = (T1n_d[0], -T1n_d[1], 0)
T2n = (xg, 0, t2a(xg)[1])                                     # T2n = t2alfa ∩ t2gamma
p2 = interseca((T1n[0], 0), P2(T2n), P2(R0), P2(R1))          # P2 = n2 ∩ r2
p1 = interseca((p2[0], 0), (p2[0], -1), P1(R0), P1(R1))
assert math.dist(p2, P2(P)) < 1e-6 and math.dist(p1, P1(P)) < 1e-6

f = Figura(600, 550, 250, "Forma canonica: dove la retta r buca il piano α (dato con le tracce)", x0=20)
f.lt(0, 560)
tracce_alfa(f, 475)
# gamma
f.traccia(P1(add(P, D, -1.25)), (xg, 0), "viola")
f.traccia((xg, 0), (xg, 240), "viola"); f.testo((xg, 240), "t_2γ", -34, 8, "viola")
# r
f.retta(P1(R0), P1(R1), "rosso"); f.retta(P2(R0), P2(R1), "rosso")
f.testo(P2(R0), "r₂", -22, 0, "rosso")
f.testo(P1(add(P, D, 0.45)), "r₁ ≡ t₁γ ≡ n₁", -20, 28, "viola")
# n
f.richiamo(T1n[0], 0, -T1n[1])
f.retta((T1n[0], 0), P2(T2n), "viola", 1.8)
f.testo(lerp((T1n[0], 0), P2(T2n), 0.8), "n₂", 8, 16, "viola")
f.punto(P1(T1n), "T_{1n}", -10, 26, "viola"); f.punto((T1n[0], 0), "(T_{1n})₂", -72, -8, "viola")
f.punto(P2(T2n), "T_{2n}", 8, 20, "viola"); f.punto((xg, 0), "(T_{2n})₁", 6, 18, "viola")
# P
f.richiamo(P[0], p2[1], p1[1])
f.punto(p2, "P₂", -5, -16, "nero"); f.punto(p1, "P₁", -8, 22, "nero")
righe(f, 518, ["γ proiettante in prima per r: t₁γ ≡ r₁. n = α ∩ γ: T₁ₙ = t₁α ∩ t₁γ, T₂ₙ = t₂α ∩ t₂γ, n₁ ≡ t₁γ.",
               "n₂ unisce T₂ₙ e (T₁ₙ)₂. Dove n₂ incontra r₂ c'è P₂; P₁ sta su r₁, sulla linea di richiamo."])
f.salva(OUT + "b10-intersezione-retta-piano-tracce.svg")

# ---------- 1b. nello spazio ----------
f = Figura(620, 520, 0, "Nello spazio: γ contiene r e taglia α lungo n; r e n si incontrano in P")
t = Triedro(f, (330, 225), X3=500, U=480, Y=270, Z=250, scala=0.62)
t.piani()
t.piano(n_a, d_a, "blu", 0.13)
t.tracce(n_a, d_a, "nero", "α")
ng, dg = piano(R0, R1, (R0[0], R0[1], R0[2] + 100))
t.piano(ng, dg, "viola", 0.10)
t.tracce(ng, dg, "viola")
t.testo((xg, 0, 120), "t_2γ", 6, 0, "viola", 13)
Tr1 = lerp(R0, R1, -R0[2] / (R1[2] - R0[2]))            # prima traccia di r
t.testo(lerp((T1n[0], T1n[1], 0), Tr1, 0.85), "t_1γ ≡ r₁", 4, 18, "viola", 13)
t.segmento(T1n, T2n, "viola", 2.4)
t.testo(lerp(T1n, T2n, 0.75), "n", -14, -2, "viola", 15)
t.segmento(add(P, D, -1.1), Tr1, "rosso", 2.2)
t.testo(add(P, D, -1.1), "r", -14, 0, "rosso", 16)
t.richiamo(P, (P[0], P[1], 0))
Rlo = add(P, D, -1.1)
t.segmento((Rlo[0], Rlo[1], 0), Tr1, "rosso", 1, "5,3")
t.punto((P[0], P[1], 0), "P₁", -24, 6)
t.punto(T1n, "T_{1n}", -52, 0, "viola"); t.punto(T2n, "T_{2n}", -40, 0, "viola")
t.punto(P, "P", 8, -8, "nero")
righe(f, 500, ["Il piano γ è verticale (proiettante in prima) e contiene r. n = α ∩ γ va da T₁ₙ a T₂ₙ;",
               "r e n stanno tutte e due su γ, quindi si incontrano: il punto comune P è il punto in cui r buca α."])
f.salva(OUT + "b10-spazio-intersezione-retta-piano-tracce.svg")


# =========================================================================================
# 2. Distanza punto-piano, in forma canonica. Qui alfa e' una falda poco inclinata (come un
#    tetto): t1alfa ripida, t2alfa bassa. Cosi' nella vista nello spazio il segmento PH si vede.
# =========================================================================================
K2 = (40, 0, 0)
nb, db = piano(K2, (200, 240, 0), (480, 0, 110))        # t1: aggetto 1.5 (x-40); t2: quota 0.25 (x-40)


def t1b(x):
    return (x, -(db - nb[0] * x) / nb[1])


def t2b(x):
    return (x, (db - nb[0] * x) / nb[2])


Q = (330, 60, 200)                           # il punto esterno (nel testo e nel disegno: P)
s = (dot(nb, Q) - db) / dot(nb, nb)
H = add(Q, nb, -s)                           # piede della perpendicolare
assert abs(dot(nb, H) - db) < 1e-6 and H[1] > 0 and H[2] > 0 and H[2] < Q[2]
dPH = math.dist(Q, H)
dr = (H[0] - Q[0], H[1] - Q[1], H[2] - Q[2])
v1 = (H[0] - Q[0], -(H[1] - Q[1])); v2 = (H[0] - Q[0], H[2] - Q[2])
w1 = (t1b(200)[0] - 40, t1b(200)[1]); w2 = (t2b(400)[0] - 40, t2b(400)[1])
assert abs(dot(v1, w1)) < 1e-6 and abs(dot(v2, w2)) < 1e-6         # teorema di Monge

xg2 = interseca(P1(Q), P1(H), (0, 0), (1, 0))[0]
T1n2_d = interseca(P1(Q), P1(H), t1b(0), t1b(200))
T1n2 = (T1n2_d[0], -T1n2_d[1], 0)
T2n2 = (xg2, 0, t2b(xg2)[1])
h2 = interseca((T1n2[0], 0), P2(T2n2), P2(Q), P2(H))
assert math.dist(h2, P2(H)) < 1e-6
dg1 = unit(v1)
u = (dg1[1], -dg1[0])
if u[0] < 0:
    u = (-u[0], -u[1])
Qs, Hs = ribalta(Q, u), ribalta(H, u)
assert abs(math.dist(Qs, Hs) - dPH) < 1e-6

f = Figura(620, 580, 250, "La distanza del punto P dal piano α (forma canonica)", x0=10)
f.lt(0, 590)
f.traccia((40, 0), t2b(560)); f.testo(t2b(560), "t_2α", -10, -10)
f.traccia((40, 0), t1b(190)); f.testo(t1b(190), "t_1α", -36, 4)
d2 = unit(v2)
# gamma
f.traccia(lungo(P1(T1n2), dg1, -25), (xg2, 0), "viola")
f.traccia((xg2, 0), (xg2, 150), "viola"); f.testo((xg2, 150), "t_2γ", 6, 4, "viola")
f.testo(lungo(P1(T1n2), dg1, -25), "r₁ ≡ t₁γ ≡ n₁", -40, 22, "viola")
# r2 (r1 coincide con t1gamma)
f.retta(lungo(P2(Q), d2, -30), lungo(P2(H), d2, 45), "rosso")
f.testo(lungo(P2(Q), d2, -30), "r₂", 6, 4, "rosso")
x_r2 = interseca(P2(Q), P2(H), (40, 0), t2b(400))
f.angolo_retto(x_r2, (-d2[0], -d2[1]), unit(w2))
f.angolo_retto(P1(T1n2), dg1, unit(w1))
# n
f.richiamo(T1n2[0], 0, -T1n2[1])
f.retta((T1n2[0], 0), P2(T2n2), "viola", 1.8)
f.testo(lerp((T1n2[0], 0), P2(T2n2), 0.45), "n₂", -6, -10, "viola")
f.punto(P1(T1n2), "T_{1n}", 10, 6, "viola"); f.punto((T1n2[0], 0), "(T_{1n})₂", -40, 20, "viola")
f.punto(P2(T2n2), "T_{2n}", 8, 18, "viola"); f.punto((xg2, 0), None, colore="viola")
# P e H
f.richiamo(Q[0], P2(Q)[1], P1(Q)[1]); f.richiamo(H[0], P2(H)[1], P1(H)[1])
segmento_spesso(f, P2(Q), P2(H)); segmento_spesso(f, P1(Q), P1(H))
f.punto(P2(Q), "P₂", 8, -4); f.punto(P1(Q), "P₁", -26, -4)
f.punto(P2(H), "H₂", 14, 20); f.punto(P1(H), "H₁", -26, -6)
# ribaltamento di gamma su pi1 intorno a t1gamma
for X, Xs, n_t in [(Q, Qs, 1), (H, Hs, 2)]:
    f.costruzione(P1(X), Xs)
    tacche(f, P1(X), Xs, n_t)
    tacche(f, P2(X), (X[0], 0), n_t, t=0.35)
    f.angolo_retto(P1(X), dg1, u)
segmento_spesso(f, Qs, Hs, "verde", 3.2)
f.punto(Qs, "P*", 8, 4, "verde"); f.punto(Hs, "H*", 8, 4, "verde")
f.testo(lerp(Qs, Hs, 0.5), "distanza vera", 12, 4, "verde", 13, False)
righe(f, 528, ["1. r per P: r₁ ⊥ t₁α, r₂ ⊥ t₂α.  2. γ proiettante in prima per r (t₁γ ≡ r₁): n = α ∩ γ, H₂ = n₂ ∩ r₂.",
               "3. γ si ribalta su π₁ intorno a t₁γ: P* e H* stanno sulle perpendicolari a t₁γ, alla distanza",
               "della quota (una e due lineette). P*H* è la distanza di P da α in vera grandezza."])
f.salva(OUT + "b10-distanza-punto-piano-tracce.svg")

# ---------- 2b. nello spazio ----------
f = Figura(620, 540, 0, "Nello spazio: la perpendicolare da P incontra α in H; PH è la distanza")
t = Triedro(f, (330, 235), X3=470, U=440, Y=260, Z=230, scala=0.66)
t.piani()
t.piano(nb, db, "blu", 0.14)
t.tracce(nb, db, "nero", "α")
ng2, dg2 = piano(Q, H, (Q[0], Q[1], Q[2] + 100))
t.piano(ng2, dg2, "viola", 0.10)
t.tracce(ng2, dg2, "viola")
t.segmento(T1n2, T2n2, "viola", 2.2)
t.testo(lerp(T1n2, T2n2, 0.25), "n", -4, -10, "viola", 15)
t.segmento(add(Q, dr, -0.25), add(Q, dr, 1.3), "rosso", 1.6)
t.segmento(Q, H, "nero", 3)
angolo_retto3d(t, H, unit(add((0, 0, 0), dr, -1)), unit((T2n2[0] - H[0], T2n2[1] - H[1], T2n2[2] - H[2])))
for X, nome in [(Q, "P"), (H, "H")]:
    t.richiamo(X, (X[0], X[1], 0))
    t.punto((X[0], X[1], 0), nome + "₁", 6, 16)
t.punto(Q, "P", 8, -6); t.punto(H, "H", -20, 14)
t.testo(add(Q, dr, -0.25), "r", 8, 0, "rosso", 15)
righe(f, 515, ["r è perpendicolare ad α; il piano verticale γ che la contiene è perpendicolare ad α e lo taglia",
               "lungo n, una retta di massima pendenza. H = r ∩ n; il segmento PH è la distanza di P da α."])
f.salva(OUT + "b10-spazio-distanza-punto-piano.svg")


# =========================================================================================
# Ribaltamento in forma tecnica: gamma (proiettante in prima) ruota intorno alla sua
# orizzontale alla quota z0; le distanze da riportare sono le differenze di quota.
# =========================================================================================
def ribalta_oriz(X, z0, u):
    return lungo(P1(X), u, X[2] - z0)


def lato_lontano(u, X1, centro):
    """Sceglie il verso di u che porta lontano dal centro della figura."""
    if (X1[0] - centro[0]) * u[0] + (X1[1] - centro[1]) * u[1] < 0:
        return (-u[0], -u[1])
    return u


def triangolo(f, T, nomi_off, colore="blu", etichette=True):
    f.figura([P2(X) for X in T], colore); f.figura([P1(X) for X in T], colore)
    if not etichette:
        return
    for X, nome, d2_, d1_ in zip(T, "ABC", *zip(*nomi_off)):
        f.richiamo(X[0], P2(X)[1], P1(X)[1])
        f.punto(P2(X), nome + "₂", *d2_); f.punto(P1(X), nome + "₁", *d1_)


def oriz_front(T, X):
    """Orizzontale e frontale del triangolo T passanti per il punto X del triangolo:
    restituisce i due punti sui lati per ciascuna."""
    o = su_lati(P2, T, P2(X), (P2(X)[0] + 1, P2(X)[1]))
    fr = su_lati(P1, T, P1(X), (P1(X)[0] + 1, P1(X)[1]))
    assert len(o) == 2 and len(fr) == 2
    return sorted(o, key=lambda q: q[0]), sorted(fr, key=lambda q: q[0])


def disegna_of(f, o, fr, ext=25, etichette=((-22, 4), (-22, 4), (4, 4), (4, 4))):
    do = unit((P1(o[1])[0] - P1(o[0])[0], P1(o[1])[1] - P1(o[0])[1]))
    df = unit((P2(fr[1])[0] - P2(fr[0])[0], P2(fr[1])[1] - P2(fr[0])[1]))
    f.retta(lungo(P2(o[0]), (1, 0), -ext), lungo(P2(o[1]), (1, 0), ext), "arancio", 1.5)
    f.retta(lungo(P1(o[0]), do, -ext), lungo(P1(o[1]), do, ext), "arancio", 1.5)
    f.retta(lungo(P1(fr[0]), (1, 0), -ext), lungo(P1(fr[1]), (1, 0), ext), "verde", 1.5)
    f.retta(lungo(P2(fr[0]), df, -ext), lungo(P2(fr[1]), df, ext), "verde", 1.5)
    f.testo(lungo(P2(o[0]), (1, 0), -ext), "o₂", *etichette[0], "arancio")
    f.testo(lungo(P1(o[0]), do, -ext), "o₁", *etichette[1], "arancio")
    f.testo(lungo(P1(fr[1]), (1, 0), ext), "f₁", *etichette[2], "verde")
    f.testo(lungo(P2(fr[1]), df, ext), "f₂", *etichette[3], "verde")
    for X, col in [(o[0], "arancio"), (o[1], "arancio"), (fr[0], "verde"), (fr[1], "verde")]:
        f.richiamo(X[0], P2(X)[1], P1(X)[1])
        f.punto(P2(X), None, colore=col); f.punto(P1(X), None, colore=col)
    return do, df


# =========================================================================================
# 3. Esercizio 1: distanza punto-piano con il piano dato da un triangolo
# =========================================================================================
A, B, C = (60, 90, 50), (370, 180, 120), (230, 20, 230)
TRI = [A, B, C]
N, DD = piano(A, B, C)
nN = unit(N)
if nN[2] < 0:
    nN = tuple(-x for x in nN)
H3 = tuple(0.34 * A[i] + 0.33 * B[i] + 0.33 * C[i] for i in range(3))
P3 = add(H3, nN, 85)
assert P3[1] > 0 and P3[2] > 0
o3 = sorted([B, lerp(A, C, (B[2] - A[2]) / (C[2] - A[2]))], key=lambda q: q[0])   # orizzontale per B
f3 = sorted([A, lerp(B, C, (A[1] - B[1]) / (C[1] - B[1]))], key=lambda q: q[0])   # frontale per A
assert abs(o3[0][2] - o3[1][2]) < 1e-9 and abs(f3[0][1] - f3[1][1]) < 1e-9
vr1 = unit((P1(H3)[0] - P1(P3)[0], P1(H3)[1] - P1(P3)[1]))
vr2 = unit((P2(H3)[0] - P2(P3)[0], P2(H3)[1] - P2(P3)[1]))
LM = su_lati(P1, TRI, P1(P3), P1(H3))
assert len(LM) == 2
L3, M3 = sorted(LM, key=lambda q: q[0])
hh = interseca(P2(L3), P2(M3), P2(P3), P2(H3))
assert math.dist(hh, P2(H3)) < 1e-6
OFF3 = [((-26, -4), (-24, 18)), ((8, 4), (10, -4)), ((-6, -10), (-28, 8))]


def r_es1(f, fine1=60, fine2=60):
    f.retta(lungo(P1(P3), vr1, -40), lungo(P1(H3), vr1, fine1), "rosso")
    f.retta(lungo(P2(P3), vr2, -30), lungo(P2(H3), vr2, fine2), "rosso")


# ---- 3a: la perpendicolare con l'orizzontale e la frontale, e il piede H ----
f = Figura(600, 620, 300, "Esercizio 1 · La perpendicolare da P al triangolo e il suo piede H", x0=20)
f.lt(-10, 560)
triangolo(f, TRI, OFF3)
do3, df3 = disegna_of(f, o3, f3)
assert abs(dot(vr1, do3)) < 1e-9 and abs(dot(vr2, df3)) < 1e-9          # r1 ⊥ o1, r2 ⊥ f2
r_es1(f)
f.testo(lungo(P1(P3), vr1, -40), "r₁ ≡ γ₁", -60, 4, "rosso")
f.testo(lungo(P2(P3), vr2, -30), "r₂", -22, 0, "rosso")
f.angolo_retto(interseca(P1(P3), P1(H3), P1(o3[0]), P1(o3[1])), vr1, do3)
f.angolo_retto(interseca(P2(P3), P2(H3), P2(f3[0]), P2(f3[1])), vr2, df3)
for X, nome, d1_, d2_ in [(L3, "L", (-26, 6), (-26, 4)), (M3, "M", (8, 16), (8, -6))]:
    f.richiamo(X[0], P2(X)[1], P1(X)[1])
    f.punto(P1(X), nome + "₁", *d1_, colore="viola"); f.punto(P2(X), nome + "₂", *d2_, colore="viola")
f.retta(lerp(P2(L3), P2(M3), -0.12), lerp(P2(L3), P2(M3), 1.3), "viola", 1.8)
f.testo(lerp(P2(L3), P2(M3), 1.3), "n₂", 6, 0, "viola")
f.richiamo(P3[0], P2(P3)[1], P1(P3)[1]); f.richiamo(H3[0], P2(H3)[1], P1(H3)[1])
segmento_spesso(f, P2(P3), P2(H3)); segmento_spesso(f, P1(P3), P1(H3))
f.punto(P2(P3), "P₂", 8, -4); f.punto(P1(P3), "P₁", 8, 4)
f.punto(P2(H3), "H₂", 8, 16); f.punto(P1(H3), "H₁", 8, -8)
righe(f, 572, ["o orizzontale per B, f frontale per A. r per P: r₁ ⊥ o₁, r₂ ⊥ f₂ (angoli retti).",
               "γ proiettante in prima per r: γ₁ ≡ r₁ taglia i lati in L₁ e M₁; n₂ = L₂M₂; H₂ = n₂ ∩ r₂, H₁ su r₁."])
f.salva(OUT + "b10-es1-perpendicolare-dalla-figura.svg")

# ---- 3b: la distanza PH in vera grandezza, ribaltando gamma intorno alla sua orizzontale per H ----
g3 = lato_lontano((vr1[1], -vr1[0]), P1(H3), tuple(sum(P1(X)[i] for X in TRI) / 3 for i in range(2)))
P3s, H3s = ribalta_oriz(P3, H3[2], g3), ribalta_oriz(H3, H3[2], g3)
assert math.dist(H3s, P1(H3)) < 1e-9 and abs(math.dist(P3s, H3s) - 85) < 1e-6
f = Figura(600, 620, 300, "Esercizio 1 · La distanza PH in vera grandezza", x0=20)
f.lt(-10, 560)
triangolo(f, TRI, OFF3, "grigio", etichette=False)
r_es1(f)
f.testo(lungo(P1(P3), vr1, -40), "r₁ ≡ γ₁", -60, 4, "rosso")
f.testo(lungo(P2(P3), vr2, -30), "r₂", -22, 0, "rosso")
# l'orizzontale di gamma alla quota di H: seconda proiezione parallela alla LT per H2
f.costruzione((P3[0] - 70, H3[2]), (H3[0] + 70, H3[2]))
f.testo((H3[0] + 70, H3[2]), "quota di H", 4, 4, "grigio", 12, False)
f.richiamo(P3[0], P2(P3)[1], P1(P3)[1]); f.richiamo(H3[0], P2(H3)[1], P1(H3)[1])
segmento_spesso(f, P2(P3), P2(H3)); segmento_spesso(f, P1(P3), P1(H3))
tacche(f, P2(P3), (P3[0], H3[2]), 1)
f.costruzione(P1(P3), P3s); tacche(f, P1(P3), P3s, 1)
f.angolo_retto(P1(P3), vr1, g3)
segmento_spesso(f, P3s, H3s, "verde", 3.2)
f.punto(P2(P3), "P₂", 8, -4); f.punto(P1(P3), "P₁", 8, 4)
f.punto(P2(H3), "H₂", 8, 16)
f.punto(P3s, "P*", -30, -6, "verde"); f.punto(H3s, "H₁ ≡ H*", 8, -8, "verde")
f.testo(lerp(P3s, H3s, 0.5), "distanza vera", -110, -12, "verde", 13, False)
righe(f, 572, ["γ ruota intorno alla sua orizzontale alla quota di H: H non si muove (H* ≡ H₁). Da P₁, perpendicolare",
               "a γ₁, si riporta la differenza di quota tra P e H (una lineetta): P*. P*H* è la distanza vera."])
f.salva(OUT + "b10-es1-distanza-vera-grandezza.svg")

# =========================================================================================
# 4. Esercizio 2: dal punto Q del triangolo, il segmento perpendicolare lungo 3 cm (a ritroso)
#    Il triangolo sta su un piano z = -30 + 0.6 x + 0.8 y (piu' alto davanti): nella vista
#    nello spazio la perpendicolare si vede bene.
# =========================================================================================
CM = 30                                        # nello schema 1 cm = 30 unita'


def z4(x, y):
    return -30 + 0.6 * x + 0.8 * y


A4, B4, C4 = (70, 40, z4(70, 40)), (300, 60, z4(300, 60)), (170, 170, z4(170, 170))
T4 = [A4, B4, C4]
N4, D4 = piano(A4, B4, C4)
n4 = unit(N4)
if n4[2] < 0:
    n4 = tuple(-x for x in n4)
_oL, _oR = sorted(su_lati(P2, T4, (0, 140), (1, 140)), key=lambda q: q[0])
Q4 = lerp(_oL, _oR, 0.3)                       # un punto dentro il triangolo, sull'orizzontale a quota 140
E4 = add(Q4, n4, 3 * CM)                       # l'estremo vero del segmento di 3 cm
S4 = add(Q4, n4, 1.5 * CM)                     # un punto qualunque della perpendicolare
assert min(E4[1], S4[1]) > 0
o4, f4 = oriz_front(T4, Q4)
w1_4 = unit((P1(E4)[0] - P1(Q4)[0], P1(E4)[1] - P1(Q4)[1]))
w2_4 = unit((P2(E4)[0] - P2(Q4)[0], P2(E4)[1] - P2(Q4)[1]))
c4 = tuple(sum(P1(X)[i] for X in T4) / 3 for i in range(2))
g4 = (w1_4[1], -w1_4[0])
if g4[0] > 0:
    g4 = (-g4[0], -g4[1])                      # verso sinistra, fuori dal triangolo
# il ribaltamento di gamma su pi1 intorno alla prima traccia (t1gamma ≡ r1): si riportano le quote
Q4s, S4s = ribalta(Q4, g4), ribalta(S4, g4)
dr4 = unit((S4s[0] - Q4s[0], S4s[1] - Q4s[1]))
E4s = lungo(Q4s, dr4, 3 * CM)                  # 3 cm misurati sulla retta ribaltata
# a ritroso: da E* perpendicolare a r1 -> E1; richiamo -> E2 su r2
E1 = interseca(E4s, lungo(E4s, g4, 1), P1(Q4), P1(E4))
E2 = interseca((E1[0], 0), (E1[0], 1), P2(Q4), P2(E4))
assert math.dist(E1, P1(E4)) < 1e-6 and math.dist(E2, P2(E4)) < 1e-6
assert abs(math.dist(E4s, E1) - E4[2]) < 1e-6

f = Figura(680, 640, 330, "Esercizio 2 · Da Q, punto del triangolo, il segmento QE perpendicolare lungo 3 cm", x0=150)
f.lt(-140, 510)
triangolo(f, T4, [((-24, 4), (-24, 6)), ((8, 4), (8, 8)), ((-6, -10), (-26, 14))])
do4, df4 = disegna_of(f, o4, f4, etichette=((-22, 4), (-26, 8), (4, 4), (4, 4)))
assert abs(dot(w1_4, do4)) < 1e-9 and abs(dot(w2_4, df4)) < 1e-9
f.retta(lungo(P1(Q4), w1_4, -60), lungo(E1, w1_4, 30), "rosso")
f.retta(lungo(P2(Q4), w2_4, -50), lungo(E2, w2_4, 40), "rosso")
f.testo(lungo(P1(Q4), w1_4, -60), "r₁ ≡ t₁γ", 6, 10, "rosso")
f.testo(lungo(E2, w2_4, 40), "r₂", 6, 4, "rosso")
f.angolo_retto(P1(Q4), w1_4, do4); f.angolo_retto(P2(Q4), w2_4, df4)
for X, Xs, n_t, nome in [(Q4, Q4s, 1, "Q"), (S4, S4s, 2, "S")]:
    f.richiamo(X[0], P2(X)[1], P1(X)[1])
    f.costruzione(P1(X), Xs)
    tacche(f, P1(X), Xs, n_t, t=0.6)
    f.costruzione(P2(X), (X[0], 0))
    tacche(f, P2(X), (X[0], 0), n_t, t=0.75)
f.costruzione(E1, E4s); f.angolo_retto(E1, w1_4, g4)
f.punto(P2(S4), "S₂", 8, 4, "grigio"); f.punto(P1(S4), "S₁", -24, -4, "grigio")
f.retta(lungo(Q4s, dr4, -25), lungo(Q4s, dr4, 3 * CM + 45), "verde", 1.4)
f.testo(lungo(Q4s, dr4, -25), "r*", 6, 6, "verde")
f.punto(S4s, "S*", -6, -10, "grigio")
segmento_spesso(f, Q4s, E4s, "verde", 3.2)
f.testo(lerp(Q4s, E4s, 0.5), "3 cm", -14, 24, "verde", 13, False)
f.punto(Q4s, "Q*", -8, 22, "verde"); f.punto(E4s, "E*", -10, -12, "verde")
segmento_spesso(f, P2(Q4), E2); segmento_spesso(f, P1(Q4), E1)
f.punto(P2(Q4), "Q₂", 8, 18); f.punto(P1(Q4), "Q₁", 4, 22)
f.punto(E2, "E₂", 8, -6); f.punto(E1, "E₁", 8, -8)
righe(f, 590, ["1. Q nel triangolo con l'orizzontale o; f frontale per Q.  2. r per Q: r₁ ⊥ o₁, r₂ ⊥ f₂.",
               "3. Un punto qualunque S di r; γ (t₁γ ≡ r₁) si ribalta su π₁: Q* e S* con le quote; r* = Q*S*.",
               "4. Su r* si misurano 3 cm: E*.  5. A ritroso: da E* perpendicolare a r₁ → E₁; richiamo → E₂ su r₂."])
f.salva(OUT + "b10-es2-segmento-3-cm.svg")

# ---------- 4b. nello spazio ----------
f = Figura(620, 500, 0, "Nello spazio: il segmento QE esce dal triangolo, perpendicolare, lungo 3 cm")
t = Triedro(f, (330, 230), X3=380, U=360, Y=230, Z=260, scala=0.8)
t.piani()
ng4, dg4 = piano(Q4, E4, (Q4[0], Q4[1], Q4[2] + 100))
t.piano(ng4, dg4, "viola", 0.10)
t.tracce(ng4, dg4, "viola")
t._poligono(T4, "blu", 0.30, "blu")
for X, nome, dx, dy in [(A4, "A", -16, 4), (B4, "B", 8, 6), (C4, "C", -14, 16)]:
    t.punto(X, nome, dx, dy, "blu")
t.segmento(o4[0], o4[1], "arancio", 1.6)
t.segmento(E4, add(Q4, n4, 3 * CM + 35), "rosso", 1.4)
t.segmento(Q4, E4, "verde", 3.2)
angolo_retto3d(t, Q4, n4, unit((o4[1][0] - o4[0][0], o4[1][1] - o4[0][1], 0)), 10)
for X, nome in [(Q4, "Q"), (E4, "E")]:
    t.richiamo(X, (X[0], X[1], 0))
t.punto((Q4[0], Q4[1], 0), "Q₁", 6, 16); t.punto((E4[0], E4[1], 0), "E₁", -22, -4)
t.segmento((Q4[0], Q4[1], 0), (E4[0], E4[1], 0), "nero", 1.6)
t.punto(Q4, "Q", 8, 14); t.punto(E4, "E", 8, -4, "verde")
t.testo(lerp(Q4, E4, 0.5), "3 cm", -40, 0, "verde", 13)
t.testo(add(Q4, n4, 3 * CM + 35), "r", 6, 0, "rosso", 15)
t.testo(o4[1], "o", 6, 4, "arancio", 15)
righe(f, 480, ["QE è perpendicolare al triangolo (e quindi anche alla sua orizzontale o). La prima proiezione",
               "Q₁E₁ sta sulla traccia del piano verticale γ ed è più corta di 3 cm: per misurare serve il ribaltamento."])
f.salva(OUT + "b10-spazio-es2-segmento-3-cm.svg")

# =========================================================================================
# 5. La scala in pianta: uno o due segni di interruzione (dal PDF «Il disegno della scala»)
# =========================================================================================
f = Figura(640, 330, 300, "La scala a due rampe in pianta: uno o due segni di interruzione", x0=0)


def vano(f, x0):
    for a, b in [((x0, 40), (x0 + 250, 40)), ((x0 + 250, 40), (x0 + 250, 250)),
                 ((x0 + 250, 250), (x0, 250))]:
        f._linea(a, b, "grigio", 6)
    return x0 + 20, x0 + 190


def segno(x_basso):
    """Il segno di interruzione: retta inclinata (circa 70 gradi) da (x_basso, 46) in su."""
    return lambda y: x_basso + (y - 46) * 36 / 98


def rampa(f, xa, xb, y0, y1, taglio=None, prima="nero", dopo="grigio"):
    """Gradini tra xa e xb; se c'e' il taglio, a sinistra del segno colore 'prima', a destra 'dopo'
    (tratteggiato se grigio)."""
    n = 9
    stile = lambda c: "4,3" if c == "grigio" else None
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    for x in xs:
        if taglio is None:
            f._linea((x, y0), (x, y1), prima, 1.2, stile(prima)); continue
        ys = (x - taglio(46)) * 98 / 36 + 46            # dove il segno incontra l'alzata x
        ys = min(max(ys, y0), y1)
        f._linea((x, y0), (x, ys), dopo, 1.2, stile(dopo))
        f._linea((x, ys), (x, y1), prima, 1.2, stile(prima))
    for y in (y0, y1):
        if taglio is None:
            f._linea((xa, y), (xb, y), prima, 1.2, stile(prima)); continue
        xc = min(max(taglio(y), xa), xb)
        f._linea((xa, y), (xc, y), prima, 1.2, stile(prima))
        f._linea((xc, y), (xb, y), dopo, 1.2, stile(dopo))


# a sinistra: pianta del piano terra, un solo segno
x0 = 40
xa, xb = vano(f, x0)
tg = segno(xa + 78)
rampa(f, xa, xb, 50, 140, tg)                       # rampa 1: prima del segno piena, dopo tratteggiata
rampa(f, xa, xb, 150, 240, None, "grigio")          # rampa 2: sopra il piano di sezione
for a, b in [((xb, 50), (x0 + 240, 50)), ((x0 + 240, 50), (x0 + 240, 240)), ((xb, 240), (x0 + 240, 240))]:
    f._linea(a, b, "grigio", 1.2, "4,3")            # pianerottolo
f._linea((tg(46), 46), (tg(144), 144), "nero", 2.2)
f.testo((x0, 250), "piano terra: un solo segno", 0, -14, "nero", 13, False)

# a destra: pianta di un piano intermedio, due segni
x0 = 350
xa, xb = vano(f, x0)
rampa(f, xa, xb, 50, 140)
rampa(f, xa, xb, 150, 240)
for a, b in [((xb, 50), (x0 + 240, 50)), ((x0 + 240, 50), (x0 + 240, 240)), ((xb, 240), (x0 + 240, 240))]:
    f._linea(a, b, "nero", 1.2)
for xb_ in (xa + 70, xa + 86):
    tg = segno(xb_)
    f._linea((tg(46), 46), (tg(144), 144), "nero", 2.2)
f.testo((x0, 250), "piano intermedio: due segni", 0, -14, "nero", 13, False)
righe(f, 290, ["A sinistra la rampa è tagliata una volta: oltre il segno la scala sale sopra il piano di sezione",
               "e si tratteggia. A destra c'è una scala sopra e una sotto: i segni sono due, e i gradini che",
               "salgono dal piano inferiore, visti dall'alto, non si tratteggiano."])
f.h = 345
f.salva(OUT + "b10-scala-uno-o-due-segni.svg")
print("ok", round(dPH, 1), E4, Q4)
