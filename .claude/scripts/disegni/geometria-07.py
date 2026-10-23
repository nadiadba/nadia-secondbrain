"""Schemi per la sbobina di geometria descrittiva del 22 ottobre (07-...): il ribaltamento
dei piani proiettanti.

Usa disegni_monge.py senza modificarlo. In piu' qui ci sono: archi di circonferenza
(come polilinee), lineette di uguaglianza sui segmenti e il controllo delle misure vere.

Lo stesso triangolo, dato con coordinate nel proprio piano (s = distanza lungo la traccia
dalla linea di terra, h = distanza dalla traccia-cerniera), viene messo nei vari piani:
cosi' tutte le figure ribaltate devono risultare uguali (lo verifica lo script).
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"

# il triangolo nel suo piano: (s, h)
TRI = {"A": (70, 45), "B": (250, 70), "C": (150, 165)}
NOMI = "ABC"


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def dist(a, b):
    return math.dist(a, b)


def lati(pts):
    """Lunghezze AB, BC, CA."""
    return [round(dist(pts[i], pts[(i + 1) % 3]), 3) for i in range(3)]


def lati_veri(tri=TRI):
    p = [tri[n] for n in NOMI]
    return lati(p)


def arco(f, c, r, a0, a1, colore="grigio", spessore=1, tratteggio="4,3", n=48):
    """Arco di circonferenza in coordinate di disegno, centro c, raggio r, da a0 a a1 (gradi)."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(f._s((c[0] + r * math.cos(a), c[1] + r * math.sin(a))))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    f.parti.append(f'<path d="{d}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                   f'stroke-width="{spessore}"{dash}/>')


def angolo(c, p):
    return math.degrees(math.atan2(p[1] - c[1], p[0] - c[0]))


def tacche(f, a, b, n, colore="nero", t=0.5):
    """n lineette di uguaglianza, a meta' del segmento ab."""
    L = dist(a, b)
    d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    q = (-d[1], d[0])
    m = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        c = lungo(m, d, o)
        f._linea(lungo(c, q, -5), lungo(c, q, 5), colore, 1.3)


def arco3d(t, c, e1, e2, r, a0, a1, colore="grigio", n=40):
    """Arco nello spazio: c + r (cos a e1 + sin a e2), disegnato nel triedro."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(t._p(tuple(c[j] + r * (math.cos(a) * e1[j] + math.sin(a) * e2[j]) for j in range(3))))
    dd = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    t.f.parti.append(f'<path d="{dd}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                     f'stroke-width="1.2" stroke-dasharray="5,3"/>')


def nota2(f, y, riga1, riga2):
    """Didascalia su due righe in fondo al disegno."""
    f.nota(20, y, riga1)
    f.nota(20, y + 17, riga2)


def controlla(nome, pts):
    vere = lati_veri()
    trovate = lati(pts)
    assert all(abs(x - y) < 1e-6 for x, y in zip(vere, trovate)), (nome, vere, trovate)
    print(f"{nome}: lati {trovate} = veri {vere}")


# =========================================================================================
# 1. Piano proiettante in prima: ribaltamento su pi1 intorno alla prima traccia
# =========================================================================================
TH = math.radians(30)
K = (40, 0)
d = (math.cos(TH), -math.sin(TH))            # direzione di t1alfa nel disegno
nr = (-math.sin(TH), -math.cos(TH))          # perpendicolare a t1alfa, dalla parte opposta alla LT
f = Figura(600, 490, 205, "Piano α proiettante in prima: ribaltamento su π₁ intorno a t₁α", x0=40)
f.lt(-20, 540)
fine1 = lungo(K, d, 360)
f.traccia(K, fine1); f.testo(fine1, "t_1α", 4, 14)
f.traccia(K, (K[0], 190)); f.testo((K[0], 190), "t_2α", 6, 4)
f.angolo_retto(K, (1, 0), (0, 1))
p1, p2, pr = {}, {}, {}
spazio = {}
for n_ in NOMI:
    s, h = TRI[n_]
    p1[n_] = lungo(K, d, s)
    p2[n_] = (p1[n_][0], h)
    pr[n_] = lungo(p1[n_], nr, h)
    # punto nello spazio (x, aggetto, quota) per il controllo
    spazio[n_] = (p1[n_][0], -p1[n_][1], h)
controlla("prima proiettante in prima, nello spazio", [spazio[n_] for n_ in NOMI])
controlla("ribaltato su pi1", [pr[n_] for n_ in NOMI])
f.figura([p2[n_] for n_ in NOMI], "blu")
f.figura([pr[n_] for n_ in NOMI], "rosso")
for i, n_ in enumerate(NOMI):
    f.richiamo(p1[n_][0], p2[n_][1], p1[n_][1])
    f.costruzione(p1[n_], pr[n_])
    a = angolo(p1[n_], pr[n_])
    arco(f, p1[n_], TRI[n_][1], a - 14, a + 14, "grigio", 1, None)
    tacche(f, (p2[n_][0], 0), p2[n_], i + 1)
    tacche(f, p1[n_], pr[n_], i + 1)
f.angolo_retto(p1["C"], d, nr)
et2 = {"A": (-24, -4), "B": (6, -6), "C": (6, -6)}
et1 = {"A": (6, -4), "B": (8, -4), "C": (8, -4)}
etr = {"A": (-28, 4), "B": (8, 10), "C": (-12, 18)}
for n_ in NOMI:
    f.punto(p2[n_], n_ + "₂", *et2[n_], "blu")
    f.punto(p1[n_], n_ + "₁", *et1[n_])
    f.punto(pr[n_], n_ + "*", *etr[n_], "rosso")
f.testo(p1["B"], "A₁B₁C₁ ≡ t₁α", 60, -20, "grigio", 12, False)
nota2(f, 462, "Ogni punto ribaltato sta sulla perpendicolare a t₁α, a una distanza", "uguale alla sua quota: le lineette indicano i segmenti uguali.")
f.salva(OUT + "07-ribaltamento-proiettante-in-prima-su-pi1.svg")

# =========================================================================================
# 2. Nello spazio: il piano proiettante in prima che si abbatte su pi1
# =========================================================================================
SC = 0.62          # il triangolo un po' piu' piccolo per stare nel triedro


def triedro(titolo, h=490, w=600):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, (262, 200), X3=400, U=360, Y=230, Z=220, scala=0.75)
    t.piani()
    return f, t


f, t = triedro("Nello spazio: il piano α ruota intorno a t₁α fino a coincidere con π₁")
th = math.radians(70)       # inclinazione scelta perche' si vedano bene sia il piano sia gli archi
K3 = (250, 0, 0)
u = (math.cos(th), math.sin(th), 0)
w = (-math.sin(th), math.cos(th), 0)
ez = (0, 0, 1)
n, dd = piano(K3, tuple(K3[j] + u[j] for j in range(3)), tuple(K3[j] + ez[j] for j in range(3)))
t.piano(n, dd, "blu", 0.14)
t.tracce(n, dd, "nero", "α")
P, Pr, Pp = {}, {}, {}
for n_ in NOMI:
    s, h = TRI[n_][0] * SC, TRI[n_][1] * SC
    base = tuple(K3[j] + s * u[j] for j in range(3))
    P[n_] = tuple(base[j] + h * ez[j] for j in range(3))
    Pr[n_] = tuple(base[j] + h * w[j] for j in range(3))
    Pp[n_] = base
    arco3d(t, base, ez, w, h, 0, 90, "rosso")
    t.richiamo(P[n_], base)
t._poligono([P[n_] for n_ in NOMI], "blu", 0.3, "blu")
t._poligono([Pr[n_] for n_ in NOMI], "rosso", 0.2, "rosso")
for n_ in NOMI:
    t.punto(P[n_], n_, 6, -4, "blu")
    t.punto(Pr[n_], n_ + "*", *({"A": (-30, 2)}.get(n_, (8, 14))), "rosso")
    t.punto(Pp[n_], None)
nota2(f, 462, "Ogni punto descrive un arco di circonferenza su un piano perpendicolare", "a t₁α, con centro sulla traccia; le prime proiezioni A₁ B₁ C₁ stanno su t₁α.")
f.salva(OUT + "07-spazio-ribaltamento-su-pi1.svg")

# =========================================================================================
# 3. La sezione: rotazione = proiezione perpendicolare al piano bisettore
# =========================================================================================
f = Figura(480, 300, 230, "Sezione perpendicolare a t₁α: la rotazione e il piano bisettore", x0=110)
O = (0, 0)
h = 150
f.retta((0, 0), (0, 200), "blu", 2.2); f.testo((0, 200), "α", 8, 12, "blu")
f.retta((-60, 0), (300, 0), "nero", 2.2); f.testo((300, 0), "π₁", -20, 20)
f.costruzione((-30, -30), (200, 200)); f.testo((200, 200), "piano bisettore", -150, 4, "grigio", 13, False)
A = (0, h); Ar = (h, 0)
arco(f, O, h, 90, 0, "rosso", 1.4, "5,4")
f.retta(A, Ar, "arancio", 1.4)
M = (h / 2, h / 2)
f.angolo_retto(M, (math.cos(math.radians(45)), math.sin(math.radians(45))),
               (math.cos(math.radians(-45)), math.sin(math.radians(-45))))
tacche(f, O, A, 1); tacche(f, O, Ar, 1)
f.punto(A, "A", 8, -2, "blu"); f.punto(Ar, "A*", -6, 22, "rosso")
f.punto(O, "t₁α ≡ A₁", -78, 22)
f.salva(OUT + "07-sezione-piano-bisettore.svg")

# =========================================================================================
# 4. Piano proiettante in prima: ribaltamento su pi2 intorno alla seconda traccia (la porta)
# =========================================================================================
f = Figura(660, 500, 200, "Piano α proiettante in prima: ribaltamento su π₂ intorno a t₂α", x0=20)
f.lt(0, 640)
K = (300, 0)
fine1 = lungo(K, d, 340)
f.traccia(K, fine1); f.testo(fine1, "t_1α", -30, 16)
f.traccia(K, (K[0], 190)); f.testo((K[0], 190), "t_2α", 6, 4)
f.angolo_retto(K, (1, 0), (0, 1))
p1, p2, pr = {}, {}, {}
for n_ in NOMI:
    s, h = TRI[n_]
    p1[n_] = lungo(K, d, s)
    p2[n_] = (p1[n_][0], h)
    pr[n_] = (K[0] - s, h)
controlla("ribaltato su pi2 (proiettante in prima)", [pr[n_] for n_ in NOMI])
f.figura([p2[n_] for n_ in NOMI], "blu")
f.figura([pr[n_] for n_ in NOMI], "rosso")
for n_ in NOMI:
    s, h = TRI[n_]
    f.richiamo(p1[n_][0], p2[n_][1], p1[n_][1])
    arco(f, K, s, angolo(K, p1[n_]), -180, "grigio", 1, "4,3")
    f.richiamo(pr[n_][0], 0, h)
    f.costruzione(pr[n_], p2[n_])
et2 = {"A": (4, 18), "B": (6, -6), "C": (6, -6)}
et1 = {"A": (10, -2), "B": (10, -2), "C": (10, -2)}
etr = {"A": (4, 18), "B": (-28, -6), "C": (-12, -8)}
for n_ in NOMI:
    f.punto(p2[n_], n_ + "₂", *et2[n_], "blu")
    f.punto(p1[n_], n_ + "₁", *et1[n_])
    f.punto(pr[n_], n_ + "*", *etr[n_], "rosso")
nota2(f, 470, "Centro dei compassi in K, dove t₂α incontra la LT. La quota non cambia:", "A* sta alla stessa altezza di A₂ (come la maniglia della porta).")
f.testo(K, "K", -18, 16)
f.salva(OUT + "07-ribaltamento-proiettante-in-prima-su-pi2.svg")

# =========================================================================================
# 5. Nello spazio: la porta che si chiude su pi2
# =========================================================================================
f, t = triedro("Nello spazio: il piano α si chiude su π₂ come una porta, con cerniera su t₂α")
th = math.radians(55)
K3 = (240, 0, 0)
u = (math.cos(th), math.sin(th), 0)
n, dd = piano(K3, tuple(K3[j] + u[j] for j in range(3)), (K3[0], 0, 1))
t.piano(n, dd, "blu", 0.14)
t.tracce(n, dd, "nero", "α")
P, Pr = {}, {}
for n_ in NOMI:
    s, h = TRI[n_][0] * SC, TRI[n_][1] * SC
    P[n_] = (K3[0] + s * u[0], s * u[1], h)
    Pr[n_] = (K3[0] - s, 0, h)
    arco3d(t, (K3[0], 0, h), (1, 0, 0), (0, 1, 0), s, math.degrees(th), 180, "rosso")
t._poligono([P[n_] for n_ in NOMI], "blu", 0.3, "blu")
t._poligono([Pr[n_] for n_ in NOMI], "rosso", 0.2, "rosso")
for n_ in NOMI:
    t.punto(P[n_], n_, 6, -4, "blu")
    t.punto(Pr[n_], n_ + "*", -22, -6, "rosso")
nota2(f, 462, "Gli archi sono orizzontali, con centro su t₂α: come la maniglia della porta,", "ogni punto resta alla sua quota. La figura è portata dalla parte opposta a quella di partenza.")
f.salva(OUT + "07-spazio-ribaltamento-su-pi2.svg")

# =========================================================================================
# 6. Piano proiettante in seconda: ribaltamento su pi1 intorno alla prima traccia
# =========================================================================================
PH = math.radians(50)
e = (math.cos(PH), math.sin(PH))
f = Figura(560, 520, 255, "Piano α proiettante in seconda: ribaltamento su π₁ intorno a t₁α", x0=40)
f.lt(-20, 500)
K = (40, 0)
fine2 = lungo(K, e, 330)
f.traccia(K, fine2); f.testo(fine2, "t_2α", 6, 6)
f.traccia(K, (K[0], -190)); f.testo((K[0], -190), "t_1α", 6, 4)
f.angolo_retto(K, (1, 0), (0, -1))
p1, p2, pr = {}, {}, {}
spazio = {}
for n_ in NOMI:
    s, y = TRI[n_]
    p2[n_] = lungo(K, e, s)
    p1[n_] = (p2[n_][0], -y)
    pr[n_] = (K[0] + s, -y)
    spazio[n_] = (p2[n_][0], y, p2[n_][1])
controlla("proiettante in seconda, nello spazio", [spazio[n_] for n_ in NOMI])
controlla("ribaltato su pi1 (proiettante in seconda)", [pr[n_] for n_ in NOMI])
f.figura([p1[n_] for n_ in NOMI], "blu")
f.figura([pr[n_] for n_ in NOMI], "rosso")
for n_ in NOMI:
    s, y = TRI[n_]
    f.richiamo(p2[n_][0], p2[n_][1], p1[n_][1])
    arco(f, K, s, math.degrees(PH), 0, "grigio", 1, "4,3")
    f.richiamo(pr[n_][0], 0, -y)
    f.costruzione(p1[n_], pr[n_])
et2 = {"A": (-26, -2), "B": (-26, -2), "C": (-26, -2)}
et1 = {"A": (-24, 16), "B": (-26, 16), "C": (-26, 16)}
etr = {"A": (6, -6), "B": (6, 16), "C": (6, 16)}
et1["B"] = (8, 18)
for n_ in NOMI:
    f.punto(p2[n_], n_ + "₂", *et2[n_])
    f.punto(p1[n_], n_ + "₁", *et1[n_], "blu")
    f.punto(pr[n_], n_ + "*", *etr[n_], "rosso")
f.testo(K, "K", -16, 16)
nota2(f, 482, "Centro dei compassi in K, dove t₁α incontra la LT. L'aggetto non cambia:", "A* sta alla stessa distanza dalla LT di A₁.")
f.salva(OUT + "07-ribaltamento-proiettante-in-seconda-su-pi1.svg")

# =========================================================================================
# 7. Piano proiettante in seconda: ribaltamento su pi2 intorno alla seconda traccia
# =========================================================================================
f = Figura(560, 530, 270, "Piano α proiettante in seconda: ribaltamento su π₂ intorno a t₂α", x0=110)
f.lt(-90, 430)
K = (40, 0)
nq = (-math.sin(PH), math.cos(PH))           # perpendicolare a t2alfa, dalla parte opposta alla LT
fine2 = lungo(K, e, 330)
f.traccia(K, fine2); f.testo(fine2, "t_2α", 6, 6)
f.traccia(K, (K[0], -190)); f.testo((K[0], -190), "t_1α", 6, 4)
f.angolo_retto(K, (1, 0), (0, -1))
p1, p2, pr = {}, {}, {}
for n_ in NOMI:
    s, y = TRI[n_]
    p2[n_] = lungo(K, e, s)
    p1[n_] = (p2[n_][0], -y)
    pr[n_] = lungo(p2[n_], nq, y)
controlla("ribaltato su pi2 (proiettante in seconda)", [pr[n_] for n_ in NOMI])
f.figura([p1[n_] for n_ in NOMI], "blu")
f.figura([pr[n_] for n_ in NOMI], "rosso")
for i, n_ in enumerate(NOMI):
    s, y = TRI[n_]
    f.richiamo(p2[n_][0], p2[n_][1], p1[n_][1])
    f.costruzione(p2[n_], pr[n_])
    a = angolo(p2[n_], pr[n_])
    arco(f, p2[n_], y, a - 14, a + 14, "grigio", 1, None)
    tacche(f, (p1[n_][0], 0), p1[n_], i + 1)
    tacche(f, p2[n_], pr[n_], i + 1)
f.angolo_retto(p2["C"], e, nq)
et2 = {"A": (8, 12), "B": (8, 12), "C": (8, 14)}
et1 = {"A": (-26, 14), "B": (6, 14), "C": (10, 4)}
etr = {"A": (-28, -4), "B": (6, -8), "C": (-30, -6)}
for n_ in NOMI:
    f.punto(p2[n_], n_ + "₂", *et2[n_])
    f.punto(p1[n_], n_ + "₁", *et1[n_], "blu")
    f.punto(pr[n_], n_ + "*", *etr[n_], "rosso")
nota2(f, 492, "Ogni punto ribaltato sta sulla perpendicolare a t₂α, a una distanza", "uguale al suo aggetto: le lineette indicano i segmenti uguali.")
f.salva(OUT + "07-ribaltamento-proiettante-in-seconda-su-pi2.svg")
print("ok")
