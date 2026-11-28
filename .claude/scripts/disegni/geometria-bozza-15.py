"""Schemi per la bozza di geometria descrittiva 15 (lezione del 24 novembre 2026, ripasso per la Prova n. 2):
le viste nello spazio che accompagnano gli schemi sul foglio gia' fatti per la sbobina (geometria-15.py).
1. il parallelepipedo tagliato da un piano proiettante in seconda (stessi dati dello schema 15a);
2. la piramide tagliata da un piano generico, con i piani proiettanti che passano per gli spigoli VC e VA
   (stessi dati degli schemi 15c-15e).

Usa disegni_monge.py senza modificarlo e riusa le primitive di geometria-bozza-11.py (TriedroLavagna,
disegna_solido, ...). Coordinate nello spazio (x, aggetto, quota). Immagini in bozze/img/ con prefisso b15-.
Se si cambia un disegno, alzare VER (Obsidian non ricarica le immagini con lo stesso nome).
"""
import importlib.util
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro

_spec = importlib.util.spec_from_file_location(
    "b11", "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts/disegni/geometria-bozza-11.py")
b11 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b11)
from_b11 = ("add", "sub", "mul", "dot", "cross", "rline", "rpoly", "rtext", "rdot", "retino", "note",
            "disegna_solido", "vista_da")
globals().update({k: getattr(b11, k) for k in from_b11})

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"
VER = ""
KY, KZ = 0.45, 0.35          # l'aggetto scende verso sinistra (in cavaliera): si guarda da davanti, da destra e dall'alto
VISTA = vista_da((1, -KY, 0), (0, -KZ, 1))


class Diedro(Triedro):
    """Il diedro pi1-pi2 visto da davanti, un po' da destra e dall'alto (cosi' i piani inclinati si vedono bene).
    o = posizione sul foglio dell'origine (0, 0, 0); X3 e U danno la lunghezza della LT (da X3 - U a X3)."""

    def _p(self, p):
        return (self.o[0] + self.k * (p[0] - KY * p[1]), self.o[1] - self.k * (p[2] - KZ * p[1]))

    def _rettangoli(self):
        r = Triedro._rettangoli(self)
        return {1: r[1], 2: r[2]}

    def piani(self, etichette=True):
        r = self._rettangoli()
        for i in (1, 2):
            self._poligono(r[i], "#9aa5b1", 0.10, "#b7bfc8")
        self._linea((self.X3 - self.U, 0, 0), (self.X3, 0, 0), "nero", 1.6)


def piano3(a, b, c):
    n = cross(sub(b, a), sub(c, a))
    return n, dot(n, a)


def taglio(pl, P, Q):
    n, d = pl
    fP, fQ = dot(n, P) - d, dot(n, Q) - d
    return add(P, mul(sub(Q, P), fP / (fP - fQ)))


def intersezione_piani(p1, p2):
    (n1, d1), (n2, d2) = p1, p2
    u = cross(n1, n2)
    uu = dot(u, u)
    P = add(mul(cross(u, n1), d2 / uu), mul(cross(n2, u), d1 / uu))
    return P, add(P, u)


def tracce(P, Q):
    t1 = add(P, mul(sub(Q, P), -P[2] / (Q[2] - P[2]))) if Q[2] != P[2] else None
    t2 = add(P, mul(sub(Q, P), -P[1] / (Q[1] - P[1]))) if Q[1] != P[1] else None
    return t1, t2


def su_piano(pl, P, tol=1e-6):
    n, d = pl
    return abs(dot(n, P) - d) < tol * max(1, math.sqrt(dot(n, n)))


# =====================================================================
# 1. Il parallelepipedo tagliato da un piano proiettante in seconda, nello spazio
# =====================================================================

def parallelepipedo_spazio():
    X1, X2, Y1, Y2, H = 40, 180, 20, 100, 90
    alfa = ((5, 0, 7), 1180)                     # proiettante in seconda: t2a per (110, 90) e (180, 40)
    S1, S2, S3, S4 = (X2, Y1, 40), (X2, Y2, 40), (110, Y2, H), (110, Y1, H)
    for P in (S1, S2, S3, S4):
        assert su_piano(alfa, P)

    f = Figura(620, 640, 0, "Nello spazio: il piano proiettante in seconda taglia il parallelepipedo")
    retino(f)
    X3 = 270
    t = Diedro(f, (220, 270), X3=X3, U=320, Y=200, Z=210, scala=1.2)
    t.piani(etichette=False)
    t.testo((-20, 185, 0), "π_1", 0, 0, "grigio", 15)
    t.testo((-30, 0, 190), "π_2", 0, 0, "grigio", 15)
    t.testo((X3, 0, 0), "LT", 6, 4, "nero", 13)
    p = t._p

    # alfa (rosa) e le sue tracce
    t.piano(*alfa, "rosso", 0.07)
    t.tracce(*alfa, "nero")
    t.testo((40, 0, (1180 - 200) / 7), "t_2α", -34, 0, "nero", 13)
    t.testo((236, 190, 0), "t_1α", 6, 12, "nero", 13)
    # beta: piano di profilo del fianco destro; gamma: piano orizzontale della faccia superiore
    t.tracce((1, 0, 0), X2, "verde")
    t.testo((X2, 0, 190), "t_2β", 6, 4, "verde", 13)
    t.testo((X2, 190, 0), "t_1β", -34, 14, "verde", 13)
    t.tracce((0, 0, 1), H, "verde")
    t.testo((-50, 0, H), "t_2γ", 0, -8, "verde", 13)

    # la parte di solido che il piano porta via (grigio, tratteggiata)
    for y in (Y1, Y2):
        rline(f, p((110, y, H)), p((X2, y, H)), "grigio", 1, "5,4")
        rline(f, p((X2, y, H)), p((X2, y, 40)), "grigio", 1, "5,4")
    rline(f, p((X2, Y1, H)), p((X2, Y2, H)), "grigio", 1, "5,4")

    # solido rimasto
    facce = [
        [(X1, Y1, 0), (X2, Y1, 0), (X2, Y2, 0), (X1, Y2, 0)],
        [(X1, Y1, 0), (X2, Y1, 0), S1, S4, (X1, Y1, H)],
        [(X1, Y2, 0), (X2, Y2, 0), S2, S3, (X1, Y2, H)],
        [(X1, Y1, 0), (X1, Y2, 0), (X1, Y2, H), (X1, Y1, H)],
        [(X2, Y1, 0), (X2, Y2, 0), S2, S1],
        [(X1, Y1, H), S4, S3, (X1, Y2, H)],
        [S4, S3, S2, S1],
    ]
    disegna_solido(f, p, facce, VISTA, "blu", 0.12, 2)
    rpoly(f, [p(S1), p(S2), p(S3), p(S4)], "rosso", 0, "rosso", 2.6, None, True)

    # le rette di intersezione: proiettanti in seconda, bucano pi2 in un punto (r2, s2)
    rline(f, p((X2, 0, 40)), p((X2, 160, 40)), "arancio", 1.6)
    rline(f, p((110, 0, H)), p((110, 160, H)), "arancio", 1.6)
    rdot(f, p((X2, 0, 40)), "arancio")
    rdot(f, p((110, 0, H)), "arancio")
    rtext(f, p((X2, 0, 40)), "r_2", 6, -6, "arancio", 14)
    rtext(f, p((110, 0, H)), "s_2", 8, -8, "arancio", 14)
    rtext(f, p((X2, 160, 40)), "r", 6, 4, "arancio", 15)
    rtext(f, p((110, 160, H)), "s", 6, 4, "arancio", 15)
    for P, s, dx, dy in ((S1, "1", 4, 20), (S2, "2", 8, 6), (S3, "3", -16, -6), (S4, "4", -20, -2)):
        rdot(f, p(P))
        rtext(f, p(P), s, dx, dy, "nero", 14)

    note(f, 400, [
        "α (in rosa) taglia il fianco destro (piano di profilo β) lungo r e la faccia superiore (piano orizzontale γ)",
        "lungo s: r e s sono perpendicolari a π₂ e lo bucano in un punto, r₂ e s₂, che stanno su t₂α.",
        "r taglia gli spigoli del fianco in 1 e 2, s quelli della faccia superiore in 3 e 4; la parte in grigio si elimina."], 12.5)
    f.h = 464
    f.salva(OUT + f"b15-spazio-parallelepipedo-proiettante-in-seconda{VER}.svg")


# =====================================================================
# 2. La piramide tagliata da un piano generico, con i piani proiettanti per gli spigoli, nello spazio
# =====================================================================

def piramide_spazio():
    SC = 1.3
    A, B, C, V = [mul(q, SC) for q in [(40, 30, 0), (120, 125, 0), (190, 30, 0), (120, 80, 166)]]
    XA, KA = -40 * SC, 0.8
    ab = sub(B, A)
    O = (XA, 0, 0)
    npl = (-ab[1], ab[0], 0)
    if dot(npl, sub(C, O)) < 0:
        npl = mul(npl, -1)
    L = math.hypot(npl[0], npl[1])
    alfa = piano3(O, add(O, ab), add(O, (npl[0] / L * 10, npl[1] / L * 10, 10 * KA)))
    p1, p2, p3 = taglio(alfa, C, V), taglio(alfa, A, V), taglio(alfa, B, V)
    beta = piano3(V, C, add(C, (0, 0, 1)))          # proiettante in prima per VC
    gamma = piano3(V, A, add(A, (0, 1, 0)))         # proiettante in seconda per VA
    T1r, T2r = tracce(*intersezione_piani(alfa, beta))
    T1s, T2s = tracce(*intersezione_piani(alfa, gamma))
    assert su_piano(beta, p1) and su_piano(gamma, p2)

    X3, U, Y, Z = 330, 400, 200, 260
    f = Figura(620, 640, 0, "Nello spazio: la piramide, il piano α e i piani proiettanti per gli spigoli")
    retino(f)
    t = Diedro(f, (170, 290), X3=X3, U=U, Y=Y, Z=Z, scala=1.0)
    t.piani(etichette=False)
    t.testo((330, 150, 0), "π_1", 0, 0, "grigio", 15)
    t.testo((-50, 0, 240), "π_2", 0, 0, "grigio", 15)
    t.testo((X3, 0, 0), "LT", 6, 4, "nero", 13)
    p = t._p

    t.piano(*alfa, "rosso", 0.06)
    tr = t.tracce(*alfa, "nero")
    t.testo((-30, 0, 0.612 * 22), "t_2α", -10, -14, "nero", 13)
    t.testo(add(O, mul(ab, 1.55)), "t_1α", 8, 4, "nero", 13)
    tb = t.tracce(*beta, "verde")
    tg = t.tracce(*gamma, "viola")
    t.testo((T2r[0], 0, 250), "t_2β", 6, 10, "verde", 13)
    t.testo(tb[1][1] if tb[1][1][1] > tb[1][0][1] else tb[1][0], "t_1β", -36, 6, "verde", 13)
    t.testo((A[0], 0, 0) if False else tg[2][1] if tg[2][1][2] > tg[2][0][2] else tg[2][0], "t_2γ", -34, 10, "viola", 13)
    t.testo((A[0], Y, 0), "t_1γ", -34, 6, "viola", 13)

    # piramide
    facce = [[A, B, C], [A, B, V], [B, C, V], [C, A, V]]
    disegna_solido(f, p, facce, VISTA, "blu", 0.10, 2)

    # rette di intersezione r = alfa ∩ beta, s = alfa ∩ gamma
    rline(f, p(T1r), p(T2r), "arancio", 1.6)
    rline(f, p(T1s), p(T2s), "arancio", 1.6)
    for P, s, dx, dy in ((T1r, "T_{1r}", 10, 4), (T2r, "T_{2r}", 6, -6), (T1s, "T_{1s}", -40, 14), (T2s, "T_{2s}", -42, -4)):
        rdot(f, p(P), "arancio")
        rtext(f, p(P), s, dx, dy, "arancio", 13)
    rtext(f, p(add(T1r, mul(sub(T2r, T1r), 0.75))), "r", 4, 16, "arancio", 15)
    rtext(f, p(add(T1s, mul(sub(T2s, T1s), 0.1))), "s", -18, 0, "arancio", 15)

    # sezione
    rpoly(f, [p(p1), p(p2), p(p3)], "rosso", 0, "rosso", 2.6, None, True)
    for P, s, dx, dy in ((p1, "1", 8, -2), (p2, "2", -16, -4), (p3, "3", 8, 12)):
        rdot(f, p(P))
        rtext(f, p(P), s, dx, dy, "nero", 14)
    for P, s, dx, dy in ((A, "A", -16, 14), (B, "B", 6, 16), (C, "C", 8, 4), (V, "V", 6, -8)):
        rtext(f, p(P), s, dx, dy, "blu", 15)

    note(f, 400, [
        "β (tracce verdi) è il piano verticale che contiene lo spigolo VC: α lo taglia lungo r, che incontra VC in 1.",
        "γ (tracce viola) è proiettante in seconda e contiene lo spigolo VA: α lo taglia lungo s, che incontra VA in 2.",
        "Il terzo punto, su VB, si trova con l'omologia: la sezione 1-2-3 (in rosso) sta tutta nel piano α."], 12.5)
    f.h = 464
    f.salva(OUT + f"b15-spazio-piramide-piani-per-gli-spigoli{VER}.svg")


if __name__ == "__main__":
    parallelepipedo_spazio()
    piramide_spazio()
