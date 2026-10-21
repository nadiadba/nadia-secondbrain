"""Schemi per la sbobina di geometria descrittiva del 15 ottobre (05-...).

Usa disegni_monge.py senza modificarlo. Qui sotto ci sono in piu' le funzioni per la
terza proiezione: pi3 sta a destra di un asse verticale (x = XA nel disegno), e un punto
(x, aggetto, quota) ha P''' = (XA + aggetto, quota). Gli archi di richiamo vanno da P'
all'asse e poi, con un quarto di circonferenza centrato su LT, fino alla LT a destra.
"""
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, P1, P2, interseca, direzione, su_lt, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def P3(p, xa):
    return (xa + p[1], p[2])


def asse(f, xa, y1, y2):
    """Asse verticale che separa pi2 da pi3 (sopra) e pi1 (sotto)."""
    f._linea((xa, y1), (xa, y2), "nero", 1.2)


def arco(f, xa, y):
    """Richiamo da pi1 a pi3: orizzontale da (x, -y) all'asse, poi quarto di cerchio fino a (xa+y, 0)."""
    sx, sy = f._s((xa, -y))
    ex, ey = f._s((xa + y, 0))
    f.parti.append(f'<path d="M {sx:.1f} {sy:.1f} A {y:.1f} {y:.1f} 0 0 0 {ex:.1f} {ey:.1f}" '
                   f'fill="none" stroke="{COLORI["grigio"]}" stroke-width="0.9" stroke-dasharray="3,3"/>')


def richiamo_orizz(f, x1, x2, y):
    f._linea((x1, y), (x2, y), "grigio", 0.9, "3,3")


def nome_piano(f, x, y, testo):
    f.nota(x, y, testo, 13)


# Piano proiettante in seconda: z = M (x - X0), per ogni aggetto
X0, M, XA = 120, 0.62, 400


def quota(x):
    return M * (x - X0)


# 1. Il piano proiettante in seconda con le tre tracce -----------------------------
f = Figura(620, 410, 190, "Piano α proiettante in seconda: le tre tracce", x0=30)
f.lt(-10, 570)
asse(f, XA, 175, -175)
f.testo((XA, 40), "π_2", -30, 0, "grigio"); f.testo((XA, 40), "π_3", 12, 0, "grigio")
f.testo((XA, -175), "π_1", -34, -4, "grigio")
H = quota(XA)
f.traccia((X0, 0), (XA, H)); f.testo(((X0 + XA) / 2, quota((X0 + XA) / 2)), "t_2α", -36, -6)
f.traccia((X0, 0), (X0, -165)); f.testo((X0, -165), "t_1α", 8, 4)
f.angolo_retto((X0, 0), (1, 0), (0, -1))
f.traccia((XA, H), (560, H)); f.testo((560, H), "t_3α", -30, -8)
f.richiamo(XA, 0, H)
f.punto((XA, H))
f.nota(20, 402, "t₁α ⊥ LT · t₂α inclinata · t₃α parallela alla LT: t₂α e t₃α si incontrano sull'asse di π₃")
f.salva(OUT + "04-piano-proiettante-in-seconda-tre-tracce.svg")

# 2. Triangolo nel piano proiettante in seconda: dalla prima alla seconda e terza ----
A = (250, 40, quota(250))
B = (250, 120, quota(250))   # AB proiettante in seconda: stessa x e stessa quota
C = (330, 70, quota(330))
f = Figura(660, 430, 200, "Triangolo ABC nel piano proiettante in seconda α", x0=30)
f.lt(-10, 610)
asse(f, XA, 185, -185)
f.traccia((X0, 0), (XA, H)); f.testo((XA, H), "t_2α", -50, -8)
f.traccia((X0, 0), (X0, -175)); f.testo((X0, -175), "t_1α", 8, 4)
f.traccia((XA, H), (600, H)); f.testo((600, H), "t_3α", -30, -8)
for p in (A, B, C):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    richiamo_orizz(f, p[0], XA, -p[1])
    arco(f, XA, p[1])
    f.richiamo(XA + p[1], 0, p[2])
    richiamo_orizz(f, p[0], XA + p[1], p[2])
f.figura([P1(A), P1(B), P1(C)], "blu")
f.retta(P2(A), P2(C), "blu", 4)
f.figura([P3(A, XA), P3(B, XA), P3(C, XA)], "rosso")
f.punto(P1(A), "A₁", -24, 4); f.punto(P1(B), "B₁", -24, 6); f.punto(P1(C), "C₁", 8, 6)
f.punto(P2(A), "A₂ ≡ B₂", -64, -8); f.punto(P2(C), "C₂", -10, -12)
f.punto(P3(A, XA), "A₃", -14, 20); f.punto(P3(B, XA), "B₃", 2, 20); f.punto(P3(C, XA), "C₃", 8, -6)
f.nota(20, 422, "A₃B₃ è parallelo alla LT: A e B hanno la stessa quota, AB è una retta proiettante in seconda")
f.salva(OUT + "04-triangolo-piano-proiettante-in-seconda.svg")

# 3. Piani che contengono una retta proiettante in prima ----------------------------
f = Figura(620, 405, 190, "Piani che contengono la retta r proiettante in prima", x0=30)
f.lt(-10, 570)
xr, yr = 250, 90
T1 = (xr, -yr)
f.retta((xr, 0), (xr, 170), "rosso", 2); f.testo((xr, 150), "r₂", 6, 0, "rosso")
# frontale alfa: t1 parallela alla LT per T1r'
f.traccia((-5, -yr), (560, -yr), "verde"); f.testo((560, -yr), "t_1α", -30, 18, "verde")
f.testo((480, 150), "t_2α∞", 0, 0, "verde")
# profilo gamma: x = xr, tracce sulla stessa perpendicolare alla LT
f.traccia((xr, 0), (xr, -175), "viola"); f.testo((xr, -175), "t_1γ", 8, 4, "viola")
f._linea((xr, 0), (xr, 175), "viola", 4.5)
f.retta((xr, 0), (xr, 170), "rosso", 1.8)
f.testo((xr, 175), "t_2γ", -34, 10, "viola")
# proiettante in prima beta: t1 inclinata per T1r', t2 perpendicolare alla LT
Kb = (130, 0)
db = direzione(Kb, T1)
f.traccia(Kb, lungo(Kb, db, 250), "blu"); f.testo(lungo(Kb, db, 250), "t_1β", 6, 8, "blu")
f.traccia(Kb, (Kb[0], 170), "blu"); f.testo((Kb[0], 170), "t_2β", 6, 4, "blu")
f.punto(T1, "r₁ ≡ T_{1r}", 10, -8, "rosso")
f.punto((xr, 0), "(T_{1r})₂", 6, 18)
f.nota(20, 398, "verde: α frontale · viola: γ di profilo (t₂γ contiene r₂) · blu: β proiettante in prima")
f.salva(OUT + "04-piani-per-retta-proiettante-in-prima.svg")

# 4. Piani che contengono una retta proiettante in seconda ---------------------------
f = Figura(620, 405, 190, "Piani che contengono la retta r proiettante in seconda", x0=30)
f.lt(-10, 570)
xr, zr = 250, 90
T2 = (xr, zr)
f.retta((xr, 0), (xr, -170), "rosso", 2); f.testo((xr, -150), "r₁", 6, 0, "rosso")
# proiettante in seconda beta
Kb = (110, 0)
db = direzione(Kb, T2)
f.traccia(Kb, lungo(Kb, db, 330), "blu"); f.testo(lungo(Kb, db, 330), "t_2β", 6, 4, "blu")
f.traccia(Kb, (Kb[0], -170), "blu"); f.testo((Kb[0], -170), "t_1β", 6, 4, "blu")
# orizzontale alfa
f.traccia((-5, zr), (560, zr), "verde"); f.testo((560, zr), "t_2α", -30, -8, "verde")
f.testo((480, -150), "t_1α∞", 0, 0, "verde")
# profilo gamma
f.traccia((xr, 0), (xr, 175), "viola"); f.testo((xr, 175), "t_2γ", 8, 10, "viola")
f._linea((xr, 0), (xr, -175), "viola", 4.5)
f.retta((xr, 0), (xr, -170), "rosso", 1.8)
f.testo((xr, -175), "t_1γ", -34, 0, "viola")
f.punto(T2, "r₂ ≡ T_{2r}", -98, -10, "rosso")
f.punto((xr, 0), "(T_{2r})₁", 6, 18)
f.nota(20, 398, "blu: β proiettante in seconda · verde: α orizzontale · viola: γ di profilo (t₁γ contiene r₁)")
f.salva(OUT + "04-piani-per-retta-proiettante-in-seconda-riepilogo.svg")

# Piano generico per gli schemi 5-7
K = (60, 0)
t2a = (460, 170)
t1a = (460, -170)

# 5. Punto del piano generico con un'orizzontale -------------------------------------
f = Figura(600, 370, 180, "Un punto P del piano generico α, con l'orizzontale o", x0=20)
f.lt(-10, 570)
f.traccia(K, t2a); f.testo(t2a, "t_2α", 4, 4)
f.traccia(K, t1a); f.testo(t1a, "t_1α", 4, 12)
h = 100
T2o2 = interseca(K, t2a, (0, h), (1, h))
T2o1 = (T2o2[0], 0)
d1 = direzione(K, t1a)
o1_fine = lungo(T2o1, d1, 250)
f.retta(T2o2, (540, h), "arancio"); f.testo((540, h), "o₂", -18, -8, "arancio")
f.retta(T2o1, o1_fine, "arancio"); f.testo(o1_fine, "o₁", 6, 0, "arancio")
f.testo(o1_fine, "T_{1o}∞", -50, 22, "arancio")
f.richiamo(T2o2[0], T2o2[1], 0)
f.punto(T2o2, "T_{2o}", -46, -8); f.punto(T2o1, "(T_{2o})₁", -10, 20)
xP = 420
P1p = interseca(T2o1, o1_fine, (xP, 0), (xP, -1))
f.richiamo(xP, h, P1p[1])
f.punto((xP, h), "P₂", 6, -8, "rosso"); f.punto(P1p, "P₁", 8, -8, "rosso")
f.salva(OUT + "04-punto-piano-generico-orizzontale.svg")

# 6. P appartiene ad alfa? Verifica con una retta generica ----------------------------
f = Figura(600, 395, 180, "P appartiene ad α? Verifica con una retta generica r", x0=20)
f.lt(-10, 570)
f.traccia(K, t2a); f.testo(t2a, "t_2α", 4, 4)
f.traccia(K, t1a); f.testo(t1a, "t_1α", 4, 12)
T2r2 = interseca(K, t2a, (300, 0), (300, 1))
P2p = (360, 55)
T1r2 = su_lt(T2r2, P2p)
T2r1 = (T2r2[0], 0)
T1r1 = interseca(K, t1a, (T1r2[0], 0), (T1r2[0], -1))
d2 = direzione(T2r2, T1r2)
f.retta(T2r2, lungo(T1r2, d2, 25), "rosso"); f.testo(((T2r2[0] + P2p[0]) / 2, (T2r2[1] + P2p[1]) / 2), "r₂", 4, -6, "rosso")
d1 = direzione(T2r1, T1r1)
f.retta(T2r1, lungo(T1r1, d1, 25), "rosso"); f.testo(lungo(T2r1, d1, 35), "r₁", -24, 4, "rosso")
f.richiamo(T2r2[0], T2r2[1], 0)
f.richiamo(T1r2[0], 0, T1r1[1])
f.punto(T2r2, "T_{2r}", -50, -6); f.punto(T2r1, "(T_{2r})₁", -50, 18)
f.punto(T1r2, "(T_{1r})₂", 6, -8); f.punto(T1r1, "T_{1r}", -54, 12)
X = interseca(T2r1, T1r1, (P2p[0], 0), (P2p[0], 1))
P1p = (P2p[0], -40)
f.richiamo(P2p[0], P2p[1], X[1] - 10)
f.punto(P2p, "P₂", -8, -10, "blu"); f.punto(P1p, "P₁", 8, -2, "blu")
f.parti.append('<circle cx="{:.1f}" cy="{:.1f}" r="4" fill="none" stroke="{}" stroke-width="1.2"/>'.format(
    *f._s(X), COLORI["rosso"]))
f.testo(X, "qui P₁ starebbe su r₁", 8, 12, "grigio", 11, False)
f.nota(20, 388, "P₂ sta su r₂, ma P₁ non sta su r₁: P non appartiene alla retta r, quindi P non appartiene ad α")
f.salva(OUT + "04-verifica-punto-con-retta-generica.svg")

# 7. Frontale del piano generico e un punto su di essa ---------------------------------
f = Figura(600, 370, 180, "Una frontale f del piano generico α e un punto P su f", x0=20)
f.lt(-10, 570)
f.traccia(K, t2a); f.testo(t2a, "t_2α", 4, 4)
f.traccia(K, t1a); f.testo(t1a, "t_1α", 4, 12)
yf = 70
T1f1 = interseca(K, t1a, (0, -yf), (1, -yf))
T1f2 = (T1f1[0], 0)
f.retta(T1f1, (540, -yf), "verde"); f.testo((540, -yf), "f₁", -16, 18, "verde")
d2 = direzione(K, t2a)
f2_fine = lungo(T1f2, d2, 340)
f.retta(T1f2, f2_fine, "verde"); f.testo(f2_fine, "f₂", 6, 4, "verde")
f.testo(f2_fine, "T_{2f}∞", -60, -12, "verde")
f.richiamo(T1f2[0], 0, -yf)
f.punto(T1f2, "(T_{1f})₂", -14, -10); f.punto(T1f1, "T_{1f}", -44, 18)
xP = 400
P2p = interseca(T1f2, f2_fine, (xP, 0), (xP, 1))
f.richiamo(xP, P2p[1], -yf)
f.punto(P2p, "P₂", -8, -10, "rosso"); f.punto((xP, -yf), "P₁", 6, 16, "rosso")
f.salva(OUT + "04-frontale-piano-generico.svg")
print("ok")
