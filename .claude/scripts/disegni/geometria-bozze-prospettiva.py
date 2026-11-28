"""Schemi per le bozze di geometria descrittiva sulla prospettiva (13-..., 14-..., 16-...).

Gli schemi delle sbobine (geometria-13-14.py, geometria-16.py) si riusano cosi' come sono; qui ci sono:
- le viste nello spazio (punto di vista, quadro, geometrale, orizzonte, fondamentale, O0, O*, tracce e fughe,
  traccia del piano verticale, occhio di formica);
- il punto di misura passo per passo e il perche' funziona (in pianta);
- gli esercizi-tipo risolti delle tre bozze.

Convenzioni del foglio (come nelle sbobine): l'orizzonte e' orizzontale a quota 0; la fondamentale sta sotto,
alla distanza h (l'altezza dell'occhio); O0 e' il punto principale sull'orizzonte, O* sta sotto O0 alla
distanza d. Un punto del geometrale ha coordinate (X, Y): X lungo il quadro, Y = profondita' oltre il quadro.
La sua prospettiva, a quota z, e' (X d/(d+Y), (z-h) d/(d+Y)): ogni costruzione e' controllata con questi conti.
Nelle viste nello spazio un punto e' (X, Y, Z), con Z la quota.

Ogni volta che si cambia un disegno alzare VER (Obsidian non ricarica le immagini con lo stesso nome),
cancellare i vecchi SVG e aggiornare gli embed nelle bozze.

Usa disegni_monge.py senza modificarlo.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, interseca, COLORI

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"
CAM = (1.0, -0.7, 1.2)
VER = ""          # suffisso di versione per i nomi dei file (es. "-v2")


def nome(n):
    return OUT + n + VER + ".svg"


def vicino(p, q, tol=0.01):
    return math.dist(p, q) < tol


def arco(f, c, r, a0, a1, colore="grigio", spessore=1, tratteggio="4,3", n=60):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append(f._s((c[0] + r * math.cos(a), c[1] + r * math.sin(a))))
    dd = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    f.parti.append(f'<path d="{dd}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                   f'stroke-width="{spessore}"{dash}/>')


def prosp(X, Y, d, h, z=0.0):
    """Prospettiva del punto (X, Y) del geometrale a quota z: l'occhio e' a quota h."""
    k = d / (d + Y)
    return (X * k, (z - h) * k)


def ang_retto(f, V, P, Q, lato=11):
    u = ((P[0] - V[0]) / math.dist(P, V), (P[1] - V[1]) / math.dist(P, V))
    w = ((Q[0] - V[0]) / math.dist(Q, V), (Q[1] - V[1]) / math.dist(Q, V))
    f.angolo_retto(V, u, w, lato)


def gradi(c, p):
    return math.degrees(math.atan2(p[1] - c[1], p[0] - c[0]))


# ---------------------------------------------------------------------------------------------
# Vista nello spazio: assonometria semplice. X verso destra (un po' in basso), Y (profondita')
# verso destra in alto, Z in alto. Il quadro e' il piano Y = 0, il geometrale il piano Z = 0.
# ---------------------------------------------------------------------------------------------
class Spazio:
    """Proiezione ortogonale vista da una camera in direzione w (dalla scena verso chi guarda)."""

    def __init__(self, f, w=None):
        w = w or CAM
        n = math.sqrt(sum(c * c for c in w))
        fw = [-c / n for c in w]
        r = (fw[1], -fw[0], 0.0)
        rn = math.hypot(r[0], r[1])
        self.r = (r[0] / rn, r[1] / rn, 0.0)
        self.u = (self.r[1] * fw[2] - self.r[2] * fw[1], self.r[2] * fw[0] - self.r[0] * fw[2],
                  self.r[0] * fw[1] - self.r[1] * fw[0])
        self.f = f
        self.w = tuple(c / n for c in w)

    def scatola(self, base, H, colore="blu", riempi=None):
        """Parallelepipedo con base (4 punti 3D a quota 0, in ordine) e altezza H: spigoli nascosti tratteggiati."""
        top = [(q[0], q[1], q[2] + H) for q in base]
        cx = sum(q[0] for q in base) / 4
        cy = sum(q[1] for q in base) / 4
        facce = {"giu": (0, 0, -1), "su": (0, 0, 1)}
        lat = []
        for i in range(4):
            a, b = base[i], base[(i + 1) % 4]
            nx, ny = (b[1] - a[1]), -(b[0] - a[0])
            mx, my = (a[0] + b[0]) / 2 - cx, (a[1] + b[1]) / 2 - cy
            if nx * mx + ny * my < 0:
                nx, ny = -nx, -ny
            lat.append((nx, ny, 0))
        vis = lambda nrm: sum(nrm[j] * self.w[j] for j in range(3)) > 0
        for i in range(4):
            j = (i + 1) % 4
            # spigolo di base i-j: facce giu e laterale i; spigolo in alto: su e laterale i
            for (a, b, f1) in [(base[i], base[j], facce["giu"]), (top[i], top[j], facce["su"])]:
                v = vis(f1) or vis(lat[i])
                self.linea(a, b, colore, 1.8 if v else 1, None if v else "4,3")
            # spigolo verticale i: facce laterali i-1 e i
            v = vis(lat[i]) or vis(lat[i - 1])
            self.linea(base[i], top[i], colore, 1.8 if v else 1, None if v else "4,3")
        if riempi is not None:
            self.poligono(riempi, colore, 0.18)

    def p(self, P):
        return (sum(P[j] * self.r[j] for j in range(3)), sum(P[j] * self.u[j] for j in range(3)))

    def linea(self, a, b, colore="nero", spessore=1.4, tratteggio=None):
        self.f._linea(self.p(a), self.p(b), colore, spessore, tratteggio)

    def poligono(self, punti, colore, opacita=0.12, bordo=None, spessore=1):
        pts = " ".join("{:.1f},{:.1f}".format(*self.f._s(self.p(q))) for q in punti)
        c = COLORI.get(colore, colore)
        b = f' stroke="{COLORI.get(bordo, bordo)}" stroke-width="{spessore}"' if bordo else ' stroke="none"'
        self.f.parti.append(f'<polygon points="{pts}" fill="{c}" fill-opacity="{opacita}"{b}/>')

    def punto(self, P, etichetta=None, dx=6, dy=-6, colore="nero"):
        self.f.punto(self.p(P), etichetta, dx, dy, colore)

    def testo(self, P, t, dx=6, dy=-6, colore="nero", dimensione=14, corsivo=True):
        self.f.testo(self.p(P), t, dx, dy, colore, dimensione, corsivo)

    def arco(self, c, e1, e2, r, a0, a1, colore="grigio", spessore=1.2, tratteggio="5,3", n=50):
        pts = []
        for i in range(n + 1):
            a = math.radians(a0 + (a1 - a0) * i / n)
            q = tuple(c[j] + r * (math.cos(a) * e1[j] + math.sin(a) * e2[j]) for j in range(3))
            pts.append(self.f._s(self.p(q)))
        dd = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
        self.f.parti.append(f'<path d="{dd}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                            f'stroke-width="{spessore}"{dash}/>')


def buca_quadro(O, P):
    """Dove il raggio da O a P buca il quadro Y = 0."""
    t = -O[1] / (P[1] - O[1])
    return tuple(O[j] + t * (P[j] - O[j]) for j in range(3))


# ---------------------------------------------------------------------------------------------
# Solidi (parallelepipedi) per gli esercizi: visibilita' degli spigoli con il raggio visivo
# ---------------------------------------------------------------------------------------------
class Scatola:
    """Parallelepipedo appoggiato sul geometrale: base P0 + u ur + v un (0<=u<=L, 0<=v<=W), quota 0..H."""

    def __init__(self, P0, ur, un, L, W, H, z0=0.0):
        self.P0, self.ur, self.un, self.L, self.W, self.H, self.z0 = P0, ur, un, L, W, H, z0

    def loc(self, P):
        dx, dy = P[0] - self.P0[0], P[1] - self.P0[1]
        return (dx * self.ur[0] + dy * self.ur[1], dx * self.un[0] + dy * self.un[1], P[2] - self.z0)

    def vertice(self, u, v, z):
        return (self.P0[0] + u * self.ur[0] + v * self.un[0], self.P0[1] + u * self.ur[1] + v * self.un[1],
                self.z0 + z)

    def spigoli(self):
        L, W, H = self.L, self.W, self.H
        c = [(0, 0), (L, 0), (L, W), (0, W)]
        out = []
        for i in range(4):
            a, b = c[i], c[(i + 1) % 4]
            out.append((self.vertice(*a, 0), self.vertice(*b, 0)))
            out.append((self.vertice(*a, H), self.vertice(*b, H)))
            out.append((self.vertice(*a, 0), self.vertice(*a, H)))
        return out

    def blocca(self, E, Q, eps=1e-3):
        """Il segmento da E a Q (escluso l'ultimo tratto) passa dentro la scatola?"""
        e, q = self.loc(E), self.loc(Q)
        t0, t1 = 0.0, 1.0 - 1e-4
        for k, (lo, hi) in enumerate([(0, self.L), (0, self.W), (0, self.H)]):
            lo, hi = lo + eps, hi - eps
            dk = q[k] - e[k]
            if abs(dk) < 1e-12:
                if e[k] < lo or e[k] > hi:
                    return False
                continue
            ta, tb = (lo - e[k]) / dk, (hi - e[k]) / dk
            if ta > tb:
                ta, tb = tb, ta
            t0, t1 = max(t0, ta), min(t1, tb)
            if t0 >= t1:
                return False
        return True


def disegna_scatole(f, scatole, E, proj, colore="rosso", n=60, spessore=2):
    """Disegna gli spigoli: visibili pieni, nascosti tratteggiati. proj: punto 3D -> foglio."""
    for s in scatole:
        for a, b in s.spigoli():
            runs, cur, start = [], None, 0
            for i in range(n + 1):
                t = i / n
                P = tuple(a[j] + t * (b[j] - a[j]) for j in range(3))
                vis = not any(o.blocca(E, P) for o in scatole)
                if cur is None:
                    cur, start = vis, t
                elif vis != cur:
                    runs.append((start, t, cur))
                    cur, start = vis, t
            runs.append((start, 1.0, cur))
            for t0, t1, vis in runs:
                P0 = tuple(a[j] + t0 * (b[j] - a[j]) for j in range(3))
                P1 = tuple(a[j] + t1 * (b[j] - a[j]) for j in range(3))
                if math.dist(proj(P0), proj(P1)) < 0.5:
                    continue
                if vis:
                    f._linea(proj(P0), proj(P1), colore, spessore)
                else:
                    f._linea(proj(P0), proj(P1), colore, 1, "4,3")


# =============================================================================================
# BOZZA 13
# =============================================================================================

# --- 13.1 Nello spazio: gli elementi della prospettiva ---------------------------------------
d, h = 170, 85
f = Figura(760, 530, 260, "Nello spazio: gli elementi della prospettiva", x0=330)
S = Spazio(f)
Xa, Xb = -110, 230
geo = [(Xa - 20, -d - 20, 0), (Xb, -d - 20, 0), (Xb, 180, 0), (Xa - 20, 180, 0)]
S.poligono(geo, "#c9b98f", 0.18, "#b5a77f")
S.testo((Xb, 170, 0), "geometrale", dx=-90, dy=-4, colore="#8a7a4f", dimensione=13, corsivo=False)
quadro = [(Xa, 0, 0), (Xb, 0, 0), (Xb, 0, 200), (Xa, 0, 200)]
S.poligono(quadro, "#7fa6c9", 0.22, "#5d88b0", 1.2)
S.testo((Xa, 0, 200), "quadro", dx=4, dy=16, colore="#3f6b94", dimensione=13, corsivo=False)
# fondamentale e orizzonte
S.linea((Xa, 0, 0), (Xb, 0, 0), "nero", 2.2)
S.testo((Xb, 0, 0), "fondamentale", dx=6, dy=10, dimensione=13, corsivo=False)
S.linea((Xa, 0, h), (Xb, 0, h), "nero", 2.2)
S.testo((Xa, 0, h), "orizzonte", dx=-66, dy=4, dimensione=13, corsivo=False)
# piano d'orizzonte (orizzontale, all'altezza dell'occhio): solo il contorno
S.poligono([(Xa, -d - 20, h), (Xb, -d - 20, h), (Xb, 0, h), (Xa, 0, h)], "#d9a441", 0.08, "#d9a441")
S.testo((Xa, -d - 20, h), "piano d'orizzonte", dx=4, dy=16, colore="#b07d1e", dimensione=12, corsivo=False)
# punto di vista
O = (0, -d, h)
O0 = (0, 0, h)
S.linea((0, -d, 0), O, "grigio", 3)
S.punto(O, "O", dx=-18, dy=-6)
S.testo((0, -d, h / 2), "h", dx=-16, dy=4, colore="grigio")
S.linea(O, O0, "nero", 1.2, "6,4")
S.testo(((0, -d / 2, h)), "d", dx=-4, dy=-8)
S.punto(O0, "O_0", dx=4, dy=-8)
# un punto P del geometrale e il suo raggio proiettante
P = (120, 150, 0)
Pp = buca_quadro(O, P)
S.linea(O, P, "rosso", 1.2, "5,3")
S.punto(P, "P", dx=6, dy=4, colore="rosso")
S.punto(Pp, "P′", dx=6, dy=-6, colore="rosso")
# il piede di P sotto la retta d'orizzonte: P' sta tra orizzonte e fondamentale
f.nota(16, 502, "O guarda il quadro da distanza d, con l'occhio all'altezza h. O₀ è il piede della perpendicolare da O al quadro: sta sull'orizzonte.", 13)
f.nota(16, 520, "Il raggio da O al punto P del geometrale buca il quadro in P′: P′ è la prospettiva di P.", 13)
f.salva(nome("b13-spazio-elementi-della-prospettiva"))

# --- 13.2 Nello spazio: il ribaltamento di O, il cerchio di distanza, i punti di distanza ----
d, h = 150, 150
f = Figura(760, 430, 330, "Nello spazio: O ribaltato sul quadro diventa O*, il cerchio di distanza", x0=300)
S = Spazio(f, w=(0.35, -1.0, 0.45))
Xa, Xb = -230, 230
S.poligono([(Xa, 0, -10), (Xb, 0, -10), (Xb, 0, 310), (Xa, 0, 310)], "#7fa6c9", 0.20, "#5d88b0", 1.2)
S.testo((Xa, 0, 310), "quadro", dx=4, dy=16, colore="#3f6b94", dimensione=13, corsivo=False)
S.linea((Xa, 0, h), (Xb, 0, h), "nero", 2.2)
S.testo((Xa, 0, h), "orizzonte", dx=-66, dy=4, dimensione=13, corsivo=False)
S.poligono([(Xa, -d - 20, h), (Xb, -d - 20, h), (Xb, 0, h), (Xa, 0, h)], "#d9a441", 0.10, "#d9a441")
S.testo((Xa, -d - 20, h), "piano d'orizzonte", dx=4, dy=-6, colore="#b07d1e", dimensione=12, corsivo=False)
O = (0, -d, h)
O0 = (0, 0, h)
Os3 = (0, 0, h - d)
S.punto(O, "O", dx=-20, dy=12)
S.linea(O, O0, "nero", 1.2, "6,4")
S.testo((0, -d / 2, h), "d", dx=-14, dy=-4)
S.punto(O0, "O_0", dx=-26, dy=-6)
# le rette a 45 gradi da O, nel piano d'orizzonte, arrivano sull'orizzonte a distanza d da O0
Dd3, Ds3 = (d, 0, h), (-d, 0, h)
S.linea(O, Dd3, "verde", 1.6)
S.linea(O, Ds3, "verde", 1.6)
S.punto(Dd3, "D_d", dx=4, dy=-8, colore="verde")
S.punto(Ds3, "D_s", dx=-26, dy=-8, colore="verde")
# il ribaltamento intorno all'orizzonte: O scende sul quadro in O*
S.arco(O0, (0, -1, 0), (0, 0, -1), d, 0, 90, colore="arancio", spessore=1.6, tratteggio="6,3")
S.linea(O0, Os3, "arancio", 1.2, "6,4")
S.punto(Os3, "O*", dx=8, dy=4, colore="arancio")
# il cerchio di distanza sul quadro: centro O0, raggio d
S.arco(O0, (1, 0, 0), (0, 0, 1), d, 0, 360, colore="grigio", spessore=1.1, tratteggio="2,4", n=90)
S.testo((-d * 0.72, 0, h + d * 0.69), "cerchio di distanza", dx=-40, dy=-8, colore="grigio", dimensione=12, corsivo=False)
# le stesse rette ribaltate: da O* a D_d e D_s
S.linea(Os3, Dd3, "verde", 1, "4,3")
S.linea(Os3, Ds3, "verde", 1, "4,3")
f.nota(16, 402, "Il piano d'orizzonte gira intorno all'orizzonte e si appoggia sul quadro: O va in O*, sotto O₀ alla distanza d.", 13)
f.nota(16, 420, "Le rette da O a 45° arrivano sull'orizzonte nei due punti di distanza, dove l'orizzonte incontra il cerchio di distanza.", 13)
f.salva(nome("b13-spazio-ribaltamento-di-o-e-cerchio-di-distanza"))

# --- 13.3 Nello spazio: traccia e fuga di una retta del geometrale -----------------------------
d, h = 170, 85
f = Figura(760, 540, 260, "Nello spazio: la traccia e la fuga di una retta del geometrale", x0=330)
S = Spazio(f)
Xa, Xb = -150, 260
S.poligono([(Xa - 20, -d - 20, 0), (Xb, -d - 20, 0), (Xb, 180, 0), (Xa - 20, 180, 0)], "#c9b98f", 0.18, "#b5a77f")
S.testo((Xb, 170, 0), "geometrale", dx=-90, dy=-4, colore="#8a7a4f", dimensione=13, corsivo=False)
S.poligono([(Xa, 0, 0), (Xb, 0, 0), (Xb, 0, 190), (Xa, 0, 190)], "#7fa6c9", 0.22, "#5d88b0", 1.2)
S.testo((Xa, 0, 190), "quadro", dx=4, dy=16, colore="#3f6b94", dimensione=13, corsivo=False)
S.linea((Xa, 0, 0), (Xb, 0, 0), "nero", 2.2)
S.testo((Xb, 0, 0), "fondamentale", dx=6, dy=10, dimensione=13, corsivo=False)
S.linea((Xa, 0, h), (Xb, 0, h), "nero", 2.2)
S.testo((Xa, 0, h), "orizzonte", dx=-66, dy=4, dimensione=13, corsivo=False)
O = (0, -d, h)
S.linea((0, -d, 0), O, "grigio", 3)
S.punto(O, "O", dx=-18, dy=-6)
S.punto((0, 0, h), "O_0", dx=6, dy=16)
# retta r del geometrale, inclinata sul quadro: traccia T_r sulla fondamentale
th = math.radians(42)
Tr3 = (-60, 0, 0)
ur3 = (math.cos(th), math.sin(th), 0)
r_end = (Tr3[0] + 290 * ur3[0], 290 * ur3[1], 0)
S.linea(Tr3, r_end, "blu", 2.4)
S.testo(r_end, "r", dx=4, dy=-4, colore="blu")
S.punto(Tr3, "T_r", dx=-24, dy=14, colore="blu")
# la parallela a r per O arriva sull'orizzonte in F_r
Fr3 = (d / math.tan(th), 0, h)
assert abs((Fr3[0] - O[0]) * ur3[1] - (Fr3[1] - O[1]) * ur3[0]) < 1e-9
S.linea(O, Fr3, "verde", 1.6, "6,3")
S.punto(Fr3, "F_r", dx=4, dy=-8, colore="verde")
S.testo(((O[0] + Fr3[0]) / 2, (O[1] + Fr3[1]) / 2, h), "parallela a r per O", dx=-110, dy=16, colore="verde",
        dimensione=12, corsivo=False)
# r' sul quadro
S.linea(Tr3, Fr3, "rosso", 2.4)
# un punto A di r e la sua prospettiva sta su r'
A3 = (Tr3[0] + 170 * ur3[0], 170 * ur3[1], 0)
Ap3 = buca_quadro(O, A3)
# controllo: A' sta sulla retta T_r F_r (nel quadro, coordinate X e Z)
assert abs((Ap3[0] - Tr3[0]) * (Fr3[2] - Tr3[2]) - (Ap3[2] - Tr3[2]) * (Fr3[0] - Tr3[0])) < 1e-6
S.linea(O, A3, "grigio", 1, "4,3")
S.punto(A3, "A", dx=6, dy=4, colore="blu")
S.punto(Ap3, "A′", dx=-4, dy=-10, colore="rosso")
S.testo(((Tr3[0] + Fr3[0]) / 2, 0, h / 2), "r′", dx=10, dy=12, colore="rosso")
# retta p perpendicolare al quadro: la sua fuga e' O0
Tp3 = (-120, 0, 0)
S.linea(Tp3, (-120, 220, 0), "viola", 2)
S.testo((-120, 220, 0), "p", dx=6, dy=0, colore="viola")
S.linea(Tp3, (0, 0, h), "viola", 1.6, "6,3")
S.punto(Tp3, "T_p", dx=-26, dy=12, colore="viola")
S.testo((-60, 0, h / 2), "p′", dx=-4, dy=18, colore="viola")
f.nota(16, 494, "La traccia Tᵣ è dove r incontra il quadro (sulla fondamentale).", 13)
f.nota(16, 512, "La fuga Fᵣ è dove la parallela a r per O incontra il quadro (sull'orizzonte). r′ congiunge traccia e fuga:", 13)
f.nota(16, 530, "ogni punto A di r ha la prospettiva A′ su r′. La retta p, perpendicolare al quadro, ha la fuga in O₀.", 13)
f.salva(nome("b13-spazio-traccia-e-fuga-di-una-retta"))

# --- 13.4 Esercizio: la pianta di un rettangolo inclinato sul quadro, con il metodo della pianta ---
d, h = 170, 90
th = math.radians(35)
ur = (math.cos(th), math.sin(th))
un = (-math.sin(th), math.cos(th))
A = (-30, 0)
AB, AD = 150, 90
B = (A[0] + AB * ur[0], A[1] + AB * ur[1])
D = (A[0] + AD * un[0], A[1] + AD * un[1])
C = (B[0] + AD * un[0], B[1] + AD * un[1])
O = (0, -d)
Fr = (d / math.tan(th), 0)
Fn = (-d * math.tan(th), 0)
# le fughe: la parallela per O a r e a n incontra il quadro (in pianta) sull'orizzonte
assert abs((Fr[0] - O[0]) * ur[1] - (Fr[1] - O[1]) * ur[0]) < 1e-9
assert abs((Fn[0] - O[0]) * un[1] - (Fn[1] - O[1]) * un[0]) < 1e-9
Ap, Bp, Cp, Dp = (prosp(*q, d, h) for q in (A, B, C, D))
assert vicino(Ap, (A[0], -h))


def piede(q):
    """Dove il raggio proiettante da O al punto q (in pianta) incontra il quadro."""
    return interseca(O, q, (-1, 0), (1, 0))


KB, KC, KD = piede(B), piede(C), piede(D)
assert vicino(interseca(Ap, Fr, KB, (KB[0], -h)), Bp)
assert vicino(interseca(Ap, Fn, KD, (KD[0], -h)), Dp)
assert vicino(interseca(Bp, Fn, Dp, Fr), Cp)
assert abs(KC[0] - Cp[0]) < 1e-9

f = Figura(800, 440, 200, "Esercizio: il rettangolo ABCD con il metodo della pianta", x0=330)
f._linea((-320, 0), (460, 0), "nero", 1.6)
f.testo((-320, 0), "orizzonte = quadro in pianta", dx=2, dy=-8, dimensione=13, corsivo=False)
f._linea((-320, -h), (460, -h), "nero", 1.6)
f.testo((-320, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
f.punto((0, 0), "O_0", dx=4, dy=16)
f.richiamo(0, 0, -d)
f.punto(O, "O ≡ O*", dx=8, dy=4)
# pianta
f.figura([A, B, C, D], "blu")
for q, n_, dx, dy in [(A, "A", 6, -8), (B, "B", 6, 2), (C, "C", 4, -6), (D, "D", -18, -2)]:
    f.punto(q, n_, dx, dy, "blu")
f.testo(((A[0] + B[0]) / 2, (A[1] + B[1]) / 2), "r", dx=4, dy=14, colore="blu")
f.testo(((A[0] + D[0]) / 2, (A[1] + D[1]) / 2), "n", dx=-16, dy=0, colore="blu")
# le parallele per O: fughe
f._linea(O, Fr, "verde", 1.3, "6,3")
f._linea(O, Fn, "verde", 1.3, "6,3")
ang_retto(f, O, Fr, Fn)
f.punto(Fr, "F_r", dx=4, dy=-8, colore="verde")
f.punto(Fn, "F_n", dx=-24, dy=-8, colore="verde")
# raggi proiettanti e verticali
for q, K in [(B, KB), (C, KC), (D, KD)]:
    f.costruzione(O, q)
    f._linea(K, (K[0], min(-h + 6, prosp(*q, d, h)[1] - 6)), "rosso", 1, "4,3")
    f.punto(K, None)
f.richiamo(A[0], 0, -h)
# prospettiva
f.retta(Ap, Fr, "rosso", 1.2)
f.retta(Ap, Fn, "rosso", 1.2)
f._linea(Bp, Fn, "grigio", 0.9, "2,3")
f._linea(Dp, Fr, "grigio", 0.9, "2,3")
f.figura([Ap, Bp, Cp, Dp], "rosso")
f.punto(Ap, "A′", dx=-6, dy=18, colore="rosso")
f.punto(Bp, "B′", dx=8, dy=10, colore="rosso")
f.punto(Cp, "C′", dx=-4, dy=-10, colore="rosso")
f.punto(Dp, "D′", dx=-22, dy=10, colore="rosso")
f.nota(16, 412, "A sta sul quadro: A′ è sulla fondamentale ed è la traccia di r e di n. Le fughe si trovano con le parallele per O.", 13)
f.nota(16, 430, "B′ e D′ con i raggi proiettanti e le verticali; C′ dove B′Fₙ incontra D′Fᵣ (controllo: sta sulla verticale del raggio OC).", 13)
f.salva(nome("b13-esercizio-rettangolo-metodo-della-pianta"))


# =============================================================================================
# BOZZA 14
# =============================================================================================

# --- 14.1 Nello spazio: l'altezza vera sulla traccia del piano verticale ------------------------
d, h = 170, 85
f = Figura(760, 540, 270, "Nello spazio: sulla traccia del piano verticale le altezze sono vere", x0=330)
S = Spazio(f)
Xa, Xb = -150, 260
S.poligono([(Xa - 20, -d - 20, 0), (Xb, -d - 20, 0), (Xb, 180, 0), (Xa - 20, 180, 0)], "#c9b98f", 0.18, "#b5a77f")
S.testo((Xb, 170, 0), "geometrale", dx=-90, dy=-4, colore="#8a7a4f", dimensione=13, corsivo=False)
S.poligono([(Xa, 0, 0), (Xb, 0, 0), (Xb, 0, 190), (Xa, 0, 190)], "#7fa6c9", 0.22, "#5d88b0", 1.2)
S.testo((Xa, 0, 190), "quadro", dx=4, dy=16, colore="#3f6b94", dimensione=13, corsivo=False)
S.linea((Xa, 0, 0), (Xb, 0, 0), "nero", 2.2)
S.testo((Xb, 0, 0), "fondamentale", dx=6, dy=10, dimensione=13, corsivo=False)
S.linea((Xa, 0, h), (Xb, 0, h), "nero", 1.4)
S.testo((Xa, 0, h), "orizzonte", dx=-66, dy=4, dimensione=13, corsivo=False)
O = (0, -d, h)
S.linea((0, -d, 0), O, "grigio", 3)
S.punto(O, "O", dx=-18, dy=-6)
th = math.radians(40)
ur3 = (math.cos(th), math.sin(th), 0)
un3 = (-math.sin(th), math.cos(th), 0)
T3 = (-40, 0, 0)
H = 70
A3 = (T3[0] + 80 * ur3[0], 80 * ur3[1], 0)
B3 = (A3[0] + 130 * ur3[0], A3[1] + 130 * ur3[1], 0)
W = 70
C3 = (B3[0] + W * un3[0], B3[1] + W * un3[1], 0)
D3 = (A3[0] + W * un3[0], A3[1] + W * un3[1], 0)
up = lambda q, z=H: (q[0], q[1], z)
# il piano alfa che contiene la faccia AB: verticale, taglia il quadro lungo la verticale per T
S.poligono([T3, (B3[0] + 30 * ur3[0], B3[1] + 30 * ur3[1], 0), (B3[0] + 30 * ur3[0], B3[1] + 30 * ur3[1], 150),
            (T3[0], 0, 150)], "#d97706", 0.10, "#d97706")
S.testo((B3[0] + 30 * ur3[0], B3[1] + 30 * ur3[1], 150), "α", dx=4, dy=4, colore="arancio", dimensione=16)
# il solido
S.scatola([A3, B3, C3, D3], H, "blu", riempi=[A3, B3, up(B3), up(A3)])
S.testo(A3, "A", dx=-6, dy=16, colore="blu")
S.testo(B3, "B", dx=4, dy=14, colore="blu")
# la retta r di base e il suo prolungamento fino al quadro; lo spigolo superiore prolungato
S.linea(T3, A3, "blu", 1.2, "5,3")
S.linea(up(T3), up(A3), "blu", 1.2, "5,3")
S.testo(((T3[0] + A3[0]) / 2, (T3[1] + A3[1]) / 2, 0), "r", dx=2, dy=14, colore="blu")
# la traccia di alfa sul quadro: la verticale per T
S.linea(T3, (T3[0], 0, 175), "nero", 2.2)
S.testo((T3[0], 0, 175), "t_α", dx=-24, dy=4)
S.linea(T3, up(T3), "verde", 4)
S.testo((T3[0], 0, H / 2), "H vera", dx=-56, dy=4, colore="verde", dimensione=13, corsivo=False)
S.punto(T3, "T_r", dx=-26, dy=14)
f.nota(16, 512, "La faccia AB sta nel piano verticale α, che taglia il quadro lungo la verticale tα per la traccia Tᵣ della retta di base r.", 13)
f.nota(16, 530, "Su tα lo spigolo superiore prolungato arriva all'altezza vera H: sul quadro le misure non si deformano.", 13)
f.salva(nome("b14-spazio-altezza-sulla-traccia-del-piano"))

# --- 14.2 Sul foglio: l'altezza sulla traccia del piano (prospettiva con l'osservatore in piedi) ---
d, h = 240, 120
th = math.radians(40)
ur = (math.cos(th), math.sin(th))
un = (-math.sin(th), math.cos(th))
T = (-40, 0)
tA, AB, BC, H = 30, 160, 100, 80
A = (T[0] + tA * ur[0], tA * ur[1])
B = (A[0] + AB * ur[0], A[1] + AB * ur[1])
C = (B[0] + BC * un[0], B[1] + BC * un[1])
D = (A[0] + BC * un[0], A[1] + BC * un[1])
Fr = (d / math.tan(th), 0)
Fn = (-d * math.tan(th), 0)
Os = (0, -d)
Ap, Bp, Cp, Dp = (prosp(*q, d, h) for q in (A, B, C, D))
At, Bt, Ct, Dt = (prosp(*q, d, h, H) for q in (A, B, C, D))
Tp = prosp(*T, d, h)
Hq = (T[0], -h + H)
assert vicino(interseca(Hq, Fr, Ap, (Ap[0], 0)), At) and vicino(interseca(Hq, Fr, Bp, (Bp[0], 0)), Bt)
assert vicino(interseca(Bt, Fn, Cp, (Cp[0], 0)), Ct) and vicino(interseca(At, Fn, Ct, Fr), Dt)

f = Figura(800, 360, 110, "Le altezze sulla traccia del piano: H vera, dalla fondamentale in su", x0=380)
f._linea((-370, 0), (410, 0), "nero", 1.6)
f.testo((-370, 0), "orizzonte", dx=2, dy=-8, dimensione=13, corsivo=False)
f._linea((-370, -h), (410, -h), "nero", 1.6)
f.testo((-370, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
f.punto((0, 0), "O_0", dx=4, dy=-8)
f.punto(Fr, "F_r", dx=-4, dy=-10)
f.punto(Fn, "F_n", dx=-10, dy=-10)
f.retta(Tp, Fr, "rosso", 1.2)
f._linea(Ap, Fn, "grigio", 0.9, "2,3")
f._linea(Bp, Fn, "grigio", 0.9, "2,3")
f._linea(Dp, Fr, "grigio", 0.9, "2,3")
f.figura([Ap, Bp, Cp, Dp], "blu")
# traccia del piano alfa e altezza vera
f._linea((T[0], -h), (T[0], -h + H + 70), "nero", 2)
f.testo((T[0], -h + H + 70), "t_α", dx=-24, dy=4)
f._linea((T[0], -h), Hq, "verde", 4)
f.testo((T[0], -h + H / 2), "H", dx=-18, dy=4, colore="verde")
f.costruzione(Hq, Fr)
f._linea(Bt, Fn, "grigio", 0.9, "2,3")
f._linea(At, Fn, "grigio", 0.9, "2,3")
E = (0, -d, h)
proj = lambda P: prosp(P[0], P[1], d, h, P[2])
disegna_scatole(f, [Scatola(A, ur, un, AB, BC, H)], E, proj)
f.punto(Tp, "T_r′", dx=-14, dy=18, colore="rosso")
for q, n_, dx, dy in [(Ap, "A′", -8, 18), (Bp, "B′", 6, 14), (Cp, "C′", -26, 4), (Dp, "D′", -24, 12)]:
    f.punto(q, n_, dx, dy, "blu")
f.nota(16, 330, "La traccia del piano α è la verticale per Tᵣ′. Su di essa si stacca H vera dalla fondamentale; da lì si va verso Fᵣ", 13)
f.nota(16, 348, "e si trovano le cime degli spigoli per A′ e B′. Poi: cima di B′ verso Fₙ fino allo spigolo per C′; le fughe chiudono il solido.", 13)
f.salva(nome("b14-altezze-sulla-traccia-del-piano"))

# --- 14.3 Nello spazio: l'angolo vero si legge in O* ------------------------------------------
d, h = 150, 150
f = Figura(760, 500, 250, "Nello spazio: l'angolo tra due rette si legge vero in O*", x0=300)
S = Spazio(f, w=(0.35, -1.0, 0.45))
Xa, Xb = -260, 300
S.poligono([(Xa, 0, -10), (Xb, 0, -10), (Xb, 0, 220), (Xa, 0, 220)], "#7fa6c9", 0.20, "#5d88b0", 1.2)
S.testo((Xa, 0, 220), "quadro", dx=4, dy=16, colore="#3f6b94", dimensione=13, corsivo=False)
S.linea((Xa, 0, h), (Xb, 0, h), "nero", 2.2)
S.testo((Xb, 0, h), "orizzonte", dx=-64, dy=-8, dimensione=13, corsivo=False)
S.poligono([(Xa, -d - 20, h), (Xb, -d - 20, h), (Xb, 0, h), (Xa, 0, h)], "#d9a441", 0.10, "#d9a441")
O = (0, -d, h)
O0 = (0, 0, h)
Os3 = (0, 0, h - d)
th = math.radians(40)
Fr3 = (d / math.tan(th), 0, h)
Fs3 = (-d * math.tan(th), 0, h)
S.punto(O, "O", dx=-20, dy=12)
S.punto(O0, "O_0", dx=-10, dy=-10)
S.linea(O, Fr3, "rosso", 1.8)
S.linea(O, Fs3, "blu", 1.8)
S.punto(Fr3, "F_r", dx=4, dy=-8, colore="rosso")
S.punto(Fs3, "F_s", dx=-22, dy=-8, colore="blu")
S.testo(((O[0] + Fr3[0]) / 2, (O[1] + Fr3[1]) / 2, h), "parallela a r", dx=6, dy=14, colore="rosso", dimensione=12, corsivo=False)
S.testo(((O[0] + Fs3[0]) / 2, (O[1] + Fs3[1]) / 2, h), "parallela a s", dx=-80, dy=14, colore="blu", dimensione=12, corsivo=False)
# angolo retto in O (disegnato nel piano d'orizzonte)
u1 = tuple((Fr3[j] - O[j]) / math.dist(Fr3, O) for j in range(3))
u2 = tuple((Fs3[j] - O[j]) / math.dist(Fs3, O) for j in range(3))
q1 = tuple(O[j] + 14 * u1[j] for j in range(3))
q2 = tuple(O[j] + 14 * u2[j] for j in range(3))
q3 = tuple(O[j] + 14 * u1[j] + 14 * u2[j] for j in range(3))
S.linea(q1, q3, "nero", 1)
S.linea(q2, q3, "nero", 1)
S.arco(O0, (0, -1, 0), (0, 0, -1), d, 0, 90, colore="arancio", spessore=1.6, tratteggio="6,3")
S.punto(Os3, "O*", dx=8, dy=6, colore="arancio")
S.linea(Os3, Fr3, "rosso", 1.2, "5,3")
S.linea(Os3, Fs3, "blu", 1.2, "5,3")
v1 = (Fr3[0], d)
v2 = (Fs3[0], d)
assert abs(v1[0] * v2[0] + v1[1] * v2[1]) < 1e-6
f.nota(16, 472, "Le parallele a r e a s per O formano lo stesso angolo di r e s (qui 90°). Il piano d'orizzonte si ribalta sul quadro:", 13)
f.nota(16, 490, "O va in O*, Fᵣ e Fₛ restano dove sono, quindi l'angolo FᵣO*Fₛ è l'angolo vero tra r e s.", 13)
f.salva(nome("b14-spazio-angolo-vero-in-o-asterisco"))

# --- 14.4 In pianta: perche' funziona il punto di misura --------------------------------------
d = 170
th = math.radians(40)
ur = (math.cos(th), math.sin(th))
T = (-20, 0)
tA = 150
A = (T[0] + tA * ur[0], tA * ur[1])
O = (0, -d)
Fr = (d / math.tan(th), 0)
Mr = (Fr[0] - math.dist(Fr, O), 0)
Ar = (T[0] + tA, 0)
# A Ar e' parallela a O Mr
assert abs((A[0] - Ar[0]) * (O[1] - Mr[1]) - (A[1] - Ar[1]) * (O[0] - Mr[0])) < 1e-6
f = Figura(760, 380, 140, "In pianta: perché il punto di misura funziona", x0=300)
f._linea((-290, 0), (440, 0), "nero", 1.8)
f.testo((440, 0), "quadro (in pianta)", dx=-124, dy=16, dimensione=13, corsivo=False)
f.punto(O, "O", dx=8, dy=4)
f.costruzione(O, (0, 0))
f.testo((0, -d / 2), "d", dx=6, dy=4)
f.retta(T, (T[0] + 250 * ur[0], 250 * ur[1]), "blu", 2)
f.testo((T[0] + 250 * ur[0], 250 * ur[1]), "r", dx=4, dy=4, colore="blu")
f._linea(O, Fr, "rosso", 1.4, "6,3")
f.testo(((O[0] + Fr[0]) / 2, (O[1] + Fr[1]) / 2), "parallela a r", dx=10, dy=6, colore="rosso", dimensione=12, corsivo=False)
arco(f, Fr, math.dist(Fr, O), 180, 360 + gradi(Fr, O))
arco(f, T, tA, 0, gradi(T, A))
f._linea(O, Mr, "verde", 1.8)
f._linea(A, Ar, "verde", 1.8)
f.punto(T, "T_r", dx=-10, dy=-10, colore="blu")
f.punto(A, "A", dx=-16, dy=-2, colore="blu")
f.punto(Fr, "F_r", dx=4, dy=-8, colore="rosso")
f.punto(Mr, "M_r", dx=-18, dy=-10, colore="verde")
f.punto(Ar, "A_r", dx=6, dy=16, colore="verde")
f.nota(16, 334, "Triangolo FᵣOMᵣ: FᵣMᵣ = FᵣO (arco di centro Fᵣ). Triangolo TᵣAAᵣ: TᵣAᵣ = TᵣA (arco di centro Tᵣ).", 13)
f.nota(16, 352, "I due triangoli sono isosceli con i lati paralleli, quindi AAᵣ è parallela a OMᵣ: la retta AAᵣ ha la fuga in Mᵣ.", 13)
f.nota(16, 370, "Sul foglio A′ sta allora sulla retta MᵣAᵣ, e Aᵣ è sulla fondamentale a distanza vera TᵣA dalla traccia.", 13)
f.salva(nome("b14-pianta-perche-funziona-il-punto-di-misura"))

# --- 14.5 Il punto di misura passo per passo (senza pianta), e la retta s perpendicolare --------
d, h = 170, 90
th = math.radians(40)
ur = (math.cos(th), math.sin(th))
T = (-80, 0)
tA, AB = 50, 120
A = (T[0] + tA * ur[0], tA * ur[1])
B = (A[0] + AB * ur[0], A[1] + AB * ur[1])
Fr = (d / math.tan(th), 0)
Fs = (-d * math.tan(th), 0)
Os = (0, -d)
Mr = (Fr[0] - math.dist(Fr, Os), 0)
Tp, Ap, Bp = prosp(*T, d, h), prosp(*A, d, h), prosp(*B, d, h)
Ar, Br = (T[0] + tA, -h), (T[0] + tA + AB, -h)
assert vicino(interseca(Mr, Ar, Tp, Fr), Ap) and vicino(interseca(Mr, Br, Tp, Fr), Bp)
assert abs(Fr[0] * Fs[0] + d * d) < 1e-6

passi = [
    "Passo 1 · orizzonte, fondamentale, O₀, O*; si sceglie Fᵣ, la traccia Tᵣ′ e A′ su r′",
    "Passo 2 · il punto di misura: centro in Fᵣ, raggio FᵣO*, fino all'orizzonte: Mᵣ",
    "Passo 3 · da Mᵣ si proietta A′ sulla fondamentale: Aᵣ; da Aᵣ si stacca AB vera: Bᵣ",
    "Passo 4 · si riproietta Bᵣ da Mᵣ: dove la retta incontra r′ c'è B′",
    "Passo 5 · in O* l'angolo di 90° con O*Fᵣ dà Fₛ; s′ è la retta B′Fₛ",
]
didascalie = [
    ("Fᵣ sta sull'orizzonte (è una fuga), Tᵣ′ sulla fondamentale (è una traccia). r′ le congiunge; A′ si sceglie su r′,",
     "non troppo vicino all'orizzonte, se no il disegno si schiaccia."),
    ("Mᵣ è il punto di misura della retta r: serve solo per portare le misure su r. Ogni retta ha il suo.",
     "L'arco si fa con il compasso puntato in Fᵣ."),
    ("La retta da Mᵣ per A′ si prolunga fino alla fondamentale. Sulla fondamentale le misure sono vere:",
     "da Aᵣ si riporta la lunghezza AB (raddoppiata, se il disegno viene troppo piccolo)."),
    ("Bᵣ si unisce a Mᵣ: dove questa retta taglia r′ c'è B′. Il segmento A′B′ è la prospettiva di AB.",
     "Attenzione: B′ si chiude su r′ (che va verso Fᵣ), non verso il punto di misura."),
    ("L'angolo vero tra r e s si legge in O*: si unisce O* con Fᵣ e si costruisce l'angolo retto; il secondo lato",
     "incontra l'orizzonte in Fₛ. s passa per B, quindi s′ è la retta B′Fₛ."),
]
for i in range(5):
    k = i + 1
    f = Figura(800, 310, 50, passi[i], x0=420)
    f._linea((-410, 0), (370, 0), "nero", 1.6)
    f.testo((-410, 0), "orizzonte", dx=2, dy=-8, dimensione=13, corsivo=False)
    f._linea((-410, -h), (370, -h), "nero", 1.6)
    f.testo((-410, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
    f.punto((0, 0), "O_0", dx=4, dy=-8)
    f.richiamo(0, 0, -d)
    f.punto(Os, "O*", dx=8, dy=6)
    f.punto(Fr, "F_r", dx=4, dy=-8)
    f.retta(Tp, Fr, "rosso", 2)
    f.punto(Tp, "T_r′", dx=-30, dy=18, colore="rosso")
    f.testo(((Tp[0] + Fr[0]) / 2 + 60, (Tp[1] + Fr[1]) / 2 + 30), "r′", colore="rosso")
    f.punto(Ap, "A′", dx=-10, dy=-10, colore="rosso")
    if k >= 2:
        arco(f, Fr, Fr[0] - Mr[0], 180, 360 + gradi(Fr, Os), colore="verde" if k == 2 else "grigio")
        f.costruzione(Os, Fr)
        f.punto(Mr, "M_r", dx=-10, dy=-10, colore="verde")
    if k >= 3:
        f._linea(Mr, Ar, "verde" if k == 3 else "grigio", 1.2, "5,4")
        f._linea(Ar, Br, "verde", 3)
        f.punto(Ar, "A_r", dx=-8, dy=18, colore="verde")
        f.punto(Br, "B_r", dx=-8, dy=18, colore="verde")
        f.testo(((Ar[0] + Br[0]) / 2, -h), "AB vera", dx=-24, dy=34, dimensione=12, colore="verde", corsivo=False)
    if k >= 4:
        f._linea(Mr, Br, "verde" if k == 4 else "grigio", 1.2, "5,4")
        f._linea(Ap, Bp, "rosso", 4)
        f.punto(Bp, "B′", dx=-2, dy=-10, colore="rosso")
    if k >= 5:
        f._linea(Os, Fs, "blu", 1.2, "5,4")
        ang_retto(f, Os, Fr, Fs)
        f.punto(Fs, "F_s", dx=-8, dy=-10, colore="blu")
        f.retta(Bp, Fs, "blu", 2)
        f.testo(((Bp[0] + Fs[0]) / 2, (Bp[1] + Fs[1]) / 2), "s′", dx=-4, dy=18, colore="blu")
    f.nota(16, 282, didascalie[i][0], 13)
    f.nota(16, 300, didascalie[i][1], 13)
    f.salva(nome(f"b14-punto-di-misura-passo-{k}"))

# --- 14.6 Esercizio: il parallelepipedo senza pianta, con i punti di misura e la traccia del piano ---
d, h = 255, 135
th = math.radians(38)
ur = (math.cos(th), math.sin(th))
us = (-math.sin(th), math.cos(th))
T = (-60, 0)
tA, AB, BC, H = 30, 180, 120, 105
A = (T[0] + tA * ur[0], tA * ur[1])
B = (A[0] + AB * ur[0], A[1] + AB * ur[1])
C = (B[0] + BC * us[0], B[1] + BC * us[1])
D = (A[0] + BC * us[0], A[1] + BC * us[1])
Os = (0, -d)
Fr = (d / math.tan(th), 0)
Fs = (-d * math.tan(th), 0)
Mr = (Fr[0] - math.dist(Fr, Os), 0)
Ms = (Fs[0] + math.dist(Fs, Os), 0)
Ap, Bp, Cp, Dp = (prosp(*q, d, h) for q in (A, B, C, D))
Tp = prosp(*T, d, h)
Ar, Br = (T[0] + tA, -h), (T[0] + tA + AB, -h)
assert vicino(interseca(Mr, Ar, Tp, Fr), Ap) and vicino(interseca(Mr, Br, Tp, Fr), Bp)
# la retta s per B: traccia e misure dal suo punto di misura
sT = -B[1] / us[1]                     # parametro della traccia (negativo: la traccia sta "prima" di B)
Ts = (B[0] + sT * us[0], 0)
Tsp = (Ts[0], -h)
Bs = (Ts[0] - (-sT), -h)
if not vicino(interseca(Ms, Bs, Tsp, Fs), Bp):
    Bs = (Ts[0] + (-sT), -h)
assert vicino(interseca(Ms, Bs, Tsp, Fs), Bp)
Cs = None
for cand in [(Bs[0] - BC, -h), (Bs[0] + BC, -h)]:
    if vicino(interseca(Ms, cand, Bp, Fs), Cp):
        Cs = cand
assert Cs is not None
assert vicino(interseca(Ap, Fs, Cp, Fr), Dp)
At, Bt, Ct, Dt = (prosp(*q, d, h, H) for q in (A, B, C, D))
Hq = (T[0], -h + H)
assert vicino(interseca(Hq, Fr, Ap, (Ap[0], 0)), At) and vicino(interseca(Hq, Fr, Bp, (Bp[0], 0)), Bt)
assert vicino(interseca(Bt, Fs, Cp, (Cp[0], 0)), Ct) and vicino(interseca(At, Fs, Ct, Fr), Dt)

f = Figura(820, 410, 75, "Esercizio: il parallelepipedo senza pianta (AB = 6, BC = 4, H = 3,5)", x0=390)
f._linea((-380, 0), (420, 0), "nero", 1.6)
f.testo((-380, 0), "orizzonte", dx=2, dy=-8, dimensione=13, corsivo=False)
f._linea((-380, -h), (420, -h), "nero", 1.6)
f.testo((-380, -h), "fondamentale", dx=2, dy=16, dimensione=13, corsivo=False)
f.punto((0, 0), "O_0", dx=4, dy=-8)
f.richiamo(0, 0, -d)
f.punto(Os, "O*", dx=8, dy=6)
f.costruzione(Os, Fr)
f.costruzione(Os, Fs)
ang_retto(f, Os, Fr, Fs)
f.punto(Fr, "F_r", dx=4, dy=-8)
f.punto(Fs, "F_s", dx=-10, dy=-10)
arco(f, Fr, Fr[0] - Mr[0], 180, 360 + gradi(Fr, Os))
arco(f, Fs, Ms[0] - Fs[0], gradi(Fs, Os) % 360, 360)
f.punto(Mr, "M_r", dx=-26, dy=-8, colore="verde")
f.punto(Ms, "M_s", dx=4, dy=-8, colore="verde")
for M, Q in [(Mr, Ar), (Mr, Br), (Ms, Bs), (Ms, Cs)]:
    f._linea(M, Q, "grigio", 0.9, "5,4")
f._linea(Ar, Br, "verde", 3)
f._linea(Cs, Bs, "verde", 2.2, "7,3")
f.punto(Ar, "A_r", dx=-10, dy=18, colore="verde")
f.punto(Br, "B_r", dx=-6, dy=18, colore="verde")
f.punto(Bs, "B_s", dx=-8, dy=18, colore="verde")
f.punto(Cs, "C_s", dx=-22, dy=-8, colore="verde")
f.retta(Tp, Fr, "rosso", 1.2)
f._linea(Bp, Fs, "grigio", 0.9, "2,3")
f._linea(Ap, Fs, "grigio", 0.9, "2,3")
f._linea(Cp, Fr, "grigio", 0.9, "2,3")
f.figura([Ap, Bp, Cp, Dp], "blu")
f._linea((T[0], -h), (T[0], -h + H + 50), "nero", 2)
f.testo((T[0], -h + H + 50), "t_α", dx=-24, dy=4)
f._linea((T[0], -h), Hq, "verde", 4)
f.testo((T[0], -h + H / 2), "H", dx=-18, dy=4, colore="verde")
f.costruzione(Hq, Fr)
f._linea(Bt, Fs, "grigio", 0.9, "2,3")
f._linea(At, Fs, "grigio", 0.9, "2,3")
E = (0, -d, h)
proj = lambda P: prosp(P[0], P[1], d, h, P[2])
disegna_scatole(f, [Scatola(A, ur, us, AB, BC, H)], E, proj)
f.punto(Tp, "T_r′", dx=-34, dy=18, colore="rosso")
for q, n_, dx, dy in [(Ap, "A′", -24, 8), (Bp, "B′", 6, 14), (Cp, "C′", -10, -8), (Dp, "D′", -26, 6)]:
    f.punto(q, n_, dx, dy, "blu")
f.nota(16, 386, "Misure in cm sul foglio. Rosso pieno: spigoli visti; tratteggio: spigoli nascosti.", 13)
f.nota(16, 404, "Le misure vere stanno solo sulla fondamentale (lunghezze) e sulla traccia tα (altezze).", 13)
f.salva(nome("b14-esercizio-parallelepipedo-senza-pianta"))


# =============================================================================================
# BOZZA 16
# =============================================================================================

# --- 16.1 Nello spazio: l'occhio di formica ------------------------------------------------------
d = 170
f = Figura(760, 500, 220, "Nello spazio: l'occhio di formica sta sul geometrale", x0=330)
S = Spazio(f)
Xa, Xb = -150, 260
S.poligono([(Xa - 20, -d - 20, 0), (Xb, -d - 20, 0), (Xb, 180, 0), (Xa - 20, 180, 0)], "#c9b98f", 0.18, "#b5a77f")
S.testo((Xb, 170, 0), "geometrale", dx=-90, dy=-4, colore="#8a7a4f", dimensione=13, corsivo=False)
S.poligono([(Xa, 0, 0), (Xb, 0, 0), (Xb, 0, 190), (Xa, 0, 190)], "#7fa6c9", 0.22, "#5d88b0", 1.2)
S.testo((Xa, 0, 190), "quadro", dx=4, dy=16, colore="#3f6b94", dimensione=13, corsivo=False)
S.linea((Xa, 0, 0), (Xb, 0, 0), "rosso", 2.6)
S.testo((Xb, 0, 0), "orizzonte ≡ fondamentale", dx=-60, dy=22, colore="rosso", dimensione=13, corsivo=False)
O = (0, -d, 0)
S.punto(O, "O (la formica)", dx=-40, dy=18)
S.linea(O, (0, 0, 0), "nero", 1.2, "6,4")
S.testo((0, -d / 2, 0), "d", dx=-14, dy=4)
S.punto((0, 0, 0), "O_0", dx=-30, dy=14)
th = math.radians(40)
ur3 = (math.cos(th), math.sin(th), 0)
un3 = (-math.sin(th), math.cos(th), 0)
T3 = (-40, 0, 0)
H = 80
A3 = (T3[0] + 70 * ur3[0], 70 * ur3[1], 0)
B3 = (A3[0] + 130 * ur3[0], A3[1] + 130 * ur3[1], 0)
C3 = (B3[0] + 70 * un3[0], B3[1] + 70 * un3[1], 0)
D3 = (A3[0] + 70 * un3[0], A3[1] + 70 * un3[1], 0)
up = lambda q, z=H: (q[0], q[1], z)
S.scatola([A3, B3, C3, D3], H, "blu", riempi=[A3, B3, up(B3), up(A3)])
S.testo(A3, "A", dx=-6, dy=16, colore="blu")
S.testo(B3, "B", dx=4, dy=14, colore="blu")
S.linea(T3, A3, "blu", 1.2, "5,3")
S.linea(up(T3), up(A3), "blu", 1.2, "5,3")
S.linea(T3, (T3[0], 0, 165), "nero", 2.2)
S.testo((T3[0], 0, 165), "t_α", dx=-24, dy=4)
S.linea(T3, up(T3), "verde", 4)
S.testo((T3[0], 0, H / 2), "H", dx=-18, dy=4, colore="verde")
S.punto(T3, "T_r", dx=-26, dy=14)
# raggio dalla formica alla cima di B: buca il quadro sopra l'orizzonte
Bt3 = up(B3)
f.nota(16, 454, "L'occhio è sul geometrale: l'orizzonte cade sulla fondamentale e tutto il solido si vede sopra di essa;", 13)
f.nota(16, 472, "la base si schiaccia sulla linea. Le altezze vere si portano, come sempre, sulla traccia tα del piano", 13)
f.nota(16, 490, "verticale della faccia, partendo dall'orizzonte.", 13)
f.salva(nome("b16-spazio-occhio-di-formica"))

# --- 16.2 Esercizio: due solidi attaccati ad altezze diverse H1 e H2 ------------------------------
d, ha = 210, 120                    # distanza; distanza tra orizzonte e fondamentale ausiliaria (F)
th = math.radians(36)
ur = (math.cos(th), math.sin(th))
un = (-math.sin(th), math.cos(th))
T = (-130, 0)
tA, L1, L2, W, H1, H2 = 40, 110, 110, 80, 60, 110
A = (T[0] + tA * ur[0], tA * ur[1])
B = (A[0] + L1 * ur[0], A[1] + L1 * ur[1])
E_ = (B[0] + L2 * ur[0], B[1] + L2 * ur[1])
C = (B[0] + W * un[0], B[1] + W * un[1])
D = (A[0] + W * un[0], A[1] + W * un[1])
G = (E_[0] + W * un[0], E_[1] + W * un[1])
Os = (0, -d)
Fr = (d / math.tan(th), 0)
Fn = (-d * math.tan(th), 0)
Mr = (Fr[0] - math.dist(Fr, Os), 0)
Mn = (Fn[0] + math.dist(Fn, Os), 0)


def aus(q):
    k = d / (d + q[1])
    return (q[0] * k, -ha * k)


def vera(q, z):
    k = d / (d + q[1])
    return (q[0] * k, z * k)


Tp = aus(T)
Ap, Bp, Cp, Dp, Ep, Gp = (aus(q) for q in (A, B, C, D, E_, G))
Ar, Br, Er = (T[0] + tA, -ha), (T[0] + tA + L1, -ha), (T[0] + tA + L1 + L2, -ha)
for Q, Pq in [(Ar, Ap), (Br, Bp), (Er, Ep)]:
    assert vicino(interseca(Mr, Q, Tp, Fr), Pq)
sT = -B[1] / un[1]
Tn = (B[0] + sT * un[0], -ha)
Bn = None
for cand in [(Tn[0] - (-sT), -ha), (Tn[0] + (-sT), -ha)]:
    if vicino(interseca(Mn, cand, Tn, Fn), Bp):
        Bn = cand
assert Bn is not None
Cn = None
for cand in [(Bn[0] - W, -ha), (Bn[0] + W, -ha)]:
    if vicino(interseca(Mn, cand, Bp, Fn), Cp):
        Cn = cand
assert Cn is not None
assert vicino(interseca(Ap, Fn, Cp, Fr), Dp) and vicino(interseca(Ep, Fn, Cp, Fr), Gp)
# altezze sulla traccia comune t_alfa (le due facce AB e BE stanno nello stesso piano verticale)
H1q, H2q = (T[0], H1), (T[0], H2)
assert vicino(interseca(H1q, Fr, Ap, (Ap[0], 0)), vera(A, H1))
assert vicino(interseca(H2q, Fr, Ep, (Ep[0], 0)), vera(E_, H2))
assert vicino(interseca(H2q, Fr, Bp, (Bp[0], 0)), vera(B, H2))

f = Figura(820, 480, 200, "Esercizio: due solidi attaccati, H1 davanti e H2 dietro, a occhio di formica", x0=430)
f._linea((-420, 0), (380, 0), "nero", 1.6)
f.testo((-420, 0), "orizzonte ≡ fondamentale", dx=2, dy=-8, dimensione=12, corsivo=False)
f._linea((-420, -ha), (380, -ha), "nero", 1.6)
f.testo((-420, -ha), "(F) fondamentale ausiliaria", dx=2, dy=18, dimensione=12, corsivo=False)
f.punto((0, 0), "O_0", dx=4, dy=16)
f.richiamo(0, -ha - 4, -d)
f.punto(Os, "O*", dx=8, dy=6)
f.costruzione(Os, Fr)
f.costruzione(Os, Fn)
ang_retto(f, Os, Fr, Fn)
f.punto(Fr, "F_r", dx=-6, dy=18)
f.punto(Fn, "F_n", dx=-24, dy=18)
arco(f, Fr, Fr[0] - Mr[0], 180, 360 + gradi(Fr, Os))
arco(f, Fn, Mn[0] - Fn[0], gradi(Fn, Os) % 360, 360)
f.punto(Mr, "M_r", dx=-26, dy=16, colore="verde")
f.punto(Mn, "M_n", dx=4, dy=16, colore="verde")
for M, Q in [(Mr, Ar), (Mr, Br), (Mr, Er), (Mn, Bn), (Mn, Cn)]:
    f._linea(M, Q, "grigio", 0.8, "5,4")
f._linea(Ar, Er, "verde", 3)
f._linea(Cn, Bn, "verde", 2.2, "7,3")
for Q, n_, dx in [(Ar, "A_r", -10), (Br, "B_r", -8), (Er, "E_r", -8), (Bn, "B_n", -8), (Cn, "C_n", -10)]:
    f.punto(Q, n_, dx=dx, dy=18 if n_ != "C_n" else -8, colore="verde")
f.retta(Tp, Fr, "rosso", 1.2)
f._linea(Ap, Fn, "grigio", 0.8, "2,3")
f._linea(Bp, Fn, "grigio", 0.8, "2,3")
f._linea(Ep, Fn, "grigio", 0.8, "2,3")
f._linea(Dp, Fr, "grigio", 0.8, "2,3")
f.figura([Ap, Bp, Cp, Dp], "blu")
f.figura([Bp, Ep, Gp, Cp], "viola")
for q in (Ap, Bp, Ep, Dp):
    f.richiamo(q[0], q[1], 0)
# traccia del piano comune e le due altezze
f._linea((T[0], -ha), (T[0], H2 + 40), "nero", 2)
f.testo((T[0], H2 + 40), "t_α", dx=-24, dy=4)
f._linea((T[0], 0), H2q, "verde", 2)
f._linea((T[0], 0), H1q, "verde", 5)
f.testo(H1q, "H1", dx=-26, dy=14, colore="verde", dimensione=13)
f.testo(H2q, "H2", dx=-26, dy=6, colore="verde", dimensione=13)
f.costruzione(H1q, Fr)
f.costruzione(H2q, Fr)
Eye = (0, -d, 0)
proj = lambda P: vera((P[0], P[1]), P[2])
disegna_scatole(f, [Scatola(A, ur, un, L1, W, H1), Scatola(B, ur, un, L2, W, H2)], Eye, proj)
f.punto(Tp, "T_r′", dx=4, dy=18, colore="rosso")
for q, n_, dx, dy in [(Ap, "A′", -22, 8), (Bp, "B′", 0, 16), (Ep, "E′", 6, 12), (Dp, "D′", -24, 4),
                      (Cp, "C′", -8, -8), (Gp, "G′", 4, -6)]:
    f.punto(q, n_, dx, dy, "blu")
f.nota(16, 452, "Le facce AB (solido basso) e BE (solido alto) stanno nello stesso piano verticale α: una sola traccia tα per H1 e H2,", 13)
f.nota(16, 470, "staccate dall'orizzonte. Si portano da Fᵣ sulle verticali; il resto si chiude con le fughe. Il tratteggio è nascosto.", 13)
f.salva(nome("b16-esercizio-due-solidi-h1-h2"))
print("ok")
