"""Esercizio 4 (Muuratsalo): altre quattro proposte, con forme non solo rettangolari.

Le stanze sono poligoni qualsiasi; nella proposta del patio rotondo il cerchio del patio
"morde" le stanze. Superfici, sovrapposizioni, patio, recinto e porte si controllano su una
griglia di 2,5 cm. Serve numpy (c'e' nell'ambiente di sbobine-whisper).
Uso: python composizione-muuratsalo-proposte-2.py USCITA.html
"""
import math
import sys

import numpy as np

LATO, R = 14.40, 0.40
A, B_ = R, LATO - R
PASSO = 0.025

AALTO = {"SP": 9.35 * 4.35, "K": 4.25 * 3.05, "I": 4.25 * 1.25, "C": 1.00 * 6.25,
         "B": 3.25 * 1.50, "G": 3.25 * 1.95, "L2": 3.25 * 2.80, "L1": 4.25 * 3.05}
NOMI = {"SP": "Soggiorno, pranzo e atelier", "K": "Cucina", "I": "Ingresso (disimpegno)",
        "C": "Corridoio", "B": "Bagno", "G": "Guardaroba", "L2": "Camera", "L1": "Camera grande"}
CORTI = {"SP": "Soggiorno e pranzo", "K": "Cucina", "I": "Ingresso", "C": "Corridoio",
         "B": "Bagno", "G": "Guard.", "L2": "Camera", "L1": "Camera grande"}
ZONA = {"SP": "giorno", "K": "giorno", "I": "distr", "C": "distr", "B": "servizi", "G": "notte",
        "L2": "notte", "L1": "notte"}
COL = {"giorno": "#f6d5cf", "notte": "#d3e0f3", "servizi": "#e3d5ef", "distr": "#fbecb3"}
PATIO_AALTO = (B_ - A) ** 2 - sum(AALTO.values())
SOPP_AREA = 3.30 * 4.35

# griglia dei centri delle celle dentro il recinto
_g = np.arange(A + PASSO / 2, B_, PASSO)
GX, GY = np.meshgrid(_g, _g)


def dentro(poly, x, y):
    """Punto (o array di punti) dentro il poligono: regola pari/dispari."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ins = np.zeros(np.broadcast(x, y).shape, bool)
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if y1 == y2:
            continue
        cond = (y1 > y) != (y2 > y)
        xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        ins ^= cond & (x < xi)
    return ins


def cerchio(c, r, n=240):
    return [(c[0] + r * math.cos(2 * math.pi * i / n), c[1] + r * math.sin(2 * math.pi * i / n))
            for i in range(n)]


class Proposta:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.morso = kw.get("morso")          # poligono del patio che toglie spazio alle stanze
        self._maschere = None

    def in_stanza(self, k, x, y):
        m = dentro(self.stanze[k], x, y)
        if self.morso is not None:
            m &= ~dentro(self.morso, x, y)
        return m

    def maschere(self):
        if self._maschere is None:
            self._maschere = {k: self.in_stanza(k, GX, GY) for k in self.stanze}
        return self._maschere

    def area(self, k):
        return self.maschere()[k].sum() * PASSO ** 2

    def patio(self):
        tot = sum(self.maschere().values())
        return (tot == 0)


def collegato(mask):
    """Il patio e' un solo pezzo? (riempimento a macchia d'olio sulla griglia)"""
    seme = np.unravel_index(np.argmax(mask), mask.shape)
    vis = np.zeros_like(mask)
    vis[seme] = True
    while True:
        nuovo = vis.copy()
        nuovo[1:] |= vis[:-1]
        nuovo[:-1] |= vis[1:]
        nuovo[:, 1:] |= vis[:, :-1]
        nuovo[:, :-1] |= vis[:, 1:]
        nuovo &= mask
        if (nuovo == vis).all():
            return vis.sum() == mask.sum()
        vis = nuovo


def controlla(p):
    err = []
    m = p.maschere()
    tot = sum(m.values())
    if (tot > 1).sum() * PASSO ** 2 > 0.02:
        doppi = [(a, b) for a in m for b in m if a < b and (m[a] & m[b]).sum() * PASSO ** 2 > 0.02]
        err.append(f"sovrapposizioni {doppi}")
    for k in p.stanze:
        a = p.area(k)
        if k not in ("I", "C") and abs(a / AALTO[k] - 1) > 0.05:
            err.append(f"{k}: {a:.2f} invece di {AALTO[k]:.2f}")
        if min(x for x, _ in p.stanze[k]) < A - 1e-6 or max(x for x, _ in p.stanze[k]) > B_ + 1e-6 or \
           min(y for _, y in p.stanze[k]) < A - 1e-6 or max(y for _, y in p.stanze[k]) > B_ + 1e-6:
            err.append(f"{k} esce dal recinto")
    d = p.area("I") + p.area("C")
    if abs(d / (AALTO["I"] + AALTO["C"]) - 1) > 0.05:
        err.append(f"ingresso + corridoio {d:.2f}")
    pat = p.patio()
    ap = pat.sum() * PASSO ** 2
    if abs(ap / PATIO_AALTO - 1) > 0.05:
        err.append(f"patio {ap:.2f}")
    if not collegato(pat):
        err.append("il patio è diviso in più pezzi")
    # graticcio (ovest, y 7,70-12,60) e apertura sud (x 2,45-6,95) devono dare sul patio
    yy = np.arange(7.72, 12.59, 0.05)
    if not pat[((yy - A) / PASSO).astype(int), 0].all():
        err.append("il graticcio non dà sul patio")
    xx = np.arange(2.47, 6.94, 0.05)
    if not pat[-1, ((xx - A) / PASSO).astype(int)].all():
        err.append("l'apertura sud non dà sul patio")
    # porte: un punto per parte deve stare nelle due stanze
    g = {k: set() for k in p.stanze}
    for a, b, (x1, y1), (x2, y2) in p.porte:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        lx, ly = x2 - x1, y2 - y1
        L = math.hypot(lx, ly)
        nx, ny = -ly / L, lx / L
        lati = []
        for s in (1, -1):
            px, py = mx + s * 0.06 * nx, my + s * 0.06 * ny
            if not (A < px < B_ and A < py < B_):
                lati.append("fuori")
                continue
            chi = [k for k in p.stanze if p.in_stanza(k, px, py)]
            lati.append(chi[0] if chi else "patio")
        if sorted(lati) != sorted([a, b]):
            err.append(f"porta {a}-{b}: ai due lati ci sono {lati}")
        if b in p.stanze:
            g[a].add(b)
            g[b].add(a)
        if b == "fuori":
            if a != "I":
                err.append("la porta d'ingresso non dà sull'ingresso")
            if min(math.hypot(mx - cx, my - cy) for cx in (A, B_) for cy in (A, B_)) > 2.5:
                err.append("la porta d'ingresso non è nell'angolo")
    for dest in p.stanze:
        if ZONA[dest] in ("notte", "servizi"):
            vis, coda = {"I"}, ["I"]
            while coda:
                n = coda.pop()
                for q in g[n]:
                    if q in ("I", "C", dest) and q not in vis:
                        vis.add(q)
                        coda.append(q)
            if dest not in vis:
                err.append(f"{dest} non si raggiunge dal distributivo")
    vis, coda = {"I"}, ["I"]
    while coda:
        n = coda.pop()
        for q in g[n]:
            if q not in vis and ZONA[q] != "notte":
                vis.add(q)
                coda.append(q)
    for dest in ("SP", "K"):
        if dest not in vis:
            err.append(f"{dest} si raggiunge solo passando da una camera")
    if not g["SP"] & {"I", "C"}:
        err.append("il soggiorno non è sul distributivo")
    if not ("K" in g["SP"] or g["K"] & {"I", "C"}):
        err.append("la cucina non è collegata")
    # soppalco dentro la zona giorno
    s = p.sopp
    sx = np.arange(s[0] + 0.05, s[2], 0.1)
    sy = np.arange(s[1] + 0.05, s[3], 0.1)
    SX, SY = np.meshgrid(sx, sy)
    if not (p.in_stanza("SP", SX, SY) | p.in_stanza("K", SX, SY)).all():
        err.append("il soppalco esce dalla zona giorno")
    if abs((s[2] - s[0]) * (s[3] - s[1]) / SOPP_AREA - 1) > 0.01:
        err.append("soppalco con superficie diversa")
    return err, ap


def risolvi(f, obiettivo, a, b, it=40):
    """Trova t tra a e b con f(t) = obiettivo (f monotona)."""
    fa = f(a) - obiettivo
    for _ in range(it):
        m = (a + b) / 2
        fm = f(m) - obiettivo
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2


def area_poly(poly, morso=None):
    if morso is None:
        return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]))) / 2
    m = dentro(poly, GX, GY)
    if morso is not None:
        m &= ~dentro(morso, GX, GY)
    return m.sum() * PASSO ** 2


def rett(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


# --- 5. Il patio rotondo intorno al focolare ----------------------------------------------
def proposta_5():
    c = (4.70, 10.15)        # centro: a meta' del graticcio in y e dell'apertura sud in x
    r = risolvi(lambda r: (dentro(cerchio(c, r), GX, GY)).sum() * PASSO ** 2, PATIO_AALTO, 5.0, 6.5)
    morso = cerchio(c, r)
    xi0, iy = 9.0, A + AALTO["I"] / (B_ - 9.0)
    a1 = risolvi(lambda a: area_poly(rett(A, A, a, 9), morso), AALTO["L1"], 1.5, 5)
    b2 = risolvi(lambda b: area_poly(rett(a1, 1.40, b, 9), morso), AALTO["L2"], a1 + 1, a1 + 5)
    b3 = risolvi(lambda b: area_poly(rett(b2, 1.40, b, 9), morso), AALTO["G"], b2 + 0.5, b2 + 4)
    xb, yB = 12.40, iy + AALTO["B"] / (B_ - 12.40)

    def sp(yk):
        return [(b3, 1.40), (xi0, 1.40), (xi0, iy), (xb, iy), (xb, yB), (B_, yB), (B_, yk), (b3, yk)]
    yk = risolvi(lambda y: area_poly(sp(y), morso), AALTO["SP"], 6, 13.5)
    st = {"I": rett(xi0, A, B_, iy), "C": rett(a1, A, xi0, 1.40), "L1": rett(A, A, a1, 9),
          "L2": rett(a1, 1.40, b2, 9), "G": rett(b2, 1.40, b3, 9), "B": rett(xb, iy, B_, yB),
          "SP": sp(yk), "K": rett(b3, yk, B_, B_)}
    porte = [("I", "fuori", (B_, 0.55), (B_, 1.35)), ("I", "C", (xi0, 0.48), (xi0, 1.32)),
             ("I", "SP", (10.0, iy), (10.9, iy)), ("I", "B", (12.75, iy), (13.45, iy)),
             ("C", "L1", (a1, 0.48), (a1, 1.32)), ("C", "L2", (a1 + 0.5, 1.40), (a1 + 1.3, 1.40)),
             ("C", "G", (b2 + 0.4, 1.40), (b2 + 1.1, 1.40)), ("SP", "K", (11.6, yk), (12.5, yk))]
    # porta tra soggiorno e patio: sul cerchio, nel punto piu' a est
    pc = lambda a: (c[0] + r * math.cos(a), c[1] + r * math.sin(a))
    porte.append(("SP", "patio", pc(-0.36), pc(-0.20)))
    sopp = (B_ - 3.30, yB + 0.10, B_, yB + 0.10 + 4.35)
    return Proposta(
        titolo="Il patio rotondo intorno al focolare",
        idea=f"Il patio diventa un cerchio di {num(r)} m di raggio, con il centro sul focolare. "
             "Il cerchio è tagliato dal recinto proprio dove ci sono il graticcio e la grande "
             "apertura sud, che restano tutti e due sul patio. La casa avvolge il cerchio: le "
             "stanze hanno la parete verso il patio curva, e il fuoco diventa il centro di "
             "tutta la casa. Aalto disegna un cortile curvo simile nel suo studio di Helsinki "
             "(1955), dove la parete curva fa da gradinata.",
        percorso="Si entra nell'angolo nord-est. A sinistra parte il corridoio della zona "
                 "notte, lungo il muro nord: camera, guardaroba e camera grande in fila, con "
                 "le pareti curve sul patio. Dritto davanti c'è il bagno; a destra si scende nel "
                 "soggiorno, che gira intorno al cerchio e finisce nella cucina, a sud.",
        pro=["È la proposta più forte come idea: il vuoto non è un avanzo tra le stanze ma "
             "una forma precisa, e il focolare di Aalto diventa il centro del progetto.",
             "Le camere sono servite da un corridoio vero; il bagno è subito dopo l'ingresso.",
             "Il soggiorno guarda il patio da una lunga parete curva."],
        contro=["Le pareti curve nel plastico sono difficili: il Poliplat non si piega bene. "
                "Usa un cartoncino sottile curvato, oppure fai la curva a spezzata (tanti "
                "pezzi dritti, ognuno di 1-1,5 cm).",
                "Le stanze curve vanno arredate con attenzione: controlla che il letto entri "
                "nelle camere.",
                "Il tetto va ridisegnato, perché il soppalco è a est."],
        tetto="Il soppalco (3,30 × 4,35) sta nella parte est del soggiorno, lontano dalla curva: "
              "il tetto deve essere alto lì e può scendere verso il patio, così da fuori la "
              "casa sembra abbassarsi intorno al cerchio.",
        stanze=st, porte=porte, sopp=sopp, morso=morso, appendice="est",
        extra=("cerchio", c, r))


# --- 6. Il fronte a denti di sega ---------------------------------------------------------
def proposta_6():
    t = math.tan(math.radians(25))
    # proposta 2 (giorno a est, notte a nord), ma ogni parete sul patio e' girata di 25 gradi
    # attorno al suo centro: la superficie non cambia e ogni finestra guarda a sud-ovest
    def fondo(x0, x1, yb):        # muro sud di una stanza dell'ala nord
        d = t * (x1 - x0) / 2
        return (x1, yb + d), (x0, yb - d)
    yb = 4.65
    L1 = [(A, A), (3.45, A), *fondo(A, 3.45, yb)]
    L2 = [(3.45, 1.40), (6.20, 1.40), *fondo(3.45, 6.20, yb)]
    G = [(6.20, 1.40), (8.15, 1.40), *fondo(6.20, 8.15, yb)]
    Bf = fondo(8.15, 9.65, yb)
    Bq = [(8.15, 1.40), (9.65, 1.40), *Bf]
    xf, ytop = 9.65, Bf[0][1]
    def denti(y0, y1, n):         # muro ovest di una stanza dell'ala est, a n denti
        pts, h = [], (y1 - y0) / n
        for i in range(n):
            d = t * h / 2
            pts += [(xf - d, y0 + i * h), (xf + d, y0 + (i + 1) * h)]
        return pts
    SP = [(9.65, 1.62), (B_, 1.62), (B_, 10.97), *reversed(denti(ytop, 10.97, 2)), (9.65, ytop)]
    K = [(B_, 10.97), (B_, B_), *reversed(denti(10.97, B_, 1))]
    st = {"I": rett(9.65, A, B_, 1.62), "C": rett(3.45, A, 9.65, 1.40), "L1": L1, "L2": L2,
          "G": G, "B": Bq, "SP": SP, "K": K}
    porte = [("I", "fuori", (B_, 0.55), (B_, 1.45)), ("I", "SP", (12.1, 1.62), (13.0, 1.62)),
             ("I", "C", (9.65, 0.45), (9.65, 1.35)), ("SP", "K", (12.0, 10.97), (12.9, 10.97)),
             ("C", "B", (8.40, 1.40), (9.10, 1.40)), ("C", "G", (6.70, 1.40), (7.40, 1.40)),
             ("C", "L2", (4.60, 1.40), (5.40, 1.40)), ("C", "L1", (3.45, 0.45), (3.45, 1.35))]
    sopp = (9.65 + 0.70, 1.62 + 0.05, B_, 1.62 + 0.05 + 3.30 * 4.35 / (B_ - 10.35))
    return Proposta(
        titolo="Il fronte a denti di sega",
        idea="La disposizione è quella della proposta 2 (zona giorno a est, zona notte a "
             "nord, ingresso nell'angolo nord-est), ma ogni parete che dà sul patio è girata "
             "di 25 gradi. Così il fronte sul patio diventa una fila di denti di sega e tutte "
             "le finestre guardano a sud-ovest, verso il lago e il sole del pomeriggio. Ogni "
             "parete gira attorno al suo centro: quello che una stanza guadagna da una parte lo "
             "perde dall'altra, e le superfici restano identiche.",
        percorso="Come nella proposta 2: dall'angolo, a destra il soggiorno con il pranzo e la "
                 "cucina in fondo; a sinistra il corridoio con bagno, guardaroba e camere.",
        pro=["Una sola regola geometrica (girare le pareti) cambia tutto il carattere del patio, "
             "senza toccare l'organizzazione che funziona.",
             "Le finestre in diagonale prendono più sole e guardano tutte nella stessa "
             "direzione, verso il paesaggio.",
             "Nel plastico è facile: sono tutti pezzi dritti, cambiano solo gli angoli.",
             "I denti fanno ombra e proteggono le camere dagli sguardi dal patio."],
        contro=["Gli spigoli dei denti tolgono un po' di comodità all'arredo vicino alle "
                "finestre.",
                "Come nella proposta 2, la cucina è in fondo all'ala est e il tetto va "
                "ripensato per il soppalco."],
        tetto="Il soppalco sta in cima al soggiorno, vicino all'ingresso, con la stessa "
              "superficie di Aalto (14,4 m²). Il tetto sale verso nord-est, sopra il soppalco. "
              "Si può far seguire anche al tetto il ritmo dei denti, con una falda per dente.",
        stanze=st, porte=porte, sopp=sopp, appendice="est", extra=None)


# --- 7. La parete a onda ------------------------------------------------------------------
def proposta_7():
    amp, x0, x1, yb = 0.70, A, 9.75, 4.75
    def onda(x):
        return yb + amp * math.sin(2 * math.pi * (x - x0) / (x1 - x0))
    def fronte(xa, xb, n=60):
        return [(xa + (xb - xa) * i / n, onda(xa + (xb - xa) * i / n)) for i in range(n + 1)]
    def cucina(a):
        return [(A, A), (a, A), *reversed(fronte(A, a))]
    a = risolvi(lambda a: area_poly(cucina(a)), AALTO["K"], 2.0, 4.0)
    K = cucina(a)
    SP = [(a, A), (12.75, A), (12.75, yb), (x1, yb), *reversed(fronte(a, x1))]
    st = {"K": K, "SP": SP, "I": rett(12.75, A, B_, yb), "C": rett(13.0, yb, B_, 10.95),
          "B": rett(9.75, yb, 13.0, 6.25), "G": rett(9.75, 6.25, 13.0, 8.20),
          "L2": rett(9.75, 8.20, 13.0, 10.95), "L1": rett(9.75, 10.95, B_, B_)}
    porte = [("I", "fuori", (B_, 0.80), (B_, 1.70)), ("I", "SP", (12.75, 2.9), (12.75, 3.8)),
             ("SP", "K", (a, 1.6), (a, 2.5)), ("I", "C", (13.05, yb), (13.95, yb)),
             ("C", "B", (13.0, 5.10), (13.0, 5.80)), ("C", "G", (13.0, 7.00), (13.0, 7.70)),
             ("C", "L2", (13.0, 9.90), (13.0, 10.70)), ("C", "L1", (13.05, 10.95), (13.95, 10.95))]
    sopp = (A, A, A + 3.30, A + 4.35)
    return Proposta(
        titolo="La parete a onda",
        idea="La forma è la L della proposta 1, ma la lunga parete tra la zona giorno e il "
             "patio diventa un'onda: si gonfia verso il patio davanti alla cucina e al pranzo, "
             "rientra davanti al soggiorno. L'onda è uno dei temi di Aalto (il soffitto della "
             "biblioteca di Viipuri, il padiglione finlandese a New York, il vaso Savoy): "
             "qui porta la sua linea organica dentro un quadrato rigido. L'onda sale quanto "
             "scende, quindi la superficie del patio non cambia.",
        percorso="Come nella proposta 1: si entra nel disimpegno dell'angolo nord-est; a sinistra "
                 "il soggiorno, che scorre lungo l'onda fino al pranzo e alla cucina; dritto il "
                 "corridoio della zona notte, con il bagno per primo.",
        pro=["Il contrasto tra il quadrato del recinto e la curva libera è proprio il tema "
             "della lezione (geometria euclidea contro geometria organica).",
             "La curva crea due spazi diversi senza muri: un angolo raccolto dove rientra (il "
             "soggiorno) e uno più aperto verso il patio dove si gonfia (il pranzo).",
             "Il resto della casa è quello di Aalto: zona notte, ingresso e annesso non cambiano."],
        contro=["Nel plastico l'onda va fatta con un cartoncino curvato (o una striscia di "
                "Poliplat incisa a righe sul retro, così si piega).",
                "La cucina finisce in fondo, come nella proposta 1."],
        tetto="Il soppalco e il tetto restano quelli di Aalto: lo studio sta sopra la cucina, "
              "nella parte più alta, e si affaccia sul soggiorno.",
        stanze=st, porte=porte, sopp=sopp, appendice="est", extra=None)


# --- 8. L'ingresso in diagonale -----------------------------------------------------------
def proposta_8():
    h = 0.50                       # meta' larghezza dell'ingresso diagonale
    u1, u2 = 14.40 - h * math.sqrt(2), 14.40 + h * math.sqrt(2)
    yE = 4.10                       # fine dell'ingresso = inizio del corridoio

    def stanze(xE):
        xC = xE + 0.90
        I = [(u1 - A, A), (B_, A), (B_, u2 - B_), (u2 - yE, yE), (u1 - yE, yE)]
        sp = lambda yN: [(A, A), (u1 - A, A), (u1 - yE, yE), (xE, yE), (xE, yN), (A, yN)]
        yN = risolvi(lambda y: area_poly(sp(y)), AALTO["SP"], 3.0, 6.0)
        k = lambda yK: [(B_, u2 - B_), (B_, yK), (xC, yK), (xC, yE), (u2 - yE, yE)]
        yK = risolvi(lambda y: area_poly(k(y)), AALTO["K"], 3.0, 9.0)
        yB = yK + AALTO["B"] / (B_ - xC)
        yG = yB + AALTO["G"] / (B_ - xC)
        yL1 = B_ - AALTO["L1"] / (B_ - xE)
        return dict(xC=xC, I=I, sp=sp(yN), yN=yN, k=k(yK), yK=yK, yB=yB, yG=yG, yL1=yL1,
                    L2=(yL1 - yG) * (B_ - xC))
    xE = risolvi(lambda x: -stanze(x)["L2"], -AALTO["L2"], 7.0, 9.6)
    v = stanze(xE)
    xC, I, yN, yK, yB, yG, yL1 = v["xC"], v["I"], v["yN"], v["yK"], v["yB"], v["yG"], v["yL1"]
    st = {"I": I, "SP": v["sp"], "K": v["k"], "C": rett(xE, yE, xC, yL1),
          "B": rett(xC, yK, B_, yB), "G": rett(xC, yB, B_, yG), "L2": rett(xC, yG, B_, yL1),
          "L1": rett(xE, yL1, B_, B_)}
    porte = [("I", "fuori", (B_, 0.47), (B_, u2 - B_ - 0.05)),
             ("I", "SP", (u1 - 2.2, 2.2), (u1 - 2.9, 2.9)),
             ("I", "K", (u2 - 2.0, 2.0), (u2 - 2.8, 2.8)),
             ("I", "C", (max(xE, u1 - yE) + 0.05, yE), (xC - 0.05, yE)),
             ("C", "B", (xC, yB - 1.2), (xC, yB - 0.5)), ("C", "G", (xC, yG - 1.2), (xC, yG - 0.5)),
             ("C", "L2", (xC, yL1 - 1.0), (xC, yL1 - 0.2)), ("C", "L1", (xE + 0.05, yL1), (xC - 0.05, yL1)),
             ("SP", "patio", (5.5, yN), (6.4, yN))]
    sopp = (A, A, A + SOPP_AREA / (yN - A), yN)
    return Proposta(
        titolo="L'ingresso in diagonale",
        idea="L'ingresso parte dall'angolo nord-est e taglia la casa in diagonale, a 45 gradi, "
             "come la diagonale del quadrato. È una galleria larga 1,00 che va dall'angolo "
             "verso il patio: a destra c'è il soggiorno, a sinistra la cucina, in fondo il "
             "corridoio delle camere. Il prof ha fatto notare che il patio di Aalto sta «sulla "
             "diagonale» del quadrato: qui la diagonale diventa il percorso.",
        percorso="Si entra nell'angolo e si cammina in diagonale. Sulla destra si apre il "
                 "soggiorno, sulla sinistra la cucina, uno di fronte all'altra: l'ingresso fa da "
                 "passaggio tra pranzo e cucina. In fondo alla galleria si gira nel corridoio "
                 "lungo il patio, con il bagno per primo e poi guardaroba e camere.",
        pro=["La geometria nasce dal quadrato stesso: l'asse diagonale lega l'angolo "
             "dell'ingresso all'angolo opposto del patio, verso il lago.",
             "Chi entra vede subito, in fondo alla diagonale, il patio.",
             "Il soggiorno diventa un trapezio grande e luminoso; il bagno è a metà tra giorno e "
             "notte.",
             "Il tetto e il soppalco di Aalto possono restare (soggiorno a ovest)."],
        contro=["La cucina è separata dal pranzo dall'ingresso: va difesa come scelta (si "
                "attraversa solo la galleria, non una stanza).",
                "Gli angoli acuti delle stanze vicino alla diagonale sono scomodi da arredare: "
                "si possono usare per armadi e mobili fissi."],
        tetto=f"Il soppalco resta nell'angolo nord-ovest, sopra il soggiorno, nella parte più "
              f"alta del tetto di Aalto. Il soggiorno qui è profondo {num(yN - A)}, quindi il "
              f"soppalco diventa {num(SOPP_AREA / (yN - A))} × {num(yN - A)}: stessa superficie.",
        stanze=st, porte=porte, sopp=sopp, appendice="est", extra=None)


def num(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",")


PROPOSTE = [proposta_5(), proposta_6(), proposta_7(), proposta_8()]

if __name__ == "__main__":
    for n, p in enumerate(PROPOSTE, 5):
        e, ap = controlla(p)
        print(f"Proposta {n}: patio {ap:.2f}", "OK" if not e else e)
        print("   ", {k: round(p.area(k), 2) for k in p.stanze})


# --- disegno -----------------------------------------------------------------------------
def centro(mask):
    """Il punto piu' lontano dai bordi della maschera (erosione ripetuta)."""
    cur = mask.copy()
    while True:
        e = cur.copy()
        e[1:] &= cur[:-1]
        e[:-1] &= cur[1:]
        e[:, 1:] &= cur[:, :-1]
        e[:, :-1] &= cur[:, 1:]
        e[0] = e[-1] = False
        e[:, 0] = e[:, -1] = False
        if not e.any():
            xs, ys = GX[cur], GY[cur]
            k = np.argmin((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2)
            return xs[k], ys[k]
        cur = e


def assiale(poly):
    return all(abs(x1 - x2) < 1e-9 or abs(y1 - y2) < 1e-9
               for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]))


def appendice(lato):
    E, An = (14.40, -1.30, 16.10, 4.70), (16.10, -3.50, 23.40, 0.15)
    return E, An


def svg_pianta(p, s=30):
    E, An = appendice(p.appendice)
    x0, y0 = -0.8, An[1] - 0.9
    x1, y1 = An[2] + 0.8, LATO + 1.6
    W, H = (x1 - x0) * s, (y1 - y0) * s
    X = lambda x: (x - x0) * s
    Y = lambda y: (y - y0) * s
    pts = lambda poly: " ".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in poly)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="100%" '
         f'font-family="Helvetica, Arial, sans-serif"><defs><clipPath id="int{id(p)}">'
         f'<rect x="{X(A)}" y="{Y(A)}" width="{(B_-A)*s}" height="{(B_-A)*s}"/></clipPath></defs>',
         f'<rect x="{X(A)}" y="{Y(A)}" width="{(B_-A)*s}" height="{(B_-A)*s}" fill="#e9f2e1"/>']
    for q, nome in ((E, "Ingresso in legno"), (An, "Annesso degli ospiti")):
        o.append(f'<rect x="{X(q[0])}" y="{Y(q[1])}" width="{(q[2]-q[0])*s}" height="{(q[3]-q[1])*s}" '
                 f'fill="#f1ece4" stroke="#8a7a66" stroke-width="2"/>')
        cx = X((q[0] + q[2]) / 2)
        if q is E:
            cy = Y((3.0 + q[3]) / 2)
            o.append(f'<text x="{cx}" y="{cy}" font-size="10" text-anchor="middle" fill="#5d5143" '
                     f'transform="rotate(-90 {cx} {cy})">{nome}</text>')
        else:
            cy = Y((q[1] + q[3]) / 2)
            o.append(f'<text x="{cx}" y="{cy}" font-size="11" text-anchor="middle" fill="#5d5143">{nome}'
                     f'<tspan x="{cx}" dy="13" font-size="9.5">(si può anche togliere)</tspan></text>')
    for k, poly in p.stanze.items():
        o.append(f'<polygon points="{pts(poly)}" fill="{COL[ZONA[k]]}" stroke="#333" stroke-width="1.6" '
                 f'stroke-linejoin="round"/>')
    if p.morso is not None:
        o.append(f'<polygon points="{pts(p.morso)}" fill="#e9f2e1" stroke="#333" stroke-width="2.2" '
                 f'clip-path="url(#int{id(p)})"/>')
        c, r = p.extra[1], p.extra[2]
        o.append(f'<rect x="{X(c[0]-0.7)}" y="{Y(c[1]-0.7)}" width="{1.4*s}" height="{1.4*s}" fill="#d9c9b0" '
                 f'stroke="#8a7a66"/><text x="{X(c[0])}" y="{Y(c[1]+1.25)}" font-size="9.5" '
                 f'text-anchor="middle" fill="#6b5a44">focolare</text>')
    q = p.sopp
    o.append(f'<rect x="{X(q[0])+3}" y="{Y(q[1])+3}" width="{(q[2]-q[0])*s-6}" height="{(q[3]-q[1])*s-6}" '
             f'fill="none" stroke="#b0412f" stroke-width="1.4" stroke-dasharray="6 4"/>')
    o.append(f'<text x="{X(q[0])+7}" y="{Y(q[1])+16}" font-size="9.5" fill="#b0412f">soppalco (studio)</text>')
    o.append(f'<path d="M{X(0)} {Y(0)}H{X(LATO)}V{Y(LATO)}H{X(0)}Z M{X(A)} {Y(A)}V{Y(B_)}H{X(B_)}V{Y(A)}Z" '
             f'fill="#555" fill-rule="evenodd"/>')
    gy0, gy1 = 7.70, 12.60
    o.append(f'<rect x="{X(0)}" y="{Y(gy0)}" width="{R*s}" height="{(gy1-gy0)*s}" fill="#fff" stroke="#555"/>')
    for i in range(9):
        yy = gy0 + 0.15 + i * 0.58
        o.append(f'<line x1="{X(0)}" y1="{Y(yy)}" x2="{X(R)}" y2="{Y(yy)}" stroke="#555" stroke-width="1.5"/>')
    o.append(f'<rect x="{X(2.45)}" y="{Y(B_)-0.5}" width="{4.5*s}" height="{R*s+1}" fill="#e9f2e1"/>')
    o.append(f'<text x="{X(4.7)}" y="{Y(LATO)+14}" font-size="10" text-anchor="middle" fill="#444">'
             f'apertura del recinto (resta)</text>')
    o.append(f'<text x="{X(-0.25)}" y="{Y(10.15)}" font-size="10" text-anchor="middle" fill="#444" '
             f'transform="rotate(-90 {X(-0.25)} {Y(10.15)})">graticcio (resta)</text>')
    for a, b, (xa, ya), (xb, yb) in p.porte:
        if b == "fuori":
            o.append(f'<line x1="{X(xa)}" y1="{Y(ya)}" x2="{X(xb)}" y2="{Y(yb)}" stroke="#fff" stroke-width="{R*s*2}"/>'
                     f'<line x1="{X(xa)}" y1="{Y(ya)}" x2="{X(xb)}" y2="{Y(yb)}" stroke="#c0392b" stroke-width="3"/>')
            ym = Y((ya + yb) / 2)
            o.append(f'<line x1="{X(15.35)}" y1="{ym}" x2="{X(14.55)}" y2="{ym}" stroke="#c0392b" stroke-width="3"/>'
                     f'<path d="M{X(14.55)} {ym} l9 -6 v12 Z" fill="#c0392b"/>')
        else:
            o.append(f'<line x1="{X(xa)}" y1="{Y(ya)}" x2="{X(xb)}" y2="{Y(yb)}" stroke="#fff" stroke-width="4.5"/>'
                     f'<line x1="{X(xa)}" y1="{Y(ya)}" x2="{X(xb)}" y2="{Y(yb)}" stroke="#333" stroke-width="1" '
                     f'stroke-dasharray="2 2"/>')
    m = p.maschere()
    for k in p.stanze:
        mk = m[k]
        xs, ys = GX[mk], GY[mk]
        sq = p.sopp
        ml = mk.copy()
        if k in ("SP", "K"):
            libero = mk & ~((GX > sq[0] - 0.9) & (GX < sq[2] + 0.9) & (GY > sq[1] - 0.9) & (GY < sq[3] + 0.9))
            if libero.sum() * PASSO ** 2 > 6:
                ml = libero
        cx, cy = centro(ml)
        w, h = xs.max() - xs.min(), ys.max() - ys.min()
        X0, Y0 = X(cx), Y(cy)
        verticale = w < 1.9 and h > w
        rot = f' transform="rotate(-90 {X0} {Y0})"' if verticale else ""
        lungo, corto = (h, w) if verticale else (w, h)
        poly = p.stanze[k]
        rettangolo = assiale(poly) and len(poly) == 4 and abs(area_poly(poly) - p.area(k)) < 0.05
        misure = f"{num(w)} × {num(h)} · " if rettangolo else ""
        testo = f"{misure}{num(p.area(k), 1)} m²"
        fs = 11 if lungo * s > 70 else 9.5
        if corto < 1.4:
            riga = f"{CORTI[k]} · {testo}"
            fs = min(fs, (lungo * s - 8) / (len(riga) * 0.5))
            o.append(f'<text x="{X0}" y="{Y0 + 4}" font-size="{fs:.1f}" font-weight="bold" text-anchor="middle" '
                     f'fill="#222"{rot}>{CORTI[k]}<tspan font-weight="normal" font-size="{fs-1.5:.1f}"> · {testo}'
                     f'</tspan></text>')
        else:
            fs = min(fs, (lungo * s - 6) / (max(len(CORTI[k]), len(testo)) * 0.56))
            o.append(f'<text x="{X0}" y="{Y0 - 2}" font-size="{fs:.1f}" font-weight="bold" text-anchor="middle" '
                     f'fill="#222"{rot}>{CORTI[k]}<tspan x="{X0}" dy="{fs+2}" font-weight="normal" '
                     f'font-size="{fs-1.5:.1f}">{testo}</tspan></text>')
    pat = p.patio()
    bp = centro(pat)
    bp = (bp[0], bp[1] - 0.6)
    if p.morso is not None:
        bp = (p.extra[1][0], p.extra[1][1] - 2.2)
    ap = pat.sum() * PASSO ** 2
    o.append(f'<text x="{X(bp[0])}" y="{Y(bp[1])}" font-size="15" font-weight="bold" text-anchor="middle" '
             f'fill="#4c7a34">PATIO<tspan x="{X(bp[0])}" dy="17" font-size="11.5" font-weight="normal">'
             f'{num(ap,1)} m² (Aalto: {num(PATIO_AALTO,1)})</tspan></text>')
    nx, ny = X(x1 - 0.5), Y(y0 + 0.4)
    o.append(f'<path d="M{nx} {ny} l-7 20 l7 -5 l7 5 Z" fill="#333"/><text x="{nx}" y="{ny+33}" '
             f'font-size="11" text-anchor="middle">N</text>')
    sx, sy = X(x0 + 0.5), Y(y1 - 0.45)
    for i in range(5):
        o.append(f'<rect x="{sx + i*s}" y="{sy}" width="{s}" height="5" fill="{"#333" if i % 2 == 0 else "#fff"}" '
                 f'stroke="#333" stroke-width="0.8"/>')
    o.append(f'<text x="{sx}" y="{sy-4}" font-size="9.5">0</text><text x="{sx+5*s}" y="{sy-4}" '
             f'font-size="9.5" text-anchor="middle">5 m</text></svg>')
    return "".join(o)


CSS = """
@page { size: A4; margin: 13mm 14mm 13mm 14mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pianta { width: 84%; margin: 2pt auto 0; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 9.6pt; color: #222; line-height: 1.34; margin: 0; }
h1 { font-size: 19pt; margin: 0 0 4pt; } h2 { font-size: 14.5pt; margin: 0 0 4pt; color: #8e2f22; }
h3 { font-size: 11pt; margin: 9pt 0 3pt; } p { margin: 3pt 0 5pt; }
.pagina { page-break-after: always; } .pagina:last-child { page-break-after: auto; }
.sotto { color: #666; margin-bottom: 8pt; }
ul { margin: 2pt 0 4pt; padding-left: 15pt; } li { margin: 1.5pt 0; }
.box { border-left: 4px solid #4c7a34; background: #f1f7ec; padding: 5pt 9pt; margin: 6pt 0; }
.due { display: flex; gap: 12pt; } .due > div { flex: 1; }
table { border-collapse: collapse; font-size: 9pt; width: 100%; margin-top: 4pt; }
th, td { border: 1px solid #ccc; padding: 2.5pt 5pt; text-align: left; } th { background: #f2f2f2; }
td.n, th.n { text-align: right; }
.leg span { display: inline-block; width: 11pt; height: 9pt; border: 1px solid #333; vertical-align: -1pt; margin: 0 3pt 0 9pt; }
"""


def html():
    r = ['<div class="pagina">',
         "<h1>Esercizio 4 · Altre quattro proposte, con geometrie diverse</h1>",
         '<p class="sotto">Casa sperimentale di Aalto a Muuratsalo · nuova disposizione (punto 5) · '
         "seguito delle proposte 1-4</p>",
         "<p>Le proposte 1-4 spostavano rettangoli. Queste quattro partono invece da un'idea "
         "geometrica: un cerchio, una rotazione, una curva, una diagonale. È il tema della lezione "
         "del 10 novembre: la geometria euclidea del quadrato (il recinto) contro la geometria "
         "organica di Aalto. Tutte tengono l'ingresso principale in un angolo.</p>",
         "<h3>Le regole restano le stesse</h3><ul>"
         "<li>Il recinto non si tocca; graticcio e apertura sud restano sul patio.</li>"
         "<li>Ogni stanza tiene la sua superficie (entro il 5%); il patio resta di circa 86,5 m² ed è un "
         "solo vuoto.</li>"
         "<li>L'ingresso è nell'angolo e dà sul distributivo; camere e bagno si raggiungono dal "
         "distributivo; soggiorno e cucina senza passare da una camera.</li>"
         "<li>Il soppalco tiene la sua superficie (14,4 m²) e sta sopra la zona giorno.</li></ul>",
         "<p>Un programma ha controllato tutto su una griglia di 2,5 cm: superfici, sovrapposizioni, "
         "patio in un solo pezzo, porte tra le stanze giuste, percorsi. Le stanze con pareti curve o "
         "inclinate hanno solo la superficie, perché non hanno due misure semplici.</p>",
         '<h3>Come leggere le piante</h3><p class="leg"><span style="background:#f6d5cf"></span>zona giorno'
         '<span style="background:#d3e0f3"></span>zona notte<span style="background:#e3d5ef"></span>bagno'
         '<span style="background:#fbecb3"></span>ingresso e corridoio<span style="background:#e9f2e1"></span>patio</p>'
         "<p>Freccia rossa: l'ingresso. Righe tratteggiate: porte interne. Riquadro rosso tratteggiato: "
         "il soppalco. Misure in metri, dentro le stanze.</p>",
         "<h3>In breve</h3><ul>"
         "<li><b>5 · Il patio rotondo</b>: il vuoto diventa un cerchio con il focolare al centro.</li>"
         "<li><b>6 · I denti di sega</b>: le pareti sul patio ruotano di 25° e guardano tutte il lago.</li>"
         "<li><b>7 · La parete a onda</b>: la L di Aalto con il fronte del soggiorno curvo.</li>"
         "<li><b>8 · L'ingresso in diagonale</b>: dall'angolo parte una galleria a 45° che distribuisce "
         "tutta la casa.</li></ul></div>"]
    for n, p in enumerate(PROPOSTE, 5):
        err, ap = controlla(p)
        if err:
            raise SystemExit(f"Proposta {n}: {err}")
        r += ['<div class="pagina">', f"<h2>Proposta {n} · {p.titolo}</h2>", f"<p>{p.idea}</p>",
              '<div class="pianta">' + svg_pianta(p) + "</div>",
              f"<h3>Il percorso dall'ingresso</h3><p>{p.percorso}</p>",
              '<div class="due"><div><h3>Pro</h3><ul>' + "".join(f"<li>{x}</li>" for x in p.pro) +
              '</ul></div><div><h3>Contro</h3><ul>' + "".join(f"<li>{x}</li>" for x in p.contro) +
              "</ul></div></div>", f"<h3>Soppalco e tetto</h3><p>{p.tetto}</p>", "</div>"]
    r.append('<div class="pagina"><h2>Controllo delle superfici</h2><p>Superfici in m², misurate '
             "dentro le stanze. Ingresso e corridoio si controllano insieme.</p><table><tr><th>Stanza</th>"
             "<th class='n'>Aalto</th>" + "".join(f"<th class='n'>Prop. {n}</th>" for n in range(5, 9)) + "</tr>")
    for k in AALTO:
        r.append(f"<tr><td>{NOMI[k]}</td><td class='n'>{num(AALTO[k],1)}</td>" +
                 "".join(f"<td class='n'>{num(p.area(k),1)}</td>" for p in PROPOSTE) + "</tr>")
    r.append(f"<tr><th>Patio</th><th class='n'>{num(PATIO_AALTO,1)}</th>" +
             "".join(f"<th class='n'>{num(controlla(p)[1],1)}</th>" for p in PROPOSTE) + "</tr></table>")
    r.append('<div class="box"><b>Controllato in tutte e quattro:</b> stanze dentro il recinto e senza '
             "sovrapposizioni; patio in un solo pezzo, con graticcio e apertura sud; ingresso nell'angolo "
             "sul distributivo; camere e bagno raggiungibili dal distributivo; soggiorno e cucina "
             "raggiungibili senza passare da una camera; soppalco dentro la zona giorno.</div>")
    r.append("<h3>Quale scegliere?</h3><p>La <b>5</b> è la più coraggiosa e la più facile da "
             "raccontare: il vuoto è una forma, non un avanzo, e il focolare di Aalto diventa il centro. "
             "Costa fatica nel plastico (le pareti curve). La <b>6</b> è la più sicura: tiene "
             "l'organizzazione migliore delle prime quattro (la proposta 2) e cambia il carattere con "
             "una sola regola, tutta di pezzi dritti. La <b>7</b> è la più vicina ad Aalto come "
             "linguaggio. La <b>8</b> è la più «da architetto» come ragionamento sul quadrato, ma ha la "
             "cucina separata dal pranzo dalla galleria.</p>"
             "<h3>Nel plastico</h3><ul><li>Curve (5 e 7): cartoncino sottile curvato, oppure Poliplat "
             "inciso a righe sul retro ogni 3-4 mm, così si piega senza spezzarsi.</li>"
             "<li>Pareti inclinate (6 e 8): pezzi dritti; disegna gli angoli sulla base con la squadra "
             "prima di incollare.</li><li>Il tetto nuovo delle proposte 5 e 6 va disegnato anche in "
             "sezione (almeno 2,20 m sopra e sotto il soppalco).</li></ul></div>")
    return (f"<!doctype html><html lang='it'><head><meta charset='utf-8'><title>caricamento</title>"
            f"<style>{CSS}</style></head><body>{''.join(r)}"
            f"<script>window.onload=function(){{document.title='PRONTO'}}</script></body></html>")


if __name__ == "__main__" and len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(html())
