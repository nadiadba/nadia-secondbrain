"""Schemi nuovi per la bozza di geometria descrittiva 04 (lezione del 13 ottobre) e due riquadri
aggiunti alla sbobina 04.

- per la sbobina (sbobine/img/04-...): il triedro disegnato come alla lavagna (pianta in vera forma,
  angolo retto alla base) e il piano frontale "che non e' una figura";
- per la bozza (bozze/img/b04-...): due disegni proposti (non fatti a lezione): le tracce del piano
  della figura ABCD (compito per casa) e un punto sulla retta di profilo trovato con la terza proiezione.

Usa disegni_monge.py senza modificarlo: la vista "come alla lavagna" e' una sottoclasse di Triedro
che cambia solo l'angolo degli assi (45 gradi, cosi' la pianta resta in vera forma).
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, piano, COLORI

GEO = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/"
OUT_SBOBINA = GEO + "sbobine/img/"
OUT_BOZZA = GEO + "bozze/img/"


# ---------------------------------------------------------------- utilita' (come in geometria-04.py)

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
    f._linea((x1, y), (x2, y), "grigio", 0.9, "3,3")


def foglio(titolo, X3, alto, basso, w=660, xfine=None):
    f = Figura(w, alto + basso + 46, alto + 10, titolo, x0=30)
    xfine = xfine if xfine is not None else w - 50
    f.lt(-10, xfine)
    f._linea((X3, alto), (X3, -basso), "nero", 1.2)
    f.testo((-10, alto), "π_2", 4, 12, "grigio", 13, False)
    f.testo((-10, -basso), "π_1", 4, -2, "grigio", 13, False)
    f.testo((X3, alto), "π_3", 8, 12, "grigio", 13, False)
    f.testo((xfine, -basso), "π₁ ≡ π₂ ≡ π₃", -96, -2, "grigio", 12, False)
    return f


def piano_per(p, d1, d2):
    q = tuple(p[i] + d1[i] for i in range(3))
    r = tuple(p[i] + d2[i] for i in range(3))
    return piano(p, q, r)


class TriedroLavagna(Triedro):
    """Il triedro come lo disegna la docente: pi1 in vera forma (angolo retto alla base),
    la LT che scende a sinistra e l'asse dell'aggetto che scende a destra, tutti e due a 45 gradi."""

    def _p(self, p):
        c = math.cos(math.radians(45))
        u = (self.X3 - p[0]) * self.k
        y, z = p[1] * self.k, p[2] * self.k
        return (self.o[0] - u * c + y * c, self.o[1] + u * c + y * c - z)


# ================================================================ PER LA SBOBINA

# 1. Il triedro come alla lavagna --------------------------------------------------------
f = Figura(560, 500, 0, "Il triedro come alla lavagna: π₁ in vera forma, angolo retto alla base")
t = TriedroLavagna(f, (260, 160), X3=400, U=360, Y=260, Z=220, scala=0.62)
t.piani(etichette=False)
t.testo((150, 150, 0), "π_1", 0, 0, "grigio", 16)
t.testo((200, 0, 150), "π_2", 0, 0, "grigio", 16)
t.testo((400, 140, 170), "π_3", 0, 0, "grigio", 16)
t.testo((40, 0, 0), "LT", -26, 4, "nero", 15)
# angolo retto tra la LT e lo spigolo pi1/pi3 (resta di 90 gradi perche' pi1 e' in vera forma)
a, b, c = t._p((385, 0, 0)), t._p((385, 15, 0)), t._p((400, 15, 0))
f.parti.append(f'<polyline points="{a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f}" '
               f'fill="none" stroke="#1f1f1f" stroke-width="1"/>')
t.testo((400, 0, 0), "90°", -10, 38, "nero", 13)
t.testo((400, 0, 220), "π₂ ∩ π₃", 6, 4, "grigio", 12)
t.testo((400, 260, 0), "π₁ ∩ π₃", -10, 18, "grigio", 12)
f.nota(16, 470, "La LT è l'intersezione tra π₁ e π₂. Lo schema rimanda al modello:")
f.nota(16, 488, "la pianta mantiene la sua forma, gli angoli di 90° restano di 90°.")
f.salva(OUT_SBOBINA + "04-triedro-come-alla-lavagna.svg")

# 2. Il piano frontale non e' una figura ------------------------------------------------
f = Figura(560, 500, 0, "Il piano β frontale non è una figura: si rappresenta con le sue tracce")
t = TriedroLavagna(f, (260, 160), X3=400, U=360, Y=260, Z=220, scala=0.62)
t.piani()
n, d = piano_per((0, 110, 0), (1, 0, 0), (0, 0, 1))
t.piano(n, d, "verde", 0.14)
t.tracce(n, d, "nero")
# il "rettangolo" del cartoncino prosegue: tratteggi oltre i bordi
for a_, b_ in [((40, 110, 220), (-20, 110, 220)), ((40, 110, 220), (40, 110, 270)),
               ((40, 110, 0), (-20, 110, 0)), ((400, 110, 220), (400, 110, 270))]:
    t.segmento(a_, b_, "verde", 1.2, "5,4")
t.testo((220, 110, 0), "t_1β", -4, 20, "nero", 15)
t.testo((400, 110, 110), "t_3β", 8, 4, "nero", 15)
t.testo((180, 110, 130), "β", 0, 0, "verde", 18)
t.testo((120, 0, 250), "t_2β∞", 0, 0, "nero", 14)
f.nota(16, 470, "Il rettangolo serve solo per comodità: il piano è infinito (i tratteggi: prosegue).")
f.nota(16, 488, "Restano le tracce t₁β e t₃β; t₂β è all'infinito perché β è parallelo a π₂.")
f.salva(OUT_SBOBINA + "04-spazio-piano-non-e-una-figura.svg")


# ================================================================ PER LA BOZZA

X3 = 380

# 3. Disegno proposto: le tracce del piano della figura ABCD (compito per casa) ----------
Y0, Z0 = 150, 120


def zq(y):
    return Z0 * (1 - y / Y0)


A = (130, 120, zq(120)); B = (270, 120, zq(120)); C = (130, 40, zq(40)); D = (270, 40, zq(40))
f = foglio("Compito: le tracce del piano α della figura ABCD (rette di profilo r = AC e s = BD)", X3, 175, 165)
# tracce del piano (risultato)
f.traccia((-5, Z0), (X3, Z0)); f.testo((-5, Z0), "t_2α", 2, -8)
f.traccia((-5, -Y0), (X3, -Y0)); f.testo((-5, -Y0), "t_1α", 2, -8)
f.traccia((X3, Z0), (X3 + Y0, 0)); f.testo((X3 + Y0, 0), "t_3α", 6, -10)
# richiami della figura e terza proiezione
for p in (B, D):
    orizz(f, p[0], X3, -p[1])
    arco(f, X3, p[1])
    f.richiamo(X3 + p[1], 0, p[2])
    orizz(f, p[0], X3 + p[1], p[2])
f.figura([P1(A), P1(B), P1(D), P1(C)], "blu")
f.figura([P2(A), P2(B), P2(D), P2(C)], "blu")
f.retta(P3(A, X3), P3(C, X3), "blu", 4)
# le rette di profilo r (AC) e s (BD), prolungate fino alle tracce
for x, nome in ((130, "r"), (270, "s")):
    f.retta((x, Z0), (x, 0), "viola", 1.6)
    f.retta((x, 0), (x, -Y0), "viola", 1.6)
# terza proiezione prolungata: incontra la verticale in (T2)3 e la LT in (T1)3
arco(f, X3, Y0)
f.punto((130, Z0), "T_{2r}", -46, -6, "viola")
f.punto((270, Z0), "T_{2s}", 6, -6, "viola")
f.punto((130, -Y0), "T_{1r}", -46, 18, "viola")
f.punto((270, -Y0), "T_{1s}", 6, 18, "viola")
f.punto((X3, Z0), "(T_{2r})₃", 8, -6)
f.punto((X3 + Y0, 0), "(T_{1r})₃", -8, 18)
f.punto(P1(A), "A₁", -24, 16); f.punto(P1(B), "B₁", 6, 16)
f.punto(P1(C), "C₁", -24, -2); f.punto(P1(D), "D₁", 6, -2)
f.punto(P2(A), "A₂", -24, 14); f.punto(P2(B), "B₂", 6, 14)
f.punto(P2(C), "C₂", -24, -2); f.punto(P2(D), "D₂", 6, -2)
f.punto(P3(A, X3), "A₃ ≡ B₃", -78, 18)
f.punto(P3(C, X3), "C₃ ≡ D₃", 10, -8)
f.nota(20, 380, "r e s sono di profilo: le tracce si trovano in terza proiezione. t₁α passa per T₁ᵣ e T₁ₛ, t₂α per T₂ᵣ e T₂ₛ.")
f.salva(OUT_BOZZA + "b04-tracce-del-piano-della-figura.svg")

# 4. Disegno proposto: un punto P sulla retta di profilo -------------------------------
xp, yp1, zp2 = 220, 110, 120
zP = 50
uP = yp1 * (1 - zP / zp2)
f = foglio("Un punto P della retta r di profilo: serve la terza proiezione", X3, 175, 165)
f.retta((xp, zp2), (xp, -yp1), "viola", 2)
f.testo((xp, 95), "r₂", 6, 0, "viola"); f.testo((xp, -95), "r₁", 6, 0, "viola")
arco(f, X3, yp1)
orizz(f, xp, X3, -yp1)
orizz(f, xp, X3, zp2)
f.retta((X3 + yp1, 0), (X3, zp2), "viola"); f.testo((X3 + yp1 * 0.75, zp2 * 0.3), "r₃", 8, 0, "viola")
f.punto((xp, zp2), "T_{2r}", -48, -4, "viola")
f.punto((xp, -yp1), "T_{1r}", -48, 6, "viola")
f.punto((X3, zp2), "(T_{2r})₃", 6, -8)
f.punto((X3 + yp1, 0), "(T_{1r})₃", 6, 16)
# P: dalla quota di P2 si trova P3 su r3, poi l'aggetto torna con l'arco
orizz(f, xp, X3 + uP, zP)
f.richiamo(X3 + uP, zP, 0)
arco(f, X3, uP)
orizz(f, xp, X3, -uP)
f.punto((xp, zP), "P₂", -26, -4, "rosso")
f.punto((X3 + uP, zP), "P₃", 8, -6, "rosso")
f.punto((xp, -uP), "P₁", -26, 4, "rosso")
f.nota(20, 380, "r₁ e r₂ stanno sulla stessa linea: P₂ da solo non dice dov'è P₁. Si passa per r₃: P₃ sta su r₃ alla quota di P₂.")
f.salva(OUT_BOZZA + "b04-punto-sulla-retta-di-profilo.svg")
print("ok")
