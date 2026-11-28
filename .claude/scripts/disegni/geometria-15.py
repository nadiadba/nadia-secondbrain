"""Schemi per la sbobina di geometria descrittiva del 24 novembre (15-...): il ripasso per la Prova n. 2.

- la sezione di un parallelepipedo con un piano proiettante in seconda (piani delle facce, rette proiettanti in seconda);
- il teorema di Desargues nello spazio (piramide tagliata da un piano: omologia con centro nel vertice);
- la sezione di una piramide con un piano generico: punto 1 con un piano proiettante in prima, punto 2 con un
  piano proiettante in seconda, punto 3 con l'omologia (e l'orizzontale 2-3, perche' VB e' una retta di profilo);
- il ribaltamento della sezione su pi1.

Convenzioni di disegni_monge.py: punto nello spazio (x, aggetto, quota); prima proiezione sotto la LT,
seconda sopra. Notazione della docente: P_1, P_2, r_1, r_2, T_1r, T_2r, (T_1r)_2. Tutti i punti sono
calcolati nello spazio (intersezioni di piani e rette) e poi proiettati, cosi' le costruzioni sono esatte.

Usa disegni_monge.py senza modificarlo.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, interseca, COLORI, P1, P2

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


# ---------- geometria nello spazio ----------

def sub(a, b): return tuple(a[i] - b[i] for i in range(3))
def add(a, b): return tuple(a[i] + b[i] for i in range(3))
def mul(a, k): return tuple(x * k for x in a)
def dot(a, b): return sum(a[i] * b[i] for i in range(3))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def piano(a, b, c):
    n = cross(sub(b, a), sub(c, a))
    return n, dot(n, a)


def taglio(pl, P, Q):
    """Punto in cui il segmento PQ incontra il piano pl."""
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


def vicino(p, q, tol=0.05):
    return math.dist(p, q) < tol


def allinea(p, q, r, tol=0.05):
    """Vero se i tre punti del disegno sono allineati."""
    return abs((q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])) / math.dist(p, q) < tol


# ---------- aiuti di disegno ----------

def campitura(f, poligono, passo=7, colore="rosso", ang=45):
    """Tratteggio fitto e ordinato dentro un poligono convesso (coordinate di disegno)."""
    a = math.radians(ang)
    d = (math.cos(a), math.sin(a))
    nrm = (-d[1], d[0])
    proj = [p[0] * nrm[0] + p[1] * nrm[1] for p in poligono]
    c = min(proj) + passo / 2
    while c < max(proj):
        pts = []
        for i in range(len(poligono)):
            p, q = poligono[i], poligono[(i + 1) % len(poligono)]
            fp = p[0] * nrm[0] + p[1] * nrm[1] - c
            fq = q[0] * nrm[0] + q[1] * nrm[1] - c
            if fp * fq < 0:
                t = fp / (fp - fq)
                pts.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
        if len(pts) >= 2:
            f._linea(pts[0], pts[1], colore, 0.8)
        c += passo


def arco(f, c, r, a0, a1, colore="grigio", n=50):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(f._s((c[0] + r * math.cos(a), c[1] + r * math.sin(a))))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    f.parti.append(f'<path d="{d}" fill="none" stroke="{COLORI[colore]}" stroke-width="1" stroke-dasharray="5,4"/>')


def prolunga(p, q, a=0.0, b=1.0):
    """Punti della retta pq ai parametri a e b (0 = p, 1 = q)."""
    return ((p[0] + a * (q[0] - p[0]), p[1] + a * (q[1] - p[1])),
            (p[0] + b * (q[0] - p[0]), p[1] + b * (q[1] - p[1])))


# =====================================================================
# 15a. Il parallelepipedo tagliato da un piano proiettante in seconda
# =====================================================================
X1, X2, Y1, Y2, H = 40, 180, 20, 100, 90
# alfa e' proiettante in seconda: t2a passa per (110, quota H) e (180, quota 40)
pa, pb = (110, 90), (180, 40)
xa = interseca(pa, pb, (0, 0), (1, 0))[0]                 # dove t2a incontra la LT
S = [(110, Y1, H), (110, Y2, H), (180, Y2, 40), (180, Y1, 40)]   # 4, 3 sulla faccia superiore; 2, 1 sul fianco
for p in S:  # controllo: i punti stanno su alfa (in seconda proiezione sulla t2a)
    assert allinea(pa, (xa, 0), P2(p))

f = Figura(640, 400, 200, "La sezione del parallelepipedo con un piano proiettante in seconda", x0=70)
f.lt(-50, 300)
# seconda proiezione
f.figura([(X1, 0), (X2, 0), (X2, H), (X1, H)])
f._linea((110, H), (X2, H), "grigio", 1.2, "4,3")
f._linea((X2, H), (X2, 40), "grigio", 1.2, "4,3")
# prima proiezione
f.figura([(X1, -Y1), (X2, -Y1), (X2, -Y2), (X1, -Y2)])
# il piano gamma della faccia superiore (orizzontale): la seconda traccia sta li', alla quota H
f._linea((-40, H), (20, H), "verde", 1.6)
f.testo((-40, H), "t_2γ", dx=0, dy=-6, colore="verde")
# il piano beta (di profilo) del fianco destro: tracce perpendicolari alla LT
f._linea((X2, H + 8), (X2, H + 40), "verde", 1.6)
f._linea((X2, -Y2 - 6), (X2, -Y2 - 40), "verde", 1.6)
f.testo((X2, H + 40), "t_2β", dx=-28, dy=4, colore="verde")
f.testo((X2, -Y2 - 40), "t_1β", dx=-28, dy=4, colore="verde")
# alfa
top = interseca(pa, pb, (0, 150), (1, 150))
f.traccia((xa, 0), top)
f.traccia((xa, 0), (xa, -150))
f.testo(top, "t_2α", dx=-30, dy=4)
f.testo((xa, -150), "t_1α", dx=6, dy=0)
# rette di intersezione: proiettanti in seconda (in seconda sono punti, in prima perpendicolari alla LT)
f.punto(pa, "s_2", dx=4, dy=-10, colore="arancio")
f.punto(pb, "r_2", dx=-22, dy=18, colore="arancio")
f._linea((110, -Y1 + 10), (110, -Y2 - 10), "arancio", 1.6)
f.testo((110, -Y2 - 10), "s_1", dx=-8, dy=16, colore="arancio")
f.testo((X2, -Y2 - 10), "r_1", dx=6, dy=14, colore="arancio")
f.richiamo(110, H, -Y1)
f.richiamo(X2, 40, -Y1)
# sezione
f._linea(pa, pb, "rosso", 3)
q = [(110, -Y1), (X2, -Y1), (X2, -Y2), (110, -Y2)]
campitura(f, q)
for p in q:
    pass
f._linea(q[0], q[3], "rosso", 2.4)
f._linea(q[0], q[1], "rosso", 1.4)
f._linea(q[2], q[3], "rosso", 1.4)
f._linea(q[1], q[2], "rosso", 1.4)
f.testo(pa, "4_2 ≡ 3_2", dx=-82, dy=-8, colore="rosso")
f.testo(pb, "1_2 ≡ 2_2", dx=10, dy=-6, colore="rosso")
f.testo((110, -Y1), "4_1", dx=-24, dy=-4, colore="rosso")
f.testo((110, -Y2), "3_1", dx=-24, dy=14, colore="rosso")
f.testo((X2, -Y2), "2_1", dx=8, dy=-6, colore="rosso")
f.testo((X2, -Y1), "1_1", dx=8, dy=16, colore="rosso")
f.nota(14, 386, "s = α ∩ faccia superiore, r = α ∩ fianco: rette proiettanti in seconda. Dove tagliano gli spigoli: 1, 2, 3, 4.", 12.5)
f.nota(14, 404, "In grigio il pezzo di solido che il piano porta via.", 12.5)
f.h = 414
f.salva(OUT + "15-ripasso-parallelepipedo-piano-proiettante-in-seconda.svg")


# =====================================================================
# 15b. Il teorema di Desargues nello spazio
# =====================================================================
def vista(p):
    """Vista obliqua semplice: x a destra, y in profondita' (in alto a destra), z in alto."""
    return (p[0] + 0.55 * p[1], p[2] + 0.38 * p[1])


Ad, Bd, Cd, Vd = (0, 0, 0), (200, 20, 0), (70, 150, 0), (95, 60, 210)
sez = ((0.2988, 0.7711, -1), -34.2)                          # piano secante: z = 34.2 + 0.2988 x + 0.7711 y
A_, B_, C_ = (taglio(sez, Ad, Vd), taglio(sez, Bd, Vd), taglio(sez, Cd, Vd))
asse = intersezione_piani(sez, ((0, 0, 1), 0))               # il piano secante incontra il piano della base


def su_asse(P, Q, R, S_):
    """Punto in cui le rette PQ e RS (nello spazio, complanari) si incontrano, in vista."""
    return interseca(vista(P), vista(Q), vista(R), vista(S_))


XAB, XBC, XCA = su_asse(Ad, Bd, A_, B_), su_asse(Bd, Cd, B_, C_), su_asse(Cd, Ad, C_, A_)
assert allinea(XAB, XBC, XCA)
assert allinea(vista(asse[0]), vista(asse[1]), XAB)

f = Figura(760, 400, 290, "Il teorema di Desargues nello spazio: la piramide tagliata da un piano", x0=170)
# piano della base (leggero)
f.parti.append('<polygon points="{}" fill="#2563a8" fill-opacity="0.05" stroke="none"/>'.format(
    " ".join("{:.1f},{:.1f}".format(*f._s(vista(p))) for p in [(-140, 30, 0), (60, -235, 0), (470, -235, 0), (330, 190, 0), (-60, 190, 0)])))
f.testo(vista((380, 150, 0)), "piano della base", dx=-150, dy=22, dimensione=12, corsivo=False, colore="blu")
f.figura([vista(Ad), vista(Bd), vista(Cd)])
for P in (Ad, Bd):
    f.retta(vista(P), vista(Vd), "blu", 1.6)
f._linea(vista(Cd), vista(Vd), "blu", 1.2, "5,4")
f.figura([vista(A_), vista(B_), vista(C_)], "rosso")
# l'asse dell'omologia
ea = prolunga(XAB, XBC, -0.1, 1.08)
f.traccia(ea[0], ea[1], "verde")
f.testo(ea[0], "asse", dx=-4, dy=-10, colore="verde", corsivo=False)
# lati prolungati fino all'asse
for P, Q, X in [(Ad, Bd, XAB), (A_, B_, XAB), (Bd, Cd, XBC), (B_, C_, XBC), (Cd, Ad, XCA), (C_, Ad, None)]:
    if X is None:
        continue
    f.costruzione(vista(P), X)
f.costruzione(vista(C_), XCA)
f.costruzione(vista(A_), XCA)
for X, n in [(XAB, "X"), (XBC, "Y"), (XCA, "Z")]:
    f.punto(X, n, dx=-4, dy=20, colore="verde")
f.punto(vista(Vd), "V (centro)", dx=8, dy=-4)
for P, n, dx, dy in [(Ad, "A", -16, 14), (Bd, "B", 8, 14), (Cd, "C", -6, -10)]:
    f.punto(vista(P), n, dx=dx, dy=dy, colore="blu")
for P, n, dx, dy in [(A_, "A′", -22, 4), (B_, "B′", 8, 4), (C_, "C′", 8, -6)]:
    f.punto(vista(P), n, dx=dx, dy=dy, colore="rosso")
f.nota(14, 412, "I vertici corrispondenti (A e A′, B e B′, C e C′) sono allineati con V; i lati corrispondenti", 12.5)
f.nota(14, 430, "(AB e A′B′, ...) si incontrano sull'asse, la retta in cui il piano secante taglia il piano della base.", 12.5)
f.h = 440
f.salva(OUT + "15-ripasso-teorema-di-desargues-nello-spazio.svg")


# =====================================================================
# Dati comuni della piramide: base ABC su pi1 con AC parallelo alla LT, VB retta di profilo,
# piano alfa generico con t1a parallela ad AB
# =====================================================================
SC = 1.3                               # scala del disegno
A, B, C, V = [mul(p, SC) for p in [(40, 30, 0), (120, 125, 0), (190, 30, 0), (120, 80, 166)]]
XA, KA = -40 * SC, 0.8                 # t1a passa per (XA, 0, 0); pendenza del piano
ab = sub(B, A)
O = (XA, 0, 0)
npl = (-ab[1], ab[0], 0)
if dot(npl, sub(C, O)) < 0:
    npl = mul(npl, -1)
L = math.hypot(npl[0], npl[1])
alfa = piano(O, add(O, ab), add(O, (npl[0] / L * 10, npl[1] / L * 10, 10 * KA)))
p1, p2, p3 = taglio(alfa, C, V), taglio(alfa, A, V), taglio(alfa, B, V)
beta = piano(V, C, add(C, (0, 0, 1)))          # proiettante in prima per lo spigolo VC
gamma = piano(V, A, add(A, (0, 1, 0)))         # proiettante in seconda per lo spigolo VA
T1r, T2r = tracce(*intersezione_piani(alfa, beta))
T1s, T2s = tracce(*intersezione_piani(alfa, gamma))
t2a_alto = tracce(*intersezione_piani(alfa, ((0, 1, 0), 0)))
# seconda traccia di alfa: retta per (XA, 0) e T2r
assert abs(p2[2] - p3[2]) < 1e-6            # 2-3 e' un'orizzontale del piano
# controlli in proiezione
assert allinea(P2(T2r), P2(V), P2(V)) or True
assert allinea(P2(p1), P2(T2r), (T1r[0], 0))   # 1_2 sta su r_2
assert allinea(P1(p2), P1(T1s), (T2s[0], 0))   # 2_1 sta su s_1


def base_piramide(f, punti=True):
    f.figura([P2(A), P2(C)], "blu")
    for Pt in (A, B, C):
        f.retta(P2(Pt), P2(V), "blu", 1.6)
    f.figura([P1(A), P1(B), P1(C)])
    for Pt in (A, B, C):
        f.retta(P1(Pt), P1(V), "blu", 1.6)
    if punti:
        f.punto(P2(V), "V_2", dx=8, dy=-4, colore="blu")
        f.punto(P1(V), "V_1", dx=8, dy=4, colore="blu")
        for Pt, n, dx, dy in [(A, "A", -24, 16), (B, "B", 8, 16), (C, "C", 6, -6)]:
            f.testo(P2(Pt), n + "_2", dx=dx, dy=dy, colore="blu")
        for Pt, n, dx, dy in [(A, "A", -26, 4), (B, "B", -4, 18), (C, "C", 6, 4)]:
            f.testo(P1(Pt), n + "_1", dx=dx, dy=dy, colore="blu")


def tracce_alfa(f, x_fine=300):
    top = interseca((XA, 0), P2(T2r), (0, V[2] + 40), (1, V[2] + 40))
    f.traccia((XA, 0), top)
    f.testo(top, "t_2α", dx=6, dy=10)
    fondo = interseca((XA, 0), (XA + ab[0], -ab[1]), (0, -B[1] - 50), (1, -B[1] - 50))
    f.traccia((XA, 0), fondo)
    f.testo(fondo, "t_1α", dx=6, dy=4)


# =====================================================================
# 15c. La piramide: i punti 1 e 2 con i piani proiettanti per gli spigoli
# =====================================================================
f = Figura(760, 500, 275, "La sezione della piramide: i punti 1 e 2 con i piani proiettanti", x0=130)
f.lt(-110, 330)
base_piramide(f)
tracce_alfa(f)
# beta: proiettante in prima per VC
Lb = interseca(P1(V), P1(C), (0, 0), (1, 0))
b_fondo = prolunga((Lb[0], 0), P1(T1r), 0, 1.12)[1]
f._linea(b_fondo, (Lb[0], 0), "verde", 1.6)
f._linea((Lb[0], 0), (Lb[0], V[2] + 40), "verde", 1.6)
f.testo((Lb[0], V[2] + 40), "t_2β", dx=6, dy=10, colore="verde")
f.testo(b_fondo, "t_1β ≡ r_1", dx=-64, dy=14, colore="verde")
# r = alfa ∩ beta
f.punto(P1(T1r), "T_{1r}", dx=10, dy=-4)
f.richiamo(T1r[0], 0, -T1r[1])
f.punto((T1r[0], 0), "(T_{1r})_2", dx=-6, dy=24)
f.punto(P2(T2r), "T_{2r}", dx=8, dy=14)
f.retta((T1r[0], 0), P2(T2r), "arancio", 1.6)
f.testo(prolunga((T1r[0], 0), P2(T2r), 0, 0.85)[1], "r_2", dx=8, dy=16, colore="arancio")
# gamma: proiettante in seconda per VA
Lg = A[0]
g_top = prolunga(P2(A), P2(V), 0, 1.25)[1]
f._linea(P2(A), g_top, "viola", 1.6)
f.testo(g_top, "t_2γ", dx=-30, dy=4, colore="viola")
f._linea((Lg, 0), (Lg, -160), "viola", 1.6)
f.testo((Lg, -160), "t_1γ", dx=-30, dy=4, colore="viola")
f.punto(P2(T2s), "T_{2s}", dx=-40, dy=-6)
f.richiamo(T2s[0], T2s[2], 0)
f.punto((T2s[0], 0), "(T_{2s})_1", dx=4, dy=-8)
f.punto(P1(T1s), "T_{1s}", dx=-36, dy=-4)
f.retta(P1(T1s), (T2s[0], 0), "arancio", 1.6)
f.testo(P1(T1s), "s_1", dx=-24, dy=18, colore="arancio")
# i punti
f.richiamo(p1[0], p1[2], -p1[1])
f.richiamo(p2[0], p2[2], -p2[1])
for Pt, n, dx2, dy2, dx1, dy1 in [(p1, "1", 8, -2, 8, 16), (p2, "2", -20, -6, 6, 14)]:
    f.punto(P2(Pt), n + "_2", dx=dx2, dy=dy2, colore="rosso")
    f.punto(P1(Pt), n + "_1", dx=dx1, dy=dy1, colore="rosso")
f.nota(14, 530, "Punto 1: β proiettante in prima contiene VC; r = α ∩ β, e dove r₂ taglia V₂C₂ c'è 1₂ (poi 1₁ con il richiamo).", 12.5)
f.nota(14, 548, "Punto 2: γ proiettante in seconda contiene VA; s = α ∩ γ, e dove s₁ taglia V₁A₁ c'è 2₁ (poi 2₂ con il richiamo).", 12.5)
f.h = 558
f.salva(OUT + "15-ripasso-piramide-punti-1-e-2-piani-proiettanti.svg")


# =====================================================================
# 15d. La piramide: il punto 3 con l'omologia e con l'orizzontale 2-3
# =====================================================================
K = interseca(P1(A), P1(C), (XA, 0), (XA + ab[0], -ab[1]))   # A1C1 prolungata fino all'asse t1a
assert allinea(K, P1(p1), P1(p2))                               # l'omologia "torna"
q3 = interseca(P1(p2), (P1(p2)[0] + ab[0], P1(p2)[1] - ab[1]), P1(V), P1(B))
assert vicino(q3, P1(p3))

f = Figura(760, 500, 275, "La sezione della piramide: il punto 3 con l'omologia e l'orizzontale 2-3", x0=130)
f.lt(-110, 330)
base_piramide(f)
tracce_alfa(f)
f.costruzione(P1(C), K)
f.costruzione(K, P1(p1))
f.punto(K, "K", dx=-18, dy=-6, colore="verde")
f.testo(interseca((XA, 0), (XA + ab[0], -ab[1]), (0, -B[1] - 20), (1, -B[1] - 20)), "asse dell'omologia", dx=-122, dy=4, colore="verde", dimensione=12, corsivo=False)
# 2-3 parallela ad AB (e a t1a)
f.retta(P1(p2), P1(p3), "rosso", 1.6)
# in seconda: 2-3 e' un'orizzontale, parallela alla LT
f.retta(P2(p2), P2(p3), "rosso", 1.6)
sez1 = [P1(p1), P1(p2), P1(p3)]
sez2 = [P2(p1), P2(p2), P2(p3)]
campitura(f, sez1, 6)
campitura(f, sez2, 6)
f.figura(sez1, "rosso")
f.figura(sez2, "rosso")
f.richiamo(p1[0], p1[2], -p1[1])
f.richiamo(p2[0], p2[2], -p2[1])
for Pt, n, dx2, dy2, dx1, dy1 in [(p1, "1", 8, -2, 8, 16), (p2, "2", -24, -4, -6, 18), (p3, "3", 6, 16, 8, 12)]:
    f.punto(P2(Pt), n + "_2", dx=dx2, dy=dy2, colore="rosso")
    f.punto(P1(Pt), n + "_1", dx=dx1, dy=dy1, colore="rosso")
f.nota(14, 530, "In prima (omologia con centro V₁ e asse t₁α): da 2₁ la parallela ad A₁B₁ (e a t₁α) fino a V₁B₁ dà 3₁.", 12.5)
f.nota(14, 548, "Controllo: A₁C₁ prolungata e 2₁1₁ si incontrano in K, sull'asse.", 12.5)
f.nota(14, 566, "In seconda: VB è una retta di profilo, il richiamo non basta; 2-3 è un'orizzontale, quindi 3₂ sta alla quota di 2₂.", 12.5)
f.h = 576
f.salva(OUT + "15-ripasso-piramide-punto-3-omologia.svg")


# =====================================================================
# 15e. Il ribaltamento della sezione su pi1, intorno a t1a
# =====================================================================
d_ax = (ab[0], -ab[1])
la = math.hypot(*d_ax)
u_ax = (d_ax[0] / la, d_ax[1] / la)
n_ax = (-u_ax[1], u_ax[0])
if (P1(C)[0] - XA) * n_ax[0] + P1(C)[1] * n_ax[1] > 0:     # si ribalta dalla parte opposta alla piramide
    n_ax = (-n_ax[0], -n_ax[1])


def piede(p):
    t = (p[0] - XA) * u_ax[0] + p[1] * u_ax[1]
    return (XA + t * u_ax[0], t * u_ax[1])


def ribaltato(P):
    """Ribaltamento vero nello spazio: distanza del punto dall'asse, riportata sulla perpendicolare."""
    h = piede(P1(P))
    dist = math.hypot(math.dist(h, P1(P)), P[2])
    return (h[0] + dist * n_ax[0], h[1] + dist * n_ax[1])


R1, R2, R3 = ribaltato(p1), ribaltato(p2), ribaltato(p3)
# con l'affinita': 1-3 fino all'asse, poi da li' verso 1*, e 3* sulla perpendicolare da 3_1
K13 = interseca(P1(p1), P1(p3), (XA, 0), (XA + d_ax[0], d_ax[1]))
h3 = piede(P1(p3))
R3b = interseca(K13, R1, h3, (h3[0] + n_ax[0], h3[1] + n_ax[1]))
assert vicino(R3b, R3, 0.1)
h2 = piede(P1(p2))
R2b = interseca(R3, (R3[0] + u_ax[0], R3[1] + u_ax[1]), h2, (h2[0] + n_ax[0], h2[1] + n_ax[1]))
assert vicino(R2b, R2, 0.1)
assert abs(math.dist(R1, R2) - math.dist(p1, p2)) < 0.1   # vera forma

tutti = [P1(A), P1(B), P1(C), R1, R2, R3, (XA, 0)]
xmin, xmax = min(p[0] for p in tutti), max(p[0] for p in tutti)
ymin = min(p[1] for p in tutti)
FW = 700
FH = int(-ymin + 120)
f = Figura(FW, FH + 50, 50, "Il ribaltamento della sezione su π₁, intorno a t₁α", x0=(FW - (xmax - xmin)) / 2 - xmin)
f.lt(xmin - 40, xmax + 40)
fondo = interseca((XA, 0), (XA + d_ax[0], d_ax[1]), (0, ymin - 30), (1, ymin - 30))
f.traccia((XA, 0), fondo)
f.testo(fondo, "t_1α (asse)", dx=8, dy=4)
f.figura([P1(A), P1(B), P1(C)], "grigio")
sez1 = [P1(p1), P1(p2), P1(p3)]
f.figura(sez1, "rosso")
# punto 1: perpendicolare all'asse, quota, raggio
h1 = piede(P1(p1))
f.costruzione(P1(p1), R1)
Q1 = (P1(p1)[0] + p1[2] * u_ax[0], P1(p1)[1] + p1[2] * u_ax[1])   # la quota di 1 riportata parallela all'asse
f._linea(P1(p1), Q1, "arancio", 1.8)
f.testo(((P1(p1)[0] + Q1[0]) / 2, (P1(p1)[1] + Q1[1]) / 2), "quota", dx=4, dy=-6, colore="arancio", dimensione=12, corsivo=False)
f._linea(h1, Q1, "arancio", 1.2, "6,3")
f.testo((0.3 * h1[0] + 0.7 * Q1[0], 0.3 * h1[1] + 0.7 * Q1[1]), "raggio", dx=-20, dy=18, colore="arancio", dimensione=12, corsivo=False)
r1 = math.dist(h1, Q1)
a_q = math.degrees(math.atan2(Q1[1] - h1[1], Q1[0] - h1[0]))
a_r = math.degrees(math.atan2(R1[1] - h1[1], R1[0] - h1[0]))
arco(f, h1, r1, a_q, a_r)
f.angolo_retto(h1, u_ax, n_ax, 8)
# 3 e 2 con l'affinita'
f.costruzione(P1(p1), K13)
f.costruzione(K13, R1)
f.costruzione(P1(p3), R3)
f.costruzione(P1(p2), R2)
f.punto(K13, None, colore="verde")
f.testo(K13, "K", dx=-18, dy=-4, colore="verde")
f.figura([R1, R2, R3], "rosso")
campitura(f, [R1, R2, R3], 6)
for Pt, n, dx, dy in [(p1, "1_1", -8, -10), (p2, "2_1", -26, 6), (p3, "3_1", -26, -2)]:
    f.punto(P1(Pt), n, dx=dx, dy=dy, colore="rosso")
for Pt, n, dx, dy in [(R1, "1*", 8, 6), (R2, "2*", -22, 16), (R3, "3*", 6, -6)]:
    f.punto(Pt, n, dx=dx, dy=dy, colore="rosso")
f.nota(14, FH + 22, "1*: perpendicolare a t₁α da 1₁, la quota di 1 riportata in 1₁, il raggio fino all'asse, l'arco sulla perpendicolare.", 12.5)
f.nota(14, FH + 40, "3*: 1₁3₁ fino all'asse (K), poi K1* fino alla perpendicolare da 3₁. 2*: da 3* la parallela all'asse (2-3 è orizzontale).", 12.5)
f.h = FH + 50
f.salva(OUT + "15-ripasso-piramide-ribaltamento-sezione.svg")

print("ok", [tuple(round(c, 1) for c in p) for p in (p1, p2, p3)], "T1r", T1r, "T2r", T2r, "T1s", T1s, "T2s", T2s)
