"""Piccola libreria per disegnare schemi di geometria descrittiva (metodo di Monge) in SVG.

Convenzioni (come a lezione):
- la linea di terra LT e' orizzontale;
- sopra LT ci sono le seconde proiezioni (P''), sotto LT le prime proiezioni (P');
- un punto nello spazio ha coordinate (x, y, z): x lungo la LT, y = aggetto
  (distanza da pi2, verso chi guarda), z = quota (altezza su pi1).
  Quindi P'' sta a (x, z) e P' sta a (x, -y) nel disegno.
- prima traccia di una retta = dove buca pi1 (z = 0); seconda traccia = dove buca pi2 (y = 0).

Etichette: "_" introduce un pedice, tra graffe se e' piu' di un carattere
(es. "t_1α", "T_{2o}″", "P′").
"""
import math
import re

COLORI = {
    "nero": "#1f1f1f",
    "rosso": "#c0392b",
    "blu": "#2563a8",
    "verde": "#2e8b57",
    "arancio": "#d97706",
    "viola": "#7b4fa0",
    "grigio": "#8a8a8a",
}


# ---------- geometria nello spazio ----------

def P1(p):
    """Prima proiezione di un punto 3D, in coordinate di disegno."""
    return (p[0], -p[1])


def P2(p):
    """Seconda proiezione di un punto 3D, in coordinate di disegno."""
    return (p[0], p[2])


def _lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(len(a)))


def tracce_retta(a, b):
    """Prima traccia (z=0) e seconda traccia (y=0) della retta per a e b: punti 3D o None."""
    t1 = t2 = None
    if b[2] != a[2]:
        t1 = _lerp(a, b, -a[2] / (b[2] - a[2]))
    if b[1] != a[1]:
        t2 = _lerp(a, b, -a[1] / (b[1] - a[1]))
    return t1, t2


def piano(a, b, c):
    """Piano per tre punti: (n, d) con n . X = d."""
    u = [b[i] - a[i] for i in range(3)]
    v = [c[i] - a[i] for i in range(3)]
    n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    return n, sum(n[i] * a[i] for i in range(3))


def tracce_piano(n, d, x1, x2):
    """Tracce del piano tra x1 e x2, in coordinate di disegno: (t1, t2), ognuna una coppia di punti o None.
    t1: intersezione con pi1 (z=0), disegnata sotto LT; t2: con pi2 (y=0), sopra LT."""
    t1 = t2 = None
    if n[1] != 0:  # z=0: n0 x + n1 y = d  ->  y = (d - n0 x)/n1, disegnata a -y
        t1 = tuple((x, -(d - n[0] * x) / n[1]) for x in (x1, x2))
    if n[2] != 0:  # y=0: n0 x + n2 z = d
        t2 = tuple((x, (d - n[0] * x) / n[2]) for x in (x1, x2))
    return t1, t2


# ---------- geometria nel piano del disegno ----------

def interseca(p1, p2, q1, q2):
    """Intersezione delle rette p1p2 e q1q2 (coordinate di disegno), o None se parallele."""
    d = (p2[0] - p1[0]) * (q2[1] - q1[1]) - (p2[1] - p1[1]) * (q2[0] - q1[0])
    if abs(d) < 1e-9:
        return None
    t = ((q1[0] - p1[0]) * (q2[1] - q1[1]) - (q1[1] - p1[1]) * (q2[0] - q1[0])) / d
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))


def su_lt(p, q):
    """Dove la retta pq incontra la linea di terra."""
    return interseca(p, q, (0, 0), (1, 0))


def direzione(p, q):
    l = math.hypot(q[0] - p[0], q[1] - p[1])
    return ((q[0] - p[0]) / l, (q[1] - p[1]) / l)


def perpendicolare(d):
    return (-d[1], d[0])


# ---------- disegno SVG ----------

class Figura:
    def __init__(self, larghezza, altezza, y_lt, titolo=None, x0=0):
        self.w, self.h, self.y_lt, self.x0 = larghezza, altezza, y_lt, x0
        self.parti = []
        self.titolo = titolo

    def _s(self, p):
        return (self.x0 + p[0], self.y_lt - p[1])

    def _linea(self, a, b, colore, spessore, tratteggio=None):
        (x1, y1), (x2, y2) = self._s(a), self._s(b)
        dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
        self.parti.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{COLORI.get(colore, colore)}" stroke-width="{spessore}"{dash} stroke-linecap="round"/>'
        )

    def lt(self, x1, x2, etichetta=True):
        self._linea((x1, 0), (x2, 0), "nero", 1.6)
        if etichetta:
            self.testo((x1, 0), "LT", dx=2, dy=-6, colore="nero")

    def traccia(self, a, b, colore="nero"):
        self._linea(a, b, colore, 2.4)

    def retta(self, a, b, colore="rosso", spessore=1.8):
        self._linea(a, b, colore, spessore)

    def costruzione(self, a, b):
        self._linea(a, b, "grigio", 1, "5,4")

    def richiamo(self, x, y1, y2):
        """Linea di richiamo verticale tra le due proiezioni di un punto."""
        self._linea((x, y1), (x, y2), "grigio", 0.9, "3,3")

    def figura(self, punti, colore="blu"):
        pts = " ".join("{:.1f},{:.1f}".format(*self._s(p)) for p in punti)
        c = COLORI.get(colore, colore)
        self.parti.append(f'<polygon points="{pts}" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-width="1.8"/>')

    def punto(self, p, etichetta=None, dx=6, dy=-6, colore="nero"):
        x, y = self._s(p)
        self.parti.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="{COLORI.get(colore, colore)}"/>')
        if etichetta:
            self.testo(p, etichetta, dx, dy, colore)

    def angolo_retto(self, vertice, d1, d2, lato=9):
        a = (vertice[0] + d1[0] * lato, vertice[1] + d1[1] * lato)
        c = (vertice[0] + d2[0] * lato, vertice[1] + d2[1] * lato)
        b = (a[0] + d2[0] * lato, a[1] + d2[1] * lato)
        self._linea(a, b, "nero", 1)
        self._linea(b, c, "nero", 1)

    def testo(self, p, etichetta, dx=6, dy=-6, colore="nero", dimensione=15, corsivo=True):
        x, y = self._s(p)
        stile = ' font-style="italic"' if corsivo else ""
        self.parti.append(
            f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-family="Helvetica, Arial, sans-serif" '
            f'font-size="{dimensione}" fill="{COLORI.get(colore, colore)}"{stile}>{_etichetta(etichetta)}</text>'
        )

    def nota(self, x, y, testo, dimensione=13):
        """Testo libero in coordinate SVG assolute (per titoli e didascalie)."""
        self.parti.append(
            f'<text x="{x}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="{dimensione}" '
            f'fill="#444">{_escape(testo)}</text>'
        )

    def svg(self):
        corpo = "\n".join(self.parti)
        titolo, fascia = "", 0
        if self.titolo:
            # il titolo sta in una fascia sopra il disegno, cosi' le linee non lo coprono
            fascia = 36
            titolo = (f'<text x="12" y="24" font-family="Helvetica, Arial, sans-serif" font-size="15" '
                      f'font-weight="bold" fill="#333">{_escape(self.titolo)}</text>')
        h = self.h + fascia
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {h}" '
            f'width="{self.w}" height="{h}">\n'
            f'<rect width="100%" height="100%" fill="#ffffff"/>\n{titolo}\n'
            f'<g transform="translate(0,{fascia})">\n{corpo}\n</g>\n</svg>\n'
        )

    def salva(self, percorso):
        with open(percorso, "w", encoding="utf-8") as f:
            f.write(self.svg())


def _escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _etichetta(s):
    """'T_{2o}″' -> testo SVG con pedice."""
    out = []
    for parte in re.split(r"(_\{[^}]*\}|_.)", s):
        if not parte:
            continue
        if parte.startswith("_"):
            sub = parte[2:-1] if parte.startswith("_{") else parte[1:]
            out.append(f'<tspan dy="4" font-size="70%">{_escape(sub)}</tspan><tspan dy="-4"></tspan>')
        else:
            out.append(_escape(parte))
    return "".join(out)
