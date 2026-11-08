"""Disegni per la bozza di matematica 07 (insiemi, numeri e intervalli).

Script senza dipendenze: python3 -I .claude/scripts/disegni/matematica-07.py
Le immagini vanno in anno-1/semestre-1/matematica/bozze/img/ con prefisso 07-.

Disegni:
- 07-appartenenza-inclusione  a in A, a non in A, B contenuto in A (come sugli appunti)
- 07-operazioni-venn          unione, intersezione, differenza, complementare
- 07-insiemi-numerici         N dentro Z dentro Q dentro R, con esempi
- 07-retta-reale              la retta reale con alcuni numeri (interi, razionali, irrazionali)
- 07-valore-assoluto          |a| e |a - b| come distanze sulla retta
- 07-intervalli               i tipi di intervallo e la loro notazione
- 07-esercizio-intervalli     l'esercizio del professore: X, Y, Z e la loro intersezione
"""
import math
import os

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/matematica/bozze/img/"

NERO = "#1f2937"
GRIGIO = "#9ca3af"
GRIGLIA = "#e5e7eb"
BLU = "#2563eb"
ROSSO = "#dc2626"
VERDE = "#16a34a"
ARANCIO = "#d97706"
VIOLA = "#7c3aed"
RIEMPI = "#bfdbfe"
FONT = "font-family=\"Helvetica, Arial, sans-serif\""


class SVG:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parti = []

    def add(self, s):
        self.parti.append(s)

    def testo(self, x, y, t, size=15, colore=NERO, anchor="middle", peso="normal", stile="normal"):
        t = str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" fill="{colore}" '
                 f'text-anchor="{anchor}" font-weight="{peso}" font-style="{stile}">{t}</text>')

    def linea(self, x1, y1, x2, y2, colore=NERO, sp=1.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{colore}" stroke-width="{sp}"{d}/>')

    def freccia(self, x1, y1, x2, y2, colore=NERO, sp=1.5):
        self.linea(x1, y1, x2, y2, colore, sp)
        a = math.atan2(y2 - y1, x2 - x1)
        L = 10
        p1 = (x2 - L * math.cos(a - 0.4), y2 - L * math.sin(a - 0.4))
        p2 = (x2 - L * math.cos(a + 0.4), y2 - L * math.sin(a + 0.4))
        self.add(f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" '
                 f'fill="{colore}"/>')

    def pallino(self, x, y, pieno=True, colore=BLU, r=5.5):
        fill = colore if pieno else "white"
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{colore}" stroke-width="2"/>')

    def cerchio(self, cx, cy, r, fill="none", stroke=NERO, sp=2, clip=None):
        c = f' clip-path="url(#{clip})"' if clip else ""
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{sp}"{c}/>')

    def ellisse(self, cx, cy, rx, ry, fill="none", stroke=NERO, sp=2):
        self.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sp}"/>')

    def rett(self, x, y, w, h, fill, stroke="none", sp=1.5, rx=0):
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sp}"/>')

    def salva(self, nome):
        os.makedirs(OUT, exist_ok=True)
        s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
             f'viewBox="0 0 {self.w} {self.h}">\n'
             f'<rect width="{self.w}" height="{self.h}" fill="white"/>\n' + "\n".join(self.parti) + "\n</svg>\n")
        with open(OUT + nome + ".svg", "w", encoding="utf-8") as f:
            f.write(s)
        print("scritto", nome)


# ---------------------------------------------------------------- insiemi

def appartenenza_inclusione():
    s = SVG(660, 240)
    # a in A
    s.cerchio(110, 110, 70, RIEMPI, BLU)
    s.pallino(110, 110, True, NERO, 4)
    s.testo(122, 105, "a", 17, stile="italic", anchor="start")
    s.testo(50, 50, "A", 18, BLU, stile="italic")
    s.testo(110, 226, "a ∈ A", 17)
    # a non in A
    s.cerchio(320, 110, 70, RIEMPI, BLU)
    s.pallino(410, 60, True, NERO, 4)
    s.testo(422, 56, "a", 17, stile="italic", anchor="start")
    s.testo(262, 50, "A", 18, BLU, stile="italic")
    s.testo(330, 226, "a ∉ A", 17)
    # B contenuto in A
    s.cerchio(550, 110, 80, RIEMPI, BLU)
    s.cerchio(565, 125, 35, "#fde68a", ARANCIO)
    s.testo(565, 131, "B", 17, ARANCIO, stile="italic")
    s.testo(468, 50, "A", 18, BLU, stile="italic")
    s.testo(550, 226, "B ⊆ A", 17)
    s.salva("07-appartenenza-inclusione")


def operazioni_venn():
    s = SVG(790, 260)
    r = 52
    pannelli = [
        (15, "unione", "A ∪ B"),
        (210, "intersezione", "A ∩ B"),
        (405, "differenza", "A \\ B"),
        (600, "complementare", "Aᶜ (in U)"),
    ]
    for i, (x0, tipo, nome) in enumerate(pannelli):
        cxA, cxB, cy = x0 + 62, x0 + 110, 120
        if tipo == "complementare":
            cxA = x0 + 85
        s.add(f'<clipPath id="clipA{i}"><circle cx="{cxA}" cy="{cy}" r="{r}"/></clipPath>')
        # riquadro universo
        s.rett(x0, 40, 170, 160, "white", GRIGIO, 1.2, 6)
        if tipo == "unione":
            s.cerchio(cxA, cy, r, RIEMPI, "none")
            s.cerchio(cxB, cy, r, RIEMPI, "none")
        elif tipo == "intersezione":
            s.cerchio(cxB, cy, r, RIEMPI, "none", clip=f"clipA{i}")
        elif tipo == "differenza":
            s.cerchio(cxA, cy, r, RIEMPI, "none")
            s.cerchio(cxB, cy, r, "white", "none")
        elif tipo == "complementare":
            s.rett(x0, 40, 170, 160, RIEMPI, GRIGIO, 1.2, 6)
            s.cerchio(cxA, cy, r, "white", "none")
        s.cerchio(cxA, cy, r, "none", BLU, 2)
        if tipo != "complementare":
            s.cerchio(cxB, cy, r, "none", ARANCIO, 2)
            s.testo(cxB + 44, cy - 50, "B", 16, ARANCIO, stile="italic")
        s.testo(cxA - 44, cy - 50, "A", 16, BLU, stile="italic")
        s.testo(x0 + 157, 192, "U", 13, GRIGIO, stile="italic")
        s.testo(x0 + 85, 26, tipo, 15, peso="bold")
        s.testo(x0 + 85, 228, nome, 17)
    s.salva("07-operazioni-venn")


def insiemi_numerici():
    s = SVG(640, 350)
    s.add('<g transform="translate(0,20)">')
    s.ellisse(320, 170, 300, 150, "#ede9fe", VIOLA)
    s.ellisse(270, 180, 225, 118, "#dcfce7", VERDE)
    s.ellisse(225, 190, 150, 88, "#fef3c7", ARANCIO)
    s.ellisse(185, 200, 80, 55, "#dbeafe", BLU)
    s.testo(185, 172, "ℕ", 22, BLU, peso="bold")
    s.testo(185, 205, "0   1   2", 15)
    s.testo(185, 228, "3   …", 15)
    s.testo(330, 160, "ℤ", 22, ARANCIO, peso="bold")
    s.testo(330, 192, "−1", 15)
    s.testo(325, 222, "−7", 15)
    s.testo(435, 145, "ℚ", 22, VERDE, peso="bold")
    s.testo(440, 178, "1/2", 15)
    s.testo(445, 208, "−0,75", 15)
    s.testo(425, 242, "5/3", 15)
    s.testo(560, 130, "ℝ", 22, VIOLA, peso="bold")
    s.testo(565, 168, "√2", 15)
    s.testo(565, 200, "π", 15, stile="italic")
    s.testo(565, 232, "−√3", 15)
    s.add("</g>")
    s.testo(320, 24, "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ", 17)
    s.salva("07-insiemi-numerici")


# ---------------------------------------------------------------- retta reale

def retta_reale():
    s = SVG(700, 150)
    vmin, vmax = -3.5, 4.5
    x0, x1 = 40, 660

    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    y = 80
    s.freccia(x0 - 15, y, x1 + 20, y, NERO, 1.5)
    s.testo(x1 + 22, y + 22, "ℝ", 16)
    for k in range(-3, 5):
        s.linea(X(k), y - 5, X(k), y + 5, NERO, 1.5)
        s.testo(X(k), y + 24, str(k).replace("-", "−"), 14)
    punti = [(-math.sqrt(2), "−√2", ROSSO), (0.5, "1/2", VERDE), (-2.5, "−5/2", VERDE),
             (math.pi, "π", ROSSO), (math.sqrt(2), "√2", ROSSO), (3.5, "7/2", VERDE)]
    for v, nome, c in punti:
        s.pallino(X(v), y, True, c, 4.5)
        s.testo(X(v), y - 14, nome, 15, c)
    s.testo(40, 140, "verde: razionali (frazioni)", 13, VERDE, anchor="start")
    s.testo(300, 140, "rosso: irrazionali", 13, ROSSO, anchor="start")
    s.testo(480, 140, "tacche nere: interi", 13, NERO, anchor="start")
    s.salva("07-retta-reale")


def valore_assoluto():
    s = SVG(700, 210)
    vmin, vmax = -5.5, 5.5
    x0, x1 = 40, 660

    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    # riga 1: |-3| = |3| = 3
    y = 70
    s.freccia(x0 - 15, y, x1 + 20, y, GRIGIO, 1.5)
    for k in range(-5, 6):
        s.linea(X(k), y - 4, X(k), y + 4, GRIGIO, 1.2)
        s.testo(X(k), y + 22, str(k).replace("-", "−"), 13, GRIGIO)
    s.linea(X(-3), y - 14, X(0), y - 14, ROSSO, 3)
    s.linea(X(0), y - 14, X(3), y - 14, BLU, 3)
    s.pallino(X(-3), y, True, ROSSO, 4.5)
    s.pallino(X(3), y, True, BLU, 4.5)
    s.pallino(X(0), y, True, NERO, 3.5)
    s.testo(X(-1.5), y - 24, "|−3| = 3", 15, ROSSO)
    s.testo(X(1.5), y - 24, "|3| = 3", 15, BLU)
    # riga 2: |a - b| distanza tra 1 e 4 e tra -2 e 1
    y = 160
    s.freccia(x0 - 15, y, x1 + 20, y, GRIGIO, 1.5)
    for k in range(-5, 6):
        s.linea(X(k), y - 4, X(k), y + 4, GRIGIO, 1.2)
        s.testo(X(k), y + 22, str(k).replace("-", "−"), 13, GRIGIO)
    s.linea(X(1), y - 14, X(4), y - 14, VERDE, 3)
    s.pallino(X(1), y, True, VERDE, 4.5)
    s.pallino(X(4), y, True, VERDE, 4.5)
    s.testo(X(2.5), y - 24, "|4 − 1| = 3", 15, VERDE)
    s.linea(X(-4), y - 14, X(-1), y - 14, VIOLA, 3)
    s.pallino(X(-4), y, True, VIOLA, 4.5)
    s.pallino(X(-1), y, True, VIOLA, 4.5)
    s.testo(X(-2.5), y - 24, "|−1 − (−4)| = 3", 15, VIOLA)
    s.salva("07-valore-assoluto")


def intervalli():
    righe = [
        ("[a, b]", "a ≤ x ≤ b", "chiuso", (True, True, False, False)),
        ("(a, b)", "a < x < b", "aperto", (False, False, False, False)),
        ("[a, b)", "a ≤ x < b", "chiuso a sinistra, aperto a destra", (True, False, False, False)),
        ("(a, b]", "a < x ≤ b", "aperto a sinistra, chiuso a destra", (False, True, False, False)),
        ("[a, +∞)", "x ≥ a", "illimitato a destra", (True, None, False, True)),
        ("(−∞, b)", "x < b", "illimitato a sinistra", (None, False, True, False)),
    ]
    s = SVG(780, 50 + 52 * len(righe))
    s.testo(60, 28, "notazione", 14, GRIGIO, peso="bold")
    s.testo(175, 28, "disuguaglianza", 14, GRIGIO, peso="bold")
    s.testo(625, 28, "sulla retta", 14, GRIGIO, peso="bold")
    L0, L1 = 495, 760
    xa, xb = 545, 690
    for i, (nota, dis, nome, (ac, bc, infs, infd)) in enumerate(righe):
        y = 70 + 52 * i
        s.testo(60, y + 5, nota, 17)
        s.testo(175, y + 5, dis, 16, stile="italic")
        s.testo(265, y + 5, nome, 12, GRIGIO, anchor="start")
        s.freccia(L0, y, L1, y, GRIGIO, 1.2)
        a = L0 + 2 if infs else xa
        b = L1 - 12 if infd else xb
        s.linea(a, y, b, y, BLU, 4)
        if infd:
            s.add(f'<polygon points="{L1},{y} {L1-14},{y-7} {L1-14},{y+7}" fill="{BLU}"/>')
        if infs:
            s.add(f'<polygon points="{L0-4},{y} {L0+10},{y-7} {L0+10},{y+7}" fill="{BLU}"/>')
        if not infs:
            s.pallino(xa, y, ac, BLU)
            s.testo(xa, y + 22, "a", 14, stile="italic")
        if not infd:
            s.pallino(xb, y, bc, BLU)
            s.testo(xb, y + 22, "b", 14, stile="italic")
    s.salva("07-intervalli")


def esercizio_intervalli():
    s = SVG(720, 300)
    vmin, vmax = -3, 5.2
    x0, x1 = 120, 680

    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    r2, p, s72, r17 = -math.sqrt(2), math.pi, 3.5, math.sqrt(17)
    # fascia della soluzione
    s.rett(X(p), 30, X(s72) - X(p), 230, "#dcfce7")
    # riga dei valori
    y = 45
    s.freccia(x0 - 10, y, x1 + 16, y, NERO, 1.5)
    for v, nome, sotto in [(r2, "−√2 ≈ −1,41", 0), (0, "0", 0), (p, "π ≈ 3,14", 0),
                           (s72, "7/2 = 3,5", 1), (r17, "√17 ≈ 4,12", 0)]:
        s.linea(X(v), y - 5, X(v), y + 5, NERO, 1.5)
        s.testo(X(v), y - 12 if not sotto else y + 22, nome, 13)
        s.linea(X(v), y + 5, X(v), 250, GRIGIO, 1, "4,4")

    def riga(yy, nome, a, b, ac, bc, col):
        s.testo(20, yy + 5, nome, 15, col, anchor="start")
        s.linea(x0 - 10, yy, x1 + 10, yy, GRIGLIA, 1)
        xa = X(a) if a is not None else x0 - 10
        xb = X(b) if b is not None else x1 + 10
        s.linea(xa, yy, xb, yy, col, 4)
        if a is None:
            s.add(f'<polygon points="{x0-14},{yy} {x0-4},{yy-6} {x0-4},{yy+6}" fill="{col}"/>')
        else:
            s.pallino(X(a), yy, ac, col)
        if b is None:
            s.add(f'<polygon points="{x1+14},{yy} {x1+4},{yy-6} {x1+4},{yy+6}" fill="{col}"/>')
        else:
            s.pallino(X(b), yy, bc, col)

    riga(105, "X: x ≥ −√2", r2, None, True, None, BLU)
    riga(150, "Y: x < 7/2", None, s72, None, False, ARANCIO)
    riga(195, "Z: π ≤ x < √17", p, r17, True, False, VIOLA)
    riga(245, "X ∩ Y ∩ Z", p, s72, True, False, VERDE)
    s.testo(X((p + s72) / 2), 280, "[π, 7/2)", 15, VERDE, peso="bold")
    s.salva("07-esercizio-intervalli")


if __name__ == "__main__":
    appartenenza_inclusione()
    operazioni_venn()
    insiemi_numerici()
    retta_reale()
    valore_assoluto()
    intervalli()
    esercizio_intervalli()
