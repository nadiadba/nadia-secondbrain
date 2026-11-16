"""Schemi nello spazio per la bozza di geometria descrittiva del 12 novembre (12-...).

Gli schemi sul foglio sono quelli della sbobina (geometria-12.py); qui ci sono due viste
del triedro in piu':
- il piano proiettante in seconda che ruota intorno a t2alfa fino a coincidere con pi2
  (la figura non si restringe: il lato AB, perpendicolare a pi2, resta lungo uguale);
- il piano generico con un'orizzontale o e una frontale f: t1alfa e' parallela a o (e a o1),
  t2alfa e' parallela a f (e a f2), non a un lato qualunque della figura.

Usa disegni_monge.py senza modificarlo. Le misure vengono controllate con i conti.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, piano, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"


def arco3d(t, c, e1, e2, r, a0, a1, colore="grigio", n=40):
    """Arco nello spazio: c + r (cos a e1 + sin a e2), disegnato nel triedro."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(t._p(tuple(c[j] + r * (math.cos(a) * e1[j] + math.sin(a) * e2[j]) for j in range(3))))
    dd = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    t.f.parti.append(f'<path d="{dd}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                     f'stroke-width="1.2" stroke-dasharray="5,3"/>')


def somma(a, b, k=1.0):
    return tuple(a[j] + k * b[j] for j in range(3))


def nota_righe(f, y, righe):
    for i, r in enumerate(righe):
        f.nota(20, y + 17 * i, r)


def triedro(titolo, h=500, w=620, etichette=True):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, (272, 205), X3=400, U=360, Y=230, Z=220, scala=0.75)
    t.piani(etichette)
    return f, t


# =========================================================================================
# 1. Piano proiettante in seconda: rotazione intorno a t2alfa fino a pi2
# =========================================================================================
f, t = triedro("Nello spazio: il piano proiettante in seconda ruota su π₂ intorno a t₂α", etichette=False)
t.testo((400 - 360 * 0.9, 0, 220 * 0.95), "π_2", colore="grigio")
t.testo((400 - 360 * 0.85, 230 * 0.8, 0), "π_1", colore="grigio")
t.testo((400, 230 * 0.75, 220 * 0.85), "π_3", colore="grigio")
t.testo((400 - 360, 0, 0), "LT", -22, 4, "nero")
PH = math.radians(40)
K = (80, 0, 0)
e = (math.cos(PH), 0, math.sin(PH))          # direzione di t2alfa (su pi2)
w = (-math.sin(PH), 0, math.cos(PH))         # su pi2, perpendicolare a t2alfa
Yd = (0, 1, 0)                               # direzione dell'aggetto, perpendicolare a pi2
n, dd = piano(K, somma(K, e), somma(K, Yd))
t.piano(n, dd, "blu", 0.14)
t.tracce(n, dd, "nero")
t.testo(somma(K, e, 300), "t_2α", -40, 0)
t.testo((K[0], 200, 0), "t_1α", 10, 4)

# (s lungo t2alfa, aggetto): A e B hanno la stessa s, quindi A2 = B2
TRI = {"A": (120, 120), "B": (120, 50), "C": (250, 70)}
P, P2, Pr = {}, {}, {}
for k, (s, y) in TRI.items():
    P2[k] = somma(K, e, s)
    P[k] = somma(P2[k], Yd, y)
    Pr[k] = somma(P2[k], w, y)
    arco3d(t, P2[k], Yd, w, y, 0, 90, "rosso")
    t.richiamo(P[k], P2[k])
# controllo: la figura ribaltata ha gli stessi lati di quella vera
for a, b in ("AB", "BC", "CA"):
    assert abs(math.dist(P[a], P[b]) - math.dist(Pr[a], Pr[b])) < 1e-9
assert abs(math.dist(Pr["A"], Pr["B"]) - 70) < 1e-9
for p in Pr.values():
    assert 400 - 360 <= p[0] <= 400 and 0 <= p[2] <= 220
t._poligono([P[k] for k in "ABC"], "blu", 0.3, "blu")
t._poligono([Pr[k] for k in "ABC"], "rosso", 0.2, "rosso")
t.segmento(P2["A"], P2["C"], "blu", 3)
et = {"A": (8, 14), "B": (4, -10), "C": (8, -4)}
etr = {"A": (-28, -2), "B": (-30, -4), "C": (-10, -10)}
for k in "ABC":
    t.punto(P[k], k, *et[k], "blu")
    t.punto(Pr[k], k + "*", *etr[k], "rosso")
t.punto(P2["A"], "A_2 ≡ B_2", -92, 14, "blu")
t.punto(P2["C"], "C_2", -30, 2, "blu")
nota_righe(f, 452, [
    "Il piano è perpendicolare a π₂: tutta la figura si proietta su t₂α. Ogni punto ruota su un arco",
    "che ha centro nella sua seconda proiezione e raggio uguale al suo aggetto. A e B hanno la stessa",
    "seconda proiezione: dopo la rotazione A*B* è lungo come AB. La figura gira, non si restringe.",
])
f.salva(OUT + "b12-spazio-proiettante-in-seconda-su-pi2.svg")

# =========================================================================================
# 2. Il piano generico con un'orizzontale e una frontale
# =========================================================================================
f, t = triedro("Nello spazio: le tracce del piano sono parallele all'orizzontale e alla frontale")
K = (60, 0, 0)
Q2 = (260, 0, 200)     # su t2alfa
Q1 = (300, 180, 0)     # su t1alfa
n, dd = piano(K, Q2, Q1)
t.piano(n, dd, "blu", 0.14)
t.tracce(n, dd, "nero")
t.testo(somma(K, (1, 0, 1), 175), "t_2α", -40, 0)
t.testo(somma(K, (1, 0.75, 0), 290), "t_1α", -10, 20)
d1 = tuple((Q1[j] - K[j]) / 240 for j in range(3))      # direzione di t1alfa (x di passo 1)
d2 = tuple((Q2[j] - K[j]) / 200 for j in range(3))      # direzione di t2alfa
H, AG = 90, 110                                         # quota dell'orizzontale, aggetto della frontale
T2o = somma(K, d2, H)                 # (150, 0, 90)
T1f = somma(K, d1, AG / 0.75)         # aggetto 110 sulla t1alfa
A = somma(T2o, d1, AG / 0.75)         # punto comune a o e f
assert abs(A[1] - AG) < 1e-9 and abs(A[2] - H) < 1e-9
assert abs(sum(n[j] * A[j] for j in range(3)) - dd) < 1e-6
assert abs(math.dist(somma(T1f, d2, H), A)) < 1e-9      # A sta anche sulla frontale
o_fine = somma(T2o, d1, 200)
f_fine = somma(T1f, d2, 150)
assert f_fine[2] <= 220 and o_fine[1] <= 230
t.segmento(T2o, o_fine, "verde", 2.2)
t.segmento(T1f, f_fine, "arancio", 2.2)
# proiezioni o1 (su pi1) e f2 (su pi2), e richiami delle tracce sulla LT
o1a, o1b = (T2o[0], 0, 0), (o_fine[0], o_fine[1], 0)
f2a, f2b = (T1f[0], 0, 0), (f_fine[0], 0, f_fine[2])
t.segmento(o1a, o1b, "verde", 1.2, "6,4")
t.segmento(f2a, f2b, "arancio", 1.2, "6,4")
t.richiamo(T2o, o1a)
t.richiamo(T1f, f2a)
t.richiamo(A, (A[0], A[1], 0))
t.richiamo(A, (A[0], 0, A[2]))
t.punto(T2o, "T_{2o}", -40, -6, "verde")
t.punto(T1f, "T_{1f}", -12, 20, "arancio")
t.punto(A, "A", -22, 18, "blu")
t.testo(o_fine, "o", 6, 4, "verde")
t.testo(f_fine, "f", 6, 4, "arancio")
t.testo((o1b[0], o1b[1], 0), "o_1", 6, 14, "verde", 13)
t.testo(f2b, "f_2", 6, -2, "arancio", 13)
nota_righe(f, 452, [
    "L'orizzontale o sta alla quota di A ed è parallela a t₁α; la frontale f sta all'aggetto di A ed è",
    "parallela a t₂α. Per questo t₁α passa per T₁f ed è parallela a o₁, t₂α passa per T₂o ed è",
    "parallela a f₂: le due tracce si incontrano sulla LT.",
])
f.salva(OUT + "b12-spazio-tracce-orizzontale-frontale.svg")
print("ok")
