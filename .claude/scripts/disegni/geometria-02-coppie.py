"""Coppie di disegni per le omologie particolari della bozza 02: lo stesso caso disegnato sul foglio
(il piano alfa visto dall'alto) e nello spazio (con la vista del disegno dei due centri).

Alfa e' il piano y = 0 (il foglio). Il piano della figura di partenza alfa0 e':
- verticale (z = 0) nell'affinita': si taglia con alfa lungo l'asse u (asse x), asse proprio;
- orizzontale (y = h) nell'omotetia e nella traslazione: e' parallelo ad alfa, asse improprio u_inf.
I due centri S e S1 sono allineati parallelamente al foglio (stessa altezza) nell'affinita' e nella
traslazione: la retta S S1 non buca il foglio, il centro U e' improprio (U_inf, direzione S -> S1).

Immagini: bozze/img/b02-<caso>-foglio.svg e b02-<caso>-spazio.svg
"""
import importlib.util
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("g02", os.path.join(QUI, "geometria-02.py"))
g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g)

F, su_piano3, direzione, lungo, allineati, paralleli = g.F, g.su_piano3, g.direzione, g.lungo, g.allineati, g.paralleli
BZ = g.BZ

CASI = {
    "affinita-ortogonale": dict(
        titolo="Affinità ortogonale", S=(0, 220, -200), S1=(0, 220, -60),
        piano=("verticale",), T0=[(-40, 80, 0), (0, 120, 0), (120, 40, 0)]),
    "affinita-obliqua": dict(
        titolo="Affinità obliqua", S=(100, 220, -160), S1=(200, 220, -100),
        piano=("verticale",), T0=[(40, 40, 0), (160, 120, 0), (200, 80, 0)]),
    "omotetia": dict(
        titolo="Omotetia", S=(200, 280, -160), S1=(140, 220, -120),
        piano=("orizzontale", 130), T0=[(120, 130, 0), (200, 130, -60), (200, 130, 0)]),
    "traslazione": dict(
        titolo="Traslazione", S=(0, 340, -220), S1=(120, 340, -220),
        piano=("orizzontale", 130), T0=[(20, 130, -60), (120, 130, -40), (60, 130, 50)]),
}

def dati(c):
    S, S1, T0 = c["S"], c["S1"], c["T0"]
    T = [su_piano3(S, X, 1, 0) for X in T0]
    T1 = [su_piano3(S1, X, 1, 0) for X in T0]
    proprio_U = abs(S[1] - S1[1]) > 1e-9
    U = su_piano3(S, S1, 1, 0) if proprio_U else None
    dU = None if proprio_U else direzione((S[0], S[2]), (S1[0], S1[2]))
    verticale = c["piano"][0] == "verticale"
    K = [su_piano3(T0[i], T0[j], 1, 0) for i, j in ((0, 1), (1, 2), (2, 0))] if verticale else None
    a2 = lambda p: (p[0], p[2])  # noqa: E731
    for X, X1 in zip(T, T1):                          # corrispondenti allineati con U (o paralleli a U_inf)
        if proprio_U:
            assert allineati(a2(U), a2(X), a2(X1))
        else:
            assert paralleli(g.sub(a2(X1), a2(X)), dU)
    for n, (i, j) in enumerate(((0, 1), (1, 2), (2, 0))):
        d0, d1 = g.sub(a2(T[j]), a2(T[i])), g.sub(a2(T1[j]), a2(T1[i]))
        if verticale:                                 # lati corrispondenti sull'asse
            assert allineati(a2(T[i]), a2(T[j]), a2(K[n])) and allineati(a2(T1[i]), a2(T1[j]), a2(K[n]))
        else:                                         # asse improprio: lati corrispondenti paralleli
            assert paralleli(d0, d1)
    return S, S1, T0, T, T1, U, dU, K


def limiti(T, T1, U, K):
    xs = [X[0] for X in T + T1] + ([V[0] for V in K] if K else []) + ([U[0]] if U else [])
    return min(xs) - 30, max(xs) + 30


def foglio(nome, c):
    S, S1, T0, T, T1, U, dU, K = dati(c)
    xa, xb = limiti(T, T1, U, K)
    k = min(1.4, 540 / (xb - xa))
    ox, oy = 30 - k * xa, 60
    f = F(640, 470, c["titolo"] + " sul foglio")

    def s(p):
        return (ox + k * p[0], oy + k * p[2])

    if K:
        f.linea(s((xa, 0, 0)), s((xb, 0, 0)), "nero", 2.4)
        f.testo(s((xb, 0, 0)), "u", 4, 4, "nero", 16)
    else:
        f.u_inf((585, 175))
    for X, X1 in zip(T, T1):                          # rette dei corrispondenti
        if U is not None:
            far = X1 if math.dist(U, X1) > math.dist(U, X) else X
            f.raggio(s(U), s(far), 18)
        else:
            f.tratt(lungo(s(X), direzione(s(X1), s(X)), 18), lungo(s(X1), direzione(s(X), s(X1)), 18))
    if K:
        for (i, j), V in zip(((0, 1), (1, 2), (2, 0)), K):
            far = T[i] if math.dist(V, T[i]) > math.dist(V, T[j]) else T[j]
            far1 = T1[i] if math.dist(V, T1[i]) > math.dist(V, T1[j]) else T1[j]
            f.linea(s(V), s(far), "blu", 1, "3,3"); f.linea(s(V), s(far1), "verde", 1, "3,3")
    f.poligono([s(X) for X in T], "blu", 0.10); f.poligono([s(X) for X in T1], "verde", 0.12)
    if K:
        for V in K:
            f.unito(s(V))
    if U is not None:
        f.punto(s(U), "U", -18, -6, "rosso")
    else:
        f.U_inf((585, 120), dU, "U_∞", -40, -10)
    for X, n in zip(T, "ABC"):
        f.punto(s(X), n, 8, -4, "blu")
    for X, n in zip(T1, ("A′", "B′", "C′")):
        f.punto(s(X), n, -24, 6, "verde")
    f.didascalia(c["didascalia_foglio"])
    f.salva(BZ + f"b02-{nome}-foglio.svg")


def spazio(nome, c):
    S, S1, T0, T, T1, U, dU, K = dati(c)
    xa, xb = limiti(T, T1, U, K)
    xa, xb = min(xa, -100), max(xb, 340)
    ox, oy = 50 - xa + 26, 60
    f = F(int(ox + xb + 0.42 * 300 + 60), 480, c["titolo"] + " nello spazio")

    def s(p):
        return (ox + p[0] + 0.42 * p[2], oy + p[1] + 0.3 * p[2])

    f.poligono([s(p) for p in [(xa, 0, -60), (xb, 0, -60), (xb, 0, 300), (xa, 0, 300)]], "grigio", 0.08, 1)
    f.testo(s((xa, 0, -60)), "α ≡ α′ (il foglio)", 40, 16, "grigio", 14)
    if K:
        f.poligono([s(p) for p in [(xa, 0, 0), (xb, 0, 0), (xb, 200, 0), (xa, 200, 0)]], "grigio", 0.10, 1)
        f.testo(s((xb, 200, 0)), "α_0", -30, 20, "grigio", 15)
        f.linea(s((xa - 20, 0, 0)), s((xb + 20, 0, 0)), "nero", 2.4)
        f.testo(s((xb + 20, 0, 0)), "u", 4, 4, "nero", 16)
    else:
        h = c["piano"][1]
        x0, x1 = min(X[0] for X in T0) - 50, max(X[0] for X in T0) + 50
        z0, z1 = min(X[2] for X in T0) - 40, max(X[2] for X in T0) + 40
        f.poligono([s(p) for p in [(x0, h, z0), (x1, h, z0), (x1, h, z1), (x0, h, z1)]], "grigio", 0.12, 1)
        f.testo(s((x1, h, z0)), "α_0 (parallelo al foglio)", -150, 18, "grigio", 13)
    for X in T:
        f.linea(s(S), s(X), "blu", 0.8, "5,4")
    for X1 in T1:
        f.linea(s(S1), s(X1), "verde", 0.8, "5,4")
    if U is not None:                                 # la retta dei due centri buca il foglio in U
        f.linea(s(S), s(U), "rosso", 1.6, "7,4")
        for X, X1 in zip(T, T1):
            far = X1 if math.dist(U, X1) > math.dist(U, X) else X
            f.linea(s(U), lungo(s(far), direzione(s(U), s(far)), 14), "grigio", 1.1, "2,3")
    else:                                             # la retta dei due centri e' parallela al foglio
        d = direzione(s(S), s(S1))
        f.linea(lungo(s(S), d, -40), lungo(s(S1), d, 60), "rosso", 1.6, "7,4")
        f.testo(lungo(s(S1), d, 60), "S S₁ parallela al foglio", 6, 4, "rosso", 12, False)
        for X, X1 in zip(T, T1):
            dd = direzione(s(X1), s(X))
            f.linea(lungo(s(X), dd, 14), lungo(s(X1), dd, -14), "grigio", 1.1, "2,3")
    if K:
        for (i, j), V in zip(((0, 1), (1, 2), (2, 0)), K):
            far0 = T0[i] if math.dist(V, T0[i]) > math.dist(V, T0[j]) else T0[j]
            f.linea(s(V), s(far0), "nero", 0.8, "6,4")
    f.poligono([s(X) for X in T0], "grigio", 0.20, 2.2)
    f.poligono([s(X) for X in T], "blu", 0.12, 2.2)
    f.poligono([s(X) for X in T1], "verde", 0.14, 2.2)
    if K:
        for V in K:
            f.unito(s(V))
    for X, n in zip(T0, ("A_0", "B_0", "C_0")):
        f.punto(s(X), n, 6, -6)
    for X, n in zip(T, "ABC"):
        f.punto(s(X), n, 6, 16, "blu")
    for X, n in zip(T1, ("A′", "B′", "C′")):
        f.punto(s(X), n, -22, -6, "verde")
    f.punto(s(S), "S", 8, -4); f.punto(s(S1), "S_1", 8, -2)
    if U is not None:
        f.punto(s(U), "U", -18, -6, "rosso")
    f.didascalia(c["didascalia_spazio"], 12)
    f.salva(BZ + f"b02-{nome}-spazio.svg")


CASI["affinita-ortogonale"].update(
    didascalia_foglio="Le rette AA′, BB′, CC′ sono parallele e perpendicolari all'asse; i lati si incontrano su u.",
    didascalia_spazio="S e S₁ alla stessa altezza: S S₁ è parallela al foglio, quindi U è all'infinito (U∞).")
CASI["affinita-obliqua"].update(
    didascalia_foglio="Le rette AA′, BB′, CC′ sono parallele e inclinate rispetto all'asse; i lati si incontrano su u.",
    didascalia_spazio="S e S₁ alla stessa altezza, ma spostati di lato: U∞ ha una direzione inclinata.")
CASI["omotetia"].update(
    didascalia_foglio="A′, B′, C′ sui raggi da U; i lati corrispondenti sono paralleli (asse all'infinito, u∞).",
    didascalia_spazio="α₀ è parallelo al foglio: non lo taglia mai, quindi l'asse è all'infinito (u∞).")
CASI["traslazione"].update(
    didascalia_foglio="Tutti i punti si spostano nella stessa direzione e della stessa quantità: U∞ e u∞.",
    didascalia_spazio="α₀ parallelo al foglio (u∞) e S, S₁ alla stessa altezza (U∞): la figura si sposta uguale.")

if __name__ == "__main__":
    for nome, c in CASI.items():
        foglio(nome, c)
        spazio(nome, c)
    print("ok")
