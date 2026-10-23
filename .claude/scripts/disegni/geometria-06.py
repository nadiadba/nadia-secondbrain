import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import (Figura, P1, P2, tracce_retta, piano, tracce_piano, interseca,
                           direzione, perpendicolare)

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def pt_su(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


# 1. Punto di un piano generico, con l'orizzontale ------------------------------
f = Figura(620, 360, 175, "Un punto P del piano generico α, con un'orizzontale o", x0=40)
f.lt(-20, 560)
K = (60, 0)
t2a = (400, 160)
t1a = (400, -165)
f.traccia(K, t2a); f.testo(t2a, "t_2α", 4, 4)
f.traccia(K, t1a); f.testo(t1a, "t_1α", 4, 10)
h = 95
T2o2 = interseca(K, t2a, (0, h), (1, h))           # T2o'' su t2α
T2o1 = (T2o2[0], 0)
d1 = direzione(K, t1a)                               # o' parallela a t1α
o1_fine = lungo(T2o1, d1, 300)
f.retta(T2o2, (540, h), "arancio"); f.testo((540, h), "o₂", -18, -8, "arancio")
f.retta(T2o1, o1_fine, "arancio"); f.testo(o1_fine, "o₁", -22, 2, "arancio")
f.testo(o1_fine, "T_{1o}∞", -40, 20, "arancio")
f.richiamo(T2o2[0], T2o2[1], 0)
f.punto(T2o2, "T_{2o}", -46, -8); f.punto(T2o1, "(T_{2o})₁", -12, 20)
xP = 430
P2p = (xP, h)
P1p = interseca(T2o1, o1_fine, (xP, 0), (xP, -1))
f.richiamo(xP, P2p[1], P1p[1])
f.punto(P2p, "P₂", 6, -8, "rosso"); f.punto(P1p, "P₁", 8, 14, "rosso")
f.salva(OUT + "06-punto-piano-generico-orizzontale.svg")

# 2. Piano proiettante in seconda, punto e frontale -----------------------------
f = Figura(600, 350, 180, "Piano β proiettante in seconda: un punto P e la frontale f", x0=30)
f.lt(-10, 560)
K = (200, 0)
f.traccia(K, (200, -150)); f.testo((200, -150), "t_1β", 6, 4)
t2b = (480, 140)
f.traccia(K, t2b); f.testo(t2b, "t_2β ≡ f₂", 8, 4)
f.angolo_retto(K, (1, 0), (0, -1))
xP = 380
P2p = interseca(K, t2b, (xP, 0), (xP, 1))
P1p = (xP, -85)
f.retta((200, -85), (540, -85), "verde"); f.testo((540, -85), "f₁", -14, -8, "verde")
f.punto((200, -85), "T_{1f}", -52, 16)
f.punto(K, "(T_{1f})₂", -44, -8)
f.testo(t2b, "T_{2f}∞", 8, 24, "verde")
f.richiamo(xP, P2p[1], P1p[1])
f.punto(P2p, "P₂", -26, -6, "rosso"); f.punto(P1p, "P₁", 8, 16, "rosso")
f.salva(OUT + "06-piano-proiettante-in-seconda-frontale.svg")

# 3. Retta generica e i due punti notevoli sulla LT -----------------------------
f = Figura(600, 340, 175, "Retta generica r: i punti notevoli sulla linea di terra", x0=30)
f.lt(-10, 530)
a, b = 140, 380
T1r1, T1r2 = (a, -70), (a, 0)
T2r2, T2r1 = (b, 125), (b, 0)
d2 = direzione(T1r2, T2r2); d1 = direzione(T1r1, T2r1)
f.retta(lungo(T1r2, d2, -60), lungo(T2r2, d2, 30), "rosso"); f.testo(lungo(T2r2, d2, 30), "r₂", 4, 0, "rosso")
f.retta(lungo(T1r1, d1, -60), lungo(T2r1, d1, 60), "rosso"); f.testo(lungo(T2r1, d1, 60), "r₁", 6, 4, "rosso")
f.richiamo(a, 0, T1r1[1]); f.richiamo(b, 0, T2r2[1])
f.punto(T1r2, "(T_{1r})₂", -18, -10); f.punto(T1r1, "T_{1r}", 8, 16)
f.punto(T2r1, "(T_{2r})₁", 6, 18); f.punto(T2r2, "T_{2r}", -50, -6)
f.nota(20, 328, "(T₁ᵣ)₂ = seconda proiezione della prima traccia · (T₂ᵣ)₁ = prima proiezione della seconda traccia")
f.salva(OUT + "06-retta-generica-punti-notevoli.svg")

# 4. Triangolo con un lato orizzontale e uno frontale: le tracce del piano --------
A = (180, 40, 70)
B = (330, 100, 70)    # AB orizzontale (stessa quota)
C = (270, 40, 160)    # AC frontale (stesso aggetto)
T1o, T2o = tracce_retta(A, B)
T1f, T2f = tracce_retta(A, C)
n, d = piano(A, B, C)
f = Figura(660, 400, 225, "Triangolo ABC: dall'orizzontale o e dalla frontale f alle tracce del piano γ", x0=60)
f.lt(-40, 540)
t1, t2 = tracce_piano(n, d, 10, 470)
f.traccia(t1[0], (330, interseca(*t1, (330, 0), (330, 1))[1])); f.testo((330, interseca(*t1, (330, 0), (330, 1))[1]), "t_1γ", 4, 14)
f.traccia(t2[0], (190, interseca(*t2, (190, 0), (190, 1))[1])); f.testo((190, interseca(*t2, (190, 0), (190, 1))[1]), "t_2γ", -34, 0)
f.figura([P2(A), P2(B), P2(C)], "blu"); f.figura([P1(A), P1(B), P1(C)], "blu")
# orizzontale
f.retta(P2(T2o), (500, 70), "arancio"); f.testo((500, 70), "o₂", -4, -8, "arancio")
o1a = (T2o[0], 0); do1 = direzione(o1a, P1(B))
f.retta(o1a, lungo(o1a, do1, 330), "arancio"); f.testo(lungo(o1a, do1, 330), "o₁", 4, 4, "arancio")
f.testo(lungo(o1a, do1, 330), "T_{1o}∞", -10, 22, "arancio")
f.richiamo(T2o[0], P2(T2o)[1], 0)
f.punto(P2(T2o), "T_{2o}", -54, -6); f.punto(o1a, "(T_{2o})₁", -10, 18)
# frontale
f.retta(P1(T1f), (480, -40), "verde"); f.testo((480, -40), "f₁", 2, 14, "verde")
f1a = (T1f[0], 0); df2 = direzione(f1a, P2(C))
f.retta(f1a, lungo(f1a, df2, 250), "verde"); f.testo(lungo(f1a, df2, 250), "f₂  T_{2f}∞", -70, -4, "verde")
f.richiamo(T1f[0], 0, P1(T1f)[1])
f.punto(f1a, "(T_{1f})₂", -10, -10); f.punto(P1(T1f), "T_{1f}", -54, 14)
for p, nome, dx2, dy2, dx1, dy1 in [(A, "A", -18, -6, -20, 6), (B, "B", 6, -6, 6, 16), (C, "C", 10, 6, 4, -6)]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.punto(P2(p), nome + "₂", dx2, dy2); f.punto(P1(p), nome + "₁", dx1, dy1)
f.salva(OUT + "06-triangolo-tracce-piano-generico.svg")

# 5. Lo stesso triangolo in quattro posizioni ------------------------------------
f = Figura(990, 360, 185)
casi = [
    ("piano orizzontale", [(30, 40, 60), (170, 25, 60), (110, 115, 60)]),
    ("piano proiettante in seconda", [(40, 30, 14), (170, 50, 92), (110, 120, 56)]),
    ("piano proiettante in prima", [(40, 15, 40), (170, 80, 70), (100, 45, 130)]),
    ("piano frontale", [(30, 40, 40), (170, 40, 60), (100, 40, 135)]),
]
for i, (nome, pts) in enumerate(casi):
    ox = 30 + 245 * i
    f.nota(ox, 22, nome, 14)
    g = Figura(0, 0, 185, x0=ox)  # usa lo stesso sistema di coordinate, spostato
    g.parti = f.parti
    g.lt(-10, 215, etichetta=(i == 0))
    g.figura([P2(p) for p in pts], "blu"); g.figura([P1(p) for p in pts], "blu")
    for p, nome_p in zip(pts, "ABC"):
        g.richiamo(p[0], P2(p)[1], P1(p)[1])
        g.punto(P2(p), nome_p + "₂", 5, -5); g.punto(P1(p), nome_p + "₁", 5, 14)
    if i == 0:
        g.traccia((-10, 60), (215, 60)); g.testo((215, 60), "t_2γ", -22, 18)
        g.testo((150, -150), "t_1γ∞", 0, 0)
        g.testo((40, 95), "vera forma in prima proiezione", 0, 0, "grigio", 11, False)
    elif i == 1:
        x0 = 10 / 0.6
        g.traccia((x0, 0), (215, 0.6 * 215 - 10)); g.testo((215, 0.6 * 215 - 10), "t_2β", -28, -6)
        g.traccia((x0, 0), (x0, -140)); g.testo((x0, -140), "t_1β", 6, 4)
    elif i == 2:
        g.traccia((10, 0), (215, -(0.5 * 215 - 5))); g.testo((215, -(0.5 * 215 - 5)), "t_1δ", -30, 14)
        g.traccia((10, 0), (10, 140)); g.testo((10, 140), "t_2δ", -26, 8)
    else:
        g.traccia((-10, -40), (215, -40)); g.testo((215, -40), "t_1ε", -10, 22)
        g.testo((150, 150), "t_2ε∞", 0, 0)
        g.testo((10, -95), "vera forma in seconda proiezione", 0, 0, "grigio", 11, False)
f.salva(OUT + "06-triangolo-quattro-posizioni.svg")

# 6. Retta perpendicolare a un piano (teorema di Monge) ---------------------------
f = Figura(600, 380, 195, "Retta r perpendicolare al piano α: r₂ ⊥ t₂α e r₁ ⊥ t₁α", x0=40)
f.lt(-20, 540)
K = (40, 0); t2a = (440, 170); t1a = (440, -160)
f.traccia(K, t2a); f.testo(t2a, "t_2α", 4, 4)
f.traccia(K, t1a); f.testo(t1a, "t_1α", 4, 12)
P = (300, 60, 110)
d2 = perpendicolare(direzione(K, t2a)); d1 = perpendicolare(direzione(K, t1a))
f.retta(lungo(P2(P), d2, -50), lungo(P2(P), d2, 70), "rosso"); f.testo(lungo(P2(P), d2, 70), "r₂", 6, 4, "rosso")
f.retta(lungo(P1(P), d1, 80), lungo(P1(P), d1, -60), "rosso"); f.testo(lungo(P1(P), d1, 80), "r₁", 6, 0, "rosso")
X2 = interseca(P2(P), lungo(P2(P), d2, 1), K, t2a)
X1 = interseca(P1(P), lungo(P1(P), d1, 1), K, t1a)
f.angolo_retto(X2, direzione(X2, t2a), direzione(X2, P2(P)))
f.angolo_retto(X1, direzione(X1, t1a), direzione(X1, P1(P)))
f.richiamo(P[0], P2(P)[1], P1(P)[1])
f.punto(P2(P), "P₂", 8, -4, "rosso"); f.punto(P1(P), "P₁", 8, 14, "rosso")
f.salva(OUT + "06-retta-perpendicolare-al-piano.svg")

# 7. Due piani proiettanti in prima perpendicolari ---------------------------------
f = Figura(560, 360, 180, "Due piani proiettanti in prima γ e δ perpendicolari: t₁γ ⊥ t₁δ", x0=20)
f.lt(0, 520)
Q = (260, -110)
Kg = (Q[0] + 110 / 0.8, 0)       # t1γ: direzione (1, 0.8)
Kd = (Q[0] - 0.8 * 110, 0)        # t1δ: direzione (-0.8, 1)
f.traccia(Kg, lungo(Q, direzione(Q, Kg), -60)); f.testo(lungo(Q, direzione(Q, Kg), -60), "t_1γ", -30, 6)
f.traccia(Kd, lungo(Q, direzione(Q, Kd), -60)); f.testo(lungo(Q, direzione(Q, Kd), -60), "t_1δ", 6, 6)
f.traccia(Kg, (Kg[0], 160)); f.testo((Kg[0], 160), "t_2γ", 6, 4)
f.traccia(Kd, (Kd[0], 160)); f.testo((Kd[0], 160), "t_2δ", 6, 4)
f.angolo_retto(Q, direzione(Q, Kg), direzione(Q, Kd))
f.angolo_retto(Kg, (0, 1), (-1, 0))
# retta r di δ, perpendicolare a γ: r' su t1δ, r'' parallela a LT
h = 95
f.retta((Kd[0], h), (Kg[0], h), "rosso"); f.testo(((Kd[0] + Kg[0]) / 2, h), "r₂", 0, -8, "rosso")
f.retta(Kd, Q, "rosso", 3); f.testo(pt_su(Kd, Q, 0.5), "r₁ ≡ t₁δ", 8, 4, "rosso")
f.angolo_retto((Kg[0], h), (0, -1), (-1, 0))
f.salva(OUT + "06-piani-proiettanti-perpendicolari.svg")

# 8. Piano proiettante in prima perpendicolare a un piano generico -------------------
f = Figura(560, 380, 190, "Piano γ proiettante in prima perpendicolare al generico α: t₁γ ⊥ t₁α", x0=20)
f.lt(0, 520)
K = (440, 0); t2a = (230, 158); t1a = (40, -133)
f.traccia(K, t2a); f.testo(pt_su(K, t2a, 0.45), "t_2α", 4, -8)
f.traccia(K, t1a); f.testo(t1a, "t_1α", -8, 18)
M = interseca(K, t1a, (240, 0), (240, 1))
dg = direzione(M, (M[0] - 1, M[1] + 3))            # perpendicolare a t1α, verso l'alto
Kg = interseca(M, lungo(M, dg, 1), (0, 0), (1, 0))
f.traccia(Kg, lungo(M, dg, -35))
f.traccia(Kg, (Kg[0], 170)); f.testo((Kg[0], 170), "t_2γ", 6, 4)
f.angolo_retto(M, direzione(M, K), dg)
# retta r di γ perpendicolare ad α: r' su t1γ, r'' perpendicolare a t2α
P1p = lungo(M, dg, -25)
P2p = (P1p[0], 110)
d2 = perpendicolare(direzione(K, t2a))
f.retta(lungo(P2p, d2, -70), lungo(P2p, d2, 60), "rosso"); f.testo(lungo(P2p, d2, -70), "r₂", 4, 14, "rosso")
f.retta(lungo(M, dg, -35), Kg, "rosso", 3); f.testo(lungo(M, dg, -35), "r₁ ≡ t₁γ", 8, 14, "rosso")
X = interseca(P2p, lungo(P2p, d2, 1), K, t2a)
f.angolo_retto(X, direzione(X, K), direzione(X, P2p))
f.richiamo(P2p[0], P2p[1], P1p[1])
f.punto(P2p, "P₂", -24, -4, "rosso"); f.punto(P1p, "P₁", -24, 6, "rosso")
f.salva(OUT + "06-piano-perpendicolare-al-generico.svg")

# 9. Perpendicolare al piano del triangolo senza tracce: r′ ⊥ o′ e r″ ⊥ f″ ------------
f = Figura(640, 400, 205, "Senza tracce: r è perpendicolare al piano di ABC se r₁ ⊥ o₁ e r₂ ⊥ f₂", x0=40)
f.lt(-20, 560)
f.figura([P2(A), P2(B), P2(C)], "blu"); f.figura([P1(A), P1(B), P1(C)], "blu")
f.retta((120, 70), (470, 70), "arancio", 1.4); f.testo((470, 70), "o₂", 4, 4, "arancio")
do = direzione(P1(A), P1(B))
f.retta(lungo(P1(A), do, -60), lungo(P1(A), do, 330), "arancio", 1.4); f.testo(lungo(P1(A), do, 330), "o₁", 4, 4, "arancio")
f.retta((130, -40), (360, -40), "verde", 1.4); f.testo((130, -40), "f₁", -18, 4, "verde")
df = direzione(P2(A), P2(C))
f.retta(lungo(P2(A), df, -60), lungo(P2(A), df, 175), "verde", 1.4); f.testo(lungo(P2(A), df, 175), "f₂", 4, 0, "verde")
for p, nome, d2x, d2y, d1x, d1y in [(A, "A", -24, -6, -24, 14), (B, "B", 6, -6, -4, 18), (C, "C", -24, -4, 6, -6)]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.punto(P2(p), nome + "₂", d2x, d2y); f.punto(P1(p), nome + "₁", d1x, d1y)
Q2, Q1 = (420, 30), (420, -165)
r2 = perpendicolare(df); r1 = perpendicolare(do)
if r1[1] < 0: r1 = (-r1[0], -r1[1])
X2 = interseca(Q2, lungo(Q2, r2, 1), P2(A), P2(C))
X1 = interseca(Q1, lungo(Q1, r1, 1), P1(A), P1(B))
f.retta(lungo(Q2, direzione(Q2, X2), -40), lungo(X2, direzione(Q2, X2), 25), "rosso")
f.testo(lungo(Q2, direzione(Q2, X2), -40), "r₂", 6, 4, "rosso")
f.retta(lungo(Q1, r1, -25), lungo(X1, r1, 40), "rosso"); f.testo(lungo(Q1, r1, -25), "r₁", 8, 4, "rosso")
f.angolo_retto(X2, df, direzione(X2, Q2))
f.angolo_retto(X1, do, direzione(X1, Q1))
f.richiamo(420, Q2[1], Q1[1])
f.punto(Q2, "Q₂", 8, 14, "rosso"); f.punto(Q1, "Q₁", 8, 14, "rosso")
f.salva(OUT + "06-perpendicolare-con-orizzontale-e-frontale.svg")
print("ok")
