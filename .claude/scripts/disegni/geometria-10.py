"""Schemi per la sbobina di geometria descrittiva del 5 novembre (10-...):
il punto di intersezione tra una retta e un piano dato con una figura (triangolo ABC),
con il piano ausiliario proiettante in prima; il segno di sezione a baionetta.

Usa disegni_monge.py senza modificarlo. Le parti nascoste (tratteggio) sono calcolate:
in seconda proiezione e' nascosta la parte di r che sta dietro al piano (aggetto minore),
in prima quella che sta sotto (quota minore), solo dove si sovrappone al triangolo.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"

# ---------- dati nello spazio (x, aggetto, quota) ----------
A, B, C = (60, 20, 70), (380, 190, 80), (240, 10, 230)
P = tuple(0.4 * A[i] + 0.3 * B[i] + 0.3 * C[i] for i in range(3))   # punto del triangolo
D = (140, 10, -80)                                                 # direzione di r
R0 = tuple(P[i] - 1.0 * D[i] for i in range(3))
R1 = tuple(P[i] + 1.0 * D[i] for i in range(3))
N, DD = piano(A, B, C)


def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(len(a)))


def taglia_lati(proj):
    """Dove la retta proj(r) incontra i lati del triangolo proj(ABC): lista di (punto 3D sul lato)."""
    out = []
    for a, b in [(A, B), (B, C), (C, A)]:
        q = interseca(proj(R0), proj(R1), proj(a), proj(b))
        if q is None:
            continue
        pa, pb = proj(a), proj(b)
        L = math.dist(pa, pb)
        t = math.dist(pa, q) / L
        if -1e-9 <= t <= 1 + 1e-9 and abs(math.dist(pa, q) + math.dist(q, pb) - L) < 1e-6:
            out.append((lerp(a, b, t), (a, b)))
    return out


def param(proj, q):
    """Parametro lungo r (0 in R0, 1 in R1) del punto q del disegno."""
    a, b = proj(R0), proj(R1)
    return ((q[0] - a[0]) * (b[0] - a[0]) + (q[1] - a[1]) * (b[1] - a[1])) / math.dist(a, b) ** 2


def lato_davanti(asse):
    """+1 se la parte di r oltre P (verso R1) sta davanti al piano rispetto all'osservatore."""
    f = sum(N[i] * R1[i] for i in range(3)) - DD
    return 1 if f * N[asse] > 0 else -1


def retta_con_visibilita(f, proj, asse, nome, dx, dy):
    """Disegna r in una proiezione: piena, tratteggiata dove e' coperta dal triangolo."""
    tagli = sorted(param(proj, proj(q)) for q, _ in taglia_lati(proj))
    sP = param(proj, proj(P))
    davanti_oltre = lato_davanti(asse) > 0
    # tratto nascosto: tra P e l'uscita dal triangolo, dalla parte che sta dietro
    if davanti_oltre:
        h0, h1 = tagli[0], sP
    else:
        h0, h1 = sP, tagli[-1]
    a, b = proj(R0), proj(R1)
    pt = lambda s: lerp(a, b, s)
    c = COLORI["rosso"]
    for s0, s1, dash in [(0, h0, None), (h0, h1, "6,5"), (h1, 1, None)]:
        (x1, y1), (x2, y2) = f._s(pt(s0)), f._s(pt(s1))
        d = f' stroke-dasharray="{dash}"' if dash else ""
        f.parti.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" '
                       f'stroke-width="2"{d} stroke-linecap="round"/>')
    f.testo(b, nome, dx, dy, "rosso")


# ---------- 1. sul foglio ----------
f = Figura(560, 540, 260, "Il punto di intersezione tra la retta r e il piano del triangolo ABC", x0=30)
f.lt(-10, 500)
f.figura([P2(A), P2(B), P2(C)], "blu")
f.figura([P1(A), P1(B), P1(C)], "blu")
for p, nome, d2, d1 in [(A, "A", (-24, 4), (-24, 6)), (B, "B", (8, 4), (8, 6)), (C, "C", (-6, -10), (8, 6))]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.punto(P2(p), nome + "₂", *d2); f.punto(P1(p), nome + "₁", *d1)

# r1 e gamma1 (piano ausiliario proiettante in prima per r)
f.testo(P1(R1), "≡ γ₁", 26, 6, "viola")
retta_con_visibilita(f, P1, 2, "r₁", 6, 6)
retta_con_visibilita(f, P2, 1, "r₂", 6, 4)

# L, M: dove r1 (cioe' gamma1) taglia i lati del triangolo in prima proiezione
LM = taglia_lati(P1)
assert len(LM) == 2
(L, latoL), (M, latoM) = sorted(LM, key=lambda q: q[0][0])
for q, nome, d1, d2 in [(L, "L", (-8, 20), (-22, -6)), (M, "M", (-30, 20), (8, 14))]:
    f.richiamo(q[0], P2(q)[1], P1(q)[1])
    f.punto(P1(q), nome + "₁", *d1, colore="viola")
    f.punto(P2(q), nome + "₂", *d2, colore="viola")
# n2 = L2 M2, prolungata un poco
e0, e1 = lerp(P2(L), P2(M), -0.15), lerp(P2(L), P2(M), 1.15)
f.retta(e0, e1, "viola", 1.8); f.testo(e1, "n₂", 4, 4, "viola")
f.testo(lerp(P1(P), P1(M), 0.55), "n₁", -4, -10, "viola")

# P2 = n2 ∩ r2, poi P1 su r1 con la linea di richiamo
p2 = interseca(P2(L), P2(M), P2(R0), P2(R1))
p1 = interseca((p2[0], 0), (p2[0], -1), P1(R0), P1(R1))
assert math.dist(p2, P2(P)) < 1e-6 and math.dist(p1, P1(P)) < 1e-6   # il punto trovato e' davvero P
f.richiamo(p2[0], p2[1], p1[1])
f.punto(p2, "P₂", -8, -12, "nero"); f.punto(p1, "P₁", -22, -8, "nero")
f.nota(16, 512, "γ è proiettante in prima e contiene r: γ₁ ≡ r₁. γ taglia il triangolo lungo n, con n₁ ≡ r₁.")
f.nota(16, 530, "Da L₁ e M₁ si richiamano L₂ e M₂ sui lati: n₂ = L₂M₂. Dove n₂ incontra r₂ c'è P₂; P₁ sta su r₁.")
f.salva(OUT + "10-intersezione-retta-figura-piana.svg")

# ---------- 2. nello spazio ----------
f = Figura(620, 500, 0, "Nello spazio: il piano ausiliario γ per r taglia il triangolo lungo n")
t = Triedro(f, (320, 235), X3=420, U=420, Y=300, Z=300, scala=0.65)
t.piani()
# gamma: piano verticale che contiene r
ng, dg = piano(R0, R1, (R0[0], R0[1], R0[2] + 100))
t.piano(ng, dg, "viola", 0.12)
tr = t.tracce(ng, dg, "viola")
a1, b1 = sorted(tr[1], key=lambda q: q[1], reverse=True)
t.testo(lerp(a1, b1, 0.12), "t_1γ ≡ r₁", 8, 16, "viola", 13)
# r prolungata fino a pi1 (prima traccia) per vederla meglio
Tr1 = lerp(R0, R1, -R0[2] / (R1[2] - R0[2]))
# visibilita' per chi guarda il triedro: davanti = verso (-1, 1, 1)
fR1 = sum(N[i] * R1[i] for i in range(3)) - DD
oltre_davanti = fR1 * (-N[0] + N[1] + N[2]) > 0
lontano, vicino = ((R0, P), (P, Tr1)) if oltre_davanti else ((P, Tr1), (R0, P))
t.segmento(*lontano, "rosso", 2.2)
t._poligono([A, B, C], "blu", 0.30, "blu")
t.segmento(*vicino, "rosso", 2.2)
t.segmento(L, M, "viola", 2.2)
for p, nome, dx, dy in [(A, "A", -16, 4), (B, "B", 8, 4), (C, "C", 4, -8)]:
    t.punto(p, nome, dx, dy, "blu")
t.punto(L, "L", -14, -6, "viola"); t.punto(M, "M", 6, 14, "viola")
t.testo(lerp(L, M, 0.25), "n", -4, -8, "viola")
t.punto(P, "P", 8, -6, "nero")
t.punto(Tr1, "T_{1r}", 8, -10)
t.testo(R0, "r", -14, 0, "rosso", 16)
# prima proiezione di r su t1gamma
t.richiamo(R0, (R0[0], R0[1], 0)); t.richiamo(P, (P[0], P[1], 0))
t.punto((P[0], P[1], 0), "P₁", 6, 16)
f.nota(16, 492, "γ è verticale e contiene r: la sua prima traccia è r₁. n = γ ∩ (piano ABC); P = n ∩ r.")
f.salva(OUT + "10-spazio-intersezione-retta-figura-piana.svg")


# ---------- 3. il segno di sezione a baionetta ----------
def freccia(f, a, b, colore="nero", spessore=2.2):
    f._linea(a, b, colore, spessore)
    d = ((b[0] - a[0]) / math.dist(a, b), (b[1] - a[1]) / math.dist(a, b))
    q = (-d[1], d[0])
    p1 = (b[0] - d[0] * 11 + q[0] * 5, b[1] - d[1] * 11 + q[1] * 5)
    p2 = (b[0] - d[0] * 11 - q[0] * 5, b[1] - d[1] * 11 - q[1] * 5)
    pts = " ".join("{:.1f},{:.1f}".format(*f._s(p)) for p in (b, p1, p2))
    f.parti.append(f'<polygon points="{pts}" fill="{COLORI[colore]}"/>')


f = Figura(560, 330, 300, "Il segno di sezione a baionetta, come si usa nella pratica", x0=0)
# pianta schematica: muri perimetrali
for a, b in [((90, 40), (470, 40)), ((470, 40), (470, 260)), ((470, 260), (90, 260)), ((90, 260), (90, 40))]:
    f._linea(a, b, "grigio", 5)
# percorso della sezione: entra da sinistra a y=190, gira a x=280, prosegue a y=110 fino a destra
xg, ya, yb = 280, 215, 85
nero = "nero"
# tratti alle estremita' (fuori e dentro il disegno per un pezzo) con le frecce di vista
f._linea((40, ya), (120, ya), nero, 3)
f._linea((440, yb), (520, yb), nero, 3)
freccia(f, (40, ya), (40, ya + 40)); freccia(f, (520, yb), (520, yb + 40))
f.testo((40, ya + 40), "A", -5, -8, nero, 15, False); f.testo((520, yb + 40), "A", -5, -8, nero, 15, False)
# l'angolo dove la sezione gira: in basso e in alto, con l'angolo retto
f._linea((xg - 40, ya), (xg, ya), nero, 3); f._linea((xg, ya), (xg, ya - 30), nero, 3)
f._linea((xg, yb + 30), (xg, yb), nero, 3); f._linea((xg, yb), (xg + 40, yb), nero, 3)
# il percorso intero (sottile, solo per far capire dove passa: nel disegno non si traccia)
f._linea((120, ya), (xg - 40, ya), "grigio", 1, "2,6")
f._linea((xg, ya - 30), (xg, yb + 30), "grigio", 1, "2,6")
f._linea((xg + 40, yb), (440, yb), "grigio", 1, "2,6")
f.nota(16, 316, "Si disegnano solo le estremità (con le frecce nel senso della vista) e gli angoli in cui la")
f.nota(16, 332, "sezione gira; in mezzo la linea è interrotta (il puntinato grigio indica solo il percorso).")
f.h = 340
f.salva(OUT + "10-segno-sezione-a-baionetta.svg")
print("ok", P, L, M)
