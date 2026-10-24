"""Schemi per la bozza della lezione del 15 ottobre (05-appartenenza-e-rette-ausiliarie)
e viste nello spazio aggiunte alla sbobina 05 dopo il confronto con il quaderno di Marta.

- sbobine/img/05-spazio-*.svg : viste nello spazio fatte alla lavagna (schemi del triedro nel quaderno di Marta)
- bozze/img/b05-*.svg         : esercizi tipo delle schede, svolti come nelle soluzioni della docente
"""
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, tracce_retta, interseca, su_lt

BASE = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/"
SB = BASE + "sbobine/img/"
BZ = BASE + "bozze/img/"


def piano_per(p, d1, d2):
    q = tuple(p[i] + d1[i] for i in range(3)); r = tuple(p[i] + d2[i] for i in range(3))
    return piano(p, q, r)


def P3(p, X3):
    return (X3 + p[1], p[2])


def arco(f, X3, y):
    """Arco di richiamo da (X3, -y) sotto la LT a (X3 + y, 0) sulla LT."""
    cx, cy = f._s((X3, 0))
    f.parti.append(f'<path d="M {cx:.1f} {cy + y:.1f} A {y:.1f} {y:.1f} 0 0 0 {cx + y:.1f} {cy:.1f}" '
                   f'fill="none" stroke="#8a8a8a" stroke-width="0.9" stroke-dasharray="3,3"/>')


def triedro(titolo, h=430, w=600, origine=(262, 190)):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, origine, X3=400, U=360, Y=230, Z=220, scala=0.75)
    t.piani()
    return f, t


# ============ viste nello spazio per la sbobina (dal quaderno di Marta) ============

# 1. Piani che contengono una retta proiettante in seconda
f, t = triedro("Nello spazio: i piani che contengono la retta r proiettante in seconda")
x0, z0 = 230, 120
for (nn, d_), col in [(piano_per((x0, 0, z0), (0, 1, 0), (1, 0, 0.8)), "blu"),
                      (piano_per((x0, 0, z0), (0, 1, 0), (1, 0, 0)), "verde"),
                      (piano_per((x0, 0, z0), (0, 1, 0), (0, 0, 1)), "viola")]:
    t.piano(nn, d_, col, 0.08); t.tracce(nn, d_, col)
t.segmento((x0, 0, z0), (x0, 230, z0), "rosso", 2.6); t.testo((x0, 200, z0), "r", 4, -8, "rosso", 16)
t.punto((x0, 0, z0), "T_{2r}", -40, -8)
f.nota(16, 420, "blu: β proiettante in seconda · verde: γ orizzontale · viola: δ di profilo")
f.salva(SB + "05-spazio-piani-retta-proiettante-in-seconda.svg")

# 2. Piani che contengono una retta parallela alla LT
f, t = triedro("Nello spazio: i piani che contengono la retta r parallela alla LT")
y0, z0 = 110, 90
for (nn, d_), col in [(piano_per((0, y0, z0), (1, 0, 0), (0, 1, -0.75)), "blu"),
                      (piano_per((0, y0, z0), (1, 0, 0), (0, 0, 1)), "verde"),
                      (piano_per((0, y0, z0), (1, 0, 0), (0, 1, 0)), "viola")]:
    t.piano(nn, d_, col, 0.08); t.tracce(nn, d_, col)
t.segmento((60, y0, z0), (400, y0, z0), "rosso", 2.6); t.testo((60, y0, z0), "r", 0, -12, "rosso", 16)
t.punto((400, y0, z0), "T_{3r}", 8, -4)
f.nota(16, 420, "blu: α parallelo alla LT · verde: φ frontale · viola: piano orizzontale")
f.salva(SB + "05-spazio-piani-retta-parallela-alla-lt.svg")

# 3. Retta generica: la terza traccia sta dietro pi2
f, t = triedro("Nello spazio: la terza traccia T₃ᵣ della retta generica sta dietro π₂", h=470, origine=(262, 250))
T1, T2 = (80, 90, 0), (250, 0, 100)
d = tuple(T2[i] - T1[i] for i in range(3))
k = (400 - T1[0]) / d[0]
T3 = tuple(T1[i] + d[i] * k for i in range(3))          # (400, -109, 181)
# pi3 prolungato dietro pi2 (tratteggiato)
Yb = -150
for a, b in [((400, Yb, 0), (400, Yb, 220)), ((400, Yb, 220), (400, 0, 220)), ((400, 0, 0), (400, Yb, 0))]:
    t.segmento(a, b, "grigio", 1, "5,4")
t._poligono([(400, Yb, 0), (400, 0, 0), (400, 0, 220), (400, Yb, 220)], "#9aa5b1", 0.06)
t.testo((400, Yb, 200), "π₃ prolungato dietro π₂", -150, -6, "grigio", 12)
# piano ausiliario alfa proiettante in prima per r: t1 = r1, t3 verticale
nn, d_ = piano_per(T1, d, (0, 0, 1))
t.segmento(T1, (T2[0], 0, 0), "blu", 1.6)
t.segmento((T2[0], 0, 0), (400, T3[1], 0), "blu", 1.4, "5,4")
t.segmento((T2[0], 0, 0), (T2[0], 0, 220), "blu", 1.6); t.testo((T2[0], 0, 210), "t_2α", 6, 0, "blu", 13)
t.segmento((400, T3[1], 0), (400, T3[1], 220), "blu", 1.6, "6,3"); t.testo((400, T3[1], 70), "t_3α", 6, 4, "blu", 13)
t.testo(((T1[0] + T2[0]) / 2, T1[1] / 2, 0), "r₁ ≡ t₁α", 6, 18, "blu", 13)
# la retta
t.segmento(T1, T2, "rosso", 2.4)
t.segmento(T2, T3, "rosso", 1.6, "6,4")
t.punto(T1, "T_{1r}", 8, 14); t.punto(T2, "T_{2r}", -44, -2); t.punto(T3, "T_{3r}", -40, -6, "rosso")
t.punto((400, T3[1], 0), "(T_{3r})₁", 10, 26)
t.testo(((T1[0] + T2[0]) / 2, T1[1] / 2, T2[2] / 2), "r", -16, -4, "rosso", 16)
f.nota(16, 460, "Oltre T₂ᵣ la retta va dietro π₂ (tratteggio) e buca π₃ prolungato in T₃ᵣ, sulla terza traccia di α.")
f.salva(SB + "05-spazio-retta-generica-terza-traccia.svg")

# 4. Retta generica nei due piani ausiliari
f, t = triedro("Nello spazio: la retta generica r nei piani ausiliari α e β")
T1, T2 = (230, 170, 0), (150, 0, 150)
d = tuple(T2[i] - T1[i] for i in range(3))
na, da = piano_per(T1, d, (0, 0, 1))      # alfa proiettante in prima
nb, db = piano_per(T1, d, (0, 1, 0))      # beta proiettante in seconda
t.piano(na, da, "blu", 0.10); t.tracce(na, da, "blu")
t.piano(nb, db, "verde", 0.10); t.tracce(nb, db, "verde")
t.segmento(T1, T2, "rosso", 2.6)
t.punto(T1, "T_{1r}", 8, 18); t.punto(T2, "T_{2r}", 8, -8)
t.testo(((T1[0] + T2[0]) / 2, T1[1] / 2, T2[2] / 2), "r", 8, -2, "rosso", 16)
t.testo(((T1[0] + T2[0]) / 2, T1[1] / 2, 0), "t₁α ≡ r₁", -20, 24, "blu", 13)
t.testo((T2[0], 0, 200), "t₂α", -12, -14, "blu", 13)
t.testo((150, 0, 90), "t₂β ≡ r₂", -78, 0, "verde", 13)
t.testo((T1[0], 215, 0), "t₁β", 8, 4, "verde", 13)
f.nota(16, 420, "blu: α proiettante in prima (t₁α ≡ r₁) · verde: β proiettante in seconda (t₂β ≡ r₂)")
f.salva(SB + "05-spazio-retta-generica-piani-ausiliari.svg")

# 5. Piano generico e le rette che gli appartengono
f, t = triedro("Nello spazio: le rette del piano generico α (generica, orizzontale, frontale)")
Ax, By, Cz = 130, 200, 190
n, dd = piano((Ax, 0, 0), (400, By, 0), (400, 0, Cz))
t.piano(n, dd, "blu", 0.14); t.tracce(n, dd, "nero", "α")


def su_piano(x, y):
    return (x, y, (dd - n[0] * x - n[1] * y) / n[2])


# generica r: da T1r su t1 a T2r su t2
yt1 = lambda x: (dd - n[0] * x) / n[1]
zt2 = lambda x: (dd - n[0] * x) / n[2]
T1r = (330, yt1(330), 0); T2r = (230, 0, zt2(230))
t.segmento(T1r, T2r, "rosso", 2.2); t.punto(T1r, "T_{1r}", 6, 16, "rosso"); t.punto(T2r, "T_{2r}", -42, -2, "rosso")
t.testo(T2r, "r", 14, 30, "rosso", 15)
# orizzontale o a quota h: da T2o (su t2) a T3o (su t3)
h = 60
T2o = ((dd - n[2] * h) / n[0], 0, h); T3o = (400, (dd - n[0] * 400 - n[2] * h) / n[1], h)
t.segmento(T2o, T3o, "arancio", 2.2); t.punto(T2o, "T_{2o}", -44, 8, "arancio"); t.punto(T3o, "T_{3o}", 8, 4, "arancio")
# frontale f ad aggetto k: da T1f (su t1) a T3f (su t3)
kk = 60
T1f = ((dd - n[1] * kk) / n[0], kk, 0); T3f = (400, kk, (dd - n[0] * 400 - n[1] * kk) / n[2])
t.segmento(T1f, T3f, "verde", 2.2); t.punto(T1f, "T_{1f}", -14, 18, "verde"); t.punto(T3f, "T_{3f}", 8, -2, "verde")
# proiettante in prima: buca il piano in un punto solo
v = su_piano(300, 40)
t.segmento((300, 40, 0), (300, 40, 215), "viola", 1.6, "6,4")
t.punto(v, None, colore="viola"); t.testo((300, 40, 215), "v", 6, 4, "viola", 15)
f.nota(16, 412, "rosso: r generica · arancio: o orizzontale (o parallela a t₁α) · verde: f frontale (f parallela a t₂α)")
f.nota(16, 428, "viola: v proiettante in prima, non sta su α: lo buca in un solo punto.")
f.salva(SB + "05-spazio-piano-generico-rette.svg")


# ============ esercizi tipo per la bozza (disegni proposti) ============

def piano_generico(xv, m2, m1):
    """Piano con t2 di pendenza m2 (z = m2 (x - xv)) e t1 di pendenza m1 (y = m1 (x - xv)): restituisce z(x, y)."""
    # normale = (1,0,m2) x (1,m1,0)
    nx, ny, nz = -m2 * m1, m2, m1
    return lambda x, y: -(nx * (x - xv) + ny * y) / nz


# 6. Dalla prima proiezione del triangolo alla seconda, con le rette dei lati (soluzione della scheda)
f = Figura(620, 580, 280, "Proposto: dalla prima proiezione alla seconda (piano generico)", x0=40)
zf = piano_generico(0, 0.6, 0.55)
A = (220, 50, 0); B = (380, 25, 0); C = (300, 130, 0)
A, B, C = [(p[0], p[1], zf(p[0], p[1])) for p in (A, B, C)]
f.lt(-30, 490)
f.traccia((0, 0), (450, 270)); f.testo((450, 270), "t_2α", -40, 0)
f.traccia((0, 0), (450, -247.5)); f.testo((450, -247.5), "t_1α", 6, 4)
for (p, q), nome, col in [((A, C), "r", "rosso"), ((B, C), "s", "verde")]:
    T1, T2 = tracce_retta(p, q)
    f.retta(P1(T1), P1((T2[0], 0, 0)), col, 1.5)
    f.retta(P2(T2), P2((T1[0], 0, 0)), col, 1.5)
    f.richiamo(T2[0], 0, T2[2]); f.richiamo(T1[0], 0, -T1[1])
    f.punto(P1(T1), f"T_{{1{nome}}}", 12 if nome == "r" else -46, -6 if nome == "r" else 18, col); f.punto(P2(T2), f"T_{{2{nome}}}", -44 if nome == "r" else 12, -6 if nome == "r" else 18, col)
    f.punto((T1[0], 0), None, colore=col); f.punto((T2[0], 0), None, colore=col)
    m1 = ((T1[0] + T2[0]) / 2, -T1[1] / 2); m2 = ((T1[0] + T2[0]) / 2, T2[2] / 2)
    f.testo(m1, f"{nome}₁", -30 if nome == "r" else 10, 4, col)
    f.testo(m2, f"{nome}₂", -6 if nome == "r" else 10, -10 if nome == "r" else 4, col)
f.figura([P1(A), P1(B), P1(C)], "blu")
f.figura([P2(A), P2(B), P2(C)], "blu")
for p, nome, dx, dy in [(A, "A", -26, 4), (B, "B", 8, 4), (C, "C", 8, 14)]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.punto(P1(p), nome + "₁", dx, dy, "blu")
for p, nome, dx, dy in [(A, "A", -26, -4), (B, "B", 8, 4), (C, "C", 8, 16)]:
    f.punto(P2(p), nome + "₂", dx, dy, "blu")
f.nota(16, 560, "Rosso: la retta r del lato AC · verde: la retta s del lato BC.")
f.nota(16, 578, "Le tracce di r e di s stanno sulle tracce di α, quindi r e s (e il triangolo) appartengono ad α.")
f.salva(BZ + "b05-proposto-seconda-proiezione-triangolo.svg")

# 7. La retta r appartiene al piano? Due casi
f = Figura(840, 440, 240, "Proposto: la retta r appartiene al piano α?", x0=30)
for ox, caso in [(0, "no"), (410, "si")]:
    f.retta((ox - 10, 0), (ox + 370, 0), "nero", 1.6)
    if ox == 0:
        f.testo((ox - 10, 0), "LT", 2, -6)
    f.traccia((ox + 20, 0), (ox + 340, 192)); f.testo((ox + 340, 192), "t_2α", -40, 2)
    f.traccia((ox + 20, 0), (ox + 340, -176)); f.testo((ox + 340, -176), "t_1α", 6, 4)
    if caso == "si":
        T2 = (ox + 130, 0.6 * 110); T1 = (ox + 260, -0.55 * 240)
    else:
        T2 = (ox + 140, 150); T1 = (ox + 250, -70)
    # proiezioni date, un po' prolungate
    f.retta((T2[0] - 40, T2[1] + T2[1] * 40 / (T1[0] - T2[0])), (T1[0] + 30, -T2[1] * 30 / (T1[0] - T2[0])), "rosso", 1.8)
    f.retta((T2[0] - 30, -T1[1] * 30 / (T1[0] - T2[0])), (T1[0] + 30, T1[1] + T1[1] * 30 / (T1[0] - T2[0])), "rosso", 1.8)
    f.testo((T2[0] - 40, T2[1] + T2[1] * 40 / (T1[0] - T2[0])), "r₂", -18, 0, "rosso")
    f.testo((T2[0] - 30, -T1[1] * 30 / (T1[0] - T2[0])), "r₁", -18, 8, "rosso")
    f.richiamo(T2[0], 0, T2[1]); f.richiamo(T1[0], 0, T1[1])
    f.punto((T2[0], 0), "(T_{2r})₁", -30, 22); f.punto((T1[0], 0), "(T_{1r})₂", 4, -8)
    f.punto(T2, "T_{2r}", -36, -14, "rosso"); f.punto(T1, "T_{1r}", -38, 4, "rosso")
    if caso == "si":
        f.nota(ox + 40, 435, "Sì: T₂ᵣ sta su t₂α e T₁ᵣ sta su t₁α.")
    else:
        f.nota(ox + 40, 435, "No: T₂ᵣ non sta su t₂α (e T₁ᵣ non sta su t₁α).")
f.salva(BZ + "b05-proposto-retta-appartiene.svg")

# 8. Falda su un piano generico: dalla prima proiezione la seconda e la terza, con le orizzontali
X3 = 360
f = Figura(640, 440, 220, "Proposto: la falda ABC sul piano α, seconda e terza proiezione con le orizzontali", x0=30)
zf = lambda x, y: 0.5 * x - y / 0.9          # t2α: z = 0.5 x ; t1α: y = 0.45 x
A = (150, 40); B = (250, 85); C = (270, 30)
A, B, C = [(p[0], p[1], zf(*p)) for p in (A, B, C)]
f.lt(-20, X3)
f.retta((X3, 215), (X3, -215), "nero", 1.2); f.retta((X3, 0), (590, 0), "nero", 1.2)
f.traccia((0, 0), (X3, 180)); f.testo((X3 - 60, 150), "t_2α", -40, 0)
f.traccia((0, 0), (X3, -162)); f.testo((X3 - 60, -135), "t_1α", -36, 20)
f.traccia((X3, 180), (X3 + 162, 0)); f.testo((X3 + 100, 70), "t_3α", 8, 0)
arco(f, X3, 162)
# orizzontale o per A e B
for p, q, nome, col in [(A, B, "o", "arancio"), (C, None, "o'", "verde")]:
    xT = p[0] - p[1] / 0.45          # dove o1 incontra la LT
    xe = (q or p)[0] + 40
    f.retta((xT, 0), (xe, -(p[1] + (xe - p[0]) * 0.45)), col, 1.4)
    f.richiamo(xT, 0, p[2])
    f.retta((xT, p[2]), (xe, p[2]), col, 1.4)
    f.punto((xT, p[2]), f"T_{{2{nome}}}", -34, -6, col)
    f.punto((xT, 0), None, colore=col)
    f.testo((xe, p[2]), nome + "₂", 4, -4, col)
    f.testo((xe, -(p[1] + (xe - p[0]) * 0.45)), nome + "₁", 4, 12, col)
f.figura([P1(A), P1(B), P1(C)], "blu"); f.figura([P2(A), P2(B), P2(C)], "blu")
f.figura([P3(A, X3), P3(B, X3), P3(C, X3)], "blu")
for p, nome in [(A, "A"), (B, "B"), (C, "C")]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.retta(P1(p), (X3, -p[1]), "grigio", 0.8)
    arco(f, X3, p[1])
    f.richiamo(X3 + p[1], 0, p[2])
    f.retta(P2(p), P3(p, X3), "grigio", 0.8)
lab = {"A": ((-24, 14), (-24, -4), (-6, 18)), "B": ((6, 14), (6, -6), (8, 14)), "C": ((8, 4), (8, -6), (4, -8))}
for p, nome in [(A, "A"), (B, "B"), (C, "C")]:
    (a1, a2, a3) = lab[nome]
    f.punto(P1(p), nome + "₁", *a1, "blu"); f.punto(P2(p), nome + "₂", *a2, "blu"); f.punto(P3(p, X3), nome + "₃", *a3, "blu")
f.nota(16, 432, "A₁B₁ è parallelo a t₁α: AB sta su un'orizzontale o. Per C si traccia un'altra orizzontale o'.")
f.salva(BZ + "b05-proposto-falda-seconda-e-terza.svg")
print("ok")
