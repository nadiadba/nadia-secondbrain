"""Schemi aggiunti alla sbobina del 15 ottobre dopo il confronto con il quaderno di Marta:
tre costruzioni sul foglio e le viste nello spazio (triedro) come alla lavagna."""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, P1, P2, piano, direzione

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def piano_per(p, d1, d2):
    """Piano per il punto p con le direzioni d1 e d2: (n, d)."""
    q = tuple(p[i] + d1[i] for i in range(3)); r = tuple(p[i] + d2[i] for i in range(3))
    return piano(p, q, r)


def P3(p, X3):
    """Terza proiezione dopo il ribaltamento di pi3: a destra dell'asse, a distanza pari all'aggetto."""
    return (X3 + p[1], p[2])


def arco(f, X3, y, colore="grigio"):
    """Arco di richiamo da P1 (sotto LT) a P3 (sulla LT), centro nell'incrocio LT/asse."""
    cx, cy = f._s((X3, 0))
    f.parti.append(f'<path d="M {cx:.1f} {cy + y:.1f} A {y:.1f} {y:.1f} 0 0 0 {cx + y:.1f} {cy:.1f}" '
                   f'fill="none" stroke="#8a8a8a" stroke-width="0.9" stroke-dasharray="3,3"/>')


# ===================== sul foglio =====================

# 1. Quadrato ABCD in un piano parallelo alla linea di terra (y + z = 160) -----------
X3 = 420
A, B = (140, 120, 40), (260, 120, 40)
C, D = (140, 120 - 85, 40 + 85), (260, 120 - 85, 40 + 85)
f = Figura(680, 420, 200, "Quadrato ABCD in un piano α parallelo alla linea di terra (dal quaderno di Marta)", x0=30)
f.lt(-10, X3); f.retta((X3, 190), (X3, -190), "nero", 1.2)
f.retta((X3, 0), (640, 0), "nero", 1.2)
f.traccia((-10, 160), (X3, 160)); f.testo((-10, 160), "t_2α", 2, -8)
f.traccia((-10, -160), (X3, -160)); f.testo((-10, -160), "t_1α", 2, 18)
f.traccia((X3, 160), (X3 + 160, 0)); f.testo((X3 + 90, 80), "t_3α", 8, 0)
arco(f, X3, 160)
f.figura([P2(A), P2(B), P2(D), P2(C)], "blu"); f.figura([P1(A), P1(B), P1(D), P1(C)], "blu")
f.retta(P3(A, X3), P3(C, X3), "blu", 3)
for p, nome in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.retta(P2(p), (P3(p, X3)[0], P2(p)[1]), "grigio", 0.9)
for p, nome, dx in [(A, "A", -24), (C, "C", -24)]:
    f.punto(P2(p), nome + "₂", dx, 4); f.punto(P1(p), nome + "₁", dx, 4)
for p, nome in [(B, "B"), (D, "D")]:
    f.punto(P2(p), nome + "₂", 6, 4); f.punto(P1(p), nome + "₁", 6, 4)
arco(f, X3, A[1]); arco(f, X3, C[1])
f.punto(P3(A, X3), "A₃ ≡ B₃", 8, 14); f.punto(P3(C, X3), "C₃ ≡ D₃", 8, -6)
f.nota(20, 412, "Piano parallelo alla LT: t₁α ∥ LT, t₂α ∥ LT; in terza proiezione il quadrato è un segmento su t₃α.")
f.salva(OUT + "04-quadrato-piano-parallelo-alla-lt.svg")

# 2. Retta parallela alla LT nel piano orizzontale ----------------------------------
f = Figura(560, 300, 150, "Retta r parallela alla LT: anche il piano orizzontale la contiene (dal quaderno di Marta)", x0=30)
f.lt(-10, 500)
f.traccia((-10, 90), (500, 90)); f.retta((60, 90), (440, 90), "rosso", 2.2)
f.testo((500, 90), "t_2α ≡ r₂", -70, -8)
f.retta((60, -70), (440, -70), "rosso"); f.testo((440, -70), "r₁", 6, 4, "rosso")
f.testo((300, -125), "t_1α∞", 0, 0)
f.richiamo(250, 90, -70); f.punto((250, 90), "P₂", 4, -8, "rosso"); f.punto((250, -70), "P₁", 6, 16, "rosso")
f.nota(20, 290, "Piano orizzontale α: la seconda traccia è parallela alla LT e coincide con r₂; la prima traccia è all'infinito.")
f.salva(OUT + "04-retta-parallela-alla-lt-piano-orizzontale.svg")

# 3. Esercizio p. 9: disegnare P in alfa dimostrando che P appartiene a r di alfa -------
f = Figura(560, 360, 175, "Esercizio: P ∈ α, dimostrando che P ∈ r ⊂ α (α proiettante in prima)", x0=30)
f.lt(-10, 500)
K = (120, 0)
d1 = direzione(K, (430, -150))
f.traccia(K, (120, 165)); f.testo((120, 165), "t_2α", 6, 6)
f.traccia(K, (430, -150)); f.testo((430, -150), "t_1α", 4, 14)
f.angolo_retto(K, (1, 0), (0, 1))
lam = 200
P1p = (K[0] + d1[0] * lam, d1[1] * lam)
P2p = (P1p[0], 110)
# retta r proiettante in prima per P: r2 verticale, r1 puntiforme su t1alfa
f.retta((P1p[0], 0), (P1p[0], 160), "rosso", 2); f.testo((P1p[0], 160), "r₂", 6, 4, "rosso")
f.testo((P1p[0], 160), "T_{2r}∞", 6, 22, "rosso")
f.richiamo(P1p[0], 0, P1p[1])
f.punto(P1p, "r₁ ≡ T_{1r} ≡ P₁", -150, 4, "rosso")
f.punto(P2p, "P₂", 6, -6, "rosso")
# orizzontale o per P: o2 parallela alla LT, T2o su t2alfa; o1 coincide con t1alfa
f.retta((K[0], 110), (P2p[0] + 80, 110), "arancio"); f.testo((P2p[0] + 80, 110), "o₂", 4, 4, "arancio")
f.punto((K[0], 110), "T_{2o}", -40, -4)
f.testo((400, -138), "o₁ ≡ t₁α", -40, -14, "arancio")
f.nota(20, 352, "T₁ᵣ sta su t₁α, quindi r ⊂ α; P sta su r, quindi P ∈ α. Lo conferma l'orizzontale o: T₂ₒ sta su t₂α.")
f.salva(OUT + "04-esercizio-punto-nel-piano-proiettante.svg")

# ===================== nello spazio =====================

def triedro(titolo, h=430, w=600):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, (262, 190), X3=400, U=360, Y=230, Z=220, scala=0.75)
    t.piani()
    return f, t


# 4. Retta generica e le sue tracce
f, t = triedro("Nello spazio: la retta generica r e le sue tracce")
T1, T2 = (250, 200, 0), (120, 0, 200)
d = tuple(T2[i] - T1[i] for i in range(3))
t.segmento(T1, T2, "rosso", 2.4)
fuori = tuple(T2[i] + d[i] * 0.35 for i in range(3)); dentro = tuple(T1[i] - d[i] * 0.25 for i in range(3))
t.segmento(T2, fuori, "rosso", 1.4, "5,4"); t.segmento(T1, dentro, "rosso", 1.4, "5,4")
t.segmento(T1, (T2[0], 0, 0), "rosso", 1.4); t.testo(((T1[0] + T2[0]) / 2, T1[1] / 2, 0), "r₁", 2, 16, "rosso")
t.segmento((T1[0], 0, 0), T2, "rosso", 1.4); t.testo(((T1[0] + T2[0]) / 2, 0, T2[2] / 2), "r₂", -18, -6, "rosso")
t.richiamo(T2, (T2[0], 0, 0)); t.richiamo(T1, (T1[0], 0, 0))
t.punto(T1, "T_{1r}", 8, 14); t.punto(T2, "T_{2r}", 6, -8)
t.punto((T1[0], 0, 0), "(T_{1r})₂", -66, -6); t.punto((T2[0], 0, 0), "(T_{2r})₁", 4, 18)
t.testo(T1, "r", 10, 4, "rosso", 16)
f.nota(16, 420, "r buca π₁ in T₁ᵣ e π₂ in T₂ᵣ; la terza traccia è fuori dal triedro.")
f.salva(OUT + "04-spazio-retta-generica.svg")

# 5. Piano generico: il triangolo delle tracce e un'orizzontale
f, t = triedro("Nello spazio: il piano generico α e il triangolo delle tracce")
Ax, By, Cz = 130, 200, 190
n, dd = piano((Ax, 0, 0), (400, By, 0), (400, 0, Cz))
t.piano(n, dd, "blu", 0.18)
t.tracce(n, dd, "nero", "α")
h = 95   # orizzontale a quota h
o_a = ((dd - n[2] * h) / n[0], 0, h)              # su t2 (y=0)
o_b = (400, (dd - n[0] * 400 - n[2] * h) / n[1], h)  # su t3 (x=400)
t.segmento(o_a, o_b, "arancio", 2.2); t.testo(o_b, "o", -14, -8, "arancio")
o1a, o1b = (o_a[0], 0, 0), (400, o_b[1], 0)
t.segmento(o1a, o1b, "arancio", 1.2, "6,4"); t.testo(o1b, "o₁ ∥ t₁α", -10, 18, "arancio")
t.richiamo(o_a, o1a); t.richiamo(o_b, o1b)
t.punto(o_a, "T_{2o}", -40, -6)
f.nota(16, 420, "Le tre tracce formano un triangolo; l'orizzontale o ha o₁ parallela a t₁α.")
f.salva(OUT + "04-spazio-piano-generico.svg")

# 6. Piani che contengono una retta proiettante in prima
f, t = triedro("Nello spazio: i piani che contengono la retta r proiettante in prima")
R = (250, 120, 0)
for (nn, d_), col in [(piano_per(R, (1, 0, 0), (0, 0, 1)), "verde"), (piano_per(R, (0, 1, 0), (0, 0, 1)), "viola"),
                      (piano_per(R, (1, -0.9, 0), (0, 0, 1)), "blu")]:
    t.piano(nn, d_, col, 0.08); t.tracce(nn, d_, col)
t.segmento(R, (R[0], R[1], 210), "rosso", 2.6); t.testo((R[0], R[1], 210), "r", 6, 0, "rosso", 16)
t.punto(R, "T_{1r}", 8, 16)
f.nota(16, 420, "verde: α frontale · viola: γ di profilo · blu: β proiettante in prima")
f.salva(OUT + "04-spazio-piani-retta-proiettante-in-prima.svg")

# 7. Piani che contengono una retta orizzontale
f, t = triedro("Nello spazio: i piani che contengono la retta orizzontale o")
O = (180, 60, 110); do = (1, 0.55, 0)
for (nn, d_), col in [(piano_per(O, do, (0, 1, 0)), "verde"), (piano_per(O, do, (0, 0, 1)), "viola"),
                      (piano_per(O, do, (-0.2, 0.6, -1)), "blu")]:
    t.piano(nn, d_, col, 0.08); t.tracce(nn, d_, col)
oa = (O[0] - 40, O[1] - 22, O[2]); ob = (400, O[1] + (400 - O[0]) * 0.55, O[2])
t.segmento(oa, ob, "arancio", 2.6); t.testo(ob, "o", 6, -4, "arancio", 16)
f.nota(16, 420, "verde: α orizzontale · viola: γ proiettante in prima · blu: β generico")
f.salva(OUT + "04-spazio-piani-retta-orizzontale.svg")

# 8. Piani che contengono una retta frontale
f, t = triedro("Nello spazio: i piani che contengono la retta frontale f")
F = (170, 90, 20); dfr = (1, 0, 0.75)
for (nn, d_), col in [(piano_per(F, dfr, (1, 0, 0)), "verde"), (piano_per(F, dfr, (0, 1, 0)), "viola"),
                      (piano_per(F, dfr, (0.3, 1, -0.6)), "blu")]:
    t.piano(nn, d_, col, 0.08); t.tracce(nn, d_, col)
fb = (400, F[1], F[2] + (400 - F[0]) * 0.75)
t.segmento(F, fb, "verde", 2.6); t.testo(fb, "f", 6, -4, "verde", 16)
f.nota(16, 420, "verde: β frontale · viola: γ proiettante in seconda · blu: α generico")
f.salva(OUT + "04-spazio-piani-retta-frontale.svg")

# 9. Piani che contengono una retta di profilo
f, t = triedro("Nello spazio: i piani che contengono la retta di profilo m")
M = (300, 30, 180); dm = (0, 1, -0.9)
for (nn, d_), col in [(piano_per(M, dm, (0, 0, 1)), "viola"), (piano_per(M, dm, (1, 0, 0)), "verde"),
                      (piano_per(M, dm, (1, 0.2, 0.5)), "blu")]:
    t.piano(nn, d_, col, 0.08); t.tracce(nn, d_, col)
mb = (300, 30 + 200, 0)
t.segmento(M, mb, "rosso", 2.6); t.testo(M, "m", 6, -2, "rosso", 16)
f.nota(16, 420, "viola: piano di profilo · verde: piano parallelo alla LT · blu: piano generico")
f.salva(OUT + "04-spazio-piani-retta-di-profilo.svg")

# 10. Piano proiettante in seconda con il triangolo ABC
f, t = triedro("Nello spazio: il piano α proiettante in seconda e il triangolo ABC")
nn, d_ = piano_per((100, 0, 0), (1, 0, 0.75), (0, 1, 0))
t.piano(nn, d_, "blu", 0.15); t.tracce(nn, d_, "nero", "α")
Aa, Bb, Cc = (200, 50, 75), (200, 170, 75), (290, 100, 142.5)
f.parti.append("")  # separatore
t._poligono([Aa, Bb, Cc], "rosso", 0.25, "rosso")
for p, nome in [(Aa, "A"), (Bb, "B"), (Cc, "C")]:
    t.punto(p, nome, 6, -4, "rosso")
    t.richiamo(p, (p[0], 0, p[2]))
t.punto((200, 0, 75), "A₂ ≡ B₂", -62, -4)
f.nota(16, 420, "Tutto ciò che sta su α finisce in seconda proiezione su t₂α: A₂ ≡ B₂.")
f.salva(OUT + "04-spazio-piano-proiettante-in-seconda.svg")
print("ok")
