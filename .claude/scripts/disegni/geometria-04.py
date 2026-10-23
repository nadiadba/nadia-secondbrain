"""Schemi per la sbobina di geometria descrittiva del 13 ottobre (04-...):
le rette particolari e i piani particolari nel metodo di Monge, il piano proiettante in prima,
l'esercizio della figura nel piano parallelo alla LT e la correzione dell'esercizio guidato di omologia.

Usa disegni_monge.py senza modificarlo. Terza proiezione: pi3 a destra della verticale x = X3;
un punto (x, aggetto, quota) ha P3 = (X3 + aggetto, quota); il primo piano si porta sul terzo
con archi di richiamo centrati nell'incrocio tra LT e verticale.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, piano, interseca, direzione, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


# ---------------------------------------------------------------- utilita'

def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def P1(p):
    return (p[0], -p[1])


def P2(p):
    return (p[0], p[2])


def P3(p, X3):
    return (X3 + p[1], p[2])


def arco(f, X3, y):
    """Arco di richiamo dal punto (X3, -y) del primo piano al punto (X3 + y, 0) del terzo."""
    if y <= 0:
        return
    sx, sy = f._s((X3, -y))
    ex, ey = f._s((X3 + y, 0))
    f.parti.append(f'<path d="M {sx:.1f} {sy:.1f} A {y:.1f} {y:.1f} 0 0 0 {ex:.1f} {ey:.1f}" '
                   f'fill="none" stroke="{COLORI["grigio"]}" stroke-width="0.9" stroke-dasharray="3,3"/>')


def orizz(f, x1, x2, y):
    """Richiamo orizzontale."""
    f._linea((x1, y), (x2, y), "grigio", 0.9, "3,3")


def foglio(titolo, X3, alto, basso, w=660, xfine=None):
    """Foglio con LT, verticale pi2/pi3 e nomi dei piani; restituisce la figura."""
    f = Figura(w, alto + basso + 46, alto + 10, titolo, x0=30)
    xfine = xfine if xfine is not None else w - 50
    f.lt(-10, xfine)
    f._linea((X3, alto), (X3, -basso), "nero", 1.2)
    f.testo((-10, alto), "π_2", 4, 12, "grigio", 13, False)
    f.testo((-10, -basso), "π_1", 4, -2, "grigio", 13, False)
    f.testo((X3, alto), "π_3", 8, 12, "grigio", 13, False)
    f.testo((xfine, -basso), "π₁ ≡ π₂ ≡ π₃", -96, -2, "grigio", 12, False)
    return f


def infinito(f, p, d, nome, colore, dx=6, dy=4):
    """Traccia all'infinito: la scritta con una lineetta nella direzione della retta."""
    a = lungo(p, d, -10)
    b = lungo(p, d, 10)
    f._linea(a, b, colore, 1.4)
    f.testo(p, nome, dx, dy, colore, 13)


def piano_per(p, d1, d2):
    q = tuple(p[i] + d1[i] for i in range(3))
    r = tuple(p[i] + d2[i] for i in range(3))
    return piano(p, q, r)


def triedro(titolo, h=460, w=600):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, (262, 190), X3=400, U=360, Y=230, Z=220, scala=0.75)
    t.piani()
    return f, t


def proiezioni_spazio(t, a, b, colore):
    """Proiezioni di un segmento sui tre piani, nella vista nello spazio (linee sottili tratteggiate)."""
    t.segmento((a[0], a[1], 0), (b[0], b[1], 0), colore, 1.1, "5,4")
    t.segmento((a[0], 0, a[2]), (b[0], 0, b[2]), colore, 1.1, "5,4")
    t.segmento((400, a[1], a[2]), (400, b[1], b[2]), colore, 1.1, "5,4")


X3 = 380

# ================================================================ LE RETTE

# 1. Retta parallela alla linea di terra -----------------------------------------------
yr, zr = 60, 85.7          # aggetto e quota (stessi del piano alfa dello schema 9)
f = foglio("Retta r parallela alla LT (perpendicolare a π₃)", X3, 175, 165)
f.retta((40, zr), (X3, zr)); f.testo((40, zr), "r₂", -2, -8, "rosso")
f.retta((40, -yr), (X3, -yr)); f.testo((40, -yr), "r₁", -2, 18, "rosso")
f.punto((X3, -yr), "(T_{3r})₁", 6, 16)
f.punto((X3, zr), "(T_{3r})₂", -64, -8)
arco(f, X3, yr)
f.richiamo(X3 + yr, 0, zr)
f.punto((X3 + yr, zr), "r₃ ≡ T_{3r}", 8, -6, "rosso")
infinito(f, (90, -yr), (1, 0), "T_{1r}∞", "rosso", -20, 24)
infinito(f, (90, zr), (1, 0), "T_{2r}∞", "rosso", -20, -10)
f.nota(20, 380, "r₁ e r₂ sono parallele alla LT e partono dalla verticale; r₃ è un punto e coincide con la terza traccia.")
f.salva(OUT + "04-retta-parallela-alla-lt.svg")

# 2. Retta frontale ---------------------------------------------------------------------
yf, xf0, mf = 70, 120, 0.5
zf3 = mf * (X3 - xf0)
f = foglio("Retta frontale f (parallela a π₂)", X3, 175, 165)
f.retta((xf0, -yf), (X3, -yf), "verde"); f.testo((220, -yf), "f₁", 0, 18, "verde")
f.retta((xf0, 0), (X3, zf3), "verde"); f.testo((250, mf * 130), "f₂", -18, -8, "verde")
f.retta((X3 + yf, 0), (X3 + yf, zf3), "verde"); f.testo((X3 + yf, zf3 / 2), "f₃", 6, 0, "verde")
f.richiamo(xf0, 0, -yf)
arco(f, X3, yf)
orizz(f, X3, X3 + yf, zf3)
f.punto((xf0, -yf), "T_{1f}", -46, 6)
f.punto((xf0, 0), "(T_{1f})₂", -66, -6)
f.punto((X3 + yf, 0), "(T_{1f})₃", 6, 16)
f.punto((X3, -yf), "(T_{3f})₁", 6, 16)
f.punto((X3, zf3), "(T_{3f})₂", -66, -6)
f.punto((X3 + yf, zf3), "T_{3f}", 8, -4)
infinito(f, (90, 130), direzione((0, 0), (1, mf)), "T_{2f}∞", "verde", 8, 4)
f.nota(20, 380, "f₁ è parallela alla LT; f₂ ha l'inclinazione vera della retta; f₃ è verticale. T₂f è all'infinito.")
f.salva(OUT + "04-retta-frontale.svg")

# 3. Retta orizzontale ------------------------------------------------------------------
h, xo0, ko = 90, 120, 0.45
yo3 = ko * (X3 - xo0)
f = foglio("Retta orizzontale o (parallela a π₁)", X3, 175, 165)
f.retta((xo0, h), (X3, h), "arancio"); f.testo((230, h), "o₂", 0, -8, "arancio")
f.retta((xo0, 0), (X3, -yo3), "arancio"); f.testo((250, -ko * 130), "o₁", 8, 10, "arancio")
f.retta((X3, h), (X3 + yo3, h), "arancio"); f.testo((X3 + yo3 / 2, h), "o₃", -4, -8, "arancio")
f.richiamo(xo0, h, 0)
arco(f, X3, yo3)
f.richiamo(X3 + yo3, 0, h)
f.punto((xo0, h), "T_{2o}", -48, -6)
f.punto((xo0, 0), "(T_{2o})₁", -66, 16)
f.punto((X3, h), "(T_{2o})₃", -66, -8)
f.punto((X3, -yo3), "(T_{3o})₁", 8, 6)
f.punto((X3 + yo3, h), "T_{3o}", 6, -6)
infinito(f, (90, -120), direzione((0, 0), (1, -ko)), "T_{1o}∞", "arancio", 8, 4)
f.nota(20, 380, "o₂ è parallela alla LT (le due tracce proprie hanno la stessa quota); o₁ ha l'inclinazione vera; T₁ₒ è all'infinito.")
f.salva(OUT + "04-retta-orizzontale.svg")

# 4. Retta di profilo -------------------------------------------------------------------
xp, yp1, zp2 = 220, 110, 120
f = foglio("Retta r di profilo (parallela a π₃)", X3, 175, 165)
f.retta((xp, zp2), (xp, -yp1), "viola", 2)
f.testo((xp, 40), "r₂", 6, 0, "viola"); f.testo((xp, -60), "r₁", -22, 0, "viola")
arco(f, X3, yp1)
orizz(f, xp, X3, -yp1)
orizz(f, xp, X3, zp2)
f.retta((X3 + yp1, 0), (X3, zp2), "viola"); f.testo((X3 + yp1 / 2, zp2 / 2), "r₃", 6, -2, "viola")
f.punto((xp, zp2), "T_{2r}", -48, -4)
f.punto((xp, -yp1), "T_{1r}", -48, 6)
f.punto((xp, 0), "(T_{1r})₂ ≡ (T_{2r})₁", 8, 16)
f.punto((X3, zp2), "(T_{2r})₃", 6, -8)
f.punto((X3 + yp1, 0), "(T_{1r})₃", 6, 16)
f.punto((X3, -yp1), None)
f.testo((X3 + 70, 140), "T_{3r}∞", 0, 0, "viola", 13)
f.nota(20, 380, "r₁ e r₂ stanno sulla stessa perpendicolare alla LT: la retta si vede davvero solo in terza proiezione.")
f.salva(OUT + "04-retta-di-profilo.svg")

# ---- le stesse rette nello spazio
# 5. parallela alla LT
f, t = triedro("Nello spazio: la retta r parallela alla LT")
R = (60, 80, 110)
R3 = (400, 80, 110)
t.segmento(R, R3, "rosso", 2.6); t.testo(R, "r", -14, -4, "rosso", 16)
proiezioni_spazio(t, R, R3, "rosso")
t.richiamo(R3, (400, 80, 0)); t.richiamo(R3, (400, 0, 110))
t.punto(R3, "T_{3r}", 8, -6, "rosso")
t.testo((150, 80, 0), "r₁", 0, 16, "rosso"); t.testo((150, 0, 110), "r₂", 0, -6, "rosso")
f.nota(16, 452, "r è parallela a π₁ e a π₂ (quindi alla LT) e perpendicolare a π₃, che buca in T₃ᵣ.")
f.salva(OUT + "04-spazio-retta-parallela-alla-lt.svg")

# 6. frontale
f, t = triedro("Nello spazio: la retta frontale f")
A, B = (200, 150, 0), (400, 150, 160)
t.segmento(A, B, "verde", 2.6); t.testo((300, 150, 80), "f", -16, -4, "verde", 16)
proiezioni_spazio(t, A, B, "verde")
t.richiamo(A, (200, 0, 0)); t.richiamo(B, (400, 0, 160)); t.richiamo(B, (400, 150, 0))
t.punto(A, "T_{1f}", 6, 16, "verde"); t.punto(B, "T_{3f}", 8, -4, "verde")
t.testo((300, 0, 80), "f₂", -18, -8, "verde"); t.testo((300, 150, 0), "f₁", 0, 18, "verde")
f.nota(16, 452, "f è parallela a π₂: buca π₁ in T₁f e π₃ in T₃f; la seconda traccia è all'infinito.")
f.salva(OUT + "04-spazio-retta-frontale.svg")

# 7. orizzontale
f, t = triedro("Nello spazio: la retta orizzontale o")
A, B = (160, 0, 120), (400, 160, 120)
t.segmento(A, B, "arancio", 2.6); t.testo(((A[0] + B[0]) / 2, 80, 120), "o", -6, -10, "arancio", 16)
proiezioni_spazio(t, A, B, "arancio")
t.richiamo(A, (160, 0, 0)); t.richiamo(B, (400, 160, 0)); t.richiamo(B, (400, 0, 120))
t.punto(A, "T_{2o}", -44, -6, "arancio"); t.punto(B, "T_{3o}", 8, -4, "arancio")
t.testo((280, 80, 0), "o₁", 4, 18, "arancio")
f.nota(16, 452, "o è parallela a π₁: T₂ₒ e T₃ₒ hanno la stessa quota; la prima traccia è all'infinito.")
f.salva(OUT + "04-spazio-retta-orizzontale.svg")

# 8. di profilo
f, t = triedro("Nello spazio: la retta r di profilo")
A, B = (260, 0, 170), (260, 200, 0)
t.segmento(A, B, "viola", 2.6); t.testo((260, 100, 85), "r", 8, -6, "viola", 16)
proiezioni_spazio(t, A, B, "viola")
t.richiamo(A, (260, 0, 0))
t.punto(A, "T_{2r}", -46, -6, "viola"); t.punto(B, "T_{1r}", 8, 14, "viola")
t.testo((400, 100, 85), "r₃", 6, 0, "viola")
f.nota(16, 452, "r è parallela a π₃: r₁ e r₂ sono perpendicolari alla LT; solo r₃ mostra la retta com'è.")
f.salva(OUT + "04-spazio-retta-di-profilo.svg")

# ================================================================ I PIANI

# 9. Piano alfa parallelo alla LT per la retta r (y/140 + z/150 = 1) --------------------
Y0, Z0 = 140, 150
f = foglio("Piano α parallelo alla LT che contiene la retta r", X3, 175, 165)
f.traccia((-5, Z0), (X3, Z0)); f.testo((200, Z0), "t_2α", 0, -8)
f.traccia((-5, -Y0), (X3, -Y0)); f.testo((200, -Y0), "t_1α", 0, 20)
arco(f, X3, Y0)
f.traccia((X3, Z0), (X3 + Y0, 0)); f.testo((X3 + Y0 * 0.75, Z0 * 0.25), "t_3α", 8, 0)
f.retta((40, zr), (X3, zr)); f.testo((40, zr), "r₂", -2, -8, "rosso")
f.retta((40, -yr), (X3, -yr)); f.testo((40, -yr), "r₁", -2, 18, "rosso")
arco(f, X3, yr)
f.richiamo(X3 + yr, 0, zr)
f.punto((X3 + yr, zr), "T_{3r}", -46, -6, "rosso")
f.nota(20, 380, "t₁α e t₂α sono parallele alla LT, t₃α è inclinata; r appartiene ad α perché T₃ᵣ sta su t₃α.")
f.salva(OUT + "04-piano-parallelo-alla-lt.svg")

# 10. Piano frontale beta per la frontale f -------------------------------------------
f = foglio("Piano frontale β che contiene la retta frontale f", X3, 175, 165)
f.traccia((-5, -yf), (X3, -yf)); f.testo((-5, -yf), "t_1β ≡ f₁", 4, 18)
f.retta((xf0, -yf), (X3, -yf), "verde", 1.4)
f.traccia((X3 + yf, 0), (X3 + yf, 165)); f.testo((X3 + yf, 165), "t_3β", 8, 10)
f.retta((X3 + yf, 0), (X3 + yf, zf3), "verde", 1.4)
f.retta((xf0, 0), (X3, zf3), "verde"); f.testo((250, mf * 130), "f₂", -18, -8, "verde")
f.richiamo(xf0, 0, -yf)
arco(f, X3, yf)
orizz(f, X3, X3 + yf, zf3)
f.punto((xf0, -yf), "T_{1f}", -14, 20, "verde")
f.punto((X3 + yf, zf3), "T_{3f}", 8, 6, "verde")
f.testo((130, 140), "t_2β∞", 0, 0, "nero", 13)
f.nota(20, 380, "β è parallelo a π₂: t₁β (parallela alla LT) dà l'aggetto, t₃β è verticale, t₂β è all'infinito.")
f.salva(OUT + "04-piano-frontale.svg")

# 11. Piano orizzontale gamma per l'orizzontale o ------------------------------------
f = foglio("Piano orizzontale γ che contiene la retta orizzontale o", X3, 175, 165)
f.traccia((-5, h), (X3, h)); f.testo((-5, h), "t_2γ ≡ o₂", 4, -12)
f.retta((xo0, h), (X3, h), "arancio", 1.4)
f.traccia((X3, h), (X3 + 220, h)); f.testo((X3 + 220, h), "t_3γ", -36, -8)
f.retta((X3, h), (X3 + yo3, h), "arancio", 1.4)
f.retta((xo0, 0), (X3, -yo3), "arancio"); f.testo((250, -ko * 130), "o₁", 8, 10, "arancio")
f.richiamo(xo0, h, 0)
arco(f, X3, yo3)
f.richiamo(X3 + yo3, 0, h)
f.punto((xo0, h), "T_{2o}", -16, 20, "arancio")
f.punto((X3 + yo3, h), "T_{3o}", 4, 20, "arancio")
f.testo((60, -140), "t_1γ∞", 0, 0, "nero", 13)
f.nota(20, 380, "γ è parallelo a π₁: t₂γ e t₃γ sono sulla stessa orizzontale, t₁γ è all'infinito.")
f.salva(OUT + "04-piano-orizzontale.svg")

# 12. Piano di profilo delta per la retta di profilo --------------------------------
f = foglio("Piano di profilo δ che contiene la retta r di profilo", X3, 175, 165)
f.traccia((xp, 0), (xp, 165)); f.testo((xp, 165), "t_2δ", 8, 10)
f.traccia((xp, 0), (xp, -160)); f.testo((xp, -160), "t_1δ", 8, 4)
f.retta((xp, zp2), (xp, -yp1), "viola", 1.4)
f.testo((xp, 40), "≡ r₂", 8, 0, "viola"); f.testo((xp, -40), "≡ r₁", 8, 0, "viola")
f.angolo_retto((xp, 0), (1, 0), (0, 1)); f.angolo_retto((xp, 0), (-1, 0), (0, -1))
arco(f, X3, yp1)
orizz(f, xp, X3, -yp1)
orizz(f, xp, X3, zp2)
f.retta((X3 + yp1, 0), (X3, zp2), "viola"); f.testo((X3 + yp1 / 2, zp2 / 2), "r₃", 6, -2, "viola")
f.punto((xp, zp2), "T_{2r}", -48, -4, "viola")
f.punto((xp, -yp1), "T_{1r}", -48, 6, "viola")
f.testo((X3 + 120, 140), "t_3δ∞", 0, 0, "nero", 13)
f.nota(20, 380, "δ è parallelo a π₃: t₁δ e t₂δ sono perpendicolari alla LT, t₃δ è all'infinito.")
f.salva(OUT + "04-piano-di-profilo.svg")

# ---- i piani nello spazio
# 13. parallelo alla LT
f, t = triedro("Nello spazio: il piano α parallelo alla LT e la retta r")
n, d = piano_per((0, 180, 0), (1, 0, 0), (0, -180, 160))
t.piano(n, d, "blu", 0.16); t.tracce(n, d, "nero", "α")
R, R3 = (60, 80, 160 * 100 / 180), (400, 80, 160 * 100 / 180)
t.segmento(R, R3, "rosso", 2.4); t.testo(R, "r", -14, -4, "rosso", 16)
t.punto(R3, "T_{3r}", -50, 4, "rosso")
f.nota(16, 452, "α taglia tutti e tre i piani di proiezione: t₁α e t₂α sono parallele alla LT; r sta su α.")
f.salva(OUT + "04-spazio-piano-parallelo-alla-lt.svg")

# 14. frontale
f, t = triedro("Nello spazio: il piano frontale β e la retta frontale f")
n, d = piano_per((0, 150, 0), (1, 0, 0), (0, 0, 1))
t.piano(n, d, "verde", 0.14); t.tracce(n, d, "nero", "β")
A, B = (200, 150, 0), (400, 150, 160)
t.segmento(A, B, "verde", 2.6); t.testo((300, 150, 80), "f", -16, -4, "verde", 16)
t.punto(A, "T_{1f}", 6, 16, "verde"); t.punto(B, "T_{3f}", 8, 12, "verde")
f.nota(16, 452, "β è parallelo a π₂: ha la prima e la terza traccia; la seconda è all'infinito.")
f.salva(OUT + "04-spazio-piano-frontale.svg")

# 15. orizzontale
f, t = triedro("Nello spazio: il piano orizzontale γ e la retta orizzontale o")
n, d = piano_per((0, 0, 120), (1, 0, 0), (0, 1, 0))
t.piano(n, d, "arancio", 0.14); t.tracce(n, d, "nero", "γ")
A, B = (160, 0, 120), (400, 160, 120)
t.segmento(A, B, "arancio", 2.6); t.testo((280, 80, 120), "o", -6, -10, "arancio", 16)
t.punto(A, "T_{2o}", -40, 16, "arancio"); t.punto(B, "T_{3o}", 8, 14, "arancio")
f.nota(16, 452, "γ è parallelo a π₁: ha la seconda e la terza traccia; la prima è all'infinito.")
f.salva(OUT + "04-spazio-piano-orizzontale.svg")

# 16. di profilo
f, t = triedro("Nello spazio: il piano di profilo δ e la retta r di profilo")
n, d = piano_per((260, 0, 0), (0, 1, 0), (0, 0, 1))
t.piano(n, d, "viola", 0.14); t.tracce(n, d, "nero", "δ")
A, B = (260, 0, 170), (260, 200, 0)
t.segmento(A, B, "viola", 2.6); t.testo((260, 100, 85), "r", 8, -6, "viola", 16)
t.punto(A, "T_{2r}", -46, -6, "viola"); t.punto(B, "T_{1r}", 8, 14, "viola")
f.nota(16, 452, "δ è parallelo a π₃: ha la prima e la seconda traccia; la terza è all'infinito.")
f.salva(OUT + "04-spazio-piano-di-profilo.svg")

# 17. Piano proiettante in prima con un punto P e una retta verticale ----------------
K = (100, 0)
s1 = 0.5                                 # aggetto = s1 * (x - 100)
y0 = s1 * (X3 - K[0])                    # dove t1alfa incontra la verticale
xP = 240; Pp = (xP, s1 * (xP - K[0]), 80)
f = foglio("Piano α proiettante in prima e un punto P di α", X3, 175, 165)
f.traccia(K, (X3, -y0)); f.testo(((K[0] + X3) / 2, -y0 / 2), "t_1α", -30, 16)
f.traccia(K, (K[0], 165)); f.testo((K[0], 165), "t_2α", 8, 10)
f.angolo_retto(K, (1, 0), (0, 1))
arco(f, X3, y0)
f.traccia((X3 + y0, 0), (X3 + y0, 165)); f.testo((X3 + y0, 165), "t_3α", 8, 10)
# retta r proiettante in prima per P
f.retta((xP, 0), (xP, 160)); f.testo((xP, 150), "r₂", 6, 0, "rosso")
f.retta((X3 + Pp[1], 0), (X3 + Pp[1], 160)); f.testo((X3 + Pp[1], 150), "r₃", 6, 0, "rosso")
f.richiamo(xP, 0, -Pp[1])
arco(f, X3, Pp[1])
orizz(f, xP, X3 + Pp[1], Pp[2])
f.punto(P1(Pp), "P₁ ≡ r₁ ≡ T_{1r}", 12, -10, "rosso")
f.punto(P2(Pp), "P₂", -24, -8, "rosso")
f.punto(P3(Pp, X3), "P₃", 8, -8, "rosso")
f.nota(20, 380, "P₁ cade su t₁α: nei piani verticali è una coincidenza. La regola: P sta sulla retta r, e T₁ᵣ sta su t₁α.")
f.salva(OUT + "04-piano-proiettante-in-prima.svg")

# 18. nello spazio
f, t = triedro("Nello spazio: il piano α proiettante in prima e il punto P")
n, d = piano_per((100, 0, 0), (1, 0.9, 0), (0, 0, 1))
t.piano(n, d, "blu", 0.16); t.tracce(n, d, "nero", "α")
Q = (220, 108, 0); Pq = (220, 108, 110)
t.segmento(Q, (220, 108, 215), "rosso", 2.2); t.testo((220, 108, 215), "r", 6, 0, "rosso", 16)
t.punto(Pq, "P", 8, -4, "rosso")
t.punto(Q, "P₁ ≡ T_{1r}", 8, 16, "rosso")
f.nota(16, 452, "α è perpendicolare a π₁: visto dall'alto si riduce a una linea, la prima traccia t₁α.")
f.salva(OUT + "04-spazio-piano-proiettante-in-prima.svg")

# 19. Quadrato nel piano proiettante in prima: le tre proiezioni ---------------------
xa, xb, zb = 200, 280, 30
A = (xa, s1 * (xa - K[0]), zb); B = (xb, s1 * (xb - K[0]), zb)
lato = math.hypot(xb - xa, B[1] - A[1])
D = (xa, A[1], zb + lato); C = (xb, B[1], zb + lato)
f = foglio("Quadrato ABCD nel piano α proiettante in prima", X3, 175, 165)
f.traccia(K, (X3, -y0)); f.testo((X3, -y0), "t_1α", -40, 4)
f.traccia(K, (K[0], 165)); f.testo((K[0], 165), "t_2α", 8, 10)
arco(f, X3, y0)
f.traccia((X3 + y0, 0), (X3 + y0, 165)); f.testo((X3 + y0, 165), "t_3α", 8, 10)
for p in (A, B):
    f.richiamo(p[0], C[2], -p[1])
    arco(f, X3, p[1])
    f.richiamo(X3 + p[1], 0, C[2])
for z in (zb, C[2]):
    orizz(f, xb, X3 + B[1], z)
f.retta(P1(A), P1(B), "blu", 4)
f.figura([P2(A), P2(B), P2(C), P2(D)], "blu")
f.figura([P3(A, X3), P3(B, X3), P3(C, X3), P3(D, X3)], "blu")
f.punto(P1(A), "A₁ ≡ D₁", -62, 6); f.punto(P1(B), "B₁ ≡ C₁", 8, 14)
f.punto(P2(A), "A₂", -24, 14); f.punto(P2(B), "B₂", 6, 14)
f.punto(P2(D), "D₂", -24, -4); f.punto(P2(C), "C₂", 6, -4)
f.punto(P3(A, X3), "A₃", -22, 14); f.punto(P3(B, X3), "B₃", 6, 14)
f.punto(P3(D, X3), "D₃", -22, -4); f.punto(P3(C, X3), "C₃", 6, -4)
f.nota(20, 380, f"Il lato vero è lungo come A₁B₁: in seconda il quadrato è più stretto, in terza ancora di più.")
f.salva(OUT + "04-quadrato-piano-proiettante-in-prima.svg")

# 20. Esercizio: figura nel piano parallelo alla LT, terza proiezione ------------------
Y0, Z0 = 150, 120


def zq(y):
    return Z0 * (1 - y / Y0)


A = (130, 120, zq(120)); B = (270, 120, zq(120)); C = (130, 40, zq(40)); D = (270, 40, zq(40))
f = foglio("Esercizio: terza proiezione della figura ABCD. A che piano appartiene?", X3, 175, 165)
for p in (A, B, C, D):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
for p in (B, D):
    orizz(f, p[0], X3, -p[1])
    arco(f, X3, p[1])
    f.richiamo(X3 + p[1], 0, p[2])
    orizz(f, p[0], X3 + p[1], p[2])
f.figura([P1(A), P1(B), P1(D), P1(C)], "blu")
f.figura([P2(A), P2(B), P2(D), P2(C)], "blu")
f.traccia((X3, Z0), (X3 + Y0, 0)); f.testo((X3, Z0), "t_3α", 10, -4)
f.retta(P3(A, X3), P3(C, X3), "blu", 4)
f.punto(P1(A), "A₁", -24, 4); f.punto(P1(B), "B₁", 6, 4)
f.punto(P1(C), "C₁", -24, 4); f.punto(P1(D), "D₁", 6, 4)
f.punto(P2(A), "A₂", -24, 10); f.punto(P2(B), "B₂", 6, 10)
f.punto(P2(C), "C₂", -24, -2); f.punto(P2(D), "D₂", 6, -2)
f.punto(P3(A, X3), "A₃ ≡ B₃", -76, 16); f.punto(P3(C, X3), "C₃ ≡ D₃", 8, -6)
f.nota(20, 380, "La terza proiezione è un segmento: la figura sta in un piano α parallelo alla LT, e il segmento sta su t₃α.")
f.salva(OUT + "04-esercizio-figura-piano-parallelo-alla-lt.svg")

# ================================================================ OMOLOGIA
# coordinate prese dal foglio ES.GUIDATA_Omologia_01 (y verso il basso), poi ridimensionate


class Foglio:
    def __init__(self, w, h, titolo, ox, oy, k):
        self.f = Figura(w, h, 0, titolo)
        self.ox, self.oy, self.k = ox, oy, k

    def s(self, p):
        return ((p[0] - self.ox) * self.k + 20, (p[1] - self.oy) * self.k + 20)

    def linea(self, a, b, colore="nero", spessore=1.6, tratt=None):
        (x1, y1), (x2, y2) = self.s(a), self.s(b)
        dash = f' stroke-dasharray="{tratt}"' if tratt else ""
        self.f.parti.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                            f'stroke="{COLORI.get(colore, colore)}" stroke-width="{spessore}"{dash} stroke-linecap="round"/>')

    def punto(self, p, nome=None, dx=6, dy=-6, colore="nero"):
        x, y = self.s(p)
        self.f.parti.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{COLORI.get(colore, colore)}"/>')
        if nome:
            self.testo(p, nome, dx, dy, colore)

    def testo(self, p, nome, dx=6, dy=-6, colore="nero", dim=15):
        x, y = self.s(p)
        self.f.parti.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-family="Helvetica, Arial, sans-serif" '
                            f'font-size="{dim}" font-style="italic" fill="{COLORI.get(colore, colore)}">{nome}</text>')

    def poligono(self, pts, colore):
        c = COLORI.get(colore, colore)
        s = " ".join("{:.1f},{:.1f}".format(*self.s(p)) for p in pts)
        self.f.parti.append(f'<polygon points="{s}" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-width="1.8"/>')


def inter(a, b, c, d):
    return interseca(a, b, c, d)


def oltre(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


# 21. Esercizio 4: trovare s' (centro U proprio, asse improprio) ----------------------
U = (210, 580)
s_a, s_b = (130, 550), (245, 835)
r_a, r_b = (232, 670), (402, 588)
q_a, q_b = (252, 710), (422, 628)         # r'
O = Foglio(640, 560, "Correzione dell'esercizio: trovare la retta s' corrispondente di s", -20, 520, 1.25)
O.f.parti.append("")
O.linea(s_a, s_b, "nero", 2); O.testo(s_a, "s", -14, 10)
O.linea(r_a, r_b, "nero", 2); O.testo(r_b, "r", -8, -8)
O.linea(q_a, q_b, "nero", 2); O.testo(q_b, "r′", -8, -8)
P = inter(s_a, s_b, r_a, r_b)
O.linea(P, r_a, "nero", 1.2, "6,4")                       # r prolungata fino a s
Pp = inter(U, P, q_a, q_b)
O.linea(Pp, q_a, "nero", 1.2, "6,4")                      # r' prolungata
O.linea(U, oltre(U, Pp, 1.12), "grigio", 1.1, "4,3")       # raggio da U per P
ds = direzione(s_a, s_b)
O.linea(lungo(Pp, ds, -130), lungo(Pp, ds, 170), "rosso", 2.2)
O.testo(lungo(Pp, ds, 170), "s′", 6, 0, "rosso")
# verifica con un altro punto M di s: retta per M e per A di r, parallela per A'
M = oltre(s_a, s_b, 0.72)
Aq = oltre(r_a, r_b, 0.55)
Ap = inter(U, Aq, q_a, q_b)
O.linea(U, oltre(U, Ap, 1.1), "grigio", 1, "4,3")
O.linea(M, Aq, "blu", 1.2)
dm = direzione(M, Aq)
Mp = inter(U, M, Ap, lungo(Ap, dm, 10))
O.linea(Ap, Mp, "blu", 1.2)
O.linea(U, oltre(U, Mp, 1.06), "grigio", 1, "4,3")
O.punto(U, "U", 8, -6)
O.punto(P, "P", -18, -8); O.punto(Pp, "P′", -24, 16, "rosso")
O.punto(M, "M", -20, 4, "blu"); O.punto(Mp, "M′", 8, 12, "blu")
O.punto(Aq, "A", 2, -10, "blu"); O.punto(Ap, "A′", 6, 16, "blu")
O.testo((440, 820), "u∞", 4, 4, "nero")
O.linea((428, 814), (440, 826), "nero", 1.2); O.linea((428, 826), (440, 814), "nero", 1.2)
O.f.nota(20, 552, "L'asse è all'infinito: le rette corrispondenti sono parallele (r ∥ r′, s ∥ s′). In blu la verifica con il punto M.")
O.f.salva(OUT + "04-omologia-retta-corrispondente.svg")

# 22. Esercizio 6: la figura corrispondente (centro improprio, affinita') ---------------
Ou = (920, 860)                                        # r, r' e u si incontrano qui
u_b = (1280, 590)
r_b6 = (1260, 860)
q_b6 = (975, 540)
Lfig = [(1090, 860), (1065, 785), (1120, 740), (1175, 740)]
dU = direzione((0, 0), (-1, -1.25))                     # direzione del centro improprio
O = Foglio(640, 540, "Correzione dell'esercizio: la figura corrispondente (centro U∞, asse u)", 860, 500, 1.25)
O.linea((880, 890), u_b, "nero", 2); O.testo(u_b, "u", 4, 14)
O.linea(Ou, r_b6, "nero", 2); O.testo(r_b6, "r", -8, -8)
O.linea(Ou, oltre(Ou, q_b6, 1.05), "nero", 2); O.testo(oltre(Ou, q_b6, 1.05), "r′", 6, 6)
# il vertice A sta su r: A' su r' nella direzione del centro
Aa = Lfig[0]
Ap = inter(Aa, lungo(Aa, dU, 10), Ou, q_b6)
nomi = ["A", "B", "C", "D"]
img = [Ap]
O.linea(Aa, Ap, "grigio", 1, "4,3")
for i in (1, 3, 2):
    X = Lfig[i]
    prec = Lfig[0] if i in (1, 3) else Lfig[3]
    precp = img[0] if i in (1, 3) else img_D
    W = inter(prec, X, Ou, u_b)                          # punto unito sull'asse
    Xp = inter(W, precp, X, lungo(X, dU, 10))
    O.linea(X, W, "blu", 1, "6,4")
    O.linea(W, Xp, "rosso", 1, "6,4")
    O.linea(X, Xp, "grigio", 1, "4,3")
    O.punto(W, None)
    if i == 1:
        img_B = Xp
    if i == 3:
        img_D = Xp
    if i == 2:
        img_C = Xp
O.poligono(Lfig, "blu")
O.poligono([Ap, img_B, img_C, img_D], "rosso")
O.testo((1110, 800), "ℒ", 0, 0, "blu", 17)
for p, n, dx, dy in [(Lfig[0], "A", 4, 18), (Lfig[1], "B", -18, 6), (Lfig[2], "C", -6, -8), (Lfig[3], "D", 6, -4)]:
    O.punto(p, n, dx, dy, "blu")
for p, n, dx, dy in [(Ap, "A′", -26, 6), (img_B, "B′", -26, 6), (img_C, "C′", -10, -8), (img_D, "D′", 8, -4)]:
    O.punto(p, n, dx, dy, "rosso")
cx, cy = (1215, 560)
O.linea((cx, cy), lungo((cx, cy), dU, 40), "nero", 1.4)
O.testo(lungo((cx, cy), dU, 20), "U∞", 8, 0)
O.f.nota(20, 532, "I corrispondenti stanno sulle rette con la direzione di U∞; i lati corrispondenti si incontrano sull'asse u.")
O.f.salva(OUT + "04-omologia-figura-corrispondente.svg")
print("ok")
