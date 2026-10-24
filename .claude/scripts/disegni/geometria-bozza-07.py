"""Schemi per la bozza di geometria descrittiva 07 (il ribaltamento, lezione del 22 ottobre).

Usa disegni_monge.py senza modificarlo; le funzioni per archi, lineette e controllo delle
misure vere sono copiate da geometria-07.py (che non va toccato).

Disegni:
- b07-spazio-proiettante-in-seconda-su-pi1  (proposto: il proiettante in seconda nello spazio)
- b07-punto-unito-sulla-cerniera            (proposto: verifica dell'omologia di ribaltamento)
- b07-punto-sulla-retta-di-profilo          (scheda PO_riepilogo_1, soluzione della docente)
- b07-omologia-es1 ... es6                  (scheda OMOLOGIA_riepilogo, dalla soluzione della docente)
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, piano, COLORI, interseca

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"

TRI = {"A": (70, 45), "B": (250, 70), "C": (150, 165)}   # stesso triangolo della sbobina 07
NOMI = "ABC"


# ---------- funzioni copiate da geometria-07.py ----------

def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def dist(a, b):
    return math.dist(a, b)


def lati(pts):
    return [round(dist(pts[i], pts[(i + 1) % 3]), 3) for i in range(3)]


def lati_veri(tri=TRI):
    return lati([tri[n] for n in NOMI])


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
    L = dist(a, b)
    d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
    q = (-d[1], d[0])
    m = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    for i in range(n):
        o = (i - (n - 1) / 2) * 4
        c = lungo(m, d, o)
        f._linea(lungo(c, q, -5), lungo(c, q, 5), colore, 1.3)


def arco3d(t, c, e1, e2, r, a0, a1, colore="grigio", n=40):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(t._p(tuple(c[j] + r * (math.cos(a) * e1[j] + math.sin(a) * e2[j]) for j in range(3))))
    dd = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    t.f.parti.append(f'<path d="{dd}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                     f'stroke-width="1.2" stroke-dasharray="5,3"/>')


def nota2(f, y, riga1, riga2):
    f.nota(20, y, riga1)
    f.nota(20, y + 17, riga2)


def controlla(nome, pts, tri=TRI):
    vere = lati_veri(tri)
    trovate = lati(pts)
    assert all(abs(x - y) < 1e-6 for x, y in zip(vere, trovate)), (nome, vere, trovate)
    print(f"{nome}: lati {trovate} = veri {vere}")


def a_capo(f, y, testo, larghezza=None, passo=17):
    """Didascalia che va a capo da sola (circa 6.7 px per carattere a 13 px)."""
    maxc = int(((larghezza or f.w) - 40) / 6.7)
    righe, riga = [], ""
    for parola in testo.split():
        if len(riga) + len(parola) + 1 > maxc:
            righe.append(riga); riga = parola
        else:
            riga = (riga + " " + parola).strip()
    righe.append(riga)
    for i, r in enumerate(righe):
        f.nota(20, y + i * passo, r)


def contorno(f, punti, colore="nero", spessore=1.8):
    pts = " ".join("{:.1f},{:.1f}".format(*f._s(p)) for p in punti)
    f.parti.append(f'<polygon points="{pts}" fill="none" stroke="{COLORI.get(colore, colore)}" stroke-width="{spessore}"/>')


def allineati(a, b, c):
    return abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) < 1e-6


# =========================================================================================
# 1. (proposto) Nello spazio: il piano proiettante in seconda ribaltato su pi1 intorno a t1alfa
# =========================================================================================
SC = 0.62
f = Figura(600, 470, 0, "Nello spazio: il piano α proiettante in seconda si abbatte su π₁ intorno a t₁α")
t = Triedro(f, (262, 200), X3=400, U=360, Y=230, Z=220, scala=0.75)
t.piani()
PH = math.radians(62)
K3 = (70, 0, 0)
e = (math.cos(PH), 0, math.sin(PH))           # direzione di t2alfa
n, dd = piano(K3, tuple(K3[j] + e[j] for j in range(3)), (K3[0], 1, 0))
t.piano(n, dd, "blu", 0.14)
tr = t.tracce(n, dd, "nero", None)
t.testo(tr[2][1], "t_2α", 8, 14, "nero", 13)
t.testo(tr[1][1], "t_1α", -30, 4, "nero", 13)
P, Pr, Pp = {}, {}, {}
for n_ in NOMI:
    s, y = TRI[n_][0] * SC, TRI[n_][1] * SC
    P[n_] = (K3[0] + s * e[0], y, s * e[2])
    Pr[n_] = (K3[0] + s, y, 0)
    Pp[n_] = (P[n_][0], 0, P[n_][2])           # seconda proiezione, su t2alfa
    arco3d(t, (K3[0], y, 0), (1, 0, 0), (0, 0, 1), s, math.degrees(PH), 0, "rosso")
    t.richiamo(P[n_], Pp[n_])
SCTRI = {k: (v[0] * SC, v[1] * SC) for k, v in TRI.items()}
controlla("spazio, proiettante in seconda", [P[n_] for n_ in NOMI], SCTRI)
controlla("spazio, ribaltato su pi1", [Pr[n_] for n_ in NOMI], SCTRI)
t._poligono([P[n_] for n_ in NOMI], "blu", 0.3, "blu")
t._poligono([Pr[n_] for n_ in NOMI], "rosso", 0.2, "rosso")
etP = {"A": (-4, -10), "B": (8, -2), "C": (8, -4)}
etR = {"A": (-26, 6), "B": (8, 14), "C": (-8, 20)}
for n_ in NOMI:
    t.punto(P[n_], n_, *etP[n_], "blu")
    t.punto(Pr[n_], n_ + "*", *etR[n_], "rosso")
    t.punto(Pp[n_], n_ + "_2", -26, 4, "grigio")
nota2(f, 445, "Ogni punto descrive un arco su un piano perpendicolare a t₁α (cioè parallelo a π₂):",
      "la distanza da π₂, l'aggetto, non cambia. Le seconde proiezioni A₂ B₂ C₂ stanno su t₂α.")
f.salva(OUT + "b07-spazio-proiettante-in-seconda-su-pi1.svg")

# =========================================================================================
# 2. (proposto) Omologia di ribaltamento: la retta AC e la sua ribaltata si incontrano sulla cerniera
# =========================================================================================
TH = math.radians(30)
K = (40, 0)
d = (math.cos(TH), -math.sin(TH))
nr = (-math.sin(TH), -math.cos(TH))
f = Figura(600, 500, 205, "La retta r = AC e la sua ribaltata r* si incontrano su t₁α, in T₁r", x0=40)
f.lt(-20, 540)
fine1 = lungo(K, d, 360)
f.traccia(K, fine1); f.testo(fine1, "t_1α", 4, 14)
f.traccia(K, (K[0], 190)); f.testo((K[0], 190), "t_2α", 6, 4)
f.angolo_retto(K, (1, 0), (0, 1))
p1, p2, pr = {}, {}, {}
for n_ in NOMI:
    s, h = TRI[n_]
    p1[n_] = lungo(K, d, s)
    p2[n_] = (p1[n_][0], h)
    pr[n_] = lungo(p1[n_], nr, h)
controlla("ribaltato su pi1 (verifica punto unito)", [pr[n_] for n_ in NOMI])
# traccia della retta AC: dove la quota si annulla (s = 40 nel piano)
sA, hA = TRI["A"]; sC, hC = TRI["C"]
sT = sA - hA * (sC - sA) / (hC - hA)
T1 = lungo(K, d, sT)
T2lt = (T1[0], 0)
assert abs(interseca(p2["A"], p2["C"], (0, 0), (1, 0))[0] - T1[0]) < 1e-6
assert allineati(pr["A"], pr["C"], T1), "A*C* deve passare per T1r"
f.figura([p2[n_] for n_ in NOMI], "blu")
f.figura([pr[n_] for n_ in NOMI], "rosso")
for n_ in NOMI:
    f.richiamo(p1[n_][0], p2[n_][1], p1[n_][1])
    f.costruzione(p1[n_], pr[n_])
f.angolo_retto(p1["A"], d, nr)
f.angolo_retto(p1["C"], d, nr)
# r2 prolungata fino alla LT, richiamo fino a t1alfa, r* prolungata fino a T1r
f.retta(p2["A"], T2lt, "arancio", 1.4)
f.richiamo(T1[0], 0, T1[1])
f.retta(pr["A"], T1, "arancio", 1.4)
f.punto(T1, "T_1r", -46, 4, "arancio")
f.punto(T2lt, None)
et2 = {"A": (8, 6), "B": (6, -6), "C": (6, -6)}
et1 = {"A": (6, -6), "B": (8, -4), "C": (8, -4)}
etr = {"A": (-30, 4), "B": (8, 10), "C": (-12, 18)}
for n_ in NOMI:
    f.punto(p2[n_], n_ + "₂", *et2[n_], "blu")
    f.punto(p1[n_], n_ + "₁", *et1[n_])
    f.punto(pr[n_], n_ + "*", *etr[n_], "rosso")
f.testo(p2["A"], "r_2", -34, 26, "arancio", 14)
f.testo(pr["A"], "r*", -24, -26, "arancio", 14)
nota2(f, 470, "T₁r sta sulla cerniera e non si muove: è un punto unito. Rette corrispondenti si",
      "incontrano sull'asse t₁α; punti corrispondenti stanno sulle perpendicolari all'asse.")
f.salva(OUT + "b07-punto-unito-sulla-cerniera.svg")

# =========================================================================================
# 3. Scheda PO_riepilogo_1: un punto P sulla retta di profilo, con il ribaltamento su pi2
# =========================================================================================
f = Figura(520, 365, 160, "Un punto P della retta r di profilo, con il ribaltamento del piano", x0=260)
f.lt(-240, 220)
f.traccia((0, 150), (0, -125)); f.testo((0, 150), "t_2α ≡ t_1α", 8, 14)
q2, a1 = 106, 93                 # quota di T2r e aggetto di T1r (proporzioni della scheda)
T2r, T1r = (0, q2), (0, -a1)
T1s = (-a1, 0)                   # T1r ribaltato: l'aggetto diventa distanza dalla cerniera
arco(f, (0, 0), a1, -90, -180, "grigio", 1, "4,3")
f.retta(T1s, T2r, "rosso", 1.8)
xP = 37                          # distanza di P* dalla cerniera, scelta come nella scheda
Ps = (-xP, q2 * (1 - xP / a1))
assert allineati(T1s, T2r, Ps)
P2_, P1_ = (0, Ps[1]), (0, -xP)
f.costruzione(Ps, P2_)
f.costruzione(Ps, (-xP, 0))
arco(f, (0, 0), xP, 180, 270, "grigio", 1, "4,3")
f.punto(T2r, "T_2r", 8, 4)
f.punto(T1r, "T_1r", 8, 6)
f.punto(T1s, "(T_1r)*", -64, 20, "rosso")
f.punto(Ps, "P*", -30, -6, "rosso")
f.punto(P2_, "P_2", 8, -4, "rosso")
f.punto(P1_, "P_1", 8, 6, "rosso")
f.testo((0, 40), "r_2 ≡ r_1", 8, 18, "nero", 13)
f.testo(lungo(T1s, (0.66, 0.75), 50), "r*", -30, 0, "rosso", 14)
a_capo(f, 305, "Il piano di profilo che contiene r si ribalta su π₂ intorno a t₂α: la quota resta, "
          "l'aggetto diventa distanza dalla cerniera. P* si sceglie su r*, poi si torna a P₂ e P₁.")
f.salva(OUT + "b07-punto-sulla-retta-di-profilo.svg")


# =========================================================================================
# 4-9. Scheda OMOLOGIA_riepilogo (esercitazione guidata del 22 ottobre), dalla soluzione
#      Coordinate prese dalla scheda (pixel della pagina a 1200 px di larghezza, y verso il basso).
# =========================================================================================

def Q(px, py):
    return (px, -py)


def foglio(ox, oy, w, h, titolo):
    return Figura(w, h, -oy, titolo, x0=-ox)


def X(a, b, c, d):
    return interseca(Q(*a), Q(*b), Q(*c), Q(*d))


def px(p):
    return (p[0], -p[1])


def oltre(a, b, k):
    """Punto sulla retta ab, oltre b di k volte ab (pixel)."""
    return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)


def segno_U_inf(f, c, dirz, nome="U∞"):
    """Il centro improprio: un trattino nella direzione e la scritta."""
    L = math.hypot(*dirz)
    u = (dirz[0] / L * 18, dirz[1] / L * 18)
    f.retta(Q(c[0] - u[0], c[1] - u[1]), Q(c[0] + u[0], c[1] + u[1]), "nero", 1.2)
    f.testo(Q(*c), nome, -34, 4, "nero", 14)


def segno_u_inf(f, c):
    """L'asse improprio: una crocetta e la scritta."""
    f.retta(Q(c[0] - 12, c[1] - 14), Q(c[0] + 12, c[1] + 14), "nero", 1.2)
    f.retta(Q(c[0] - 14, c[1] + 10), Q(c[0] + 14, c[1] - 10), "nero", 1.2)
    f.testo(Q(*c), "u∞", 16, 6, "nero", 14)


def seg(f, a, b, colore="nero", spessore=1.8):
    f.retta(Q(*a), Q(*b), colore, spessore)


def cost(f, a, b):
    f.costruzione(Q(*a), Q(*b))


def pt(f, p, nome, dx=6, dy=-6, colore="nero"):
    f.punto(Q(*p), nome, dx, dy, colore)


def inter_px(a, b, c, d):
    return px(interseca(Q(*a), Q(*b), Q(*c), Q(*d)))


def par(p, a, b):
    """Secondo punto della parallela ad ab per p."""
    return (p[0] + b[0] - a[0], p[1] + b[1] - a[1])


# --- Esercizio 1: centro e asse impropri (traslazione) ---
r_ = ((113, 296), (466, 229)); rr = ((110, 351), (462, 284))
P = (278, 185)
dU = (80, 100)
f = foglio(50, 140, 470, 360, "Es. 1 – U∞, u∞, r e r′: trovare P′")
seg(f, *r_); seg(f, *rr)
f.testo(Q(*r_[1]), "r", -18, -8, "nero", 15); f.testo(Q(*rr[1]), "r′", -24, 24, "nero", 15)
segno_U_inf(f, (170, 172), dU)
segno_u_inf(f, (100, 412))
M = inter_px(P, (228, 272), *r_)                       # retta ausiliaria per P, scelta liberamente
Mp = inter_px(M, (M[0] + dU[0], M[1] + dU[1]), *rr)    # M' sulla parallela a U∞
Pp = inter_px(P, (P[0] + dU[0], P[1] + dU[1]), Mp, par(Mp, P, M))
cost(f, P, oltre(P, M, 1.45)); cost(f, oltre(M, Mp, -0.6), Mp)
cost(f, Mp, Pp); cost(f, P, Pp)
pt(f, P, "P", 6, -6); pt(f, M, "M", -24, -6, "rosso"); pt(f, Mp, "M′", -22, 22, "rosso")
pt(f, Pp, "P′", 8, -2, "rosso")
a_capo(f, 312, "PM incontra r in M; da M, nella direzione di U∞, si trova M′ su r′. P′M′ è parallela" " " "a PM (asse all'infinito) e PP′ è parallela a MM′ (centro all'infinito).")
f.salva(OUT + "b07-omologia-es1.svg")
print("es1 P'", [round(v) for v in Pp])

# --- Esercizio 2: centro proprio, asse improprio (omotetia): la retta n' ---
U = (790, 157)
n_ = ((657, 213), (1030, 365)); r_ = ((620, 376), (1016, 235)); rr = ((651, 438), (1047, 298))
f = foglio(590, 130, 520, 420, "Es. 2 – U, u∞, r e r′: trovare n′")
seg(f, *n_); seg(f, *r_); seg(f, *rr)
f.testo(Q(*n_[0]), "n", -2, -8); f.testo(Q(*r_[1]), "r", -14, -10); f.testo(Q(*rr[1]), "r′", -20, 26)
pt(f, U, "U", 6, -6)
segno_u_inf(f, (1015, 418))
B = inter_px(*n_, *r_)
Bp = inter_px(U, B, *rr)
M = (803, 272.5)                        # punto scelto su n
A = (755, 327.9)                        # punto scelto su r
Ap = inter_px(U, A, *rr)
Mp = inter_px(U, M, Ap, par(Ap, A, M))  # t' parallela a t per A'
for a, b in ((U, oltre(U, A, 1.25)), (U, oltre(U, M, 1.25)), (U, oltre(U, B, 1.1)), (A, M), (Ap, Mp)):
    cost(f, a, b)
np0, np1 = oltre(Bp, Mp, 2.6), oltre(Mp, Bp, 1.9)
seg(f, np0, np1, "rosso", 2)
f.testo(Q(*np0), "n′", 4, 18, "rosso")
pt(f, B, "B", 4, -8, "rosso"); pt(f, Bp, "B′", 2, -10, "rosso")
pt(f, M, "M", -6, -10, "rosso"); pt(f, Mp, "M′", 6, 18, "rosso")
pt(f, A, "A", -22, -4, "rosso"); pt(f, Ap, "A′", -26, -4, "rosso")
f.testo(Q((A[0] + M[0]) / 2, (A[1] + M[1]) / 2), "t", 4, 8, "grigio", 13)
f.testo(Q((Ap[0] + Mp[0]) / 2, (Ap[1] + Mp[1]) / 2), "t′", 4, 10, "grigio", 13)
a_capo(f, 368, "B = n ∩ r, B′ su UB e su r′. Per M di n: la retta ausiliaria t = AM e la sua corrispondente" " " "t′ per A′, parallela a t (asse all'infinito); M′ su UM. n′ = B′M′.")
f.salva(OUT + "b07-omologia-es2.svg")
print("es2 n' // n ?", round(angolo(Bp, Mp), 2), round(angolo(*n_), 2))

# --- Esercizio 3: omologia speciale (centro sull'asse) ---
U = (247, 787); u_ = ((63, 825), (628, 705))
A, B, C = (204, 688), (436, 775), (152, 893)
Ap = oltre(U, A, 1.97)                  # A' = (163, 591) sulla scheda, allineato con U e A
f = foglio(40, 560, 620, 460, "Es. 3 – U sull'asse u, ABC, A e A′: trovare A′B′C′")
seg(f, *u_); f.testo(Q(*u_[0]), "u", 2, -8)
contorno(f, [Q(*A), Q(*B), Q(*C)], "nero")
cost(f, Ap, U)
X1 = inter_px(A, C, *u_)                 # la retta r = CA incontra l'asse
Cp = inter_px(Ap, X1, U, C)
X2 = inter_px(A, B, *u_)
Bp = inter_px(Ap, X2, U, B)
X3 = inter_px(C, B, *u_)                 # verifica: CB e C'B' sull'asse
assert allineati(Q(*Cp), Q(*Bp), Q(*X3)), "verifica sull'asse"
cost(f, oltre(C, A, 1.6), C); cost(f, Ap, Cp); cost(f, U, oltre(U, C, 1.6))
cost(f, A, X2); cost(f, Ap, X2); cost(f, U, oltre(U, B, 1.15))
cost(f, B, X3); cost(f, Bp, X3)
contorno(f, [Q(*Ap), Q(*Bp), Q(*Cp)], "rosso", 2.2)
pt(f, U, "U", 4, -10); pt(f, A, "A", 8, -4); pt(f, Ap, "A′", 6, -6)
pt(f, B, "B", 4, 20); pt(f, C, "C", -6, 22)
pt(f, Bp, "B′", -6, -10, "rosso"); pt(f, Cp, "C′", 8, 16, "rosso")
for X_ in (X1, X2, X3):
    pt(f, X_, None)
f.testo(Q(*oltre(C, A, 1.55)), "r", 6, 0, "grigio", 14)
f.testo(Q(*oltre(X1, Ap, 0.75)), "r′", -24, 0, "rosso", 14)
a_capo(f, 415, "r = CA incontra u in un punto unito; r′ lo unisce ad A′ e taglia UC in C′. Con AB si trova B′" " " "su UB. Verifica: CB e C′B′ si incontrano sull'asse.")
f.salva(OUT + "b07-omologia-es3.svg")

# --- Esercizio 4: centro proprio, asse improprio: il punto P' ---
U, P = (828, 652), (790, 751)
r_ = ((856, 808), (1015, 747)); rr = ((877, 877), (1037, 815))
f = foglio(690, 610, 380, 375, "Es. 4 – U, u∞, r e r′: trovare P′")
seg(f, *r_); seg(f, *rr)
f.testo(Q(*r_[1]), "r", -14, -10); f.testo(Q(*rr[1]), "r′", -20, -10)
segno_u_inf(f, (1015, 892))
A = (897, 792.3)
Ap = inter_px(U, A, *rr)
Pp = inter_px(U, P, Ap, par(Ap, P, A))
cost(f, U, oltre(U, Ap, 1.1)); cost(f, U, oltre(U, Pp, 1.4)); cost(f, P, A); cost(f, Pp, Ap)
pt(f, U, "U", -6, -10); pt(f, P, "P", -18, -8)
pt(f, A, "A", 6, -6, "rosso"); pt(f, Ap, "A′", 6, -8, "rosso"); pt(f, Pp, "P′", -24, -2, "rosso")
a_capo(f, 322, "UA dà A′ su r′. P′ sta su UP e sulla parallela a PA per A′ (asse all'infinito).")
f.salva(OUT + "b07-omologia-es4.svg")

# --- Esercizio 5: affinità (centro improprio, asse proprio) ---
u_ = ((116, 1304), (518, 1220))
A, Ap, B, C = (198, 1214), (241, 1133), (445, 1162), (286, 1337)
dU = (Ap[0] - A[0], Ap[1] - A[1])
f = foglio(70, 1040, 480, 460, "Es. 5 – U∞, u, ABC, A e A′: trovare A′B′C′")
seg(f, *u_); f.testo(Q(*u_[0]), "u", 2, -8)
segno_U_inf(f, (122, 1170), dU)
contorno(f, [Q(*A), Q(*B), Q(*C)], "nero")
X1 = inter_px(A, C, *u_)
Cp = inter_px(Ap, X1, C, (C[0] + dU[0], C[1] + dU[1]))
X2 = inter_px(C, B, *u_)
Bp = inter_px(Cp, X2, B, (B[0] + dU[0], B[1] + dU[1]))
X3 = interseca(Q(*A), Q(*B), Q(*Ap), Q(*Bp))
assert abs(X3[1] - interseca(Q(*A), Q(*B), Q(*u_[0]), Q(*u_[1]))[1]) < 1e-6, "verifica AB, A'B' sull'asse"
cost(f, A, Ap); cost(f, C, Cp); cost(f, B, Bp); cost(f, Ap, X1); cost(f, Cp, X2)
contorno(f, [Q(*Ap), Q(*Bp), Q(*Cp)], "rosso", 2.2)
pt(f, A, "A", -20, -2); pt(f, Ap, "A′", -24, -4); pt(f, B, "B", 8, 6); pt(f, C, "C", 8, 14)
pt(f, Bp, "B′", -10, -10, "rosso"); pt(f, Cp, "C′", -26, 6, "rosso")
pt(f, X1, None); pt(f, X2, None)
a_capo(f, 398, "AC incontra u: da lì la retta per A′ taglia in C′ la parallela ad AA′ per C. Allo stesso modo" " " "CB e C′B′ si incontrano sull'asse e B′ sta sulla parallela ad AA′ per B.")
f.salva(OUT + "b07-omologia-es5.svg")

# --- Esercizio 6: affinità, la retta m' ---
u_ = ((555, 1308), (1075, 1308))
O = (612, 1308)
r_ = (O, (858, 1187)); rr = (O, (778, 1413)); m_ = ((781, 1308), (1025, 1187))
A = (705, 1262.3)
dU = (52, 137)
Ap = inter_px(A, (A[0] + dU[0], A[1] + dU[1]), *rr)
B = (836, 1308 - 55 * 121 / 244)       # punto scelto su m
Xn = inter_px(A, B, *u_)
Bp = inter_px(Xn, Ap, B, (B[0] + dU[0], B[1] + dU[1]))
f = foglio(540, 1070, 560, 430, "Es. 6 – U∞, u, r e r′: trovare m′")
seg(f, *u_); seg(f, *r_); seg(f, *rr); seg(f, *m_)
f.testo(Q(*u_[0]), "u", 2, -8); f.testo(Q(*r_[1]), "r", -30, 10); f.testo(Q(*oltre(O, rr[1], 0.55)), "r′", -26, 14)
f.testo(Q(*m_[1]), "m", -30, 10)
segno_U_inf(f, (900, 1110), dU)
cost(f, A, oltre(A, Ap, 1.2)); cost(f, B, oltre(B, Bp, 1.2)); cost(f, A, Xn); cost(f, Ap, Xn)
mp1 = oltre(m_[0], Bp, 1.7)
seg(f, m_[0], mp1, "rosso", 2)
f.testo(Q(*mp1), "m′", 4, 14, "rosso")
pt(f, A, "A", -18, -8, "rosso"); pt(f, Ap, "A′", -32, 14, "rosso")
pt(f, B, "B", -4, -10, "rosso"); pt(f, Bp, "B′", -30, 16, "rosso")
pt(f, Xn, None); pt(f, m_[0], None)
f.testo(Q(960, 1294), "n", 0, -6, "grigio", 13)
f.testo(Q(960, 1336), "n′", 0, 18, "grigio", 13)
a_capo(f, 378, "m incontra u in un punto unito. Retta ausiliaria n = AB; la sua corrispondente n′ passa per A′" " " "e per il punto dove n incontra u; B′ sulla parallela a U∞ per B. m′ unisce il punto unito e B′.")
f.salva(OUT + "b07-omologia-es6.svg")
print("es6 m' // r' ?", round(angolo(m_[0], Bp), 2), round(angolo(*rr), 2))
print("ok")
