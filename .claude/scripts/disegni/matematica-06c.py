"""Grafici per la bozza di matematica 05 (Le funzioni elementari).

Senza dipendenze: python3 -I .claude/scripts/disegni/matematica-06c.py
Le immagini vanno in anno-1/semestre-1/matematica/bozze/img/ con prefisso 06-.
"""
import math
import os

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/matematica/bozze/img/"

COL = {
    "blu": "#1f5fa8",
    "rosso": "#c0392b",
    "verde": "#1e8449",
    "arancio": "#d4790f",
    "viola": "#7d3c98",
    "grigio": "#7f8c8d",
    "nero": "#222222",
    "griglia": "#e6e6e6",
}
FONT = "font-family=\"Helvetica, Arial, sans-serif\""
PI = math.pi


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Grafico:
    """Piano cartesiano con unita' uguali (o diverse) sui due assi."""

    def __init__(self, x0, x1, y0, y1, ux=50, uy=None, margine=30, xlab="x", ylab="y"):
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        self.ux = ux
        self.uy = uy if uy is not None else ux
        self.m = margine
        self.W = (x1 - x0) * self.ux + 2 * margine
        self.H = (y1 - y0) * self.uy + 2 * margine
        self.parti = []
        self.sopra = []
        self.xlab, self.ylab = xlab, ylab

    def X(self, x):
        return self.m + (x - self.x0) * self.ux

    def Y(self, y):
        return self.m + (self.y1 - y) * self.uy

    def P(self, x, y):
        return self.X(x), self.Y(y)

    # ---------- sfondo ----------
    def griglia(self, passo_x=1, passo_y=1):
        k = math.ceil(self.x0 / passo_x)
        while k * passo_x <= self.x1 + 1e-9:
            x = self.X(k * passo_x)
            self.parti.append(f'<line x1="{x:.1f}" y1="{self.m}" x2="{x:.1f}" y2="{self.H - self.m}" stroke="{COL["griglia"]}" stroke-width="1"/>')
            k += 1
        k = math.ceil(self.y0 / passo_y)
        while k * passo_y <= self.y1 + 1e-9:
            y = self.Y(k * passo_y)
            self.parti.append(f'<line x1="{self.m}" y1="{y:.1f}" x2="{self.W - self.m}" y2="{y:.1f}" stroke="{COL["griglia"]}" stroke-width="1"/>')
            k += 1

    def assi(self, tacche_x=None, tacche_y=None, origine=True):
        """tacche_x / tacche_y: liste di (valore, etichetta)."""
        n = COL["nero"]
        if self.y0 <= 0 <= self.y1:
            y = self.Y(0)
            self.parti.append(f'<line x1="{self.m - 12}" y1="{y:.1f}" x2="{self.W - self.m + 14}" y2="{y:.1f}" stroke="{n}" stroke-width="1.4"/>')
            xe = self.W - self.m + 14
            self.parti.append(f'<path d="M {xe:.1f} {y:.1f} l -9 -4.5 l 0 9 z" fill="{n}"/>')
            self.testo(self.xlab, xe - 2, y - 10, size=16, anchor="end", stile="italic")
        if self.x0 <= 0 <= self.x1:
            x = self.X(0)
            self.parti.append(f'<line x1="{x:.1f}" y1="{self.H - self.m + 12}" x2="{x:.1f}" y2="{self.m - 14}" stroke="{n}" stroke-width="1.4"/>')
            ye = self.m - 14
            self.parti.append(f'<path d="M {x:.1f} {ye:.1f} l -4.5 9 l 9 0 z" fill="{n}"/>')
            self.testo(self.ylab, x - 9, ye + 12, size=16, anchor="end", stile="italic")
        y = self.Y(0) if self.y0 <= 0 <= self.y1 else self.H - self.m
        x = self.X(0) if self.x0 <= 0 <= self.x1 else self.m
        for v, lab in (tacche_x or []):
            px = self.X(v)
            self.parti.append(f'<line x1="{px:.1f}" y1="{y - 4:.1f}" x2="{px:.1f}" y2="{y + 4:.1f}" stroke="{n}" stroke-width="1.2"/>')
            self.testo(lab, px, y + 19, size=13, sopra=True)
        for v, lab in (tacche_y or []):
            py = self.Y(v)
            self.parti.append(f'<line x1="{x - 4:.1f}" y1="{py:.1f}" x2="{x + 4:.1f}" y2="{py:.1f}" stroke="{n}" stroke-width="1.2"/>')
            self.testo(lab, x - 8, py + 4.5, size=13, anchor="end", sopra=True)
        if origine and self.x0 <= 0 <= self.x1 and self.y0 <= 0 <= self.y1:
            self.testo("O", self.X(0) - 7, self.Y(0) + 17, size=13, anchor="end")

    # ---------- oggetti ----------
    def curva(self, f, a=None, b=None, colore="blu", spessore=2.4, tratteggio=None, n=800, salto=None):
        a = self.x0 if a is None else a
        b = self.x1 if b is None else b
        lim = (self.y1 - self.y0) * 3
        segmenti, corr = [], []
        prec = None
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError, OverflowError):
                y = None
            if y is None or isinstance(y, complex) or abs(y) > 1e6 or y < self.y0 - lim or y > self.y1 + lim:
                if corr:
                    segmenti.append(corr)
                corr, prec = [], None
                continue
            if prec is not None and salto is not None and abs(y - prec) > salto:
                segmenti.append(corr)
                corr = []
            corr.append(self.P(x, y))
            prec = y
        if corr:
            segmenti.append(corr)
        self._linee(segmenti, colore, spessore, tratteggio)

    def parametrica(self, fx, fy, t0, t1, colore="blu", spessore=2.4, tratteggio=None, n=400):
        pts = [self.P(fx(t0 + (t1 - t0) * i / n), fy(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
        self._linee([pts], colore, spessore, tratteggio)

    def _linee(self, segmenti, colore, spessore, tratteggio):
        dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
        for s in segmenti:
            if len(s) < 2:
                continue
            d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in s)
            self.parti.append(f'<path d="{d}" fill="none" stroke="{COL.get(colore, colore)}" stroke-width="{spessore}" '
                              f'stroke-linejoin="round" stroke-linecap="round"{dash} clip-path="url(#area)"/>')

    def segmento(self, p, q, colore="grigio", spessore=1.4, tratteggio="5,4", clip=True):
        dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
        (x1, y1), (x2, y2) = self.P(*p), self.P(*q)
        cp = ' clip-path="url(#area)"' if clip else ""
        self.parti.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COL.get(colore, colore)}" '
                          f'stroke-width="{spessore}"{dash}{cp}/>')

    def asintoto_v(self, x, colore="grigio"):
        self.segmento((x, self.y0), (x, self.y1), colore, 1.4, "6,5")

    def asintoto_o(self, y, colore="grigio"):
        self.segmento((self.x0, y), (self.x1, y), colore, 1.4, "6,5")

    def punto(self, x, y, colore="nero", vuoto=False, r=4.2):
        px, py = self.P(x, y)
        fill = "white" if vuoto else COL.get(colore, colore)
        self.sopra.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{fill}" stroke="{COL.get(colore, colore)}" stroke-width="1.8"/>')

    def etichetta(self, t, x, y, colore="nero", size=15, anchor="start", dx=0, dy=0, stile=None):
        px, py = self.P(x, y)
        self.testo(t, px + dx, py + dy, colore, size, anchor, stile, sopra=True)

    def testo(self, t, px, py, colore="nero", size=15, anchor="middle", stile=None, sopra=False):
        st = f' font-style="{stile}"' if stile else ""
        el = (f'<text x="{px:.1f}" y="{py:.1f}" {FONT} font-size="{size}" fill="{COL.get(colore, colore)}" '
              f'text-anchor="{anchor}"{st} stroke="white" stroke-width="4" stroke-linejoin="round" '
              f'paint-order="stroke">{esc(t)}</text>')
        (self.sopra if sopra else self.parti).append(el)

    def area(self, pts, colore="blu", opacita=0.12):
        d = "M " + " L ".join(f"{self.X(x):.1f} {self.Y(y):.1f}" for x, y in pts) + " Z"
        self.parti.append(f'<path d="{d}" fill="{COL.get(colore, colore)}" fill-opacity="{opacita}" stroke="none" clip-path="url(#area)"/>')

    def salva(self, nome):
        W, H = self.W, self.H
        clip = (f'<clipPath id="area"><rect x="{self.m - 2}" y="{self.m - 2}" '
                f'width="{W - 2 * self.m + 4}" height="{H - 2 * self.m + 4}"/></clipPath>')
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}">'
               f'<defs>{clip}</defs><rect width="100%" height="100%" fill="white"/>'
               + "".join(self.parti) + "".join(self.sopra) + "</svg>")
        with open(os.path.join(OUT, nome), "w", encoding="utf-8") as fh:
            fh.write(svg)
        print("scritto", nome, f"{W:.0f}x{H:.0f}")


def interi(a, b, salta0=True):
    return [(k, str(k).replace("-", "−")) for k in range(a, b + 1) if not (salta0 and k == 0)]


def tacche_pi(a, b, den=2):
    """Tacche multiple di pi/den tra a*pi/den e b*pi/den."""
    out = []
    for k in range(a, b + 1):
        if k == 0:
            continue
        num, d = k, den
        g = math.gcd(abs(num), d)
        num, d = num // g, d // g
        s = "−" if num < 0 else ""
        n = abs(num)
        if d == 1:
            lab = f"{s}π" if n == 1 else f"{s}{n}π"
        else:
            lab = f"{s}π/{d}" if n == 1 else f"{s}{n}π/{d}"
        out.append((k * PI / den, lab))
    return out


os.makedirs(OUT, exist_ok=True)

# ===================== 1. RETTE =====================
g = Grafico(-4, 4, -3.5, 4.5, ux=50)
g.griglia()
g.assi(interi(-4, 4), interi(-3, 4))
g.curva(lambda x: 2 * x - 1, colore="blu")
g.curva(lambda x: -0.5 * x + 2, colore="rosso")
g.curva(lambda x: 3, colore="verde", spessore=2)
g.etichetta("y = 2x − 1", 2.75, 4.2, "blu", dx=8)
g.etichetta("y = −½x + 2", -3.9, 4.1, "rosso", dy=0)
g.etichetta("y = 3", 3.9, 3, "verde", anchor="end", dy=20)
g.punto(0, -1, "blu"); g.etichetta("q = −1", 0, -1, "blu", dx=10, dy=16)
g.punto(0, 2, "rosso"); g.etichetta("q = 2", 0, 2, "rosso", dx=-10, dy=20, anchor="end")
# triangolo della pendenza per y=2x-1: da (1,1) a (2,1) a (2,3)
g.segmento((1, 1), (2, 1), "blu", 1.4, "4,3"); g.segmento((2, 1), (2, 3), "blu", 1.4, "4,3")
g.etichetta("+1", 1.5, 1, "blu", size=13, anchor="middle", dy=16)
g.etichetta("+2", 2, 2, "blu", size=13, dx=6, dy=4)
g.salva("06-rette.svg")

# ===================== 2. POTENZE PARI =====================
g = Grafico(-2.2, 2.2, -0.8, 4.6, ux=70)
g.griglia(0.5, 0.5)
g.assi(interi(-2, 2), interi(1, 4))
g.curva(lambda x: x ** 2, colore="blu")
g.curva(lambda x: x ** 4, colore="rosso")
g.curva(lambda x: x ** 6, colore="verde", spessore=2)
for x in (-1, 1):
    g.punto(x, 1)
g.punto(0, 0)
g.etichetta("y = x²", 1.42, 1.25, "blu", dy=5)
g.etichetta("y = x⁴", 1.42, 0.92, "rosso", dy=5)
g.etichetta("y = x⁶", 1.42, 0.59, "verde", dy=5)
g.etichetta("(1, 1)", 1, 1, dx=-12, dy=-8, anchor="end")
g.etichetta("(−1, 1)", -1, 1, dx=12, dy=-8)
g.salva("06-potenze-pari.svg")

# ===================== 3. POTENZE DISPARI =====================
g = Grafico(-2.2, 2.2, -3.4, 3.4, ux=60)
g.griglia(0.5, 0.5)
g.assi(interi(-2, 2), interi(-3, 3))
g.curva(lambda x: x, colore="grigio", spessore=1.8)
g.curva(lambda x: x ** 3, colore="blu")
g.curva(lambda x: x ** 5, colore="rosso")
for p in ((1, 1), (-1, -1), (0, 0)):
    g.punto(*p)
g.etichetta("y = x", 2.15, 1.3, "grigio", anchor="end")
g.etichetta("y = x³", 1.45, 3.1, "blu", anchor="start", dx=8)
g.etichetta("y = x⁵", 1.25, 3.1, "rosso", anchor="end", dx=-6)
g.etichetta("(1, 1)", 1, 1, dx=10, dy=18)
g.etichetta("(−1, −1)", -1, -1, dx=-10, dy=-8, anchor="end")
g.salva("06-potenze-dispari.svg")

# ===================== 4. RADICE QUADRATA =====================
g = Grafico(-0.8, 4.6, -0.8, 4.6, ux=70)
g.griglia(0.5, 0.5)
g.assi(interi(1, 4), interi(1, 4))
g.curva(lambda x: x, colore="grigio", spessore=1.5, tratteggio="6,5")
g.curva(lambda x: x ** 2, a=0, colore="rosso", spessore=2)
g.curva(lambda x: math.sqrt(x), a=0, colore="blu", n=2000)
g.punto(0, 0); g.punto(1, 1); g.punto(4, 2, "blu"); g.punto(2, 4, "rosso")
g.etichetta("y = √x", 4.5, 2.12, "blu", anchor="end", dy=-10)
g.etichetta("y = x²  (x ≥ 0)", 2.12, 4.3, "rosso", anchor="start", dx=6)
g.etichetta("y = x", 3.6, 3.3, "grigio", anchor="start")
g.etichetta("(4, 2)", 4, 2, "blu", dy=22, anchor="middle")
g.etichetta("(2, 4)", 2, 4, "rosso", dx=-10, anchor="end")
g.salva("06-radice-quadrata.svg")

# ===================== 5. RADICE CUBICA =====================
cbrt = lambda x: math.copysign(abs(x) ** (1 / 3), x)
g = Grafico(-4.5, 4.5, -2.3, 2.3, ux=55)
g.griglia(1, 0.5)
g.assi(interi(-4, 4), interi(-2, 2))
g.curva(cbrt, colore="blu", n=3000)
for p in ((1, 1), (-1, -1), (0, 0)):
    g.punto(*p)
g.etichetta("y = ∛x", 3.0, 1.44, "blu", dy=-14, anchor="middle")
g.etichetta("(1, 1)", 1, 1, dx=-4, dy=-12, anchor="end")
g.etichetta("(−1, −1)", -1, -1, dx=6, dy=20)
g.salva("06-radice-cubica.svg")

# ===================== 6. IPERBOLE 1/x =====================
g = Grafico(-4.5, 4.5, -4.5, 4.5, ux=50)
g.griglia()
g.assi(interi(-4, 4), interi(-4, 4))
g.curva(lambda x: 1 / x, a=0.01, b=4.5, colore="blu", n=2000)
g.curva(lambda x: 1 / x, a=-4.5, b=-0.01, colore="blu", n=2000)
g.punto(1, 1); g.punto(-1, -1)
g.etichetta("y = 1/x", 2.2, 0.45, "blu", dy=-14)
g.etichetta("(1, 1)", 1, 1, dx=8, dy=-6)
g.etichetta("(−1, −1)", -1, -1, dx=-8, dy=18, anchor="end")
g.etichetta("non tocca mai gli assi", 0.35, 3.6, "grigio", size=13)
g.salva("06-iperbole.svg")

# ===================== 7. VALORE ASSOLUTO =====================
g = Grafico(-4.5, 3.5, -2.8, 4.3, ux=50)
g.griglia()
g.assi(interi(-4, 3), interi(-2, 4))
g.curva(lambda x: abs(x), colore="grigio", spessore=2, tratteggio="7,5")
g.curva(lambda x: abs(x + 1) - 2, colore="blu")
g.punto(-1, -2, "blu"); g.punto(-3, 0, "rosso"); g.punto(1, 0, "rosso")
g.etichetta("y = |x|", 2.6, 3.4, "grigio", anchor="start", dx=-4, dy=-14)
g.etichetta("y = |x + 1| − 2", -4.4, -1.6, "blu")
g.etichetta("vertice (−1, −2)", -1, -2, "blu", dx=10, dy=4)
g.etichetta("zero", -3, 0, "rosso", dy=-10, dx=8)
g.etichetta("zero", 1, 0, "rosso", dy=-10, dx=-8, anchor="end")
g.salva("06-valore-assoluto-grafico.svg")

# ===================== 8. PARABOLA (esercizio 12) =====================
g = Grafico(-2.5, 4.5, -2.8, 5.0, ux=50)
g.griglia()
g.assi(interi(-2, 4), interi(-2, 4))
g.curva(lambda x: -(x - 1) ** 2 + 4, colore="blu")
g.segmento((1, -2.8), (1, 5.0), "grigio", 1.3, "5,4")
g.punto(1, 4, "rosso"); g.punto(-1, 0, "verde"); g.punto(3, 0, "verde"); g.punto(0, 3)
g.etichetta("vertice V(1, 4)", 1, 4, "rosso", dx=10, dy=-8)
g.etichetta("(0, 3)", 0, 3, dx=10, dy=18, size=13)
g.etichetta("asse x = 1", 1, -2.4, "grigio", dx=6, size=13)
g.etichetta("y = −(x − 1)² + 4", 2.6, 2.0, "blu", dx=8)
g.salva("06-parabola.svg")

# ===================== 9. ESPONENZIALI =====================
g = Grafico(-3.5, 3.5, -0.8, 5.5, ux=60)
g.griglia(0.5, 0.5)
g.assi(interi(-3, 3), interi(1, 5))
g.curva(lambda x: 2 ** x, colore="blu")
g.curva(lambda x: math.e ** x, colore="verde", spessore=2)
g.curva(lambda x: 0.5 ** x, colore="rosso")
g.punto(0, 1)
g.punto(1, 2, "blu"); g.punto(-1, 2, "rosso"); g.punto(1, math.e, "verde")
g.etichetta("y = 2ˣ", 2.33, 5.0, "blu", anchor="start", dx=6)
g.etichetta("y = eˣ", 1.62, 5.0, "verde", anchor="end", dx=-6)
g.etichetta("y = (½)ˣ", -2.32, 5.0, "rosso", anchor="end", dx=-6)
g.etichetta("(1, 2)", 1, 2, "blu", dx=10, dy=8)
g.etichetta("(1, e)", 1, math.e, "verde", dx=-8, dy=-4, anchor="end")
g.etichetta("(−1, 2)", -1, 2, "rosso", dx=-8, dy=-6, anchor="end")
g.etichetta("asintoto y = 0", 2.2, 0, "grigio", dy=40, size=13, anchor="middle")
g.salva("06-esponenziali.svg")

# ===================== 10. ESPONENZIALE E LOGARITMO SIMMETRICI =====================
g = Grafico(-3.3, 5.3, -3.3, 5.3, ux=52)
g.griglia()
g.assi(interi(-3, 5), interi(-3, 5))
g.curva(lambda x: x, colore="grigio", spessore=1.5, tratteggio="6,5")
g.curva(lambda x: 2 ** x, colore="blu")
g.curva(lambda x: math.log2(x), a=0.001, colore="rosso", n=4000)
g.punto(0, 1, "blu"); g.punto(1, 2, "blu"); g.punto(2, 4, "blu")
g.punto(1, 0, "rosso"); g.punto(2, 1, "rosso"); g.punto(4, 2, "rosso")
g.segmento((2, 4), (4, 2), "viola", 1.3, "3,3")
g.segmento((1, 2), (2, 1), "viola", 1.3, "3,3")
g.etichetta("y = 2ˣ", 2.3, 5.0, "blu", anchor="end", dx=-4)
g.etichetta("y = log₂ x", 5.2, 2.37, "rosso", anchor="end", dy=-10)
g.etichetta("y = x", 5.2, 5.2, "grigio", anchor="end", dx=-6, dy=4)
g.etichetta("(2, 4)", 2, 4, "blu", dx=-8, anchor="end")
g.etichetta("(4, 2)", 4, 2, "rosso", dy=22, anchor="middle")
g.etichetta("(0, 1)", 0, 1, "blu", dx=-8, dy=-4, anchor="end", size=13)
g.salva("06-esp-log-simmetrici.svg")

# ===================== 11. LOGARITMI CON BASI DIVERSE =====================
g = Grafico(-0.8, 6.5, -3.3, 3.3, ux=60)
g.griglia(0.5, 0.5)
g.assi(interi(1, 6), interi(-3, 3))
g.curva(lambda x: math.log2(x), a=0.0005, colore="blu", n=5000)
g.curva(lambda x: math.log(x), a=0.0005, colore="verde", spessore=2, n=5000)
g.curva(lambda x: math.log(x, 0.5), a=0.0005, colore="rosso", n=5000)
g.punto(1, 0); g.punto(2, 1, "blu"); g.punto(math.e, 1, "verde"); g.punto(2, -1, "rosso")
g.etichetta("y = log₂ x", 6.4, math.log2(6.4), "blu", anchor="end", dy=-10)
g.etichetta("y = ln x", 6.4, math.log(6.4), "verde", anchor="end", dy=20)
g.etichetta("y = log½ x", 6.4, math.log(6.4, 0.5), "rosso", anchor="end", dy=24)
g.etichetta("(e, 1)", math.e, 1, "verde", dx=8, dy=18, size=13)
g.etichetta("asintoto x = 0", 0, -2.9, "grigio", dx=8, size=13)
g.salva("06-logaritmi.svg")

# ===================== 12. ESERCIZIO 9: 2^x - 1 e ln(x+2) =====================
g = Grafico(-3.3, 3.5, -2.8, 3.8, ux=58)
g.griglia(0.5, 0.5)
g.assi(interi(-3, 3), interi(-2, 3))
g.curva(lambda x: 2 ** x - 1, colore="blu")
g.curva(lambda x: math.log(x + 2), a=-1.9999, colore="rosso", n=5000)
g.asintoto_o(-1, "blu")
g.asintoto_v(-2, "rosso")
g.punto(0, 0)
g.punto(-1, 0, "rosso"); g.punto(0, math.log(2), "rosso")
g.etichetta("y = 2ˣ − 1", 2.1, 3.3, "blu", anchor="end", dx=-4)
g.etichetta("y = ln(x + 2)", 3.4, math.log(5.4), "rosso", anchor="end", dy=-10)
g.etichetta("y = −1", -3.2, -1, "blu", dy=18, size=13)
g.etichetta("x = −2", -2, -2.6, "rosso", dx=-6, anchor="end", size=13)
g.etichetta("(0, ln 2)", 0, math.log(2), "rosso", dx=-8, dy=-6, anchor="end", size=13)
g.etichetta("(−1, 0)", -1, 0, "rosso", dx=-8, dy=-10, anchor="end", size=13)
g.salva("06-esercizio-esp-log.svg")

# ===================== 13. CRESCITA ESPONENZIALE =====================
g = Grafico(0, 60, 0, 2200, ux=8.5, uy=0.17, margine=55, xlab="t (anni)", ylab="N")
g.griglia(10, 200)
g.assi([(k, str(k)) for k in range(10, 61, 10)], [(k, str(k)) for k in range(200, 2001, 400)], origine=False)
g.curva(lambda t: 200 * math.exp(0.04 * t), colore="blu")
T = math.log(2) / 0.04
for k, val in ((1, 400), (2, 800), (3, 1600)):
    t = k * T
    g.segmento((t, 0), (t, val), "grigio", 1.2, "4,4")
    g.segmento((0, val), (t, val), "grigio", 1.2, "4,4")
    g.punto(t, val, "rosso")
g.punto(0, 200, "rosso")
g.etichetta("N(t) = 200·e^(0,04 t)", 30, 1500, "blu", anchor="end", dx=-20)
g.etichetta("ogni 17,3 anni la popolazione raddoppia", 31, 300, "rosso", size=13)
g.etichetta("17,3", T, 0, "rosso", dy=-6, dx=4, size=12)
g.etichetta("34,7", 2 * T, 0, "rosso", dy=-6, dx=4, size=12)
g.etichetta("52,0", 3 * T, 0, "rosso", dy=-6, dx=4, size=12)
g.salva("06-crescita-raddoppio.svg")


# ===================== TRIGONOMETRIA: circonferenze =====================
def circonferenza_base(g):
    g.parametrica(math.cos, math.sin, 0, 2 * PI, colore="nero", spessore=1.6)


# 14. radiante: arco lungo quanto il raggio
g = Grafico(-1.5, 1.6, -1.4, 1.5, ux=150)
g.assi([], [])
circonferenza_base(g)
g.segmento((0, 0), (1, 0), "blu", 2.6, None)
g.segmento((0, 0), (math.cos(1), math.sin(1)), "blu", 2.6, None)
g.parametrica(math.cos, math.sin, 0, 1, colore="rosso", spessore=4.5)
g.parametrica(lambda t: 0.25 * math.cos(t), lambda t: 0.25 * math.sin(t), 0, 1, colore="nero", spessore=1.4)
g.etichetta("r", 0.5, 0, "blu", dy=20, anchor="middle", size=17, stile="italic")
g.etichetta("r", 0.5 * math.cos(1), 0.5 * math.sin(1), "blu", dx=-14, dy=0, size=17, stile="italic")
g.etichetta("arco lungo r", math.cos(0.5), math.sin(0.5), "rosso", dx=12, size=15)
g.etichetta("1 rad ≈ 57,3°", 0.27, 0.13, dx=4, size=14)
g.salva("06-radiante.svg")

# 15. circonferenza goniometrica: seno, coseno, tangente
a = 0.85
g = Grafico(-1.5, 1.75, -1.4, 1.6, ux=150)
g.assi([], [])
circonferenza_base(g)
c, s = math.cos(a), math.sin(a)
g.etichetta("1", 1, 0, dx=-6, dy=20, anchor="end", size=13)
g.etichetta("−1", -1, 0, dx=-6, dy=20, anchor="end", size=13)
g.etichetta("1", 0, 1, dx=-6, dy=-6, anchor="end", size=13)
g.etichetta("−1", 0, -1, dx=-6, dy=20, anchor="end", size=13)
g.segmento((1, -1.4), (1, 1.6), "grigio", 1.2, "5,4")
g.segmento((0, 0), (1, math.tan(a)), "grigio", 1.3, "5,4")
g.segmento((0, 0), (c, s), "nero", 2.2, None)
g.segmento((c, 0), (c, s), "rosso", 3.2, None)
g.segmento((0, 0), (c, 0), "blu", 3.2, None)
g.segmento((1, 0), (1, math.tan(a)), "verde", 3.2, None)
g.parametrica(lambda t: 0.22 * math.cos(t), lambda t: 0.22 * math.sin(t), 0, a, colore="nero", spessore=1.4)
g.punto(c, s); g.punto(1, math.tan(a), "verde"); g.punto(1, 0)
g.etichetta("P = (cos α, sin α)", c, s, dx=8, dy=-10)
g.etichetta("sin α", c, s / 2, "rosso", dx=-8, dy=5, anchor="end")
g.etichetta("cos α", c / 2, 0, "blu", dy=22, anchor="middle")
g.etichetta("tan α", 1, math.tan(a) * 0.55, "verde", dx=8)
g.etichetta("α", 0.3, 0.13, size=16, stile="italic")
g.salva("06-circonferenza-goniometrica.svg")

# 16. angoli notevoli sulla circonferenza
g = Grafico(-1.75, 1.75, -1.55, 1.55, ux=150)
g.assi([], [])
circonferenza_base(g)
notevoli = [(0, "0"), (PI / 6, "π/6"), (PI / 4, "π/4"), (PI / 3, "π/3"), (PI / 2, "π/2"),
            (2 * PI / 3, "2π/3"), (3 * PI / 4, "3π/4"), (5 * PI / 6, "5π/6"), (PI, "π"),
            (7 * PI / 6, "7π/6"), (5 * PI / 4, "5π/4"), (4 * PI / 3, "4π/3"), (3 * PI / 2, "3π/2"),
            (5 * PI / 3, "5π/3"), (7 * PI / 4, "7π/4"), (11 * PI / 6, "11π/6")]
for ang, lab in notevoli:
    c, s = math.cos(ang), math.sin(ang)
    g.segmento((0, 0), (c, s), "griglia", 1, None)
    g.punto(c, s, "blu", r=3.6)
    anc = "start" if c > 0.2 else ("end" if c < -0.2 else "middle")
    g.etichetta(lab, 1.16 * c, 1.16 * s, "nero", size=14, anchor=anc, dy=5)
# coordinate di pi/6, pi/4, pi/3
g.etichetta("(√3/2, 1/2)", math.cos(PI / 6), math.sin(PI / 6), "rosso", size=12, anchor="end", dx=-8, dy=14)
g.etichetta("(√2/2, √2/2)", math.cos(PI / 4), math.sin(PI / 4), "rosso", size=12, anchor="end", dx=-8, dy=14)
g.etichetta("(1/2, √3/2)", math.cos(PI / 3), math.sin(PI / 3), "rosso", size=12, anchor="end", dx=-8, dy=14)
g.etichetta("(0°)", 1.16, 0, "grigio", size=11, dy=20)
g.etichetta("(90°)", 0, 1.16, "grigio", size=11, dx=26, dy=5)
g.etichetta("(180°)", -1.16, 0, "grigio", size=11, anchor="end", dy=20)
g.etichetta("(270°)", 0, -1.16, "grigio", size=11, dx=30, dy=5)
g.salva("06-angoli-notevoli.svg")

# ===================== 17. SENO E COSENO =====================
g = Grafico(-2 * PI - 0.3, 2 * PI + 0.5, -1.6, 1.8, ux=42, uy=80)
g.griglia(PI / 2, 0.5)
g.assi(tacche_pi(-4, 4), [(1, "1"), (-1, "−1")])
g.curva(math.sin, colore="rosso")
g.curva(math.cos, colore="blu")
g.etichetta("y = sin x", PI / 2, 1, "rosso", dy=-10, anchor="middle")
g.etichetta("y = cos x", -2 * PI, 1, "blu", dx=6, dy=-10)
g.segmento((0, -1.45), (2 * PI, -1.45), "viola", 1.6, None)
g.etichetta("un periodo: 2π", PI, -1.45, "viola", dy=-6, size=13, anchor="middle")
g.salva("06-seno-coseno.svg")

# ===================== 18. TANGENTE =====================
g = Grafico(-3 * PI / 2 - 0.3, 3 * PI / 2 + 0.5, -4, 4, ux=48, uy=40)
g.griglia(PI / 4, 1)
g.assi(tacche_pi(-3, 3), interi(-3, 3))
g.curva(math.tan, colore="verde", n=4000, salto=5)
for k in (-3, -1, 1, 3):
    g.asintoto_v(k * PI / 2)
g.etichetta("y = tan x", PI / 4, 1, "verde", dx=10, dy=6)
g.etichetta("asintoti x = π/2 + kπ", PI / 2, 3.6, "grigio", dx=6, size=13)
g.salva("06-tangente.svg")

# ===================== 19. A cos(Bx) + C =====================
g = Grafico(-0.4, 2 * PI + 0.5, -1.7, 5.6, ux=60, uy=45)
g.griglia(PI / 4, 1)
g.assi(tacche_pi(1, 4, 2), interi(-1, 5))
g.curva(math.cos, colore="grigio", spessore=1.8, tratteggio="6,5")
g.curva(lambda x: 3 * math.cos(2 * x) + 2, colore="blu")
g.asintoto_o(2, "viola")
g.segmento((PI, 2), (PI, 5), "rosso", 2, None)
g.segmento((0, 5.3), (PI, 5.3), "verde", 1.6, None)
g.etichetta("y = 3 cos(2x) + 2", 3 * PI / 2, -1, "blu", dx=12, dy=4)
g.etichetta("y = cos x", 2 * PI, 1, "grigio", anchor="end", dx=-8, dy=-6, size=13)
g.etichetta("y = 2", 2 * PI + 0.45, 2, "viola", dy=-6, anchor="end", size=13)
g.etichetta("ampiezza 3", PI, 3.5, "rosso", dx=8, size=13)
g.etichetta("periodo π", PI / 2, 5.3, "verde", dy=-6, anchor="middle", size=13)
g.salva("06-coseno-trasformato.svg")

# ===================== 20. EQUAZIONI sin x = k e cos x = k sulla circonferenza =====================
g = Grafico(-1.6, 1.6, -1.45, 1.55, ux=140)
g.assi([], [])
circonferenza_base(g)
k = math.sqrt(3) / 2
g.segmento((-1.6, k), (1.6, k), "rosso", 1.5, "6,4")
for ang, lab, anc, dx in ((PI / 3, "π/3", "start", 8), (2 * PI / 3, "2π/3", "end", -8)):
    c, s = math.cos(ang), math.sin(ang)
    g.segmento((0, 0), (c, s), "blu", 2, None)
    g.punto(c, s, "blu")
    g.etichetta(lab, c, s, "blu", dx=dx, dy=-10, anchor=anc, size=15)
g.etichetta("y = √3/2", 1.58, k, "rosso", anchor="end", dy=20, size=13)
g.etichetta("sin x = √3/2", -1.5, -1.25, "nero", size=15)
g.salva("06-equazione-seno.svg")

g = Grafico(-1.6, 1.6, -1.45, 1.55, ux=140)
g.assi([], [])
circonferenza_base(g)
g.segmento((-0.5, -1.45), (-0.5, 1.55), "rosso", 1.5, "6,4")
for ang, lab, dy in ((2 * PI / 3, "2π/3", -10), (4 * PI / 3, "4π/3", 22)):
    c, s = math.cos(ang), math.sin(ang)
    g.segmento((0, 0), (c, s), "blu", 2, None)
    g.punto(c, s, "blu")
    g.etichetta(lab, c, s, "blu", dx=-10, dy=dy, anchor="end", size=15)
g.etichetta("x = −1/2", -0.5, -1.3, "rosso", dx=8, size=13)
g.etichetta("cos x = −1/2", 0.55, -1.25, "nero", size=15)
g.salva("06-equazione-coseno.svg")

# ===================== 21. ARCOSENO =====================
g = Grafico(-2.0, 2.0, -2.0, 2.0, ux=100)
g.griglia(0.5, 0.5)
g.assi([(-PI / 2, "−π/2"), (-1, "−1"), (1, "1"), (PI / 2, "π/2")],
       [(-PI / 2, "−π/2"), (-1, "−1"), (1, "1"), (PI / 2, "π/2")])
g.curva(lambda x: x, colore="grigio", spessore=1.4, tratteggio="6,5")
g.curva(math.sin, a=-PI / 2, b=PI / 2, colore="rosso", spessore=2)
g.curva(math.asin, a=-1, b=1, colore="blu", n=4000)
g.punto(1, PI / 2, "blu"); g.punto(-1, -PI / 2, "blu")
g.punto(PI / 2, 1, "rosso"); g.punto(-PI / 2, -1, "rosso")
g.etichetta("y = arcsin x", 1, PI / 2, "blu", dx=-10, anchor="end", dy=4)
g.etichetta("y = sin x", PI / 2, 1, "rosso", anchor="middle", dy=26)
g.etichetta("y = x", 1.9, 1.9, "grigio", anchor="end", dx=-6, dy=4, size=13)
g.salva("06-arcoseno.svg")

# ===================== 22. ARCOCOSENO =====================
g = Grafico(-1.6, 3.6, -1.5, 3.6, ux=90)
g.griglia(0.5, 0.5)
g.assi([(-1, "−1"), (1, "1"), (PI / 2, "π/2"), (PI, "π")],
       [(-1, "−1"), (1, "1"), (PI / 2, "π/2"), (PI, "π")])
g.curva(lambda x: x, colore="grigio", spessore=1.4, tratteggio="6,5")
g.curva(math.cos, a=0, b=PI, colore="rosso", spessore=2)
g.curva(math.acos, a=-1, b=1, colore="blu", n=4000)
g.punto(-1, PI, "blu"); g.punto(1, 0, "blu"); g.punto(0, PI / 2, "blu")
g.punto(PI, -1, "rosso"); g.punto(0, 1, "rosso")
g.etichetta("y = arccos x", 0.15, 2.6, "blu")
g.etichetta("y = cos x", PI, -1, "rosso", anchor="end", dx=-4, dy=24)
g.etichetta("y = x", 3.5, 3.5, "grigio", anchor="end", dx=-6, dy=4, size=13)
g.salva("06-arcocoseno.svg")

# ===================== 23. ARCOTANGENTE =====================
g = Grafico(-6.3, 6.3, -2.2, 2.2, ux=50, uy=80)
g.griglia(1, 0.5)
g.assi(interi(-6, 6), [(-PI / 2, "−π/2"), (PI / 2, "π/2"), (-1, "−1"), (1, "1")])
g.curva(math.atan, colore="blu")
g.asintoto_o(PI / 2); g.asintoto_o(-PI / 2)
g.punto(1, PI / 4, "blu")
g.etichetta("y = arctan x", 3.5, math.atan(3.5), "blu", dy=24, anchor="middle")
g.etichetta("(1, π/4)", 1, PI / 4, "blu", dx=10, dy=22, size=13)
g.etichetta("y = π/2 (mai raggiunto)", -6.1, PI / 2, "grigio", dy=-7, size=13)
g.etichetta("y = −π/2", 6.1, -PI / 2, "grigio", dy=18, anchor="end", size=13)
g.salva("06-arcotangente.svg")

# ===================== 24. PENDENZA =====================
g = Grafico(-0.5, 11.6, -1.0, 2.6, ux=55)
g.area([(0, 0), (10, 0), (10, 1.2)], "arancio", 0.18)
g.segmento((0, 0), (10.6, 0), "nero", 1.6, None)
g.segmento((0, 0), (10, 1.2), "arancio", 3.2, None)
g.segmento((10, 0), (10, 1.2), "nero", 1.6, "5,4")
g.parametrica(lambda t: 2.2 * math.cos(t), lambda t: 2.2 * math.sin(t), 0, math.atan(0.12), colore="nero", spessore=1.4)
g.etichetta("α", 2.3, 0.13, size=16, dx=4, stile="italic")
g.etichetta("100 m in orizzontale", 5, 0, dy=22, anchor="middle", size=14)
g.etichetta("12 m", 10, 0.6, dx=8, size=14)
g.etichetta("pendenza 12% = 12/100 = tan α", 4.6, 1.75, "arancio", anchor="middle", size=15)
g.salva("06-pendenza.svg")
