"""Schemi per la sbobina di geometria descrittiva del 26 novembre (15-...): la prospettiva a occhio di formica.

Convenzioni (come in geometria-13-14.py):
- l'orizzonte e' orizzontale, a quota 0 nel disegno; O0 e' il punto principale, O* sta sotto a distanza d;
- nella prospettiva a occhio di formica l'occhio sta sul geometrale: orizzonte e fondamentale coincidono.
  Per disegnare la pianta si usa una fondamentale ausiliaria (F), a distanza h sotto l'orizzonte: la pianta
  e' allora una normale prospettiva con l'occhio a quota h, e un punto (X, Y) del geometrale va in
  (X d/(d+Y), -h d/(d+Y));
- nella prospettiva vera (occhio a quota 0) il punto (X, Y) a quota z va in (X d/(d+Y), z d/(d+Y)):
  stessa ascissa della pianta ausiliaria, quindi gli spigoli si tirano su in verticale dalla pianta,
  e la base si schiaccia sull'orizzonte. Ogni costruzione e' controllata con questi conti.

Usa disegni_monge.py senza modificarlo.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def arco(f, c, r, a0, a1, colore="grigio", spessore=1, tratteggio="4,3", n=60):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(f._s((c[0] + r * math.cos(a), c[1] + r * math.sin(a))))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    f.parti.append(f'<path d="{d}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                   f'stroke-width="{spessore}"{dash}/>')


def vicino(p, q, tol=0.01):
    return math.dist(p, q) < tol


# =====================================================================
# 15a. Lo schema laterale: l'omino e la formica
# =====================================================================
f = Figura(820, 250, 190, "Lo schema laterale: l'omino e la formica", x0=0)
for x0, chi, hh in [(30, "omino", 90), (400, "formica", 0)]:
    q = x0 + 200                                   # il quadro visto di lato
    f._linea((x0 - 10, 0), (q + 120, 0), "nero", 1.4)
    f.testo((x0 - 10, 0), "geometrale", dx=0, dy=18, dimensione=12, corsivo=False)
    f._linea((q, -5), (q, 150), "nero", 1.6)
    f.testo((q, 150), "quadro", dx=6, dy=4, dimensione=12, corsivo=False)
    eye = (x0 + 20, hh)
    if hh:
        f._linea((x0 + 20, 0), eye, "grigio", 3)
    f.punto(eye, "O", dx=-6, dy=-10)
    # il raggio orizzontale dall'occhio: dove buca il quadro c'e' l'orizzonte
    f._linea(eye, (q + 110, hh), "rosso", 1.4, "6,4")
    f.punto((q, hh), None, colore="rosso")
    f.punto((q, 0), None, colore="nero")
    if hh:
        f.testo((q, hh), "orizzonte", dx=6, dy=-8, dimensione=12, colore="rosso", corsivo=False)
        f.testo((q, 0), "fondamentale", dx=6, dy=18, dimensione=12, corsivo=False)
        f._linea((x0 + 120, 0), (x0 + 120, hh), "grigio", 1, "3,3")
        f.testo((x0 + 120, hh / 2), "h", dx=6, dy=4)
    else:
        f.testo((q, 0), "orizzonte ≡ fondamentale", dx=6, dy=-10, dimensione=12, colore="rosso", corsivo=False)
    f._linea((x0 + 20, -24), (q, -24), "grigio", 1, "3,3")
    f.testo(((x0 + 20 + q) / 2, -24), "d", dx=-4, dy=-5)
f.nota(30, 244, "La formica sta sul geometrale: il suo orizzonte cade sulla fondamentale. La distanza d dal quadro si sceglie lo stesso.", 13)
f.salva(OUT + "15-occhio-di-formica-schema-laterale.svg")


# =====================================================================
# Dati comuni: il rettangolo ABCD in pianta, la retta r (lato AB) e la retta n (lato BC)
# =====================================================================
d, h = 210, 120                     # distanza e distanza tra orizzonte e fondamentale ausiliaria
th = math.radians(40)
ur = (math.cos(th), math.sin(th))   # direzione di r
un = (-math.sin(th), math.cos(th))  # direzione di n, perpendicolare a r
T = (-40, 0)                         # traccia di r sul quadro (in pianta)
tA, AB, BC = 30, 180, 120
A = (T[0] + tA * ur[0], tA * ur[1])
B = (A[0] + AB * ur[0], A[1] + AB * ur[1])
C = (B[0] + BC * un[0], B[1] + BC * un[1])
D = (A[0] + BC * un[0], A[1] + BC * un[1])


def aus(p):
    """Pianta in prospettiva con la fondamentale ausiliaria (occhio a quota h)."""
    k = d / (d + p[1])
    return (p[0] * k, -h * k)


def vera(p, z):
    """Prospettiva a occhio di formica (occhio a quota 0)."""
    k = d / (d + p[1])
    return (p[0] * k, z * k)


Os = (0, -d)
Fr = (d * ur[0] / ur[1], 0)
Fn = (d * un[0] / un[1], 0)
Mr = (Fr[0] - math.dist(Fr, Os), 0)
Mn = (Fn[0] + math.dist(Fn, Os), 0)
v1, v2 = (Fr[0], d), (Fn[0], d)
assert abs(v1[0] * v2[0] + v1[1] * v2[1]) < 1e-6           # angolo retto in O*
Ap, Bp, Cp, Dp = aus(A), aus(B), aus(C), aus(D)
Tr = aus(T)
assert vicino(Tr, (T[0], -h))
# r: misure sulla fondamentale ausiliaria, proiettate da M_r
Ar = (T[0] + tA, -h)
Br = (T[0] + tA + AB, -h)
assert vicino(interseca(Mr, Ar, Tr, Fr), Ap) and vicino(interseca(Mr, Br, Tr, Fr), Bp)
# n: la retta per B perpendicolare a r; la sua traccia e le misure da M_n
sT = -B[1] / un[1]
Tn = (B[0] + sT * un[0], -h)
Bn = (Tn[0] - (-sT), -h)            # n va verso sinistra entrando nel quadro
Cn = (Bn[0] - BC, -h)
assert vicino(interseca(Mn, Bn, Tn, Fn), Bp) and vicino(interseca(Mn, Cn, Tn, Fn), Cp)
# D': rette parallele hanno la stessa fuga
assert vicino(interseca(Ap, Fn, Cp, Fr), Dp)


def base_pianta(f, misure=True):
    f._linea((-300, 0), (300, 0), "nero", 1.6)
    f._linea((-300, -h), (300, -h), "nero", 1.6)
    f.testo((-300, -h), "(F) fondamentale ausiliaria", dx=2, dy=18, dimensione=12, corsivo=False)
    f.punto((0, 0), "O_0", dx=-8, dy=-10)
    f.richiamo(0, 0, -d)
    f.punto(Os, "O*", dx=8, dy=6)
    f.punto(Fr, "F_r", dx=-4, dy=-10)
    f.punto(Fn, "F_n", dx=-24, dy=18)
    f.costruzione(Os, Fr)
    f.costruzione(Os, Fn)
    f.angolo_retto(Os, (v1[0] / math.hypot(*v1), v1[1] / math.hypot(*v1)),
                   (v2[0] / math.hypot(*v2), v2[1] / math.hypot(*v2)), 12)
    # r' e le altre rette verso le fughe (sottili)
    f.retta(Tr, Fr, "rosso", 1.4)
    f._linea(Ap, Fn, "grigio", 0.9, "2,3")
    f._linea(Dp, Fr, "grigio", 0.9, "2,3")
    f._linea(Bp, Fn, "grigio", 0.9, "2,3")
    f.figura([Ap, Bp, Cp, Dp], "blu")
    f.punto(Tr, "T_r′", dx=2, dy=20, colore="rosso")
    if misure:
        f._linea(Tn, Bp, "grigio", 0.9, "2,3")
        a0 = math.degrees(math.atan2(Os[1], Os[0] - Fr[0]))
        arco(f, Fr, Fr[0] - Mr[0], 180, 360 + a0)
        a1 = math.degrees(math.atan2(Os[1], Os[0] - Fn[0]))
        arco(f, Fn, Mn[0] - Fn[0], a1, 360)
        f.punto(Mr, "M_r", dx=-10, dy=-10, colore="verde")
        f.punto(Mn, "M_n", dx=-6, dy=-10, colore="verde")
        for M, Q in [(Mr, Ar), (Mr, Br), (Mn, Bn), (Mn, Cn)]:
            f.costruzione(M, Q)
        f._linea(Ar, Br, "verde", 3)
        f._linea(Cn, Bn, "verde", 2, "6,3")
        f.punto(Ar, "A_r", dx=-6, dy=18, colore="verde")
        f.punto(Br, "B_r", dx=-8, dy=18, colore="verde")
        f.punto(Bn, "B_n", dx=-8, dy=-8, colore="verde")
        f.punto(Cn, "C_n", dx=-24, dy=-6, colore="verde")
        f.punto(Tn, "T_n′", dx=-4, dy=20, colore="grigio")


# =====================================================================
# 15b. La pianta con la fondamentale ausiliaria e i punti di misura
# =====================================================================
f = Figura(820, 270, 30, "La pianta con la fondamentale ausiliaria (F) e i punti di misura", x0=440)
base_pianta(f)
f.testo((-300, 0), "orizzonte ≡ fondamentale", dx=2, dy=-8, dimensione=12, corsivo=False)
for p, n, dx, dy in [(Ap, "A′", -26, -4), (Bp, "B′", 6, 14), (Cp, "C′", -6, -10), (Dp, "D′", -22, -4)]:
    f.punto(p, n, dx, dy, "blu")
f.salva(OUT + "15-occhio-di-formica-pianta-fondamentale-ausiliaria.svg")


# =====================================================================
# 15c. Le altezze sulla traccia del piano verticale alfa
# =====================================================================
H = 90
f = Figura(820, 380, 130, "Le altezze: si misurano sulla traccia del piano, dall'orizzonte in su", x0=440)
base_pianta(f, misure=False)
f.testo((-300, 0), "orizzonte ≡ fondamentale", dx=2, dy=-8, dimensione=12, corsivo=False)
for p, n, dx, dy in [(Ap, "A′", -26, -4), (Bp, "B′", 6, 14), (Cp, "C′", 6, -2), (Dp, "D′", -22, -4)]:
    f.punto(p, n, dx, dy, "blu")
# traccia del piano alfa (verticale, contiene r): la verticale per T_r'
f._linea((T[0], -h - 8), (T[0], H + 25), "nero", 2)
f.testo((T[0], H + 25), "t_α", dx=-24, dy=4)
# l'altezza vera, dall'orizzonte in su
f._linea((T[0], 0), (T[0], H), "verde", 4)
f.testo((T[0], H * 0.3), "H", dx=-16, dy=4, colore="verde")
At, Bt, Ct, Dt = vera(A, H), vera(B, H), vera(C, H), vera(D, H)
# verifiche: la quota portata da F_r tocca le verticali di A' e B'; gli spigoli stanno sopra la pianta
assert vicino(interseca((T[0], H), Fr, Ap, (Ap[0], 0)), At)
assert vicino(interseca((T[0], H), Fr, Bp, (Bp[0], 0)), Bt)
assert vicino(interseca(Bt, Fn, Cp, (Cp[0], 0)), Ct)
assert vicino(interseca(At, Fn, Ct, Fr), Dt)
f.costruzione((T[0], H), Fr)
f._linea(Bt, Fn, "grigio", 0.9, "2,3")
f._linea(At, Fn, "grigio", 0.9, "2,3")
# gli spigoli si tirano su in verticale dalla pianta
for p in (Ap, Bp, Cp, Dp):
    f.richiamo(p[0], p[1], 0)
xs = [vera(p, 0)[0] for p in (A, B, C, D)]
f._linea((min(xs), 0), (max(xs), 0), "rosso", 3)           # la base si riduce a una linea
for p, t in [(A, At), (B, Bt), (D, Dt)]:
    f._linea(vera(p, 0), t, "rosso", 2)
f._linea(vera(C, 0), Ct, "rosso", 1.2, "4,3")               # spigolo nascosto
f._linea(At, Bt, "rosso", 2)
f._linea(At, Dt, "rosso", 2)
f._linea(Bt, Ct, "rosso", 1.2, "4,3")
f._linea(Dt, Ct, "rosso", 1.2, "4,3")
f.testo((26, 18), "faccia α", dx=0, dy=0, dimensione=12,
        colore="rosso", corsivo=False)
f.nota(20, 365, "La traccia del piano α è la verticale che sale da Tᵣ′. H si stacca su di essa dall'orizzonte e si porta da Fᵣ sugli spigoli.", 13)
f.salva(OUT + "15-occhio-di-formica-altezze-traccia-piano.svg")
print("ok")
