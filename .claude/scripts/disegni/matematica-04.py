#!/usr/bin/env python3
"""Disegni per la bozza di matematica 04-le-funzioni.

Uso: python3 -I .claude/scripts/disegni/matematica-04.py
Le immagini SVG vanno in anno-1/semestre-1/matematica/bozze/img/ (prefisso 04-).
Nessuna dipendenza esterna.
"""
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(QUI, "..", "..", "..", "anno-1", "semestre-1",
                                    "matematica", "bozze", "img"))
os.makedirs(OUT, exist_ok=True)

BLU = "#1f5fa8"
ROSSO = "#c0392b"
VERDE = "#2e8b57"
ARANCIO = "#d4810f"
VIOLA = "#7d3c98"
GRIGIO = "#888888"
NERO = "#222222"
FONT = "Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.el = []
        self.nclip = 0
        self.colori = set()

    def marker(self, color):
        self.colori.add(color)
        return f"url(#fr{color[1:]})"

    def add(self, s):
        self.el.append(s)

    def text(self, x, y, s, color=NERO, size=15, anchor="start", italic=False, bold=False):
        st = ' font-style="italic"' if italic else ""
        bw = ' font-weight="bold"' if bold else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
                 f'fill="{color}" text-anchor="{anchor}"{st}{bw}>{esc(s)}</text>')

    def line(self, x1, y1, x2, y2, color=NERO, width=1.5, dash=None, arrow=False):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = f' marker-end="{self.marker(color)}"' if arrow else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{color}" stroke-width="{width}"{d}{m}/>')

    def save(self, nome):
        testa = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                 f'viewBox="0 0 {self.w} {self.h}">\n'
                 '<defs>' + "".join(
                     f'<marker id="fr{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" '
                     'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                     f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in sorted(self.colori))
                 + '</defs>\n'
                 f'<rect width="{self.w}" height="{self.h}" fill="white"/>\n')
        with open(os.path.join(OUT, nome), "w", encoding="utf-8") as f:
            f.write(testa + "\n".join(self.el) + "\n</svg>\n")
        print("scritto", nome)


class Grafico:
    """Un riquadro con assi cartesiani dentro un SVG."""

    def __init__(self, svg, x0, y0, w, h, xr, yr, titolo=None, passo=1, etich=None,
                 xlab="x", ylab="y", colore_titolo=NERO):
        self.s = svg
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xr, self.yr = xr, yr
        svg.nclip += 1
        self.clip = f"clip{svg.nclip}"
        svg.add(f'<clipPath id="{self.clip}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}"/></clipPath>')
        if titolo:
            svg.text(x0 + w / 2, y0 - 12, titolo, colore_titolo, 16, "middle", bold=True)
        # griglia
        for k in range(math.ceil(xr[0]), math.floor(xr[1]) + 1):
            if k % passo == 0:
                svg.line(self.X(k), y0, self.X(k), y0 + h, "#e6e6e6", 1)
        for k in range(math.ceil(yr[0]), math.floor(yr[1]) + 1):
            if k % passo == 0:
                svg.line(x0, self.Y(k), x0 + w, self.Y(k), "#e6e6e6", 1)
        # assi
        ya = self.Y(0) if yr[0] <= 0 <= yr[1] else y0 + h
        xa = self.X(0) if xr[0] <= 0 <= xr[1] else x0
        svg.line(x0, ya, x0 + w, ya, NERO, 1.4, arrow=True)
        svg.line(xa, y0 + h, xa, y0, NERO, 1.4, arrow=True)
        svg.text(x0 + w - 4, ya + 18, xlab, NERO, 15, "end", italic=True)
        svg.text(xa + 8, y0 + 13, ylab, NERO, 15, "start", italic=True)
        etich = etich if etich is not None else passo
        if etich:
            for k in range(math.ceil(xr[0]), math.floor(xr[1]) + 1):
                if k != 0 and k % etich == 0 and self.X(k) < x0 + w - 18:
                    svg.line(self.X(k), ya - 3, self.X(k), ya + 3, NERO, 1)
                    svg.text(self.X(k), ya + 16, str(k).replace("-", "−"), "#555", 12, "middle")
            for k in range(math.ceil(yr[0]), math.floor(yr[1]) + 1):
                if k != 0 and k % etich == 0 and self.Y(k) > y0 + 18:
                    svg.line(xa - 3, self.Y(k), xa + 3, self.Y(k), NERO, 1)
                    svg.text(xa - 6, self.Y(k) + 4, str(k).replace("-", "−"), "#555", 12, "end")
            if xr[0] < 0 < xr[1] and yr[0] < 0 < yr[1]:
                svg.text(xa - 6, ya + 16, "0", "#555", 12, "end")

    def X(self, x):
        return self.x0 + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * self.w

    def Y(self, y):
        return self.y0 + self.h - (y - self.yr[0]) / (self.yr[1] - self.yr[0]) * self.h

    def curva(self, f, a, b, color=BLU, width=2.6, n=500, dash=None):
        pezzi, cur = [], []
        ylim = (self.yr[1] - self.yr[0]) * 3
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError):
                y = None
            if y is None or abs(y) > ylim + abs(self.yr[0]) + abs(self.yr[1]):
                if len(cur) > 1:
                    pezzi.append(cur)
                cur = []
                continue
            cur.append((self.X(x), self.Y(y)))
        if len(cur) > 1:
            pezzi.append(cur)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        for p in pezzi:
            pts = " ".join(f"{u:.1f},{v:.1f}" for u, v in p)
            self.s.add(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}" '
                       f'stroke-linejoin="round" stroke-linecap="round" clip-path="url(#{self.clip})"{d}/>')

    def spezzata(self, pts, color=BLU, width=2.6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts)
        self.s.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{width}" '
                   f'stroke-linejoin="round" clip-path="url(#{self.clip})"{d}/>')

    def punto(self, x, y, color=BLU, vuoto=False, r=5):
        fill = "white" if vuoto else color
        self.s.add(f'<circle cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="{r}" fill="{fill}" '
                   f'stroke="{color}" stroke-width="2"/>')

    def scritta(self, x, y, s, color=NERO, anchor="start", dx=0, dy=0, size=14, italic=False,
                bold=False):
        self.s.text(self.X(x) + dx, self.Y(y) + dy, s, color, size, anchor, italic, bold)

    def tratteggio(self, x1, y1, x2, y2, color=GRIGIO, width=1.4):
        self.s.line(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), color, width, "5,4")

    def segmento(self, x1, y1, x2, y2, color=NERO, width=1.6, freccia=False, dash=None):
        self.s.line(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), color, width, dash, freccia)

    def banda_x(self, a, b, color, chiusoa=True, chiusob=True, freccia_b=False, freccia_a=False):
        """Intervallo evidenziato sull'asse x."""
        ya = self.Y(0) if self.yr[0] <= 0 <= self.yr[1] else self.y0 + self.h
        xa, xb = self.X(max(a, self.xr[0])), self.X(min(b, self.xr[1]))
        self.s.add(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{ya:.1f}" stroke="{color}" '
                   f'stroke-width="7" stroke-opacity="0.55" stroke-linecap="butt"/>')
        if a >= self.xr[0] and not freccia_a:
            self.s.add(f'<circle cx="{xa:.1f}" cy="{ya:.1f}" r="5" fill="{color if chiusoa else "white"}" stroke="{color}" stroke-width="2"/>')
        if b <= self.xr[1] and not freccia_b:
            self.s.add(f'<circle cx="{xb:.1f}" cy="{ya:.1f}" r="5" fill="{color if chiusob else "white"}" stroke="{color}" stroke-width="2"/>')

    def banda_y(self, a, b, color, chiusoa=True, chiusob=True, freccia_a=False, freccia_b=False):
        xa = self.X(0) if self.xr[0] <= 0 <= self.xr[1] else self.x0
        ya, yb = self.Y(max(a, self.yr[0])), self.Y(min(b, self.yr[1]))
        self.s.add(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xa:.1f}" y2="{yb:.1f}" stroke="{color}" '
                   f'stroke-width="7" stroke-opacity="0.55" stroke-linecap="butt"/>')
        if a >= self.yr[0] and not freccia_a:
            self.s.add(f'<circle cx="{xa:.1f}" cy="{ya:.1f}" r="5" fill="{color if chiusoa else "white"}" stroke="{color}" stroke-width="2"/>')
        if b <= self.yr[1] and not freccia_b:
            self.s.add(f'<circle cx="{xa:.1f}" cy="{yb:.1f}" r="5" fill="{color if chiusob else "white"}" stroke="{color}" stroke-width="2"/>')


def legenda(svg, x, y, voci, size=14):
    for i, (col, testo, dash) in enumerate(voci):
        yy = y + i * 22
        svg.line(x, yy - 5, x + 28, yy - 5, col, 3, dash)
        svg.text(x + 36, yy, testo, NERO, size)


# ---------------------------------------------------------------------------
# 1. Diagrammi a frecce: funzione e controesempi
def diagrammi_frecce():
    s = SVG(1000, 330)

    def insieme(cx, cy, nomi, etich):
        s.add(f'<ellipse cx="{cx}" cy="{cy}" rx="52" ry="105" fill="#f3f6fb" stroke="{GRIGIO}" stroke-width="1.5"/>')
        s.text(cx, cy - 115, etich, NERO, 15, "middle", italic=True)
        pos = []
        n = len(nomi)
        for i, nm in enumerate(nomi):
            y = cy - 60 + i * (120 / (n - 1) if n > 1 else 0)
            s.add(f'<circle cx="{cx}" cy="{y:.1f}" r="4.5" fill="{NERO}"/>')
            s.text(cx + (-14 if etich in ("A",) else 14), y + 5, nm, NERO, 15,
                   "end" if etich == "A" else "start")
            pos.append((cx, y))
        return pos

    def freccia(p, q, col=BLU):
        s.line(p[0] + 7, p[1], q[0] - 9, q[1], col, 2, arrow=True)

    titoli = [("È una funzione", VERDE), ("Non è una funzione", ROSSO), ("Non è una funzione", ROSSO)]
    sotto = ["ogni elemento di A ha una sola freccia",
             "1 ha due frecce",
             "3 non ha nessuna freccia"]
    for k in range(3):
        ox = 40 + k * 330
        s.text(ox + 130, 30, titoli[k][0], titoli[k][1], 17, "middle", bold=True)
        A = insieme(ox + 50, 175, ["1", "2", "3", "4"], "A")
        B = insieme(ox + 210, 175, ["a", "b", "c", "d"], "B")
        if k == 0:
            for i, j in [(0, 0), (1, 0), (2, 2), (3, 1)]:
                freccia(A[i], B[j])
        elif k == 1:
            for i, j in [(0, 0), (1, 1), (2, 2), (3, 3)]:
                freccia(A[i], B[j])
            freccia(A[0], B[2], ROSSO)
        else:
            for i, j in [(0, 0), (1, 1), (3, 3)]:
                freccia(A[i], B[j])
            s.add(f'<circle cx="{A[2][0]}" cy="{A[2][1]:.1f}" r="11" fill="none" stroke="{ROSSO}" stroke-width="2"/>')
        s.text(ox + 130, 315, sotto[k], "#444", 13.5, "middle")
    s.save("04-diagrammi-frecce.svg")


# 2. Area del quadrato in funzione del lato
def area_quadrato():
    s = SVG(620, 440)
    g = Grafico(s, 60, 30, 520, 360, (-0.6, 5.6), (-1.5, 18), passo=1, etich=0,
                xlab="s (m)", ylab="A (m²)")
    for k in range(1, 5):
        g.segmento(k, -0.2, k, 0.2, NERO, 1)
        g.scritta(k, 0, str(k), "#555", "middle", dy=17, size=12)
    for k in (1, 4, 9, 16):
        g.segmento(-0.06, k, 0.06, k, NERO, 1)
        g.scritta(0, k, str(k), "#555", "end", dx=-6, dy=4, size=12)
    g.curva(lambda x: x * x, 0, 4.6, GRIGIO, 1.6, dash="6,5")
    g.curva(lambda x: x * x, 1, 4, BLU, 3)
    g.punto(1, 1, BLU)
    g.punto(4, 16, BLU)
    g.tratteggio(4, 0, 4, 16)
    g.tratteggio(0, 16, 4, 16)
    g.tratteggio(1, 0, 1, 1)
    g.tratteggio(0, 1, 1, 1)
    g.banda_x(1, 4, VERDE)
    g.banda_y(1, 16, ARANCIO)
    g.scritta(2.5, 0, "dominio [1, 4] m", VERDE, "middle", dy=36, size=14, bold=True)
    g.scritta(0, 9, "immagine", ARANCIO, "start", dx=10, dy=-4, size=14, bold=True)
    g.scritta(0, 9, "[1, 16] m²", ARANCIO, "start", dx=10, dy=14, size=14, bold=True)
    g.scritta(3.2, 10.24, "A(s) = s²", BLU, "end", dx=-10, dy=-4, size=16, italic=True)
    s.save("04-area-quadrato.svg")


# 3. Test della retta verticale
def retta_verticale():
    s = SVG(900, 400)
    g1 = Grafico(s, 40, 40, 380, 320, (-3.2, 3.2), (-1.5, 5), "y = x²: è una funzione", colore_titolo=VERDE)
    g1.curva(lambda x: x * x, -3.2, 3.2, BLU)
    g1.segmento(1.5, -1.5, 1.5, 5, VERDE, 2, dash="7,5")
    g1.punto(1.5, 2.25, VERDE)
    g1.scritta(1.5, 0.6, "un solo punto", VERDE, "start", dx=6, size=13)
    g2 = Grafico(s, 480, 40, 380, 320, (-3.2, 3.2), (-2.6, 2.6), "x² + y² = 4: non è una funzione",
                 colore_titolo=ROSSO)
    g2.curva(lambda t: None, 0, 1)
    pts = [(2 * math.cos(t * math.pi / 180), 2 * math.sin(t * math.pi / 180)) for t in range(0, 361, 3)]
    g2.spezzata(pts, BLU)
    g2.segmento(1, -2.6, 1, 2.6, ROSSO, 2, dash="7,5")
    g2.punto(1, math.sqrt(3), ROSSO)
    g2.punto(1, -math.sqrt(3), ROSSO)
    g2.scritta(1, 2.25, "due punti", ROSSO, "start", dx=6, size=13)
    s.save("04-retta-verticale.svg")


# 4. Domini: radice e frazione
def dominio_esempi():
    s = SVG(900, 400)
    g1 = Grafico(s, 40, 40, 380, 320, (-4, 4), (-1, 5), "y = √(5 − 2x)")
    g1.curva(lambda x: math.sqrt(5 - 2 * x) if 5 - 2 * x >= 0 else None, -4, 2.5, BLU, n=2000)
    g1.punto(2.5, 0, BLU)
    g1.banda_x(-4, 2.5, VERDE, freccia_a=True)
    g1.scritta(2.5, 0, "5/2", VERDE, "start", dx=8, dy=-8, size=13, bold=True)
    g1.scritta(-1.5, 0, "dominio: x ≤ 5/2", VERDE, "middle", dy=36, size=14, bold=True)
    g2 = Grafico(s, 480, 40, 380, 320, (-6, 6), (-3, 3), "y = 1 / (x² − 9)")
    f = lambda x: 1 / (x * x - 9)
    g2.curva(f, -6, -3.0001, BLU, n=800)
    g2.curva(f, -2.9999, 2.9999, BLU, n=800)
    g2.curva(f, 3.0001, 6, BLU, n=800)
    for a in (-3, 3):
        g2.segmento(a, -3, a, 3, ROSSO, 1.6, dash="6,5")
        g2.punto(a, 0, ROSSO, vuoto=True)
    g2.scritta(-3, 2.6, "x = −3", ROSSO, "end", dx=-5, size=13)
    g2.scritta(3, 2.6, "x = 3", ROSSO, "start", dx=5, size=13)
    s.text(670, 388, "dominio: x ≠ −3 e x ≠ 3", VERDE, 14, "middle", bold=True)
    s.save("04-dominio-esempi.svg")


# 5. Immagine della parabola (x+1)^2 - 4
def immagine_parabola():
    s = SVG(620, 460)
    g = Grafico(s, 50, 30, 520, 390, (-5.5, 3.5), (-5, 6))
    f = lambda x: (x + 1) ** 2 - 4
    g.banda_y(-4, 6, ARANCIO, freccia_b=True)
    g.curva(f, -5.5, 3.5, BLU)
    g.punto(-1, -4, BLU)
    g.tratteggio(-1, -4, 0, -4, ARANCIO)
    g.punto(-3, 0, VERDE)
    g.punto(1, 0, VERDE)
    g.scritta(-1, -4, "vertice (−1, −4)", BLU, "middle", dy=24, size=14)
    g.scritta(1.4, f(1.4), "f(x) = (x + 1)² − 4", BLU, "start", dx=12, size=15, italic=True)
    g.scritta(0, 3.5, "immagine [−4, +∞)", ARANCIO, "end", dx=-24, dy=5, size=14, bold=True)
    # proiezioni di alcuni punti sull'asse y
    for x in (-4, 2):
        g.tratteggio(x, f(x), 0, f(x), GRIGIO)
        g.punto(x, f(x), BLU, r=3.5)
    s.save("04-immagine-parabola.svg")


# 6. Immagine della radice traslata
def immagine_radice():
    s = SVG(620, 420)
    g = Grafico(s, 50, 30, 520, 350, (-1, 10), (-1, 7))
    f = lambda x: math.sqrt(x - 2) + 3 if x >= 2 else None
    g.curva(lambda x: math.sqrt(x) if x >= 0 else None, 0, 10, GRIGIO, 1.6, n=2000, dash="6,5")
    g.banda_x(2, 10, VERDE, freccia_b=True)
    g.banda_y(3, 7, ARANCIO, freccia_b=True)
    g.curva(f, 2, 10, BLU, n=2000)
    g.punto(2, 3, BLU)
    g.tratteggio(2, 0, 2, 3)
    g.tratteggio(0, 3, 2, 3)
    g.scritta(2, 3, "(2, 3)", BLU, "end", dx=-8, dy=-8, size=14)
    g.scritta(7, f(7), "g(x) = √(x − 2) + 3", BLU, "middle", dy=-14, size=15, italic=True)
    g.scritta(8.3, math.sqrt(8.3), "y = √x", GRIGIO, "start", dx=4, dy=18, size=13, italic=True)
    g.scritta(6, 0, "dominio [2, +∞)", VERDE, "middle", dy=34, size=14, bold=True)
    g.scritta(0, 5.2, "immagine [3, +∞)", ARANCIO, "start", dx=10, size=14, bold=True)
    s.save("04-immagine-radice.svg")


# 7. h(x) = (x^2-4)/(x-2): retta con un buco
def retta_bucata():
    s = SVG(560, 420)
    g = Grafico(s, 50, 30, 460, 350, (-4, 5), (-2, 7))
    g.curva(lambda x: x + 2, -4, 5, BLU)
    g.punto(2, 4, BLU, vuoto=True, r=6)
    g.tratteggio(2, 0, 2, 3.8)
    g.tratteggio(0, 4, 1.8, 4)
    g.punto(0, 4, ARANCIO, vuoto=True, r=5)
    g.punto(2, 0, VERDE, vuoto=True, r=5)
    g.scritta(2, 4, "buco in (2, 4)", BLU, "start", dx=12, dy=12, size=14)
    g.scritta(2.6, 5.6, "y = x + 2", BLU, "end", dx=-10, size=15, italic=True)
    s.save("04-retta-bucata.svg")


# 8. Test della retta orizzontale
def retta_orizzontale():
    s = SVG(900, 400)
    g1 = Grafico(s, 40, 40, 380, 320, (-2.6, 2.6), (-4, 4), "y = x³: iniettiva", colore_titolo=VERDE)
    g1.curva(lambda x: x ** 3, -2.6, 2.6, BLU)
    for k in (2, -1):
        g1.segmento(-2.6, k, 2.6, k, VERDE, 1.8, dash="7,5")
        g1.punto(math.copysign(abs(k) ** (1 / 3), k), k, VERDE)
    s.text(230, 390, "ogni retta orizzontale incontra il grafico una volta sola", VERDE, 13, "middle")
    g2 = Grafico(s, 480, 40, 380, 320, (-2.6, 2.6), (-1, 5), "y = x²: non iniettiva",
                 colore_titolo=ROSSO)
    g2.curva(lambda x: x * x, -2.6, 2.6, BLU)
    g2.segmento(-2.6, 2, 2.6, 2, ROSSO, 1.8, dash="7,5")
    g2.punto(-math.sqrt(2), 2, ROSSO)
    g2.punto(math.sqrt(2), 2, ROSSO)
    g2.scritta(-math.sqrt(2), 2, "−√2", ROSSO, "end", dx=-8, dy=20, size=13)
    g2.scritta(math.sqrt(2), 2, "√2", ROSSO, "start", dx=8, dy=20, size=13)
    s.text(670, 390, "la retta y = 2 incontra il grafico in due punti", ROSSO, 13, "middle")
    s.save("04-retta-orizzontale.svg")


# 9. x^2 su R e su [0,+inf)
def restrizione_x2():
    s = SVG(900, 400)
    g1 = Grafico(s, 40, 40, 380, 320, (-2.6, 2.6), (-1, 5), "x²: ℝ → ℝ")
    g1.curva(lambda x: x * x, -2.6, 2.6, BLU)
    g1.banda_y(-1, 0, ROSSO, freccia_a=True, chiusob=False)
    g1.scritta(0, -0.6, "valori negativi mai raggiunti", ROSSO, "start", dx=10, size=13)
    s.text(230, 390, "non iniettiva e non suriettiva", NERO, 14, "middle")
    g2 = Grafico(s, 480, 40, 380, 320, (-2.6, 2.6), (-1, 5), "x²: [0, +∞) → [0, +∞)")
    g2.curva(lambda x: x * x, -2.6, 0, GRIGIO, 1.5, dash="6,5")
    g2.curva(lambda x: x * x, 0, 2.6, BLU)
    g2.punto(0, 0, BLU)
    g2.banda_x(0, 2.6, VERDE, freccia_b=True)
    g2.banda_y(0, 5, ARANCIO, freccia_b=True)
    g2.scritta(0.25, 4.4, "biettiva", VERDE, "start", size=14, bold=True)
    s.text(670, 390, "iniettiva e suriettiva: biettiva", NERO, 14, "middle")
    s.save("04-restrizione-x2.svg")


# 10. Inversa: simmetria rispetto a y = x
def inversa_bisettrice():
    s = SVG(900, 420)
    g1 = Grafico(s, 40, 40, 380, 340, (-2, 6), (-2, 6), "f(x) = 5 − 2x e la sua inversa")
    g1.curva(lambda x: x, -2, 6, GRIGIO, 1.4, dash="6,5")
    g1.curva(lambda x: 5 - 2 * x, -2, 6, BLU)
    g1.curva(lambda x: (5 - x) / 2, -2, 6, ROSSO)
    g1.punto(1, 3, BLU)
    g1.punto(3, 1, ROSSO)
    g1.tratteggio(1, 3, 3, 1, VIOLA)
    g1.scritta(1, 3, "(1, 3)", BLU, "start", dx=8, dy=-4, size=13)
    g1.scritta(3, 1, "(3, 1)", ROSSO, "start", dx=4, dy=20, size=13)
    g1.scritta(5.3, 5.3, "y = x", GRIGIO, "end", dx=-4, dy=-8, size=13, italic=True)
    legenda(s, 60, 400, [(BLU, "f(x) = 5 − 2x", None)])
    legenda(s, 250, 400, [(ROSSO, "f⁻¹(x) = (5 − x)/2", None)])
    g2 = Grafico(s, 480, 40, 380, 340, (-1, 5), (-1, 5), "x² su [0, +∞) e √x")
    g2.curva(lambda x: x, -1, 5, GRIGIO, 1.4, dash="6,5")
    g2.curva(lambda x: x * x, 0, 3, BLU)
    g2.curva(lambda x: math.sqrt(x) if x >= 0 else None, 0, 5, ROSSO, n=2000)
    g2.punto(2, 4, BLU)
    g2.punto(4, 2, ROSSO)
    g2.tratteggio(2, 4, 4, 2, VIOLA)
    g2.scritta(2, 4, "(2, 4)", BLU, "end", dx=-8, dy=4, size=13)
    g2.scritta(4, 2, "(4, 2)", ROSSO, "start", dx=4, dy=20, size=13)
    g2.scritta(4.5, 4.5, "y = x", GRIGIO, "end", dx=-4, dy=-8, size=13, italic=True)
    legenda(s, 520, 400, [(BLU, "y = x²", None)])
    legenda(s, 680, 400, [(ROSSO, "y = √x", None)])
    s.save("04-inversa-bisettrice.svg")


# 11. Restrizioni di (x-1)^2
def restrizione_x_meno_1():
    s = SVG(900, 400)
    for k, (a, b, tit, inv) in enumerate([(1, 3.6, "su [1, +∞): inversa 1 + √x", lambda x: 1 + math.sqrt(x)),
                                          (-1.6, 1, "su (−∞, 1]: inversa 1 − √x", lambda x: 1 - math.sqrt(x))]):
        g = Grafico(s, 40 + k * 440, 40, 380, 320, (-2, 5), (-2, 5), tit)
        g.curva(lambda x: x, -2, 5, GRIGIO, 1.4, dash="6,5")
        g.curva(lambda x: (x - 1) ** 2, -2, 5, GRIGIO, 1.4, dash="2,4")
        g.curva(lambda x: (x - 1) ** 2, a, b, BLU)
        g.curva(lambda x: inv(x) if x >= 0 else None, 0, 5, ROSSO, n=2000)
        g.punto(1, 0, BLU)
        g.punto(0, 1, ROSSO)
    legenda(s, 120, 390, [(BLU, "y = (x − 1)² sul pezzo scelto", None)])
    legenda(s, 520, 390, [(ROSSO, "la sua inversa", None)])
    s.save("04-restrizione-x-meno-1.svg")


# 12. Composizione: due macchine in fila
def composizione():
    s = SVG(860, 200)

    def scatola(x, nome, col):
        s.add(f'<rect x="{x}" y="60" width="130" height="70" rx="10" fill="{col}" fill-opacity="0.12" '
              f'stroke="{col}" stroke-width="2"/>')
        s.text(x + 65, 103, nome, col, 22, "middle", italic=True, bold=True)

    s.text(40, 101, "x", NERO, 22, "middle", italic=True)
    s.line(60, 95, 165, 95, NERO, 2, arrow=True)
    scatola(170, "g", VERDE)
    s.line(300, 95, 420, 95, NERO, 2, arrow=True)
    s.text(360, 82, "g(x)", VERDE, 18, "middle", italic=True)
    scatola(425, "f", BLU)
    s.line(555, 95, 660, 95, NERO, 2, arrow=True)
    s.text(740, 101, "f(g(x))", BLU, 22, "middle", italic=True)
    s.text(235, 160, "prima g", VERDE, 14, "middle")
    s.text(490, 160, "poi f", BLU, 14, "middle")
    s.add(f'<rect x="150" y="30" width="430" height="150" rx="14" fill="none" stroke="{VIOLA}" '
          f'stroke-width="1.6" stroke-dasharray="7,5"/>')
    s.text(365, 22, "la macchina composta f ∘ g", VIOLA, 15, "middle", bold=True)
    s.save("04-composizione.svg")


# 13. Pari e dispari
def pari_dispari():
    s = SVG(900, 410)
    g1 = Grafico(s, 40, 40, 380, 330, (-2.4, 2.4), (-2, 4), "pari: x⁴ − 2x²", colore_titolo=BLU)
    g1.curva(lambda x: x ** 4 - 2 * x * x, -2.4, 2.4, BLU)
    g1.punto(-1.7, 1.7 ** 4 - 2 * 1.7 ** 2, VIOLA)
    g1.punto(1.7, 1.7 ** 4 - 2 * 1.7 ** 2, VIOLA)
    yv = 1.7 ** 4 - 2 * 1.7 ** 2
    g1.tratteggio(-1.7, yv, 1.7, yv, VIOLA)
    g1.scritta(-1.7, yv, "(−a, f(a))", VIOLA, "end", dx=-6, dy=-6, size=13)
    g1.scritta(1.7, yv, "(a, f(a))", VIOLA, "start", dx=6, dy=-6, size=13)
    s.text(230, 400, "simmetria rispetto all'asse y", NERO, 14, "middle")
    g2 = Grafico(s, 480, 40, 380, 330, (-2.2, 2.2), (-4, 4), "dispari: x³ + x", colore_titolo=ROSSO)
    g2.curva(lambda x: x ** 3 + x, -2.2, 2.2, ROSSO)
    a = 1.1
    fa = a ** 3 + a
    g2.punto(a, fa, VIOLA)
    g2.punto(-a, -fa, VIOLA)
    g2.tratteggio(-a, -fa, a, fa, VIOLA)
    g2.punto(0, 0, NERO, r=3.5)
    g2.scritta(a, fa, "(a, f(a))", VIOLA, "start", dx=8, dy=4, size=13)
    g2.scritta(-a, -fa, "(−a, −f(a))", VIOLA, "end", dx=-8, dy=4, size=13)
    s.text(670, 400, "simmetria rispetto all'origine", NERO, 14, "middle")
    s.save("04-pari-dispari.svg")


# 14. Monotonia
def monotonia():
    s = SVG(900, 400)
    g1 = Grafico(s, 40, 40, 380, 320, (-5.5, 2.5), (-1, 6), "(x + 2)²")
    g1.curva(lambda x: (x + 2) ** 2, -5.5, -2, ROSSO)
    g1.curva(lambda x: (x + 2) ** 2, -2, 2.5, VERDE)
    g1.punto(-2, 0, NERO)
    g1.banda_x(-5.5, -2, ROSSO, freccia_a=True)
    g1.banda_x(-2, 2.5, VERDE, freccia_b=True)
    g1.scritta(-4.1, 5.0, "decrescente", ROSSO, "start", dx=10, size=14, bold=True)
    g1.scritta(0.3, 1.5, "crescente", VERDE, "start", size=14, bold=True)
    g2 = Grafico(s, 480, 40, 380, 320, (-1, 7), (-1, 5), "|x − 3|")
    g2.curva(lambda x: abs(x - 3), -1, 3, ROSSO)
    g2.curva(lambda x: abs(x - 3), 3, 7, VERDE)
    g2.punto(3, 0, NERO)
    g2.banda_x(-1, 3, ROSSO, freccia_a=True)
    g2.banda_x(3, 7, VERDE, freccia_b=True)
    g2.scritta(0.6, 2.4, "decrescente", ROSSO, "start", dx=10, size=14, bold=True)
    g2.scritta(5.4, 2.4, "crescente", VERDE, "end", dx=-10, size=14, bold=True)
    s.save("04-monotonia.svg")


# 15. Traslazioni
def traslazioni():
    s = SVG(900, 420)
    q = lambda x: x * x
    g1 = Grafico(s, 40, 40, 380, 320, (-3, 5), (-1, 6), "orizzontale: f(x − 2)")
    g1.curva(q, -3, 5, GRIGIO, 2, dash="6,5")
    g1.curva(lambda x: (x - 2) ** 2, -3, 5, BLU)
    g1.segmento(2.12, 4, 3.88, 4, VIOLA, 2, freccia=True)
    g1.scritta(3, 4, "+2", VIOLA, "middle", dy=-8, size=14, bold=True)
    legenda(s, 60, 395, [(GRIGIO, "y = x²", "6,5")])
    legenda(s, 220, 395, [(BLU, "y = (x − 2)²", None)])
    g2 = Grafico(s, 480, 40, 380, 320, (-3, 3), (-3, 4), "verticale: f(x) − 2")
    g2.curva(q, -3, 3, GRIGIO, 2, dash="6,5")
    g2.curva(lambda x: x * x - 2, -3, 3, ROSSO)
    g2.segmento(1.5, 2.25, 1.5, 0.35, VIOLA, 2, freccia=True)
    g2.scritta(1.5, 1.2, "−2", VIOLA, "end", dx=-5, size=13, bold=True)
    legenda(s, 500, 395, [(GRIGIO, "y = x²", "6,5")])
    legenda(s, 660, 395, [(ROSSO, "y = x² − 2", None)])
    s.save("04-traslazioni.svg")


# 16. Riflessioni
def riflessioni():
    s = SVG(900, 420)
    r = lambda x: math.sqrt(x) if x >= 0 else None
    g1 = Grafico(s, 40, 40, 380, 320, (-5, 5), (-3, 3), "−f(x): ribalta sull'asse x")
    g1.curva(r, 0, 5, GRIGIO, 2, n=2000, dash="6,5")
    g1.curva(lambda x: -math.sqrt(x) if x >= 0 else None, 0, 5, BLU, n=2000)
    legenda(s, 60, 395, [(GRIGIO, "y = √x", "6,5")])
    legenda(s, 220, 395, [(BLU, "y = −√x", None)])
    g2 = Grafico(s, 480, 40, 380, 320, (-5, 5), (-3, 3), "f(−x): ribalta sull'asse y")
    g2.curva(r, 0, 5, GRIGIO, 2, n=2000, dash="6,5")
    g2.curva(lambda x: math.sqrt(-x) if x <= 0 else None, -5, 0, ROSSO, n=2000)
    legenda(s, 500, 395, [(GRIGIO, "y = √x", "6,5")])
    legenda(s, 660, 395, [(ROSSO, "y = √(−x)", None)])
    s.save("04-riflessioni.svg")


# 17. Valore assoluto e dilatazioni
def valore_assoluto():
    s = SVG(900, 420)
    p = lambda x: x * x - 4
    g1 = Grafico(s, 40, 40, 380, 320, (-3.5, 3.5), (-5, 6), "|f(x)|: la parte sotto sale")
    g1.curva(p, -3.5, 3.5, GRIGIO, 2, dash="6,5")
    g1.curva(lambda x: abs(p(x)), -3.5, 3.5, BLU)
    g1.punto(-2, 0, BLU)
    g1.punto(2, 0, BLU)
    legenda(s, 60, 395, [(GRIGIO, "y = x² − 4", "6,5")])
    legenda(s, 220, 395, [(BLU, "y = |x² − 4|", None)])
    g2 = Grafico(s, 480, 40, 380, 320, (-3, 3), (-1, 6), "dilatazioni: k·f(x)")
    g2.curva(lambda x: x * x, -3, 3, GRIGIO, 2, dash="6,5")
    g2.curva(lambda x: 3 * x * x, -3, 3, ROSSO)
    g2.curva(lambda x: 0.5 * x * x, -3, 3, VERDE)
    legenda(s, 495, 395, [(GRIGIO, "x²", "6,5")])
    legenda(s, 600, 395, [(ROSSO, "3x² (più stretta)", None)])
    legenda(s, 760, 395, [(VERDE, "x²/2", None)])
    s.save("04-valore-assoluto-dilatazioni.svg")


# 18. Esercizio 11: |x+1| - 2 costruito a passi
def esercizio_11():
    s = SVG(960, 360)
    passi = [("1. y = |x|", lambda x: abs(x), None),
             ("2. y = |x + 1|", lambda x: abs(x + 1), lambda x: abs(x)),
             ("3. y = |x + 1| − 2", lambda x: abs(x + 1) - 2, lambda x: abs(x + 1))]
    for k, (tit, f, prima) in enumerate(passi):
        g = Grafico(s, 30 + k * 315, 40, 280, 280, (-4.5, 3), (-3, 4.5), tit)
        if prima:
            g.curva(prima, -4.5, 3, GRIGIO, 1.8, dash="6,5")
        g.curva(f, -4.5, 3, BLU)
        if k == 1:
            g.segmento(-0.05, -1.5, -0.95, -1.5, VIOLA, 2, freccia=True)
            g.scritta(-0.95, -1.5, "−1", VIOLA, "end", dx=-6, dy=5, size=13, bold=True)
        if k == 2:
            g.segmento(1.8, 2.8, 1.8, 0.9, VIOLA, 2, freccia=True)
            g.scritta(1.8, 1.9, "−2", VIOLA, "start", dx=6, size=13, bold=True)
            g.punto(-1, -2, ROSSO)
            g.punto(-3, 0, VERDE)
            g.punto(1, 0, VERDE)
            g.scritta(-1, -2, "V(−1, −2)", ROSSO, "middle", dy=22, size=13)
    s.save("04-esercizio-11.svg")


# 19. Esercizio 12: -(x-1)^2 + 4
def esercizio_12():
    s = SVG(560, 420)
    g = Grafico(s, 50, 30, 460, 350, (-3, 5), (-4, 5.5))
    f = lambda x: -(x - 1) ** 2 + 4
    g.banda_y(-4, 4, ARANCIO, freccia_a=True)
    g.curva(f, -3, 5, BLU)
    g.punto(1, 4, ROSSO)
    g.punto(-1, 0, VERDE)
    g.punto(3, 0, VERDE)
    g.tratteggio(0, 4, 1, 4, ARANCIO)
    g.scritta(1, 4, "V(1, 4)", ROSSO, "start", dx=10, dy=-6, size=14)
    g.scritta(-1, 0, "−1", VERDE, "end", dx=-6, dy=-8, size=13, bold=True)
    g.scritta(3, 0, "3", VERDE, "start", dx=6, dy=-8, size=13, bold=True)
    g.scritta(0, -2.2, "immagine (−∞, 4]", ARANCIO, "start", dx=10, size=14, bold=True)
    g.scritta(3.4, f(3.4), "y = −(x − 1)² + 4", BLU, "start", dx=10, dy=6, size=14, italic=True)
    s.save("04-esercizio-12.svg")


# 20. Tariffa T(t) = 4 + 2t
def tariffa():
    s = SVG(620, 440)
    g = Grafico(s, 60, 30, 500, 360, (-1, 7), (-1, 17), passo=1, etich=2,
                xlab="t (ore)", ylab="T (euro)")
    T = lambda t: 4 + 2 * t if t >= 0 else None
    g.banda_y(4, 17, ARANCIO, freccia_b=True)
    g.curva(T, 0, 7, BLU)
    g.punto(0, 4, BLU)
    g.punto(3, 10, ROSSO)
    g.tratteggio(0, 10, 3, 10, ROSSO)
    g.tratteggio(3, 0, 3, 10, ROSSO)
    g.segmento(0.2, 10, 2.8, 10, ROSSO, 1.6, freccia=True)
    g.segmento(3, 9.6, 3, 0.5, ROSSO, 1.6, freccia=True)
    g.scritta(3, 0, "3", ROSSO, "middle", dy=17, size=13, bold=True)
    g.scritta(3, 10, "T⁻¹(10) = 3", ROSSO, "start", dx=10, dy=14, size=14, bold=True)
    g.scritta(0, 4, "4 € fissi", BLU, "start", dx=10, dy=18, size=13)
    g.scritta(5.4, T(5.4), "T(t) = 4 + 2t", BLU, "end", dx=-12, dy=-6, size=15, italic=True)
    g.scritta(0, 14.5, "immagine [4, +∞)", ARANCIO, "start", dx=10, size=14, bold=True)
    s.save("04-tariffa.svg")


if __name__ == "__main__":
    diagrammi_frecce()
    area_quadrato()
    retta_verticale()
    dominio_esempi()
    immagine_parabola()
    immagine_radice()
    retta_bucata()
    retta_orizzontale()
    restrizione_x2()
    inversa_bisettrice()
    restrizione_x_meno_1()
    composizione()
    pari_dispari()
    monotonia()
    traslazioni()
    riflessioni()
    valore_assoluto()
    esercizio_11()
    esercizio_12()
    tariffa()
