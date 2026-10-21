"""Schemi per la sbobina di geometria descrittiva del 13 ottobre (04): rette e piani nel metodo di Monge.

Per la terza proiezione: il terzo piano π3 e' a destra, la sua intersezione con π2 e' la verticale x = X3.
Un punto (x, y, z) ha la terza proiezione in (X3 + y, z): il primo piano si ribalta con archi di
richiamo centrati nel punto (X3, 0).
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import (Figura, P1, P2, tracce_retta, piano, interseca, direzione, COLORI)

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def P3(p, X3):
    """Terza proiezione di un punto 3D (terzo piano ribaltato a destra)."""
    return (X3 + p[1], p[2])


def asse_terzo(f, X3, y1, y2):
    """Verticale π2/π3 (e π1/π3 sotto la LT)."""
    f._linea((X3, y1), (X3, y2), "nero", 1.2)


def arco(f, X3, y, colore="grigio"):
    """Arco di richiamo: dal punto (X3, -y) del primo piano al punto (X3 + y, 0) del terzo."""
    pts = []
    for i in range(25):
        t = math.pi / 2 * i / 24
        pts.append(f._s((X3 + y * math.sin(t), -y * math.cos(t))))
    d = "M " + " L ".join(f"{x:.1f},{yy:.1f}" for x, yy in pts)
    f.parti.append(f'<path d="{d}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                   f'stroke-width="0.9" stroke-dasharray="3,3"/>')


def tratteggiata(f, a, b, colore="rosso", spessore=1.6):
    f._linea(a, b, colore, spessore, "6,4")


def orizz(f, x, y1, y2):
    """Richiamo orizzontale (verso il terzo piano)."""
    f._linea((y1, x), (y2, x), "grigio", 0.9, "3,3")


def pannello(f, ox):
    """Restituisce una figura che disegna nelle stesse parti di f, spostata di ox."""
    g = Figura(0, 0, f.y_lt, x0=ox)
    g.parti = f.parti
    return g


# 1. Piani che contengono una retta proiettante in seconda --------------------------
f = Figura(690, 300, 150, "Retta r proiettante in seconda: i piani che la contengono")
titoli = ["piano proiettante in seconda β", "piano orizzontale γ", "piano di profilo δ"]
for i, tit in enumerate(titoli):
    ox = 15 + 230 * i
    f.nota(ox, 18, tit, 13)
    g = pannello(f, ox)
    g.lt(0, 205, etichetta=(i == 0))
    xr, zr = 110, 70
    # r'' e' un punto (≡ T2r), r' e' perpendicolare alla LT
    g.retta((xr, 0), (xr, -120), "rosso")
    if i != 2:
        g.testo((xr, -120), "r₁", 6, 6, "rosso")
    g.testo((xr, -120), "T_{1r}∞", -46, 6, "rosso")
    g.richiamo(xr, zr, 0)
    if i == 0:
        K = (60, 0)
        dt = direzione(K, (xr, zr))
        g.traccia(K, lungo(K, dt, 110)); g.testo(lungo(K, dt, 110), "t_2β", 4, 4)
        g.traccia(K, (60, -120)); g.testo((60, -120), "t_1β", -30, 6)
        g.angolo_retto(K, (1, 0), (0, -1))
    elif i == 1:
        g.traccia((10, zr), (200, zr)); g.testo((200, zr), "t_2γ", -28, -8)
        g.testo((150, -95), "t_1γ∞", 0, 0)
    else:
        g.traccia((xr, 0), (xr, 110)); g.testo((xr, 110), "t_2δ", 6, 4)
        g.traccia((xr, 0), (xr, -120), "nero")
        g.retta((xr, 0), (xr, -120), "rosso", 1.4)
        g.testo((xr, -60), "t_1δ ≡ r₁", 8, 4)
    g.punto((xr, zr), "r₂ ≡ T_{2r}", 10, 18 if i != 2 else -8, "rosso")
f.salva(OUT + "04-piani-per-retta-proiettante-in-seconda.svg")

# 2. Piani che contengono una retta parallela alla LT (con la terza proiezione) -------
f = Figura(690, 330, 160, "Retta r parallela alla LT: i piani che la contengono")
y_r, z_r = 40, 50
for i, tit in enumerate(["piano α parallelo alla linea di terra", "piano frontale φ"]):
    ox = 15 + 345 * i
    f.nota(ox, 18, tit, 13)
    g = pannello(f, ox)
    X3 = 200
    g.lt(0, 320, etichetta=(i == 0))
    asse_terzo(g, X3, 140, -140)
    g.testo((X3, 140), "π_3", 6, 10, "grigio", 12, False)
    g.testo((0, 140), "π_2", 2, 10, "grigio", 12, False)
    g.testo((0, -140), "π_1", 2, 0, "grigio", 12, False)
    g.retta((15, z_r), (X3, z_r), "rosso"); g.testo((15, z_r), "r₂", 0, -8, "rosso")
    g.retta((15, -y_r), (X3, -y_r), "rosso"); g.testo((15, -y_r), "r₁", 0, 16, "rosso")
    arco(g, X3, y_r)
    T3 = (X3 + y_r, z_r)
    g.richiamo(X3 + y_r, 0, z_r)
    if i == 0:
        z2, y1 = 100, 80
        g.traccia((5, z2), (X3, z2)); g.testo((5, z2), "t_2α", 0, -8)
        g.traccia((5, -y1), (X3, -y1)); g.testo((5, -y1), "t_1α", 0, 18)
        arco(g, X3, y1)
        g.traccia((X3, z2), (X3 + y1, 0)); g.testo((X3 + y1, 0), "t_3α", 6, 16)
    else:
        g.traccia((5, -y_r), (X3, -y_r)); g.testo((95, -y_r), "t_1φ ≡ r₁", 0, 18)
        g.testo((60, 120), "t_2φ∞", 0, 0)
        g.traccia((X3 + y_r, 0), (X3 + y_r, 130)); g.testo((X3 + y_r, 130), "t_3φ", 6, 4)
    g.punto(T3, "r₃ ≡ T_{3r}", 8, -6, "rosso")
f.salva(OUT + "04-piani-per-retta-parallela-alla-lt.svg")

# Retta generica usata negli schemi 3, 4 e 5
T1 = (100, 60, 0)
T2 = (200, 0, 40)

# 3. Retta generica: dalle tracce alle proiezioni -------------------------------------
f = Figura(520, 240, 120, "Retta generica r: le proiezioni passano per le tracce", x0=30)
f.lt(-10, 400)
d2 = direzione(P2(T1), P2(T2)); d1 = direzione(P1(T1), P1(T2))
f.retta(lungo(P2(T1), d2, -40), lungo(P2(T2), d2, 50), "rosso"); f.testo(lungo(P2(T2), d2, 50), "r₂", 6, 0, "rosso")
f.retta(lungo(P1(T1), d1, -40), lungo(P1(T2), d1, 60), "rosso"); f.testo(lungo(P1(T2), d1, 60), "r₁", 6, 0, "rosso")
f.richiamo(T1[0], 0, -T1[1]); f.richiamo(T2[0], T2[2], 0)
f.punto(P1(T1), "T_{1r} ≡ T_{1r}", -96, 14)
f.punto(P2(T1), "(T_{1r})₂", -50, -8)
f.punto(P2(T2), "T_{2r} ≡ T_{2r}", -112, -4)
f.punto(P1(T2), "(T_{2r})₁", 8, 18)
f.salva(OUT + "04-retta-generica-proiezioni.svg")

# 4. Retta generica: terza proiezione e terza traccia ---------------------------------
X3 = 330
t3 = (X3 - T1[0]) / (T2[0] - T1[0])
T3 = tuple(T1[i] + (T2[i] - T1[i]) * t3 for i in range(3))       # y negativo: dietro π2
f = Figura(600, 270, 150, "Retta generica r: la terza proiezione e la terza traccia T₃ᵣ", x0=40)
f.lt(-20, 520)
asse_terzo(f, X3, 140, -110)
f.testo((X3, 140), "π_3", 6, 10, "grigio", 12, False)
f.testo((-20, 140), "π_2", 2, 10, "grigio", 12, False)
f.testo((-20, -110), "π_1", 2, 0, "grigio", 12, False)
# piano ausiliario α proiettante in prima: t1α ≡ r', t2α verticale per T2r'
f.traccia((T2[0], 0), (T2[0], 130)); f.testo((T2[0], 130), "t_2α", -32, 4)
f.traccia((P3(T3, X3)[0], 0), (P3(T3, X3)[0], 130)); f.testo((P3(T3, X3)[0], 130), "t_3α", 6, 4)
# r'' e r'
f.retta(lungo(P2(T1), d2, -30), P2(T2), "rosso"); tratteggiata(f, P2(T2), P2(T3))
f.testo(P2(T2), "r₂", -60, -26, "rosso")
f.retta(lungo(P1(T1), d1, -30), P1(T2), "rosso"); tratteggiata(f, P1(T2), P1(T3))
f.testo(lungo(P1(T1), d1, -30), "r₁ ≡ t_1α", -64, 14, "rosso")
f.richiamo(T1[0], 0, -T1[1]); f.richiamo(T2[0], T2[2], 0)
# terza proiezione: T1 e T2 portati sul terzo piano
arco(f, X3, T1[1])
orizz(f, T2[2], T2[0], X3)
f.retta(P3(T1, X3), P3(T2, X3), "rosso"); tratteggiata(f, P3(T2, X3), P3(T3, X3))
f.testo(P3(T1, X3), "r₃", 6, -6, "rosso")
f.punto(P3(T1, X3), "(T_{1r})₃", 4, 18); f.punto(P3(T2, X3), "(T_{2r})₃", 6, 4)
# terza traccia: dal ribaltamento di t1α e dalla seconda proiezione
arco(f, X3, T3[1])
orizz(f, T3[2], P2(T3)[0], P3(T3, X3)[0])
f.punto(P2(T3), "(T_{3r})₂", 6, -4)
f.punto(P1(T3), "(T_{3r})₁", 6, 14)
f.punto(P3(T3, X3), "T_{3r}", -40, -6, "rosso")
f.punto(P1(T1), "T_{1r}", 8, 14); f.punto(P2(T1), "(T_{1r})₂", -18, -10)
f.punto(P2(T2), "T_{2r}", -50, -4); f.punto(P1(T2), "(T_{2r})₁", 6, 18)
f.salva(OUT + "04-retta-generica-terza-traccia.svg")

# 5. Retta generica nei due piani proiettanti ----------------------------------------
f = Figura(690, 320, 150, "Retta generica r nei piani ausiliari: proiettante in prima α e in seconda β")
for i, tit in enumerate(["piano α proiettante in prima", "piano β proiettante in seconda"]):
    ox = 20 + 345 * i
    f.nota(ox, 18, tit, 13)
    g = pannello(f, ox)
    g.lt(0, 320, etichetta=(i == 0))
    a1, a2 = (90, -90), (90, 0)
    b2, b1 = (200, 90), (200, 0)
    e2 = direzione(a2, b2); e1 = direzione(a1, b1)
    g.richiamo(90, 0, -90); g.richiamo(200, 90, 0)
    if i == 0:
        g.traccia(lungo(a1, e1, -40), lungo(b1, e1, 70)); g.testo(lungo(b1, e1, 70), "t_1α ≡ r₁", -10, -10)
        g.retta(lungo(a1, e1, -40), lungo(b1, e1, 70), "rosso", 1.4)
        g.traccia(b1, (200, 115)); g.testo((200, 115), "t_2α", 6, 4)
        g.retta(lungo(a2, e2, -20), lungo(b2, e2, 30), "rosso"); g.testo(lungo(b2, e2, 30), "r₂", 6, 10, "rosso")
    else:
        g.traccia(lungo(a2, e2, -40), lungo(b2, e2, 30)); g.testo(lungo(b2, e2, 30), "t_2β ≡ r₂", 6, 4)
        g.retta(lungo(a2, e2, -40), lungo(b2, e2, 30), "rosso", 1.4)
        g.traccia(a2, (90, -135)); g.testo((90, -135), "t_1β", 6, 4)
        g.retta(lungo(a1, e1, -20), lungo(b1, e1, 40), "rosso"); g.testo(lungo(b1, e1, 40), "r₁", 6, 4, "rosso")
    g.punto(a1, "T_{1r}", -40, 8); g.punto(a2, "(T_{1r})₂", -46, -8)
    g.punto(b2, "T_{2r}", -52, -2); g.punto(b1, "(T_{2r})₁", 8, 16)
f.salva(OUT + "04-retta-generica-piani-proiettanti.svg")

# Piano generico α usato negli schemi 6 e 7
K = (60, 0, 0)
A = (300, 0, 90)      # su t2α
B = (300, 110, 0)     # su t1α
n, dd = piano(K, A, B)
X3 = 420
z0 = (dd - n[0] * X3) / n[2]       # dove t2α incontra la verticale π2/π3
y0 = (dd - n[0] * X3) / n[1]       # dove t1α incontra la verticale π1/π3


def piano_generico(f):
    asse_terzo(f, X3, 175, -185)
    f.testo((X3, 175), "π_3", 6, 10, "grigio", 12, False)
    f.traccia((K[0], 0), (X3, z0)); f.testo(((K[0] + X3) / 2, z0 / 2), "t_2α", -10, -12)
    f.traccia((K[0], 0), (X3, -y0)); f.testo(((K[0] + X3) / 2, -y0 / 2), "t_1α", -24, 18)
    arco(f, X3, y0)
    f.traccia((X3, z0), (X3 + y0, 0)); f.testo((X3 + y0 * 0.8, z0 * 0.2), "t_3α", 8, 0)


def su_alfa_y(x, z):
    """Aggetto del punto di α con ascissa x e quota z."""
    return (dd - n[0] * x - n[2] * z) / n[1]


# 6. Piano generico: le tre tracce e un'orizzontale -----------------------------------
h = 55
xo = (dd - n[2] * h) / n[0]                # T2o: y = 0, z = h
f = Figura(640, 390, 195, "Piano generico α: le tre tracce e una retta orizzontale o del piano", x0=20)
f.lt(0, 600)
piano_generico(f)
yo3 = su_alfa_y(X3, h)
f.retta((xo, h), (X3, h), "arancio"); f.testo(((xo + X3) / 2, h), "o₂", 0, -8, "arancio")
f.retta((xo, 0), (X3, -yo3), "arancio"); f.testo(((xo + X3) / 2, -yo3 / 2), "o₁", 4, -8, "arancio")
f.testo((X3, -yo3), "T_{1o}∞", -60, 20, "arancio")
f.retta((X3, h), (X3 + yo3 + 70, h), "arancio", 1.4); f.testo((X3 + yo3 + 70, h), "o₃", -8, -8, "arancio")
f.richiamo(xo, h, 0)
arco(f, X3, yo3)
f.richiamo(X3 + yo3, 0, h)
f.punto((xo, h), "T_{2o}", -50, -8); f.punto((xo, 0), "(T_{2o})₁", -12, 18)
f.punto((X3, -yo3), "(T_{3o})₁", 6, 14)
f.punto((X3 + yo3, h), "T_{3o}", -8, 20)
f.salva(OUT + "04-piano-generico-orizzontale.svg")

# 7. Piano generico: una frontale ---------------------------------------------------
yf = 50
xf = (dd - n[1] * yf) / n[0]               # T1f: z = 0, y = yf
zf3 = (dd - n[0] * X3 - n[1] * yf) / n[2]
f = Figura(640, 390, 195, "Piano generico α: una retta frontale f del piano", x0=20)
f.lt(0, 600)
piano_generico(f)
f.retta((xf, -yf), (X3, -yf), "verde"); f.testo(((xf + X3) / 2, -yf), "f₁", 0, 16, "verde")
f.retta((xf, 0), (X3, zf3), "verde"); f.testo(((xf + X3) / 2, zf3 / 2), "f₂", -8, -10, "verde")
f.testo((X3, zf3), "T_{2f}∞", -58, 2, "verde")
f.retta((X3 + yf, 0), (X3 + yf, 150), "verde", 1.4); f.testo((X3 + yf, 150), "f₃", 6, 4, "verde")
f.richiamo(xf, 0, -yf)
arco(f, X3, yf)
orizz(f, zf3, X3, X3 + yf)
f.punto((xf, -yf), "T_{1f}", -18, 18); f.punto((xf, 0), "(T_{1f})₂", -18, -10)
f.punto((X3, zf3), "(T_{3f})₂", 6, -6)
f.punto((X3 + yf, zf3), "T_{3f}", 6, -6)
f.salva(OUT + "04-piano-generico-frontale.svg")

# 8. I piani che contengono un'orizzontale -----------------------------------------
f = Figura(690, 300, 140, "I piani che contengono una retta orizzontale o")
for i, tit in enumerate(["piano orizzontale α", "piano generico β", "piano proiettante in prima γ"]):
    ox = 15 + 230 * i
    f.nota(ox, 18, tit, 13)
    g = pannello(f, ox)
    g.lt(0, 205, etichetta=(i == 0))
    x0, h = 80, 70
    do = direzione((x0, 0), (180, -110))
    o1_fine = lungo((x0, 0), do, 140)
    g.richiamo(x0, h, 0)
    if i == 0:
        g.traccia((5, h), (200, h)); g.testo((200, h), "t_2α ≡ o₂", -64, -8)
        g.testo((10, -110), "t_1α∞", 0, 0)
    elif i == 1:
        Kb = (20, 0)
        g.traccia(Kb, lungo(Kb, direzione(Kb, (x0, h)), 115)); g.testo(lungo(Kb, direzione(Kb, (x0, h)), 115), "t_2β", 4, 4)
        g.traccia(Kb, lungo(Kb, do, 150)); g.testo(lungo(Kb, do, 150), "t_1β", -34, 4)
    else:
        g.traccia((x0, 0), (x0, 105)); g.testo((x0, 105), "t_2γ", 6, 4)
        g.traccia((x0, 0), o1_fine)
        g.testo(o1_fine, "t_1γ ≡ o₁", -80, 4)
    g.retta((x0, h), (200, h), "arancio")
    if i != 0:
        g.testo((200, h), "o₂", -14, -8, "arancio")
    g.retta((x0, 0), o1_fine, "arancio", 1.4)
    if i != 2:
        g.testo(o1_fine, "o₁", 6, 4, "arancio")
    g.punto((x0, h), "T_{2o}", -48, -8 if i != 0 else 18); g.punto((x0, 0), "(T_{2o})₁", *((-46, -8) if i == 1 else (-46, 16)))
f.salva(OUT + "04-piani-per-retta-orizzontale.svg")

# 9. I piani che contengono una frontale ---------------------------------------------
f = Figura(690, 300, 150, "I piani che contengono una retta frontale f")
for i, tit in enumerate(["piano frontale β", "piano generico α", "piano proiettante in seconda γ"]):
    ox = 15 + 230 * i
    f.nota(ox, 18, tit, 13)
    g = pannello(f, ox)
    g.lt(0, 205, etichetta=(i == 0))
    x0, yf = 80, 70
    df = direzione((x0, 0), (180, 110))
    f2_fine = lungo((x0, 0), df, 140)
    g.richiamo(x0, 0, -yf)
    if i == 0:
        g.traccia((5, -yf), (200, -yf)); g.testo((200, -yf), "t_1β ≡ f₁", -64, 18)
        g.testo((10, 110), "t_2β∞", 0, 0)
    elif i == 1:
        Kb = (20, 0)
        g.traccia(Kb, lungo(Kb, direzione(Kb, (x0, -yf)), 130)); g.testo(lungo(Kb, direzione(Kb, (x0, -yf)), 130), "t_1α", 4, 10)
        g.traccia(Kb, lungo(Kb, df, 140)); g.testo(lungo(Kb, df, 140), "t_2α", -34, 4)
    else:
        g.traccia((x0, 0), (x0, -125)); g.testo((x0, -125), "t_1γ", 6, 4)
        g.traccia((x0, 0), f2_fine)
        g.testo(f2_fine, "t_2γ ≡ f₂", -80, 0)
    g.retta((x0, -yf), (200, -yf), "verde"); g.testo((200, -yf), "f₁", -14, -8 if i == 0 else 18, "verde")
    g.retta((x0, 0), f2_fine, "verde", 1.4)
    if i != 2:
        g.testo(f2_fine, "f₂", 6, 4, "verde")
    g.punto((x0, -yf), "T_{1f}", -48, 16 if i != 0 else -8); g.punto((x0, 0), "(T_{1f})₂", *((6, 16) if i == 1 else (-48, -8)))
f.salva(OUT + "04-piani-per-retta-frontale.svg")

# 10. I piani che contengono una retta di profilo (con la terza proiezione) ------------
f = Figura(700, 330, 165, "Retta di profilo m: i piani che la contengono")
ym, zm = 60, 70
for i, tit in enumerate(["piano di profilo δ e piano ε parallelo alla LT", "piano generico α"]):
    ox = 15 + 350 * i
    f.nota(ox, 18, tit, 13)
    g = pannello(f, ox)
    X0, X3 = (90, 200) if i == 0 else (110, 170)
    g.lt(0, 320, etichetta=(i == 0))
    asse_terzo(g, X3, 130, -150)
    g.testo((X3, 130), "π_3", 6, 10, "grigio", 12, False)
    T1m, T2m = (X0, ym, 0), (X0, 0, zm)
    arco(g, X3, ym)
    orizz(g, zm, X0, X3)
    if i == 0:
        g.traccia((X0, 0), (X0, 120)); g.testo((X0, 120), "t_2δ ≡ m₂", 6, 4)
        g.traccia((X0, 0), (X0, -140)); g.testo((X0, -140), "t_1δ ≡ m₁", 6, 4)
        g.traccia((5, zm), (X3, zm)); g.testo((5, zm), "t_2ε", 0, -8)
        g.traccia((5, -ym), (X3, -ym)); g.testo((5, -ym), "t_1ε", 0, 18)
        g.traccia(P3(T1m, X3), P3(T2m, X3)); g.testo((X3 + ym / 2, zm / 2), "t_3ε ≡ m₃", 8, -4)
    else:
        Ka = (20, 0)
        ya = ym * (X3 - Ka[0]) / (X0 - Ka[0]); za = zm * (X3 - Ka[0]) / (X0 - Ka[0])
        g.traccia(Ka, (X3, za)); g.testo((X3, za), "t_2α", -36, 0)
        g.traccia(Ka, (X3, -ya)); g.testo((X3, -ya), "t_1α", -36, 14)
        arco(g, X3, ya)
        g.traccia((X3, za), (X3 + ya, 0)); g.testo((X3 + ya, 0), "t_3α", 4, -6)
        g.retta(P3(T1m, X3), P3(T2m, X3), "rosso")
    g.retta((X0, zm), (X0, -ym), "rosso", 1.4)
    if i == 1:
        g.testo((X0, -ym / 2), "m₁ ≡ m₂", 6, 4, "rosso")
        g.testo((X3 + ym / 2, zm / 2), "m₃", -26, 18, "rosso")
    g.punto((X0, zm), "T_{2m}", -50, -6); g.punto((X0, -ym), "T_{1m}", -50, 14)
    g.punto(P3(T1m, X3), None); g.punto(P3(T2m, X3), None)
f.salva(OUT + "04-piani-per-retta-di-profilo.svg")
print("ok")
