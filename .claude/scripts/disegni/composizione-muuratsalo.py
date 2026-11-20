#!/usr/bin/env python3
"""Casa sperimentale di Aalto a Muuratsalo (esercizio 4 di composizione): pianta quotata,
altezze, schema di taglio del foglio di Poliplat 50 x 70 x 0,5 cm e passaggi di montaggio in 3D.

Uso: python3 -I composizione-muuratsalo.py
Coordinate in metri sulla casa (= cm sul plastico 1:100): x verso est dal filo esterno ovest,
y verso sud dal filo esterno nord, z dal pavimento. Le misure in pianta sono prese dalla
scala grafica della scheda (pianta misurata 14,25 m, riportata al 14,40 detto dal prof).
Sul plastico tutti i muri sono spessi 0,5 cm: il filo verso l'esterno e verso il patio resta
fermo, lo spessore in piu' va dentro le stanze.
"""
import math
import os

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/composizione-architettonica/bozze/img/"
T = 0.5
FONT = 'font-family="Helvetica, Arial, sans-serif"'
NERO, BLU, ROSSO, GRIGIO = "#1f1f1f", "#1f5fae", "#c62828", "#8a8a8a"


def num(v, dec=2):
    s = ("%.*f" % (dec, v)).rstrip("0").rstrip(".") if dec else "%d" % round(v)
    return s.replace(".", ",")


def h_tetto(x):
    """Quota dell'estradosso del tetto della fascia nord (sezione ovest-est)."""
    return 6.05 - 3.45 / 12.25 * x if x <= 12.25 else 2.60 + 0.65 / 2.15 * (x - 12.25)


def h_ala(x):
    """Estradosso del tetto dell'ala delle camere: da 3,35 sul patio a 2,60 a est."""
    return 3.35 - 0.75 / 4.95 * (x - 9.45)


# =====================================================================================
# I pezzi del plastico
# =====================================================================================
class Pezzo:
    """kind: 'x' muro lungo x (spessore verso +y da y0), 'y' muro lungo y (spessore verso +x da x0),
    'piano' lastra (poligono 3D della faccia di sotto, estrusa verso l'alto)."""

    def __init__(self, cod, nome, kind, passo, x0=0, y0=0, u0=0, forma=None, buchi=(), d3=None,
                 dim=None, nota=""):
        self.cod, self.nome, self.kind, self.passo = cod, nome, kind, passo
        self.x0, self.y0, self.u0 = x0, y0, u0
        self.forma = forma            # poligono (u, v) del pezzo piatto
        self.buchi = list(buchi)      # rettangoli (u1, v1, u2, v2) da togliere
        self.d3 = d3                  # per i piani: vertici 3D della faccia di sotto
        self.dim = dim                # (larghezza, altezza) del pezzo piatto, per i piani
        self.nota = nota

    def piatto(self):
        if self.forma:
            return self.forma
        w, h = self.dim
        return [(0, 0), (w, 0), (w, h), (0, h)]

    def bbox(self):
        p = self.piatto()
        return max(a for a, _ in p), max(b for _, b in p)

    def misura(self):
        w, h = self.bbox()
        return "%s × %s" % (num(w), num(h))


def rett(w, h):
    return [(0, 0), (w, 0), (w, h), (0, h)]


def muro_x(cod, nome, passo, x1, x2, y0, h, buchi=(), forma=None, nota=""):
    """Muro lungo x da x1 a x2; buchi in coordinate assolute (xa, za, xb, zb)."""
    b = [(a - x1, za, c - x1, zb) for a, za, c, zb in buchi]
    return Pezzo(cod, nome, "x", passo, x0=x1, y0=y0, forma=forma or rett(x2 - x1, h), buchi=b, nota=nota)


def muro_y(cod, nome, passo, y1, y2, x0, h, buchi=(), forma=None, nota=""):
    b = [(a - y1, za, c - y1, zb) for a, za, c, zb in buchi]
    return Pezzo(cod, nome, "y", passo, x0=x0, y0=y1, forma=forma or rett(y2 - y1, h), buchi=b, nota=nota)


def piano(cod, nome, passo, pts, dim, nota=""):
    return Pezzo(cod, nome, "piano", passo, d3=pts, dim=dim, nota=nota)


def pezzi():
    P = []
    # --- 1. base
    P.append(piano("M01", "Base del plastico", 1,
                   [(-1.8, -5.55, -T), (25.2, -5.55, -T), (25.2, 16.45, -T), (-1.8, 16.45, -T)], (27, 22),
                   "Misura libera: lascia circa 2 cm di bordo intorno a casa e annesso."))
    # --- 2. muri esterni della casa
    hN = lambda x: h_tetto(x) - T
    P.append(muro_x("M02", "Muro nord", 2, 0, 14.40, 0, 0,
                    forma=[(0, 0), (14.40, 0), (14.40, hN(14.40)), (12.25, hN(12.25)), (0, hN(0))],
                    buchi=[(2.35, 1.10, 3.30, 2.10), (5.25, 1.10, 6.20, 2.10), (9.85, 1.10, 11.50, 2.10),
                           (2.00, 3.30, 3.70, 4.40)],
                    nota="Il bordo in alto è inclinato: segue il tetto (giù fino a 12,25 cm, poi risale)."))
    P.append(muro_y("M03", "Muro ovest dell'atelier", 2, 0.5, 5.0, 0, hN(0),
                    buchi=[(0.75, 1.10, 2.60, 2.10)]))
    eN, eS = hN(14.40), 2.10
    P.append(muro_y("M04", "Muro est", 2, 0.5, 13.90, 13.90, 0,
                    forma=[(0, 0), (13.40, 0), (13.40, eS), (4.5, eS), (4.5, eN), (0, eN)],
                    buchi=[(1.55, 1.10, 2.50, 2.10), (3.60, 0, 4.70, 2.20), (6.30, 0.90, 7.25, 1.80),
                           (8.90, 0.90, 9.85, 1.80), (11.50, 0.90, 12.45, 1.80)],
                    nota="Il gradino in alto sta a 4,5 cm dal bordo nord: la parte alta va verso nord."))
    # --- 3. il recinto del patio
    P.append(muro_y("M05", "Recinto ovest", 3, 5.0, 13.90, 0, 6.05,
                    buchi=[(7.70, 0.60, 12.60, 2.20)], nota="La grande «finestra» sul lago."))
    P.append(muro_x("M06", "Recinto sud, pezzo ovest", 3, 0, 2.45, 13.90, 4.50))
    P.append(muro_x("M07", "Recinto sud, pezzo est", 3, 6.95, 9.45, 13.90, 4.50))
    # --- 4. l'ala delle camere
    P.append(muro_x("M08", "Muro sud delle camere", 4, 9.45, 14.40, 13.90, 0,
                    forma=[(0, 0), (4.95, 0), (4.95, 2.10), (0, 2.85)], buchi=[(9.95, 0.90, 10.85, 1.80)]))
    P.append(muro_y("M09", "Muro tra patio e corridoio", 4, 5.0, 13.90, 9.45, 2.85,
                    buchi=[(6.40, 0.45, 8.50, 2.10), (10.95, 0, 11.55, 2.20)]))
    # --- 5. il muro dell'atelier sul patio e il camino
    P.append(muro_x("M10", "Muro tra atelier e patio", 5, 0.5, 9.45, 4.5, 0,
                    forma=[(0, 0), (8.95, 0), (8.95, hN(9.45)), (0, hN(0.5))],
                    buchi=[(2.20, 0.50, 6.10, 2.10), (5.05, 0, 6.10, 0.50)],
                    nota="Il bordo in alto è inclinato come il tetto."))
    P.append(muro_y("M11", "Muro tra pranzo e cucina", 5, 0.5, 3.60, 9.45, 2.75))
    P.append(muro_y("M12", "Camino", 5, 1.95, 3.60, 8.95, 2.20))
    # --- 6. le pareti interne
    P.append(muro_x("M13", "Parete della cucina, pezzo ovest", 6, 9.95, 12.10, 3.35, 2.05))
    P.append(muro_x("M14", "Parete della cucina, pezzo est", 6, 12.90, 13.90, 3.35, 2.05))
    P.append(muro_x("M15", "Parete nord del bagno", 6, 11.55, 13.90, 4.70, 2.05))
    P.append(muro_x("M16", "Parete tra bagno e guardaroba", 6, 10.75, 13.90, 6.20, 2.10))
    P.append(muro_y("M17", "Corridoio, pezzo nord", 6, 7.30, 9.20, 10.75, 2.10))
    P.append(muro_y("M18", "Corridoio, pezzo sud", 6, 9.75, 10.95, 10.75, 2.10))
    P.append(muro_x("M19", "Parete tra le due camere", 6, 11.25, 13.90, 8.15, 2.10))
    P.append(muro_x("M20", "Parete della camera sud", 6, 10.75, 13.90, 10.95, 2.10))
    # --- 7. il soppalco
    P.append(piano("M21", "Soppalco dello studio", 7,
                   [(0.5, 0.5, 2.35), (3.70, 0.5, 2.35), (3.70, 4.5, 2.35), (0.5, 4.5, 2.35)], (3.20, 4.00),
                   "Il piano di sotto sta a 2,35 cm dal pavimento, quello di sopra a 2,85."))
    # --- 8. l'ingresso (in legno)
    P.append(muro_y("M22", "Ingresso, muro ovest", 8, -1.30, 0, 14.40, 2.60))
    P.append(muro_y("M23", "Ingresso, muro est", 8, 0.15, 3.60, 15.60, 2.60))
    P.append(muro_x("M24", "Ingresso, muro sud", 8, 14.40, 16.10, 4.70, 2.60))
    # --- 9. l'annesso degli ospiti (in legno)
    P.append(muro_x("M25", "Annesso, muro nord", 9, 16.10, 23.40, -3.50, 2.60, buchi=[(17.40, 1.00, 19.30, 1.90)]))
    P.append(muro_x("M26", "Annesso, muro sud", 9, 16.10, 23.40, -0.35, 2.60, buchi=[(18.60, 1.00, 19.40, 1.90)]))
    P.append(muro_y("M27", "Annesso, muro ovest", 9, -3.00, -1.30, 16.10, 2.60))
    P.append(muro_y("M28", "Annesso, muro est", 9, -3.00, -0.35, 22.90, 2.60))
    P.append(muro_y("M29", "Annesso, parete del bagno", 9, -3.00, -0.85, 17.15, 2.60))
    P.append(muro_y("M30", "Annesso, parete tra le camere", 9, -3.00, -0.85, 20.70, 2.60))
    P.append(muro_x("M31", "Annesso, parete sud del bagno", 9, 16.60, 17.15, -1.70, 2.60))
    # --- 10. i tetti
    la = math.hypot(12.25, 3.45)
    lb = math.hypot(2.15, 0.65)
    lw = math.hypot(4.95, 0.75)
    P.append(piano("M32", "Tetto grande (falda ovest)", 10,
                   [(0, 0, hN(0)), (12.25, 0, hN(12.25)), (12.25, 5.0, hN(12.25)), (0, 5.0, hN(0))],
                   (round(la, 2), 5.0), "Scende da ovest a est fino alla linea più bassa (a 12,25 cm)."))
    P.append(piano("M33", "Tetto piccolo (falda est)", 10,
                   [(12.25, 0, hN(12.25)), (14.40, 0, hN(14.40)), (14.40, 5.0, hN(14.40)), (12.25, 5.0, hN(12.25))],
                   (round(lb, 2), 5.0), "Risale verso est: con M32 fa la «farfalla» della sezione."))
    P.append(piano("M34", "Tetto dell'ala delle camere", 10,
                   [(9.45, 5.0, h_ala(9.45) - T), (14.40, 5.0, h_ala(14.40) - T),
                    (14.40, 14.40, h_ala(14.40) - T), (9.45, 14.40, h_ala(9.45) - T)],
                   (round(lw, 2), 9.40), "Scende verso est."))
    P.append(piano("M35", "Tetto dell'ingresso", 10,
                   [(14.40, -1.30, 2.60), (16.10, -1.30, 2.60), (16.10, 5.20, 2.60), (14.40, 5.20, 2.60)], (1.70, 6.50)))
    P.append(piano("M36", "Tetto dell'annesso", 10,
                   [(16.10, -3.50, 2.60), (23.40, -3.50, 2.60), (23.40, 0.15, 2.60), (16.10, 0.15, 2.60)], (7.30, 3.65)))
    P.append(muro_x("M37", "Comignolo", 10, 9.0, 9.60, 2.45, 0, forma=rett(0.60, 2.40),
                    nota="Va in piedi sul tetto grande, sopra il camino."))
    # il comignolo parte dal tetto: lo alzo in 3D
    P[-1].z0 = h_tetto(9.3)
    return P


# =====================================================================================
# Geometria 3D dei pezzi
# =====================================================================================
def facce(p):
    """Lista di (vertici 3D, buchi 3D, normale) di un pezzo."""
    z0 = getattr(p, "z0", 0.0)
    if p.kind == "piano":
        bot = [tuple(v) for v in p.d3]
        top = [(x, y, z + T) for x, y, z in bot]
        out = [(top, [], (0, 0, 1)), (bot[::-1], [], (0, 0, -1))]
        n = len(bot)
        for i in range(n):
            a, b = bot[i], bot[(i + 1) % n]
            q = [a, b, (b[0], b[1], b[2] + T), (a[0], a[1], a[2] + T)]
            nx, ny = b[1] - a[1], -(b[0] - a[0])
            l = math.hypot(nx, ny) or 1
            out.append((q, [], (nx / l, ny / l, 0)))
        return out
    if p.kind == "x":
        f = lambda u, v, s: (p.x0 + u, p.y0 + s, z0 + v)
        n1, n2 = (0, -1, 0), (0, 1, 0)
    else:
        f = lambda u, v, s: (p.x0 + s, p.y0 + u, z0 + v)
        n1, n2 = (-1, 0, 0), (1, 0, 0)
    forma = p.piatto()
    A = [f(u, v, 0) for u, v in forma]
    B = [f(u, v, T) for u, v in forma]
    hb = lambda s: [[f(u1, v1, s), f(u2, v1, s), f(u2, v2, s), f(u1, v2, s)] for u1, v1, u2, v2 in p.buchi]
    out = [(A, hb(0), n1), (B, hb(T), n2)]
    n = len(forma)
    for i in range(n):
        (u1, v1), (u2, v2) = forma[i], forma[(i + 1) % n]
        q = [f(u1, v1, 0), f(u2, v2, 0), f(u2, v2, T), f(u1, v1, T)]
        du, dv = u2 - u1, v2 - v1
        nu, nv = dv, -du                       # normale verso l'esterno del poligono (antiorario)
        l = math.hypot(nu, nv) or 1
        nu, nv = nu / l, nv / l
        if p.kind == "x":
            nn = (nu, 0, nv)
        else:
            nn = (0, nu, nv)
        out.append((q, [], nn))
    return out


# vista dall'alto, da sud-est
VIEW = (0.62, 0.95, 0.95)
_l = math.sqrt(sum(c * c for c in VIEW))
V = tuple(c / _l for c in VIEW)
R = (V[1], -V[0], 0)
_l = math.hypot(R[0], R[1])
R = (R[0] / _l, R[1] / _l, 0)
U = (R[1] * V[2] - R[2] * V[1], R[2] * V[0] - R[0] * V[2], R[0] * V[1] - R[1] * V[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def proj(p):
    return dot(p, R), -dot(p, U)


def vista3d(tutti, passo, titolo, path, scala=26):
    polys = []
    for p in tutti:
        if p.passo > passo:
            continue
        nuovo = p.passo == passo
        fs = facce(p)
        allv = [v for f in fs for v in f[0]]
        cen = [(min(v[i] for v in allv) + max(v[i] for v in allv)) / 2 for i in range(3)]
        # la base sempre per prima; poi un pezzo dopo l'altro, dal piu' lontano al piu' vicino
        kp = -1e9 if p.cod == "M01" else dot(cen, V)
        for verts, buchi, n in fs:
            if dot(n, V) <= 1e-6:
                continue
            c = [sum(v[i] for v in verts) / len(verts) for i in range(3)]
            luce = 0.55 + 0.45 * max(0, dot(n, (0.3, 0.5, 0.8)) / math.sqrt(0.98))
            polys.append(((kp, dot(c, V)), verts, buchi, nuovo, luce, p))
    polys.sort(key=lambda t: t[0])
    pts = [proj(v) for _, vs, _, _, _, _ in polys for v in vs]
    minx, maxx = min(a for a, _ in pts), max(a for a, _ in pts)
    miny, maxy = min(b for _, b in pts), max(b for _, b in pts)
    W, H = (maxx - minx) * scala + 60, (maxy - miny) * scala + 90
    tr = lambda q: ((q[0] - minx) * scala + 30, (q[1] - miny) * scala + 60)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="16" y="28" {FONT} font-size="17" font-weight="bold" fill="#333">{titolo}</text>']
    etich = {}
    for _, vs, buchi, nuovo, luce, p in polys:
        base = (232, 96, 96) if nuovo else (236, 236, 236)
        col = "rgb(%d,%d,%d)" % tuple(int(c * luce) for c in base)
        d = "M " + " L ".join("%.1f %.1f" % tr(proj(v)) for v in vs) + " Z"
        for b in buchi:
            d += " M " + " L ".join("%.1f %.1f" % tr(proj(v)) for v in b) + " Z"
        out.append(f'<path d="{d}" fill="{col}" fill-rule="evenodd" stroke="#555" stroke-width="0.7" stroke-linejoin="round"/>')
        if nuovo:
            etich.setdefault(p.cod, []).extend(tr(proj(v)) for v in vs)
    for cod, ps in etich.items():
        x = sum(a for a, _ in ps) / len(ps)
        y = sum(b for _, b in ps) / len(ps)
        out.append(f'<text x="{x:.0f}" y="{y + 4:.0f}" {FONT} font-size="13" font-weight="bold" fill="#7a0000" '
                   f'text-anchor="middle" stroke="#fff" stroke-width="3" paint-order="stroke">{cod}</text>')
    out.append(f'<text x="{W - 16:.0f}" y="28" {FONT} font-size="13" fill="#555" text-anchor="end">vista da sud-est</text>')
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))


# =====================================================================================
# Schema di taglio: il foglio 70 x 50 (MaxRects, il lato lungo dei pezzi in orizzontale)
# =====================================================================================
def impacca(lista, W=70.0, H=50.0, g=0.3):
    liberi = [(0.0, 0.0, W, H)]
    posti = []
    for p in sorted(lista, key=lambda q: -(q.bbox()[0] * q.bbox()[1])):
        w0, h0 = p.bbox()
        best = None
        for rot in (False, True):
            w, h = (h0, w0) if rot else (w0, h0)
            for (fx, fy, fw, fh) in liberi:
                if w + g <= fw + 1e-9 and h + g <= fh + 1e-9:
                    score = (fy, fx)          # in alto a sinistra: lascia libera la parte bassa del foglio
                    if best is None or score < best[0]:
                        best = (score, fx, fy, w, h, rot)
        if best is None:
            raise SystemExit("non entra: " + p.cod)
        _, x, y, w, h, rot = best
        posti.append((p, x, y, rot))
        r = (x, y, w + g, h + g)
        nuovi = []
        for f in liberi:
            fx, fy, fw, fh = f
            if r[0] >= fx + fw or r[0] + r[2] <= fx or r[1] >= fy + fh or r[1] + r[3] <= fy:
                nuovi.append(f)
                continue
            if r[0] > fx:
                nuovi.append((fx, fy, r[0] - fx, fh))
            if r[0] + r[2] < fx + fw:
                nuovi.append((r[0] + r[2], fy, fx + fw - r[0] - r[2], fh))
            if r[1] > fy:
                nuovi.append((fx, fy, fw, r[1] - fy))
            if r[1] + r[3] < fy + fh:
                nuovi.append((fx, r[1] + r[3], fw, fy + fh - r[1] - r[3]))
        liberi = [a for a in nuovi if not any(a != b and a[0] >= b[0] and a[1] >= b[1] and
                                              a[0] + a[2] <= b[0] + b[2] and a[1] + a[3] <= b[1] + b[3]
                                              for b in nuovi)]
    usato = max(y + (p.bbox()[0] if rot else p.bbox()[1]) for p, x, y, rot in posti)
    return posti, usato


def schema_taglio(P, path):
    posti, usato = impacca(P)
    s = 13.5
    W, H = 70 * s + 60, 50 * s + 150
    o = (30, 70)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="16" y="28" {FONT} font-size="17" font-weight="bold" fill="#333">Il foglio di Poliplat 70 × 50 cm: dove tagliare i pezzi</text>',
           f'<text x="16" y="50" {FONT} font-size="13" fill="#555">Misure in cm. Il rosa è il pezzo; le parti a righe si buttano, comprese quelle dentro i pezzi (finestre e porte).</text>',
           f'<rect x="{o[0]}" y="{o[1]}" width="{70 * s}" height="{50 * s}" fill="#fafafa" stroke="#333" stroke-width="1.5"/>']
    out.append('<defs><pattern id="righe" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               '<line x1="0" y1="0" x2="0" y2="6" stroke="#bbb" stroke-width="2"/></pattern></defs>')
    # parte libera per il secondo plastico
    out.append(f'<rect x="{o[0]}" y="{o[1] + usato * s + 4}" width="{70 * s}" height="{(50 - usato) * s - 4}" fill="#eef5ea" stroke="#7aa56a" stroke-dasharray="6,4"/>')
    out.append(f'<text x="{o[0] + 35 * s}" y="{o[1] + (usato + 50) / 2 * s + 6}" {FONT} font-size="16" fill="#4c7a3d" text-anchor="middle">'
               f'avanza una striscia di 70 × {num(50 - usato, 1)} cm: tienila per il plastico della tua nuova disposizione</text>')
    for p, x, y, rot in posti:
        w0, h0 = p.bbox()
        def T2(u, v):
            # v verso l'alto nel pezzo: nel foglio l'alto del pezzo e' verso l'alto
            if rot:
                return (o[0] + (x + v) * s, o[1] + (y + u) * s)
            return (o[0] + (x + u) * s, o[1] + (y + h0 - v) * s)
        bw, bh = (h0, w0) if rot else (w0, h0)
        out.append(f'<rect x="{o[0] + x * s:.1f}" y="{o[1] + y * s:.1f}" width="{bw * s:.1f}" height="{bh * s:.1f}" fill="url(#righe)" stroke="#999" stroke-width="0.6"/>')
        d = "M " + " L ".join("%.1f %.1f" % T2(u, v) for u, v in p.piatto()) + " Z"
        for u1, v1, u2, v2 in p.buchi:
            d += " M " + " L ".join("%.1f %.1f" % T2(u, v) for u, v in [(u1, v1), (u2, v1), (u2, v2), (u1, v2)]) + " Z"
        out.append(f'<path d="{d}" fill="#f6c9c9" fill-rule="evenodd" stroke="{ROSSO}" stroke-width="1.2"/>')
        cx, cy = o[0] + (x + bw / 2) * s, o[1] + (y + bh / 2) * s
        fs = 12 if min(bw, bh) * s > 26 else 9
        out.append(f'<text x="{cx:.0f}" y="{cy + 4:.0f}" {FONT} font-size="{fs}" font-weight="bold" fill="#7a0000" '
                   f'text-anchor="middle" stroke="#fff" stroke-width="2.5" paint-order="stroke">{p.cod}</text>')
    yb = o[1] + 50 * s + 30
    out.append(f'<text x="16" y="{yb}" {FONT} font-size="13" fill="#555">Lo schema è in scala: 1 cm del foglio vero è uguale per tutti i pezzi. Le misure esatte sono nella tabella. '
               f'Tra un pezzo e l\'altro ci sono 3 mm per la lama.</text>')
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))
    return posti, usato


# =====================================================================================
# Pianta quotata (la casa vera, in metri)
# =====================================================================================
class Disegno:
    def __init__(self, x0, y0, x1, y1, s, titolo):
        self.s, self.x0, self.y0 = s, x0, y0
        self.W, self.H = (x1 - x0) * s, (y1 - y0) * s + 40
        self.parti = [f'<rect width="100%" height="100%" fill="#ffffff"/>',
                      f'<text x="14" y="26" {FONT} font-size="17" font-weight="bold" fill="#333">{titolo}</text>']

    def P(self, x, y):
        return ((x - self.x0) * self.s, (y - self.y0) * self.s + 40)

    def rect(self, x1, y1, x2, y2, fill=NERO, stroke="none", sw=1, extra=""):
        a, b = self.P(x1, y1)
        c, d = self.P(x2, y2)
        self.parti.append(f'<rect x="{min(a, c):.1f}" y="{min(b, d):.1f}" width="{abs(c - a):.1f}" height="{abs(d - b):.1f}" '
                          f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')

    def line(self, x1, y1, x2, y2, col=NERO, sw=1, dash=None):
        a, b = self.P(x1, y1)
        c, d = self.P(x2, y2)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.parti.append(f'<line x1="{a:.1f}" y1="{b:.1f}" x2="{c:.1f}" y2="{d:.1f}" stroke="{col}" stroke-width="{sw}"{da}/>')

    def text(self, x, y, t, col=NERO, size=12, anchor="middle", rot=0, bold=False):
        a, b = self.P(x, y)
        r = f' transform="rotate({rot} {a:.1f} {b:.1f})"' if rot else ""
        w = ' font-weight="bold"' if bold else ""
        self.parti.append(f'<text x="{a:.1f}" y="{b:.1f}" {FONT} font-size="{size}" fill="{col}" text-anchor="{anchor}"{w}{r}>{t}</text>')

    def catena(self, pos, quote, asse, off, col=None, size=11):
        """Catena di quote: asse 'x' (orizzontale a y=off) o 'y' (verticale a x=off).
        quote: lista di (posizione, colore) ordinata."""
        for i in range(len(pos) - 1):
            a, b = pos[i], pos[i + 1]
            c = col[i] if col else NERO
            if asse == "x":
                self.line(a, off, b, off, GRIGIO, 0.8)
                self.text((a + b) / 2, off - 0.12, num(b - a), c, size)
            else:
                self.line(off, a, off, b, GRIGIO, 0.8)
                self.text(off - 0.12, (a + b) / 2, num(b - a), c, size, rot=-90)
        for a in pos:
            if asse == "x":
                self.line(a - 0.1, off + 0.1, a + 0.1, off - 0.1, NERO, 1.2)
                self.line(a, off - 0.25, a, off + 0.25, GRIGIO, 0.6)
            else:
                self.line(off - 0.1, a + 0.1, off + 0.1, a - 0.1, NERO, 1.2)
                self.line(off - 0.25, a, off + 0.25, a, GRIGIO, 0.6)

    def salva(self, path):
        with open(path, "w") as fh:
            fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W:.0f} {self.H:.0f}" '
                     f'width="{self.W:.0f}" height="{self.H:.0f}">\n' + "\n".join(self.parti) + "\n</svg>\n")


def muro(d, x1, y1, x2, y2, buchi=(), asse="x", fill=NERO):
    """Muro rettangolare con aperture (intervalli lungo l'asse del muro)."""
    if asse == "x":
        tagli = sorted(buchi)
        a = x1
        for b1, b2 in tagli:
            d.rect(a, y1, b1, y2, fill)
            d.line(b1, (y1 + y2) / 2, b2, (y1 + y2) / 2, "#777", 0.8)
            d.line(b1, y1, b2, y1, "#777", 0.6)
            d.line(b1, y2, b2, y2, "#777", 0.6)
            a = b2
        d.rect(a, y1, x2, y2, fill)
    else:
        a = y1
        for b1, b2 in sorted(buchi):
            d.rect(x1, a, x2, b1, fill)
            d.line((x1 + x2) / 2, b1, (x1 + x2) / 2, b2, "#777", 0.8)
            d.line(x1, b1, x1, b2, "#777", 0.6)
            d.line(x2, b1, x2, b2, "#777", 0.6)
            a = b2
        d.rect(x1, a, x2, y2, fill)


def pianta_quotata(path):
    d = Disegno(-2.6, -5.6, 25.0, 17.0, 46, "Pianta quotata della casa (misure in metri)")
    L = "#6d4c2f"     # legno
    # muri in muratura
    muro(d, 0, 0, 14.40, 0.35, [(2.35, 3.30), (5.25, 6.20), (9.85, 11.50)])
    muro(d, 0, 0.35, 0.40, 14.00, [(0.75, 2.60), (7.70, 12.60)], "y")
    muro(d, 14.10, 0.35, 14.40, 14.00, [(1.55, 2.50), (3.60, 4.70), (6.30, 7.25), (8.90, 9.85), (11.50, 12.45)], "y")
    muro(d, 0, 14.00, 14.40, 14.40, [(2.45, 6.95), (9.95, 10.85)])
    muro(d, 0.40, 4.70, 9.45, 5.00, [(2.20, 5.05), (5.05, 6.10)])
    muro(d, 9.45, 5.00, 9.75, 14.00, [(6.40, 8.50), (10.95, 11.55)], "y")
    muro(d, 9.45, 0.35, 9.75, 3.60, [], "y")
    d.rect(9.00, 1.95, 9.45, 3.60, "#444")
    # tramezzi (sottili)
    for x1, y1, x2, y2, b, a in [(9.75, 3.35, 14.10, 3.45, [(12.10, 12.90)], "x"),
                                 (11.55, 4.70, 14.10, 4.80, [], "x"),
                                 (11.55, 4.80, 11.65, 6.20, [(5.20, 6.00)], "y"),
                                 (10.75, 6.20, 14.10, 6.30, [], "x"),
                                 (10.75, 6.30, 10.85, 10.95, [(6.45, 7.05), (9.20, 9.75)], "y"),
                                 (10.85, 8.15, 14.10, 8.25, [], "x"),
                                 (10.75, 10.95, 14.10, 11.05, [], "x")]:
        muro(d, x1, y1, x2, y2, b, a, "#555")
    # soppalco e scala
    d.rect(0.40, 0.35, 3.70, 4.70, "none", BLU, 1.2, 'stroke-dasharray="6,4"')
    d.text(2.05, 1.30, "soppalco (studio)", BLU, 11)
    d.text(2.05, 1.75, "a +2,85", BLU, 11)
    for i in range(9):
        yy = 2.30 + i * 0.245
        d.line(0.40, yy, 1.00, yy, "#777", 0.6)
    d.rect(0.40, 2.30, 1.00, 4.50, "none", "#777", 0.8)
    # ingresso e annesso (legno)
    muro(d, 14.40, -1.30, 14.50, 0, [], "y", L)
    muro(d, 14.40, -1.30, 16.10, -1.20, [(14.60, 15.50), (15.50, 16.10)], "x", L)
    muro(d, 16.00, 0.15, 16.10, 4.70, [(3.60, 4.70)], "y", L)
    muro(d, 14.40, 4.70, 16.10, 4.80, [], "x", L)
    muro(d, 16.10, -3.50, 23.40, -3.40, [(17.40, 19.30)], "x", L)
    muro(d, 16.10, 0.05, 23.40, 0.15, [(18.60, 19.40)], "x", L)
    muro(d, 16.10, -3.40, 16.20, -1.30, [], "y", L)
    muro(d, 23.30, -3.40, 23.40, 0.05, [], "y", L)
    muro(d, 17.15, -3.40, 17.25, -0.85, [], "y", L)
    muro(d, 20.70, -3.40, 20.80, -0.85, [], "y", L)
    muro(d, 16.20, -1.70, 17.15, -1.60, [], "x", L)
    # nomi delle stanze
    for x, y, t in [(5.0, 2.6, "atelier e soggiorno"), (7.6, 1.6, "pranzo"), (11.6, 1.8, "cucina"),
                    (4.7, 9.3, "PATIO"), (12.3, 5.6, "bagno"), (12.0, 7.3, "guardaroba"),
                    (12.1, 9.6, "camera"), (11.9, 12.6, "camera"), (10.25, 8.8, "corr."),
                    (15.25, 2.0, "ingresso"), (16.65, -2.6, "wc"), (18.9, -1.9, "camera"), (22.0, -1.9, "camera"),
                    (19.7, -4.6, "ANNESSO DEGLI OSPITI (in legno)")]:
        d.text(x, y, t, "#333", 12 if t not in ("PATIO",) else 15, bold=t.isupper())
    d.text(15.25, -1.75, "entrata", "#333", 10)
    d.text(4.7, 14.85, "apertura del recinto", "#333", 11)
    d.text(-0.55, 10.15, "«finestra»", "#333", 11, rot=-90)
    # quote: lato nord (sopra)
    d.catena([0, 2.35, 3.30, 5.25, 6.20, 9.85, 11.50, 14.40], None, "x", -0.55,
             [BLU] * 7)
    d.catena([0, 14.40], None, "x", -1.25, [NERO])
    d.catena([14.40, 16.10, 23.40], None, "x", -4.15, [BLU, BLU])
    # lato sud (sotto)
    d.catena([0, 2.45, 6.95, 9.45, 9.95, 10.85, 14.40], None, "x", 15.45, [BLU] * 6)
    # lato ovest (a sinistra)
    d.catena([0, 0.75, 2.60, 4.70, 5.00, 7.70, 12.60, 14.40], None, "y", -1.25, [BLU] * 7)
    d.catena([0, 14.40], None, "y", -2.0, [NERO])
    # lato est (a destra)
    d.catena([0, 1.55, 2.50, 3.60, 4.70, 6.30, 7.25, 8.90, 9.85, 11.50, 12.45, 14.40], None, "y", 17.1, [BLU] * 11)
    d.catena([-3.50, -1.30, 0.15], None, "y", 24.2, [BLU, BLU])
    # quote interne
    d.catena([0.40, 9.45, 9.75, 10.75, 14.10], None, "x", 6.4, [BLU] * 4, 10)
    d.catena([0.35, 3.35, 4.70, 6.20, 8.15, 10.95, 14.00], None, "y", 13.75, [BLU] * 6, 10)
    d.text(7.2, 16.4, "Spessori: muri esterni circa 0,40 (prof), interni 0,30, tramezzi 0,10. Marrone: legno.", "#333", 12)
    # nord
    a, b = d.P(-1.9, -4.6)
    d.parti.append(f'<path d="M {a:.0f} {b - 16:.0f} L {a - 7:.0f} {b + 6:.0f} L {a:.0f} {b:.0f} L {a + 7:.0f} {b + 6:.0f} Z" fill="#333"/>')
    d.text(-1.9, -4.15, "N", "#333", 13, bold=True)
    d.salva(path)


# =====================================================================================
# Le altezze: due sezioni ovest-est
# =====================================================================================
def sezioni(path):
    s = 40
    W, H = 16.5 * s + 330, 2 * 7.6 * s + 120
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="14" y="26" {FONT} font-size="17" font-weight="bold" fill="#333">Le altezze: due sezioni da ovest (a sinistra) a est</text>']

    def blocco(oy, titolo, poligoni, quote, note):
        P = lambda x, z: (60 + x * s, oy - z * s)
        out.append(f'<text x="14" y="{oy - 7.0 * s:.0f}" {FONT} font-size="14" font-weight="bold" fill="#333">{titolo}</text>')
        a, b = P(-0.8, 0)
        c, _ = P(15.2, 0)
        out.append(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{b}" stroke="#333" stroke-width="1.5"/>')
        for pts, fill in poligoni:
            d = "M " + " L ".join("%.1f %.1f" % P(*q) for q in pts) + " Z"
            out.append(f'<path d="{d}" fill="{fill}" stroke="#333" stroke-width="1"/>')
        for x, z, t, col in quote:
            a, b = P(x, z)
            out.append(f'<line x1="{a - 5}" y1="{b}" x2="{a + 5}" y2="{b}" stroke="{col}" stroke-width="1.2"/>')
            out.append(f'<text x="{a + 7}" y="{b + 4}" {FONT} font-size="12" fill="{col}">{t}</text>')
        for i, t in enumerate(note):
            out.append(f'<text x="{60 + 15.6 * s}" y="{oy - 6.2 * s + i * 17:.0f}" {FONT} font-size="12" fill="#444">{t}</text>')

    # 1. fascia nord (atelier, pranzo, cucina): il tetto a farfalla
    prof = [(x, h_tetto(x)) for x in (0, 12.25, 14.40)]
    tetto = [(0, 6.05), (12.25, 2.60), (14.40, 3.25), (14.40, 2.75), (12.25, 2.10), (0, 5.55)]
    blocco(7.3 * s + 50, "1. Fascia nord: atelier, pranzo, cucina (sezione ovest-est della scheda)",
           [([(0, 0), (0.40, 0), (0.40, 5.55), (0, 5.55)], "#555"),
            ([(14.10, 0), (14.40, 0), (14.40, 2.75), (14.10, 2.75)], "#555"),
            ([(9.45, 0), (9.75, 0), (9.75, 2.75), (9.45, 2.75)], "#999"),
            (tetto, "#bbb"),
            ([(0.40, 2.35), (3.70, 2.35), (3.70, 2.85), (0.40, 2.85)], "#9cc0e8")],
           [(0, 6.05, "+6,05", NERO), (12.25, 2.60, "+2,60 (punto più basso, a 12,25)", BLU), (14.40, 3.25, "+3,25", NERO),
            (3.70, 2.85, "+2,85 soppalco", NERO), (0.40, 0, "±0,00 pavimento", NERO)],
           ["Il tetto è a «farfalla»:", "scende da ovest a est fino", "a 12,25 m e poi risale.", "Lo spessore del tetto è 0,50", "(il Poliplat)."])
    # 2. ala delle camere e recinto ovest
    blocco(2 * 7.3 * s + 90, "2. Patio e ala delle camere (sezione sul patio della scheda)",
           [([(0, 0), (0.40, 0), (0.40, 6.05), (0, 6.05)], "#555"),
            ([(9.45, 0), (9.75, 0), (9.75, 2.85), (9.45, 2.85)], "#555"),
            ([(14.10, 0), (14.40, 0), (14.40, 2.10), (14.10, 2.10)], "#555"),
            ([(9.45, 2.85), (14.40, 2.10), (14.40, 2.60), (9.45, 3.35)], "#bbb")],
           [(0, 6.05, "+6,05 recinto ovest", BLU), (9.45, 3.35, "+3,35", BLU), (14.40, 2.60, "+2,60", BLU),
            (14.40, 2.10, "+2,10", BLU), (9.75, 2.85, "+2,85", BLU)],
           ["Il recinto sud (con la grande", "apertura) non si vede nelle", "sezioni: l'ho fatto alto 4,50", "(ipotesi da chiedere al prof).",
            "Le camere hanno il tetto che", "scende verso est."])
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))


# =====================================================================================
def main():
    P = pezzi()
    # controllo: nessun pezzo piu' grande del foglio, e ogni muro ha i buchi dentro la sagoma
    for p in P:
        w, h = p.bbox()
        assert w <= 70 and h <= 50, p.cod
        for u1, v1, u2, v2 in p.buchi:
            assert 0 <= u1 < u2 <= w and 0 <= v1 < v2 <= h, (p.cod, u1, v1, u2, v2)
    pianta_quotata(OUT + "muuratsalo-1-pianta-quotata.svg")
    sezioni(OUT + "muuratsalo-2-altezze.svg")
    posti, usato = schema_taglio(P, OUT + "muuratsalo-3-taglio-foglio.svg")
    titoli = {1: "Passo 1: la base", 2: "Passo 2: i muri esterni nord, ovest ed est", 3: "Passo 3: il recinto del patio",
              4: "Passo 4: l'ala delle camere", 5: "Passo 5: il muro dell'atelier sul patio e il camino",
              6: "Passo 6: le pareti interne", 7: "Passo 7: il soppalco", 8: "Passo 8: l'ingresso",
              9: "Passo 9: l'annesso degli ospiti", 10: "Passo 10: i tetti e il comignolo"}
    for k, t in titoli.items():
        vista3d(P, k, t, OUT + "muuratsalo-passo-%02d.svg" % k)
    # tabella per la pagina
    for p in P:
        print("| %s | %s | %s | %s |" % (p.cod, p.nome, p.misura(), p.passo))
    print("usato in altezza:", round(usato, 2))
    for p, x, y, rot in posti:
        print(p.cod, round(x, 2), round(y, 2), "ruotato" if rot else "")


if __name__ == "__main__":
    main()
