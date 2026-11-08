#!/usr/bin/env python3
"""Disegni per la bozza di matematica 02-retta-e-circonferenza.

Genera gli SVG in anno-1/semestre-1/matematica/bozze/img/ con prefisso 03-.
Nessuna dipendenza: python3 -I .claude/scripts/disegni/matematica-03.py
"""
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(QUI, "..", "..", "..",
                                    "anno-1", "semestre-1", "matematica", "bozze", "img"))

BLU = "#1f5fa8"
ROSSO = "#c0392b"
VERDE = "#2e8b57"
ARANCIO = "#d68910"
VIOLA = "#7d3c98"
GRIGIO = "#666666"
NERO = "#222222"
FONT = "Helvetica, Arial, sans-serif"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Piano:
    """Piano cartesiano: coordinate matematiche -> pixel."""

    def __init__(self, xmin, xmax, ymin, ymax, scala=50, margine=40, extra_dx=0):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.s = scala
        self.m = margine
        self.w = (xmax - xmin) * scala + 2 * margine + extra_dx
        self.h = (ymax - ymin) * scala + 2 * margine
        self.el = []
        self.defs = set()

    def px(self, x, y):
        return (self.m + (x - self.xmin) * self.s, self.m + (self.ymax - y) * self.s)

    # --- elementi di base -------------------------------------------------
    def griglia(self, passo=1):
        x = math.ceil(self.xmin)
        while x <= self.xmax:
            a, b = self.px(x, self.ymin), self.px(x, self.ymax)
            self.el.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#e6e6e6" stroke-width="1"/>')
            x += passo
        y = math.ceil(self.ymin)
        while y <= self.ymax:
            a, b = self.px(self.xmin, y), self.px(self.xmax, y)
            self.el.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#e6e6e6" stroke-width="1"/>')
            y += passo

    def freccia(self, x1, y1, x2, y2, colore=NERO, w=1.6, pix=False, testa=10):
        if not pix:
            (x1, y1), (x2, y2) = self.px(x1, y1), self.px(x2, y2)
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - testa * math.cos(ang), y2 - testa * math.sin(ang)
        self.el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{colore}" stroke-width="{w}"/>')
        p1 = (x2, y2)
        p2 = (bx + testa * 0.4 * math.sin(ang), by - testa * 0.4 * math.cos(ang))
        p3 = (bx - testa * 0.4 * math.sin(ang), by + testa * 0.4 * math.cos(ang))
        self.el.append(f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" fill="{colore}"/>')

    def assi(self, tacche=True, numeri=True, passo=1, salta=()):
        o = self.px(0, 0)
        a = self.px(self.xmin, 0)
        b = self.px(self.xmax, 0)
        self.freccia(a[0], a[1], b[0] + 18, b[1], pix=True)
        a = self.px(0, self.ymin)
        b = self.px(0, self.ymax)
        self.freccia(a[0], a[1], b[0], b[1] - 18, pix=True)
        self.testo_px(self.px(self.xmax, 0)[0] + 14, o[1] + 20, "x", 17, corsivo=True)
        self.testo_px(o[0] - 16, self.px(0, self.ymax)[1] - 8, "y", 17, corsivo=True)
        if tacche:
            x = math.ceil(self.xmin)
            while x <= self.xmax:
                if x != 0:
                    p = self.px(x, 0)
                    self.el.append(f'<line x1="{p[0]:.1f}" y1="{p[1]-4:.1f}" x2="{p[0]:.1f}" y2="{p[1]+4:.1f}" stroke="{NERO}" stroke-width="1.2"/>')
                    if numeri and x not in salta and x % passo == 0:
                        self.testo_px(p[0], p[1] + 18, f"{x:g}".replace("-", "−"), 12, colore=GRIGIO, sfondo=True)
                x += 1
            y = math.ceil(self.ymin)
            while y <= self.ymax:
                if y != 0:
                    p = self.px(0, y)
                    self.el.append(f'<line x1="{p[0]-4:.1f}" y1="{p[1]:.1f}" x2="{p[0]+4:.1f}" y2="{p[1]:.1f}" stroke="{NERO}" stroke-width="1.2"/>')
                    if numeri and ("y", y) not in salta and y % passo == 0:
                        self.testo_px(p[0] - 9, p[1] + 4, f"{y:g}".replace("-", "−"), 12, colore=GRIGIO, anc="end", sfondo=True)
                y += 1
            self.testo_px(o[0] - 9, o[1] + 17, "O", 13, colore=GRIGIO, anc="end")

    def testo_px(self, x, y, t, size=15, colore=NERO, anc="middle", corsivo=False, peso="normal", sfondo=False):
        st = ' font-style="italic"' if corsivo else ""
        halo = (f' stroke="white" stroke-width="4" stroke-linejoin="round" paint-order="stroke"' if sfondo else "")
        self.el.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" fill="{colore}" text-anchor="{anc}" font-weight="{peso}"{st}{halo}>{esc(t)}</text>')

    def testo(self, x, y, t, size=15, colore=NERO, anc="middle", dx=0, dy=0, **kw):
        p = self.px(x, y)
        self.testo_px(p[0] + dx, p[1] + dy, t, size, colore, anc, sfondo=True, **kw)

    def segmento(self, x1, y1, x2, y2, colore=NERO, w=2, tratt=False):
        a, b = self.px(x1, y1), self.px(x2, y2)
        d = ' stroke-dasharray="6,4"' if tratt else ""
        self.el.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{colore}" stroke-width="{w}"{d} stroke-linecap="round"/>')

    def retta(self, a, b, c, colore=BLU, w=2.2, tratt=False):
        """Disegna la retta ax + by + c = 0 tagliata al riquadro."""
        pts = []
        X0, X1, Y0, Y1 = self.xmin, self.xmax, self.ymin, self.ymax
        if b != 0:
            for x in (X0, X1):
                y = (-c - a * x) / b
                if Y0 - 1e-9 <= y <= Y1 + 1e-9:
                    pts.append((x, y))
        if a != 0:
            for y in (Y0, Y1):
                x = (-c - b * y) / a
                if X0 - 1e-9 <= x <= X1 + 1e-9:
                    pts.append((x, y))
        if len(pts) < 2:
            return
        pts.sort()
        self.segmento(pts[0][0], pts[0][1], pts[-1][0], pts[-1][1], colore, w, tratt)

    def punto(self, x, y, etichetta="", colore=NERO, dx=8, dy=-8, anc="start", size=15, r=4):
        p = self.px(x, y)
        self.el.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" fill="{colore}" stroke="white" stroke-width="1"/>')
        if etichetta:
            self.testo_px(p[0] + dx, p[1] + dy, etichetta, size, colore, anc, sfondo=True)

    def cerchio(self, cx, cy, r, colore=BLU, w=2.2, riemp="none", tratt=False):
        p = self.px(cx, cy)
        d = ' stroke-dasharray="6,4"' if tratt else ""
        self.el.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r*self.s:.1f}" fill="{riemp}" stroke="{colore}" stroke-width="{w}"{d}/>')

    def poligono(self, pts, riemp="#dfe9f5", bordo="none", w=1.5, opac=1.0):
        s = " ".join(f"{self.px(x, y)[0]:.1f},{self.px(x, y)[1]:.1f}" for x, y in pts)
        self.el.append(f'<polygon points="{s}" fill="{riemp}" fill-opacity="{opac}" stroke="{bordo}" stroke-width="{w}"/>')

    def angolo_retto(self, vx, vy, ux, uy, wx, wy, l=0.3, colore=NERO):
        """Quadratino nel vertice V tra le direzioni u e w (unita' matematiche)."""
        nu = math.hypot(ux, uy)
        nw = math.hypot(wx, wy)
        ux, uy, wx, wy = ux / nu * l, uy / nu * l, wx / nw * l, wy / nw * l
        pts = [(vx + ux, vy + uy), (vx + ux + wx, vy + uy + wy), (vx + wx, vy + wy)]
        s = " ".join(f"{self.px(x, y)[0]:.1f},{self.px(x, y)[1]:.1f}" for x, y in pts)
        self.el.append(f'<polyline points="{s}" fill="none" stroke="{colore}" stroke-width="1.3"/>')

    def arco(self, cx, cy, r, a1, a2, colore=NERO, w=1.5):
        """Arco di raggio r (unita') da a1 a a2 gradi, antiorario."""
        p1 = self.px(cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
        p2 = self.px(cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2)))
        large = 1 if (a2 - a1) % 360 > 180 else 0
        self.el.append(f'<path d="M {p1[0]:.1f} {p1[1]:.1f} A {r*self.s:.1f} {r*self.s:.1f} 0 {large} 0 {p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{colore}" stroke-width="{w}"/>')

    def raw(self, s):
        self.el.append(s)

    def salva(self, nome):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w:.0f}" height="{self.h:.0f}" '
               f'viewBox="0 0 {self.w:.0f} {self.h:.0f}">\n'
               f'<rect width="100%" height="100%" fill="white"/>\n' + "\n".join(self.el) + "\n</svg>\n")
        with open(os.path.join(OUT, nome), "w", encoding="utf-8") as f:
            f.write(svg)
        print("scritto", nome)


class Spazio:
    """Assonometria semplice per le figure 3D (x verso chi guarda, y a destra, z in alto)."""

    def __init__(self, w, h, ox, oy, s=45):
        self.w, self.h, self.ox, self.oy, self.s = w, h, ox, oy, s
        self.el = []
        self.kx = (-0.62 * s, 0.42 * s)  # direzione dell'asse x sul foglio

    def px(self, x, y, z):
        return (self.ox + x * self.kx[0] + y * self.s, self.oy + x * self.kx[1] - z * self.s)

    def seg(self, a, b, colore=NERO, w=1.8, tratt=False):
        p, q = self.px(*a), self.px(*b)
        d = ' stroke-dasharray="5,4"' if tratt else ""
        self.el.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{colore}" stroke-width="{w}"{d} stroke-linecap="round"/>')

    def freccia(self, a, b, colore=NERO, w=1.6):
        (x1, y1), (x2, y2) = self.px(*a), self.px(*b)
        ang = math.atan2(y2 - y1, x2 - x1)
        t = 10
        bx, by = x2 - t * math.cos(ang), y2 - t * math.sin(ang)
        self.el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{colore}" stroke-width="{w}"/>')
        p2 = (bx + 4 * math.sin(ang), by - 4 * math.cos(ang))
        p3 = (bx - 4 * math.sin(ang), by + 4 * math.cos(ang))
        self.el.append(f'<polygon points="{x2:.1f},{y2:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" fill="{colore}"/>')

    def testo(self, P, t, size=15, colore=NERO, anc="middle", dx=0, dy=0, corsivo=False):
        p = self.px(*P)
        st = ' font-style="italic"' if corsivo else ""
        self.el.append(f'<text x="{p[0]+dx:.1f}" y="{p[1]+dy:.1f}" font-family="{FONT}" font-size="{size}" fill="{colore}" text-anchor="{anc}" stroke="white" stroke-width="4" stroke-linejoin="round" paint-order="stroke"{st}>{esc(t)}</text>')

    def punto(self, P, colore=NERO, r=4):
        p = self.px(*P)
        self.el.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" fill="{colore}" stroke="white" stroke-width="1"/>')

    def poligono(self, pts, riemp, opac=0.5):
        s = " ".join(f"{self.px(*P)[0]:.1f},{self.px(*P)[1]:.1f}" for P in pts)
        self.el.append(f'<polygon points="{s}" fill="{riemp}" fill-opacity="{opac}" stroke="none"/>')

    def assi(self, lx, ly, lz):
        self.freccia((0, 0, 0), (lx, 0, 0))
        self.freccia((0, 0, 0), (0, ly, 0))
        self.freccia((0, 0, 0), (0, 0, lz))
        self.testo((lx, 0, 0), "x", 17, corsivo=True, dx=-8, dy=16)
        self.testo((0, ly, 0), "y", 17, corsivo=True, dx=12, dy=6)
        self.testo((0, 0, lz), "z", 17, corsivo=True, dx=-12, dy=4)
        self.testo((0, 0, 0), "O", 13, GRIGIO, dx=-12, dy=-6)

    def raw(self, s):
        self.el.append(s)

    def salva(self, nome):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">\n'
               f'<rect width="100%" height="100%" fill="white"/>\n' + "\n".join(self.el) + "\n</svg>\n")
        with open(os.path.join(OUT, nome), "w", encoding="utf-8") as f:
            f.write(svg)
        print("scritto", nome)


# ---------------------------------------------------------------------------
# 1. Piano cartesiano e quadranti
def piano_cartesiano():
    p = Piano(-5, 5, -4, 4, scala=46)
    p.poligono([(0, 0), (5, 0), (5, 4), (0, 4)], "#eaf1fa")
    p.poligono([(0, 0), (-5, 0), (-5, -4), (0, -4)], "#eaf1fa")
    p.griglia()
    p.assi()
    for (x, y, t, s) in [(3.8, 3.3, "I quadrante", "(+, +)"), (-3.8, 3.3, "II quadrante", "(−, +)"),
                         (-3.8, -2.7, "III quadrante", "(−, −)"), (3.8, -2.7, "IV quadrante", "(+, −)")]:
        p.testo(x, y, t, 14, GRIGIO)
        p.testo(x, y, s, 14, GRIGIO, dy=18)
    # P(3, 2)
    p.segmento(3, 0, 3, 2, BLU, 1.4, True)
    p.segmento(0, 2, 3, 2, BLU, 1.4, True)
    p.punto(3, 2, "P(3, 2)", BLU)
    # Q(-2, -1)
    p.segmento(-2, 0, -2, -1, ROSSO, 1.4, True)
    p.segmento(0, -1, -2, -1, ROSSO, 1.4, True)
    p.punto(-2, -1, "Q(−2, −1)", ROSSO, dx=-8, dy=20, anc="end")
    p.salva("03-piano-cartesiano.svg")


# 2. Distanza con Pitagora
def distanza():
    p = Piano(-1, 7, -3, 3, scala=55)
    p.griglia()
    p.assi()
    p.poligono([(1, -1), (5, -1), (5, 1)], "#fdf2e0")
    p.segmento(1, -1, 5, -1, ARANCIO, 2.4)
    p.segmento(5, -1, 5, 1, VERDE, 2.4)
    p.segmento(1, -1, 5, 1, BLU, 3)
    p.angolo_retto(5, -1, -1, 0, 0, 1, 0.3)
    p.punto(1, -1, "A(1, −1)", NERO, dx=-8, dy=20, anc="end")
    p.punto(5, 1, "B(5, 1)", NERO, dx=8, dy=-8)
    p.testo(3, -1, "x_B − x_A = 4".replace("_B", "ʙ"), 14, ARANCIO, dy=22)
    p.el.pop()  # sostituito sotto con pedici leggibili
    p.testo(3, -1, "Δx = 5 − 1 = 4", 14, ARANCIO, dy=22)
    p.testo(5, -0.5, "Δy = 1 − (−1) = 2", 14, VERDE, anc="start", dx=10, dy=5)
    p.testo(2.6, 0.55, "d = √(4² + 2²) = √20", 15, BLU, anc="middle")
    p.salva("03-distanza-pitagora.svg")


# 3. Punto medio
def punto_medio():
    p = Piano(-1, 7, -3, 3, scala=55)
    p.griglia()
    p.assi()
    p.segmento(1, -1, 5, 1, BLU, 2.6)
    for x, y in [(1, -1), (3, 0), (5, 1)]:
        p.segmento(x, y, x, -2.6, GRIGIO, 1, True)
    p.punto(1, -1, "A(1, −1)", NERO, dx=-8, dy=-8, anc="end")
    p.punto(5, 1, "B(5, 1)", NERO, dx=8, dy=-8)
    p.punto(3, 0, "M(3, 0)", ROSSO, dx=-6, dy=-12, anc="end")
    p.testo(2, -2.6, "2", 14, ARANCIO, dy=-6)
    p.testo(4, -2.6, "2", 14, ARANCIO, dy=-6)
    p.segmento(1, -2.6, 5, -2.6, ARANCIO, 1.6)
    p.testo(3, -2.6, "x_M = (1 + 5) / 2 = 3".replace("x_M", "xₘ"), 14, ARANCIO, dy=20)
    p.salva("03-punto-medio.svg")


# 4. Valore assoluto come distanza sulla retta dei numeri
def valore_assoluto():
    W, H = 760, 230
    p = Piano(-6, 6, 0, 1, scala=56, margine=40)
    p.h = H
    y0 = 95
    def X(x):
        return p.px(x, 0)[0]
    p.freccia(X(-6.2), y0, X(6.2) + 10, y0, pix=True)
    for x in range(-6, 7):
        p.raw(f'<line x1="{X(x):.1f}" y1="{y0-5}" x2="{X(x):.1f}" y2="{y0+5}" stroke="{NERO}" stroke-width="1.2"/>')
        p.testo_px(X(x), y0 + 22, f"{x}".replace("-", "−"), 13, GRIGIO)
    # |−4| = 4 : distanza da 0
    p.raw(f'<line x1="{X(-4):.1f}" y1="{y0-30}" x2="{X(0):.1f}" y2="{y0-30}" stroke="{ROSSO}" stroke-width="2.4"/>')
    for x in (-4, 0):
        p.raw(f'<line x1="{X(x):.1f}" y1="{y0-36}" x2="{X(x):.1f}" y2="{y0-24}" stroke="{ROSSO}" stroke-width="2"/>')
    p.testo_px(X(-2), y0 - 42, "|−4| = 4", 15, ROSSO)
    p.testo_px(X(-2), y0 - 62, "distanza di −4 da 0", 13, ROSSO)
    # |5 − 2| = 3 : distanza tra 2 e 5
    p.raw(f'<line x1="{X(2):.1f}" y1="{y0-30}" x2="{X(5):.1f}" y2="{y0-30}" stroke="{BLU}" stroke-width="2.4"/>')
    for x in (2, 5):
        p.raw(f'<line x1="{X(x):.1f}" y1="{y0-36}" x2="{X(x):.1f}" y2="{y0-24}" stroke="{BLU}" stroke-width="2"/>')
    p.testo_px(X(3.5), y0 - 42, "|5 − 2| = 3", 15, BLU)
    p.testo_px(X(3.5), y0 - 62, "distanza tra 2 e 5", 13, BLU)
    # |x| < 3 : intervallo
    yb = y0 + 75
    p.raw(f'<line x1="{X(-3):.1f}" y1="{yb}" x2="{X(3):.1f}" y2="{yb}" stroke="{VERDE}" stroke-width="5" stroke-linecap="butt"/>')
    for x in (-3, 3):
        p.raw(f'<circle cx="{X(x):.1f}" cy="{yb}" r="5" fill="white" stroke="{VERDE}" stroke-width="2"/>')
    p.testo_px(X(0), yb + 26, "|x| < 3 : i numeri che distano da 0 meno di 3, cioè −3 < x < 3", 14, VERDE)
    p.salva("03-valore-assoluto-distanza.svg")


# 5. Coordinate e distanza nello spazio
def coordinate_spazio():
    S = Spazio(620, 440, 250, 300, s=50)
    P = (3, 4, 3)
    # parallelepipedo tratteggiato
    x, y, z = P
    base = [(0, 0, 0), (x, 0, 0), (x, y, 0), (0, y, 0)]
    S.poligono(base, "#eaf1fa", 0.9)
    S.assi(4.6, 5.8, 4.4)
    S.seg((x, 0, 0), (x, y, 0), GRIGIO, 1.2, True)
    S.seg((0, y, 0), (x, y, 0), GRIGIO, 1.2, True)
    S.seg((x, y, 0), (x, y, z), ROSSO, 2.2)
    S.seg((0, 0, 0), (x, y, 0), VERDE, 2.2)
    S.seg((0, 0, 0), (x, y, z), BLU, 2.8)
    S.seg((0, y, 0), (0, y, z), GRIGIO, 1.2, True)
    S.seg((0, y, z), (x, y, z), GRIGIO, 1.2, True)
    S.seg((0, 0, z), (0, y, z), GRIGIO, 1.2, True)
    S.seg((x, 0, 0), (x, 0, z), GRIGIO, 1.2, True)
    S.seg((x, 0, z), (x, y, z), GRIGIO, 1.2, True)
    S.seg((0, 0, z), (x, 0, z), GRIGIO, 1.2, True)
    S.punto(P, BLU)
    S.testo(P, "P(x, y, z)", 15, BLU, anc="start", dx=10, dy=-6)
    S.punto((x, y, 0), VERDE)
    S.testo((x, y, 0), "H(x, y, 0)", 14, VERDE, anc="start", dx=8, dy=18)
    S.testo((x, 0, 0), "x", 15, GRIGIO, dx=-10, dy=14, corsivo=True)
    S.testo((0, y, 0), "y", 15, GRIGIO, dx=0, dy=20, corsivo=True)
    S.testo((0, 0, z), "z", 15, GRIGIO, dx=-12, dy=4, corsivo=True)
    S.testo((x / 2, y / 2, 0), "√(x² + y²)", 14, VERDE, dx=-4, dy=22)
    S.testo((x, y, z / 2), "z", 15, ROSSO, anc="start", dx=8, corsivo=True)
    S.testo((x / 2, y / 2, z / 2), "d = √(x² + y² + z²)", 15, BLU, anc="end", dx=-12, dy=-14)
    S.salva("03-coordinate-spazio.svg")


# 6. Pendenza
def pendenza():
    p = Piano(-1, 8, -1, 6, scala=55)
    p.griglia()
    p.assi()
    # retta per A(1,1) e B(6,4): m = 3/5
    m = 3 / 5
    p.retta(m, -1, 1 - m)
    p.poligono([(1, 1), (6, 1), (6, 4)], "#fdf2e0", opac=0.8)
    p.segmento(1, 1, 6, 1, ARANCIO, 2.4)
    p.segmento(6, 1, 6, 4, VERDE, 2.4)
    p.angolo_retto(6, 1, -1, 0, 0, 1)
    p.retta(m, -1, 1 - m)
    p.punto(1, 1, "A(1, 1)", NERO, dx=-6, dy=-10, anc="end")
    p.punto(6, 4, "B(6, 4)", NERO, dx=-10, dy=-8, anc="end")
    p.testo(3.5, 1, "Δx = 6 − 1 = 5", 14, ARANCIO, dy=22)
    p.testo(6, 2.5, "Δy = 4 − 1 = 3", 14, VERDE, anc="start", dx=10, dy=5)
    # angolo alfa con l'asse x: la retta taglia l'asse x in x = -2/3
    x0 = -(1 - m) / m
    p.arco(1, 1, 1.1, 0, math.degrees(math.atan(m)), ROSSO, 1.8)
    p.testo(2.25, 1.32, "α", 16, ROSSO)
    p.testo(4.3, 5.2, "m = Δy / Δx = 3/5 = tg α", 16, BLU)
    p.salva("03-pendenza.svg")


# 7. Rette con pendenze diverse
def pendenze_confronto():
    p = Piano(-5, 5, -4, 4, scala=46, extra_dx=0)
    p.griglia()
    p.assi(numeri=False)
    casi = [(2, ROSSO, "m = 2"), (1, ARANCIO, "m = 1"), (0.5, VERDE, "m = 1/2"),
            (0, GRIGIO, "m = 0"), (-1, VIOLA, "m = −1")]
    for m, col, t in casi:
        p.retta(m, -1, 0, col, 2.2)
    p.testo(2.0, 3.6, "m = 2", 14, ROSSO, anc="start", dx=6)
    p.testo(4.9, 3.0, "m = 1", 14, ARANCIO, anc="end")
    p.testo(4.2, 2.1, "m = 1/2", 14, VERDE, anc="end", dy=-10)
    p.testo(4.9, 0, "m = 0", 14, GRIGIO, anc="end", dy=-8)
    p.testo(-2.0, 3.6, "m = −1", 14, VIOLA, anc="start")
    p.testo(-4.9, -2.6, "m > 0: la retta sale", 13, GRIGIO, anc="start")
    p.testo(-4.9, -2.6, "m < 0: la retta scende", 13, GRIGIO, anc="start", dy=18)
    p.testo(-4.9, -2.6, "più |m| è grande, più è ripida", 13, GRIGIO, anc="start", dy=36)
    p.salva("03-pendenze-confronto.svg")


# 8. Rampa
def rampa():
    W, H = 760, 300
    p = Piano(0, 13, -1, 2.8, scala=52, margine=30)
    el = p.el
    a = p.px(0.5, 0)
    b = p.px(12.5, 0)
    c = p.px(12.5, 1)
    el.append(f'<polygon points="{a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f}" fill="#efe6d6" stroke="#8a7a5a" stroke-width="2"/>')
    # piano rialzato
    d = p.px(12.5, 1)
    e = p.px(13, 1)
    f = p.px(13, 0)
    el.append(f'<polygon points="{d[0]:.1f},{d[1]:.1f} {e[0]:.1f},{e[1]:.1f} {f[0]:.1f},{f[1]:.1f} {b[0]:.1f},{b[1]:.1f}" fill="#d8ccb4" stroke="#8a7a5a" stroke-width="2"/>')
    p.segmento(0, 0, 13, 0, NERO, 2)
    # quote
    p.segmento(0.5, -0.45, 12.5, -0.45, ARANCIO, 1.4)
    p.segmento(0.5, -0.3, 0.5, -0.6, ARANCIO, 1.4)
    p.segmento(12.5, -0.3, 12.5, -0.6, ARANCIO, 1.4)
    p.testo(6.5, -0.45, "lunghezza in pianta: 12 m (Δx)", 14, ARANCIO, dy=20)
    p.segmento(12.5, 0, 12.5, 1, VERDE, 2.4)
    p.testo(12.5, 1.45, "dislivello 1 m (Δy)", 14, VERDE, anc="end")
    p.arco(0.5, 0, 2.2, 0, math.degrees(math.atan(1 / 12)), ROSSO, 1.6)
    p.testo(2.95, 0.05, "α", 15, ROSSO, dy=-2)
    p.testo(6.5, 2.4, "pendenza = 1 / 12 ≈ 0,083 = 8,3%", 16, BLU)
    p.salva("03-rampa.svg")


# 9. Il ruolo di q
def ruolo_q():
    p = Piano(-5, 5, -4, 4, scala=46)
    p.griglia()
    p.assi(numeri=False)
    for q, col in [(2, ROSSO), (0, BLU), (-3, VERDE)]:
        p.retta(0.5, -1, q, col)
        p.punto(0, q, f"q = {q}".replace("-", "−"), col, dx=-8 if q != -3 else 10, dy=-8 if q != -3 else 20, anc="end" if q != -3 else "start")
    p.testo(2.2, 2.4, "y = ½x + 2", 14, ROSSO, anc="start")
    p.testo(4.9, 2.5, "y = ½x", 14, BLU, anc="end", dy=-6)
    p.testo(4.9, -0.5, "y = ½x − 3", 14, VERDE, anc="end", dy=-10)
    p.testo(-2.6, 3.4, "stessa m = ½: rette parallele", 13, GRIGIO)
    p.salva("03-ruolo-di-q.svg")


# 10. Rette orizzontali e verticali
def orizz_vert():
    p = Piano(-5, 5, -4, 4, scala=46)
    p.griglia()
    p.assi()
    p.retta(0, 1, -2, BLU)       # y = 2
    p.retta(1, 0, 3, ROSSO)      # x = -3
    p.testo(4.8, 2, "y = 2  (m = 0)", 15, BLU, anc="end", dy=-10)
    p.testo(-3, -3.3, "x = −3", 15, ROSSO, anc="start", dx=8)
    p.testo(-3, -3.3, "(pendenza non definita)", 13, ROSSO, anc="start", dx=8, dy=18)
    p.punto(-3, 2, "(−3, 2)", NERO, dx=8, dy=-8)
    p.salva("03-orizzontali-verticali.svg")


# 11. Retta per due punti
def retta_due_punti():
    p = Piano(-2, 7, -3, 3, scala=55)
    p.griglia()
    p.assi()
    p.retta(1, -2, -3, BLU)   # x - 2y - 3 = 0, cioe' y = x/2 - 3/2
    p.punto(1, -1, "A(1, −1)", NERO, dx=8, dy=20, anc="start")
    p.punto(5, 1, "B(5, 1)", NERO, dx=-6, dy=-10, anc="end")
    p.punto(0, -1.5, "q = −3/2", ROSSO, dx=-8, dy=-8, anc="end")
    p.punto(3, 0, "", GRIGIO)
    p.testo(6.4, 2.35, "y = ½x − 3/2", 15, BLU, anc="end")
    p.salva("03-retta-due-punti.svg")


# 12. Parallele e perpendicolari
def par_perp():
    p = Piano(-5, 5, -4, 4, scala=46)
    p.griglia()
    p.assi(numeri=False)
    p.retta(2, -1, 1, BLU)       # y = 2x + 1
    p.retta(2, -1, -3, VERDE)    # y = 2x - 3
    p.retta(-0.5, -1, 1, ROSSO)  # y = -x/2 + 1
    # intersezione r e t: 2x+1 = -x/2+1 -> x=0, y=1
    p.angolo_retto(0, 1, 1, 2, 2, -1, 0.35)
    p.testo(-2.3, -3.1, "r: y = 2x + 1", 14, BLU, anc="end")
    p.testo(3.3, 3.4, "s: y = 2x − 3", 14, VERDE, anc="start", dx=6)
    p.testo(-4.8, 3.4, "t: y = −½x + 1", 14, ROSSO, anc="start", dy=-6)
    p.testo(2.6, -3.1, "r ∥ s : stessa pendenza 2", 13, GRIGIO, anc="start", dx=-20)
    p.testo(2.6, -3.1, "r ⊥ t : 2 · (−½) = −1", 13, GRIGIO, anc="start", dx=-20, dy=18)
    p.salva("03-parallele-perpendicolari.svg")


# 13. Perche' m1 m2 = -1
def perche_perp():
    p = Piano(-3, 4, -1, 4, scala=60)
    p.griglia()
    p.assi(numeri=False)
    m = 2
    # triangolo 1: da O, 1 a destra, m in su
    p.poligono([(0, 0), (1, 0), (1, m)], "#dfe9f5", BLU, 1.2, 0.8)
    p.segmento(0, 0, 1, m, BLU, 2.6)
    # triangolo ruotato di 90 gradi: (1,0)->(0,1), (1,m)->(-m,1)
    p.poligono([(0, 0), (0, 1), (-m, 1)], "#f8e0dd", ROSSO, 1.2, 0.8)
    p.segmento(0, 0, -m, 1, ROSSO, 2.6)
    p.retta(m, -1, 0, BLU, 1.2, True)
    p.retta(1, m, 0, ROSSO, 1.2, True)
    p.angolo_retto(0, 0, 1, m, -m, 1, 0.3)
    p.testo(0.5, 0, "1", 14, BLU, dy=-6)
    p.testo(1, 1, "m", 15, BLU, anc="start", dx=8, corsivo=True)
    p.testo(0, 0.5, "1", 14, ROSSO, anc="end", dx=-6)
    p.testo(-1, 1, "m", 15, ROSSO, dy=-10, corsivo=True)
    p.punto(1, m, "(1, m)", BLU, dx=10, dy=0)
    p.punto(-m, 1, "(−m, 1)", ROSSO, dx=-4, dy=24, anc="end")
    p.testo(2.6, 2.6, "pendenza m", 14, BLU)
    p.testo(-1.9, 2.6, "pendenza 1/(−m) = −1/m", 14, ROSSO)
    p.salva("03-perpendicolari-perche.svg")


# 14. Intersezione di due rette
def intersezione():
    p = Piano(-2, 6, -2, 5, scala=52)
    p.griglia()
    p.assi()
    p.retta(1, 1, -5, BLU)     # x + y = 5
    p.retta(2, -1, -1, ROSSO)  # 2x - y = 1
    p.punto(2, 3, "P(2, 3)", NERO, dx=10, dy=-4)
    p.segmento(2, 0, 2, 3, GRIGIO, 1.2, True)
    p.segmento(0, 3, 2, 3, GRIGIO, 1.2, True)
    p.testo(4.0, 1.8, "x + y = 5", 14, BLU, anc="start", dx=8)
    p.testo(3.0, 4.6, "2x − y = 1", 14, ROSSO, anc="start", dx=8)
    p.salva("03-intersezione.svg")


# 15. Distanza punto-retta (esercizio 22 del prof)
def dist_punto_retta():
    p = Piano(-1, 6, -1, 4, scala=60)
    p.griglia()
    p.assi()
    p.retta(2, -1, -2, BLU)        # 2x - y - 2 = 0
    p.segmento(4, 1, 2, 2, ROSSO, 2.6)
    p.angolo_retto(2, 2, 1, 2, 2, -1, 0.25)
    p.punto(1, 0, "A(1, 0)", NERO, dx=-10, dy=-8, anc="end")
    p.punto(4, 1, "P(4, 1)", NERO, dx=8, dy=6)
    p.punto(2, 2, "H(2, 2)", NERO, dx=-10, dy=-4, anc="end")
    p.testo(3.2, 1.85, "d = √5", 15, ROSSO, anc="start")
    p.testo(3.1, 3.6, "r: 2x − y − 2 = 0", 14, BLU, anc="start", dx=6)
    p.salva("03-distanza-punto-retta.svg")


# 16. Circonferenza: definizione
def circ_definizione():
    p = Piano(-1, 7, -1, 6, scala=52)
    p.griglia()
    p.assi(numeri=False)
    cx, cy, r = 3, 2.5, 2.5
    p.cerchio(cx, cy, r, BLU)
    a = math.radians(37)
    px_, py_ = cx + r * math.cos(a), cy + r * math.sin(a)
    p.poligono([(cx, cy), (px_, cy), (px_, py_)], "#fdf2e0", opac=0.8)
    p.segmento(cx, cy, px_, cy, ARANCIO, 2.2)
    p.segmento(px_, cy, px_, py_, VERDE, 2.2)
    p.segmento(cx, cy, px_, py_, ROSSO, 2.6)
    p.angolo_retto(px_, cy, -1, 0, 0, 1, 0.22)
    p.punto(cx, cy, "C(x₀, y₀)", NERO, dx=-8, dy=20, anc="end")
    p.punto(px_, py_, "P(x, y)", NERO, dx=8, dy=-8)
    p.testo((cx + px_) / 2, cy, "x − x₀", 14, ARANCIO, dy=20)
    p.testo(px_, (cy + py_) / 2, "y − y₀", 14, VERDE, anc="start", dx=8, dy=5)
    p.testo((cx + px_) / 2, (cy + py_) / 2, "r", 17, ROSSO, dx=-10, dy=-6, corsivo=True)
    p.testo(3, 5.6, "(x − x₀)² + (y − y₀)² = r²", 15, BLU)
    p.salva("03-circonferenza-definizione.svg")


# 17. Esempio: x^2 + y^2 - 4x + 2y - 4 = 0
def circ_esempio():
    p = Piano(-2, 6, -5, 3, scala=48)
    p.griglia()
    p.assi()
    p.cerchio(2, -1, 3, BLU)
    p.punto(2, -1, "C(2, −1)", NERO, dx=8, dy=18)
    p.segmento(2, -1, 5, -1, ROSSO, 2.4)
    p.testo(3.5, -1, "r = 3", 14, ROSSO, dy=-8)
    p.testo(2, 2.6, "x² + y² − 4x + 2y − 4 = 0", 14, BLU, dy=4)
    p.salva("03-circonferenza-esempio.svg")


# 18. Posizioni retta-circonferenza
def retta_circ_casi():
    p = Piano(0, 15, 0, 5.4, scala=48)
    el = p.el
    r = 1.6
    centri = [(2.5, 2.6), (7.5, 2.6), (12.5, 2.6)]
    titoli = [("secante", "d < r : 2 punti", ROSSO), ("tangente", "d = r : 1 punto", VERDE),
              ("esterna", "d > r : nessun punto", GRIGIO)]
    dist = [0.8, 1.6, 2.3]
    for (cx, cy), (t1, t2, col), d in zip(centri, titoli, dist):
        p.cerchio(cx, cy, r, BLU)
        p.punto(cx, cy, "C", NERO, dx=-6, dy=16, anc="end")
        yl = cy + d
        p.segmento(cx - 2.3, yl, cx + 2.3, yl, col, 2.4)
        p.segmento(cx, cy, cx, yl, ARANCIO, 1.8, True)
        p.angolo_retto(cx, yl, 1, 0, 0, -1, 0.18, ARANCIO)
        p.testo(cx, cy + d / 2, "d", 15, ARANCIO, anc="start", dx=6, dy=5, corsivo=True)
        if d < r:
            h = math.sqrt(r * r - d * d)
            p.punto(cx - h, yl, "", col)
            p.punto(cx + h, yl, "", col)
        elif d == r:
            p.punto(cx, yl, "", col)
        p.testo(cx, 0.55, t1, 15, col, peso="bold")
        p.testo(cx, 0.55, t2, 13, NERO, dy=20)
    p.h += 10
    p.salva("03-retta-circonferenza.svg")


# 19. Esempio secante: x^2+y^2 = 25, y = x + 1
def esempio_secante():
    p = Piano(-6, 6, -6, 6, scala=36)
    p.griglia()
    p.assi(passo=2)
    p.cerchio(0, 0, 5, BLU)
    p.retta(1, -1, 1, ROSSO)
    p.punto(3, 4, "(3, 4)", NERO, dx=8, dy=-6)
    p.punto(-4, -3, "(−4, −3)", NERO, dx=-12, dy=-6, anc="end")
    p.testo(-3.4, 4.6, "x² + y² = 25", 14, BLU, dy=-4)
    p.testo(5.9, 4.3, "y = x + 1", 14, ROSSO, anc="end")
    p.salva("03-esempio-secante.svg")


# 20. Sfera nello spazio
def sfera():
    S = Spazio(560, 430, 230, 290, s=46)
    C = (1, 3.4, 2.3)
    r = 1.7
    S.assi(4, 6.4, 5)
    c = S.px(*C)
    R = r * 46
    S.raw(f'<defs><radialGradient id="g" cx="0.35" cy="0.35" r="0.75"><stop offset="0" stop-color="#ffffff"/>'
          f'<stop offset="1" stop-color="#a9c6e8"/></radialGradient></defs>')
    S.raw(f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{R:.1f}" fill="url(#g)" stroke="{BLU}" stroke-width="2"/>')
    # equatore (ellisse): meta' dietro tratteggiata
    S.raw(f'<path d="M {c[0]-R:.1f} {c[1]:.1f} A {R:.1f} {R*0.3:.1f} 0 0 1 {c[0]+R:.1f} {c[1]:.1f}" fill="none" stroke="{BLU}" stroke-width="1.2" stroke-dasharray="5,4"/>')
    S.raw(f'<path d="M {c[0]-R:.1f} {c[1]:.1f} A {R:.1f} {R*0.3:.1f} 0 0 0 {c[0]+R:.1f} {c[1]:.1f}" fill="none" stroke="{BLU}" stroke-width="1.4"/>')
    # raggio verso un punto P
    a = math.radians(40)
    Pp = (c[0] + R * math.cos(a), c[1] - R * math.sin(a))
    S.raw(f'<line x1="{c[0]:.1f}" y1="{c[1]:.1f}" x2="{Pp[0]:.1f}" y2="{Pp[1]:.1f}" stroke="{ROSSO}" stroke-width="2.4"/>')
    S.raw(f'<circle cx="{Pp[0]:.1f}" cy="{Pp[1]:.1f}" r="4" fill="{NERO}"/>')
    S.raw(f'<text x="{Pp[0]+8:.1f}" y="{Pp[1]-6:.1f}" font-family="{FONT}" font-size="15" fill="{NERO}">P(x, y, z)</text>')
    S.raw(f'<text x="{(c[0]+Pp[0])/2-4:.1f}" y="{(c[1]+Pp[1])/2-6:.1f}" font-family="{FONT}" font-size="16" font-style="italic" fill="{ROSSO}" text-anchor="end">r</text>')
    S.punto(C)
    S.raw(f'<text x="{c[0]:.1f}" y="{c[1]+44:.1f}" font-family="{FONT}" font-size="14" fill="{NERO}" text-anchor="middle">C(x₀, y₀, z₀)</text>')
    S.raw(f'<text x="{S.w/2:.0f}" y="{S.h-18:.0f}" font-family="{FONT}" font-size="15" fill="{BLU}" text-anchor="middle">(x − x₀)² + (y − y₀)² + (z − z₀)² = r²</text>')
    S.salva("03-sfera.svg")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    piano_cartesiano()
    distanza()
    punto_medio()
    valore_assoluto()
    coordinate_spazio()
    pendenza()
    pendenze_confronto()
    rampa()
    ruolo_q()
    orizz_vert()
    retta_due_punti()
    par_perp()
    perche_perp()
    intersezione()
    dist_punto_retta()
    circ_definizione()
    circ_esempio()
    retta_circ_casi()
    esempio_secante()
    sfera()
