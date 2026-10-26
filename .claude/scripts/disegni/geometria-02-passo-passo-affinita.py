"""Tutorial grafico del Disegno 15 della bozza 02: l'affinita' ortogonale sul foglio, costruita una linea
alla volta come in un esercizio (dati u, la direzione di U_inf, il triangolo ABC e A'; trovare B' e C').

Stessi dati del disegno b02-affinita-ortogonale-foglio.svg (geometria-02-coppie.py).
Immagini: bozze/img/b02-aff-passo-NN.svg  -  Nota: bozze/02-affinita-ortogonale-passo-passo.md
"""
import importlib.util
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("coppie", os.path.join(QUI, "geometria-02-coppie.py"))
cp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cp)
g = cp.g
F, direzione, lungo, interseca, allineati = g.F, g.direzione, g.lungo, g.interseca, g.allineati
NUOVO = "arancio"

S, S1, T0, T, T1, U, dU, K = cp.dati(cp.CASI["affinita-ortogonale"])
xa, xb = cp.limiti(T, T1, U, K)
k = min(1.4, 540 / (xb - xa))
ox, oy = 30 - k * xa, 60


def s(p):
    return (ox + k * p[0], oy + k * p[2])


A, B, C = (s(X) for X in T)
A1, B1, C1 = (s(X) for X in T1)
ua, ub = s((xa, 0, 0)), s((xb, 0, 0))
d = (dU[0], dU[1])                                    # direzione di U_inf sul foglio (perpendicolare a u)
V1, V2, V3 = interseca(A, B, ua, ub), interseca(A, C, ua, ub), interseca(B, C, ua, ub)
assert allineati(V1, A1, B1) and allineati(V2, A1, C1) and allineati(V3, B1, C1)


def col(n, c):
    return NUOVO if n else c


def sp(n, x):
    return x + 1.6 if n else x


def oltre2(p, q, px=26):
    """Segmento da p a q, prolungato di px oltre q."""
    return p, lungo(q, direzione(p, q), px)


def parallela(f, P, Q, n, c="grigio"):
    """Retta per P (e Q) parallela alla direzione di U_inf, un po' oltre i due punti."""
    lo = min((P, Q), key=lambda X: X[1]); hi = max((P, Q), key=lambda X: X[1])
    f.linea(lungo(lo, d, -24), lungo(hi, d, 24), col(n, c), sp(n, 1), "5,4")


PASSI = []


def passo(testo):
    def dec(fn):
        PASSI.append((testo, fn))
        return fn
    return dec


@passo("I dati: l'asse u e la direzione di U∞ (la lineetta), perpendicolare all'asse.")
def _(f, n):
    f.linea(lungo(ua, (-1, 0), 10), lungo(ub, (1, 0), 10), col(n, "nero"), sp(n, 2.4))
    f.testo(lungo(ub, (1, 0), 10), "u", 4, 4, col(n, "nero"), 16)
    f.U_inf((585, 120), d, "U_∞", -40, -10)


@passo("I dati: il triangolo ABC.")
def _(f, n):
    f.poligono([A, B, C], col(n, "blu"), 0.10, sp(n, 1.8))
    for P, nm in ((A, "A"), (B, "B"), (C, "C")):
        f.punto(P, nm, 8, -4, col(n, "blu"))


@passo("I dati: A′, sulla retta per A parallela alla direzione di U∞ (perpendicolare all'asse).")
def _(f, n):
    parallela(f, A, A1, n)
    f.punto(A1, "A′", -24, 6, col(n, "verde"))


@passo("Prolunga il lato AB fino all'asse: lì c'è il primo punto unito, V₁.")
def _(f, n):
    f.linea(*oltre2(A, V1, 0), col(n, "blu"), sp(n, 1), "3,3")
    f.unito(V1, "V_1", -6, 22)


@passo("Dal punto unito V₁ tira la retta che passa per A′ e prolungala.")
def _(f, n):
    f.linea(*oltre2(V1, B1, 30), col(n, "verde"), sp(n, 1), "3,3")


@passo("Per B tira la parallela alla direzione di U∞ (perpendicolare all'asse).")
def _(f, n):
    parallela(f, B, B1, n)


@passo("B′ NON si sceglie: è l'incrocio tra la retta da V₁ per A′ e la parallela per B.")
def _(f, n):
    f.punto(B1, "B′", -26, 6, col(n, "verde"))


@passo("Prolunga il lato AC fino all'asse: secondo punto unito, V₂.")
def _(f, n):
    f.linea(*oltre2(A, V2, 0), col(n, "blu"), sp(n, 1), "3,3")
    f.unito(V2, "V_2", -6, 22)


@passo("Dal punto unito V₂ tira la retta che passa per A′ e prolungala.")
def _(f, n):
    far = max((A1, C1), key=lambda X: math.dist(V2, X))
    f.linea(*oltre2(V2, far, 30), col(n, "verde"), sp(n, 1), "3,3")


@passo("Per C tira la parallela alla direzione di U∞.")
def _(f, n):
    parallela(f, C, C1, n)


@passo("C′ NON si sceglie: è l'incrocio tra la retta da V₂ per A′ e la parallela per C.")
def _(f, n):
    f.punto(C1, "C′", -26, 6, col(n, "verde"))


@passo("Unisci A′, B′ e C′: è il triangolo corrispondente.")
def _(f, n):
    f.poligono([A1, B1, C1], col(n, "verde"), 0.12, sp(n, 1.8))


@passo("Verifica: prolungati, i lati BC e B′C′ si incontrano anche loro sull'asse (V₃).")
def _(f, n):
    far = max((B, C), key=lambda X: math.dist(V3, X)); far1 = max((B1, C1), key=lambda X: math.dist(V3, X))
    f.linea(V3, far, col(n, "blu"), sp(n, 1), "3,3"); f.linea(V3, far1, col(n, "verde"), sp(n, 1), "3,3")
    f.unito(V3, "V_3", -6, 22)


TOT = len(PASSI)
PUNTI = {2, 3, 6, 7, 10, 12}                         # passi che mettono punti: sopra alle linee
for kk in range(TOT):
    f = F(640, 470, f"Affinità ortogonale, passo {kk + 1} di {TOT}")
    fatti = list(range(kk + 1))
    for i in [i for i in fatti if i not in PUNTI] + [i for i in fatti if i in PUNTI]:
        PASSI[i][1](f, i == kk)
    f.didascalia(PASSI[kk][0], 12)
    f.salva(g.BZ + f"b02-affinita-passo-{kk + 1:02d}.svg")
print(TOT, "passi")
