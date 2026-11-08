"""Disegni per la bozza di matematica 01 (equazioni e disequazioni).

Script senza dipendenze: python3 -I .claude/scripts/disegni/matematica-01.py
Le immagini vanno in anno-1/semestre-1/matematica/bozze/img/ con prefisso 01-.

Disegni:
- 01-retta-reale-intervalli   intervalli aperti, chiusi, illimitati sulla retta reale
- 01-parabola-discriminante   i tre casi del discriminante (due zeri, uno, nessuno)
- 01-parabola-segno           segno di x^2 - 5x + 6: positivo fuori, negativo dentro
- 01-equazione-irrazionale    sqrt(x+3) = x - 3: la soluzione falsa x = 1
- 01-valore-assoluto          |x - 1| = 3 e |x - 1| < 3 sul grafico
- 01-tabella-segni            tabella dei segni di (x+2)(x-1)/(x-3)
- 01-sistema-disequazioni     intersezione delle soluzioni di un sistema
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
FONT = "font-family=\"Helvetica, Arial, sans-serif\""


class SVG:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.parti = []

    def add(self, s):
        self.parti.append(s)

    def testo(self, x, y, t, size=15, colore=NERO, anchor="middle", peso="normal", stile="normal"):
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

    def rett(self, x, y, w, h, fill, opac=1.0, stroke="none"):
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" '
                 f'fill-opacity="{opac}" stroke="{stroke}"/>')

    def salva(self, nome):
        os.makedirs(OUT, exist_ok=True)
        s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
             f'viewBox="0 0 {self.w} {self.h}">\n'
             f'<rect width="{self.w}" height="{self.h}" fill="white"/>\n' + "\n".join(self.parti) + "\n</svg>\n")
        with open(OUT + nome + ".svg", "w", encoding="utf-8") as f:
            f.write(s)
        print("scritto", nome)


class Piano:
    """Un riquadro con assi cartesiani dentro un SVG."""
    n = 0

    def __init__(self, svg, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.s = svg
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        Piano.n += 1
        self.clip = f"riquadro{Piano.n}"
        svg.add(f'<clipPath id="{self.clip}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}"/></clipPath>')

    def X(self, x):
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def Y(self, y):
        return self.y0 + (self.ymax - y) / (self.ymax - self.ymin) * self.h

    def griglia(self, passo=1):
        x = math.ceil(self.xmin)
        while x <= self.xmax:
            self.s.linea(self.X(x), self.y0, self.X(x), self.y0 + self.h, GRIGLIA, 1)
            x += passo
        y = math.ceil(self.ymin)
        while y <= self.ymax:
            self.s.linea(self.x0, self.Y(y), self.x0 + self.w, self.Y(y), GRIGLIA, 1)
            y += passo

    def assi(self, tacche_x=(), tacche_y=(), nome_x="x", nome_y="y", size=13):
        s = self.s
        s.freccia(self.x0, self.Y(0), self.x0 + self.w + 8, self.Y(0))
        s.freccia(self.X(0), self.y0 + self.h, self.X(0), self.y0 - 8)
        s.testo(self.x0 + self.w + 8, self.Y(0) + 20, nome_x, 15, stile="italic")
        s.testo(self.X(0) + 12, self.y0 - 4, nome_y, 15, stile="italic", anchor="start")
        for t in tacche_x:
            s.linea(self.X(t), self.Y(0) - 4, self.X(t), self.Y(0) + 4)
            s.testo(self.X(t), self.Y(0) + 23, str(t).replace("-", "−"), size)
        for t in tacche_y:
            s.linea(self.X(0) - 4, self.Y(t), self.X(0) + 4, self.Y(t))
            s.testo(self.X(0) - 8, self.Y(t) + 5, str(t).replace("-", "−"), size, anchor="end")

    def curva(self, f, a, b, colore=BLU, sp=2.5, dash=None, n=300):
        pts = []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            y = f(x)
            if y is None:
                continue
            pts.append(f"{self.X(x):.1f},{self.Y(y):.1f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.s.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{colore}" '
                   f'stroke-width="{sp}" stroke-linejoin="round" clip-path="url(#{self.clip})"{d}/>')


# ---------------------------------------------------------------- retta reale

def retta_reale(s, y, x0, x1, vmin, vmax, tacche, intervalli, colore=BLU, etichetta=None, et_x=None):
    """Disegna una retta reale con gli intervalli evidenziati.
    intervalli: lista di (a, b, a_chiuso, b_chiuso); a o b = None per l'infinito."""
    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    s.freccia(x0 - 10, y, x1 + 14, y, GRIGIO, 1.5)
    for t, nome in tacche:
        s.linea(X(t), y - 5, X(t), y + 5, GRIGIO, 1.5)
        s.testo(X(t), y + 22, nome, 15)
    for a, b, ac, bc in intervalli:
        xa = X(a) if a is not None else x0 - 6
        xb = X(b) if b is not None else x1 + 6
        s.linea(xa, y, xb, y, colore, 5)
        if a is None:
            s.freccia(xa + 12, y, xa - 4, y, colore, 5)
        if b is None:
            s.freccia(xb - 12, y, xb + 4, y, colore, 5)
        if a is not None:
            s.pallino(xa, y, ac, colore)
        if b is not None:
            s.pallino(xb, y, bc, colore)
    if etichetta:
        s.testo(et_x if et_x else x1 + 30, y + 5, etichetta, 15, anchor="start")


def fig_intervalli():
    s = SVG(640, 371)
    righe = [
        ("[a, b]", "a ≤ x ≤ b", [(2, 6, True, True)]),
        ("(a, b)", "a &lt; x &lt; b", [(2, 6, False, False)]),
        ("[a, b)", "a ≤ x &lt; b", [(2, 6, True, False)]),
        ("[a, +∞)", "x ≥ a", [(2, None, True, False)]),
        ("(−∞, b)", "x &lt; b", [(None, 6, False, False)]),
    ]
    s.testo(70, 26, "intervallo", 14, GRIGIO, peso="bold")
    s.testo(195, 26, "disequazione", 14, GRIGIO, peso="bold")
    s.testo(440, 26, "sulla retta reale", 14, GRIGIO, peso="bold")
    for i, (nota, dis, iv) in enumerate(righe):
        y = 66 + i * 58
        s.testo(70, y + 5, nota, 17, NERO)
        s.testo(195, y + 5, dis, 16, NERO, stile="italic")
        retta_reale(s, y, 290, 600, 0, 8, [(2, "a"), (6, "b")], iv)
    s.add(f'<circle cx="50" cy="352" r="5.5" fill="{BLU}" stroke="{BLU}" stroke-width="2"/>')
    s.testo(62, 357, "pallino pieno: il numero è compreso", 13, anchor="start")
    s.add(f'<circle cx="330" cy="352" r="5.5" fill="white" stroke="{BLU}" stroke-width="2"/>')
    s.testo(342, 357, "pallino vuoto: il numero è escluso", 13, anchor="start")
    s.salva("01-retta-reale-intervalli")


# ---------------------------------------------------------------- parabole

def fig_discriminante():
    s = SVG(660, 310)
    casi = [
        ("Δ &gt; 0: due soluzioni", lambda x: x * x - 4, [-2, 2], "y = x² − 4"),
        ("Δ = 0: una soluzione", lambda x: (x - 0) ** 2, [0], "y = x²"),
        ("Δ &lt; 0: nessuna soluzione", lambda x: x * x + 1.5, [], "y = x² + 1,5"),
    ]
    for i, (tit, f, zeri, eq) in enumerate(casi):
        x0 = 20 + i * 215
        p = Piano(s, x0, 60, 190, 200, -3.2, 3.2, -4.6, 5)
        p.griglia()
        p.assi()
        for z in zeri:
            if z != 0:
                s.testo(p.X(z) + (16 if z > 0 else -16), p.Y(0) + 22, str(z).replace("-", "−"), 13)
        p.curva(f, -3.2, 3.2, BLU)
        for z in zeri:
            s.pallino(p.X(z), p.Y(0), True, ROSSO)
        if 0 in zeri:
            s.testo(p.X(0) + 14, p.Y(0) + 23, "0", 13)
        s.testo(x0 + 95, 26, tit, 14, peso="bold")
        s.testo(x0 + 95, 296, eq, 14, BLU, stile="italic")
    s.salva("01-parabola-discriminante")


def fig_parabola_segno():
    s = SVG(620, 400)
    p = Piano(s, 50, 30, 520, 300, -0.6, 6.0, -1.5, 6.0)
    p.griglia()
    # fasce sotto l'asse x
    s.rett(p.X(-0.6), p.Y(0) + 30, p.X(2) - p.X(-0.6), 12, VERDE, 0.8)
    s.rett(p.X(2), p.Y(0) + 30, p.X(3) - p.X(2), 12, ROSSO, 0.8)
    s.rett(p.X(3), p.Y(0) + 30, p.X(6.0) - p.X(3), 12, VERDE, 0.8)
    p.assi(tacche_x=[1, 2, 3, 4, 5], tacche_y=[2, 4])
    f = lambda x: x * x - 5 * x + 6
    # parte positiva verde, negativa rossa
    p.curva(f, -0.35, 2, VERDE, 3)
    p.curva(f, 2, 3, ROSSO, 3)
    p.curva(f, 3, 5.35, VERDE, 3)
    s.pallino(p.X(2), p.Y(0), True, NERO, 4.5)
    s.pallino(p.X(3), p.Y(0), True, NERO, 4.5)
    s.testo(p.X(0.8), p.Y(0) + 64, "+  (esterno)", 15, VERDE, peso="bold")
    s.testo(p.X(2.5), p.Y(0) + 64, "−", 18, ROSSO, peso="bold")
    s.testo(p.X(2.5), p.Y(0) + 82, "(interno)", 14, ROSSO, peso="bold")
    s.testo(p.X(4.6), p.Y(0) + 64, "+  (esterno)", 15, VERDE, peso="bold")
    s.testo(p.X(2.5), p.Y(4.4), "y = x² − 5x + 6", 16, NERO, stile="italic")
    s.testo(p.X(2.5), p.Y(-0.25) + 22, "", 12)
    s.testo(310, 392, "La parabola sta sotto l'asse x solo tra le due radici 2 e 3.", 14, NERO)
    s.salva("01-parabola-segno")


def fig_irrazionale():
    s = SVG(620, 410)
    p = Piano(s, 50, 30, 520, 330, -3.6, 8, -4.5, 5.2)
    p.griglia()
    p.assi(tacche_x=[-3, 1, 3, 6], tacche_y=[-2, 2, 3])
    p.curva(lambda x: math.sqrt(x + 3) if x >= -3 else None, -3, 8, BLU, 3)
    p.curva(lambda x: -math.sqrt(x + 3) if x >= -3 else None, -3, 8, BLU, 2, dash="6,5")
    p.curva(lambda x: x - 3, -1.2, 8, ARANCIO, 3)
    s.pallino(p.X(6), p.Y(3), True, VERDE, 6)
    s.pallino(p.X(1), p.Y(-2), True, ROSSO, 6)
    s.linea(p.X(6), p.Y(3), p.X(6), p.Y(0), GRIGIO, 1.2, "4,3")
    s.linea(p.X(1), p.Y(-2), p.X(1), p.Y(0), GRIGIO, 1.2, "4,3")
    s.testo(p.X(6) - 12, p.Y(3) - 14, "x = 6: soluzione vera", 14, VERDE, anchor="end", peso="bold")
    s.testo(p.X(1.3), p.Y(-3.4), "x = 1: soluzione falsa", 14, ROSSO, anchor="start", peso="bold")
    s.testo(p.X(-3.4), p.Y(2.6), "y = √(x + 3)", 14, BLU, anchor="start", stile="italic")
    s.testo(p.X(6.5), p.Y(-4.1), "y = −√(x + 3)", 14, BLU, stile="italic")
    s.testo(p.X(6.6), p.Y(4.9), "y = x − 3", 15, ARANCIO, stile="italic")
    s.testo(310, 398, "Elevando al quadrato si trovano anche gli incontri con la curva tratteggiata.", 14)
    s.salva("01-equazione-irrazionale")


def fig_valore_assoluto():
    s = SVG(620, 400)
    p = Piano(s, 50, 30, 520, 300, -4, 6.5, -1.4, 5.2)
    p.griglia()
    s.rett(p.X(-2), p.Y(0) + 28, p.X(4) - p.X(-2), 12, VERDE, 0.8)
    p.assi(tacche_x=[-2, 1, 4])
    p.curva(lambda x: abs(x - 1), -4, 6.2, BLU, 3)
    p.curva(lambda x: 3, -4, 6.4, ROSSO, 2, dash="7,5")
    s.pallino(p.X(-2), p.Y(3), True, NERO, 5)
    s.pallino(p.X(4), p.Y(3), True, NERO, 5)
    s.linea(p.X(-2), p.Y(3), p.X(-2), p.Y(0), GRIGIO, 1.2, "4,3")
    s.linea(p.X(4), p.Y(3), p.X(4), p.Y(0), GRIGIO, 1.2, "4,3")
    s.testo(p.X(-3.2), p.Y(4.6), "y = |x − 1|", 16, BLU, stile="italic", anchor="start")
    s.testo(p.X(6.4), p.Y(3) - 10, "y = 3", 15, ROSSO, stile="italic", anchor="end")
    s.testo(p.X(1), 356, "|x − 1| &lt; 3  per  −2 &lt; x &lt; 4", 15, VERDE, peso="bold")
    s.testo(310, 388, "Il grafico a V sta sotto la retta y = 3 tra i due punti d'incontro.", 14)
    s.salva("01-valore-assoluto")


# ---------------------------------------------------------------- tabella dei segni

def fig_tabella_segni():
    s = SVG(640, 330)
    x0, x1 = 170, 610
    vmin, vmax = -4, 5
    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    punti = [(-2, "−2"), (1, "1"), (3, "3")]
    yr = 40
    s.freccia(x0, yr, x1 + 10, yr, NERO, 1.5)
    for v, n in punti:
        s.testo(X(v), yr - 10, n, 15)
    s.testo(x1 + 4, yr - 10, "x", 15, stile="italic")
    for v, n in punti:
        s.linea(X(v), yr + 8, X(v), 270, GRIGIO, 1, "3,3")
    righe = [
        ("x + 2", -2, False),
        ("x − 1", 1, False),
        ("x − 3", 3, True),
    ]
    for i, (nome, z, denom) in enumerate(righe):
        y = 90 + i * 50
        s.testo(20, y + 5, nome + ("  (den.)" if denom else ""), 15, anchor="start", stile="italic")
        # negativo tratteggiato a sinistra, positivo pieno a destra
        s.linea(X(vmin) + 4, y, X(z), y, ROSSO, 2.5, "6,5")
        s.linea(X(z), y, x1, y, VERDE, 3)
        if denom:
            s.testo(X(z), y + 6, "×", 20, NERO, peso="bold")
        else:
            s.pallino(X(z), y, True, NERO, 4.5)
        # segni negli intervalli
        bordi = [vmin, -2, 1, 3, vmax]
        for k in range(4):
            m = (bordi[k] + bordi[k + 1]) / 2
            seg = "+" if m > z else "−"
            s.testo(X(m), y - 9, seg, 17, VERDE if seg == "+" else ROSSO, peso="bold")
    # riga del risultato
    y = 270
    s.linea(20, y - 25, x1, y - 25, NERO, 1)
    s.testo(20, y + 5, "frazione", 15, anchor="start", peso="bold")
    bordi = [vmin, -2, 1, 3, vmax]
    segni = ["−", "+", "−", "+"]
    for k in range(4):
        m = (bordi[k] + bordi[k + 1]) / 2
        col = VERDE if segni[k] == "+" else ROSSO
        s.testo(X(m), y + 7, segni[k], 22, col, peso="bold")
    s.testo(330, 316, "Soluzione di  (x + 2)(x − 1) / (x − 3) ≥ 0 :   [−2, 1] ∪ (3, +∞)", 15, NERO)
    s.salva("01-tabella-segni")


def fig_sistema():
    s = SVG(640, 265)
    x0, x1 = 200, 600
    tacche = [(-1, "−1"), (2, "2"), (4, "4")]
    s.testo(20, 55, "2x − 4 &gt; 0", 16, anchor="start", stile="italic")
    retta_reale(s, 50, x0, x1, -3, 6, tacche, [(2, None, False, False)], BLU)
    s.testo(20, 115, "x² − 3x − 4 ≤ 0", 16, anchor="start", stile="italic")
    retta_reale(s, 110, x0, x1, -3, 6, tacche, [(-1, 4, True, True)], ARANCIO)
    s.linea(20, 150, x1 + 20, 150, NERO, 1)
    s.testo(20, 195, "sistema", 16, anchor="start", peso="bold")
    retta_reale(s, 190, x0, x1, -3, 6, tacche, [(2, 4, False, True)], VERDE)
    s.testo(330, 252, "Soluzione del sistema: dove valgono tutte e due, cioè 2 &lt; x ≤ 4.", 14)
    s.salva("01-sistema-disequazioni")


if __name__ == "__main__":
    fig_intervalli()
    fig_discriminante()
    fig_parabola_segno()
    fig_irrazionale()
    fig_valore_assoluto()
    fig_tabella_segni()
    fig_sistema()
