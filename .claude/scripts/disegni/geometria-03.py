"""Schemi per la sbobina di Geometria descrittiva dell'8 ottobre (03-...).

Nelle proiezioni ortogonali la docente usa i pedici: P1, P2, P3 (l'apice resta per
l'omologia e per l'assonometria). Le coordinate 3D sono (x, aggetto, quota).
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, COLORI, interseca, direzione  # noqa: E402

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def arco(f, centro, raggio, da, a, colore="grigio"):
    """Arco di circonferenza tratteggiato (coordinate di disegno) da 'da' ad 'a', senso antiorario sul foglio."""
    (x1, y1), (x2, y2) = f._s(da), f._s(a)
    f.parti.append(
        f'<path d="M {x1:.1f} {y1:.1f} A {raggio:.1f} {raggio:.1f} 0 0 0 {x2:.1f} {y2:.1f}" fill="none" '
        f'stroke="{COLORI.get(colore, colore)}" stroke-width="1" stroke-dasharray="5,4"/>'
    )


def freccia(f, a, b, colore="grigio", spessore=1):
    """Segmento con punta di freccia in b."""
    f._linea(a, b, colore, spessore)
    d = direzione(a, b)
    n = (-d[1], d[0])
    for s in (1, -1):
        c = (b[0] - d[0] * 8 + n[0] * 3.5 * s, b[1] - d[1] * 8 + n[1] * 3.5 * s)
        f._linea(b, c, colore, spessore)


def direzione_impropria(f, p, d, nome, colore="nero"):
    """Punto improprio: un trattino nella direzione d, con il nome."""
    f._linea(lungo(p, d, -12), lungo(p, d, 12), colore, 1.6)
    f.testo(p, nome, 8, 4, colore)


# 1. Omologia: dato U, u, r e r', trovare P' -------------------------------------
f = Figura(600, 330, 310, "Omologia: dati U, u e le rette corrispondenti r e r′, trovare P′", x0=0)
u_a, u_b = (20, 40), (580, 75)                       # asse u
f._linea(u_a, u_b, "nero", 2.2); f.testo(u_a, "u", 0, -10)
U = (500, 290)
V = interseca(u_a, u_b, (130, 0), (130, 1))           # punto unito di r e r'
r_dir = direzione(V, (300, 290))
r1_dir = direzione(V, (200, 300))
f.retta(lungo(V, r_dir, -40), lungo(V, r_dir, 290), "blu"); f.testo(lungo(V, r_dir, 290), "r", 6, 4, "blu")
f.retta(lungo(V, r1_dir, -40), lungo(V, r1_dir, 270), "verde"); f.testo(lungo(V, r1_dir, 270), "r′", -20, 0, "verde")
A = lungo(V, r_dir, 220)
A1 = interseca(U, A, V, lungo(V, r1_dir, 1))
f.costruzione(U, lungo(A1, direzione(U, A1), 25))
P = (390, 150)
W = interseca(A, P, u_a, u_b)                         # punto unito della retta s = AP
f.retta(lungo(A, direzione(W, A), 25), W, "arancio", 1.4); f.testo(lungo(A, direzione(W, A), 25), "s", 4, -4, "arancio")
P1 = interseca(U, P, W, A1)
f.retta(W, lungo(A1, direzione(W, A1), 25), "arancio", 1.4); f.testo(lungo(W, direzione(W, A1), 150), "s′", -4, 22, "arancio")
f.costruzione(U, lungo(P1, direzione(U, P1), 25))
f.punto(U, "U", 8, -4)
f.punto(V, "V", -24, 18); f.punto(W, "W", 2, 20)
f.punto(A, "A", 8, 14, "blu"); f.punto(A1, "A′", -26, -4, "verde")
f.punto(P, "P", 8, -4, "rosso"); f.punto(P1, "P′", -24, 2, "rosso")
f.salva(OUT + "03-omologia-punto-corrispondente.svg")

# 2. Affinità ortogonale e obliqua ------------------------------------------------
f = Figura(640, 300, 290)
for i, (nome, d) in enumerate([("affinità ortogonale", (0, 1)), ("affinità obliqua", direzione((0, 0), (0.6, 1)))]):
    ox = 20 + 320 * i
    f.nota(ox, 22, nome, 14)
    g = Figura(0, 0, 290, x0=ox)
    g.parti = f.parti
    g._linea((0, 40), (290, 40), "nero", 2.2); g.testo((290, 40), "u", -14, -8)
    k = 0.35
    tri = [(40, 230), (190, 250), (120, 150)]
    img = []
    for p in tri:
        t = (p[1] - 40) * (k - 1) / d[1]               # P' = P + t*d, distanza dall'asse ridotta di k
        img.append(lungo(p, d, t))
    g.figura(tri, "blu"); g.figura(img, "verde")
    for p, q, n in zip(tri, img, "ABC"):
        g.costruzione(lungo(q, d, -10), lungo(p, d, 14))
        g.punto(p, n, 6, -6, "blu"); g.punto(q, n + "′", -26 if n == "A" else 6, 14 if n != "A" else 4, "verde")
    direzione_impropria(g, (255, 170), d, "U_∞")
f.salva(OUT + "03-affinita-ortogonale-obliqua.svg")

# 3. Proiezione centrale e proiezione cilindrica --------------------------------------
def schermo(p, ox, oy):
    """Vista obliqua semplice: x verso destra, y in alto, z in profondita' (verso l'alto a destra)."""
    x, y, z = p
    return (ox + x + 0.45 * z, oy + y + 0.3 * z)


f = Figura(700, 360, 180)
for i, nome in enumerate(["centro proprio: proiezione centrale", "centro improprio: proiezione cilindrica"]):
    ox = 20 + 355 * i
    f.nota(ox, 22, nome, 14)
    xq = 270                                           # piano di quadro x = xq
    xf = 150                                           # figura x = xf
    h, w = 40, 30
    fig3 = [(xf, -h, -w), (xf, h, -w), (xf, h, w), (xf, -h, w)]
    if i == 0:
        S = (20, 0, 0)
        proi = [(xq, S[1] + (p[1] - S[1]) * (xq - S[0]) / (xf - S[0]), (p[2]) * (xq - S[0]) / (xf - S[0])) for p in fig3]
    else:
        proi = [(xq, p[1], p[2]) for p in fig3]
    pq = [(xq, -110, -75), (xq, 110, -75), (xq, 110, 75), (xq, -110, 75)]
    f.figura([schermo(p, ox - 40 * i, 0) for p in pq], "grigio")
    f.testo(schermo(pq[0], ox - 40 * i, 0), "piano di quadro", -40, 18, "grigio", 12, False)
    for p, q in zip(fig3, proi):
        if i == 0:
            f.costruzione(schermo(S, ox, 0), schermo(q, ox, 0))
        else:
            f.costruzione(schermo((xf - 100, p[1], p[2]), ox - 40, 0), schermo(q, ox - 40, 0))
    o = ox - 40 * i
    f.figura([schermo(p, o, 0) for p in fig3], "blu")
    f.figura([schermo(p, o, 0) for p in proi], "verde")
    for p, q, n in zip(fig3, proi, "ABCD"):
        f.testo(schermo(p, o, 0), n, -14 if n in "AB" else 4, 14 if n in "AD" else -4, "blu", 13)
        f.testo(schermo(q, o, 0), n + "′", -26 if n == "B" else 4, 14 if n in "AD" else -4, "verde", 13)
    if i == 0:
        f.punto(schermo(S, ox, 0), "S", -6, -10)
    else:
        f.testo(schermo((xf - 100, 0, 0), o, 0), "S_∞: raggi paralleli", -10, 80, "nero", 12, False)
f.salva(OUT + "03-proiezione-centrale-e-cilindrica.svg")

# 4. Il punto nel triedro --------------------------------------------------------------
def ob(p, ox=170, oy=0):
    """Vista obliqua del triedro: x lungo LT, aggetto y verso chi guarda (in basso a sinistra), quota z in alto."""
    x, y, z = p
    return (ox + x - 0.55 * y, oy + z - 0.4 * y)


f = Figura(620, 340, 225, "Il punto P nel triedro: le tre proiezioni, l'aggetto e la quota")
X0, Y, Z = 300, 240, 200
f.figura([ob((0, 0, 0)), ob((X0, 0, 0)), ob((X0, 0, Z)), ob((0, 0, Z))], "grigio")             # pi2
f.figura([ob((0, 0, 0)), ob((X0, 0, 0)), ob((X0, Y, 0)), ob((0, Y, 0))], "grigio")             # pi1
f.figura([ob((X0, 0, 0)), ob((X0, Y, 0)), ob((X0, Y, Z)), ob((X0, 0, Z))], "grigio")           # pi3
f._linea(ob((-30, 0, 0)), ob((X0, 0, 0)), "nero", 1.6); f.testo(ob((-30, 0, 0)), "LT", -4, -6)
f.testo(ob((20, 0, Z)), "π_2", 4, 20); f.testo(ob((20, Y, 0)), "π_1", 12, -8); f.testo(ob((X0, Y * 0.5, Z * 0.9)), "π_3", -6, 0)
P = (150, 120, 110)
P1 = (150, 120, 0); P2 = (150, 0, 110); P3 = (X0, 120, 110)
for q in (P1, P2, P3):
    f.costruzione(ob(P), ob(q))
f.costruzione(ob(P1), ob((150, 0, 0))); f.costruzione(ob(P2), ob((150, 0, 0)))
f.punto(ob(P), "P", -16, -6, "rosso")
f.punto(ob(P1), "P_1", 6, 16); f.punto(ob(P2), "P_2", 6, -6); f.punto(ob(P3), "P_3", 6, -6)
f.testo(ob((150, 60, 110)), "aggetto", 10, 18, "arancio", 12, False)
f.testo(ob((150, 120, 55)), "quota", -40, 4, "verde", 12, False)
f._linea(ob(P), ob(P2), "arancio", 2.2); f._linea(ob(P), ob(P1), "verde", 2.2)
f.salva(OUT + "03-punto-nel-triedro.svg")

# 5. Le tre proiezioni del punto dopo il ribaltamento ------------------------------------
f = Figura(600, 380, 190, "Le tre proiezioni del punto P sul foglio: π₁ ≡ π₂ ≡ π₃", x0=40)
x0v = 300
f.lt(-20, 530)
f._linea((x0v, 170), (x0v, -170), "nero", 1.2)
xP, ag, qu = 140, 110, 95
P2p, P1p, P3p = (xP, qu), (xP, -ag), (x0v + ag, qu)
f.richiamo(xP, qu, -ag)
f.costruzione(P1p, (x0v, -ag))
arco(f, (x0v, 0), ag, (x0v, -ag), (x0v + ag, 0))
f.costruzione((x0v + ag, 0), P3p)
f.costruzione(P2p, P3p)
f._linea((xP + 14, 0), (xP + 14, qu), "verde", 2); f.testo((xP + 14, qu / 2), "quota", 6, 4, "verde", 12, False)
f._linea((xP + 14, 0), (xP + 14, -ag), "arancio", 2); f.testo((xP + 14, -ag / 2), "aggetto", 6, 4, "arancio", 12, False)
f._linea((x0v, qu + 14), (x0v + ag, qu + 14), "arancio", 2); f.testo((x0v + ag / 2, qu + 14), "aggetto", -22, -6, "arancio", 12, False)
f.punto(P2p, "P_2", -26, -6, "rosso"); f.punto(P1p, "P_1", -26, 14, "rosso"); f.punto(P3p, "P_3", 8, -6, "rosso")
f.salva(OUT + "03-tre-proiezioni-del-punto.svg")

# 6. Retta proiettante in prima ------------------------------------------------------------
f = Figura(600, 360, 175, "Retta r proiettante in prima (perpendicolare a π₁) con un punto P", x0=40)
x0v = 300
f.lt(-20, 530)
f._linea((x0v, 165), (x0v, -165), "nero", 1.2)
xr, ag, qP = 140, 100, 80
f.retta((xr, 0), (xr, 150), "rosso"); f.testo((xr, 150), "r_2", 8, 8, "rosso")
f.testo((xr, 150), "T_{2r}∞", -58, 8, "rosso")
f.retta((x0v + ag, 0), (x0v + ag, 150), "rosso"); f.testo((x0v + ag, 150), "r_3", 8, 8, "rosso")
f.testo((x0v + ag, 150), "T_{3r}∞", 8, 26, "rosso")
f.angolo_retto((xr, 0), (1, 0), (0, 1))
f.richiamo(xr, 0, -ag)
f.punto((xr, -ag), "r_1 ≡ T_{1r} ≡ P_1", 8, 18, "rosso")
f.punto((xr, 0))
f.costruzione((xr, -ag), (x0v, -ag))
arco(f, (x0v, 0), ag, (x0v, -ag), (x0v + ag, 0))
f.costruzione((xr, qP), (x0v + ag, qP))
f.punto((xr, qP), "P_2", -28, -6, "rosso"); f.punto((x0v + ag, qP), "P_3", 8, -6, "rosso")
f.salva(OUT + "03-retta-proiettante-in-prima.svg")

# 7. Retta proiettante in seconda ------------------------------------------------------------
f = Figura(600, 360, 175, "Retta m proiettante in seconda (perpendicolare a π₂)", x0=40)
f.lt(-20, 530)
f._linea((x0v, 165), (x0v, -165), "nero", 1.2)
xm, qm = 140, 100
f.punto((xm, qm), "m_2 ≡ T_{2m}", -90, -8, "rosso")
f.richiamo(xm, qm, 0)
f.retta((xm, 0), (xm, -150), "rosso"); f.testo((xm, -150), "m_1", 8, 0, "rosso")
f.testo((xm, -150), "T_{1m}∞", 8, 18, "rosso")
f.angolo_retto((xm, 0), (1, 0), (0, -1))
f.costruzione((xm, qm), (x0v, qm))
f.retta((x0v, qm), (520, qm), "rosso"); f.testo((520, qm), "m_3", -24, -8, "rosso")
f.testo((520, qm), "T_{3m}∞", -50, 20, "rosso")
f.salva(OUT + "03-retta-proiettante-in-seconda.svg")
print("ok")
