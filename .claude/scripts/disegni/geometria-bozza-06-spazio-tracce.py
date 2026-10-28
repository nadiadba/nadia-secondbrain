"""Vista nello spazio del Disegno 16 di «PO 3 - La retta»: la retta con T2r sotto la linea di terra
(stessi punti di b06-retta-tracce-sotto-la-lt.svg in geometria-bozza-06.py). Disegno proposto.

Vista bassa e quasi di fronte (il pavimento pi1 si vede schiacciato), cosi' la parte di pi2 che scende
sotto il pavimento resta visibile: con la vista del triedro dall'alto finirebbe nascosta dal pavimento."""
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro

BOZ = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"

T1 = (170, 80, 0)        # prima traccia: sul pavimento, davanti a pi2
T2 = (390, 0, -70)       # seconda traccia: sulla parete, ma sotto il pavimento
d = tuple(T2[i] - T1[i] for i in range(3))
XA, XB, Y, ZSU, ZGIU = 20, 520, 160, 170, 140


class Vista(Triedro):
    def _p(self, p):
        return (self.o[0] + p[0] - 0.45 * p[1], self.o[1] - p[2] + 0.33 * p[1])


def su_r(t):
    return tuple(T1[i] + d[i] * t for i in range(3))


f = Figura(640, 470, 0, "Nello spazio: la retta r con T₂ᵣ sotto la linea di terra")
t = Vista(f, (110, 200), 0, 0, 0, 0)

# pi2 sotto il pavimento (dietro), il pavimento pi1, pi2 sopra il pavimento
t._poligono([(XA, 0, 0), (XB, 0, 0), (XB, 0, -ZGIU), (XA, 0, -ZGIU)], "#b9c6d6", 0.22, "#9aa5b1")
t._poligono([(XA, 0, 0), (XB, 0, 0), (XB, Y, 0), (XA, Y, 0)], "#9aa5b1", 0.16, "#9aa5b1")
t._poligono([(XA, 0, 0), (XB, 0, 0), (XB, 0, ZSU), (XA, 0, ZSU)], "#9aa5b1", 0.07, "#b7bfc8")
t._linea((XA - 10, 0, 0), (XB + 10, 0, 0), "nero", 1.8)
t.testo((XB + 10, 0, 0), "LT", 6, 5)
t.testo((XB, 0, ZSU), "π₂ sopra il pavimento", -170, 22, "grigio", 13)
t.testo((XB, 0, -ZGIU), "π₂ sotto il pavimento", -170, -10, "grigio", 13)
t.testo((XB, Y, 0), "π₁ (il pavimento)", -118, -8, "grigio", 13)

# proiezioni: r1 sul pavimento per T1 e (T2r)1, r2 sulla parete per (T1r)2 e T2
L1, L2 = (T2[0], 0, 0), (T1[0], 0, 0)
r1a = tuple(L1[i] + (T1[i] - L1[i]) * 1.75 for i in range(3))
t.segmento(L1, r1a, "arancio", 1.6); t.testo(r1a, "r₁", -22, 4, "arancio", 15)
r2a, r2b = tuple(L2[i] - (T2[i] - L2[i]) * 0.55 for i in range(3)), tuple(L2[i] + (T2[i] - L2[i]) * 1.25 for i in range(3))
t.segmento(r2a, r2b, "blu", 1.6); t.testo(r2a, "r₂", -22, 0, "blu", 15)

# la retta: sopra il pavimento si vede; tra T1 e T2 e' sotto il pavimento (tratteggiata)
t.segmento(su_r(-0.7), T1, "rosso", 2.8)
t.testo(su_r(-0.7), "r", -16, 2, "rosso", 17)
t.segmento(T1, T2, "rosso", 2, "6,4")
t.segmento(T2, su_r(1.2), "rosso", 1.2, "3,4")

t.richiamo(T1, L2)
t.richiamo(T2, L1)
t.punto(T1, "T_{1r}", -8, 22, "rosso")
t.punto(T2, "T_{2r}", 8, 18, "rosso")
t.punto(L2, "(T_{1r})₂", -64, -10)
t.punto(L1, "(T_{2r})₁", 4, -10)

f.nota(16, 392, "r arriva da sopra il pavimento e lo buca in T₁ᵣ. Poi prosegue sotto (tratteggiata) e incontra")
f.nota(16, 410, "la parete π₂ solo sotto il pavimento, in T₂ᵣ: per questo sul foglio T₂ᵣ cade sotto la LT.")
f.nota(16, 428, "r₁ (arancio) è l'ombra di r sul pavimento, r₂ (blu) la sua immagine sulla parete.")
f.nota(16, 446, "Schema proposto, non disegnato a lezione.")
f.salva(BOZ + "b06-spazio-retta-tracce-sotto-la-lt.svg")
print("ok")
