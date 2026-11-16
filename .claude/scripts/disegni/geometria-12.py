"""Schemi per la sbobina di geometria descrittiva del 12 novembre (12-...).

Prima parte, correzione della Prova n. 1:
- omologia: l'esercizio «madre» (coppia A, A', asse e centro: trovare B');
- omologia speciale con l'asse all'infinito (omotetia): trovare s' corrispondente di s;
- ribaltamento di un piano proiettante in prima su pi1 (le quote non cambiano);
- ribaltamento del piano generico che contiene il triangolo ABC con A su pi1;
- tracce del piano da un'orizzontale e una frontale, e retta perpendicolare al piano;
- ribaltamento di un piano proiettante in seconda su pi2 (il lato proiettante resta in vera lunghezza).
Seconda parte, assonometria obliqua con il quadro verticale (x e z sul quadro, y obliqua):
- nello spazio: la direzione di proiezione e la riduzione dell'unita' su y;
- sul foglio: ribaltamento del triangolo intorno a y' (y* a 90 gradi da y') e direzione s*;
- metodo con la pianta: pianta ribaltata sotto x', affinita' di asse x' con la pianta assonometrica.

Usa disegni_monge.py senza modificarlo. Ogni costruzione viene controllata con i conti veri.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, P1, P2, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


# ---------- funzioni di servizio (come in geometria-09.py) ----------

def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def unit(v):
    l = math.hypot(*v)
    return (v[0] / l, v[1] / l)


def arco(f, c, r, a0, a1, colore="grigio", spessore=1, tratteggio="4,3", n=48):
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
    L = math.dist(a, b)
    d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    q = (-d[1], d[0])
    m = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        c = lungo(m, d, o)
        f._linea(lungo(c, q, -5), lungo(c, q, 5), colore, 1.3)


def nota_righe(f, y, righe):
    for i, r in enumerate(righe):
        f.nota(20, y + 17 * i, r)


def piede(p, a, b):
    d = unit((b[0] - a[0], b[1] - a[1]))
    t = (p[0] - a[0]) * d[0] + (p[1] - a[1]) * d[1]
    return (a[0] + d[0] * t, a[1] + d[1] * t)


def lato(p, a, b):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def prolunga(a, b, l0, l1):
    """Segmento sulla retta ab da l0 prima di a a l1 oltre b."""
    d = unit((b[0] - a[0], b[1] - a[1]))
    return lungo(a, d, -l0), lungo(b, d, l1)


def tratt(f, a, b, colore="grigio", spessore=1.1):
    f._linea(a, b, colore, spessore, "5,4")


def lati_uguali(nome, veri, trovati):
    n = len(veri)
    for i in range(n):
        a = math.dist(veri[i], veri[(i + 1) % n])
        b = math.dist(trovati[i], trovati[(i + 1) % n])
        assert abs(a - b) < 1e-6, (nome, i, a, b)
    print(f"{nome}: misure vere ok")


# =========================================================================================
# 1. Omologia: l'esercizio «madre»
# =========================================================================================

def omologia_madre():
    U = (330, 400)                       # centro
    ua, ub = (-25, 37), (590, 116)        # asse u
    A, B = (120, 300), (300, 200)
    k = 0.55                              # A' sul raggio UA, oltre A
    Ap = (U[0] + (A[0] - U[0]) * (1 + k), U[1] + (A[1] - U[1]) * (1 + k))
    M = interseca(A, B, ua, ub)           # la retta AB incontra l'asse in M
    Bp = interseca(M, Ap, U, B)           # M-A' incontra il raggio UB in B'
    # controllo: omologia vera (birapporto costante sui raggi)
    def br(P, Pp):
        X = interseca(U, P, ua, ub)
        return (math.dist(U, Pp) / math.dist(X, Pp)) / (math.dist(U, P) / math.dist(X, P))
    assert abs(br(A, Ap) - br(B, Bp)) < 1e-9
    print("omologia madre: ok")

    f = Figura(640, 540, 440, "Omologia: l'esercizio «madre» (trovare B′ dati A, A′, asse e centro)", x0=30)
    f.retta(ua, ub, "nero", 1.6)
    f.testo(ub, "u (asse)", -60, 22)
    f.costruzione(U, Ap)
    f.costruzione(U, prolunga(U, Bp, 0, 30)[1])
    f.retta(*prolunga(M, A, 0, 40), "blu", 1.6)
    f.retta(*prolunga(M, Ap, 0, 20), "rosso", 1.6)
    f.testo(prolunga(M, A, 0, 40)[1], "s", -6, -8, "blu")
    f.testo(prolunga(M, Ap, 0, 20)[1], "s′", -4, 18, "rosso")
    f.punto(U, "U (centro)", 8, -6)
    f.punto(A, "A", -18, -6, "blu")
    f.punto(B, "B", 6, -8, "blu")
    f.punto(Ap, "A′", 6, 18, "rosso")
    f.punto(Bp, "B′", 6, 18, "rosso")
    f.punto(M, "M", -6, 20)
    nota_righe(f, 470, ["1. Raggio da U per B: B′ starà su questa retta (i punti corrispondenti sono allineati con il centro).",
                        "2. La retta s per A e B incontra l'asse in M; la corrispondente s′ passa per M e per A′.",
                        "3. Dove s′ incontra il raggio UB c'è B′."])
    f.salva(OUT + "12-omologia-esercizio-madre.svg")


# =========================================================================================
# 2. Omologia speciale con l'asse all'infinito (omotetia): s -> s'
# =========================================================================================

def omotetia_retta():
    U = (330, 330)
    k = 1.55                               # rapporto: P' = U + k (P - U)
    om = lambda P: (U[0] + k * (P[0] - U[0]), U[1] + k * (P[1] - U[1]))
    r0, r1 = (360, 250), (600, 330)        # retta r
    A = (440, 276.7)
    Ap = om(A)
    s0, s1 = (110, 390), (230, 110)        # retta s
    M = (190, 203.3)
    Mp = om(M)
    # costruzione della docente: A-M, parallela per A', intersezione con U-M
    dAM = (M[0] - A[0], M[1] - A[1])
    Mc = interseca(Ap, (Ap[0] + dAM[0], Ap[1] + dAM[1]), U, M)
    assert math.dist(Mc, Mp) < 1e-6
    print("omotetia: ok")
    ds = unit((s1[0] - s0[0], s1[1] - s0[1]))
    rp0, rp1 = om(r0), om(r1)

    f = Figura(640, 560, 450, "Omologia speciale con l'asse all'infinito: trovare s′ dato s", x0=0)
    f.retta(r0, r1, "blu", 1.6)
    f.retta(rp0, (rp0[0] + (r1[0] - r0[0]) * 0.75, rp0[1] + (r1[1] - r0[1]) * 0.75), "rosso", 1.6)
    f.testo(r1, "r", 4, 4, "blu")
    f.testo((rp0[0] + (r1[0] - r0[0]) * 0.75, rp0[1] + (r1[1] - r0[1]) * 0.75), "r′", 4, 4, "rosso")
    f.retta(s0, s1, "blu", 1.8)
    f.testo(s1, "s", 6, 4, "blu")
    f.retta(lungo(Mp, ds, -110), lungo(Mp, ds, 160), "rosso", 1.8)
    f.testo(lungo(Mp, ds, 160), "s′", 6, 4, "rosso")
    f.costruzione(U, Ap)
    f.costruzione(U, Mp)
    f.retta(*prolunga(A, M, 20, 30), "verde", 1.2)
    dd = unit(dAM)
    f.retta(lungo(Ap, dd, -20), lungo(Mp, dd, 30), "verde", 1.2)
    f.punto(U, "U", -6, -10)
    f.punto(A, "A", 4, 18, "blu")
    f.punto(Ap, "A′", 6, 18, "rosso")
    f.punto(M, "M", -22, -6, "blu")
    f.punto(Mp, "M′", -28, -6, "rosso")
    f.testo((560, 380), "u all'infinito", 0, 0, "grigio", 13)
    nota_righe(f, 486, ["1. A su r e A′ su r′, allineati con il centro U. Su s si prende un punto qualunque M.",
                        "2. La retta AM; la corrispondente passa per A′ ed è parallela ad AM (l'asse è all'infinito).",
                        "3. M′ sta sul raggio UM. s′ passa per M′ ed è parallela a s."])
    f.salva(OUT + "12-omologia-asse-all-infinito-retta.svg")


# =========================================================================================
# 3. Piano proiettante in prima: ribaltamento su pi1 intorno a t1alfa
# =========================================================================================

def proiettante_prima():
    a, b = (40, -20), (330, -150)          # t1alfa (coordinate di disegno, sotto la LT)
    d = unit((b[0] - a[0], b[1] - a[1]))

    def sul_piano(x, z):
        t = (x - a[0]) / d[0]
        p = lungo(a, d, t)
        return (x, -p[1], z)

    A, B, C = sul_piano(90, 30), sul_piano(170, 120), sul_piano(270, 60)
    n = (d[1], -d[0])                      # normale a t1 verso il basso (lontano dalla LT)
    if n[1] > 0:
        n = (-n[0], -n[1])
    star = [lungo(P1(P), n, P[2]) for P in (A, B, C)]
    lati_uguali("proiettante in prima", [A, B, C], star)
    T2 = (a[0] + (0 - a[1]) / d[1] * d[0], 0)    # dove t1 incontra la LT

    f = Figura(640, 520, 190, "Piano proiettante in prima: ribaltamento su π₁ intorno a t₁α", x0=20)
    f.lt(0, 600)
    f.traccia(T2, b)
    f.traccia(T2, (T2[0], 170))
    f.testo(b, "t_1α", 6, 6)
    f.testo((T2[0], 170), "t_2α", 6, 4)
    f.figura([P2(P) for P in (A, B, C)], "blu")
    f.retta(P1(A), P1(C), "blu", 3)
    for P, s in zip((A, B, C), star):
        f.richiamo(P[0], P2(P)[1], P1(P)[1])
        f.costruzione(P1(P), s)
        f.angolo_retto(P1(P), d, n, 7)
    tacche(f, (B[0], 0), P2(B), 2)
    tacche(f, P1(B), star[1], 2)
    f.figura(star, "rosso")
    for P, nome, e2, e1, es in [(A, "A", (-18, -4), (-8, -12), (-30, 4)), (B, "B", (4, -8), (-6, -12), (8, 6)),
                                (C, "C", (6, -4), (2, -12), (8, 6))]:
        f.punto(P2(P), nome + "_2", *e2, "blu")
        f.punto(P1(P), nome + "_1", *e1, "blu")
    for s, nome, e in zip(star, ("A*", "B*", "C*"), ((-28, 6), (8, 10), (8, 8))):
        f.punto(s, nome, *e, "rosso")
    nota_righe(f, 410, ["Il piano è verticale: tutta la figura, in prima proiezione, cade sulla traccia t₁α (A₁, B₁, C₁).",
                        "Da ogni punto si manda la perpendicolare a t₁α («a 90 gradi») e si riporta la quota del punto",
                        "(per B: le due lineette). Ruotando intorno a t₁α la quota non cambia: A*B*C* è la vera forma."])
    f.salva(OUT + "12-ribaltamento-piano-proiettante-in-prima.svg")


# =========================================================================================
# 4. Triangolo ABC con A su pi1: ribaltamento del piano generico intorno a t1alfa
# =========================================================================================

def ribalta_vero(P, a, b, verso):
    p1 = P1(P)
    H = piede(p1, a, b)
    r = math.sqrt(math.dist(p1, H) ** 2 + P[2] ** 2)
    n = unit((-(b[1] - a[1]), b[0] - a[0]))
    if lato(lungo(H, n, 1), a, b) * verso < 0:
        n = (-n[0], -n[1])
    return lungo(H, n, r)


def triangolo_generico():
    A, B, C = (90, 70, 0), (210, 25, 120), (300, 100, 55)
    t = B[2] / (B[2] - C[2])
    T1r = tuple(B[i] + (C[i] - B[i]) * t for i in range(3))       # prima traccia di r = BC
    a, b = P1(A), P1(T1r)                                          # t1alfa
    verso = -lato(P1(B), a, b)                                     # B* dalla parte opposta
    b1 = P1(B)
    H = piede(b1, a, b)
    dasse = unit((b[0] - a[0], b[1] - a[1]))
    Bbar = lungo(b1, dasse, B[2])                                  # quota di B ribaltata
    r = math.dist(H, Bbar)                                         # raggio di rotazione
    g = unit((b1[0] - H[0], b1[1] - H[1]))
    if lato(lungo(H, g, 1), a, b) * verso < 0:
        g = (-g[0], -g[1])
    Bst = lungo(H, g, r)
    assert math.dist(Bst, ribalta_vero(B, a, b, verso)) < 1e-6
    # affinita' ortogonale di asse t1alfa: r1 -> r* per T1r e B*; C* sulla perpendicolare da C1
    c1 = P1(C)
    Hc = piede(c1, a, b)
    Cst = interseca(b, Bst, c1, Hc)
    assert math.dist(Cst, ribalta_vero(C, a, b, verso)) < 1e-6
    Ast = a
    lati_uguali("triangolo con A su pi1", [A, B, C], [Ast, Bst, Cst])

    f = Figura(660, 640, 175, "Prova: il triangolo ABC con A su π₁, ribaltato su π₁", x0=10)
    f.lt(0, 640)
    t1a, t1b = prolunga(a, b, 70, 60)
    f.traccia(t1a, t1b)
    f.testo(t1b, "t_1α", 6, 6)
    f.figura([P2(P) for P in (A, B, C)], "blu")
    f.figura([P1(P) for P in (A, B, C)], "blu")
    for P in (A, B, C):
        f.richiamo(P[0], P2(P)[1], P1(P)[1])
    # retta r = BC: proiezioni prolungate fino alla traccia
    f.retta(P2(B), (T1r[0], 0), "verde", 1.2)
    f.retta(P1(B), P1(T1r), "verde", 1.2)
    f.richiamo(T1r[0], 0, P1(T1r)[1])
    f.testo((T1r[0], 0), "(T_{1r})_2", -10, -10, "verde", 13)
    f.testo(P2(C), "r_2", 40, 14, "verde", 13)
    f.testo(P1(C), "r_1", 52, 30, "verde", 13)
    # ribaltamento di B
    f.retta(lungo(b1, g, -40), lungo(H, g, r + 30), "grigio", 1)
    f.angolo_retto(H, dasse, g)
    f.costruzione(b1, Bbar)
    f.angolo_retto(b1, dasse, (-g[0], -g[1]))
    tacche(f, (B[0], 0), P2(B), 2)
    tacche(f, b1, Bbar, 2)
    f.retta(H, Bbar, "verde", 1.4)
    f.testo(((H[0] + Bbar[0]) / 2, (H[1] + Bbar[1]) / 2), "raggio", -30, -10, "verde", 12)
    a0, a1 = angolo(H, Bbar), angolo(H, Bst)
    if a1 < a0 - 180:
        a1 += 360
    if a1 > a0 + 180:
        a1 -= 360
    arco(f, H, r, a0, a1)
    # affinita'
    f.costruzione(P1(T1r), Cst)
    f.costruzione(c1, Cst)
    f.figura([Ast, Bst, Cst], "rosso")
    for P, nome, e2, e1 in [(A, "A", (-14, -8), None), (B, "B", (4, -8), (8, -2)), (C, "C", (8, -2), (-4, 24))]:
        f.punto(P2(P), nome + "_2", *e2, "blu")
        if e1:
            f.punto(P1(P), nome + "_1", *e1, "blu")
    f.punto(a, "A_1", -34, 8, "blu")
    f.testo(a, "≡ A*", -46, 26, "rosso", 13)
    f.punto(P1(T1r), "T_{1r}", 8, -4, "verde")
    f.punto(Bbar, "B̄", 6, -2, "verde")
    f.punto(H, None)
    f.punto(Bst, "B*", 8, 8, "rosso")
    f.punto(Cst, "C*", 8, 12, "rosso")
    nota_righe(f, 520, ["1. A₂ sta sulla LT: A è già su π₁, quindi la prima traccia del piano passa per A₁.",
                        "2. r è la retta del lato BC: la sua prima traccia T₁ᵣ. t₁α = A₁T₁ᵣ è l'asse di rotazione.",
                        "3. Ruota B: perpendicolare a t₁α da B₁, si ribalta la quota di B (B̄); il «raggio» di rotazione",
                        "    si riporta sulla perpendicolare e si trova B*.",
                        "4. Affinità ortogonale di asse t₁α: r* passa per T₁ᵣ e B*; C* sta sulla perpendicolare all'asse da C₁.",
                        "    A non si muove: A₁ ≡ A*."])
    f.salva(OUT + "12-ribaltamento-triangolo-con-a-su-pi1.svg")


# =========================================================================================
# 5. Tracce del piano da orizzontale e frontale; retta perpendicolare al piano
# =========================================================================================

def tracce_orizzontale_frontale():
    A = (150, 40, 50)
    D = (290, 100, 50)                    # AD orizzontale (stessa quota)
    B = (200, 40, 140)                    # AB frontale (stesso aggetto)
    C = tuple(B[i] + (D[i] - A[i]) * 0.85 for i in range(3))
    # frontale f = AB: prima traccia (z = 0)
    tf = -A[2] / (B[2] - A[2])
    T1f = tuple(A[i] + (B[i] - A[i]) * tf for i in range(3))
    # orizzontale o = AD: seconda traccia (y = 0)
    to = -A[1] / (D[1] - A[1])
    T2o = tuple(A[i] + (D[i] - A[i]) * to for i in range(3))
    do = unit((P1(D)[0] - P1(A)[0], P1(D)[1] - P1(A)[1]))          # direzione di o1
    df = unit((P2(B)[0] - P2(A)[0], P2(B)[1] - P2(A)[1]))          # direzione di f2
    K = interseca(P1(T1f), lungo(P1(T1f), do, 1), (0, 0), (1, 0))  # t1 sulla LT
    K2 = interseca(P2(T2o), lungo(P2(T2o), df, 1), (0, 0), (1, 0))
    assert math.dist(K, K2) < 1e-6                                 # le tracce si incontrano sulla LT
    # piano vero: controllo che t1 e t2 siano giuste
    u = [B[i] - A[i] for i in range(3)]
    v = [D[i] - A[i] for i in range(3)]
    n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    dd = sum(n[i] * A[i] for i in range(3))
    assert abs(n[0] * K[0] - dd) < 1e-6
    print("tracce da orizzontale e frontale: ok")
    # perpendicolare al piano per C: p1 perpendicolare a t1 (e a o1), p2 perpendicolare a t2 (e a f2)
    p1d = (-do[1], do[0])
    p2d = (-df[1], df[0])

    f = Figura(640, 560, 230, "Prova: tracce del piano da un'orizzontale e una frontale", x0=0)
    f.lt(0, 620)
    f.figura([P2(P) for P in (A, B, C, D)], "blu")
    f.figura([P1(P) for P in (A, B, C, D)], "blu")
    for P in (A, B, C, D):
        f.richiamo(P[0], P2(P)[1], P1(P)[1])
    # frontale: f1 parallela alla LT, f2 = A2B2 prolungata
    f.retta(P2(A), lungo(P2(A), df, -abs(A[2] / df[1])), "verde", 1.3)
    f.retta(P1(A), (T1f[0], P1(A)[1]), "verde", 1.3)
    f.richiamo(T1f[0], 0, P1(T1f)[1])
    f.testo(lungo(P2(A), df, -abs(A[2] / df[1]) * 0.5), "f_2", 8, 4, "verde", 13)
    # orizzontale: o2 parallela alla LT, o1 = A1D1 prolungata
    f.retta(P1(A), P1(T2o), "verde", 1.3)
    f.retta(P2(A), (T2o[0], P2(A)[1]), "verde", 1.3)
    f.richiamo(T2o[0], 0, 0)
    f.testo(((P1(A)[0] + T2o[0]) / 2, P1(A)[1] / 2), "o_1", -4, -8, "verde", 13)
    # tracce
    t1fine = lungo(K, do, 400)
    t2fine = lungo(K, df, 250)
    f.traccia(K, t1fine)
    f.traccia(K, t2fine)
    f.testo(t1fine, "t_1α", 4, 14)
    f.testo(t2fine, "t_2α", 6, 4)
    # perpendicolare
    f.retta(lungo(P1(C), p1d, -60), lungo(P1(C), p1d, 90), "rosso", 1.8)
    f.retta(lungo(P2(C), p2d, -90), lungo(P2(C), p2d, 60), "rosso", 1.8)
    f.angolo_retto(interseca(P1(C), lungo(P1(C), p1d, 1), K, t1fine), do, unit(p1d) if p1d[1] < 0 else (-p1d[0], -p1d[1]), 8)
    f.testo(lungo(P1(C), p1d, 90), "p_1", 6, 4, "rosso")
    f.testo(lungo(P2(C), p2d, -90), "p_2", 6, 4, "rosso")
    for P, nome, e2, e1 in [(A, "A", (-20, -4), (-20, 14)), (B, "B", (-4, -10), (-4, -8)), (C, "C", (8, -6), (8, 12)),
                            (D, "D", (8, 14), (-30, 14))]:
        f.punto(P2(P), nome + "_2", *e2, "blu")
        f.punto(P1(P), nome + "_1", *e1, "blu")
    f.punto(P1(T1f), "T_{1f}", -38, 14, "verde")
    f.punto(P2(T2o), "T_{2o}", -30, -8, "verde")
    nota_righe(f, 418, ["1. AD è un'orizzontale (A₂D₂ parallela alla LT), AB è una frontale (A₁B₁ parallela alla LT).",
                        "2. t₁α passa per la prima traccia della frontale T₁f ed è parallela a o₁ (non a un lato qualunque).",
                        "3. t₂α passa per la seconda traccia dell'orizzontale T₂o ed è parallela a f₂. Le tracce si",
                        "    incontrano sulla LT.",
                        "4. Retta p perpendicolare al piano (qui per C): p₁ perpendicolare a t₁α e a tutte le orizzontali,",
                        "    p₂ perpendicolare a t₂α e a tutte le frontali. Vanno fatte tutte e due le proiezioni."])
    f.salva(OUT + "12-tracce-da-orizzontale-e-frontale.svg")


# =========================================================================================
# 6. Piano proiettante in seconda: ribaltamento su pi2 intorno a t2alfa
# =========================================================================================

def proiettante_seconda():
    A, B, C = (130, 25, 70), (130, 105, 70), (260, 65, 160)       # AB proiettante in seconda
    a2, c2 = P2(A), P2(C)
    d = unit((c2[0] - a2[0], c2[1] - a2[1]))                      # direzione di t2alfa
    K = interseca(a2, c2, (0, 0), (1, 0))
    n = (-d[1], d[0])                                             # normale verso l'alto-sinistra
    star = [lungo(P2(P), n, P[1]) for P in (A, B, C)]
    lati_uguali("proiettante in seconda", [A, B, C], star)

    f = Figura(640, 560, 260, "Piano proiettante in seconda: ribaltamento su π₂ intorno a t₂α", x0=-10)
    f.lt(20, 620)
    f.traccia(K, lungo(K, d, 300))
    f.traccia(K, (K[0], -170))
    f.testo(lungo(K, d, 300), "t_2α", 6, 6)
    f.testo((K[0], -170), "t_1α", 6, 4)
    f.figura([P1(P) for P in (A, B, C)], "blu")
    f.retta(P2(A), P2(C), "blu", 3)
    for P in (A, B, C):
        f.richiamo(P[0], P2(P)[1], P1(P)[1])
    for P, s in zip((A, B, C), star):
        f.costruzione(P2(P), s)
    f.angolo_retto(P2(C), d, n, 7)
    f.figura(star, "rosso")
    tacche(f, P1(A), P1(B), 3, "verde")
    tacche(f, star[0], star[1], 3, "verde")
    for P, nome, e1 in [(A, "A", (-28, 4)), (B, "B", (-28, 8)), (C, "C", (8, 6))]:
        f.punto(P1(P), nome + "_1", *e1, "blu")
    f.punto(P2(A), "A_2 ≡ B_2", 8, 16, "blu")
    f.punto(P2(C), "C_2", 8, 14, "blu")
    for s, nome, e in zip(star, ("A*", "B*", "C*"), ((8, 10), (-30, -4), (-4, -10))):
        f.punto(s, nome, *e, "rosso")
    nota_righe(f, 460, ["Il piano è perpendicolare a π₂: in seconda proiezione la figura cade su t₂α.",
                        "Si ruota intorno a t₂α («il famoso angolo di 90 gradi»): da ogni punto, perpendicolare a t₂α,",
                        "si riporta l'aggetto. Il lato AB è proiettante in seconda: in pianta A₁B₁ è già in vera lunghezza",
                        "e nel ribaltamento resta uguale (tre lineette). La figura non si restringe mentre ruota."])
    f.salva(OUT + "12-ribaltamento-piano-proiettante-in-seconda.svg")


# =========================================================================================
# Assonometria obliqua con il quadro verticale (x e z sul quadro)
# =========================================================================================
RHO = 0.7                     # riduzione dell'unita' su y'
AY = (math.cos(math.radians(225)), math.sin(math.radians(225)))   # y' sul foglio


def spazio_quadro_verticale():
    k = 60
    az, el = math.radians(-35), math.radians(20)

    def p3(p):                 # (x sul quadro, y verso chi guarda, z in alto) -> disegno
        x, y, z = p
        sx = x * math.cos(az) - y * math.sin(az)
        dep = x * math.sin(az) + y * math.cos(az)
        return (sx * k, z * k * math.cos(el) - dep * k * math.sin(el))

    u = 2.2
    O = (0, 0, 0)
    Uy = (0, u, 0)
    Uyp = (u * RHO * AY[0], 0, u * RHO * AY[1])        # proiezione di Uy sul quadro (y = 0)
    quadro = [(-3.0, 0, -2.4), (3.6, 0, -2.4), (3.6, 0, 3.0), (-3.0, 0, 3.0)]
    f = Figura(620, 560, 270, "Nello spazio: il quadro è verticale (contiene x e z)", x0=290)
    f.figura([p3(v) for v in quadro], "#9aa5b1")
    f.testo(p3((-3.0, 0, 3.0)), "quadro", 10, 22, "grigio")
    f.retta(p3(O), p3((3.2, 0, 0)), "nero", 1.8)
    f.retta(p3(O), p3((0, 0, 2.7)), "nero", 1.8)
    f.retta(p3(O), p3((0, 3.6, 0)), "nero", 1.8)
    f.testo(p3((3.2, 0, 0)), "x ≡ x′", -20, -10)
    f.testo(p3((0, 0, 2.7)), "z ≡ z′", 6, 0)
    f.testo(p3((0, 3.6, 0)), "y", 6, 10)
    f.retta(p3(O), p3(tuple(c * 1.6 for c in Uyp)), "rosso", 2)
    f.testo(p3(tuple(c * 1.6 for c in Uyp)), "y′", -20, 10, "rosso")
    f.figura([p3(O), p3(Uy), p3(Uyp)], "verde")
    f.retta(p3(Uy), p3(Uyp), "verde", 2)
    f.punto(p3(O), "O ≡ O′", -64, -6)
    f.punto(p3((u, 0, 0)), "u", -4, -10)
    f.punto(p3((0, 0, u)), "u", 8, 4)
    f.punto(p3(Uy), "U_y", 0, -10)
    f.angolo_retto(p3(O), unit(p3((1, 0, 0))), unit(p3((0, 1, 0))), 10)
    f.angolo_retto(p3(O), unit(p3((0, 0, 1))), unit(p3((0, 1, 0))), 10)
    f.punto(p3(Uyp), "u′_y", -36, 6, "verde")
    m = tuple((Uy[i] + Uyp[i]) / 2 for i in range(3))
    f.testo(p3(m), "direzione di proiezione", -60, 30, "verde", 13)
    nota_righe(f, 500, ["x e z stanno sul quadro: coincidono con x′ e z′, unità vere e angolo di 90 gradi (il prospetto",
                        "resta in vera forma). Solo y, che sporge dal quadro, viene proiettato: y′ è inclinato e l'unità",
                        "su y′ può ridursi o crescere. Il triangolo verde (O, Uy, u′y) è la «squadretta» da ribaltare."])
    f.salva(OUT + "12-spazio-assonometria-quadro-verticale.svg")


def ribaltamento_asse_y():
    k = 34
    u = 2.5 * k
    O = (0, 0)
    ys = (math.cos(math.radians(135)), math.sin(math.radians(135)))      # y*, a 90 gradi da y'
    fx, fz, fy, fys = (7 * k, 0), (0, 5.5 * k), lungo(O, AY, 6 * k), lungo(O, ys, 6 * k)
    Uys, Uyp = lungo(O, ys, u), lungo(O, AY, u * RHO)
    h = 5 * k
    H, Hp = lungo(O, ys, h), lungo(O, AY, h * RHO)
    # controllo: la parallela a s* da H arriva proprio in h' = RHO * h
    assert math.dist(interseca(H, (H[0] + Uyp[0] - Uys[0], H[1] + Uyp[1] - Uys[1]), O, AY), Hp) < 1e-6
    f = Figura(620, 560, 270, "Sul foglio: ribaltamento del triangolo intorno a y′", x0=290)
    f.retta(O, fx, "nero", 1.8)
    f.retta(O, fz, "nero", 1.8)
    f.retta(O, fy, "nero", 1.8)
    f.retta(O, fys, "rosso", 1.4)
    f.angolo_retto(O, (1, 0), (0, 1), 10)
    f.angolo_retto(O, AY, ys, 10)
    f.testo(fx, "x′ ≡ x", -40, 20)
    f.testo(fz, "z′ ≡ z", 8, 4)
    f.testo(fy, "y′", -20, 6)
    f.testo(fys, "y*", -26, 0, "rosso")
    f.punto(O, "O′", 8, 16)
    f.punto((u, 0), "u", -4, 18)
    f.punto((0, u), "u", 8, 4)
    f.punto(Uys, "u", -24, -6, "rosso")
    f.punto(Uyp, "u′_y", -40, 4, "verde")
    arco(f, O, u, 0, 135)
    f.retta(Uys, Uyp, "#1e90c8", 2.2)
    f.testo(((Uys[0] + Uyp[0]) / 2, (Uys[1] + Uyp[1]) / 2), "s*", -26, 0, "#1e90c8")
    f.punto(H, "h", -22, -4, "rosso")
    f.punto(Hp, "h′", -26, 8, "verde")
    f.retta(H, Hp, "#1e90c8", 1.2)
    nota_righe(f, 470, ["Unità uguali su x′, z′ e y* (si riportano col compasso; segnare sempre l'uguaglianza).",
                        "y* è y ribaltato sul quadro, a 90 gradi da y′. s* (in azzurro) unisce u su y* con u′y su y′.",
                        "Ogni profondità vera h presa su y* si porta su y′ con la parallela a s*: si ottiene h′."])
    f.salva(OUT + "12-assonometria-quadro-verticale-ribaltamento-y.svg")


def metodo_pianta():
    k = 36
    x0, x1 = 2.0, 6.0          # larghezza
    y0, y1 = 3.5, 5.5          # profondita': il solido e' staccato dal quadro di y0
    hz = 2.5                   # altezza
    rib = lambda x, y: (x * k, -y * k)                                  # pianta ribaltata (sotto x')
    ass = lambda x, y, z=0: (k * (x + y * RHO * AY[0]), k * (z + y * RHO * AY[1]))
    # direzione dell'affinita' (centro improprio): da P*1 a P'1, uguale per tutti i punti
    dirz = unit((RHO * AY[0], RHO * AY[1] + 1))
    nomi = ["A", "B", "C", "D"]
    pts = [(x0, y0), (x0, y1), (x1, y1), (x1, y0)]                     # A dietro a sinistra, B davanti...
    for (x, y) in pts:
        P, Q = rib(x, y), ass(x, y)
        assert abs(unit((Q[0] - P[0], Q[1] - P[1]))[0] - dirz[0]) < 1e-9
    # costruzione della docente: la profondita' y0 su y* si porta su y' con la direzione del centro;
    # r*1 = A*B* parallela a y* -> r'1 parallela a y'; B'1 nella direzione del centro;
    # B*C* parallela all'asse -> B'1C'1 parallela all'asse
    Ap = interseca((0, -y0 * k), lungo((0, -y0 * k), dirz, 1), (0, 0), AY)
    Ap = (Ap[0] + x0 * k, Ap[1])
    assert math.dist(Ap, ass(*pts[0])) < 1e-6
    Bp = interseca(Ap, lungo(Ap, AY, 1), rib(*pts[1]), lungo(rib(*pts[1]), dirz, 1))
    assert math.dist(Bp, ass(*pts[1])) < 1e-6
    print("metodo con la pianta: ok")

    f = Figura(660, 640, 200, "Il metodo con la pianta: prospetto sopra, pianta ribaltata sotto", x0=150)
    # assi
    f.retta((-3.4 * k, 0), (13.0 * k, 0), "nero", 1.8)
    f.retta((0, 0), (0, 4.2 * k), "nero", 1.8)
    f.retta((0, 0), ass(0, 7.0), "nero", 1.8)
    f.retta((0, 0), (0, -6.4 * k), "rosso", 1.2)
    f.testo((13.0 * k, 0), "x′ ≡ x*", -60, -10)
    f.testo((13.0 * k, 0), "(asse)", -46, 18)
    f.testo((0, 4.2 * k), "z′", 8, 4)
    f.testo(ass(0, 7.0), "y′", -20, 4)
    f.testo((0, -6.4 * k), "y*", 8, 4, "rosso")
    f.punto((0, 0), "O′", -24, -8)
    # prospetto in vera forma sul quadro (segno leggero)
    pros = [(x0 * k, 0), (x1 * k, 0), (x1 * k, hz * k), (x0 * k, hz * k)]
    f.figura(pros, "grigio")
    f.testo(pros[2], "prospetto (vera forma)", -40, -8, "grigio", 12)
    # pianta ribaltata
    f.figura([rib(*p) for p in pts], "blu")
    for (x, y), nm in zip(pts, nomi):
        f.punto(rib(x, y), nm + "_1*", 6 if x == x1 else -34, 18 if y == y1 else -6, "blu")
    # profondita' y0 e y1 su y*, riportate su y' con la direzione del centro
    for y, nm in ((y0, "y_0"), (y1, "y_1")):
        f.punto((0, -y * k), nm, 6, 4, "rosso")
        f.costruzione((0, -y * k), ass(0, y))
        f.punto(ass(0, y), None, colore="verde")
    # corrispondenza punto per punto (allineati con il centro improprio)
    for (x, y) in pts:
        f.costruzione(rib(x, y), ass(x, y))
    # pianta assonometrica
    f.figura([ass(*p) for p in pts], "verde")
    # il solido (spigoli verticali in vera altezza)
    base = [ass(x, y) for x, y in pts]
    top = [ass(x, y, hz) for x, y in pts]
    for i in range(4):
        j = (i + 1) % 4
        if i == 0 or j == 0:               # spigoli a terra che partono da A (dietro a sinistra): nascosti
            tratt(f, base[i], base[j], "rosso", 1.3)
        else:
            f.retta(base[i], base[j], "rosso", 2.2)
        f.retta(top[i], top[j], "rosso", 2.2)
        if i == 0:
            tratt(f, base[i], top[i], "rosso", 1.3)
        else:
            f.retta(base[i], top[i], "rosso", 2.2)
    for (x, y), nm in zip(pts, nomi):
        f.punto(ass(x, y), nm + "_1′", -34 if x == x0 else 8, 18 if y == y1 else -6, "verde")
    # freccia della direzione del centro improprio
    c0 = (9.5 * k, -3.2 * k)
    c1 = lungo(c0, dirz, 1.6 * k)
    f.retta(c0, c1, "#1e90c8", 1.8)
    f.testo(c0, "verso il centro", 8, 0, "#1e90c8", 12)
    f.testo(c0, "(all'infinito)", 8, 16, "#1e90c8", 12)
    nota_righe(f, 462, ["1. Il prospetto si disegna in vera forma sul quadro, con segno leggero (non va calcato): il solido",
                        "   gli starà davanti e lo coprirà in parte.",
                        "2. La pianta si ribalta sotto x′, girandola intorno a x′ (retta comune a π₁ e quadro): A₁*B₁*C₁*D₁*.",
                        "   Qui il solido è staccato dal quadro: la profondità parte da y₀ su y* e si porta su y′.",
                        "3. Affinità di asse x′: y* e y′ si corrispondono (si incontrano sull'asse in O′); i punti",
                        "   corrispondenti sono allineati con il centro, all'infinito (linee grigie tratteggiate).",
                        "4. r₁* = A₁*B₁* è parallela a y*, quindi r₁′ è parallela a y′; B₁′ sta nella direzione del centro.",
                        "   B₁*C₁* è parallela all'asse, quindi B₁′C₁′ è parallela all'asse. Si chiude la pianta assonometrica.",
                        "5. Dai vertici si alzano gli spigoli paralleli a z′: l'altezza non cambia. In rosso il solido."])
    f.salva(OUT + "12-assonometria-quadro-verticale-metodo-pianta.svg")


if __name__ == "__main__":
    omologia_madre()
    omotetia_retta()
    proiettante_prima()
    triangolo_generico()
    tracce_orizzontale_frontale()
    proiettante_seconda()
    spazio_quadro_verticale()
    ribaltamento_asse_y()
    metodo_pianta()
