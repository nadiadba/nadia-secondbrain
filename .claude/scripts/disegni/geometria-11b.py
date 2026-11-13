"""Schemi per la seconda parte della sbobina di geometria descrittiva del 10 novembre (11-...):
le sezioni dei solidi. Primo caso: parallelepipedo parallelo a pi1 e pi2 tagliato da un piano
parallelo alla LT (proiezioni ortogonali con la terza proiezione, poi in cavaliera militare);
secondo caso: parallelepipedo ruotato in pianta tagliato da un piano verticale (proiettante in prima),
sul foglio e nello spazio.

Usa disegni_monge.py senza modificarlo. Terza proiezione come in geometria-04.py:
pi3 a destra della verticale x = X3, un punto (x, aggetto, quota) ha P3 = (X3 + aggetto, quota).
Assi della cavaliera come in geometria-11.py: x' a 210 gradi, y' a 300 gradi, z' verticale.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, COLORI, interseca

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


# ---------------------------------------------------------------- utilita'

def P1(p):
    return (p[0], -p[1])


def P2(p):
    return (p[0], p[2])


def P3(p, X3):
    return (X3 + p[1], p[2])


def arco3(f, X3, y):
    """Arco di richiamo dal punto (X3, -y) del primo piano al punto (X3 + y, 0) del terzo."""
    sx, sy = f._s((X3, -y))
    ex, ey = f._s((X3 + y, 0))
    f.parti.append(f'<path d="M {sx:.1f} {sy:.1f} A {y:.1f} {y:.1f} 0 0 0 {ex:.1f} {ey:.1f}" '
                   f'fill="none" stroke="{COLORI["grigio"]}" stroke-width="0.9" stroke-dasharray="3,3"/>')


def orizz(f, x1, x2, y):
    f._linea((x1, y), (x2, y), "grigio", 0.9, "3,3")


def tratt(f, a, b, colore="grigio", spessore=1.1):
    f._linea(a, b, colore, spessore, "5,4")


def campitura(f, poligono, passo=7, colore="rosso"):
    """Tratteggio fitto a 45 gradi dentro un poligono convesso (coordinate di disegno)."""
    c = COLORI[colore]
    pts = " ".join("{:.1f},{:.1f}".format(*f._s(p)) for p in poligono)
    f.parti.append(f'<polygon points="{pts}" fill="{c}" fill-opacity="0.10" stroke="none"/>')
    vals = [p[0] - p[1] for p in poligono]
    lati = list(zip(poligono, poligono[1:] + poligono[:1]))
    k = math.ceil(min(vals) / passo) * passo
    while k < max(vals):
        tagli = []
        for a, b in lati:
            fa, fb = a[0] - a[1] - k, b[0] - b[1] - k
            if fa * fb < 0:
                t = fa / (fa - fb)
                tagli.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
        if len(tagli) >= 2:
            f._linea(tagli[0], tagli[1], colore, 0.8)
        k += passo


def foglio(titolo, X3, alto, basso, w, note, xfine=None):
    h = alto + basso + 20 + 22 * len(note)
    f = Figura(w, h, alto + 10, titolo, x0=30)
    xfine = xfine if xfine is not None else w - 50
    f.lt(-10, xfine)
    if X3 is not None:
        f._linea((X3, alto), (X3, -basso), "nero", 1.2)
        f.testo((X3, alto), "π_3", 8, 12, "grigio", 13, False)
    f.testo((-10, alto), "π_2", 4, 12, "grigio", 13, False)
    f.testo((-10, -basso), "π_1", 4, -2, "grigio", 13, False)
    for i, t in enumerate(note):
        f.nota(18, alto + basso + 26 + 22 * i, t)
    return f


# =====================================================================
# 1. Primo caso, proiezioni ortogonali: piano alfa parallelo alla LT
# =====================================================================

def caso1_po():
    X3 = 300
    x0, x1, y0, y1, H = 110, 250, 30, 130, 175
    a, b = 230.0, 161.0                       # t1alfa ad aggetto a, t2alfa a quota b
    zq = lambda y: b * (1 - y / a)            # quota del piano alfa all'aggetto y
    zf, zb = zq(y1), zq(y0)                   # 70 davanti (piano delta), 140 dietro (piano gamma)
    f = foglio("Sezione di un parallelepipedo con un piano α parallelo alla LT", X3, 205, 250, 620, [
        "In terza proiezione α si vede di taglio (t₃α): r₃ = t₃α ∩ t₃δ, m₃ = t₃α ∩ t₃γ.",
        "r ed m sono parallele alla LT: r₁ ≡ t₁δ e m₁ ≡ t₁γ; r₂ e m₂ tagliano gli spigoli in 1, 2 e 3, 4.",
        "La sezione 1-2-3-4 si ripassa e si campisce; la parte del solido sopra il piano si elimina (grigio)."])
    # tracce di alfa
    f.traccia((-10, -a), (X3, -a)); f.testo((X3, -a), "t_1α", -40, 18)
    f.traccia((-10, b), (X3, b)); f.testo((-10, b), "t_2α", 2, -6)
    f.traccia((X3, b), (X3 + a, 0)); f.testo((X3 + a * 0.35, b * 0.65), "t_3α", 8, -2)
    # tracce dei piani frontali delta (faccia anteriore) e gamma (faccia posteriore)
    f._linea((-10, -y1), (X3, -y1), "arancio", 1.6); f.testo((-10, -y1), "t_1δ ≡ r_1", 2, 16, "arancio", 13)
    f._linea((X3 + y1, 0), (X3 + y1, H + 25), "arancio", 1.6); f.testo((X3 + y1, H + 25), "t_3δ", 4, 4, "arancio", 13)
    f._linea((-10, -y0), (X3, -y0), "viola", 1.6); f.testo((-10, -y0), "t_1γ ≡ m_1", 2, -6, "viola", 13)
    f._linea((X3 + y0, 0), (X3 + y0, H + 25), "viola", 1.6); f.testo((X3 + y0, H + 25), "t_3γ", 6, 14, "viola", 13)
    # richiami verso la terza proiezione
    for y in (y0, y1):
        orizz(f, x1, X3, -y)
        arco3(f, X3, y)
    orizz(f, x1, X3 + y1, zf)
    orizz(f, x1, X3 + y0, zb)
    # parte eliminata (sopra il piano) in grigio tratteggiato
    tratt(f, (x0, zb), (x0, H)); tratt(f, (x1, zb), (x1, H)); tratt(f, (x0, H), (x1, H))
    tratt(f, P3((0, y0, zb), X3), P3((0, y0, H), X3)); tratt(f, P3((0, y1, zf), X3), P3((0, y1, H), X3))
    tratt(f, P3((0, y0, H), X3), P3((0, y1, H), X3))
    # seconda proiezione: faccia anteriore fino a 1-2, poi la sezione
    f.figura([(x0, 0), (x1, 0), (x1, zf), (x0, zf)], "blu")
    campitura(f, [(x0, zf), (x1, zf), (x1, zb), (x0, zb)])
    f.retta((x0, zf), (x1, zf), "rosso", 2.4)
    f.figura([(x0, zf), (x1, zf), (x1, zb), (x0, zb)], "rosso")
    # prima proiezione: dall'alto si vede tutta la sezione
    campitura(f, [(x0, -y0), (x1, -y0), (x1, -y1), (x0, -y1)])
    f.figura([(x0, -y0), (x1, -y0), (x1, -y1), (x0, -y1)], "rosso")
    for x in (x0, x1):
        f.richiamo(x, zb, -y1)
    # terza proiezione: il solido rimasto e la sezione di taglio su t3alfa
    f.figura([P3((0, y0, 0), X3), P3((0, y1, 0), X3), P3((0, y1, zf), X3), P3((0, y0, zb), X3)], "blu")
    f.retta(P3((0, y1, zf), X3), P3((0, y0, zb), X3), "rosso", 4)
    f.punto(P3((0, y1, zf), X3), "r_3", 8, 14, "rosso")
    f.punto(P3((0, y0, zb), X3), "m_3", 6, 22, "rosso")
    # r2 e m2, punti della sezione
    f.testo((x0 - 90, zf), "r_2", 0, -6, "rosso"); f._linea((x0 - 90, zf), (x0, zf), "rosso", 1.2)
    f.testo((x0 - 90, zb), "m_2", 0, -6, "rosso"); f._linea((x0 - 90, zb), (x0, zb), "rosso", 1.2)
    f.punto((x1, zf), "1_2", 6, 16); f.punto((x0, zf), "2_2", -24, 16)
    f.punto((x0, zb), "3_2", -24, -4); f.punto((x1, zb), "4_2", 6, -4)
    f.punto((x1, -y1), "1_1", 6, 16); f.punto((x0, -y1), "2_1", -24, 16)
    f.punto((x0, -y0), "3_1", -24, -4); f.punto((x1, -y0), "4_1", 6, -4)
    f.salva(OUT + "11-sezioni-po-parallelepipedo-piano-parallelo-lt.svg")


# =====================================================================
# 2. Primo caso in cavaliera militare (parallelepipedo 4 x 3 x 5)
# =====================================================================

AX = (math.cos(math.radians(210)), math.sin(math.radians(210)))   # x'
AY = (math.cos(math.radians(300)), math.sin(math.radians(300)))   # y'


def caso1_cavaliera():
    k = 34

    def A(p):
        return (k * (p[0] * AX[0] + p[1] * AY[0]), k * (p[0] * AX[1] + p[1] * AY[1] + p[2]))

    x0, x1, y0, y1, H = 1, 5, 1, 4, 5
    a, b = 5.5, 5.5                       # alfa: z = b (1 - y / a)
    zf, zb = 1.5, 4.5
    fx, fy, fz = A((7.0, 0, 0)), A((0, 8.0, 0)), A((0, 0, 6.3))
    note = [
        "1. Il piano β della faccia anteriore: t₁′β ∥ x′ e t₃′β ∥ z′.",
        "2. La retta r = α ∩ β: parte da t₃′α ∩ t₃′β ed è parallela a x′ (cioè alla LT).",
        "3. I punti dove r′ taglia gli spigoli della faccia anteriore: 1 e 2.",
        "Lo stesso con il piano γ della faccia posteriore: m′, punti 3 e 4. Sul fianco basta unire 4 e 1.",
    ]
    tutti = [fx, fy, fz, A((6.3, a, 0)), A((0, a, 0)), A((6.3, 0, b))]
    xs = [q[0] for q in tutti]
    ys = [q[1] for q in tutti]
    w = 620
    xo = (w - (max(xs) - min(xs))) / 2 - min(xs)
    alto = max(ys) + 40
    h_dis = max(ys) - min(ys) + 70
    f = Figura(w, int(h_dis + 22 * len(note) + 14), alto, "La stessa sezione in cavaliera militare", x0=xo)
    for i, t in enumerate(note):
        f.nota(18, int(h_dis + 22 * i + 8), t)
    O = A((0, 0, 0))
    f.retta(O, fx, "nero", 1.6); f.retta(O, fy, "nero", 1.6); f.retta(O, fz, "nero", 1.6)
    f.angolo_retto(O, AX, AY, 10)
    f.testo(fx, "x′", -16, 18); f.testo(fy, "y′", 8, 6); f.testo(fz, "z′", 6, 4)
    f.punto(O, "O′", -26, -6)
    # tracce di alfa
    f.traccia(A((0, a, 0)), A((6.3, a, 0))); f.testo(A((6.3, a, 0)), "t_1′α", -44, 16)
    f.traccia(A((0, 0, b)), A((6.3, 0, b))); f.testo(A((6.3, 0, b)), "t_2′α", -40, -8)
    f.traccia(A((0, 0, b)), A((0, a, 0))); f.testo(A((0, a * 0.3, b * 0.7)), "t_3′α", 8, -4)
    # piano beta (faccia anteriore) e gamma (posteriore)
    for y, col, nome, dx in ((y1, "arancio", "β", 6), (y0, "viola", "γ", 6)):
        f._linea(A((0, y, 0)), A((6.3, y, 0)), col, 1.4)
        f.testo(A((6.3, y, 0)), f"t_1′{nome}", -40, 16, col, 13)
        f._linea(A((0, y, 0)), A((0, y, 5.8)), col, 1.4)
        f.testo(A((0, y, 5.8)), f"t_3′{nome}", dx, 0, col, 13)
    # rette r' e m', parallele a x'
    f.retta(A((0, y1, zf)), A((6.3, y1, zf)), "rosso", 1.4)
    f.testo(A((6.3, y1, zf)), "r′", -16, 14, "rosso")
    f.retta(A((0, y0, zb)), A((6.3, y0, zb)), "rosso", 1.4)
    f.testo(A((6.3, y0, zb)), "m′", -22, -4, "rosso")
    f.punto(A((0, y1, zf)), None, colore="rosso")
    f.punto(A((0, y0, zb)), None, colore="rosso")
    # parte eliminata
    top = [(x0, y0, H), (x1, y0, H), (x1, y1, H), (x0, y1, H)]
    for p, q in zip(top, top[1:] + top[:1]):
        tratt(f, A(p), A(q))
    for (x, y, z) in ((x0, y1, zf), (x1, y1, zf), (x0, y0, zb), (x1, y0, zb)):
        tratt(f, A((x, y, z)), A((x, y, H)))
    # solido rimasto
    s1, s2, s3, s4 = (x1, y1, zf), (x0, y1, zf), (x0, y0, zb), (x1, y0, zb)
    campitura(f, [A(s1), A(s2), A(s3), A(s4)], 6)
    nascosto = (x0, y0, 0)
    base = [(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)]
    spigoli = list(zip(base, base[1:] + base[:1]))
    spigoli += [((x1, y1, 0), s1), ((x0, y1, 0), s2), ((x0, y0, 0), s3), ((x1, y0, 0), s4)]
    for p, q in spigoli:
        if nascosto in (p, q):
            f._linea(A(p), A(q), "blu", 1.3, "6,4")
        else:
            f.retta(A(p), A(q), "blu", 2.2)
    for p, q in ((s1, s2), (s2, s3), (s3, s4), (s4, s1)):
        f.retta(A(p), A(q), "rosso", 2.6)
    f.punto(A(s1), "1", -14, 16); f.punto(A(s2), "2", 6, 16)
    f.punto(A(s3), "3", 6, -6); f.punto(A(s4), "4", -14, -6)
    f.salva(OUT + "11-sezioni-cavaliera-parallelepipedo-piano-parallelo-lt.svg")


# =====================================================================
# 3. Secondo caso: solido ruotato in pianta, piano secante verticale
# =====================================================================

C2 = (200.0, 110.0)
U2 = (math.cos(math.radians(30)), math.sin(math.radians(30)))      # lato lungo
V2 = (-math.sin(math.radians(30)), math.cos(math.radians(30)))     # lato corto, verso chi guarda
L2, W2, H2 = 100.0, 40.0, 150.0
D2 = (math.cos(math.radians(60)), math.sin(math.radians(60)))      # direzione di t1alfa


def pt2(s, t):
    return (C2[0] + s * U2[0] + t * V2[0], C2[1] + s * U2[1] + t * V2[1])


FL, FR, BL, BR = pt2(-L2, W2), pt2(L2, W2), pt2(-L2, -W2), pt2(L2, -W2)


def taglio_alfa(p, q):
    """Dove la retta pq (in pianta) incontra t1alfa (la retta per C2 con direzione D2)."""
    return interseca(p, q, C2, (C2[0] + D2[0], C2[1] + D2[1]))


R_ = taglio_alfa(FL, FR)          # r = alfa ∩ beta (faccia anteriore), verticale
M_ = taglio_alfa(BL, BR)          # m = alfa ∩ gamma (faccia posteriore)
TA = interseca(C2, (C2[0] + D2[0], C2[1] + D2[1]), (0, 0), (1, 0))   # t1alfa sulla LT


def caso2_po():
    note = [
        "β (faccia anteriore) e γ (faccia posteriore) sono proiettanti in prima, come il piano secante α.",
        "r = α ∩ β è verticale: r₁ ≡ T₁r, r₂ ⊥ LT (T₂r all'infinito); taglia gli spigoli orizzontali in 1 e 2.",
        "Lo stesso con γ: m₁ ≡ T₁m, m₂ ⊥ LT, punti 3 e 4.",
        "In pianta la sezione è il segmento r₁m₁ su t₁α, rinforzato; qui si tiene la parte destra del solido.",
    ]
    f = foglio("Sezione di un parallelepipedo con un piano verticale", None, 195, 240, 560, note, 480)
    ext = lambda p, q, l1, l2: ((p[0] + (q[0] - p[0]) * l1, p[1] + (q[1] - p[1]) * l1),
                               (p[0] + (q[0] - p[0]) * l2, p[1] + (q[1] - p[1]) * l2))
    # tracce: alfa (t1 obliqua, t2 perpendicolare alla LT), beta e gamma (solo la prima traccia)
    yfin = 232
    sfin = (yfin - C2[1]) / D2[1]
    afin = (C2[0] + D2[0] * sfin, C2[1] + D2[1] * sfin)
    f.traccia(P1(TA), P1(afin)); f.testo(P1(afin), "t_1α", 6, 6)
    f.traccia((TA[0], 0), (TA[0], 180)); f.testo((TA[0], 180), "t_2α", -34, 4)
    for p, q, col, nome in ((FL, FR, "arancio", "t_1β"), (BL, BR, "viola", "t_1γ")):
        a, b = ext(p, q, -0.3, 1.25)
        f._linea(P1(a), P1(b), col, 1.6)
        f.testo(P1(b), nome, 6, 4, col, 13)
    # parte eliminata (a sinistra del piano) in grigio
    tratt(f, P1(R_), P1(FL)); tratt(f, P1(FL), P1(BL)); tratt(f, P1(BL), P1(M_))
    for x in (FL[0], BL[0]):
        tratt(f, (x, 0), (x, H2))
    tratt(f, (FL[0], H2), (M_[0], H2)); tratt(f, (FL[0], 0), (M_[0], 0))
    # prima proiezione del solido rimasto
    f.figura([P1(R_), P1(FR), P1(BR), P1(M_)], "blu")
    f.retta(P1(R_), P1(M_), "rosso", 4)
    # seconda proiezione del solido rimasto (tutti gli spigoli verticali si vedono)
    f.figura([(M_[0], 0), (BR[0], 0), (BR[0], H2), (M_[0], H2)], "blu")
    f.retta((FR[0], 0), (FR[0], H2), "blu", 1.8)
    campitura(f, [(M_[0], 0), (R_[0], 0), (R_[0], H2), (M_[0], H2)])
    f.figura([(M_[0], 0), (R_[0], 0), (R_[0], H2), (M_[0], H2)], "rosso")
    # rette r e m, con le tracce
    for P, nome in ((R_, "r"), (M_, "m")):
        f.richiamo(P[0], 0, -P[1])
        f._linea((P[0], 0), (P[0], H2 + 28), "rosso", 1.4)
        f.testo((P[0], H2 + 28), f"{nome}_2", -6, -6, "rosso")
    f.punto(P1(R_), "r_1 ≡ T_{1r}", -92, 16, "rosso")
    f.punto(P1(M_), "m_1 ≡ T_{1m}", -92, -4, "rosso")
    f.punto((R_[0], 0), "(T_{1r})_2", 6, 16)
    f.punto((M_[0], 0), "(T_{1m})_2", 6, 16)
    for P in (FR, BR):
        f.richiamo(P[0], H2, -P[1])
    f.punto((R_[0], H2), "1_2", 6, 16); f.punto((R_[0], 0), "2_2", 6, -6)
    f.punto((M_[0], 0), "3_2", 6, -6); f.punto((M_[0], H2), "4_2", 6, 18)
    f.salva(OUT + "11-sezioni-po-parallelepipedo-piano-verticale.svg")


def caso2_spazio():
    note = [
        "Il solido ha le facce laterali verticali: il piano secante α, anch'esso verticale, le taglia",
        "lungo rette verticali (r sulla faccia anteriore β, m su quella posteriore γ).",
        "I punti della sezione stanno dove r e m incontrano gli spigoli orizzontali: 1, 2, 3, 4.",
    ]
    f = Figura(620, 420 + 22 * len(note), 0, "Il secondo caso nello spazio")
    for i, t in enumerate(note):
        f.nota(18, 420 + 22 * i, t)
    t = Triedro(f, (330, 175), X3=400, U=430, Y=250, Z=240, scala=0.78)
    t.piani()
    # piano alfa: verticale, normale perpendicolare a D2 in pianta
    n = (D2[1], -D2[0], 0.0)
    d = n[0] * C2[0] + n[1] * C2[1]
    t.piano(n, d, "rosso", 0.10)
    t.tracce(n, d, "nero", "α")
    z = lambda p, h: (p[0], p[1], h)
    # parte eliminata (a sinistra del piano)
    for p, q in ((R_, FL), (FL, BL), (BL, M_)):
        t.segmento(z(p, 0), z(q, 0), "grigio", 1.1, "5,4")
        t.segmento(z(p, H2), z(q, H2), "grigio", 1.1, "5,4")
    for p in (FL, BL):
        t.segmento(z(p, 0), z(p, H2), "grigio", 1.1, "5,4")
    # solido rimasto: R, FR, BR, M. Si guarda da sinistra, davanti e dall'alto:
    # sono nascosti la faccia destra, quella posteriore e la base
    pol = [R_, FR, BR, M_]
    for p, q in zip(pol, pol[1:] + pol[:1]):
        t.segmento(z(p, H2), z(q, H2), "blu", 2)
    t.segmento(z(R_, 0), z(FR, 0), "blu", 2)
    t.segmento(z(FR, 0), z(BR, 0), "blu", 1.2, "6,4")
    t.segmento(z(BR, 0), z(M_, 0), "blu", 1.2, "6,4")
    t.segmento(z(FR, 0), z(FR, H2), "blu", 2)
    t.segmento(z(BR, 0), z(BR, H2), "blu", 1.2, "6,4")
    # sezione
    sez = [z(R_, H2), z(R_, 0), z(M_, 0), z(M_, H2)]
    t._poligono(sez, "rosso", 0.28)
    for p, q in zip(sez, sez[1:] + sez[:1]):
        t.segmento(p, q, "rosso", 2.6)
    # rette r e m (verticali), con la prima traccia
    for P, nome in ((R_, "r"), (M_, "m")):
        t.segmento(z(P, H2), z(P, H2 + 60), "rosso", 1.3)
        t.testo(z(P, H2 + 60), nome, 4, 0, "rosso")
    t.punto(z(R_, 0), None, colore="rosso")
    t.punto(z(M_, 0), None, colore="rosso")
    t.testo(z(R_, 0), "2 ≡ T_{1r}", 4, 26, "rosso")
    t.testo(z(M_, 0), "3 ≡ T_{1m}", -86, 4, "rosso")
    t.punto(z(R_, H2), "1", -14, -4); t.punto(z(M_, H2), "4", 6, -4)
    t.testo(z(((R_[0] + FR[0]) / 2, (R_[1] + FR[1]) / 2), H2 * 0.45), "β", -6, 0, "arancio")
    t.testo(z(pt2(L2 * 0.6, -W2), H2), "γ", 4, -8, "viola")
    f.salva(OUT + "11-spazio-sezione-parallelepipedo-piano-verticale.svg")


if __name__ == "__main__":
    caso1_po()
    caso1_cavaliera()
    caso2_po()
    caso2_spazio()
    print("R", R_, "M", M_, "TA", TA, "FL", FL, "FR", FR, "BL", BL, "BR", BR)
