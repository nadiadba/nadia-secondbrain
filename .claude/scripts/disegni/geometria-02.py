"""Schemi per la lezione di Geometria descrittiva del 6 ottobre (02-...): richiami di geometria,
fondamenti della geometria proiettiva, omologia e omologie particolari, esercizi di omologia.

Immagini della sbobina:  sbobine/img/02-*.svg
Immagini della bozza:    bozze/img/b02-*.svg

Notazione (come la docente): centro U, asse u, punti corrispondenti con l'apice (A e A');
U∞ e u∞ per centro e asse impropri (U∞ con la lineetta della direzione, u∞ con la crocetta).
Tutti i punti corrispondenti sono calcolati con le proprieta' dell'omologia (allineamento con il
centro, rette corrispondenti che si incontrano sull'asse) e verificati con un'altra coppia.

Coordinate di disegno: x verso destra, y verso l'alto, origine in basso a sinistra.
"""
import math
import os
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, COLORI, interseca, direzione, Triedro  # noqa: E402

BASE = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/"
SB = BASE + "sbobine/img/"
BZ = BASE + "bozze/img/"
os.makedirs(BZ, exist_ok=True)


# ------------------------------------------------------------------ piccola geometria
def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def mul(p, k):
    return (p[0] * k, p[1] * k)


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def oltre(a, b, t):
    """Punto a + t*(b - a)."""
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def allineati(a, b, c, tol=1e-6):
    return abs(cross(sub(b, a), sub(c, a))) <= tol * max(1, math.dist(a, b) * math.dist(a, c))


def paralleli(d1, d2, tol=1e-6):
    return abs(cross(d1, d2)) <= tol * math.hypot(*d1) * math.hypot(*d2)


# ------------------------------------------------------------------ omologia
class Omologia:
    """Omologia piana definita da centro, asse e una coppia di punti corrispondenti A -> A1.

    U: centro proprio, oppure None con d = direzione del centro improprio U∞.
    asse: (ua, ub) due punti dell'asse, oppure None se l'asse e' improprio (u∞).
    """

    def __init__(self, A, A1, U=None, d=None, asse=None):
        self.A, self.A1, self.U, self.d, self.asse = A, A1, U, d, asse
        assert self._sul_raggio(A, A1), "A e A' non sono allineati con il centro"

    def _sul_raggio(self, X, X1):
        if self.U is not None:
            return allineati(self.U, X, X1)
        return paralleli(sub(X1, X), self.d) if math.dist(X, X1) > 1e-9 else True

    def raggio(self, X):
        """Due punti della retta che unisce X al centro."""
        return (self.U, X) if self.U is not None else (X, add(X, self.d))

    def _con(self, X, A, A1):
        """Corrispondente di X usando la coppia A -> A1 (la costruzione dell'esercizio)."""
        if self.asse is not None:
            ua, ub = self.asse
            V = interseca(A, X, ua, ub)                     # punto unito della retta AX
            if V is None:                                   # AX parallela all'asse
                l1 = (A1, add(A1, sub(ub, ua)))
            else:
                l1 = (V, A1)
        else:                                               # asse improprio: rette corrispondenti parallele
            l1 = (A1, add(A1, sub(X, A)))
        r = self.raggio(X)
        return interseca(l1[0], l1[1], r[0], r[1])

    def __call__(self, X):
        X1 = self._con(X, self.A, self.A1)
        if X1 is None or self._degenere(X, self.A):
            # X sta sul raggio di A: si passa per una coppia ausiliaria
            B = add(self.A, (37.0, -53.0))
            B1 = self._con(B, self.A, self.A1)
            X1 = self._con(X, B, B1)
        # verifica con un'altra coppia (indipendente da A)
        B = add(self.A, (-71.0, 29.0))
        if not self._degenere(X, B):
            B1 = self._con(B, self.A, self.A1)
            X2 = self._con(X, B, B1)
            assert X2 is not None and math.dist(X1, X2) < 1e-6, ("verifica fallita", X, X1, X2)
        assert self._sul_raggio(X, X1)
        return X1

    def _degenere(self, X, A):
        r = self.raggio(A)
        return allineati(r[0], r[1], X, 1e-9)

    def controlla(self, coppie):
        """Le due proprieta': allineamento con il centro e rette corrispondenti che si incontrano sull'asse."""
        for X, X1 in coppie:
            assert self._sul_raggio(X, X1), ("non allineati con il centro", X, X1)
        for i, (X, X1) in enumerate(coppie):
            for Y, Y1 in coppie[i + 1:]:
                if math.dist(X, Y) < 1e-9:
                    continue
                if self.asse is None:
                    assert paralleli(sub(Y, X), sub(Y1, X1)), ("con u∞ le rette devono essere parallele", X, Y)
                else:
                    ua, ub = self.asse
                    P = interseca(X, Y, ua, ub)
                    if P is None:
                        assert paralleli(sub(Y1, X1), sub(ub, ua))
                    else:
                        assert allineati(X1, Y1, P, 1e-6), ("rette corrispondenti non sull'asse", X, Y)


# ------------------------------------------------------------------ disegno
class F(Figura):
    """Figura con y verso l'alto e origine in basso a sinistra."""

    def __init__(self, w, h, titolo=None):
        super().__init__(w, h, h, titolo)

    def clip(self, p, q, m=10):
        """Estremi della retta per p e q dentro il riquadro (con margine m)."""
        d = sub(q, p)
        t0, t1 = -1e9, 1e9
        for i, (lo, hi) in enumerate(((m, self.w - m), (m, self.h - m))):
            if abs(d[i]) < 1e-12:
                if not lo <= p[i] <= hi:
                    return None
                continue
            a, b = (lo - p[i]) / d[i], (hi - p[i]) / d[i]
            t0, t1 = max(t0, min(a, b)), min(t1, max(a, b))
        if t0 > t1:
            return None
        return oltre(p, q, t0), oltre(p, q, t1)

    def linea(self, a, b, colore="nero", sp=1.8, tratt=None):
        self._linea(a, b, colore, sp, tratt)

    def retta_tutta(self, p, q, colore="nero", sp=1.8, tratt=None, m=10):
        e = self.clip(p, q, m)
        if e:
            self._linea(e[0], e[1], colore, sp, tratt)
        return e

    def asse(self, a, b, nome="u", dx=-16, dy=-8, m=10):
        e = self.retta_tutta(a, b, "nero", 2.4, m=m)
        self.testo(e[0], nome, dx, dy, "nero", 16)
        return e

    def raggio(self, a, b, oltre_px=22, colore="grigio"):
        """Linea di costruzione (tratteggiata) da a fino a b e un po' oltre."""
        d = direzione(a, b)
        self._linea(a, lungo(b, d, oltre_px), colore, 1, "5,4")

    def tratt(self, a, b, colore="grigio", sp=1):
        self._linea(a, b, colore, sp, "5,4")

    def U_inf(self, p, d, nome="U_∞", dx=10, dy=4, l=16):
        self._linea(lungo(p, d, -l), lungo(p, d, l), "nero", 2)
        self.testo(p, nome, dx, dy, "nero", 16)

    def u_inf(self, p, nome="u_∞", dx=14, dy=5):
        for s in (1, -1):
            self._linea(add(p, (-9, -9 * s)), add(p, (9, 9 * s)), "nero", 1.6)
        self.testo(p, nome, dx, dy, "nero", 16)

    def cerchio(self, c, r, colore="nero", sp=1.8):
        x, y = self._s(c)
        self.parti.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" '
                          f'stroke="{COLORI.get(colore, colore)}" stroke-width="{sp}"/>')

    def poligono(self, pts, colore="blu", opacita=0.12, sp=1.8):
        s = " ".join("{:.1f},{:.1f}".format(*self._s(p)) for p in pts)
        c = COLORI.get(colore, colore)
        self.parti.append(f'<polygon points="{s}" fill="{c}" fill-opacity="{opacita}" stroke="{c}" stroke-width="{sp}"/>')

    def unito(self, p, nome=None, dx=6, dy=16):
        """Punto unito sull'asse: cerchietto vuoto (come nelle soluzioni della docente)."""
        x, y = self._s(p)
        self.parti.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#ffffff" stroke="#1f1f1f" stroke-width="1.6"/>')
        if nome:
            self.testo(p, nome, dx, dy, "nero")

    def didascalia(self, testo, y=None):
        self.nota(14, (self.h - 12) if y is None else y, testo, 13)

    def salva_in(self, *percorsi):
        for p in percorsi:
            self.salva(p)


def v3(p, q):
    return tuple(q[i] - p[i] for i in range(3))


def su_piano3(S, P, asse, valore):
    """Punto in cui la retta S-P incontra il piano coordinata[asse] = valore (3D)."""
    t = (valore - S[asse]) / (P[asse] - S[asse])
    return tuple(S[i] + t * (P[i] - S[i]) for i in range(3))


# ==================================================================== RICHIAMI DI GEOMETRIA
def distanza():
    f = F(580, 250, "La distanza di un punto P da una retta r")
    r_a, r_b = (30, 55), (550, 55)
    P, H = (270, 205), (270, 55)
    f.linea(r_a, r_b, "nero", 2); f.testo(r_b, "r", -14, -8)
    for Q in ((120, 55), (440, 55)):
        f.tratt(P, Q)
    f.testo((440, 55), "distanze inclinate (più lunghe)", -60, 22, "grigio", 12, False)
    f.linea(P, H, "rosso", 2.6)
    f.angolo_retto(H, (1, 0), (0, 1), 11)
    f.punto(P, "P", 8, -4, "rosso"); f.punto(H, "H", -18, 18)
    f.testo((270, 130), "PH = distanza minima", 10, 4, "rosso", 13, False)
    f.testo(H, "piede della perpendicolare", -186, 18, "nero", 12, False)
    return f


def distanza_piano():
    """Disegno proposto: distanza di un punto da un piano (vista obliqua del piano orizzontale)."""
    f = F(600, 300, "La distanza di un punto P da un piano α")
    def s(q):  # x a destra, y in alto, z in profondita'
        return (60 + q[0] + 0.5 * q[2], 45 + q[1] + 0.35 * q[2])
    f.poligono([s((0, 0, 0)), s((380, 0, 0)), s((380, 0, 200)), s((0, 0, 200))], "blu", 0.10, 1.4)
    f.testo(s((350, 0, 15)), "α", 0, 0, "blu", 18)
    H3 = (190, 0, 100); P3 = (190, 155, 100)
    H, P = s(H3), s(P3)
    # due rette del piano per H, perpendicolari a PH
    for a3, b3, nome in (((40, 0, 100), (340, 0, 100), "a"), ((190, 0, 10), (190, 0, 190), "b")):
        f.linea(s(a3), s(b3), "verde", 1.4); f.testo(s(b3), nome, 6, -2, "verde", 14)
    dx, dz = direzione(H, s((340, 0, 100))), direzione(H, s((190, 0, 190)))
    f.angolo_retto(H, dx, (0, 1), 13); f.angolo_retto(H, dz, (0, 1), 13)
    # distanze inclinate
    for Q3 in ((60, 0, 40), (320, 0, 160)):
        f.tratt(P, s(Q3))
    f.testo(P, "distanze inclinate (più lunghe)", 70, 30, "grigio", 12, False)
    f.linea(P, H, "rosso", 2.6)
    f.punto(P, "P", 8, -4, "rosso"); f.punto(H, "H", -20, 20)
    f.testo(oltre(H, P, 0.5), "PH", 9, 4, "rosso", 14, False)
    f.didascalia("PH = distanza minima: è perpendicolare a due rette a e b del piano che passano per H.")
    return f


def rette():
    f = F(690, 240, "Due rette nello stesso piano, e la parallela per un punto")
    for x, t in ((14, "rette parallele"), (246, "rette incidenti"), (478, "per P una sola parallela a r")):
        f.nota(x, 18, t, 13)
    # parallele
    d = direzione((0, 0), (180, 60))
    a = (20, 60); b = (20, 120)
    f.linea(a, lungo(a, d, 195), "blu", 2); f.testo(lungo(a, d, 195), "r", -6, 16, "blu")
    f.linea(b, lungo(b, d, 195), "verde", 2); f.testo(lungo(b, d, 195), "s", -6, -8, "verde")
    # incidenti
    r1, r2, s1, s2 = (250, 40), (440, 170), (250, 170), (440, 50)
    P = interseca(r1, r2, s1, s2)
    f.linea(r1, r2, "blu", 2); f.testo(r2, "r", -14, 2, "blu")
    f.linea(s1, s2, "verde", 2); f.testo(s2, "s", -14, 0, "verde")
    f.punto(P, "P", -4, -12)
    # parallela per P
    d = direzione((0, 0), (190, 55))
    a = (484, 50)
    P = (575, 150)
    f.linea(a, lungo(a, d, 195), "blu", 2); f.testo(lungo(a, d, 195), "r", -4, 18, "blu")
    f.linea(lungo(P, d, -95), lungo(P, d, 100), "verde", 2); f.testo(lungo(P, d, 100), "s", -10, -8, "verde")
    f.punto(P, "P", -6, -10)
    return f


def diedro_triedro():
    f = F(660, 300, "Il diedro (due semipiani con una retta comune) e il triedro (tre piani)")
    f.nota(14, 18, "diedro", 13); f.nota(350, 18, "triedro", 13)
    # diedro: due semipiani con lo spigolo r in comune
    T = Triedro(f, (250, 130), 0, 170, 120, 120, 1.0)
    T._poligono([(-170, 0, 0), (0, 0, 0), (0, 0, 120), (-170, 0, 120)], "blu", 0.12, "blu")
    T._poligono([(-170, 0, 0), (0, 0, 0), (0, 120, 0), (-170, 120, 0)], "verde", 0.12, "verde")
    T.segmento((-195, 0, 0), (25, 0, 0), "rosso", 2.4)
    T.testo((25, 0, 0), "r", 4, -4, "rosso", 15)
    T.testo((-150, 0, 100), "α", 0, 0, "blu", 16)
    T.testo((-150, 95, 0), "β", 0, 0, "verde", 16)
    # triedro: tre piani con un punto in comune, il vertice
    T = Triedro(f, (530, 130), 0, 160, 110, 120, 1.0)
    T._poligono([(-160, 0, 0), (0, 0, 0), (0, 0, 120), (-160, 0, 120)], "blu", 0.12, "blu")
    T._poligono([(-160, 0, 0), (0, 0, 0), (0, 110, 0), (-160, 110, 0)], "verde", 0.12, "verde")
    T._poligono([(0, 0, 0), (0, 110, 0), (0, 110, 120), (0, 0, 120)], "arancio", 0.12, "arancio")
    T.testo((-140, 0, 100), "α", 0, 0, "blu", 16)
    T.testo((-140, 85, 0), "β", 0, 0, "verde", 16)
    T.testo((0, 80, 100), "γ", 0, 0, "arancio", 16)
    T.punto((0, 0, 0), "V", 8, -6)
    T.testo((0, 0, 0), "vertice", 8, 12, "nero", 12)
    return f


# ==================================================================== GEOMETRIA PROIETTIVA
def schermo(p, ox, oy):
    """Vista obliqua: x a destra, y in alto, z in profondita' (verso l'alto a destra)."""
    return (ox + p[0] + 0.45 * p[2], oy + p[1] + 0.3 * p[2])


def proiezione_punto_retta():
    f = F(720, 350, "Proiettare da un centro S: un punto (a sinistra) e una retta (a destra)")
    f.nota(14, 18, "punto: il raggio proiettante", 13)
    f.nota(370, 18, "retta: un fascio di rette (in un piano)", 13)
    xq = 220
    pq = [(xq, 0, -75), (xq, 0, 120), (xq, 215, 120), (xq, 215, -75)]
    for ox in (20, 375):
        f.poligono([schermo(p, ox, 60) for p in pq], "grigio", 0.10, 1.2)
        f.testo(schermo((xq, 0, -75), ox, 60), "piano di quadro (PQ)", -30, 18, "grigio", 12, False)
    # punto
    ox, oy = 20, 60
    S = (0, 110, 30)
    P = (110, 150, 20)
    P1 = su_piano3(S, P, 0, xq)
    f.linea(schermo(S, ox, oy), schermo(P1, ox, oy), "grigio", 1.2, "5,4")
    f.punto(schermo(S, ox, oy), "S", -6, -10)
    f.punto(schermo(P, ox, oy), "P", -4, -10, "blu")
    f.punto(schermo(P1, ox, oy), "P′", 6, -6, "rosso")
    f.testo(schermo(tuple((S[i] + P1[i]) / 2 for i in range(3)), ox, oy), "raggio proiettante", -40, 26, "grigio", 12, False)
    # retta
    ox = 375
    R1, R2 = (120, 50, -20), (120, 150, 70)
    I1, I2 = su_piano3(S, R1, 0, xq), su_piano3(S, R2, 0, xq)
    f.poligono([schermo(S, ox, oy), schermo(I1, ox, oy), schermo(I2, ox, oy)], "arancio", 0.10, 0.6)
    for k in range(5):
        t = k / 4
        R = tuple(R1[i] + t * (R2[i] - R1[i]) for i in range(3))
        I = su_piano3(S, R, 0, xq)
        f.linea(schermo(S, ox, oy), schermo(I, ox, oy), "grigio", 1, "5,4")
    f.linea(schermo(R1, ox, oy), schermo(R2, ox, oy), "blu", 2.2)
    f.testo(schermo(R2, ox, oy), "r", -14, -2, "blu")
    f.linea(schermo(I1, ox, oy), schermo(I2, ox, oy), "rosso", 2.2)
    f.testo(schermo(I2, ox, oy), "r′", 6, 4, "rosso")
    f.punto(schermo(S, ox, oy), "S", -6, -10)
    return f


def proiezione_piano():
    """Disegno proposto: proiettare un piano da S -> stella di rette (non in un unico piano)."""
    f = F(560, 390, "Proiettare un piano da un centro S: una stella di rette")
    xq = 220
    ox, oy = 70, 95
    pq = [(xq, 0, -75), (xq, 0, 120), (xq, 215, 120), (xq, 215, -75)]
    f.poligono([schermo(p, ox, oy) for p in pq], "grigio", 0.10, 1.2)
    f.testo(schermo((xq, 0, -75), ox, oy), "piano di quadro (PQ)", -30, 18, "grigio", 12, False)
    S = (0, 110, 30)
    V = [(95, 78, -10), (112, 78, 62), (106, 145, 62), (90, 145, -10)]   # una porzione del piano α
    Vp = [su_piano3(S, X, 0, xq) for X in V]
    def media(pts, w):
        return tuple(sum(wi * q[i] for wi, q in zip(w, pts)) for i in range(3))
    interni = [media(V, w) for w in ((.25, .25, .25, .25), (.5, .5, 0, 0), (0, .5, .5, 0), (0, 0, .5, .5), (.5, 0, 0, .5))]
    for X in V + interni:
        f.linea(schermo(S, ox, oy), schermo(su_piano3(S, X, 0, xq), ox, oy), "grigio", 1, "5,4")
    f.poligono([schermo(X, ox, oy) for X in V], "blu", 0.18, 2)
    f.poligono([schermo(X, ox, oy) for X in Vp], "rosso", 0.10, 2)
    for X in V + interni:
        f.punto(schermo(X, ox, oy), "", 0, 0, "blu")
    f.testo(schermo(V[3], ox, oy), "α", -16, -4, "blu", 16)
    f.testo(schermo(Vp[2], ox, oy), "α′", 6, -4, "rosso", 16)
    f.punto(schermo(S, ox, oy), "S", -6, -10)
    f.didascalia("I raggi da S per i punti di α vanno in tutte le direzioni: non stanno in un unico piano.")
    return f


def retta_proiettiva():
    f = F(600, 360, "La retta proiettiva: il modello della circonferenza")
    C, R = (300, 215), 105
    S = (C[0] + R * math.cos(math.radians(150)), C[1] + R * math.sin(math.radians(150)))
    f.cerchio(C, R, "verde", 1.8)
    ry = 70
    f.linea((20, ry), (580, ry), "blu", 2.2); f.testo((20, ry), "r", 0, -8, "blu")

    def seconda(X):
        d = direzione(S, X)
        w = sub(S, C)
        t = -2 * (d[0] * w[0] + d[1] * w[1])          # |S + t d - C| = R, con S sulla circonferenza
        return lungo(S, d, t)

    for X, n, dx in (((120, ry), "A", -8), ((300, ry), "B", -6), ((470, ry), "C", -4)):
        X1 = seconda(X)
        f.tratt(S, X)
        f.punto(X, n, dx, 20, "blu")
        f.punto(X1, n + "′", 8 if n != "A" else -26, 10 if n != "C" else -4, "verde")
    # il raggio parallelo a r
    Pinf = (2 * C[0] - S[0], S[1])
    f.linea(lungo(S, (1, 0), -40), lungo(Pinf, (1, 0), 110), "rosso", 1.4, "7,4")
    f.punto(Pinf, "P′", 6, -8, "rosso")
    f.testo(Pinf, "raggio parallelo a r", 30, -12, "rosso", 12, False)
    f.U_inf((540, ry + 34), (1, 0), "P_∞", 20, 6)
    f.punto(S, "S", -20, -6)
    f.didascalia("Anche il raggio parallelo a r lascia un'immagine P′: è l'immagine del punto all'infinito P∞ di r.")
    return f


def punto_improprio():
    f = F(620, 280, "Rette parallele: si incontrano nel punto improprio, indicato con la direzione")
    d = direzione((0, 0), (300, 90))
    for p, n, c in (((30, 40), "r", "blu"), ((30, 90), "s", "verde")):
        f.linea(p, lungo(p, d, 430), c, 2); f.testo(lungo(p, d, 430), n, 2, 18, c)
    A = (130, 150)
    f.linea(lungo(A, d, -100), lungo(A, d, 330), "arancio", 1.6)
    f.testo(lungo(A, d, 330), "t", 2, 18, "arancio")
    f.punto(A, "A", -4, -12, "arancio")
    f.U_inf((570, 210), d, "P_∞", -8, -14)
    f.didascalia("r, s e t hanno la stessa direzione: passano tutte per P∞. Per A e P∞ passa una sola retta, t.")
    return f


def prospettivita():
    f = F(730, 430, "La prospettività tra due piani α e α′: centro S e asse")
    ox, oy, k = 90, 72, 1.3

    def s(p):
        return (ox + k * (p[0] + 0.5 * p[2]), oy + k * (p[1] + 0.32 * p[2]))

    S = (170, 290, -200)        # S fuori da tutti e due i piani: sopra α e davanti ad α′
    A, B, C = (60, 0, 80), (250, 0, 20), (170, 0, 190)
    tri = [A, B, C]
    img = [su_piano3(S, p, 2, 0) for p in tri]
    f.poligono([s(p) for p in [(-40, 0, 0), (360, 0, 0), (360, 0, 230), (-40, 0, 230)]], "grigio", 0.08, 1)
    f.poligono([s(p) for p in [(-40, 0, 0), (360, 0, 0), (360, 170, 0), (-40, 170, 0)]], "grigio", 0.10, 1)
    f.testo(s((360, 0, 230)), "α", -26, 16, "grigio", 16)
    f.testo(s((-40, 170, 0)), "α′", 6, 20, "grigio", 16)
    f.linea(s((-60, 0, 0)), s((380, 0, 0)), "nero", 2.4)
    f.testo(s((380, 0, 0)), "asse", -10, 18, "nero", 14)
    for p in tri:
        f.linea(s(S), s(p), "grigio", 1, "5,4")
    for (p, q), (p1, q1) in [((A, C), (img[0], img[2])), ((B, C), (img[1], img[2])), ((A, B), (img[0], img[1]))]:
        K = su_piano3(p, q, 2, 0)
        K1 = su_piano3(p1, q1, 1, 0)
        assert math.dist(K, K1) < 1e-6            # i lati corrispondenti si incontrano sull'asse
        f.linea(s(p), s(K), "blu", 1, "3,3")
        f.linea(s(p1), s(K1), "verde", 1, "3,3")
        f.unito(s(K))
    f.poligono([s(p) for p in tri], "blu")
    f.poligono([s(p) for p in img], "verde")
    for p, n, dx, dy in zip(tri, "ABC", (-18, 4, 6), (16, 18, -6)):
        f.punto(s(p), n, dx, dy, "blu")
    for p, n, dx, dy in zip(img, "ABC", (-26, 6, -6), (-6, -8, -10)):
        f.punto(s(p), n + "′", dx, dy, "verde")
    f.punto(s(S), "S", -18, -6)
    f.testo(s(S), "S è fuori dai due piani", 10, -6, "nero", 12, False)
    f.didascalia("I raggi da S uniscono i vertici corrispondenti; i lati corrispondenti si incontrano sull'asse (cerchietti).")
    return f


def omologia_due_centri(nome1="S′"):
    f = F(700, 430, "L'omologia: la stessa figura proiettata da due centri sullo stesso piano α")
    ox, oy = 140, 60

    def s(p):
        return (ox + p[0] + 0.42 * p[2], oy + p[1] + 0.3 * p[2])

    S, S1 = (150, 320, -200), (190, 200, -120)
    A0, B0 = (120, 80, 0), (220, 140, 0)
    A, B = su_piano3(S, A0, 1, 0), su_piano3(S, B0, 1, 0)
    A1, B1 = su_piano3(S1, A0, 1, 0), su_piano3(S1, B0, 1, 0)
    U = su_piano3(S, S1, 1, 0)
    K = su_piano3(A0, B0, 1, 0)
    # verifiche nello spazio: U, A, A' allineati sul piano; AB e A'B' passano per K (sull'asse)
    a2 = lambda p: (p[0], p[2])  # noqa: E731
    assert allineati(a2(U), a2(A), a2(A1)) and allineati(a2(U), a2(B), a2(B1))
    assert allineati(a2(A), a2(B), a2(K)) and allineati(a2(A1), a2(B1), a2(K))
    f.poligono([s(p) for p in [(-80, 0, -60), (360, 0, -60), (360, 0, 300), (-80, 0, 300)]], "grigio", 0.08, 1)
    f.poligono([s(p) for p in [(-80, 0, 0), (360, 0, 0), (360, 190, 0), (-80, 190, 0)]], "grigio", 0.10, 1)
    f.testo(s((-80, 0, -60)), "α ≡ α′", 40, 16, "grigio", 15)
    f.testo(s((-80, 190, 0)), "α_0", 6, 20, "grigio", 15)
    f.linea(s((-100, 0, 0)), s((380, 0, 0)), "nero", 2.4)
    f.testo(s((380, 0, 0)), "u", 4, 4, "nero", 16)
    for C, P in ((S, A), (S, B)):
        f.linea(s(C), s(P), "blu", 0.9, "5,4")
    for C, P in ((S1, A1), (S1, B1)):
        f.linea(s(C), s(P), "verde", 0.9, "5,4")
    f.linea(s(S), s(U), "rosso", 1.4, "7,4")
    f.linea(s(U), s(A1), "grigio", 1, "2,3")
    f.linea(s(U), s(B1), "grigio", 1, "2,3")
    f.linea(s(K), s(B), "blu", 1, "3,3"); f.linea(s(K), s(B1), "verde", 1, "3,3")
    f.linea(s(A0), s(B0), "nero", 2.4)
    f.linea(s(A), s(B), "blu", 2.4)
    f.linea(s(A1), s(B1), "verde", 2.4)
    f.unito(s(K))
    f.punto(s(A0), "A_0", -26, -4); f.punto(s(B0), "B_0", 6, -6)
    f.punto(s(A), "A", 4, 18, "blu"); f.punto(s(B), "B", 8, 4, "blu")
    f.punto(s(A1), "A′", -26, -2, "verde"); f.punto(s(B1), "B′", 8, -4, "verde")
    f.punto(s(S), "S", 8, -4); f.punto(s(S1), nome1, 8, -2)
    f.punto(s(U), "U", 8, 18, "rosso")
    f.didascalia("U è il punto in cui la retta dei due centri buca il piano: U, A e A′ (e U, B, B′) sono allineati.", 12)
    return f


# ==================================================================== OMOLOGIA SUL FOGLIO
def omologia_triangoli():
    f = F(640, 430, "Omologia di centro U e asse u: due triangoli corrispondenti")
    ua, ub = (20, 55), (620, 75)
    U = (590, 380)
    A = (360, 330)
    A1 = oltre(U, A, 1.9)
    om = Omologia(A, A1, U=U, asse=(ua, ub))
    B, C = (440, 230), (350, 120)
    B1, C1 = om(B), om(C)
    om.controlla([(A, A1), (B, B1), (C, C1)])
    f.asse(ua, ub, dx=0, dy=20)
    for X, X1 in ((A, A1), (B, B1), (C, C1)):
        f.raggio(U, X1 if math.dist(U, X1) > math.dist(U, X) else X, 18)
    for (X, Y), (X1, Y1) in (((A, B), (A1, B1)), ((B, C), (B1, C1)), ((C, A), (C1, A1))):
        K = interseca(X, Y, ua, ub)
        f.linea(X, K, "blu", 1, "3,3"); f.linea(X1, K, "verde", 1, "3,3")
        f.unito(K)
    f.poligono([A, B, C], "blu"); f.poligono([A1, B1, C1], "verde")
    f.punto(U, "U", 8, -4)
    f.punto(A, "A", 4, -10, "blu"); f.punto(B, "B", 8, -4, "blu"); f.punto(C, "C", 8, 6, "blu")
    f.punto(A1, "A′", -26, -4, "verde"); f.punto(B1, "B′", -30, 18, "verde"); f.punto(C1, "C′", -26, 4, "verde")
    f.didascalia("I punti corrispondenti sono allineati con U; i lati corrispondenti si incontrano sull'asse u (punti uniti).")
    return f


def esercizio_punto_coppia(titolo="Esercizio: dati U, u, la coppia A e A′ e il punto B, trovare B′"):
    f = F(640, 400, titolo)
    ua, ub = (20, 50), (620, 40)
    U = (100, 360)
    A = (230, 250)
    A1 = oltre(U, A, 1.5)
    om = Omologia(A, A1, U=U, asse=(ua, ub))
    B = (310, 340)
    B1 = om(B)
    om.controlla([(A, A1), (B, B1)])
    V = interseca(A, B, ua, ub)
    f.asse(ua, ub, dx=0, dy=-8)
    f.raggio(U, A1, 20); f.raggio(U, B1, 24)
    f.linea(V, lungo(B, direzione(V, B), 30), "blu", 1.6)
    f.testo(lungo(B, direzione(V, B), 30), "r", -14, -2, "blu")
    f.linea(V, lungo(B1, direzione(V, B1), 30), "rosso", 1.6)
    f.testo(lungo(B1, direzione(V, B1), 30), "r′", 4, 4, "rosso")
    f.unito(V, "V", -4, 22)
    f.punto(U, "U", -16, -6)
    f.punto(A, "A", -18, -4, "blu"); f.punto(A1, "A′", -28, 16, "verde")
    f.punto(B, "B", -18, -4, "blu"); f.punto(B1, "B′", 0, -12, "rosso")
    f.didascalia("r = AB incontra l'asse nel punto unito V; r′ passa per V e per A′; B′ = r′ ∩ raggio UB.")
    return f


def _speciale_dati():
    """Configurazione presa dal foglio OMOLOGIA_riepilogo (3° esercizio), ridisegnata."""
    def cv(p):
        return ((p[0] - 60) * 1.1 + 10, (1000 - p[1]) * 1.1 - 80)
    ua, ub = cv((65, 825)), cv((628, 705))
    U = cv((246, 786))
    U = interseca(ua, ub, U, (U[0], U[1] + 1))          # U esattamente sull'asse
    A, A1g, B, C = cv((204, 688)), cv((163, 592)), cv((435, 775)), cv((152, 893))
    A1 = oltre(U, A, math.dist(U, A1g) / math.dist(U, A))
    return ua, ub, U, A, A1, B, C


def omologia_speciale_teoria():
    f = F(660, 410, "Omologia speciale: il centro U sta sull'asse u")
    ua, ub, U, A, A1, B, C = _speciale_dati()
    om = Omologia(A, A1, U=U, asse=(ua, ub))
    B1, C1 = om(B), om(C)
    om.controlla([(A, A1), (B, B1), (C, C1)])
    f.asse(ua, ub, dx=0, dy=20)
    for X, X1 in ((A, A1), (B, B1), (C, C1)):
        far = X1 if math.dist(U, X1) > math.dist(U, X) else X
        f.raggio(U, far, 18)
    for (X, Y), (X1, Y1) in (((A, B), (A1, B1)), ((B, C), (B1, C1)), ((C, A), (C1, A1))):
        K = interseca(X, Y, ua, ub)
        f.linea(X, K, "blu", 1, "3,3"); f.linea(X1, K, "verde", 1, "3,3")
        f.unito(K)
    f.poligono([A, B, C], "blu", 0.08); f.poligono([A1, B1, C1], "verde", 0.10)
    f.punto(U, "U", -4, 24)
    f.punto(A, "A", 8, -4, "blu"); f.punto(B, "B", 8, 16, "blu"); f.punto(C, "C", -18, 4, "blu")
    f.punto(A1, "A′", 8, -4, "verde"); f.punto(B1, "B′", 2, -10, "verde"); f.punto(C1, "C′", 8, 14, "verde")
    f.didascalia("Si risolve come l'omologia classica: corrispondenti allineati con U, lati corrispondenti incontrati sull'asse.")
    return f


def omotetia_teoria():
    f = F(640, 400, "Omotetia: centro U proprio, asse all'infinito (u∞)")
    U = (120, 110)
    A = (190, 210)
    A1 = oltre(U, A, 2.3)
    om = Omologia(A, A1, U=U, asse=None)
    B, C = (270, 190), (230, 140)
    B1, C1 = om(B), om(C)
    om.controlla([(A, A1), (B, B1), (C, C1)])
    for X1 in (A1, B1, C1):
        f.raggio(U, X1, 20)
    f.poligono([A, B, C], "blu"); f.poligono([A1, B1, C1], "verde")
    f.punto(U, "U", -18, 4)
    f.punto(A, "A", -18, -2, "blu"); f.punto(B, "B", 4, 18, "blu"); f.punto(C, "C", -4, 20, "blu")
    f.punto(A1, "A′", -26, -2, "verde"); f.punto(B1, "B′", 8, 4, "verde"); f.punto(C1, "C′", 8, 14, "verde")
    f.u_inf((570, 330))
    f.didascalia("L'asse è all'infinito: i lati corrispondenti sono paralleli (A′B′ ∥ AB...). La figura si ingrandisce.")
    return f


def traslazione_teoria():
    f = F(640, 360, "Traslazione: centro e asse all'infinito (U∞, u∞)")
    d = direzione((0, 0), (1, 0.35))
    A, B, C = (90, 210), (230, 250), (150, 120)
    A1 = lungo(A, d, 300)
    om = Omologia(A, A1, U=None, d=d, asse=None)
    B1, C1 = om(B), om(C)
    om.controlla([(A, A1), (B, B1), (C, C1)])
    for X, X1 in ((A, A1), (B, B1), (C, C1)):
        f.tratt(X, X1)
    f.poligono([A, B, C], "blu"); f.poligono([A1, B1, C1], "verde")
    f.punto(A, "A", -18, -2, "blu"); f.punto(B, "B", -4, -10, "blu"); f.punto(C, "C", -6, 20, "blu")
    f.punto(A1, "A′", -8, -10, "verde"); f.punto(B1, "B′", 8, -4, "verde"); f.punto(C1, "C′", 8, 14, "verde")
    f.U_inf((560, 100), d, "U_∞", 16, 8)
    f.u_inf((560, 300))
    f.didascalia("La figura si sposta tale e quale: A′B′ = AB, angoli e distanze si conservano.")
    return f


def affinita_teoria():
    f = F(680, 360, "Affinità: centro all'infinito (U∞), asse u proprio")
    for i, (nome, d) in enumerate((("affinità ortogonale", (0, 1)), ("affinità obliqua", direzione((0, 0), (0.55, 1))))):
        ox = 340 * i
        f.nota(14 + ox, 18, nome, 13)
        ua, ub = (ox + 10, 60), (ox + 330, 60)
        A = (ox + 110, 280)
        A1 = lungo(A, d, -132 / d[1])                      # distanza dall'asse ridotta a 0,4
        om = Omologia(A, A1, U=None, d=d, asse=(ua, ub))
        B, C = (ox + 270, 290), (ox + 170, 185)
        B1, C1 = om(B), om(C)
        om.controlla([(A, A1), (B, B1), (C, C1)])
        f.linea(ua, ub, "nero", 2.4); f.testo(ub, "u", -14, -8, "nero", 16)
        for X, X1 in ((A, A1), (B, B1), (C, C1)):
            f.tratt(lungo(X, d, 14), lungo(X1, d, -14))
        for (X, Y), (X1, Y1) in (((A, C), (A1, C1)), ((B, C), (B1, C1))):
            K = interseca(X, Y, ua, ub)
            f.linea(X, K, "blu", 1, "3,3"); f.linea(X1, K, "verde", 1, "3,3")
            f.unito(K)
        f.poligono([A, B, C], "blu"); f.poligono([A1, B1, C1], "verde")
        f.punto(A, "A", -18, -4, "blu"); f.punto(B, "B", 8, -4, "blu"); f.punto(C, "C", 8, 4, "blu")
        f.punto(A1, "A′", -26, 4, "verde"); f.punto(B1, "B′", 8, 6, "verde"); f.punto(C1, "C′", 8, 14, "verde")
        f.U_inf((ox + 300, 200), d, "U_∞", 10, 4)
    f.didascalia("Le rette che uniscono i corrispondenti hanno la direzione di U∞; i lati corrispondenti si incontrano su u.")
    return f


# ==================================================================== ESERCIZI (bozza)
def es_speciale_punto():
    """Foglio ES.GUIDATA_Omologia_01, 2° esercizio: U sull'asse, r e r', trovare M'."""
    f = F(600, 460, "Omologia speciale: dati U sull'asse u, r e r′, trovare M′")

    def cv(p):
        return ((p[0] - 400) * 1.4 + 10, (420 - p[1]) * 1.4)
    O, U, ue, re_, r1e, M = [cv(p) for p in ((490, 372), (687, 262), (785, 205), (785, 330), (680, 108), (440, 213))]
    U = interseca(O, ue, U, (U[0], U[1] + 1))
    A = oltre(O, re_, 0.9)                                 # 1. un punto A di r
    A1 = interseca(U, A, O, r1e)                           # 2. raggio da U per A: A' su r'
    om = Omologia(A, A1, U=U, asse=(O, ue))
    M1 = om(M)
    om.controlla([(A, A1), (M, M1), (O, O)])
    W = interseca(A, M, O, ue)
    f.asse(lungo(O, direzione(O, ue), -80), ue, dx=-4, dy=-12)
    f.linea(O, re_, "nero", 2); f.testo(re_, "r", 4, 4)
    f.linea(O, r1e, "nero", 2); f.testo(r1e, "r′", 8, 0)
    f.raggio(U, A1, 24); f.raggio(U, A, 24)
    f.raggio(U, M, 24)
    f.linea(M, A, "blu", 1.4); f.testo(oltre(A, M, 0.75), "s", -4, -10, "blu")
    f.linea(A1, W, "rosso", 1.4); f.linea(W, M1, "rosso", 1.4, "4,3")
    f.testo(oltre(W, A1, 0.85), "s′", 8, 4, "rosso")
    f.unito(O); f.unito(W, "W", 8, 16)
    f.punto(U, "U", 6, 20)
    f.punto(A, "A", -4, -12, "blu"); f.punto(A1, "A′", 8, 4, "verde")
    f.punto(M, "M", -20, -4, "blu"); f.punto(M1, "M′", -30, 6, "rosso")
    return f


def es_speciale_figura():
    """OMOLOGIA_riepilogo, 3° esercizio (soluzione della docente): U sull'asse, ABC e la coppia A, A'."""
    f = F(660, 410, "Omologia speciale: dati U sull'asse u, il triangolo ABC e A′, trovare A′B′C′")
    ua, ub, U, A, A1, B, C = _speciale_dati()
    om = Omologia(A, A1, U=U, asse=(ua, ub))
    B1, C1 = om(B), om(C)
    om.controlla([(A, A1), (B, B1), (C, C1)])
    f.asse(ua, ub, dx=0, dy=20)
    f.raggio(U, A1, 16)
    f.raggio(U, B, 40) if math.dist(U, B) > math.dist(U, B1) else f.raggio(U, B1, 40)
    f.raggio(U, C, 30) if math.dist(U, C) > math.dist(U, C1) else f.raggio(U, C1, 30)
    K_ac = interseca(A, C, ua, ub)
    K_ab = interseca(A, B, ua, ub)
    K_bc = interseca(B, C, ua, ub)
    f.linea(A1, lungo(K_ac, direzione(A1, K_ac), 30), "rosso", 1, "4,3"); f.testo(lungo(K_ac, direzione(A1, K_ac), 30), "r′", 4, 6, "rosso")
    f.linea(A, lungo(A, direzione(C, A), 60), "blu", 1, "4,3"); f.testo(lungo(A, direzione(C, A), 60), "r", 4, 0, "blu")
    f.linea(B1, K_ab, "rosso", 1, "4,3"); f.linea(B, K_ab, "blu", 1, "3,3")
    f.linea(B, K_bc, "blu", 1, "3,3"); f.linea(B1, K_bc, "rosso", 1, "3,3")
    f.poligono([A, B, C], "blu", 0.08)
    f.poligono([A1, B1, C1], "rosso", 0.10, 2.4)
    f.unito(K_ac, "1", -18, -6); f.unito(K_ab, "2", -4, -10); f.unito(K_bc, "3", -4, 22)
    f.punto(U, "U", -4, 24)
    f.punto(A, "A", 8, -4, "blu"); f.punto(B, "B", 8, 16, "blu"); f.punto(C, "C", -18, 4, "blu")
    f.punto(A1, "A′", 8, -4, "rosso"); f.punto(B1, "B′", 2, -10, "rosso"); f.punto(C1, "C′", 8, 14, "rosso")
    return f


def es_omotetia_punto():
    """OMOLOGIA_riepilogo, 4° esercizio (soluzione della docente): U, u∞, r ∥ r', il punto P."""
    f = F(600, 400, "Omotetia: dati U, u∞, r e r′ (parallele) e P, trovare P′")
    U = (330, 360)
    dr = direzione((0, 0), (150, 55))
    r_a = (300, 200)
    r1_a = (310, 100)
    A = interseca(U, (420, 160), r_a, add(r_a, dr))       # un punto di r
    A1 = interseca(U, A, r1_a, add(r1_a, dr))
    om = Omologia(A, A1, U=U, asse=None)
    P = (240, 230)
    P1 = om(P)
    om.controlla([(A, A1), (P, P1)])
    f.linea(lungo(r_a, dr, -20), lungo(r_a, dr, 250), "nero", 2.2); f.testo(lungo(r_a, dr, 250), "r", -6, -10)
    f.linea(lungo(r1_a, dr, -20), lungo(r1_a, dr, 250), "nero", 2.2); f.testo(lungo(r1_a, dr, 250), "r′", -6, -10)
    f.raggio(U, A1, 40)
    f.raggio(U, P1, 60)
    f.linea(P, A, "rosso", 1.2)
    f.linea(P1, A1, "rosso", 1.2)
    f.u_inf((520, 60))
    f.punto(U, "U", 8, -4)
    f.punto(A, "A", 6, -10, "rosso"); f.punto(A1, "A′", 6, -10, "rosso")
    f.punto(P, "P", -20, -4); f.punto(P1, "P′", -26, -4, "rosso")
    return f


def es_omotetia_figura():
    """ES.GUIDATA_Omologia_01, 5° esercizio: U, u∞, la coppia A e A', trovare A'B'C'D'."""
    f = F(620, 470, "Omotetia: dati U, u∞, A e A′, trovare A′B′C′D′")
    U = (300, 280)
    A = (250, 190)
    A1 = oltre(U, A, 1.6)
    om = Omologia(A, A1, U=U, asse=None)
    B, C, D = (265, 345), (370, 370), (470, 300)
    img = [A1] + [om(X) for X in (B, C, D)]
    om.controlla(list(zip([A, B, C, D], img)))
    for X, X1 in zip((A, B, C, D), img):
        f.raggio(U, X1, 18)
    f.poligono([A, B, C, D], "blu", 0.10)
    f.poligono(img, "rosso", 0.06, 2.4)
    f.punto(U, "U", 8, -4)
    for X, n, dx, dy in zip((A, B, C, D), "ABCD", (-18, -18, -2, 4), (14, -4, -10, -10)):
        f.punto(X, n, dx, dy, "blu")
    for X, n, dx, dy in zip(img, "ABCD", (-26, -26, -4, 8), (14, -2, -10, -4)):
        f.punto(X, n + "′", dx, dy, "rosso")
    f.u_inf((540, 50))
    f.didascalia("A′B′ ∥ AB, B′C′ ∥ BC, C′D′ ∥ CD, D′A′ ∥ DA: con u∞ i lati corrispondenti sono paralleli.")
    return f, (A, B, C, D), img


def es_affinita_figura():
    """OMOLOGIA_riepilogo, 5° esercizio (soluzione della docente): U∞, u, ABC e la coppia A, A'."""
    f = F(620, 470, "Affinità: dati U∞, u, il triangolo ABC e A′, trovare A′B′C′")
    ua, ub = (14, 150), (606, 270)
    d = direzione((0, 0), (0.45, 1))
    A = (150, 300)
    A1 = lungo(A, d, 90)
    om = Omologia(A, A1, U=None, d=d, asse=(ua, ub))
    B, C = (420, 345), (230, 130)
    B1, C1 = om(B), om(C)
    om.controlla([(A, A1), (B, B1), (C, C1)])
    f.asse(ua, ub, dx=0, dy=20)
    f.tratt(A, A1)
    for X, X1 in ((B, B1), (C, C1)):
        f.tratt(lungo(X, d, -14) if X[1] < X1[1] else lungo(X, d, 14), lungo(X1, d, 14) if X[1] < X1[1] else lungo(X1, d, -14))
    K_ac = interseca(A, C, ua, ub)
    K_bc = interseca(B, C, ua, ub)
    f.linea(A1, K_ac, "rosso", 1, "4,3")
    f.linea(C1, K_bc, "rosso", 1, "4,3")
    f.poligono([A, B, C], "blu", 0.08)
    f.poligono([A1, B1, C1], "rosso", 0.10, 2.4)
    f.unito(K_ac, "1", -22, -6); f.unito(K_bc, "2", 4, 22)
    f.punto(A, "A", -18, 4, "blu"); f.punto(B, "B", 8, -4, "blu"); f.punto(C, "C", 8, 0, "blu")
    f.punto(A1, "A′", -26, -4, "rosso"); f.punto(B1, "B′", 8, -4, "rosso"); f.punto(C1, "C′", -26, -2, "rosso")
    f.U_inf((90, 400), d, "U_∞", 12, 6)
    return f


def es_affinita_retta():
    """OMOLOGIA_riepilogo, 6° esercizio (soluzione della docente): U∞, u, r e r', la retta m."""
    f = F(640, 400, "Affinità: dati U∞, u, r e r′ e la retta m, trovare m′")
    uy = 200
    ua, ub = (20, uy), (620, uy)
    O = (80, uy)
    dr = direzione((0, 0), (2, 1))
    r_b = lungo(O, dr, 330)
    r1_dir = direzione((0, 0), (1.65, -1))
    Q = (300, uy)
    m_b = lungo(Q, dr, 300)
    d = direzione((0, 0), (-0.38, 1))
    A = lungo(O, dr, 150)
    A1 = interseca(A, add(A, d), O, add(O, r1_dir))
    om = Omologia(A, A1, U=None, d=d, asse=(ua, ub))
    B = lungo(Q, dr, 70)
    B1 = om(B)
    om.controlla([(A, A1), (B, B1), (Q, Q), (O, O)])
    N = interseca(A, B, ua, ub)
    f.asse(ua, ub, dx=0, dy=-8)
    f.linea(O, r_b, "nero", 2); f.testo(r_b, "r", -6, 20)
    f.linea(O, lungo(O, r1_dir, 290), "nero", 2); f.testo(lungo(O, r1_dir, 290), "r′", 6, 4)
    f.linea(Q, m_b, "nero", 2); f.testo(m_b, "m", -6, 20)
    f.linea(lungo(A, d, 14), lungo(A1, d, -24), "rosso", 1)
    f.linea(lungo(B, d, 14), lungo(B1, d, -24), "rosso", 1)
    f.linea(A, N, "rosso", 1); f.testo(oltre(A, N, 0.62), "n", 0, -8, "rosso")
    f.linea(A1, N, "rosso", 1); f.testo(oltre(A1, N, 0.3), "n′", -4, -8, "rosso")
    f.linea(Q, lungo(Q, direzione(Q, B1), math.dist(Q, B1) + 120), "rosso", 2.4)
    f.testo(lungo(Q, direzione(Q, B1), math.dist(Q, B1) + 120), "m′", 6, 4, "rosso")
    f.unito(O); f.unito(Q, "Q", -6, -10); f.unito(N, "N", -6, -10)
    f.punto(A, "A", -18, -6, "rosso"); f.punto(A1, "A′", -26, 6, "rosso")
    f.punto(B, "B", -6, -12, "rosso"); f.punto(B1, "B′", 8, 16, "rosso")
    f.U_inf((470, 340), d, "U_∞", 12, 6)
    return f


def es_affinita_speciale():
    """OMOLOGIA_2_affinità, 1° esercizio (soluzione della docente, dal Docci-Gaiani-Maestri):
    omologia affine speciale, U∞ con la direzione dell'asse; il quadrato ABCD e B'."""
    f = F(680, 400, "Omologia affine speciale: U∞ nella direzione di u; dati il quadrato ABCD e B′")
    uy = 120
    ua, ub = (20, uy), (660, uy)
    d = (1.0, 0.0)
    A, B, C = (230, 220), (365, 330), (470, 200)
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    B1 = (600, 330)
    om = Omologia(B, B1, U=None, d=d, asse=(ua, ub))
    A1, C1, D1 = om(A), om(C), om(D)
    om.controlla([(A, A1), (B, B1), (C, C1), (D, D1)])
    f.asse(ua, ub, dx=-4, dy=22)
    K_ab = interseca(A, B, ua, ub)
    K_bc = interseca(B, C, ua, ub)
    K_cd = interseca(C, D, ua, ub)
    f.linea(A, K_ab, "nero", 1, "3,3"); f.linea(C, K_bc, "nero", 1, "3,3")
    f.linea(B1, K_ab, "rosso", 1); f.linea(B1, K_bc, "rosso", 1)
    f.linea(C1, D1, "rosso", 1)
    for X, X1 in ((A, A1), (B, B1), (C, C1), (D, D1)):
        f.tratt(X, X1)
    f.poligono([A, B, C, D], "nero", 0.04, 2)
    f.poligono([A1, B1, C1, D1], "rosso", 0.08, 2.4)
    f.unito(K_ab, "1", -6, 22); f.unito(K_bc, "2", -6, 22); f.unito(K_cd, "3", 8, 22)
    f.punto(A, "A", -18, -4); f.punto(B, "B", -6, -10); f.punto(C, "C", 8, -4); f.punto(D, "D", -4, 20)
    f.punto(A1, "A′", -6, -10, "rosso"); f.punto(B1, "B′", 8, -4, "rosso")
    f.punto(C1, "C′", 8, -4, "rosso"); f.punto(D1, "D′", -26, -4, "rosso")
    f.U_inf((600, 170), d, "U_∞", -16, -14)
    f.testo((60, 40), "β ≡ β′", 0, 0, "nero", 14)
    return f


def es_traslazione_punto():
    """OMOLOGIA_riepilogo, 1° esercizio (soluzione della docente): U∞, u∞, r ∥ r', il punto P."""
    f = F(600, 360, "Traslazione: dati U∞, u∞, r e r′ e il punto P, trovare P′")
    dr = direzione((0, 0), (360, 70))
    d = direzione((0, 0), (0.6, -0.8))
    r_a, r1_a = (60, 190), (60, 110)
    M = lungo(r_a, dr, 230)
    M1 = interseca(M, add(M, d), r1_a, add(r1_a, dr))
    om = Omologia(M, M1, U=None, d=d, asse=None)
    P = (330, 300)
    P1 = om(P)
    om.controlla([(M, M1), (P, P1)])
    f.linea(r_a, lungo(r_a, dr, 470), "nero", 2.2); f.testo(lungo(r_a, dr, 470), "r", -6, -10)
    f.linea(r1_a, lungo(r1_a, dr, 470), "nero", 2.2); f.testo(lungo(r1_a, dr, 470), "r′", -6, 20)
    f.linea(lungo(M, d, -60), M1, "rosso", 1)
    f.linea(P, M, "rosso", 1); f.linea(P1, M1, "rosso", 1); f.linea(P, P1, "rosso", 1)
    f.punto(M, "M", -24, 2, "rosso"); f.punto(M1, "M′", -6, 22, "rosso")
    f.punto(P, "P", 4, -10); f.punto(P1, "P′", 8, -2, "rosso")
    f.U_inf((90, 300), d, "U_∞", 12, 6)
    f.u_inf((60, 50))
    return f


def es_traslazione_figura():
    """ES.GUIDATA_Omologia_01, 1° esercizio: U∞, u∞, r ∥ r', il triangolo ABC."""
    f = F(620, 420, "Traslazione: dati U∞, u∞, r e r′ e il triangolo ABC, trovare A′B′C′")
    dr = direzione((0, 0), (300, 80))
    d = direzione((0, 0), (1, -0.7))
    r_a, r1_a = (30, 190), (30, 30)
    M = lungo(r_a, dr, 130)
    M1 = interseca(M, add(M, d), r1_a, add(r1_a, dr))
    om = Omologia(M, M1, U=None, d=d, asse=None)
    A, B, C = (60, 330), (220, 370), (170, 260)
    img = [om(X) for X in (A, B, C)]
    om.controlla([(M, M1)] + list(zip((A, B, C), img)))
    f.linea(r_a, lungo(r_a, dr, 570), "nero", 2.2); f.testo(lungo(r_a, dr, 570), "r", -6, -10)
    f.linea(r1_a, lungo(r1_a, dr, 570), "nero", 2.2); f.testo(lungo(r1_a, dr, 570), "r′", -6, 20)
    f.tratt(M, M1)
    f.linea(A, M, "rosso", 1); f.linea(img[0], M1, "rosso", 1)
    for X, X1 in zip((A, B, C), img):
        f.tratt(X, X1)
    f.poligono([A, B, C], "blu", 0.10)
    f.poligono(img, "rosso", 0.08, 2.4)
    f.punto(M, "M", 6, 18, "rosso"); f.punto(M1, "M′", -6, 22, "rosso")
    for X, n, dx, dy in zip((A, B, C), "ABC", (-18, -4, -24), (-4, -10, 4)):
        f.punto(X, n, dx, dy, "blu")
    for X, n, dx, dy in zip(img, "ABC", (-26, 8, 8), (8, -4, 14)):
        f.punto(X, n + "′", dx, dy, "rosso")
    f.U_inf((470, 385), d, "U_∞", 12, 6)
    f.u_inf((540, 60))
    return f


def es_classica_punto_m():
    """Foglio ES.GUIDATA_Omologia_01, 3° esercizio: U, u, r e r' che si incontrano sull'asse, trovare M'.

    Coordinate prese dal foglio (pagina a 2000 px di larghezza) e ridisegnate.
    M sta tra U e l'asse: il suo corrispondente cade oltre U, dall'altra parte del centro.
    """
    f = F(640, 600, "Omologia: dati U, u, r e r′, trovare M′")

    def cv(p):
        return ((p[0] - 1310) * 0.95 + 10, (765 - p[1]) * 0.95)
    U, M, O, ua, ub, re_, r1e = [cv(p) for p in ((1670, 316), (1696, 430), (1731, 519), (1333, 580),
                                                    (1960, 482), (1495, 725), (1901, 693))]
    O = interseca(ua, ub, O, (O[0], O[1] + 1))            # r e r' si incontrano esattamente sull'asse
    A = oltre(O, re_, 0.85)                                # 1. un punto A di r
    A1 = interseca(U, A, O, r1e)                           # 2. raggio da U per A: A' su r' (prolungata)
    om = Omologia(A, A1, U=U, asse=(ua, ub))
    W = interseca(A, M, ua, ub)                            # 3. s = AM incontra l'asse in W
    M1 = om(M)                                             # 4. M' = s' (W A') ∩ raggio UM
    assert allineati(W, A1, M1) and allineati(U, M, M1)
    om.controlla([(A, A1), (M, M1), (O, O), (W, W)])
    # r' corrisponde davvero a r: un altro punto di r va su r'
    B = oltre(O, re_, 0.4)
    assert allineati(O, r1e, om(B))

    f.asse(ua, ub, dx=-4, dy=-10)
    f.linea(O, re_, "nero", 2); f.testo(re_, "r", -14, -2)
    f.linea(O, r1e, "nero", 2); f.testo(r1e, "r′", 8, 0)
    f.tratt(O, lungo(A1, direzione(O, A1), 30), "nero")    # r' prolungata oltre l'asse
    f.raggio(U, A, 20)                                     # raggio U A (passa per A')
    f.raggio(M, M1, 22)                                    # raggio U M prolungato oltre U
    f.linea(A, M, "blu", 1.4); f.testo(oltre(A, M, 0.2), "s", 10, 2, "blu")
    f.linea(W, M1, "rosso", 1.4); f.testo(oltre(W, M1, 0.62), "s′", 8, 4, "rosso")
    f.unito(O); f.unito(W, "W", 10, 22)
    f.punto(U, "U", 10, 4)
    f.punto(A, "A", -20, 4, "blu"); f.punto(A1, "A′", -28, -2, "verde")
    f.punto(M, "M", 8, -6, "blu"); f.punto(M1, "M′", 10, 4, "rosso")
    f.didascalia("A′ = raggio UA ∩ r′;  s = AM incontra l'asse in W;  s′ = WA′;  M′ = s′ ∩ raggio UM.")
    return f


# ==================================================================== salvataggio
distanza().salva_in(SB + "02-distanza-punto-retta.svg", BZ + "b02-distanza-punto-retta.svg")
distanza_piano().salva_in(BZ + "b02-distanza-punto-piano.svg")
rette().salva_in(SB + "02-rette-parallele-incidenti.svg", BZ + "b02-rette-parallele-incidenti.svg")
diedro_triedro().salva_in(SB + "02-diedro-triedro.svg", BZ + "b02-diedro-triedro.svg")
proiezione_punto_retta().salva_in(SB + "02-proiezione-punto-retta.svg", BZ + "b02-proiezione-punto-retta.svg")
proiezione_piano().salva_in(BZ + "b02-proiezione-piano.svg")
retta_proiettiva().salva_in(SB + "02-retta-proiettiva.svg", BZ + "b02-retta-proiettiva.svg")
punto_improprio().salva_in(SB + "02-punto-improprio.svg", BZ + "b02-punto-improprio.svg")
prospettivita().salva_in(SB + "02-prospettivita.svg", BZ + "b02-prospettivita.svg")
omologia_due_centri("S′").salva_in(SB + "02-omologia-due-centri.svg")
omologia_due_centri("S_1").salva_in(BZ + "b02-omologia-due-centri.svg")
omologia_triangoli().salva_in(SB + "02-omologia-centro-asse.svg", BZ + "b02-omologia-centro-asse.svg")
esercizio_punto_coppia().salva_in(SB + "02-omologia-esercizio-punto.svg", BZ + "b02-es-punto-coppia.svg")
omologia_speciale_teoria().salva_in(SB + "02-omologia-speciale.svg", BZ + "b02-omologia-speciale.svg")
affinita_teoria().salva_in(SB + "02-affinita.svg", BZ + "b02-affinita.svg")
omotetia_teoria().salva_in(SB + "02-omotetia.svg", BZ + "b02-omotetia.svg")
traslazione_teoria().salva_in(SB + "02-traslazione.svg", BZ + "b02-traslazione.svg")

es_speciale_punto().salva_in(BZ + "b02-es-speciale-punto.svg")
es_speciale_figura().salva_in(BZ + "b02-es-speciale-figura.svg")
es_omotetia_punto().salva_in(BZ + "b02-es-omotetia-punto.svg")
es_omotetia_figura()[0].salva_in(BZ + "b02-es-omotetia-figura.svg")
es_affinita_figura().salva_in(BZ + "b02-es-affinita-figura.svg")
es_affinita_retta().salva_in(BZ + "b02-es-affinita-retta.svg")
es_affinita_speciale().salva_in(BZ + "b02-es-affinita-speciale.svg")
es_traslazione_punto().salva_in(BZ + "b02-es-traslazione-punto.svg")
es_traslazione_figura().salva_in(BZ + "b02-es-traslazione-figura.svg")
es_classica_punto_m().salva_in(BZ + "b02-es-classica-punto-m.svg")
print("ok")
