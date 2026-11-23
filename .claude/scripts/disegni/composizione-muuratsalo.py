#!/usr/bin/env python3
"""Casa sperimentale di Aalto a Muuratsalo (esercizio 4 di composizione): pianta quotata,
altezze, schema di taglio del foglio di Poliplat 50 x 70 x 0,5 cm e passaggi di montaggio in 3D.

Uso: python3 -I composizione-muuratsalo.py (con numpy e PIL, per esempio il python di
~/Library/Application Support/sbobine-whisper/.venv, i passi del montaggio escono in PNG)
Coordinate in metri sulla casa (= cm sul plastico 1:100): x verso est dal filo esterno ovest,
y verso sud dal filo esterno nord, z dal pavimento. Le misure in pianta sono prese dalla
scala grafica della scheda (pianta misurata 14,25 m, riportata al 14,40 detto dal prof).
Sul plastico tutti i muri sono spessi 0,5 cm: il filo verso l'esterno e verso il patio resta
fermo, lo spessore in piu' va dentro le stanze.
"""
import math
import os

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/composizione-architettonica/bozze/img/"
# Obsidian non ricarica un SVG rifatto con lo stesso nome: a ogni modifica si cambia la versione
VER = "v14"
T = 0.5
FONT = 'font-family="Helvetica, Arial, sans-serif"'
NERO, BLU, ROSSO, GRIGIO = "#1f1f1f", "#1f5fae", "#c62828", "#8a8a8a"


def num(v, dec=2):
    s = ("%.*f" % (dec, v)).rstrip("0").rstrip(".") if dec else "%d" % round(v)
    return s.replace(".", ",")


def h_tetto(x):
    """Quota dell'estradosso del tetto della fascia nord (sezione ovest-est)."""
    return 6.05 - 3.45 / 12.25 * x if x <= 12.25 else 2.60 + 0.65 / 2.15 * (x - 12.25)


HRECINTO = h_tetto(0.5) - T     # recinto ovest e sud-ovest alti come M02 nell'angolo (5,41): niente gradino con il muro nord


def h_ala(x):
    """Estradosso del tetto dell'ala delle camere: sta sullo stesso piano del tetto della fascia
    nord (scende fino a 2,60 a 12,25 e poi risale a 3,25 sul filo est), cosi' M32 e M33 coprono
    tutte e due le ali con un pezzo solo ciascuno (scelta di Nadia). Sul patio viene 3,39 (la foto
    del patio dava circa 3,50: siamo dentro il margine della stima)."""
    return h_tetto(x)


H4 = h_tetto(13.90)


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


def tacche(p):
    """Le porte (buchi che partono dal pavimento) diventano tacche nel contorno del pezzo:
    cosi' il pezzo resta un poligono semplice, senza buchi aperti sul bordo."""
    porte = sorted(b for b in p.buchi if b[1] <= 1e-9)
    p.porte = porte
    if not porte:
        return p
    p.buchi = [b for b in p.buchi if b[1] > 1e-9]
    f = list(p.forma)
    assert f[0] == (0, 0) and f[1][1] == 0, p.cod
    L = f[1][0]
    fondo = []
    for k, (u1, v1, u2, v2) in enumerate(porte):
        if u1 <= 1e-9:
            fondo += [(0, v2), (u2, v2), (u2, 0)]
        elif u2 >= L - 1e-9:
            fondo += [(u1, 0), (u1, v2), (L, v2)]
        else:
            fondo += [(u1, 0), (u1, v2), (u2, v2), (u2, 0)]
    if porte[0][0] > 1e-9:
        fondo = [(0, 0)] + fondo
    if porte[-1][2] < L - 1e-9:
        fondo = fondo + [(L, 0)]
    p.forma = fondo + f[2:]
    return p


def muro_x(cod, nome, passo, x1, x2, y0, h, buchi=(), forma=None, nota="", poliplat=True):
    """Muro lungo x da x1 a x2; buchi in coordinate assolute (xa, za, xb, zb)."""
    b = [(a - x1, za, c - x1, zb) for a, za, c, zb in buchi]
    p = Pezzo(cod, nome, "x", passo, x0=x1, y0=y0, forma=forma or rett(x2 - x1, h), buchi=b, nota=nota)
    p.poliplat = poliplat
    return tacche(p)


def muro_y(cod, nome, passo, y1, y2, x0, h, buchi=(), forma=None, nota="", poliplat=True):
    b = [(a - y1, za, c - y1, zb) for a, za, c, zb in buchi]
    p = Pezzo(cod, nome, "y", passo, x0=x0, y0=y1, forma=forma or rett(y2 - y1, h), buchi=b, nota=nota)
    p.poliplat = poliplat
    if not poliplat:
        p.t = 0.15
    return tacche(p)


def piano(cod, nome, passo, pts, dim, nota=""):
    return Pezzo(cod, nome, "piano", passo, d3=pts, dim=dim, nota=nota)


def pezzi():
    P = []
    # --- 1. base
    P.append(piano("M01", "Base del plastico", 1,
                   [(-0.8, -4.55, -T), (24.2, -4.55, -T), (24.2, 15.45, -T), (-0.8, 15.45, -T)], (25, 20),
                   "Misura libera: lascia circa 1 cm di bordo intorno a casa e annesso."))
    # --- 2. muri esterni della casa
    hN = lambda x: h_tetto(x) - T
    P.append(muro_x("M02", "Muro nord", 2, 0.5, 13.90, 0, 0,
                    forma=[(0, 0), (13.40, 0), (13.40, hN(13.90)), (11.75, hN(12.25)), (0, hN(0.5))],
                    buchi=[(2.35, 1.10, 3.30, 2.10), (5.25, 1.10, 6.20, 2.10), (9.85, 1.10, 11.50, 2.10),
                           (2.00, 3.30, 3.70, 4.40)],
                    nota="Il bordo in alto è inclinato: segue il tetto (giù fino a 12,25 cm, poi risale)."))
    eN = hN(14.40)
    # M03 e M04 sono i due muri lunghi, da angolo ad angolo; M02, M06 e M07 si fermano contro di loro
    P.append(muro_y("M04", "Muro est", 2, 0, 14.40, 13.90, 0,
                    forma=rett(14.40, H4),
                    buchi=[(1.55, 1.10, 2.50, 2.10), (3.60, 0, 4.70, 2.20), (6.30, 0.90, 7.25, 1.80),
                           (8.90, 0.90, 9.85, 1.80), (11.50, 0.90, 12.45, 1.80)],
                    nota="Da angolo ad angolo, alto 3,1 (come il tetto a 13,9 cm dal bordo ovest): M02, M07 e i tetti finiscono contro la sua faccia interna."))
    # --- 3. il recinto del patio
    # Altezze del recinto ricavate dalla foto del patio verso il lago (apertura larga 4,5 m come
    # riferimento) e dalla sezione sul patio della scheda: sono stime, con un margine di 20-30 cm.
    HR, PAR = HRECINTO, 1.80
    # muro ovest dell'atelier e recinto ovest: un pezzo solo, dall'angolo nord-ovest all'angolo sud-ovest,
    # tutto alla stessa altezza di M02 nell'angolo (scelta di Nadia: niente gradino)
    P.append(muro_y("M03", "Muro ovest, atelier e recinto (un pezzo, tacca del muretto)", 2, 0, 14.40, 0, HR,
                    forma=[(0, 0), (14.40, 0), (14.40, HR), (12.60, HR), (12.60, PAR), (7.70, PAR), (7.70, HR), (0, HR)],
                    buchi=[(0.75, 1.10, 2.60, 2.10)],
                    nota="Un pezzo solo dall'angolo nord-ovest all'angolo sud-ovest: la tacca in alto è il muretto del graticcio."))
    P.append(muro_x("M06", "Recinto sud, pezzo ovest", 3, 0.5, 2.45, 13.90, 0,
                    forma=[(0, 0), (1.95, 0), (1.95, 4.38), (0, HR)],
                    nota="Inclinato: alto 5,41 contro M03, 4,38 verso l'apertura."))
    # recinto sud a est dell'apertura e muro sud delle camere: un pezzo solo (scelta di Nadia)
    P.append(muro_x("M07", "Recinto sud est e muro sud delle camere (un pezzo)", 3, 6.95, 13.90, 13.90, 0,
                    forma=[(0, 0), (6.95, 0), (6.95, H4), (5.30, h_ala(12.25)), (2.50, h_ala(9.45)), (0, 4.25)],
                    buchi=[(9.95, 0.90, 10.85, 1.80)],
                    nota="Un pezzo solo dall'apertura fino a M04: scende da 4,25 a 3,39 (recinto), poi segue il tetto delle camere."))
    # il graticcio di legno bianco sopra il muretto di M03: montanti ogni 0,6 e due traversi.
    # Non e' di Poliplat (sarebbe troppo spesso): stuzzicadenti o listelli di balsa da 2 mm.
    for k in range(8):
        y = 7.70 + 0.6 * (k + 1) - 0.05
        g = muro_y("G01", "Graticcio, montanti (8 stuzzicadenti)", 3, y, y + 0.15, 0.17, HR - PAR, poliplat=False)
        g.z0 = PAR
        P.append(g)
    for zt in (2.60, HR - 0.70):
        g = muro_y("G02", "Graticcio, traversi (2 stuzzicadenti)", 3, 7.70, 12.60, 0.02, 0.15, poliplat=False)
        g.z0 = zt
        P.append(g)
    # --- 4. l'ala delle camere
    P.append(muro_y("M09", "Muro tra patio e corridoio", 4, 5.0, 13.90, 9.45, h_ala(9.45) - T,
                    buchi=[(6.40, 0.45, 8.50, 2.10), (10.95, 0, 11.55, 2.20)]))
    # --- 5. il muro dell'atelier sul patio e il camino
    P.append(muro_x("M10", "Muro tra atelier e patio", 5, 0.5, 9.95, 4.5, 0,
                    # finestra lunga e portafinestra insieme: un'unica tacca dal pavimento
                    forma=[(0, 0), (4.55, 0), (4.55, 0.50), (1.70, 0.50), (1.70, 2.10), (5.60, 2.10), (5.60, 0),
                           (9.45, 0), (9.45, hN(9.95)), (0, hN(0.5))],
                    nota="Il bordo in alto è inclinato come il tetto."))
    P.append(muro_y("M11", "Muro tra pranzo e cucina", 5, 0.5, 3.60, 9.45, 2.75))
    # --- 6. le pareti interne
    # i tramezzi arrivano sotto il tetto (bordo alto inclinato come il tetto); le porte sono buchi
    # alti 2,1 dentro un muro unico (scelta di Nadia)
    def sotto_nord(x1, x2):
        pts = [(0, 0), (x2 - x1, 0), (x2 - x1, hN(x2))]
        if x1 < 12.25 < x2:
            pts.append((12.25 - x1, hN(12.25)))
        return pts + [(0, hN(x1))]

    def sotto_ala(x1, x2):
        pts = [(0, 0), (x2 - x1, 0), (x2 - x1, h_ala(x2) - T)]
        if x1 < 12.25 < x2:
            pts.append((12.25 - x1, h_ala(12.25) - T))
        return pts + [(0, h_ala(x1) - T)]
    PD = 2.10
    P.append(muro_x("M13", "Parete sud della cucina (porta)", 6, 9.95, 13.90, 3.35, 0, forma=sotto_nord(9.95, 13.90),
                    buchi=[(12.10, 0, 12.90, 1.90)]))
    P.append(muro_x("M15", "Parete nord del bagno", 6, 11.55, 13.90, 4.70, 0, forma=sotto_nord(11.55, 13.90)))
    # la parete ovest del bagno: e' quasi tutta porta (la porta, alta 1,9 sotto il tetto basso, e
    # un pezzetto di muro di 2 mm verso sud)
    P.append(muro_y("M39", "Parete ovest del bagno (porta)", 6, 5.20, 6.20, 11.55, h_ala(12.05) - T,
                    buchi=[(5.20, 0, 6.00, 1.90)]))
    P.append(muro_x("M16", "Parete tra bagno e guardaroba", 6, 10.75, 13.90, 6.20, 0, forma=sotto_ala(10.75, 13.90)))
    P.append(muro_y("M17", "Parete del corridoio (porte del guardaroba e della camera)", 6, 6.70, 10.95, 10.75,
                    h_ala(11.25) - T, buchi=[(6.70, 0, 7.30, PD), (9.20, 0, 9.75, PD)]))
    P.append(muro_x("M19", "Parete tra le due camere", 6, 11.25, 13.90, 8.15, 0, forma=sotto_ala(11.25, 13.90)))
    P.append(muro_x("M20", "Parete della camera sud", 6, 10.75, 13.90, 10.95, 0, forma=sotto_ala(10.75, 13.90)))
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
    lb = math.hypot(1.65, 0.65 * 1.65 / 2.15)
    lw = math.hypot(2.80, 0.90)
    # un pezzo per falda, che copre la fascia nord e l'ala delle camere (scelta di Nadia)
    ka = la / 12.25                       # allungamento lungo la falda che scende
    m32 = piano("M32", "Tetto, falda che scende (fascia nord e camere, a L)", 10,
                [(0.5, 0, hN(0.5)), (12.25, 0, hN(12.25)), (12.25, 13.90, hN(12.25)), (9.45, 13.90, hN(9.45)),
                 (9.45, 5.0, hN(9.45)), (0.5, 5.0, hN(0.5))], (round(11.75 * ka, 2), 13.90),
                "Un pezzo a L: scende da ovest a est fino alla linea più bassa (a 12,25 cm); il braccio lungo copre le camere.")
    m32.forma = [(0, 0), (round(11.75 * ka, 3), 0), (round(11.75 * ka, 3), 13.90), (round(8.95 * ka, 3), 13.90),
                 (round(8.95 * ka, 3), 5.0), (0, 5.0)]
    P.append(m32)
    P.append(piano("M33", "Tetto, falda che risale (fascia nord e camere)", 10,
                   [(12.25, 0, hN(12.25)), (13.90, 0, hN(13.90)), (13.90, 13.90, hN(13.90)), (12.25, 13.90, hN(12.25))],
                   (round(lb, 2), 13.90), "Risale verso est per tutta la lunghezza della casa: con M32 fa la «farfalla»."))
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
    t = getattr(p, "t", T)
    B = [f(u, v, t) for u, v in forma]
    hb = lambda s: [[f(u1, v1, s), f(u2, v1, s), f(u2, v2, s), f(u1, v2, s)] for u1, v1, u2, v2 in p.buchi]
    out = [(A, hb(0), n1), (B, hb(t), n2)]
    n = len(forma)
    for i in range(n):
        (u1, v1), (u2, v2) = forma[i], forma[(i + 1) % n]
        q = [f(u1, v1, 0), f(u2, v2, 0), f(u2, v2, t), f(u1, v1, t)]
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
        # prima la base, poi muri e soppalco, poi i tetti (che stanno sopra), per ultimo il comignolo
        strato = 0 if p.cod == "M01" else 3 if p.cod == "M37" else 2 if p.passo == 10 else 1
        kp = (strato, dot(cen, V))
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


def vista3d_png(tutti, passo, titolo, path, scala=52, ss=2):
    """Come vista3d, ma disegnata con lo z-buffer (numpy + PIL): ogni pixel mostra la faccia piu'
    vicina, quindi i pezzi non si sovrappongono mai nel modo sbagliato. Esce un PNG leggero."""
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    facc = []
    for p in tutti:
        if p.passo > passo:
            continue
        for verts, buchi, n in facce(p):
            if dot(n, V) <= 1e-6:
                continue
            luce = 0.55 + 0.45 * max(0, dot(n, (0.3, 0.5, 0.8)) / math.sqrt(0.98))
            facc.append((verts, buchi, n, p.passo == passo, luce, p.cod))
    pts = [proj(v) for f in facc for v in f[0]]
    minx, maxx = min(a for a, _ in pts), max(a for a, _ in pts)
    miny, maxy = min(b for _, b in pts), max(b for _, b in pts)
    k = scala * ss
    ox, oy = 30 * ss, 90 * ss
    W, H = int((maxx - minx) * k + 60 * ss), int((maxy - miny) * k + 120 * ss)
    tr = lambda q: ((q[0] - minx) * k + ox, (q[1] - miny) * k + oy)
    zbuf = np.full((H, W), -1e9)
    ids = np.full((H, W), -1, dtype=np.int32)
    col = np.full((H, W, 3), 255, dtype=np.uint8)
    yy, xx = np.mgrid[0:H, 0:W]
    for i, (verts, buchi, n, nuovo, luce, cod) in enumerate(facc):
        poly = [tr(proj(v)) for v in verts]
        x0, x1 = int(max(0, min(a for a, _ in poly))), int(min(W - 1, max(a for a, _ in poly) + 1))
        y0, y1 = int(max(0, min(b for _, b in poly))), int(min(H - 1, max(b for _, b in poly) + 1))
        if x1 <= x0 or y1 <= y0:
            continue
        m = Image.new("L", (x1 - x0 + 1, y1 - y0 + 1), 0)
        d = ImageDraw.Draw(m)
        d.polygon([(a - x0, b - y0) for a, b in poly], fill=1)
        for b in buchi:
            d.polygon([(a - x0, c - y0) for a, c in (tr(proj(v)) for v in b)], fill=0)
        mask = np.array(m, dtype=bool)
        # profondita' del piano della faccia in ogni pixel: p = X R - Y U + t V
        X = (xx[y0:y1 + 1, x0:x1 + 1] - ox) / k + minx
        Y = (yy[y0:y1 + 1, x0:x1 + 1] - oy) / k + miny
        # normale vera del piano della faccia (metodo di Newell): i tetti sono inclinati
        nx = sum((verts[j][1] - verts[(j + 1) % len(verts)][1]) * (verts[j][2] + verts[(j + 1) % len(verts)][2]) for j in range(len(verts)))
        ny = sum((verts[j][2] - verts[(j + 1) % len(verts)][2]) * (verts[j][0] + verts[(j + 1) % len(verts)][0]) for j in range(len(verts)))
        nz = sum((verts[j][0] - verts[(j + 1) % len(verts)][0]) * (verts[j][1] + verts[(j + 1) % len(verts)][1]) for j in range(len(verts)))
        nv = (nx, ny, nz)
        if abs(dot(nv, V)) < 1e-9:
            continue
        c = dot(nv, verts[0])
        t = (c - X * dot(nv, R) + Y * dot(nv, U)) / dot(nv, V)
        zb = zbuf[y0:y1 + 1, x0:x1 + 1]
        ok = mask & (t > zb + 1e-4)
        zb[ok] = t[ok]
        ids[y0:y1 + 1, x0:x1 + 1][ok] = i
        base = (232, 96, 96) if nuovo else (236, 236, 236)
        col[y0:y1 + 1, x0:x1 + 1][ok] = [int(cc * luce) for cc in base]
    # contorni dove cambia la faccia
    e = np.zeros((H, W), dtype=bool)
    e[:, 1:] |= ids[:, 1:] != ids[:, :-1]
    e[1:, :] |= ids[1:, :] != ids[:-1, :]
    e2 = e.copy()
    e2[:, 1:] |= e[:, :-1]
    e2[1:, :] |= e[:-1, :]
    col[e2] = (85, 85, 85)
    im = Image.fromarray(col).resize((W // ss, H // ss), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    try:
        fb = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30, index=1)
        fn = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        fl = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22, index=1)
    except OSError:
        fb = fn = fl = ImageFont.load_default()
    d.text((20, 18), titolo, fill=(51, 51, 51), font=fb)
    d.text((im.width - 20, 24), "vista da sud-est", fill=(85, 85, 85), font=fn, anchor="ra")
    # etichette dei pezzi nuovi, al centro della parte che si vede
    for cod in sorted({f[5] for f in facc if f[3]}):
        sel = np.isin(ids, [i for i, f in enumerate(facc) if f[5] == cod])
        if not sel.any():
            continue
        ys, xs = np.nonzero(sel)
        cx, cy = xs.mean() / ss, ys.mean() / ss
        d.text((cx, cy), cod, fill=(122, 0, 0), font=fl, anchor="mm", stroke_width=3, stroke_fill=(255, 255, 255))
    im.save(path, optimize=True)


# =====================================================================================
# Schema di taglio: il foglio 70 x 50 (MaxRects, il lato lungo dei pezzi in orizzontale)
# =====================================================================================
def _maxrects(items, W, H, regola, liberi=None):
    """Mette i rettangoli (p, w, h) nel riquadro W x H senza spazi tra loro. Ruota se serve."""
    liberi = list(liberi) if liberi else [(0.0, 0.0, W, H)]
    posti = []
    e = 1e-9
    for p, w0, h0 in items:
        best = None
        for rot in (False, True):
            w, h = (h0, w0) if rot else (w0, h0)
            for (fx, fy, fw, fh) in liberi:
                if w <= fw + e and h <= fh + e:
                    if regola == "sinistra":
                        sc = (fx + w, fy)
                    elif regola == "lato":
                        sc = (min(fw - w, fh - h), max(fw - w, fh - h))
                    elif regola == "area":
                        sc = (fw * fh - w * h, min(fw - w, fh - h))
                    else:   # contatto: quanto bordo tocca gli altri pezzi o il riquadro
                        c = 0.0
                        if abs(fx) < e or abs(fx + w - W) < e:
                            c += h
                        if abs(fy) < e or abs(fy + h - H) < e:
                            c += w
                        for q, qx, qy, qw, qh in posti:
                            if abs(qx + qw - fx) < e or abs(fx + w - qx) < e:
                                c += max(0, min(fy + h, qy + qh) - max(fy, qy))
                            if abs(qy + qh - fy) < e or abs(fy + h - qy) < e:
                                c += max(0, min(fx + w, qx + qw) - max(fx, qx))
                        sc = (-c, fx)
                    if best is None or sc < best[0]:
                        best = (sc, fx, fy, w, h, rot)
        if best is None:
            return None
        _, x, y, w, h, rot = best
        posti.append((p, x, y, w, h))
        nuovi = []
        for f in liberi:
            fx, fy, fw, fh = f
            if x >= fx + fw - e or x + w <= fx + e or y >= fy + fh - e or y + h <= fy + e:
                nuovi.append(f)
                continue
            if x > fx + e:
                nuovi.append((fx, fy, x - fx, fh))
            if x + w < fx + fw - e:
                nuovi.append((x + w, fy, fx + fw - x - w, fh))
            if y > fy + e:
                nuovi.append((fx, fy, fw, y - fy))
            if y + h < fy + fh - e:
                nuovi.append((fx, y + h, fw, fy + fh - y - h))
        liberi = [a for a in nuovi if not any(a != b and a[0] >= b[0] - e and a[1] >= b[1] - e and
                                              a[0] + a[2] <= b[0] + b[2] + e and a[1] + a[3] <= b[1] + b[3] + e
                                              for b in nuovi)]
    return posti


def coppia_inclinata(P):
    """M02 e M10 hanno il bordo in alto con la stessa pendenza (quella del tetto): capovolgendo M10
    si incastra contro M02 e il taglio inclinato e' uno solo. Restituisce l'altezza del blocco e
    le due trasformazioni dal pezzo al blocco (U lungo 14,4, V verso l'alto)."""
    m02 = [p for p in P if p.cod == "M02"][0]
    m10 = [p for p in P if p.cod == "M10"][0]
    xe = 12.25                                       # M10 finisce dove M02 smette di scendere
    top02 = lambda u: h_tetto(u) - T
    alt10 = lambda u: h_tetto(0.5 + u) - T           # altezza di M10 al punto u (da ovest)
    H = top02(xe) + alt10(0)
    for u in (3.5, 6.0, 9.0, 12.0):                  # controllo: i due bordi combaciano
        assert abs(top02(u) + alt10(xe - u) - H) < 1e-9
    return m02, m10, H, (lambda u, v: (u, v)), (lambda u, v: (xe - u, H - v))


def _skyline(items, H):
    """Appoggia i pezzi uno alla volta contro la base (a sinistra) e contro quelli gia' messi.
    Il profilo (skyline) dice, per ogni tratto di altezza y, fin dove arriva la fila di pezzi.
    Ogni pezzo va dove lascia meno vuoto dietro di se'. items: (p, w, h, girabile).
    Restituisce (vuoti, larghezza, posti) oppure None."""
    sky = [[0.0, H, 0.0]]            # tratti [y1, y2, x]
    posti = []
    vuoto = 0.0
    e = 1e-9
    for p, w0, h0, gira in items:
        best = None
        for w, h, rot in ((w0, h0, False), (h0, w0, True)) if gira else ((w0, h0, False),):
            if h > H + e:
                continue
            for i in range(len(sky)):
                y1 = sky[i][0]
                if y1 + h > H + e:
                    break
                y2 = y1 + h
                xs, v = 0.0, 0.0
                for a, b, x in sky:
                    if b > y1 + e and a < y2 - e:
                        xs = max(xs, x)
                for a, b, x in sky:
                    if b > y1 + e and a < y2 - e:
                        v += (xs - x) * (min(b, y2) - max(a, y1))
                sc = (round(v, 6), xs + w, y1)
                if best is None or sc < best[0]:
                    best = (sc, y1, xs, w, h, rot)
        if best is None:
            return None
        (v, _, _), y1, xs, w, h, rot = best
        vuoto += v
        posti.append((p, xs, y1, w, h, rot))
        y2 = y1 + h
        nuovo = []
        for a, b, x in sky:
            if b <= y1 + e or a >= y2 - e:
                nuovo.append([a, b, x])
            else:
                if a < y1 - e:
                    nuovo.append([a, y1, x])
                if b > y2 + e:
                    nuovo.append([y2, b, x])
        nuovo.append([y1, y2, xs + w])
        nuovo.sort()
        sky = []
        for t in nuovo:                  # unisce i tratti vicini alla stessa x
            if sky and abs(sky[-1][2] - t[2]) < e and abs(sky[-1][1] - t[0]) < e:
                sky[-1][1] = t[1]
            else:
                sky.append(t)
    larg = max(x for _, _, x in sky)
    return vuoto, larg, posti


def _dallalto(items, R, Hmax, pre=()):
    """Impila i pezzi dall'alto verso il basso in una striscia larga R: ogni pezzo sale finche'
    tocca il bordo in alto o un pezzo gia' messo, nel posto che lascia meno vuoto sopra di se'.
    Il vuoto che resta in fondo non e' un buco: tocca la striscia che avanza.
    items: (p, w, h, girabile); pre: pezzi gia' fissati (p, x, y, w, h, rot).
    Restituisce (vuoti, profondita', posti) oppure None."""
    e = 1e-9
    sky = [[0.0, R, 0.0]]                # tratti [x1, x2, y]: fin dove arrivano i pezzi
    posti = []
    vuoto = 0.0

    def metti(x1, w, y):
        nonlocal sky
        x2 = x1 + w
        nuovo = []
        for a, b, yy in sky:
            if b <= x1 + e or a >= x2 - e:
                nuovo.append([a, b, yy])
            else:
                if a < x1 - e:
                    nuovo.append([a, x1, yy])
                if b > x2 + e:
                    nuovo.append([x2, b, yy])
        nuovo.append([x1, x2, y])
        nuovo.sort()
        sky = []
        for t in nuovo:
            if sky and abs(sky[-1][2] - t[2]) < e and abs(sky[-1][1] - t[0]) < e:
                sky[-1][1] = t[1]
            else:
                sky.append(t)

    for p, x, y, w, h, rot in pre:
        metti(x, w, y + h)
        posti.append((p, x, y, w, h, rot))
    for p, w0, h0, gira in items:
        best = None
        for w, h, rot in ((w0, h0, False), (h0, w0, True)) if gira else ((w0, h0, False),):
            # il pezzo puo' cominciare all'inizio di un tratto o finire alla fine di un tratto
            inizi = set()
            for a, b, _ in sky:
                inizi.add(a)
                inizi.add(b - w)
            for x1 in inizi:
                if x1 < -e or x1 + w > R + e:
                    continue
                x2 = x1 + w
                ys = max(yy for a, b, yy in sky if b > x1 + e and a < x2 - e)
                if ys + h > Hmax + e:
                    continue
                v = sum((ys - yy) * (min(b, x2) - max(a, x1)) for a, b, yy in sky if b > x1 + e and a < x2 - e)
                sc = (round(v, 6), ys + h, x1)
                if best is None or sc < best[0]:
                    best = (sc, x1, ys, w, h, rot)
        if best is None:
            return None
        (v, _, _), x1, ys, w, h, rot = best
        vuoto += v
        posti.append((p, x1, ys, w, h, rot))
        metti(x1, w, ys + h)
    # quanto e' irregolare il fondo: le fessure profonde tra i pezzi pesano molto
    fondo = sum((Hmax - yy) ** 2 * (b - a) for a, b, yy in sky)
    return vuoto, fondo, posti


def impacca(lista, W=70.0, H=50.0):
    """La base va nell'angolo in alto a sinistra. Gli altri pezzi occupano tutta la larghezza del
    foglio a destra della base, appoggiati al bordo in alto: cosi' la fila e' la meno profonda
    possibile e i bordi del foglio fanno da lato ai pezzi. La coppia M02 + M10 va nell'angolo in
    alto a destra, con le parti da buttare contro il bordo del foglio. Tra i pezzi niente buchi:
    il vuoto resta solo sul fondo, attaccato all'avanzo."""
    import random
    base = [p for p in lista if p.cod == "M01"][0]
    bw, bh = base.bbox()
    m02, m10, Hc, f02, f10 = coppia_inclinata(lista)
    Lc = m02.bbox()[0]
    altri = [p for p in lista if p not in (base, m02, m10) and getattr(p, "poliplat", True)]
    COPPIA = "coppia"
    elementi = [(p, *p.bbox(), True) for p in altri]
    R = W - bw
    rnd = random.Random(11)
    modi = {"in piedi": (COPPIA, R - Hc, 0.0, Hc, Lc, False),     # scarti verso il bordo destro
            "sdraiata": (COPPIA, R - Lc, 0.0, Lc, Hc, True)}     # scarti verso il bordo in alto

    def prof(r):
        return max(y + h for _, x, y, w, h, _ in r[2])

    voto = lambda r: (round(r[0], 3), round(prof(r), 2), round(r[1], 1))
    migliore = None
    for nome, pre in modi.items():
        chiavi = [lambda t: -max(t[1], t[2]), lambda t: -(t[1] * t[2]), lambda t: -min(t[1], t[2])]
        partenze = [sorted(elementi, key=k) for k in chiavi]
        for _ in range(150):
            l = elementi[:]
            rnd.shuffle(l)
            partenze.append(l)
        cand = []
        for l in partenze:
            r = _dallalto(l, R, bh, [pre])
            if r is not None:
                cand.append((voto(r), l, r))
        cand.sort(key=lambda t: t[0])
        for v, l, r in cand[:4]:
            for _ in range(3000):
                m = l[:]
                a, b = rnd.randrange(len(m)), rnd.randrange(len(m))
                if rnd.random() < 0.5:
                    m[a], m[b] = m[b], m[a]
                else:
                    m.insert(b, m.pop(a))
                r2 = _dallalto(m, R, bh, [pre])
                if r2 is not None and voto(r2) <= v:
                    v, l, r = voto(r2), m, r2
            if migliore is None or v < migliore[0]:
                migliore = (v, r, nome)
    (vuoto, D, fondo), r, nome = migliore
    posti = [(base, (lambda u, v: (u, bh - v)), (0.0, 0.0, bw, bh))]
    for p, x, y, w, h, rot in r[2]:
        X, Y = bw + x, y
        if p == COPPIA:
            if rot:   # sdraiata, scarti in alto
                blocco = (lambda X, Y: lambda u, v: (X + u, Y + Hc - v))(X, Y)
            else:     # in piedi, scarti a destra
                blocco = (lambda X, Y: lambda u, v: (X + v, Y + u))(X, Y)
            posti.append((m02, (lambda b: lambda u, v: b(*f02(u, v)))(blocco), (X, Y, w, h)))
            posti.append((m10, (lambda b: lambda u, v: b(*f10(u, v)))(blocco), None))
            continue
        h0 = p.bbox()[1]
        if rot:
            fn = (lambda X, Y: lambda u, v: (X + v, Y + u))(X, Y)
        else:
            fn = (lambda X, Y, h0: lambda u, v: (X + u, Y + h0 - v))(X, Y, h0)
        posti.append((p, fn, (X, Y, w, h)))
    print("coppia %s; buchi tra i pezzi %.2f cm2; fila profonda %.2f cm" % (nome, vuoto, D))
    return posti, D


def _txt(x, y, t, size=11, bold=False, col="#7a0000", rot=0, anchor="middle"):
    w = ' font-weight="bold"' if bold else ""
    r = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}"{w} fill="{col}" text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="2.5" paint-order="stroke"{r}>{t}</text>')


def schema_taglio(P, path):
    posti, D = impacca(P)
    s = 20.0
    o = (40, 96)
    W, H = 70 * s + 80, 50 * s + 150
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="16" y="30" {FONT} font-size="20" font-weight="bold" fill="#333">Il foglio di Poliplat 70 × 50 cm: dove tagliare i pezzi (misure in cm)</text>',
           f'<text x="16" y="54" {FONT} font-size="14" fill="#555">Dentro ogni pezzo: il codice e le misure come sta nel foglio (larghezza × altezza). '
           f'Le parti a righe si buttano. Finestre, porte e bordi inclinati sono quotati nell\'immagine dei pezzi con le aperture.</text>',
           '<defs><pattern id="righe" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           '<line x1="0" y1="0" x2="0" y2="6" stroke="#bbb" stroke-width="2"/></pattern></defs>',
           f'<rect x="{o[0]}" y="{o[1]}" width="{70 * s}" height="{50 * s}" fill="#eef5ea" stroke="#333" stroke-width="2"/>']
    # quote del foglio
    out.append(_txt(o[0] + 35 * s, o[1] - 10, "70", 14, True, "#333"))
    out.append(_txt(o[0] - 14, o[1] + 25 * s, "50", 14, True, "#333", -90))
    for p, fn, box in posti:
        if box:
            bx, by, bw_, bh_ = box
            out.append(f'<rect x="{o[0] + bx * s:.1f}" y="{o[1] + by * s:.1f}" width="{bw_ * s:.1f}" height="{bh_ * s:.1f}" fill="url(#righe)" stroke="#999" stroke-width="0.6"/>')
    for p, fn, box in posti:
        T2 = lambda u, v: (o[0] + fn(u, v)[0] * s, o[1] + fn(u, v)[1] * s)
        d = "M " + " L ".join("%.1f %.1f" % T2(u, v) for u, v in p.piatto()) + " Z"
        for u1, v1, u2, v2 in p.buchi:
            d += " M " + " L ".join("%.1f %.1f" % T2(u, v) for u, v in [(u1, v1), (u2, v1), (u2, v2), (u1, v2)]) + " Z"
        out.append(f'<path d="{d}" fill="#f6c9c9" fill-rule="evenodd" stroke="{ROSSO}" stroke-width="1.3"/>')
    # etichette: codice e misure, nel verso in cui c'e' piu' posto
    for p, fn, box in posti:
        if p.cod in ("M02", "M10"):
            pts = [fn(u, v) for u, v in p.piatto()]
            xs, ys = [a for a, _ in pts], [b for _, b in pts]
            bx, by, bw_, bh_ = min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
        else:
            bx, by, bw_, bh_ = box
        w0, h0 = p.bbox()
        dims = "%s × %s" % (num(bw_), num(bh_))
        cx, cy = o[0] + (bx + bw_ / 2) * s, o[1] + (by + bh_ / 2) * s
        if p.cod in ("M02", "M10"):
            cx += (-0.25 if p.cod == "M02" else 0.25) * bw_ * s
        lw, lh = bw_ * s, bh_ * s
        need = len(dims) * 6.2
        if lw >= need and lh >= 30:
            out.append(_txt(cx, cy - 3, p.cod, 13, True))
            out.append(_txt(cx, cy + 12, dims, 11, False, "#333"))
        elif lh >= need and lw >= 30:
            out.append(_txt(cx - 3, cy, p.cod, 13, True, rot=-90))
            out.append(_txt(cx + 12, cy, dims, 11, False, "#333", -90))
        elif min(lw, lh) >= 22:      # due righe piccole, nel verso piu' lungo
            r = 0 if lw >= lh else -90
            if r == 0:
                out.append(_txt(cx, cy - 1, p.cod, 9, True))
                out.append(_txt(cx, cy + 9, dims.replace(" ", ""), 8, False, "#333"))
            else:
                out.append(_txt(cx - 1, cy, p.cod, 9, True, rot=-90))
                out.append(_txt(cx + 9, cy, dims.replace(" ", ""), 8, False, "#333", -90))
        elif lw >= lh:
            out.append(_txt(cx, cy + 3, p.cod + " " + dims.replace(" ", ""), 7.5, True))
        else:
            out.append(_txt(cx + 3, cy, p.cod + " " + dims.replace(" ", ""), 7.5, True, rot=-90))
    # l'avanzo
    out.append(_txt(o[0] + 35 * s, o[1] + 36 * s, "avanza tutta la parte verde: tienila per il plastico della tua nuova disposizione", 18, False, "#4c7a3d"))
    out.append(_txt(o[0] + 35 * s, o[1] + 36 * s + 24, "(sotto la base resta una striscia intera di 70 × %s cm)" % num(50 - [q for q, _, _ in posti if q.cod == "M01"][0].bbox()[1]), 14, False, "#4c7a3d"))
    yb = o[1] + 50 * s + 30
    out.append(f'<text x="16" y="{yb}" {FONT} font-size="14" fill="#555">Tra i pezzi non c\'è spazio: due pezzi vicini hanno la linea di taglio in comune. '
               f'I pezzi a destra della base usano come lati il bordo in alto e il bordo destro del foglio.</text>')
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))
    return posti, D


def schema_taglio_nadia(path_json, path):
    """Lo schema di taglio con la disposizione fatta da Nadia nella pagina interattiva
    (i contorni e i buchi dei pezzi sono gia' nelle coordinate del foglio, in cm)."""
    import json
    pezzi = json.load(open(path_json))
    s = 20.0
    o = (40, 96)
    W, H = 70 * s + 80, 50 * s + 150
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="16" y="30" {FONT} font-size="20" font-weight="bold" fill="#333">Il foglio di Poliplat 70 × 50 cm: la disposizione di Nadia (misure in cm)</text>',
           f'<text x="16" y="54" {FONT} font-size="14" fill="#555">Dentro ogni pezzo: il codice e le misure come sta nel foglio (larghezza × altezza). '
           f'I buchi dentro i pezzi sono finestre e porte. Il verde avanza.</text>',
           f'<rect x="{o[0]}" y="{o[1]}" width="{70 * s}" height="{50 * s}" fill="#eef5ea" stroke="#333" stroke-width="2"/>']
    for x in range(0, 71, 5):
        out.append(_txt(o[0] + x * s, o[1] - 10, str(x), 12, False, "#666"))
    for y in range(0, 51, 5):
        out.append(_txt(o[0] - 8, o[1] + y * s + 4, str(y), 12, False, "#666", anchor="end"))
    for p in pezzi:
        T2 = lambda q: (o[0] + q[0] * s, o[1] + q[1] * s)
        d = "M " + " L ".join("%.1f %.1f" % T2(q) for q in p["outline"]) + " Z"
        for hl in p["holes"]:
            d += " M " + " L ".join("%.1f %.1f" % T2(q) for q in hl) + " Z"
        out.append(f'<path d="{d}" fill="#f6c9c9" fill-rule="evenodd" stroke="{ROSSO}" stroke-width="1.3"/>')
    for p in pezzi:
        xs = [a for a, _ in p["outline"]]
        ys = [b for _, b in p["outline"]]
        bw_, bh_ = max(xs) - min(xs), max(ys) - min(ys)
        cx = o[0] + sum(xs) / len(xs) * s
        cy = o[1] + sum(ys) / len(ys) * s
        dims = "%s × %s" % (num(bw_), num(bh_))
        lw, lh = bw_ * s, bh_ * s
        need = len(dims) * 6.2
        if lw >= need and lh >= 30:
            out.append(_txt(cx, cy - 3, p["cod"], 13, True))
            out.append(_txt(cx, cy + 12, dims, 11, False, "#333"))
        elif lh >= need and lw >= 30:
            out.append(_txt(cx - 3, cy, p["cod"], 13, True, rot=-90))
            out.append(_txt(cx + 12, cy, dims, 11, False, "#333", -90))
        elif min(lw, lh) >= 22:
            if lw >= lh:
                out.append(_txt(cx, cy - 1, p["cod"], 9, True))
                out.append(_txt(cx, cy + 9, dims.replace(" ", ""), 8, False, "#333"))
            else:
                out.append(_txt(cx - 1, cy, p["cod"], 9, True, rot=-90))
                out.append(_txt(cx + 9, cy, dims.replace(" ", ""), 8, False, "#333", -90))
        elif lw >= lh:
            out.append(_txt(cx, cy + 3, p["cod"] + " " + dims.replace(" ", ""), 7.5, True))
        else:
            out.append(_txt(cx + 3, cy, p["cod"] + " " + dims.replace(" ", ""), 7.5, True, rot=-90))
    out.append(_txt(o[0] + 35 * s, o[1] + 40 * s, "avanza tutta la parte verde: tienila per il plastico della tua nuova disposizione", 18, False, "#4c7a3d"))
    out.append(_txt(o[0] + 35 * s, o[1] + 40 * s + 24, "(in basso resta una striscia intera di 70 × 20 cm)", 14, False, "#4c7a3d"))
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))


def pezzi_quotati(P, path):
    """I pezzi con finestre, porte o bordo inclinato, ognuno con le sue quote, come in pianta."""
    codici = ["M02", "M10", "M04", "M09", "M03", "M06", "M07", "M25", "M26"]
    sel = [p for c in codici for p in P if p.cod == c]
    s = 34.0
    col_w = 640
    out_parti = []
    x0, y0, riga_h, colonna = 0, 70, 0, 0
    pos = []
    for p in sel:
        w, h = p.bbox()
        pw, ph = w * s + 130, h * s + 120
        if colonna == 1 and pw > col_w:
            colonna, x0, y0 = 0, 0, y0 + riga_h
            riga_h = 0
        pos.append((p, x0 + 70, y0 + 40, pw, ph))
        riga_h = max(riga_h, ph)
        if pw > col_w or colonna == 1:
            colonna, x0, y0, riga_h = 0, 0, y0 + riga_h, 0
        else:
            colonna, x0 = 1, col_w
    W = 2 * col_w + 40
    H = y0 + riga_h + 30
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="16" y="30" {FONT} font-size="20" font-weight="bold" fill="#333">I pezzi con finestre, porte o bordo inclinato (misure in cm)</text>',
           f'<text x="16" y="54" {FONT} font-size="14" fill="#555">Ogni pezzo è disegnato in piedi, come sarà nel plastico: le misure in basso si contano da sinistra, quelle di lato dal basso.</text>']
    for p, px, py, pw, ph in pos:
        w, h = p.bbox()
        forma = p.piatto()
        T2 = lambda u, v: (px + u * s, py + 26 + (h - v) * s)
        out.append(f'<text x="{px - 50}" y="{py + 6}" {FONT} font-size="15" font-weight="bold" fill="#7a0000">{p.cod}  {p.nome}</text>')
        d = "M " + " L ".join("%.1f %.1f" % T2(u, v) for u, v in forma) + " Z"
        for u1, v1, u2, v2 in p.buchi:
            d += " M " + " L ".join("%.1f %.1f" % T2(u, v) for u, v in [(u1, v1), (u2, v1), (u2, v2), (u1, v2)]) + " Z"
        out.append(f'<path d="{d}" fill="#f6c9c9" fill-rule="evenodd" stroke="{ROSSO}" stroke-width="1.5"/>')
        # catena orizzontale sotto: bordi del pezzo, delle aperture e degli spigoli in alto
        tutti_b = p.buchi + getattr(p, "porte", [])
        xs = sorted({0.0, round(w, 3)} | {round(a, 3) for b in tutti_b for a in (b[0], b[2])} |
                    {round(u, 3) for u, v in forma if 0 < u < w})
        yq = py + 26 + h * s + 26
        for a, b in zip(xs, xs[1:]):
            A, B = T2(a, 0)[0], T2(b, 0)[0]
            out.append(f'<line x1="{A:.1f}" y1="{yq}" x2="{B:.1f}" y2="{yq}" stroke="#888" stroke-width="0.8"/>')
            # se il tratto e' corto la misura va sotto la linea
            out.append(_txt((A + B) / 2, yq - 5 if B - A > 24 else yq + 15, num(b - a), 11, False, BLU))
        for a in xs:
            A = T2(a, 0)[0]
            out.append(f'<line x1="{A - 4:.1f}" y1="{yq + 4}" x2="{A + 4:.1f}" y2="{yq - 4}" stroke="#333" stroke-width="1.2"/>')
            out.append(f'<line x1="{A:.1f}" y1="{yq - 9}" x2="{A:.1f}" y2="{T2(0, 0)[1] + 4:.1f}" stroke="#bbb" stroke-width="0.6" stroke-dasharray="2,2"/>')
        out.append(_txt((T2(0, 0)[0] + T2(w, 0)[0]) / 2, yq + 20, "totale " + num(w), 12, True, "#333"))
        # catena verticale a sinistra: davanzali e architravi, e l'altezza del lato sinistro
        hs = sorted({0.0} | {round(v, 3) for b in tutti_b for v in (b[1], b[3])} |
                    {round(v, 3) for u, v in forma if abs(u) < 1e-6})
        xq = px - 22
        for a, b in zip(hs, hs[1:]):
            A, B = T2(0, a)[1], T2(0, b)[1]
            out.append(f'<line x1="{xq}" y1="{A:.1f}" x2="{xq}" y2="{B:.1f}" stroke="#888" stroke-width="0.8"/>')
            out.append(_txt(xq - 6 if A - B > 24 else xq - 20, (A + B) / 2, num(b - a), 11, False, BLU, -90))
        for a in hs:
            A = T2(0, a)[1]
            out.append(f'<line x1="{xq - 4}" y1="{A + 4:.1f}" x2="{xq + 4}" y2="{A - 4:.1f}" stroke="#333" stroke-width="1.2"/>')
        # altezze dei vertici in alto (bordo inclinato o a gradino)
        for u, v in forma:
            if v > 0:
                X, Y = T2(u, v)
                anchor = "start" if u >= w - 1e-6 else ("end" if u <= 1e-6 else "middle")
                dx = 6 if anchor == "start" else (-6 if anchor == "end" else 0)
                out.append(_txt(X + dx, Y - 6, "h " + num(v), 11, True, "#333", anchor=anchor))
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))


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
    muro(d, 0.40, 4.70, 9.75, 5.00, [(2.20, 5.05), (5.05, 6.10)])
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
    # il focolare al centro del patio (il quadrato della scheda, circa 1,40 di lato)
    d.rect(4.25, 8.75, 5.65, 10.15, "none", "#333", 1.4)
    d.rect(4.45, 8.95, 5.45, 9.95, "none", "#333", 0.7)
    d.text(4.95, 10.55, "focolare", "#333", 10)
    d.catena([4.25, 5.65], None, "x", 8.45, [BLU], 10)
    d.catena([8.75, 10.15], None, "y", 3.95, [BLU], 10)
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
                    (4.7, 6.9, "PATIO"), (12.3, 5.6, "bagno"), (12.0, 7.3, "guardaroba"),
                    (12.1, 9.6, "camera"), (11.9, 12.6, "camera"), (10.25, 8.8, "corr."),
                    (15.25, 2.0, "ingresso"), (16.65, -2.6, "wc"), (18.9, -1.9, "camera"), (22.0, -1.9, "camera"),
                    (19.7, -4.6, "ANNESSO DEGLI OSPITI (in legno)")]:
        d.text(x, y, t, "#333", 12 if t not in ("PATIO",) else 15, bold=t.isupper())
    d.text(15.25, -1.75, "entrata", "#333", 10)
    d.text(4.7, 14.85, "apertura del recinto", "#333", 11)
    d.text(-0.55, 10.15, "graticcio di legno", "#333", 11, rot=-90)
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
    tetto = [(0, 6.05), (12.25, 2.60), (13.90, H4), (13.90, H4 - 0.5), (12.25, 2.10), (0, 5.55)]
    blocco(7.3 * s + 50, "1. Fascia nord: atelier, pranzo, cucina (sezione ovest-est della scheda)",
           [([(0, 0), (0.40, 0), (0.40, 5.55), (0, 5.55)], "#555"),
            ([(14.10, 0), (14.40, 0), (14.40, H4), (14.10, H4)], "#555"),
            ([(9.45, 0), (9.75, 0), (9.75, 2.75), (9.45, 2.75)], "#999"),
            (tetto, "#bbb"),
            ([(0.40, 2.35), (3.70, 2.35), (3.70, 2.85), (0.40, 2.85)], "#9cc0e8")],
           [(0, 6.05, "+6,05", NERO), (12.25, 2.60, "+2,60 (punto più basso, a 12,25)", BLU), (14.40, 3.25, "+3,25", NERO),
            (3.70, 2.85, "+2,85 soppalco", NERO), (0.40, 0, "±0,00 pavimento", NERO)],
           ["Il tetto è a «farfalla»:", "scende da ovest a est fino", "a 12,25 m e poi risale.", "Lo spessore del tetto è 0,50", "(il Poliplat)."])
    # 2. ala delle camere e recinto ovest
    blocco(2 * 7.3 * s + 90, "2. Patio e ala delle camere (sezione sul patio della scheda)",
           [([(0, 0), (0.40, 0), (0.40, HRECINTO), (0, HRECINTO)], "#555"),
            ([(9.45, 0), (9.75, 0), (9.75, h_ala(9.45) - 0.5), (9.45, h_ala(9.45) - 0.5)], "#555"),
            ([(14.10, 0), (14.40, 0), (14.40, H4), (14.10, H4)], "#555"),
            ([(9.45, h_ala(9.45) - 0.5), (12.25, 2.10), (13.90, H4 - 0.5), (13.90, H4), (12.25, 2.60), (9.45, h_ala(9.45))], "#bbb")],
           [(0, HRECINTO, "+%s recinto ovest (muretto 1,80 nel tratto del graticcio)" % num(HRECINTO), BLU), (9.45, h_ala(9.45), "+" + num(h_ala(9.45)), BLU),
            (14.40, 3.25, "+3,25", BLU), (12.25, 2.10, "+2,10 / +2,60", BLU), (9.75, h_ala(9.45) - 0.5, "+" + num(h_ala(9.45) - 0.5), BLU)],
           ["Recinto sud (dalla foto del patio):", "pezzo ovest da %s nell'angolo" % num(HRECINTO), "a 4,38 verso l'apertura;", "pezzo est da 4,25 verso",
            "l'apertura a %s verso le camere." % num(h_ala(9.45)), "Il tetto delle camere sta sullo", "stesso piano di quello della fascia nord."])
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
    pianta_quotata(OUT + "muuratsalo-%s-1-pianta-quotata.svg" % VER)
    sezioni(OUT + "muuratsalo-%s-2-altezze.svg" % VER)
    nadia = os.path.join(os.path.dirname(os.path.abspath(__file__)), "composizione-muuratsalo-taglio-nadia.json")
    if os.path.exists(nadia):     # la disposizione scelta da Nadia nella pagina interattiva
        schema_taglio_nadia(nadia, OUT + "muuratsalo-%s-3-taglio-foglio.svg" % VER)
    else:
        schema_taglio(P, OUT + "muuratsalo-%s-3-taglio-foglio.svg" % VER)
    pezzi_quotati(P, OUT + "muuratsalo-%s-4-pezzi-quotati.svg" % VER)
    titoli = {1: "Passo 1: la base", 2: "Passo 2: i muri esterni nord, ovest ed est", 3: "Passo 3: il recinto del patio",
              4: "Passo 4: l'ala delle camere", 5: "Passo 5: il muro dell'atelier sul patio e il camino",
              6: "Passo 6: le pareti interne", 7: "Passo 7: il soppalco", 8: "Passo 8: l'ingresso",
              9: "Passo 9: l'annesso degli ospiti", 10: "Passo 10: i tetti e il comignolo"}
    for k, t in titoli.items():
        try:
            vista3d_png(P, k, t, OUT + "muuratsalo-%s-passo-%02d.png" % (VER, k))
        except ImportError:      # senza numpy e PIL: il disegno vettoriale di prima
            vista3d(P, k, t, OUT + "muuratsalo-%s-passo-%02d.svg" % (VER, k))
    # tabella per la pagina
    for p in P:
        if getattr(p, "poliplat", True):
            print("| %s | %s | %s | %s |" % (p.cod, p.nome, p.misura(), p.passo))


if __name__ == "__main__":
    main()
