"""Schemi per la bozza di geometria descrittiva 11 (lezione del 10 novembre 2026):
assonometria ortogonale (ripasso: triangolo delle tracce e ribaltamento dei piani coordinati),
assonometria obliqua cavaliera militare (direzione di proiezione, ribaltamento dell'asse z,
esercizio del prisma 4 x 2 cm) e sezioni del parallelepipedo con un piano parallelo alla LT
(proiezioni ortogonali, spazio, cavaliera) e con un piano verticale (proiezioni ortogonali, spazio).

Usa disegni_monge.py senza modificarlo. Coordinate nello spazio (x, y, z): x lungo la LT
(o lungo l'asse x dell'assonometria), y = aggetto, z = quota. Immagini in bozze/img/ con prefisso b11-.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, COLORI, _etichetta, P1, P2

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"


# ---------------------------------------------------------------- vettori

def add(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(len(a)))


def mul(a, k):
    return tuple(x * k for x in a)


def dot(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def unit(a):
    n = math.sqrt(dot(a, a))
    return tuple(x / n for x in a)


def inter2(p1, p2, q1, q2):
    d = (p2[0] - p1[0]) * (q2[1] - q1[1]) - (p2[1] - p1[1]) * (q2[0] - q1[0])
    t = ((q1[0] - p1[0]) * (q2[1] - q1[1]) - (q1[1] - p1[1]) * (q2[0] - q1[0])) / d
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))


# ---------------------------------------------------------------- primitive SVG (coordinate SVG assolute)

def _c(c):
    return COLORI.get(c, c)


def rline(f, a, b, colore="nero", spessore=1.6, tratteggio=None):
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    f.parti.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                   f'stroke="{_c(colore)}" stroke-width="{spessore}"{dash} stroke-linecap="round"/>')


def rpoly(f, pts, colore="blu", opacita=0.12, bordo=None, spessore=1.6, tratteggio=None, retino=False):
    s = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    fill = 'url(#retino)' if retino else _c(colore)
    op = 1 if retino else opacita
    st = f' stroke="{_c(bordo)}" stroke-width="{spessore}"' if bordo else ' stroke="none"'
    if bordo and tratteggio:
        st += f' stroke-dasharray="{tratteggio}"'
    f.parti.append(f'<polygon points="{s}" fill="{fill}" fill-opacity="{op}"{st} stroke-linejoin="round"/>')


def rtext(f, p, s, dx=6, dy=-6, colore="nero", dim=15, corsivo=True):
    st = ' font-style="italic"' if corsivo else ""
    f.parti.append(f'<text x="{p[0] + dx:.1f}" y="{p[1] + dy:.1f}" font-family="Helvetica, Arial, sans-serif" '
                   f'font-size="{dim}" fill="{_c(colore)}"{st}>{_etichetta(s)}</text>')


def rdot(f, p, colore="nero", r=2.8):
    f.parti.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" fill="{_c(colore)}"/>')


def rarc(f, c, r, p0, p1, grande=0, verso=0, colore="grigio", tratteggio="5,4", spessore=1):
    f.parti.append(f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r:.1f} {r:.1f} 0 {grande} {verso} {p1[0]:.1f} {p1[1]:.1f}" '
                   f'fill="none" stroke="{_c(colore)}" stroke-width="{spessore}" stroke-dasharray="{tratteggio}"/>')


def ranglo(f, v, d1, d2, lato=9):
    a = (v[0] + d1[0] * lato, v[1] + d1[1] * lato)
    c = (v[0] + d2[0] * lato, v[1] + d2[1] * lato)
    b = (a[0] + d2[0] * lato, a[1] + d2[1] * lato)
    f.parti.append(f'<polyline points="{a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f}" '
                   f'fill="none" stroke="#1f1f1f" stroke-width="1"/>')


def u2(a, b):
    l = math.hypot(b[0] - a[0], b[1] - a[1])
    return ((b[0] - a[0]) / l, (b[1] - a[1]) / l)


def retino(f):
    f.parti.append('<defs><pattern id="retino" patternUnits="userSpaceOnUse" width="7" height="7" '
                   'patternTransform="rotate(45)"><rect width="7" height="7" fill="#c0392b" fill-opacity="0.10"/>'
                   '<line x1="0" y1="0" x2="0" y2="7" stroke="#c0392b" stroke-width="1"/></pattern></defs>')


def note(f, y0, righe, dim=13):
    for i, t in enumerate(righe):
        f.nota(16, y0 + 20 * i, t, dim)


# ---------------------------------------------------------------- solidi convessi in una vista parallela

def disegna_solido(f, proj, facce, vista, colore="blu", riempi=0.10, spessore=2.0, nascoste=True, fondo=None):
    """facce: liste di punti 3D di un poliedro convesso. vista: vettore verso chi guarda.
    Le facce visibili si riempiono; gli spigoli di facce tutte nascoste si tratteggiano."""
    c = tuple(sum(p[j] for fc in facce for p in fc) / sum(len(fc) for fc in facce) for j in range(3))
    vis = []
    for fc in facce:
        n = cross(sub(fc[1], fc[0]), sub(fc[2], fc[0]))
        cf = tuple(sum(p[j] for p in fc) / len(fc) for j in range(3))
        if dot(n, sub(cf, c)) < 0:
            n = mul(n, -1)
        vis.append(dot(n, vista) > 1e-9)
    spig = {}
    for i, fc in enumerate(facce):
        for a, b in zip(fc, fc[1:] + fc[:1]):
            k = tuple(sorted([tuple(round(v, 6) for v in a), tuple(round(v, 6) for v in b)]))
            spig.setdefault(k, []).append(vis[i])
    for i, fc in enumerate(facce):
        if vis[i] and riempi:
            rpoly(f, [proj(p) for p in fc], fondo or colore, riempi)
    for (a, b), vv in spig.items():
        if any(vv):
            rline(f, proj(a), proj(b), colore, spessore)
        elif nascoste:
            rline(f, proj(a), proj(b), colore, 1.2, "5,4")
    return vis


def vista_da(R1, R2):
    """Direzione verso chi guarda per una proiezione parallela con righe R1 (x schermo), R2 (y schermo, in alto)."""
    n = cross(R1, R2)
    return n if n[2] > 0 else mul(n, -1)


def scatola(x0, x1, y0, y1, z0, z1):
    v = lambda x, y, z: (x, y, z)
    return [
        [v(x0, y0, z0), v(x1, y0, z0), v(x1, y1, z0), v(x0, y1, z0)],
        [v(x0, y0, z1), v(x1, y0, z1), v(x1, y1, z1), v(x0, y1, z1)],
        [v(x0, y0, z0), v(x1, y0, z0), v(x1, y0, z1), v(x0, y0, z1)],
        [v(x0, y1, z0), v(x1, y1, z0), v(x1, y1, z1), v(x0, y1, z1)],
        [v(x0, y0, z0), v(x0, y1, z0), v(x0, y1, z1), v(x0, y0, z1)],
        [v(x1, y0, z0), v(x1, y1, z0), v(x1, y1, z1), v(x1, y0, z1)],
    ]


class TriedroLavagna(Triedro):
    """Il triedro come lo disegna la docente (stesso di geometria-bozza-04.py): pi1 in vera forma,
    la LT che scende a sinistra e l'asse dell'aggetto che scende a destra, a 45 gradi."""

    def _p(self, p):
        c = math.cos(math.radians(45))
        u = (self.X3 - p[0]) * self.k
        y, z = p[1] * self.k, p[2] * self.k
        return (self.o[0] - u * c + y * c, self.o[1] + u * c + y * c - z)


VISTA_TRIEDRO = vista_da((1, 1, 0), (-1, 1, -math.sqrt(2)))  # righe di _p (y schermo verso il basso -> invertita)
# _p: sx = c(x - X3) + c y ; sy(giu') = c(X3 - x) + c y - z  -> in alto: c x - c y + z
VISTA_TRIEDRO = vista_da((1, 1, 0), (1, -1, math.sqrt(2)))


# =====================================================================
# 1. Assonometria ortogonale sul foglio: triangolo delle tracce e ribaltamenti
# =====================================================================

def ortogonale_foglio():
    a, b, c = 4.5, 7.0, 6.0
    X, Y, Z = (a, 0, 0), (0, b, 0), (0, 0, c)
    n = unit((1 / a, 1 / b, 1 / c))
    Oq = mul(n, dot(n, X))
    e1 = unit(add((0, 0, 1), mul(n, -n[2])))
    e2 = cross(e1, n)
    k = 42
    W, H = 640, 640
    ox, oy = 300, 300            # O' in coordinate SVG

    def q(p):
        v = sub(p, Oq)
        return (ox + dot(v, e2) * k, oy - dot(v, e1) * k)

    Xs, Ys, Zs, Os = q(X), q(Y), q(Z), (ox, oy)
    f = Figura(W, H, 0, "Assonometria ortogonale: il triangolo delle tracce e i ribaltamenti")
    rpoly(f, [Xs, Ys, Zs], "blu", 0.07, "blu", 1.6)

    def ribalta(P, Q, R, colore):
        """Ribalta la faccia O-P-Q intorno al lato PQ (R e' il vertice opposto): O* sulla perpendicolare
        da O' a PQ, sulla semicirconferenza di diametro PQ, dalla parte opposta a R."""
        M = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
        rr = math.dist(P, Q) / 2
        d = u2(P, Q)
        nn = (-d[1], d[0])
        # verso opposto a R
        if (R[0] - M[0]) * nn[0] + (R[1] - M[1]) * nn[1] > 0:
            nn = (-nn[0], -nn[1])
        # O* = O' + t*nn con |O* - M| = rr
        w = (Os[0] - M[0], Os[1] - M[1])
        bq = 2 * (w[0] * nn[0] + w[1] * nn[1])
        cq = w[0] ** 2 + w[1] ** 2 - rr * rr
        t = (-bq + math.sqrt(bq * bq - 4 * cq)) / 2
        Ost = (Os[0] + t * nn[0], Os[1] + t * nn[1])
        # semicirconferenza (dalla parte di O*)
        ang = lambda p: math.atan2(p[1] - M[1], p[0] - M[0])
        rarc(f, M, rr, P, Q, 0, 1 if (Ost[0] - M[0]) * (-d[1]) + (Ost[1] - M[1]) * d[0] < 0 else 0)
        rline(f, Os, Ost, "grigio", 1, "5,4")
        rline(f, Ost, P, colore, 1.6)
        rline(f, Ost, Q, colore, 1.6)
        ranglo(f, Ost, u2(Ost, P), u2(Ost, Q), 10)
        rdot(f, Ost)
        return Ost

    O1 = ribalta(Xs, Ys, Zs, "verde")       # faccia xOy intorno a XY
    O2 = ribalta(Ys, Zs, Xs, "arancio")     # faccia yOz intorno a YZ
    # verifica: lunghezze vere
    assert abs(math.dist(O1, Xs) - a * k) < 0.5 and abs(math.dist(O1, Ys) - b * k) < 0.5
    assert abs(math.dist(O2, Zs) - c * k) < 0.5

    # assi assonometrici
    for V, nome, dx, dy in ((Xs, "x′", -18, 18), (Ys, "y′", 6, 18), (Zs, "z′", 8, 0)):
        d = u2(Os, V)
        fine = (V[0] + d[0] * 40, V[1] + d[1] * 40)
        rline(f, Os, fine, "nero", 1.8)
        rtext(f, fine, nome, dx, dy)
    rdot(f, Os)
    rtext(f, Os, "O′", 8, -8)

    # unita' vera u = 1.6 sui ribaltati, riportata sugli assi con perpendicolari alla cerniera
    u = 1.6 * k

    def riporta(Ost, V, P, Q, nome, colore, dx, dy, dx2, dy2):
        d = u2(Ost, V)
        Us = (Ost[0] + d[0] * u, Ost[1] + d[1] * u)
        dc = u2(P, Q)
        perp = (-dc[1], dc[0])
        Uq = inter2(Us, (Us[0] + perp[0], Us[1] + perp[1]), Os, V)
        rline(f, Us, Uq, "grigio", 1, "3,3")
        rdot(f, Us, colore)
        rdot(f, Uq, colore)
        rtext(f, Us, f"u*_{nome}", dx, dy, colore, 14)
        rtext(f, Uq, f"u′_{nome}", dx2, dy2, colore, 14)
        return math.dist(Os, Uq) / u

    rx = riporta(O1, Xs, Xs, Ys, "x", "verde", -34, 8, -36, -6)
    ry = riporta(O1, Ys, Xs, Ys, "y", "verde", 8, 4, 2, -10)
    rz = riporta(O2, Zs, Ys, Zs, "z", "arancio", 8, -4, -36, 0)
    rtext(f, O1, "O*", -10, 22)
    rtext(f, O2, "O*", 8, 6)
    rtext(f, ((O1[0] * 0.3 + Xs[0] * 0.7), (O1[1] * 0.3 + Xs[1] * 0.7)), "x*", -26, 6, "verde")
    rtext(f, ((O1[0] + Ys[0]) / 2, (O1[1] + Ys[1]) / 2), "y*", 10, 10, "verde")
    rtext(f, ((O2[0] + Ys[0]) / 2, (O2[1] + Ys[1]) / 2), "y*", 8, 14, "arancio")
    rtext(f, ((O2[0] + Zs[0]) / 2, (O2[1] + Zs[1]) / 2), "z*", 8, -6, "arancio")
    rtext(f, Xs, "X", -16, -8, "blu")
    rtext(f, Ys, "Y", 2, -10, "blu")
    rtext(f, Zs, "Z", -18, -4, "blu")
    print("riduzioni ortogonale:", round(rx, 3), round(ry, 3), round(rz, 3))
    return f, (Xs, Ys, Zs, O1, O2)


def ortogonale_salva():
    f, pts = ortogonale_foglio()
    ys = [p[1] for p in pts]
    f.h = int(max(ys) + 56)
    note(f, f.h, [
        "In verde la faccia xOy ribaltata intorno a XY, in arancio la faccia yOz ribaltata intorno a YZ:",
        "O* sta sulla semicirconferenza (angolo retto in O*) e sulla perpendicolare alla cerniera da O′.",
        "L'unità vera u* sugli assi ribaltati torna sugli assi con la perpendicolare alla cerniera: u′ è più corta."])
    f.h += 66
    f.salva(OUT + "b11-ortogonale-ribaltamento-piani-coordinati.svg")


# =====================================================================
# 2. Assonometria ortogonale nello spazio: il quadro taglia i tre assi
# =====================================================================

def ortogonale_spazio():
    f = Figura(600, 470, 0, "Nello spazio: il quadro taglia gli assi e O′ cade nell'ortocentro")
    X3 = 400
    t = TriedroLavagna(f, (330, 190), X3=X3, U=330, Y=300, Z=270, scala=0.62)
    t.piani(etichette=False)
    t.testo((110, 120, 0), "π_1", 0, 0, "grigio", 15)
    t.testo((110, 0, 240), "π_2", 0, 0, "grigio", 15)
    t.testo((X3, 270, 250), "π_3", -10, 0, "grigio", 15)
    a, b, c = 130, 270, 240
    O = (X3, 0, 0)
    X, Y, Z = (X3 - a, 0, 0), (X3, b, 0), (X3, 0, c)
    # piano del quadro: x' = X3 - x ; (X3 - x)/a + y/b + z/c = 1
    n = (-1 / a, 1 / b, 1 / c)
    d = 1 - X3 / a
    t.piano(n, d, "blu", 0.20)
    for P, Q in ((X, Y), (Y, Z), (Z, X)):
        t.segmento(P, Q, "blu", 2)
    # piede della perpendicolare da O al quadro
    nn = dot(n, n)
    lam = (d - dot(n, O)) / nn
    Oq = add(O, mul(n, lam))
    t.segmento(O, Oq, "rosso", 1.6, "5,4")
    for V in (X, Y, Z):
        t.segmento(Oq, V, "nero", 1.6)
    t.punto(O, "O", 8, 14)
    t.punto(Oq, "O′", -26, -6, "rosso")
    t.punto(X, "X", -20, -4, "blu")
    t.punto(Y, "Y", 8, 4, "blu")
    t.punto(Z, "Z", 8, 4, "blu")
    t.testo((X3 - a - 40, 0, 0), "x", -4, 18, "nero", 15)
    t.testo((X3, b + 25, 0), "y", 4, 16, "nero", 15)
    t.testo((X3, 0, c + 25), "z", 8, 0, "nero", 15)
    note(f, 486, [
        "Il quadro (in blu) taglia gli assi in X, Y, Z: il triangolo XYZ è il triangolo delle tracce.",
        "La proiettante da O è perpendicolare al quadro e lo buca in O′, l'ortocentro del triangolo;",
        "O′X, O′Y, O′Z sono gli assi x′, y′, z′ e stanno sulle altezze del triangolo."])
    f.h = 550
    f.salva(OUT + "b11-spazio-ortogonale-triangolo-tracce.svg")


# =====================================================================
# 3. Cavaliera militare nello spazio: la squadretta
# =====================================================================

def cavaliera_spazio():
    f = Figura(620, 470, 0, "Cavaliera militare nello spazio: il quadro è π₁, la squadretta è verticale")
    k = 120
    cs, sn = math.cos(math.radians(30)), math.sin(math.radians(30))
    org = (270, 250)

    def p(P):
        x, y, z = P
        return (org[0] - x * cs * k + y * cs * k, org[1] + (x + y) * sn * k * 0.75 - z * k)

    # direzione di z' sul quadro: verso il fondo, a destra
    Wd = unit((-1.0, -0.12, 0))
    quadro = [(1.6, -0.9, 0), (1.6, 1.2, 0), (-1.8, 1.2, 0), (-1.8, -0.9, 0)]
    rpoly(f, [p(v) for v in quadro], "#9aa5b1", 0.12, "#b7bfc8", 1)
    rtext(f, p((-1.8, -0.9, 0)), "π₁ = quadro", 8, 0, "grigio", 14, True)
    O = (0, 0, 0)
    u = 1.0
    rline(f, p(O), p((1.45, 0, 0)), "nero", 1.8)
    rline(f, p(O), p((0, 1.35, 0)), "nero", 1.8)
    rline(f, p(O), p((0, 0, 1.55)), "nero", 1.8)
    rtext(f, p((1.45, 0, 0)), "x ≡ x′", -50, 2)
    rtext(f, p((0, 1.35, 0)), "y ≡ y′", 8, 12)
    rtext(f, p((0, 0, 1.55)), "z", 8, 4)
    for P, dx, dy in (((u, 0, 0), -6, 22), ((0, u, 0), -4, 22)):
        rdot(f, p(P))
        rtext(f, p(P), "u", dx, dy, "nero", 14)
    ranglo(f, p(O), u2(p(O), p((1, 0, 0))), u2(p(O), p((0, 1, 0))), 11)
    Uz = (0, 0, u)
    zfine = mul(Wd, 2.0)
    rline(f, p(O), p(zfine), "rosso", 2)
    rtext(f, p(zfine), "z′", 6, 4, "rosso")
    rpoly(f, [p(O), p(Uz), p(mul(Wd, u))], "verde", 0.16)
    casi = [(0.55, "arancio", "u′_z < u", -60, 70), (1.0, "verde", "45°: u′_z = u", -10, 66),
            (1.6, "viola", "u′_z > u", -10, 32)]
    for r, col, s_, dx, dy in casi:
        Q = mul(Wd, u * r)
        rline(f, p(Uz), p(Q), col, 2)
        rdot(f, p(Q), col)
        rline(f, p(Q), (p(Q)[0] + dx + 16, p(Q)[1] + dy - 14), col, 0.8)
        rtext(f, p(Q), s_, dx, dy, col, 14)
    ranglo(f, p(O), u2(p(O), p(Uz)), u2(p(O), p(Wd)), 10)
    rdot(f, p(Uz))
    rtext(f, p(Uz), "U_z", -32, 4)
    rdot(f, p(O))
    rtext(f, p(O), "O ≡ O′", -64, -8)
    rtext(f, p(mul(Uz, 0.5)), "u", -16, 4, "nero", 14)
    note(f, 405, [
        "Il triangolo verde è la squadretta: un cateto è l'unità u sull'asse z, l'altro è u′z sul quadro,",
        "l'ipotenusa è la direzione di proiezione. A 45° i cateti sono uguali (u′z = u);",
        "con una direzione più ripida u′z si accorcia (arancio), con una più inclinata si allunga (viola)."])
    f.h = 465
    f.salva(OUT + "b11-spazio-cavaliera-squadretta.svg")


# =====================================================================
# Cavaliera militare sul foglio
# =====================================================================
AX = (math.cos(math.radians(210)), -math.sin(math.radians(210)))   # x' in coordinate SVG (y in basso)
AY = (math.cos(math.radians(300)), -math.sin(math.radians(300)))   # y'


def cav(org, k, kz):
    def p(P):
        x, y, z = P
        return (org[0] + (x * AX[0] + y * AY[0]) * k, org[1] + (x * AX[1] + y * AY[1]) * k - z * kz * k)
    R1 = (AX[0], AY[0], 0)
    R2 = (-AX[1], -AY[1], kz)          # y schermo verso l'alto
    return p, vista_da(R1, R2)


# =====================================================================
# 4. Cavaliera: ribaltamento dell'asse z
# =====================================================================

def cavaliera_ribaltamento():
    f = Figura(600, 470, 0, "Cavaliera militare: il ribaltamento dell'asse z")
    k = 60
    org = (240, 220)
    p, _ = cav(org, k, 1)
    O = org
    fx, fy = p((3.3, 0, 0)), p((0, 2.7, 0))
    fz, fs = (org[0], org[1] - 3.2 * k), (org[0] + 5.6 * k, org[1])
    rline(f, O, fx, "nero", 1.8)
    rline(f, O, fy, "nero", 1.8)
    rline(f, O, fz, "nero", 1.8)
    rline(f, O, fs, "rosso", 1.6)
    ranglo(f, O, AX, AY, 10)
    ranglo(f, O, (0, -1), (1, 0), 10)
    rtext(f, fx, "x′ ≡ x*", -50, 20)
    rtext(f, fy, "y′ ≡ y*", 6, 16)
    rtext(f, fz, "z′", 8, 4)
    rtext(f, fs, "z*", -8, 22, "rosso")
    rdot(f, O)
    rtext(f, O, "O′", -28, -8)
    rid = 0.75
    Ux, Uy = p((1, 0, 0)), p((0, 1, 0))
    Us, Uq = (org[0] + k, org[1]), (org[0], org[1] - rid * k)
    # arco del compasso: da u su x' fino a z*, passando per y'
    rarc(f, O, k, Ux, Us, 0, 0)
    for P, dx, dy in ((Ux, -6, -10), (Uy, 8, 4)):
        rdot(f, P)
        rtext(f, P, "u", dx, dy, "nero", 14)
    rdot(f, Us, "rosso")
    rtext(f, Us, "u", 4, 20, "rosso", 14)
    h = 2.6
    Hs, Hq = (org[0] + h * k, org[1]), (org[0], org[1] - h * rid * k)
    rline(f, Us, Uq, "verde", 2.2)
    rline(f, Hs, Hq, "verde", 1.4, "7,4")
    rdot(f, Uq, "verde")
    rtext(f, Uq, "u′_z", -40, 6, "verde", 14)
    rdot(f, Hs, "rosso")
    rtext(f, Hs, "h", -4, 22, "rosso", 15)
    rdot(f, Hq, "verde")
    rtext(f, Hq, "h′", -28, 4, "verde", 15)
    m = ((Us[0] + Uq[0]) / 2, (Us[1] + Uq[1]) / 2)
    rtext(f, m, "s*", 4, -6, "verde", 15)
    m2 = ((Hs[0] * 0.45 + Hq[0] * 0.55), (Hs[1] * 0.45 + Hq[1] * 0.55))
    rtext(f, m2, "parallela a s*", 8, -6, "verde", 13)
    # lineette di uguaglianza sulle unita'
    for A, B in ((O, Ux), (O, Uy), (O, Us)):
        mm = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
        d = u2(A, B)
        nn = (-d[1] * 6, d[0] * 6)
        rline(f, (mm[0] - nn[0], mm[1] - nn[1]), (mm[0] + nn[0], mm[1] + nn[1]), "nero", 1.2)
    note(f, 420, [
        "u è la stessa su x′, y′ e z* (una lineetta: misure uguali, riportate col compasso); u′z su z′ si sceglie.",
        "s* unisce u su z* con u′z su z′; un'altezza vera h presa su z* va su z′ con la parallela a s*: è h′."])
    f.h = 462
    f.salva(OUT + "b11-cavaliera-ribaltamento-asse-z.svg")


# =====================================================================
# 5. Cavaliera: l'esercizio del prisma (pianta 4 x 2 cm, altezza 5 cm)
# =====================================================================

def cavaliera_prisma():
    f = Figura(620, 520, 0, "Esercizio: prisma con pianta 4 × 2 cm e altezza 5 cm")
    k = 25                    # 1 cm = 25 px
    rid = 0.75                # u'z / u = 1,5 / 2
    org = (300, 240)
    p, vista = cav(org, k, rid)
    x0, x1, y0, y1, H = 1.5, 5.5, 1.5, 3.5, 5.0
    # assi
    fx, fy, fz = p((8.4, 0, 0)), p((0, 6.4, 0)), p((0, 0, 7.6 / rid))
    rline(f, org, fx, "nero", 1.8)
    rline(f, org, fy, "nero", 1.8)
    rline(f, org, fz, "nero", 1.8)
    ranglo(f, org, AX, AY, 9)
    # ribaltamento di z e direzione s*
    zs_end = (org[0] + 7.2 * k, org[1])
    rline(f, org, zs_end, "rosso", 1.6)
    Us, Uq = (org[0] + 2 * k, org[1]), p((0, 0, 2))
    Hs, Hq = (org[0] + H * k, org[1]), p((0, 0, H))
    Ux, Uy = p((2, 0, 0)), p((0, 2, 0))
    rarc(f, org, 2 * k, Ux, Us, 0, 0)
    rline(f, Us, Uq, "verde", 2)
    rline(f, Hs, Hq, "verde", 1.4, "7,4")
    # altezza h' riportata sui piani coordinati: parallele a x' e a y'
    rline(f, Hq, p((x1 + 0.6, 0, H)), "grigio", 1, "3,3")
    rline(f, Hq, p((0, y1 + 0.6, H)), "grigio", 1, "3,3")
    # seconda proiezione (su pi2, y = 0) e terza (su pi3, x = 0)
    sec = [(x0, 0, 0), (x1, 0, 0), (x1, 0, H), (x0, 0, H)]
    ter = [(0, y0, 0), (0, y1, 0), (0, y1, H), (0, y0, H)]
    rpoly(f, [p(v) for v in sec], "arancio", 0.16, "arancio", 1.8)
    rpoly(f, [p(v) for v in ter], "viola", 0.16, "viola", 1.8)
    # proiezioni della pianta sugli assi
    for x in (x0, x1):
        rline(f, p((x, y0, 0)), p((x, 0, 0)), "grigio", 1, "3,3")
    for y in (y0, y1):
        rline(f, p((x1, y, 0)), p((0, y, 0)), "grigio", 1, "3,3")
    # il solido: le facce visibili, quasi opache, coprono quello che sta dietro
    facce = scatola(x0, x1, y0, y1, 0, H)
    disegna_solido(f, p, facce, vista, "blu", 0.85, 2.2, True, "#e8eff8")
    # punti e scritte sopra a tutto
    rtext(f, fx, "x′ ≡ x*", -52, 18)
    rtext(f, fy, "y′ ≡ y*", 6, 14)
    rtext(f, fz, "z′", 8, 4)
    rtext(f, zs_end, "z*", -8, 22, "rosso")
    rdot(f, Us, "rosso"); rtext(f, Us, "2", -4, 20, "rosso", 14)
    rdot(f, Hs, "rosso"); rtext(f, Hs, "5", -4, 20, "rosso", 14)
    rdot(f, Uq, "verde")      # u'z = 1,5 cm (detto nella didascalia: qui la scritta coprirebbe il solido)
    rdot(f, Hq, "verde"); rtext(f, Hq, "h′", 6, -6, "verde", 15)
    rtext(f, Us, "s*", 4, -12, "verde", 14)
    rdot(f, Ux); rtext(f, Ux, "2", -6, -8, "nero", 13)
    rdot(f, Uy); rtext(f, Uy, "2", 8, 2, "nero", 13)
    rtext(f, p((x1, y1, 0)), "pianta", -20, 22, "blu", 13)
    rtext(f, p((x1, 0, 0)), "seconda proiezione", -128, -6, "arancio", 13)
    rtext(f, p((0, y1, 0)), "terza proiezione", 10, 14, "viola", 13)
    note(f, 462, [
        "Unità 2 cm su x′ e y′ (uguali, vere) e 1,5 cm su z′: s* unisce 2 su z* con 1,5 su z′.",
        "L'altezza vera 5 cm, portata da z* a z′ con la parallela a s*, diventa h′ = 3,75 cm.",
        "Pianta in vera forma; prospetti assonometrici su π₂ (arancio) e π₃ (viola); il solido, in blu."])
    f.h = 520
    f.salva(OUT + "b11-cavaliera-esercizio-prisma.svg")


# =====================================================================
# Sezione con un piano parallelo alla LT: dati comuni
# =====================================================================
BX0, BX1, BY0, BY1, BH = 40, 160, 30, 120, 150      # parallelepipedo 4 x 3 x 5 (1 = 30 px)
AQ, AA = 140, 210                                   # alfa: t2 a quota 140, t1 ad aggetto 210


def za(y):
    return AQ * (1 - y / AA)


ZR, ZM = za(BY1), za(BY0)     # quota della sezione sulla faccia anteriore (r) e posteriore (m)


def arco_terza(f, X3, y):
    sx, sy = f._s((X3, -y))
    ex, ey = f._s((X3 + y, 0))
    f.parti.append(f'<path d="M {sx:.1f} {sy:.1f} A {y:.1f} {y:.1f} 0 0 0 {ex:.1f} {ey:.1f}" '
                   f'fill="none" stroke="{COLORI["grigio"]}" stroke-width="0.9" stroke-dasharray="3,3"/>')


def orizz(f, x1, x2, y):
    f._linea((x1, y), (x2, y), "grigio", 0.9, "3,3")


def poly(f, pts, colore="blu", opacita=0.12, bordo=None, spessore=1.6, tratteggio=None, retino_=False):
    rpoly(f, [f._s(q) for q in pts], colore, opacita, bordo, spessore, tratteggio, retino_)


# =====================================================================
# 6. Sezione con piano parallelo alla LT in proiezioni ortogonali
# =====================================================================

def sezione_po_parallela():
    X3 = 250
    alto, basso = 180, 240
    f = Figura(640, alto + basso + 10, alto + 6, "Sezione con un piano α parallelo alla LT (proiezioni ortogonali)", x0=120)
    retino(f)
    f.lt(-110, X3 + AA + 40)
    f._linea((X3, alto), (X3, -basso), "nero", 1.2)
    f.testo((-110, alto), "π_2", 4, 12, "grigio", 13, False)
    f.testo((-110, -basso), "π_1", 4, 16, "grigio", 13, False)
    f.testo((X3, alto), "π_3", 8, 12, "grigio", 13, False)
    # tracce di alfa
    f.traccia((-110, AQ), (X3, AQ)); f.testo((-110, AQ), "t_2α", 0, -8)
    f.traccia((-110, -AA), (X3, -AA)); f.testo((-110, -AA), "t_1α", 0, -8)
    f.traccia((X3, AQ), (X3 + AA, 0)); f.testo((X3 + AA * 0.7, AQ * 0.3), "t_3α", 8, -8)
    arco_terza(f, X3, AA)
    # piani delle facce: delta (anteriore, y = BY1) e gamma (posteriore, y = BY0)
    for y, nome, col, dy in ((BY1, "δ", "arancio", 18), (BY0, "γ", "viola", -8)):
        f._linea((-110, -y), (X3, -y), col, 1.6)
        f._linea((X3 + y, 0), (X3 + y, alto - 10), col, 1.6)
        arco_terza(f, X3, y)
        f.testo((X3 + y, alto - 10), f"t_3{nome}", 4, 10, col, 14)
    f.testo((-110, -BY1), "t_1δ ≡ r_1", 0, 18, "arancio", 14)
    f.testo((-110, -BY0), "t_1γ ≡ m_1", 0, -6, "viola", 14)
    # solido: parte eliminata in grigio
    poly(f, [(BX0, ZR), (BX1, ZR), (BX1, BH), (BX0, BH)], "grigio", 0.0, "grigio", 1, "5,4")
    poly(f, [(X3 + BY0, ZM), (X3 + BY0, BH), (X3 + BY1, BH), (X3 + BY1, ZR)], "grigio", 0.0, "grigio", 1, "5,4")
    # seconda proiezione: faccia anteriore (blu) + sezione (rossa)
    poly(f, [(BX0, 0), (BX1, 0), (BX1, ZR), (BX0, ZR)], "blu", 0.12, "blu", 2)
    poly(f, [(BX0, ZR), (BX1, ZR), (BX1, ZM), (BX0, ZM)], "rosso", 0, "rosso", 2.4, None, True)
    # terza proiezione
    poly(f, [(X3 + BY0, 0), (X3 + BY1, 0), (X3 + BY1, ZR), (X3 + BY0, ZM)], "blu", 0.12, "blu", 2)
    f._linea((X3 + BY1, ZR), (X3 + BY0, ZM), "rosso", 4)
    # prima proiezione: la sezione copre la pianta
    poly(f, [(BX0, -BY0), (BX1, -BY0), (BX1, -BY1), (BX0, -BY1)], "rosso", 0, "rosso", 2.4, None, True)
    # rette r e m in seconda proiezione e richiami
    f._linea((-110, ZR), (BX0, ZR), "rosso", 1.6)
    f._linea((-110, ZM), (BX0, ZM), "rosso", 1.6)
    f.testo((-110, ZR), "r_2", 0, -6, "rosso", 14)
    f.testo((-110, ZM), "m_2", 0, -6, "rosso", 14)
    orizz(f, BX1, X3 + BY1, ZR)
    orizz(f, BX1, X3 + BY0, ZM)
    for x in (BX0, BX1):
        f.richiamo(x, -BY1, 0)
    f.punto((X3 + BY1, ZR), "r_3", -24, 20, "rosso")
    f.punto((X3 + BY0, ZM), "m_3", 8, -8, "rosso")
    for P, s, dx, dy in (((BX1, ZR), "1_2", 6, 16), ((BX0, ZR), "2_2", -22, 16),
                         ((BX0, ZM), "3_2", -22, -6), ((BX1, ZM), "4_2", 6, -6),
                         ((BX1, -BY1), "1_1", 6, 18), ((BX0, -BY1), "2_1", -22, 18),
                         ((BX0, -BY0), "3_1", -22, -6), ((BX1, -BY0), "4_1", 6, -6)):
        f.punto(P, s, dx, dy)
    note(f, alto + basso + 40, [
        "In terza proiezione α si vede di taglio: r₃ è dove t₃α incontra t₃δ, m₃ dove incontra t₃γ.",
        "r ed m sono parallele alla LT (r₁ ≡ t₁δ, m₁ ≡ t₁γ): r₂ e m₂ tagliano gli spigoli in 1, 2 e 3, 4.",
        "La sezione si campisce; la parte di solido sopra α si elimina (in grigio)."])
    f.h = alto + basso + 100
    f.salva(OUT + "b11-sezione-po-piano-parallelo-lt.svg")


# =====================================================================
# 7. Sezione con piano parallelo alla LT nello spazio
# =====================================================================

def sezione_spazio_parallela():
    f = Figura(600, 500, 0, "Nello spazio: il piano α parallelo alla LT taglia il parallelepipedo")
    retino(f)
    X3 = 400
    t = TriedroLavagna(f, (320, 190), X3=X3, U=380, Y=260, Z=210, scala=0.68)
    t.piani(etichette=False)
    t.testo((330, 235, 0), "π_1", 0, 0, "grigio", 15)
    t.testo((170, 0, 195), "π_2", 0, 0, "grigio", 15)
    t.testo((X3, 230, 195), "π_3", 0, 0, "grigio", 15)
    dx = 120                                  # il solido spostato a destra lungo la LT
    x0, x1 = BX0 + dx, BX1 + dx
    n, d = (0, AQ / AA, 1), AQ
    t.piano(n, d, "rosso", 0.07)
    tr = t.tracce(n, d, "nero")
    t.testo((70, 0, AQ), "t_2α", 0, -12, "nero", 13)
    t.testo((70, AA, 0), "t_1α", -4, 16, "nero", 13)
    t.testo((X3, AA * 0.55, za(AA * 0.55)), "t_3α", 8, 0, "nero", 13)
    p = t._p
    # parte eliminata
    for a_, b_ in (((x0, BY0, ZM), (x0, BY0, BH)), ((x1, BY0, ZM), (x1, BY0, BH)),
                   ((x0, BY1, ZR), (x0, BY1, BH)), ((x1, BY1, ZR), (x1, BY1, BH))):
        rline(f, p(a_), p(b_), "grigio", 1, "5,4")
    rpoly(f, [p((x0, BY0, BH)), p((x1, BY0, BH)), p((x1, BY1, BH)), p((x0, BY1, BH))], "grigio", 0, "grigio", 1, "5,4")
    # solido rimasto (convesso): base, facce verticali tagliate, sezione
    S1, S2, S3, S4 = (x1, BY1, ZR), (x0, BY1, ZR), (x0, BY0, ZM), (x1, BY0, ZM)
    facce = [
        [(x0, BY0, 0), (x1, BY0, 0), (x1, BY1, 0), (x0, BY1, 0)],
        [(x0, BY1, 0), (x1, BY1, 0), S1, S2],
        [(x0, BY0, 0), (x1, BY0, 0), S4, S3],
        [(x0, BY0, 0), (x0, BY1, 0), S2, S3],
        [(x1, BY0, 0), (x1, BY1, 0), S1, S4],
        [S1, S2, S3, S4],
    ]
    disegna_solido(f, p, facce, VISTA_TRIEDRO, "blu", 0.12, 2)
    rpoly(f, [p(S1), p(S2), p(S3), p(S4)], "rosso", 0, "rosso", 2.4, None, True)
    # rette r e m: dalla terza traccia fino oltre il solido
    rline(f, p((x0 - 40, BY1, ZR)), p((X3, BY1, ZR)), "rosso", 1.4)
    rline(f, p((x0 - 40, BY0, ZM)), p((X3, BY0, ZM)), "rosso", 1.4)
    rdot(f, p((X3, BY1, ZR)), "rosso")
    rdot(f, p((X3, BY0, ZM)), "rosso")
    rtext(f, p((x0 - 40, BY1, ZR)), "r", -14, 4, "rosso")
    rtext(f, p((x0 - 40, BY0, ZM)), "m", -18, 4, "rosso")
    for P, s, ddx, ddy in ((S1, "1", 6, 16), (S2, "2", -14, 16), (S3, "3", -14, -4), (S4, "4", 4, -8)):
        rdot(f, p(P))
        rtext(f, p(P), s, ddx, ddy, "nero", 14)
    note(f, 516, [
        "La faccia anteriore (piano δ) e quella posteriore (piano γ) sono tagliate da α lungo r ed m,",
        "parallele alla LT, che partono dai punti di π₃ dove t₃α incontra t₃δ e t₃γ.",
        "La sezione 1-2-3-4 (in rosso) è inclinata; la parte del solido sopra α (in grigio) si elimina."])
    f.h = 576
    f.salva(OUT + "b11-spazio-sezione-piano-parallelo-lt.svg")


# =====================================================================
# 8. Sezione con piano parallelo alla LT in cavaliera militare
# =====================================================================

def sezione_cavaliera():
    f = Figura(620, 640, 0, "La stessa sezione in cavaliera militare")
    retino(f)
    k = 1.0
    org = (370, 250)
    p, vista = cav(org, k, 1)
    # assi
    for P, s, ddx, ddy in (((250, 0, 0), "x′", -18, 16), ((0, 275, 0), "y′", 6, 14), ((0, 0, 200), "z′", 8, 4)):
        rline(f, org, p(P), "nero", 1.6)
        rtext(f, p(P), s, ddx, ddy)
    rdot(f, org); rtext(f, org, "O′", 28, 6)
    # tracce di alfa
    rline(f, p((0, 0, AQ)), p((215, 0, AQ)), "nero", 2.4)
    rline(f, p((0, AA, 0)), p((215, AA, 0)), "nero", 2.4)
    rline(f, p((0, 0, AQ)), p((0, AA, 0)), "nero", 2.4)
    rtext(f, p((215, 0, AQ)), "t_2′α", -36, -6)
    rtext(f, p((215, AA, 0)), "t_1′α", -40, 18)
    rtext(f, p((0, AA * 0.62, za(AA * 0.62))), "t_3′α", 8, 0)
    # piani beta (faccia anteriore) e gamma (posteriore)
    for y, nome, col, ddy in ((BY1, "β", "arancio", 18), (BY0, "γ", "viola", 18)):
        rline(f, p((0, y, 0)), p((195, y, 0)), col, 1.6)
        rline(f, p((0, y, 0)), p((0, y, 185)), col, 1.6)
        rtext(f, p((195, y, 0)), f"t_1′{nome}", -40, ddy, col, 14)
        rtext(f, p((0, y, 185)), f"t_3′{nome}", 4, -4, col, 14)
    # parte eliminata
    S1, S2, S3, S4 = (BX1, BY1, ZR), (BX0, BY1, ZR), (BX0, BY0, ZM), (BX1, BY0, ZM)
    for P in (S1, S2, S3, S4):
        rline(f, p(P), p((P[0], P[1], BH)), "grigio", 1, "5,4")
    rpoly(f, [p((BX0, BY0, BH)), p((BX1, BY0, BH)), p((BX1, BY1, BH)), p((BX0, BY1, BH))], "grigio", 0, "grigio", 1, "5,4")
    facce = [
        [(BX0, BY0, 0), (BX1, BY0, 0), (BX1, BY1, 0), (BX0, BY1, 0)],
        [(BX0, BY1, 0), (BX1, BY1, 0), S1, S2],
        [(BX0, BY0, 0), (BX1, BY0, 0), S4, S3],
        [(BX0, BY0, 0), (BX0, BY1, 0), S2, S3],
        [(BX1, BY0, 0), (BX1, BY1, 0), S1, S4],
        [S1, S2, S3, S4],
    ]
    disegna_solido(f, p, facce, vista, "blu", 0.12, 2.2)
    rpoly(f, [p(S1), p(S2), p(S3), p(S4)], "rosso", 0, "rosso", 2.6, None, True)
    # rette r' e m'
    rline(f, p((0, BY1, ZR)), p((BX1 + 35, BY1, ZR)), "rosso", 1.4)
    rline(f, p((0, BY0, ZM)), p((BX1 + 35, BY0, ZM)), "rosso", 1.4)
    rdot(f, p((0, BY1, ZR)), "rosso"); rdot(f, p((0, BY0, ZM)), "rosso")
    rtext(f, p((BX1 + 35, BY1, ZR)), "r′", -18, 16, "rosso")
    rtext(f, p((BX1 + 35, BY0, ZM)), "m′", -22, -2, "rosso")
    for P, s, ddx, ddy in ((S1, "1", -14, 16), (S2, "2", 6, 16), (S3, "3", 6, -6), (S4, "4", -16, -4)):
        rdot(f, p(P))
        rtext(f, p(P), s, ddx, ddy, "nero", 14)
    note(f, 580, [
        "1. Il piano β della faccia anteriore: t₁′β parallela a x′, t₃′β parallela a z′.",
        "2. r = α ∩ β parte da dove t₃′α incontra t₃′β ed è parallela a x′. 3. r′ taglia gli spigoli della faccia in 1 e 2.",
        "Lo stesso con γ (faccia posteriore): m′ dà 3 e 4. La sezione 1-2-3-4 si ripassa e si campisce."])
    f.h = 642
    f.salva(OUT + "b11-sezione-cavaliera-piano-parallelo-lt.svg")


# =====================================================================
# Sezione con un piano verticale: dati comuni
# =====================================================================
PHI, PSI = math.radians(25), math.radians(62)
A0 = (150.0, 40.0)
LL, WW, HV = 175.0, 72.0, 130.0
DD = (math.cos(PHI), math.sin(PHI))
NN = (-math.sin(PHI), math.cos(PHI))
B0 = A0
B1 = (A0[0] + LL * DD[0], A0[1] + LL * DD[1])
B2 = (B1[0] + WW * NN[0], B1[1] + WW * NN[1])
B3 = (A0[0] + WW * NN[0], A0[1] + WW * NN[1])
CEN = (A0[0] + 0.42 * LL * DD[0] + 0.5 * WW * NN[0], A0[1] + 0.42 * LL * DD[1] + 0.5 * WW * NN[1])
DA = (math.cos(PSI), math.sin(PSI))
NA = (-DA[1], DA[0])          # verso la parte eliminata (sinistra)
TR = inter2(CEN, (CEN[0] + DA[0], CEN[1] + DA[1]), B3, B2)    # su beta (anteriore)
TM = inter2(CEN, (CEN[0] + DA[0], CEN[1] + DA[1]), B0, B1)    # su gamma (posteriore)


def lato(q):
    return (q[0] - CEN[0]) * NA[0] + (q[1] - CEN[1]) * NA[1]


def taglia(poligono, tieni_destra=True):
    out = []
    for a, b in zip(poligono, poligono[1:] + poligono[:1]):
        la, lb = lato(a), lato(b)
        ina = la <= 0 if tieni_destra else la >= 0
        inb = lb <= 0 if tieni_destra else lb >= 0
        if ina:
            out.append(a)
        if ina != inb:
            t = la / (la - lb)
            out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    return out


DESTRA = taglia([B0, B1, B2, B3], True)
SINISTRA = taglia([B0, B1, B2, B3], False)


# =====================================================================
# 9. Sezione con piano verticale in proiezioni ortogonali
# =====================================================================

def sezione_po_verticale():
    alto, basso = 175, 250
    f = Figura(560, alto + basso + 10, alto + 6, "Sezione con un piano α verticale (proiezioni ortogonali)", x0=30)
    retino(f)
    f.lt(-10, 480)
    f.testo((-10, alto), "π_2", 4, 12, "grigio", 13, False)
    f.testo((-10, -basso), "π_1", 4, 16, "grigio", 13, False)
    # t1alfa e t2alfa
    xa = CEN[0] - CEN[1] * DA[0] / DA[1]          # dove t1alfa incontra la LT
    yfine = 205
    f.traccia((xa, 0), (xa + (yfine) * DA[0] / DA[1], -yfine))
    f.traccia((xa, 0), (xa, alto - 15))
    f.testo((xa + yfine * DA[0] / DA[1], -yfine), "t_1α", 6, 6)
    f.testo((xa, alto - 15), "t_2α", -34, 12)
    # tracce dei piani delle facce: prolungamento dei lati lunghi
    for P, Q, nome, col in ((B3, B2, "β", "arancio"), (B0, B1, "γ", "viola")):
        a = (P[0] - (70 if nome == "β" else 25) * DD[0], P[1] - (70 if nome == "β" else 25) * DD[1])
        b = (Q[0] + 50 * DD[0], Q[1] + 50 * DD[1])
        f._linea(P1((a[0], a[1], 0)), P1((b[0], b[1], 0)), col, 1.6)
        f.testo(P1((b[0], b[1], 0)), f"t_1{nome}", 4, 12, col, 14)
    # pianta: parte eliminata e parte rimasta
    poly(f, [P1((q[0], q[1], 0)) for q in SINISTRA], "grigio", 0, "grigio", 1, "5,4")
    poly(f, [P1((q[0], q[1], 0)) for q in DESTRA], "blu", 0.12, "blu", 2)
    f._linea(P1((TR[0], TR[1], 0)), P1((TM[0], TM[1], 0)), "rosso", 4.5)
    # seconda proiezione: parte eliminata in grigio
    xs_s = [q[0] for q in SINISTRA]
    poly(f, [(min(xs_s), 0), (max(xs_s), 0), (max(xs_s), HV), (min(xs_s), HV)], "grigio", 0, "grigio", 1, "5,4")
    # parte rimasta: facce visibili da davanti (y crescente)
    xs = [q[0] for q in DESTRA]
    xmin, xmax = min(xs), max(xs)
    poly(f, [(xmin, 0), (xmax, 0), (xmax, HV), (xmin, HV)], "blu", 0.12, "blu", 2)
    poly(f, [(TM[0], 0), (TR[0], 0), (TR[0], HV), (TM[0], HV)], "rosso", 0, "rosso", 2.4, None, True)
    # spigoli verticali interni: visibili se nessun punto del solido sta davanti
    for q in DESTRA:
        if abs(q[0] - xmin) < 1e-6 or abs(q[0] - xmax) < 1e-6:
            continue
        if abs(q[0] - TR[0]) < 1e-6 or abs(q[0] - TM[0]) < 1e-6:
            continue
        davanti = any(c[1] > q[1] + 1e-6 and abs(c[0] - q[0]) < 1 for c in DESTRA)
        # verifica piu' precisa: la verticale per q attraversa il poligono davanti a q?
        ys = []
        for a, b in zip(DESTRA, DESTRA[1:] + DESTRA[:1]):
            if (a[0] - q[0]) * (b[0] - q[0]) < 0:
                ys.append(a[1] + (b[1] - a[1]) * (q[0] - a[0]) / (b[0] - a[0]))
        nascosto = any(y > q[1] + 1e-6 for y in ys)
        f._linea((q[0], 0), (q[0], HV), "blu", 1.2 if nascosto else 2, "5,4" if nascosto else None)
    # richiami e rette r, m
    for T in (TR, TM):
        f.richiamo(T[0], -T[1], 0)
    for P in DESTRA:
        if abs(P[0] - TR[0]) > 1 and abs(P[0] - TM[0]) > 1:
            f.richiamo(P[0], -P[1], 0)
    f._linea((TR[0], 0), (TR[0], HV + 30), "rosso", 1.6)
    f._linea((TM[0], 0), (TM[0], HV + 30), "rosso", 1.6)
    f.testo((TR[0], HV + 30), "r_2", 4, 4, "rosso", 14)
    f.testo((TM[0], HV + 30), "m_2", -26, 4, "rosso", 14)
    f.punto((TR[0], 0), "(T_{1r})_2", 4, 20, "nero")
    f.punto((TM[0], 0), "(T_{1m})_2", -62, 20, "nero")
    f.punto(P1((TR[0], TR[1], 0)), "r_1 ≡ T_{1r}", -100, 24, "rosso")
    f.punto(P1((TM[0], TM[1], 0)), "m_1 ≡ T_{1m}", -88, -6, "rosso")
    for P, s, ddx, ddy in (((TR[0], HV), "1_2", 6, 16), ((TR[0], 0), "2_2", 6, -6),
                           ((TM[0], 0), "3_2", -22, -6), ((TM[0], HV), "4_2", -22, 16)):
        f.punto(P, s, ddx, ddy)
    note(f, alto + basso + 40, [
        "β (faccia anteriore) e γ (faccia posteriore) sono proiettanti in prima, come il piano secante α.",
        "r = α ∩ β è verticale: r₁ ≡ T₁ᵣ, r₂ ⊥ LT (T₂ᵣ all'infinito); taglia gli spigoli orizzontali in 1 e 2.",
        "Lo stesso con γ: m dà 3 e 4. In pianta la sezione è il segmento T₁ᵣT₁ₘ su t₁α, che si rinforza."])
    f.h = alto + basso + 100
    f.salva(OUT + "b11-sezione-po-piano-verticale.svg")
    print("TR, TM:", TR, TM, "xa:", xa)


# =====================================================================
# 10. Sezione con piano verticale nello spazio
# =====================================================================

def sezione_spazio_verticale():
    f = Figura(600, 500, 0, "Nello spazio: due piani verticali si tagliano in una retta verticale")
    retino(f)
    X3 = 400
    t = TriedroLavagna(f, (320, 190), X3=X3, U=380, Y=260, Z=200, scala=0.68)
    t.piani(etichette=False)
    t.testo((330, 235, 0), "π_1", 0, 0, "grigio", 15)
    t.testo((60, 0, 60), "π_2", 0, 0, "grigio", 15)
    t.testo((X3, 230, 185), "π_3", 0, 0, "grigio", 15)
    n = (NA[0], NA[1], 0)
    d = NA[0] * CEN[0] + NA[1] * CEN[1]
    t.piano(n, d, "rosso", 0.07)
    tr = t.tracce(n, d, "nero")
    p = t._p
    xa = CEN[0] - CEN[1] * DA[0] / DA[1]
    t.testo((xa, 0, 150), "t_2α", -30, 0, "nero", 13)
    t.testo((xa + 245 * DA[0] / DA[1], 245, 0), "t_1α", 8, 4, "nero", 13)
    # parte eliminata (sinistra) in grigio
    for q in SINISTRA:
        rline(f, p((q[0], q[1], 0)), p((q[0], q[1], HV)), "grigio", 1, "5,4")
    rpoly(f, [p((q[0], q[1], HV)) for q in SINISTRA], "grigio", 0, "grigio", 1, "5,4")
    rpoly(f, [p((q[0], q[1], 0)) for q in SINISTRA], "grigio", 0, "grigio", 1, "5,4")
    # parte rimasta
    base = [(q[0], q[1], 0) for q in DESTRA]
    cima = [(q[0], q[1], HV) for q in DESTRA]
    facce = [base, cima] + [[(a[0], a[1], 0), (b[0], b[1], 0), (b[0], b[1], HV), (a[0], a[1], HV)]
                            for a, b in zip(DESTRA, DESTRA[1:] + DESTRA[:1])]
    disegna_solido(f, p, facce, VISTA_TRIEDRO, "blu", 0.12, 2)
    sez = [(TR[0], TR[1], HV), (TR[0], TR[1], 0), (TM[0], TM[1], 0), (TM[0], TM[1], HV)]
    rpoly(f, [p(q) for q in sez], "rosso", 0, "rosso", 2.4, None, True)
    # rette r e m (verticali) prolungate
    for T, s in ((TR, "r"), (TM, "m")):
        rline(f, p((T[0], T[1], 0)), p((T[0], T[1], HV + 45)), "rosso", 1.4)
        rtext(f, p((T[0], T[1], HV + 45)), s, 4, 0, "rosso")
    for P, s, ddx, ddy in ((sez[0], "1", 6, -4), (sez[1], "2 ≡ T_{1r}", -30, 24), (sez[2], "3 ≡ T_{1m}", 2, 24),
                           (sez[3], "4", -14, -4)):
        rdot(f, p(P))
        rtext(f, p(P), s, ddx, ddy, "nero", 13)
    note(f, 516, [
        "Le facce lunghe del solido stanno su piani verticali (β davanti, γ dietro), come il piano secante α:",
        "α li taglia lungo le rette verticali r ed m, che bucano π₁ in T₁ᵣ e T₁ₘ, sulla traccia t₁α.",
        "La sezione 1-2-3-4 (in rosso) è un rettangolo verticale; la parte sinistra (in grigio) si elimina."])
    f.h = 576
    f.salva(OUT + "b11-spazio-sezione-piano-verticale.svg")


if __name__ == "__main__":
    ortogonale_salva()
    ortogonale_spazio()
    cavaliera_spazio()
    cavaliera_ribaltamento()
    cavaliera_prisma()
    sezione_po_parallela()
    sezione_spazio_parallela()
    sezione_cavaliera()
    sezione_po_verticale()
    sezione_spazio_verticale()
