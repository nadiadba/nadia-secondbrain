"""Disegni per la bozza di matematica 03 - I vettori.

Uso: python3 -I .claude/scripts/disegni/matematica-05.py
Scrive gli SVG in anno-1/semestre-1/matematica/bozze/img/ (prefisso 05-).
Nessuna dipendenza esterna.
"""
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.abspath(os.path.join(QUI, "..", "..", ".."))
OUT = os.path.join(RADICE, "anno-1", "semestre-1", "matematica", "bozze", "img")

BLU = "#1f5fa8"
ROSSO = "#c0392b"
VERDE = "#2e7d4f"
VIOLA = "#7d3c98"
ARANCIO = "#d68910"
GRIGIO = "#666666"
GRIGIO_CHIARO = "#e6e6e6"
FONT = "Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fmt_label(s):
    """Markup minimo: *x* = grassetto (vettori), _x_ = pedice, ^x^ = apice."""
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "*":
            j = s.index("*", i + 1)
            out.append('<tspan font-weight="bold">%s</tspan>' % esc(s[i + 1:j]))
            i = j + 1
        elif c == "_":
            j = s.index("_", i + 1)
            out.append('<tspan font-size="75%%" dy="4">%s</tspan><tspan dy="-4">\u200b</tspan>' % esc(s[i + 1:j]))
            i = j + 1
        elif c == "^":
            j = s.index("^", i + 1)
            out.append('<tspan font-size="75%%" dy="-6">%s</tspan><tspan dy="6">\u200b</tspan>' % esc(s[i + 1:j]))
            i = j + 1
        else:
            out.append(esc(c))
            i += 1
    return "".join(out)


class Tela:
    """Tela SVG in coordinate schermo (pixel). Le sottoclassi mappano le coordinate."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.el = []

    def map(self, p):
        return p

    # primitive in coordinate "del mondo"
    def linea(self, a, b, col=GRIGIO, sw=1.5, dash=None, op=1):
        (x1, y1), (x2, y2) = self.map(a), self.map(b)
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        self.el.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s opacity="%s"/>'
                       % (x1, y1, x2, y2, col, sw, d, op))

    def poligono(self, pts, fill="none", stroke="none", sw=1, op=1, dash=None):
        s = " ".join("%.1f,%.1f" % self.map(p) for p in pts)
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        self.el.append('<polygon points="%s" fill="%s" fill-opacity="%s" stroke="%s" stroke-width="%s"%s/>'
                       % (s, fill, op, stroke, sw, d))

    def freccia(self, a, b, col=BLU, sw=2.6, dash=None, testa=12):
        (x1, y1), (x2, y2) = self.map(a), self.map(b)
        L = math.hypot(x2 - x1, y2 - y1)
        if L < 1e-6:
            return
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        bx, by = x2 - ux * testa, y2 - uy * testa
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        self.el.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s stroke-linecap="round"/>'
                       % (x1, y1, bx + ux * 2, by + uy * 2, col, sw, d))
        px, py = -uy, ux
        w = testa * 0.42
        self.el.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
                       % (x2, y2, bx + px * w, by + py * w, bx - px * w, by - py * w, col))

    def punto(self, p, col="#222", r=3.6):
        x, y = self.map(p)
        self.el.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, r, col))

    def testo(self, p, s, col="#222", size=16, anchor="middle", dx=0, dy=0, italic=False, bg=False):
        x, y = self.map(p)
        x += dx
        y += dy
        st = ' font-style="italic"' if italic else ""
        if bg:
            # alone bianco per leggibilita'
            self.el.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" text-anchor="%s"%s '
                           'stroke="white" stroke-width="4" stroke-linejoin="round" fill="white">%s</text>'
                           % (x, y, FONT, size, anchor, st, fmt_label(s)))
        self.el.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" text-anchor="%s" fill="%s"%s>%s</text>'
                       % (x, y, FONT, size, anchor, col, st, fmt_label(s)))

    def testo_px(self, x, y, s, col="#222", size=16, anchor="middle", italic=False):
        st = ' font-style="italic"' if italic else ""
        self.el.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" text-anchor="%s" fill="%s"%s>%s</text>'
                       % (x, y, FONT, size, anchor, col, st, fmt_label(s)))

    def arco(self, centro, r_px, a1, a2, col=ARANCIO, sw=2, fill=None):
        """Arco di raggio r_px (pixel) attorno a centro, angoli in gradi (matematici, antiorari) a1->a2."""
        cx, cy = self.map(centro)
        n = 40
        pts = []
        for k in range(n + 1):
            t = math.radians(a1 + (a2 - a1) * k / n)
            pts.append((cx + r_px * math.cos(t), cy - r_px * math.sin(t)))
        d = "M %.1f,%.1f " % pts[0] + " ".join("L %.1f,%.1f" % q for q in pts[1:])
        if fill:
            self.el.append('<path d="M %.1f,%.1f %s Z" fill="%s" fill-opacity="0.25" stroke="none"/>'
                           % (cx, cy, d.replace("M", "L", 1), fill))
        self.el.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, col, sw))

    def angolo_retto(self, vertice, dir1, dir2, size=12, col=GRIGIO):
        cx, cy = self.map(vertice)
        def u(d):
            x, y = self.map((vertice[0] + d[0], vertice[1] + d[1])) if len(vertice) == 2 else \
                self.map(tuple(vertice[i] + d[i] for i in range(3)))
            L = math.hypot(x - cx, y - cy)
            return (x - cx) / L, (y - cy) / L
        a, b = u(dir1), u(dir2)
        p1 = (cx + a[0] * size, cy + a[1] * size)
        p2 = (cx + (a[0] + b[0]) * size, cy + (a[1] + b[1]) * size)
        p3 = (cx + b[0] * size, cy + b[1] * size)
        self.el.append('<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.4"/>'
                       % (p1 + p2 + p3 + (col,)))

    def salva(self, nome):
        os.makedirs(OUT, exist_ok=True)
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">\n'
               '<rect width="100%%" height="100%%" fill="white"/>\n%s\n</svg>\n'
               % (self.w, self.h, self.w, self.h, "\n".join(self.el)))
        with open(os.path.join(OUT, nome), "w", encoding="utf-8") as f:
            f.write(svg)
        print("scritto", nome)


class Piano(Tela):
    """Piano cartesiano: (xmin..xmax) x (ymin..ymax), s pixel per unita', ox/oy = offset."""

    def __init__(self, xmin, xmax, ymin, ymax, s=50, margine=30, extra_w=0, ox=0):
        self.xmin, self.xmax, self.ymin, self.ymax, self.s = xmin, xmax, ymin, ymax, s
        self.m = margine
        self.ox = ox
        w = (xmax - xmin) * s + 2 * margine + extra_w
        h = (ymax - ymin) * s + 2 * margine
        super().__init__(int(w), int(h))

    def map(self, p):
        x, y = p
        return (self.ox + self.m + (x - self.xmin) * self.s, self.m + (self.ymax - y) * self.s)

    def griglia(self, assi=True, numeri=True, label=("x", "y")):
        for i in range(math.ceil(self.xmin), math.floor(self.xmax) + 1):
            self.linea((i, self.ymin), (i, self.ymax), col=GRIGIO_CHIARO, sw=1)
        for j in range(math.ceil(self.ymin), math.floor(self.ymax) + 1):
            self.linea((self.xmin, j), (self.xmax, j), col=GRIGIO_CHIARO, sw=1)
        if not assi:
            return
        e = 18.0 / self.s
        self.freccia((self.xmin, 0), (self.xmax + e, 0), col="#333", sw=1.4, testa=10)
        self.freccia((0, self.ymin), (0, self.ymax + e), col="#333", sw=1.4, testa=10)
        self.testo((self.xmax + e, 0), label[0], dx=-4, dy=20, italic=True)
        self.testo((0, self.ymax + e), label[1], dx=14, dy=10, italic=True)
        if numeri:
            for i in range(math.ceil(self.xmin), math.floor(self.xmax) + 1):
                if i != 0:
                    self.testo((i, 0), str(i).replace("-", "−"), size=12, col=GRIGIO, dy=16)
            for j in range(math.ceil(self.ymin), math.floor(self.ymax) + 1):
                if j != 0:
                    self.testo((0, j), str(j).replace("-", "−"), size=12, col=GRIGIO, dx=-8, dy=4, anchor="end")
            self.testo((0, 0), "O", size=13, col=GRIGIO, dx=-9, dy=16)


class Spazio(Tela):
    """Assonometria cavaliera: y orizzontale a destra, z verticale in alto, x obliquo verso chi guarda."""

    def __init__(self, w, h, origine, s=45, k=0.55, ang=225):
        super().__init__(w, h)
        self.o = origine
        self.s = s
        a = math.radians(ang)
        self.ex = (k * math.cos(a), -k * math.sin(a))  # direzione schermo dell'asse x (y schermo in giu')

    def map(self, p):
        x, y, z = p
        X = self.o[0] + self.s * (y + x * self.ex[0])
        Y = self.o[1] + self.s * (-z + x * self.ex[1])
        return (X, Y)

    def assi(self, lx=4, ly=4, lz=4, neg=0.0):
        self.freccia((-neg, 0, 0), (lx, 0, 0), col="#333", sw=1.4, testa=10)
        self.freccia((0, -neg, 0), (0, ly, 0), col="#333", sw=1.4, testa=10)
        self.freccia((0, 0, -neg), (0, 0, lz), col="#333", sw=1.4, testa=10)
        self.testo((lx, 0, 0), "x", italic=True, dx=-6, dy=18)
        self.testo((0, ly, 0), "y", italic=True, dx=6, dy=18)
        self.testo((0, 0, lz), "z", italic=True, dx=-12, dy=6)
        self.testo((0, 0, 0), "O", size=13, col=GRIGIO, dx=-10, dy=-6)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(k, a):
    return tuple(k * x for x in a)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def deg(v):
    return math.degrees(math.atan2(v[1], v[0]))


# ---------------------------------------------------------------- disegni

def vettore_freccia():
    """Freccia da A a B, coda e punta, e lo stesso vettore spostato (CD)."""
    t = Piano(0, 9, -0.6, 5, s=55)
    for i in range(0, 10):
        t.linea((i, 0), (i, 5), col=GRIGIO_CHIARO, sw=1)
    for j in range(0, 6):
        t.linea((0, j), (9, j), col=GRIGIO_CHIARO, sw=1)
    A, B = (1, 1), (4, 3)
    C, D = (5, 2), (8, 4)
    t.freccia(A, B, col=BLU)
    t.freccia(C, D, col=BLU)
    for p, n, dx, dy in [(A, "A (coda)", -6, 20), (B, "B (punta)", 0, -12), (C, "C", 4, 20), (D, "D", 6, -10)]:
        t.punto(p)
        t.testo(p, n, dx=dx, dy=dy, anchor="middle")
    t.testo((2.5, 2), "*v*", col=BLU, dx=-10, dy=-8, size=18)
    t.testo((6.5, 3), "*v*", col=BLU, dx=-10, dy=-8, size=18)
    t.testo((4.5, -0.45), "stessa lunghezza, stessa direzione, stesso verso: è lo stesso vettore", size=14, col=GRIGIO)
    t.salva("05-vettore-freccia.svg")


def componenti_piano():
    t = Piano(-1, 6, -1, 4.5, s=55)
    t.griglia()
    u = (4, 3)
    t.linea((u[0], 0), u, col=GRIGIO, dash="5,4")
    t.linea((0, u[1]), u, col=GRIGIO, dash="5,4")
    t.freccia((0, 0), (u[0], 0), col=ARANCIO, sw=2, testa=10)
    t.freccia((u[0], 0), u, col=VERDE, sw=2, testa=10)
    t.freccia((0, 0), u, col=BLU)
    t.testo((2, 0), "u_1_ = 4", col=ARANCIO, dy=-8, size=15)
    t.testo((4, 1.5), "u_2_ = 3", col=VERDE, dx=8, anchor="start", size=15)
    t.testo((2, 1.5), "*u* = (4, 3)", col=BLU, dx=-12, dy=-8, anchor="end", size=17)
    t.punto(u)
    t.testo(u, "punta (4, 3)", dx=6, dy=-10, anchor="start", size=14)
    t.testo((2, 1.5), "‖*u*‖ = 5", col=BLU, dx=6, dy=30, anchor="start", size=15)
    t.salva("05-componenti-piano.svg")


def componenti_spazio():
    t = Spazio(600, 420, (200, 300), s=52)
    u = (3, 4, 3)
    t.assi(lx=4.3, ly=5.2, lz=4.6)
    x, y, z = u
    # scatola tratteggiata
    P = [(0, 0, 0), (x, 0, 0), (x, y, 0), (0, y, 0)]
    for a, b in [((x, 0, 0), (x, y, 0)), ((0, y, 0), (x, y, 0)), ((x, y, 0), (x, y, z)),
                 ((0, 0, z), (x, 0, z)), ((0, 0, z), (0, y, z)), ((x, 0, z), (x, y, z)), ((0, y, z), (x, y, z)),
                 ((x, 0, 0), (x, 0, z)), ((0, y, 0), (0, y, z))]:
        t.linea(a, b, col=GRIGIO, dash="5,4", sw=1.2)
    t.poligono([(0, 0, 0), (x, 0, 0), (x, y, 0), (0, y, 0)], fill=BLU, op=0.07)
    t.freccia((0, 0, 0), u, col=BLU)
    t.punto(u)
    t.testo(u, "(u_1_, u_2_, u_3_) = (3, 4, 3)", dx=8, dy=-10, anchor="start", size=14)
    t.testo((x, 0, 0), "u_1_", col=ARANCIO, dx=-14, dy=6, size=15)
    t.testo((0, y, 0), "u_2_", col=VERDE, dx=0, dy=20, size=15)
    t.testo((0, 0, z), "u_3_", col=VIOLA, dx=-16, dy=5, size=15)
    t.testo(mul(0.55, u), "*u*", col=BLU, dx=-14, dy=-6, size=18)
    t.salva("05-componenti-spazio.svg")


def vettore_tra_punti():
    t = Piano(-1, 6, -2, 3.5, s=55)
    t.griglia()
    A, B = (1, -1), (5, 1)
    v = sub(B, A)
    t.freccia((0, 0), v, col=BLU, dash="7,5", sw=2)
    t.freccia(A, B, col=BLU)
    t.punto(A)
    t.punto(B)
    t.testo(A, "A = (1, −1)", dx=0, dy=22)
    t.testo(B, "B = (5, 1)", dx=6, dy=-10, anchor="start")
    t.testo((3.2, -1.5), "vettore AB = B − A = (4, 2)", col=BLU, anchor="start", size=15)
    t.testo(v, "(4, 2)", col=BLU, dx=-8, dy=-10, anchor="end", size=14)
    t.testo((0.2, 2.9), "la stessa freccia, spostata nell'origine", col=GRIGIO, anchor="start", size=13)
    t.salva("05-vettore-tra-punti.svg")


def somma():
    """Due pannelli: punta-coda e parallelogramma, con u=(2,-1), v=(-3,4)."""
    u, v = (2, -1), (-3, 4)
    s = add(u, v)
    t = Piano(-4, 3.6, -2, 4.6, s=48, extra_w=7.6 * 48 + 50)
    # pannello 1: punta-coda
    t.griglia(numeri=False)
    t.freccia((0, 0), u, col=BLU)
    t.freccia(u, s, col=ROSSO)
    t.freccia((0, 0), s, col=VERDE)
    t.testo(mul(0.5, u), "*u*", col=BLU, dy=22, size=18)
    t.testo(add(u, mul(0.5, v)), "*v*", col=ROSSO, dx=14, anchor="start", size=18)
    t.testo(mul(0.5, s), "*u* + *v*", col=VERDE, dx=-10, anchor="end", size=17)
    t.testo((-0.2, -2), "regola punta-coda", size=15, col="#222", dy=24)
    # pannello 2: parallelogramma (spostato a destra)
    t2 = Piano(-4, 3.6, -2, 4.6, s=48, ox=7.6 * 48 + 50)
    t2.el = t.el
    t2.griglia(numeri=False)
    t2.poligono([(0, 0), u, s, v], fill=VERDE, op=0.08)
    t2.freccia(u, s, col=ROSSO, dash="6,5", sw=1.8)
    t2.freccia(v, s, col=BLU, dash="6,5", sw=1.8)
    t2.freccia((0, 0), u, col=BLU)
    t2.freccia((0, 0), v, col=ROSSO)
    t2.freccia((0, 0), s, col=VERDE)
    t2.testo(mul(0.5, u), "*u*", col=BLU, dy=22, size=18)
    t2.testo(mul(0.5, v), "*v*", col=ROSSO, dx=-14, anchor="end", size=18)
    t2.testo(mul(0.5, s), "*u* + *v*", col=VERDE, dx=10, dy=4, anchor="start", size=17, bg=True)
    t2.punto(s)
    t2.testo(s, "(−1, 3)", dx=8, dy=-8, anchor="start", size=14)
    t2.testo((-0.2, -2), "regola del parallelogramma", size=15, col="#222", dy=24)
    t.salva("05-somma.svg")


def differenza():
    u, v = (2, -1), (-3, 4)
    d = sub(u, v)
    t = Piano(-4, 6, -6, 4.5, s=42)
    t.griglia(numeri=False)
    t.freccia((0, 0), u, col=BLU)
    t.freccia((0, 0), v, col=ROSSO)
    t.freccia(v, u, col=VIOLA)
    t.freccia((0, 0), d, col=VIOLA, dash="7,5", sw=2)
    t.testo(u, "*u*", col=BLU, dx=12, dy=4, anchor="start", size=18)
    t.testo(mul(0.5, v), "*v*", col=ROSSO, dx=-14, anchor="end", size=18)
    t.testo(add(v, mul(0.5, d)), "*u* − *v*", col=VIOLA, dx=12, dy=-4, anchor="start", size=17)
    t.punto(d)
    t.testo(d, "(5, −5)", dx=8, dy=4, anchor="start", size=14)
    t.testo((3, 3.8), "*u* − *v* va dalla punta di *v* alla punta di *u*", col=GRIGIO, size=13)
    t.salva("05-differenza.svg")


def multipli():
    u = (2, 1)
    t = Piano(-3, 5, -2, 3, s=50)
    t.griglia(numeri=False)
    t.freccia((0, 0), mul(2, u), col=VERDE, sw=2.2)
    t.freccia((0, 0), u, col=BLU, sw=3.2)
    t.freccia((0, 0), mul(-0.5, u), col=ROSSO)
    t.freccia((0, 0), mul(-1, u), col=VIOLA, dash="6,4", sw=1.8)
    t.testo(u, "*u*", col=BLU, dx=-6, dy=-12, size=18)
    t.testo(mul(2, u), "2*u*", col=VERDE, dx=6, dy=-8, anchor="start", size=17)
    t.testo(mul(-0.5, u), "−½ *u*", col=ROSSO, dx=-4, dy=-14, anchor="end", size=16)
    t.testo(mul(-1, u), "−*u* (opposto)", col=VIOLA, dx=10, dy=24, anchor="middle", size=15)
    t.salva("05-multipli.svg")


def base_standard():
    t = Piano(-1, 8, -6, 2, s=42)
    t.griglia()
    a = (7, -5)
    t.freccia((0, 0), (1, 0), col=ARANCIO, sw=3.2)
    t.freccia((0, 0), (0, 1), col=VERDE, sw=3.2)
    t.testo((1, 0), "*e*_1_", col=ARANCIO, dx=-2, dy=-10, size=17)
    t.testo((0, 1), "*e*_2_", col=VERDE, dx=14, dy=6, anchor="start", size=17)
    t.freccia((0, 0), (7, 0), col=ARANCIO, sw=1.8, dash="6,4")
    t.freccia((7, 0), a, col=VERDE, sw=1.8, dash="6,4")
    t.freccia((0, 0), a, col=BLU)
    t.testo((3.5, 0), "7*e*_1_", col=ARANCIO, dy=-10, size=15)
    t.testo((7, -2.5), "−5*e*_2_", col=VERDE, dx=8, anchor="start", size=15)
    t.testo((3.5, -2.5), "*a* = 7*e*_1_ − 5*e*_2_", col=BLU, dx=-10, dy=10, anchor="end", size=16)
    t.punto(a)
    t.testo(a, "(7, −5)", dx=-8, dy=20, anchor="end", size=14)
    t.salva("05-base-standard.svg")


def versore():
    t = Piano(-1.5, 4.5, -1.5, 4.5, s=60)
    t.griglia()
    u = (3, 4)
    # circonferenza unitaria
    c = t.map((0, 0))
    t.el.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="5,4"/>'
                % (c[0], c[1], t.s, VIOLA))
    t.freccia((0, 0), u, col=BLU, sw=2.4)
    t.freccia((0, 0), (0.6, 0.8), col=VIOLA, sw=3.4)
    t.testo(u, "*u* = (3, 4),  ‖*u*‖ = 5", col=BLU, dx=-8, dy=-12, anchor="end", size=15)
    t.testo((0.6, 0.8), "(3/5, 4/5)", col=VIOLA, dx=10, dy=6, anchor="start", size=14)
    t.testo((-0.75, -0.75), "raggio 1", col=VIOLA, dx=-6, dy=14, anchor="end", size=13)
    t.salva("05-versore.svg")


def angolo():
    u, v = (1, 2), (3, 1)
    t = Piano(-0.5, 3.8, -0.5, 2.8, s=85)
    t.griglia()
    t.arco((0, 0), 46, deg(v), deg(u), fill=ARANCIO)
    t.freccia((0, 0), u, col=BLU)
    t.freccia((0, 0), v, col=ROSSO)
    t.testo(u, "*u* = (1, 2)", col=BLU, dx=8, dy=-4, anchor="start", size=16)
    t.testo(v, "*v* = (3, 1)", col=ROSSO, dx=0, dy=-14, anchor="middle", size=16)
    m = (deg(u) + deg(v)) / 2
    t.testo((0, 0), "θ = 45°", col=ARANCIO, dx=62 * math.cos(math.radians(m)) + 4,
            dy=-62 * math.sin(math.radians(m)) + 6, anchor="start", size=15)
    t.salva("05-angolo.svg")


def segno_prodotto_scalare():
    W = 230
    t = Tela(3 * W, 250)
    casi = [((2.2, 0), (1.3, 1.4), "acuto", "*u*·*v* > 0", VERDE),
            ((2.2, 0), (0, 1.9), "retto", "*u*·*v* = 0", GRIGIO),
            ((2.2, 0), (-1.3, 1.4), "ottuso", "*u*·*v* < 0", ROSSO)]
    for i, (u, v, nome, f, col) in enumerate(casi):
        p = Piano(-1.8, 2.6, -0.3, 2.3, s=50, margine=10, ox=i * W)
        p.el = t.el
        o = (0, 0)
        if nome == "retto":
            p.angolo_retto(o, u, v, size=14)
        else:
            p.arco(o, 32, 0, deg(v), fill=col, col=col)
        p.freccia(o, u, col=BLU)
        p.freccia(o, v, col=ROSSO)
        p.testo(u, "*u*", col=BLU, dx=-4, dy=22, size=17)
        p.testo(v, "*v*", col=ROSSO, dx=10 if v[0] >= 0 else -10, dy=0, anchor="start" if v[0] >= 0 else "end", size=17)
        p.testo_px(i * W + W / 2, 200, "angolo " + nome, size=15, col=col)
        p.testo_px(i * W + W / 2, 226, f, size=16, col="#222")
    t.salva("05-segno-prodotto-scalare.svg")


def teorema_coseno():
    u, v = (1.2, 2.6), (3.6, 0.6)
    t = Piano(-0.4, 4.2, -0.4, 3.0, s=85)
    t.el = []
    t.poligono([(0, 0), u, v], fill=ARANCIO, op=0.08)
    t.arco((0, 0), 34, deg(v), deg(u), col=ARANCIO)
    t.freccia((0, 0), u, col=BLU)
    t.freccia((0, 0), v, col=ROSSO)
    t.freccia(v, u, col=VIOLA)
    t.punto((0, 0))
    t.testo((0, 0), "O", dx=-10, dy=8)
    t.testo(mul(0.5, u), "*u*", col=BLU, dx=-12, anchor="end", size=18)
    t.testo(mul(0.5, v), "*v*", col=ROSSO, dy=24, size=18)
    t.testo(mul(0.5, add(u, v)), "*u* − *v*", col=VIOLA, dx=10, dy=-6, anchor="start", size=17)
    t.testo((0, 0), "θ", col=ARANCIO, dx=44, dy=-16, size=17)
    t.salva("05-teorema-coseno.svg")


def proiezione():
    """Due pannelli: angolo acuto (proiezione concorde a v) e ottuso (discorde)."""
    W = 470
    t = Tela(2 * W, 300)
    casi = [((3, 2.5), (4.5, 0), "angolo acuto: *p* ha il verso di *v*", (-0.6, 5.2)),
            ((-2.4, 2.5), (3, 0), "angolo ottuso: *p* ha verso opposto a *v*", (-3.4, 3.8))]
    for i, (u, v, tit, (xa, xb)) in enumerate(casi):
        p = Piano(xa, xb, -0.9, 3.2, s=60, margine=20, ox=i * W + (W - (xb - xa) * 60 - 40) / 2)
        p.el = t.el
        o = (0, 0)
        pr = mul(dot(u, v) / dot(v, v), v)
        # retta di v
        p.linea((xa, 0), (xb, 0), col=GRIGIO_CHIARO, sw=1.5)
        p.linea(u, pr, col=GRIGIO, dash="5,4", sw=1.4)
        p.angolo_retto(pr, sub(u, pr), (1, 0) if pr[0] <= 0 else (-1, 0), size=11)
        p.freccia(o, v, col=ROSSO, sw=2.2)
        p.freccia(o, pr, col=VERDE, sw=4.2, testa=14)
        p.freccia(pr, u, col=VIOLA, sw=2)
        p.freccia(o, u, col=BLU)
        p.testo(mul(0.55, u), "*u*", col=BLU, dx=-10 if u[0] > 0 else 12, anchor="end" if u[0] > 0 else "start", size=18)
        p.testo(v, "*v*", col=ROSSO, dx=6, dy=-10, size=18)
        p.testo(mul(0.5, pr), "*p*", col=VERDE, dy=26, size=18)
        p.testo(add(pr, mul(0.5, sub(u, pr))), "*q*", col=VIOLA, dx=10 if i == 0 else -10,
                anchor="start" if i == 0 else "end", size=18)
        p.testo_px(i * W + W / 2, 288, tit, size=14, col="#222")
    t.salva("05-proiezione.svg")


def area_orientata():
    u, v = (4, 1), (2, 3)
    t = Piano(-0.6, 6.6, -0.6, 4.6, s=55)
    t.h += 30
    t.griglia()
    t.poligono([(0, 0), u, add(u, v), v], fill=BLU, op=0.12, stroke=BLU, sw=1, dash="4,3")
    t.arco((0, 0), 50, deg(u), deg(v), col=ARANCIO, sw=2)
    # punta di freccia sull'arco (verso antiorario)
    a = math.radians(deg(v))
    c = t.map((0, 0))
    tip = (c[0] + 50 * math.cos(a), c[1] - 50 * math.sin(a))
    tang = (-math.sin(a), -math.cos(a))
    nrm = (math.cos(a), -math.sin(a))
    b = (tip[0] - tang[0] * 10, tip[1] - tang[1] * 10)
    t.el.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
                % (tip[0], tip[1], b[0] + nrm[0] * 5, b[1] + nrm[1] * 5, b[0] - nrm[0] * 5, b[1] - nrm[1] * 5, ARANCIO))
    t.freccia((0, 0), u, col=BLU)
    t.freccia((0, 0), v, col=ROSSO)
    t.testo(u, "*u* = (4, 1)", col=BLU, dx=8, dy=14, anchor="start", size=15)
    t.testo(v, "*v* = (2, 3)", col=ROSSO, dx=-8, dy=-6, anchor="end", size=15)
    t.testo(mul(0.5, add(u, v)), "area = 10", col="#222", dx=14, dy=6, size=16, bg=True)
    t.testo_px(t.w / 2, t.h - 14, "per andare da *u* a *v* si gira in senso antiorario: det > 0", col=ARANCIO, size=14)
    t.salva("05-area-orientata.svg")


def prodotto_vettoriale():
    t = Spazio(560, 470, (250, 300), s=58, k=0.6, ang=215)
    u = (4, 0.6, 0)
    v = (0.4, 3.4, 0)
    w = (0, 0, 3.0)  # direzione di u x v (u, v nel piano xy)
    t.assi(lx=4.2, ly=4.6, lz=4.4)
    t.poligono([(0, 0, 0), u, add(u, v), v], fill=BLU, op=0.12, stroke=BLU, sw=1, dash="4,3")
    t.freccia((0, 0, 0), (0, 0, -2.0), col=VIOLA, dash="6,4", sw=2)
    t.freccia((0, 0, 0), u, col=BLU)
    t.freccia((0, 0, 0), v, col=ROSSO)
    t.freccia((0, 0, 0), w, col=VERDE, sw=3)
    t.angolo_retto((0, 0, 0), u, w, size=13)
    t.angolo_retto((0, 0, 0), v, w, size=13)
    t.testo(u, "*u*", col=BLU, dx=-8, dy=20, size=18)
    t.testo(v, "*v*", col=ROSSO, dx=0, dy=26, size=18)
    t.testo(w, "*u* × *v*", col=VERDE, dx=12, dy=4, anchor="start", size=17)
    t.testo((0, 0, -2.0), "*v* × *u* = −(*u* × *v*)", col=VIOLA, dx=12, dy=4, anchor="start", size=15)
    t.testo(mul(0.5, add(u, v)), "area = ‖*u* × *v*‖", col="#222", dx=10, dy=6, size=14, bg=True)
    t.testo_px(20, 28, "la mano destra: dita da *u* verso *v*, il pollice indica *u* × *v*", size=14, anchor="start")
    t.salva("05-prodotto-vettoriale.svg")


def parallelepipedo():
    """Parallelepipedo generato da a, b, c con il tetraedro evidenziato (esercizio 8)."""
    a, b, c = (2, 0, 1), (1, 3, 0), (0, 2, 4)
    t = Spazio(600, 500, (230, 360), s=50, k=0.6, ang=215)
    O = (0, 0, 0)
    V = {}
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                V[(i, j, k)] = add(add(mul(i, a), mul(j, b)), mul(k, c))
    # facce leggermente colorate
    t.assi(lx=3.6, ly=5.4, lz=5.6)
    spigoli = []
    for key in V:
        for d in range(3):
            if key[d] == 0:
                k2 = list(key)
                k2[d] = 1
                spigoli.append((V[key], V[tuple(k2)]))
    for p, q in spigoli:
        if p == O:
            continue
        t.linea(p, q, col="#555", sw=1.3, dash="5,3")
    # tetraedro
    t.poligono([a, b, c], fill=ARANCIO, op=0.25, stroke=ARANCIO, sw=1.5)
    t.poligono([O, b, c], fill=ARANCIO, op=0.10)
    t.freccia(O, a, col=BLU)
    t.freccia(O, b, col=ROSSO)
    t.freccia(O, c, col=VERDE)
    t.testo(a, "*a*", col=BLU, dx=-12, dy=14, size=18)
    t.testo(b, "*b*", col=ROSSO, dx=8, dy=20, size=18)
    t.testo(c, "*c*", col=VERDE, dx=-18, dy=22, size=18, bg=True)
    t.testo_px(330, 470, "parallelepipedo: V = |*a* · (*b* × *c*)| = 26", size=14, anchor="start")
    t.testo_px(330, 492, "tetraedro (arancione): V = 26/6 = 13/3", size=14, anchor="start", col="#a0650a")
    t.h = 505
    t.salva("05-parallelepipedo.svg")


def altezza_parallelepipedo():
    """Perche' il prodotto triplo e' un volume: base = parallelogramma di b e c, altezza = proiezione di a."""
    t = Spazio(560, 430, (200, 330), s=55, k=0.6, ang=215)
    b, c = (3, 0.4, 0), (0.3, 3.4, 0)
    a = (1.2, 1.0, 3.0)
    n = (0, 0, 3.6)
    O = (0, 0, 0)
    t.poligono([O, b, add(b, c), c], fill=BLU, op=0.15, stroke=BLU, sw=1)
    top = [a, add(a, b), add(add(a, b), c), add(a, c)]
    t.poligono(top, fill="none", stroke="#555", sw=1.2, dash="5,3")
    for p in [b, add(b, c), c]:
        t.linea(p, add(p, a), col="#555", sw=1.2, dash="5,3")
    t.freccia(O, n, col=VERDE, sw=2.2)
    t.linea(a, (0, 0, a[2]), col=GRIGIO, dash="4,3", sw=1.4)
    t.freccia(O, b, col=ROSSO)
    t.freccia(O, c, col=ROSSO)
    t.freccia(O, a, col=BLU)
    t.linea((0, 0, 0), (0, 0, a[2]), col=ARANCIO, sw=5, op=0.8)
    t.testo(b, "*b*", col=ROSSO, dx=-6, dy=20, size=18)
    t.testo(c, "*c*", col=ROSSO, dx=10, dy=16, size=18)
    t.testo(a, "*a*", col=BLU, dx=8, dy=22, anchor="start", size=18, bg=True)
    t.testo(n, "*b* × *c*", col=VERDE, dx=10, dy=4, anchor="start", size=16)
    t.testo((0, 0, a[2] / 2), "h", col=ARANCIO, dx=-12, dy=4, anchor="end", size=18, italic=True)
    t.testo(mul(0.5, add(b, c)), "base: ‖*b* × *c*‖", dx=0, dy=10, size=14, bg=True)
    t.salva("05-altezza-parallelepipedo.svg")


if __name__ == "__main__":
    vettore_freccia()
    componenti_piano()
    componenti_spazio()
    vettore_tra_punti()
    somma()
    differenza()
    multipli()
    base_standard()
    versore()
    angolo()
    segno_prodotto_scalare()
    teorema_coseno()
    proiezione()
    area_orientata()
    prodotto_vettoriale()
    parallelepipedo()
    altezza_parallelepipedo()
