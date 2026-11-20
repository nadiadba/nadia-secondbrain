"""Schemi per le sbobine di geometria descrittiva del 17 e del 19 novembre (13-..., 14-...): la prospettiva.

Convenzioni dei disegni (come a lezione):
- l'orizzonte e' orizzontale, a quota 0 nel disegno; la fondamentale sta sotto, alla distanza h
  (l'altezza dell'occhio); O0 e' il punto principale sull'orizzonte;
- il punto di vista O, guardato dall'alto (in pianta), sta a distanza d dal quadro: se la traccia del
  quadro in pianta coincide con l'orizzonte, O cade proprio dove sta O* (il punto di vista ribaltato
  sul quadro intorno all'orizzonte, sul cerchio di distanza);
- un punto del geometrale ha coordinate (X, Y): X lungo il quadro, Y = profondita' oltre il quadro.
  La sua prospettiva e' (X d/(d+Y), -h d/(d+Y)): ogni costruzione viene controllata con questi conti.

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


def prosp(X, Y, d, h, z=0.0):
    """Prospettiva del punto (X, Y) a quota z: l'occhio e' a quota h."""
    k = d / (d + Y)
    return (X * k, (z - h) * k)


def vicino(p, q, tol=0.01):
    return math.dist(p, q) < tol


# =====================================================================
# 13a. Il metodo con la pianta: A e B sul quadro, la retta r perpendicolare al quadro, il punto C
# =====================================================================
d, h = 200, 70
A, B, C, D = (-40, 0), (60, 0), (60, 100), (-40, 100)   # pianta: il quadrato ABCD, AB appoggiato al quadro
O = (0, -d)                                              # O in pianta, coincide con O*

f = Figura(760, 420, 160, "Il metodo con la pianta: A, B sul quadro, la retta r e il punto C", x0=300)
# orizzonte = traccia del quadro in pianta
f._linea((-290, 0), (440, 0), "nero", 1.6)
f.testo((440, 0), "orizzonte = quadro in pianta", dx=-170, dy=-8, dimensione=13, corsivo=False)
f._linea((-290, -h), (440, -h), "nero", 1.6)
f.testo((-290, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
# cerchio di distanza
arco(f, (0, 0), d, 180, 360, tratteggio="2,4")
f.punto((0, 0), "O_0", dx=-8, dy=18)
f.punto(O, "O ≡ O*", dx=8, dy=4)
f.testo((-170, -150), "cerchio di distanza", dimensione=12, colore="grigio", corsivo=False)
# pianta
f.figura([A, B, C, D], "blu")
for p, n, dx, dy in [(A, "A", -14, -6), (B, "B", 4, -6), (C, "C", 6, -4), (D, "D", -16, -4)]:
    f.punto(p, n, dx, dy, "blu")
f.testo((60, 50), "r", dx=6, dy=4, colore="blu")
# A e B stanno gia' sul quadro: si scende in verticale fino alla fondamentale
Ap, Bp = prosp(*A, d, h), prosp(*B, d, h)
assert vicino(Ap, (-40, -h)) and vicino(Bp, (60, -h))
f.richiamo(-40, 0, -h)
f.richiamo(60, 0, -h)
# raggio proiettante da O per C, incontra il quadro in pianta in K
K = interseca(O, C, (-1, 0), (1, 0))
f.costruzione(O, C)
f.punto(K, None)
f._linea(K, (K[0], -h + 10), "rosso", 1.2, "5,3")
Cp = prosp(*C, d, h)
# r' va da B' (traccia) a O0 (fuga)
f.retta(Bp, (0, 0), "rosso", 2)
assert abs(Cp[0] - K[0]) < 1e-9
assert vicino(interseca(Bp, (0, 0), K, (K[0], -h)), Cp)
f.punto(Ap, "A′", -14, 16, "rosso")
f.punto(Bp, "B′ ≡ T_r′", 6, 16, "rosso")
f.punto(Cp, "C′", 8, 10, "rosso")
f.testo((45, -30), "r′", dx=6, colore="rosso")
f.nota(470, 360, "r è perpendicolare al quadro:", 13)
f.nota(470, 378, "la sua fuga è O₀ (punto principale)", 13)
f.salva(OUT + "13-prospettiva-metodo-pianta-retta-perpendicolare.svg")


# =====================================================================
# 13b. La retta a 45 gradi: la fuga e' il punto di distanza; la diagonale passa per C'
# =====================================================================
f = Figura(760, 470, 160, "La retta a 45°: la fuga è il punto di distanza", x0=300)
f._linea((-290, 0), (440, 0), "nero", 1.6)
f.testo((440, 0), "orizzonte = quadro in pianta", dx=-170, dy=-8, dimensione=13, corsivo=False)
f._linea((-290, -h), (440, -h), "nero", 1.6)
f.testo((-290, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
arco(f, (0, 0), d, 180, 360, tratteggio="2,4")
f.punto((0, 0), "O_0", dx=-8, dy=18)
f.punto(O, "O ≡ O*", dx=8, dy=4)
Dd, Ds = (d, 0), (-d, 0)
f.punto(Dd, "D_d", dx=4, dy=-8)
f.punto(Ds, "D_s", dx=-22, dy=-8)
f.figura([A, B, C, D], "blu")
for p, n, dx, dy in [(A, "A", -14, -6), (B, "B", 4, -6), (C, "C", 6, -4), (D, "D", -16, -4)]:
    f.punto(p, n, dx, dy, "blu")
# la diagonale AC e' a 45 gradi: la sua parallela per O arriva sull'orizzonte in D_d
f._linea(A, C, "blu", 1.8)
f.testo((10, 50), "s", dx=-14, dy=0, colore="blu")
f.costruzione(O, Dd)
Ap = prosp(*A, d, h)
Cp = prosp(*C, d, h)
# s' va da A' (traccia: A sta sul quadro) a D_d (fuga)
assert vicino(interseca(Ap, Dd, Cp, (Cp[0], 0)), Cp)
f.retta(Ap, Dd, "rosso", 2)
# richiamiamo anche r' per far vedere che s' passa per C'
Bp = prosp(*B, d, h)
f.retta(Bp, (0, 0), "arancio", 1.4)
f.richiamo(-40, 0, -h)
f.punto(Ap, "A′ ≡ T_s′", -20, 18, "rosso")
f.punto(Bp, "B′", 6, 16, "arancio")
f.punto(Cp, "C′", -4, 18, "rosso")
f.testo((120, -30), "s′", colore="rosso")
f.testo((30, -40), "r′", colore="arancio")
f.nota(20, 440, "La parallela a s per O forma 45° con il quadro e incontra l'orizzonte nel punto di distanza a destra:", 13)
f.nota(20, 458, "s′ va dalla traccia A′ a questo punto e, se il disegno è giusto, passa per C′ trovato prima.", 13)
f.salva(OUT + "13-prospettiva-retta-a-45-punto-di-distanza.svg")


# =====================================================================
# 14a. Le altezze: lo schema laterale e lo spigolo portato in prospettiva
# =====================================================================
H = 60                      # altezza del prisma sul quadrato ABCD
f = Figura(820, 300, 200, "Le altezze: lo schema laterale e lo spigolo in prospettiva", x0=0)
# --- a sinistra: lo schema laterale (profondita' verso destra, quota verso l'alto), base a y=0
sx = 20                     # posizione dell'occhio nello schema
q = sx + d                  # il quadro, visto di lato, e' una verticale
f._linea((sx - 10, 0), (q + 140, 0), "nero", 1.4)
f.testo((sx - 10, 0), "geometrale", dx=0, dy=16, dimensione=12, corsivo=False)
f._linea((q, -10), (q, 170), "nero", 1.6)
f.testo((q, 170), "quadro", dx=-24, dy=-6, dimensione=12, corsivo=False)
eye = (sx, h)
f._linea((sx, 0), eye, "grigio", 3)          # l'omino
f.punto(eye, "O", dx=-14, dy=-6)
f.figura([(q, 0), (q + 100, 0), (q + 100, H), (q, H)], "blu")
f.testo((q + 100, 0), "C", dx=4, dy=16, colore="blu")
f.testo((q, 0), "B", dx=4, dy=16, colore="blu")
top = (q + 100, H)
zq = h + (H - h) * d / (d + 100)              # dove il raggio verso lo spigolo superiore buca il quadro
zb = h - h * d / (d + 100)                    # e verso lo spigolo di base
f.costruzione(eye, top)
f.costruzione(eye, (q + 100, 0))
f._linea((q, zb), (q, zq), "rosso", 3)
f.testo((q, (zq + zb) / 2), "altezza sul quadro", dx=8, dy=-50, dimensione=12, colore="rosso", corsivo=False)
f.punto((q, zq), None, colore="rosso")
f.punto((q, zb), None, colore="rosso")
# --- a destra: la prospettiva (orizzonte a y = h sopra la base dello schema, cosi' le quote si leggono uguali)
x0 = 600


def P(X, Y, z=0):
    """Prospettiva spostata: fondamentale a y = 0, orizzonte a y = h."""
    px, py = prosp(X, Y, d, h, z)
    return (x0 + px, py + h)


f._linea((x0 - 170, h), (x0 + 200, h), "nero", 1.4)
f.testo((x0 - 170, h), "orizzonte", dx=0, dy=-6, dimensione=12, corsivo=False)
f._linea((x0 - 170, 0), (x0 + 200, 0), "nero", 1.4)
f.testo((x0 - 170, 0), "fondamentale", dx=0, dy=16, dimensione=12, corsivo=False)
f.punto((x0, h), "O_0", dx=4, dy=-8)
Bb, Ct = P(*B), P(*C, H)
Cb = P(*C)
assert vicino(Cb, (Cb[0], h - h * d / (d + 100)))
assert abs((Ct[1] - 0) - zq) < 1e-9 and abs((Cb[1] - 0) - zb) < 1e-9   # la quota letta sul quadro e' quella giusta
# base e spigoli
for a, b in [(P(*A), P(*B)), (P(*B), P(*C)), (P(*C), P(*D)), (P(*D), P(*A))]:
    f._linea(a, b, "blu", 1.2)
for a, b in [(P(*A), P(*A, H)), (P(*B), P(*B, H)), (P(*C), P(*C, H)), (P(*A, H), P(*B, H)),
             (P(*B, H), P(*C, H)), (P(*A, H), P(*D, H)), (P(*C, H), P(*D, H))]:
    f._linea(a, b, "rosso", 1.8)
f._linea(P(*D), P(*D, H), "rosso", 1.2, "4,3")
# la quota del quadro portata in orizzontale sullo spigolo per C'
f._linea((x0 + 150, zb), (x0 + 150, zq), "rosso", 3)
f.costruzione((x0 + 150, zq), Ct)
f.costruzione((x0 + 150, zb), Cb)
f.punto(Ct, None, colore="rosso")
f.punto(Cb, "C′", dx=-24, dy=4, colore="rosso")
f.punto(Bb, "B′", dx=4, dy=16, colore="rosso")
f.testo(P(*B, H), "H vera", dx=8, dy=30, dimensione=12, colore="rosso", corsivo=False)
f.nota(20, 270, "Lo spigolo per B sta sul quadro: la sua altezza è vera. Per lo spigolo per C si legge sullo schema laterale", 13)
f.nota(20, 288, "il tratto rosso sul quadro, dalla fondamentale in su, e lo si porta in orizzontale sulla verticale di C′.", 13)
f.salva(OUT + "14-prospettiva-altezze-schema-laterale.svg")


# =====================================================================
# 14b. Senza pianta: il punto di misura M_r e la retta s perpendicolare a r
# =====================================================================
d, h = 170, 90
th = math.radians(55)
Fr = (d / math.tan(th), 0)
Fs = (d / math.tan(th + math.pi / 2), 0)
Os = (0, -d)
Mr = (Fr[0] - d / math.sin(th), 0)
assert abs(math.dist(Fr, Os) - (Fr[0] - Mr[0])) < 1e-9
T = (-60, 0)                     # traccia di r sul geometrale (in pianta, sul quadro)
tA, tAB = 40, 80
dirr = (math.cos(th), math.sin(th))
Apl = (T[0] + tA * dirr[0], tA * dirr[1])
Bpl = (T[0] + (tA + tAB) * dirr[0], (tA + tAB) * dirr[1])
Ap, Bp, Tp = prosp(*Apl, d, h), prosp(*Bpl, d, h), prosp(*T, d, h)
QA, QB = (T[0] + tA, -h), (T[0] + tA + tAB, -h)
# verifica: proiettando da M_r i punti della fondamentale si trovano proprio A' e B'
assert vicino(interseca(Tp, Fr, QA, Mr), Ap) and vicino(interseca(Tp, Fr, QB, Mr), Bp)
# s perpendicolare a r in B: la fuga F_s si legge in O* a 90 gradi da O*F_r
v1 = (Fr[0] - Os[0], Fr[1] - Os[1])
v2 = (Fs[0] - Os[0], Fs[1] - Os[1])
assert abs(v1[0] * v2[0] + v1[1] * v2[1]) < 1e-6

f = Figura(820, 230, 30, "Senza pianta: il punto di misura Mᵣ e la retta s perpendicolare a r", x0=440)
f._linea((-430, 0), (360, 0), "nero", 1.6)
f.testo((-430, 0), "orizzonte", dx=2, dy=-8, dimensione=13, corsivo=False)
f._linea((-430, -h), (360, -h), "nero", 1.6)
f.testo((-430, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
f.punto((0, 0), "O_0", dx=-10, dy=-10)
f.richiamo(0, 0, -d)
f.punto(Os, "O*", dx=8, dy=6)
# punto di misura: arco di centro F_r per O*
a0 = math.degrees(math.atan2(Os[1] - Fr[1], Os[0] - Fr[0]))
arco(f, Fr, Fr[0] - Mr[0], 180, 360 + a0 if a0 < 0 else a0)
f.costruzione(Os, Fr)
f.costruzione(Os, Fs)
f.angolo_retto(Os, (v1[0] / math.hypot(*v1), v1[1] / math.hypot(*v1)),
               (v2[0] / math.hypot(*v2), v2[1] / math.hypot(*v2)), 12)
f.punto(Fr, "F_r", dx=4, dy=-8)
f.punto(Fs, "F_s", dx=-8, dy=-10)
f.punto(Mr, "M_r", dx=-10, dy=-10, colore="verde")
# r' e la misura
f.retta(Tp, Fr, "rosso", 2)
f.costruzione(Mr, QA)
f.costruzione(Mr, QB)
f._linea(QA, QB, "verde", 3)
f.punto(QA, "A₀", dx=-6, dy=18, colore="verde")
f.punto(QB, "B₀", dx=-6, dy=18, colore="verde")
f.testo(((QA[0] + QB[0]) / 2, -h), "AB vera", dx=-22, dy=34, dimensione=12, colore="verde", corsivo=False)
f.punto(Tp, "T_r′", dx=-26, dy=18, colore="rosso")
f.punto(Ap, "A′", dx=-20, dy=-4, colore="rosso")
f.punto(Bp, "B′", dx=-4, dy=-10, colore="rosso")
f.retta(Bp, Fs, "blu", 2)
f.testo(((Bp[0] + Fs[0]) / 2, (Bp[1] + Fs[1]) / 2), "s′", dx=-4, dy=-8, colore="blu")
f.testo(((Tp[0] + Fr[0]) / 2, (Tp[1] + Fr[1]) / 2), "r′", dx=4, dy=14, colore="rosso")
f.salva(OUT + "14-prospettiva-punto-di-misura-e-angolo-retto.svg")
print("ok")
