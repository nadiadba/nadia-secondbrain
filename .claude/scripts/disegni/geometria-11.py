"""Schemi per la sbobina di geometria descrittiva del 10 novembre (11-...):
assonometria ortogonale (triangolo delle tracce e ortocentro) e assonometria obliqua
cavaliera militare (quadro = pi1): direzione di proiezione nello spazio, ribaltamento
dell'asse z per trovare la riduzione delle altezze, esercizio del prisma 4 x 2 cm.

Usa disegni_monge.py senza modificarlo: le proiezioni assonometriche sono calcolate qui.
Coordinate nello spazio (x, y, z) con z verticale; le unita' sono in cm.
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, COLORI, _etichetta

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/sbobine/img/"


def add(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))


def mul(a, k):
    return tuple(x * k for x in a)


def dot(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def unit(a):
    n = math.sqrt(dot(a, a))
    return tuple(x / n for x in a)


def arco(f, centro, r, a0, a1, colore="grigio"):
    """Arco di circonferenza (angoli in gradi, coordinate di disegno con y in alto)."""
    p0 = (centro[0] + r * math.cos(math.radians(a0)), centro[1] + r * math.sin(math.radians(a0)))
    p1 = (centro[0] + r * math.cos(math.radians(a1)), centro[1] + r * math.sin(math.radians(a1)))
    (x0, y0), (x1, y1) = f._s(p0), f._s(p1)
    grande = 1 if abs(a1 - a0) > 180 else 0
    verso = 0 if a1 > a0 else 1      # nel SVG la y e' rovesciata
    f.parti.append(f'<path d="M {x0:.1f} {y0:.1f} A {r:.1f} {r:.1f} 0 {grande} {verso} {x1:.1f} {y1:.1f}" '
                   f'fill="none" stroke="{COLORI[colore]}" stroke-width="1" stroke-dasharray="5,4"/>')


def figura_adattata(punti, titolo, note, margine=60, minimo=560):
    """Figura grande quanto serve per contenere i punti (coordinate di disegno), con le note sotto."""
    xs, ys = [p[0] for p in punti], [p[1] for p in punti]
    w = max(minimo, max(xs) - min(xs) + 2 * margine)
    x0 = (w - (max(xs) - min(xs))) / 2 - min(xs)
    y_lt = max(ys) + margine
    h_disegno = max(ys) - min(ys) + 2 * margine
    f = Figura(int(w), int(h_disegno + 22 * len(note) + 10), y_lt, titolo, x0=x0)
    for i, t in enumerate(note):
        f.nota(18, int(h_disegno + 22 * i + 4), t)
    return f


def tratteggio(f, a, b, colore="nero", spessore=1.4):
    f._linea(a, b, colore, spessore, "6,4")


# =====================================================================
# 1. Assonometria ortogonale: triangolo delle tracce, ortocentro, assi
# =====================================================================

def triangolo_tracce():
    a, b, c = 4.5, 7.0, 6.0                  # dove il quadro taglia x, y, z (triangolo scaleno)
    X, Y, Z = (a, 0, 0), (0, b, 0), (0, 0, c)
    n = unit((1 / a, 1 / b, 1 / c))
    d = dot(n, X)
    Oq = mul(n, d)                            # proiezione ortogonale di O sul quadro
    e1 = unit(add((0, 0, 1), mul(n, -n[2])))  # verticale del quadro: z' viene in verticale
    e2 = cross(e1, n)
    k = 40

    def q(p):
        v = add(p, mul(Oq, -1))
        return (dot(v, e2) * k, dot(v, e1) * k)

    x_, y_, z_, o_ = q(X), q(Y), q(Z), (0, 0)
    est = [(v[0] + unit2(v)[0] * 60, v[1] + unit2(v)[1] * 60) for v in (x_, y_, z_)]
    f = figura_adattata([x_, y_, z_] + est, "Assonometria ortogonale: il triangolo delle tracce", [
        "Il quadro taglia gli assi x, y, z in X, Y, Z: il triangolo XYZ è il triangolo delle tracce.",
        "La proiezione ortogonale dell'origine, O′, cade nell'ortocentro (dove si incontrano le altezze).",
        "Triangolo equilatero: isometria; isoscele: dimetria; scaleno (come qui): trimetria."], 30, 620)
    f.figura([x_, y_, z_], "blu")
    # altezze del triangolo (si incontrano nell'ortocentro)
    for v, (p, r) in ((x_, (y_, z_)), (y_, (x_, z_)), (z_, (x_, y_))):
        # piede dell'altezza da v sul lato pr
        dx, dy = r[0] - p[0], r[1] - p[1]
        t = ((v[0] - p[0]) * dx + (v[1] - p[1]) * dy) / (dx * dx + dy * dy)
        piede = (p[0] + t * dx, p[1] + t * dy)
        f.costruzione(v, piede)
        lu = math.hypot(dx, dy)
        f.angolo_retto(piede, (dx / lu, dy / lu), unit2((v[0] - piede[0], v[1] - piede[1])), 8)
    # assi assonometrici: da O' verso i vertici (e oltre)
    for v, nome in ((x_, "x′"), (y_, "y′"), (z_, "z′")):
        u = unit2(v)
        f.retta(o_, (v[0] + u[0] * 40, v[1] + u[1] * 40), "nero", 1.8)
        f.testo((v[0] + u[0] * 40, v[1] + u[1] * 40), nome, 4, 14 if u[1] < 0 else -4, "nero")
    f.punto(o_, "O′", 8, 30)
    f.testo(x_, "X", -6, -12, "blu")
    f.testo(y_, "Y", -4, -12, "blu")
    f.testo(z_, "Z", 10, 10, "blu")
    f.salva(OUT + "11-assonometria-ortogonale-triangolo-tracce.svg")


def unit2(v):
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


# =====================================================================
# 2. Nello spazio: cavaliera militare, la squadretta e la direzione
# =====================================================================

# direzione di z' sul foglio (in pianta): a 120 gradi da x e 150 gradi da y,
# come nello schema del foglio (x' a 210 gradi, y' a 300 gradi, z' in verticale)
W = (math.cos(math.radians(120)), math.cos(math.radians(150)), 0.0)


def spazio_cavaliera():
    k = 70
    # vista: la direzione di z' (W) va verso destra, un po' verso chi guarda
    aR = math.radians(240 - 15)
    R = (math.cos(aR), math.sin(aR), 0)
    D = (math.cos(aR - math.radians(90)), math.sin(aR - math.radians(90)), 0)

    def p3(p):
        return (dot(p, R) * k, -dot(p, D) * 0.38 * k + p[2] * k)

    u = 2.0
    L = 3.0
    quadro = [(-2.6, -2.6, 0), (L, -2.6, 0), (L, L, 0), (-2.6, L, 0)]
    O, Uz = (0, 0, 0), (0, 0, u)
    casi = [(1.0, "verde", "45°: u′_z = u"), (0.6, "arancio", "u′_z < u"), (1.45, "viola", "u′_z > u")]
    f = figura_adattata([p3(v) for v in quadro] + [p3((0, 0, 3.0))], "Cavaliera militare nello spazio: il quadro è π₁", [
        "In verde la «squadretta» a 45°: un cateto è u sull'asse z, l'altro sta sul quadro ed è u′z = u.",
        "Se la direzione di proiezione è più ripida u′z si accorcia (arancio), se è più inclinata si allunga (viola)."],
        30, 620)
    f.figura([p3(v) for v in quadro], "#9aa5b1")
    f.testo(p3((-2.6, L, 0)), "π_1 = quadro", 14, -16, "grigio")
    f.retta(p3(O), p3((L, 0, 0)), "nero", 1.8)
    f.retta(p3(O), p3((0, L, 0)), "nero", 1.8)
    f.retta(p3(O), p3((0, 0, 3.0)), "nero", 1.8)
    f.angolo_retto(p3(O), unit2(p3((1, 0, 0))), unit2(p3((0, 1, 0))), 10)
    f.testo(p3((L, 0, 0)), "x ≡ x′", -20, 20)
    f.testo(p3((0, L, 0)), "y ≡ y′", -50, -6)
    f.testo(p3((0, 0, 3.0)), "z", 6, 0)
    f.punto(p3(O), "O ≡ O′", -30, 22)
    f.punto(p3((u, 0, 0)), "u", -4, 18)
    f.punto(p3((0, u, 0)), "u", -4, -8)
    f.punto(p3(Uz), "U_z", -30, 4)
    f.retta(p3(O), p3(mul(W, 3.4)), "rosso", 2)
    f.testo(p3(mul(W, 3.4)), "z′", 6, 4, "rosso")
    f.figura([p3(O), p3(Uz), p3(mul(W, u))], "verde")
    for r, col, nome in casi:
        Uq = mul(W, u * r)
        f.retta(p3(Uz), p3(Uq), col, 1.8)
        f.punto(p3(Uq), None, colore=col)
    f.testo(p3(mul(W, u * 1.0)), casi[0][2], -50, 50, "verde")
    f.testo(p3(mul(W, u * 0.6)), casi[1][2], -30, 26, "arancio")
    f.testo(p3(mul(W, u * 1.45)), casi[2][2], 0, 26, "viola")
    f.angolo_retto(p3(O), unit2(p3((0, 0, 1))), unit2(p3(W)), 9)
    f.salva(OUT + "11-spazio-cavaliera-militare-direzione.svg")



# =====================================================================
# Assi sul foglio per la cavaliera militare
# =====================================================================
AX = (math.cos(math.radians(210)), math.sin(math.radians(210)))   # x'
AY = (math.cos(math.radians(300)), math.sin(math.radians(300)))   # y'
RID = 0.75                                                          # u'z / u


# =====================================================================
# 3. Sul foglio: ribaltamento dell'asse z e riduzione delle altezze
# =====================================================================

def ribaltamento():
    k = 30                       # 1 cm = 30 px
    u = 2 * k                    # unita' 2 cm su x', y' e z*
    O = (0, 0)
    pt = lambda d, l: (d[0] * l, d[1] * l)
    fine_x, fine_y, fine_z, fine_s = pt(AX, 6.6 * k), pt(AY, 5.2 * k), (0, 5.2 * k), (8.5 * k, 0)
    f = figura_adattata([fine_x, fine_y, fine_z, fine_s], "Cavaliera militare: ribaltamento dell'asse z", [
        "Unità uguali su x′, y′ e z* (si riportano col compasso); su z′ si sceglie u′z.",
        "s* unisce u su z* con u′z su z′: ogni altezza h presa su z* si porta su z′ con la parallela a s*."],
        40, 600)
    f.retta(O, fine_x, "nero", 1.8)
    f.retta(O, fine_y, "nero", 1.8)
    f.retta(O, fine_z, "nero", 1.8)
    f.retta(O, fine_s, "rosso", 1.6)
    f.angolo_retto(O, AX, AY, 10)
    f.angolo_retto(O, (0, 1), (1, 0), 10)
    f.testo(fine_x, "x′ ≡ x*", -40, 22)
    f.testo(fine_y, "y′ ≡ y*", 8, 6)
    f.testo(fine_z, "z′", 6, 4)
    f.testo(fine_s, "z*", -6, 20, "rosso")
    f.punto(O, "O′", -26, -6)
    Ux, Uy = pt(AX, u), pt(AY, u)
    Uzs, Uzq = (u, 0), (0, u * RID)
    f.punto(Ux, "u", -4, -10)
    f.punto(Uy, "u", 8, 2)
    f.punto(Uzs, "u", -4, 20, "rosso")
    f.punto(Uzq, "u′_z", -36, 4, "verde")
    arco(f, O, u, 210, 360)
    f.retta(Uzs, Uzq, "verde", 2)
    h = 5 * k
    H, Hq = (h, 0), (0, h * RID)
    f.punto(H, "h", -4, 20, "rosso")
    f.punto(Hq, "h′", -24, 4, "verde")
    f.retta(H, Hq, "verde", 1.4)
    mid = ((Uzs[0] + Uzq[0]) / 2, (Uzs[1] + Uzq[1]) / 2)
    f.testo(mid, "s*", 6, -2, "verde")
    f.testo(((H[0] + Hq[0]) / 2, (H[1] + Hq[1]) / 2), "parallela a s*", 8, -2, "verde", 13)
    f.salva(OUT + "11-cavaliera-militare-ribaltamento-asse-z.svg")


# =====================================================================
# 4. Esercizio: pianta 4 x 2 cm, altezza 5 cm, prospetti assonometrici
# =====================================================================

def esercizio():
    k = 34                       # 1 cm = 34 px

    def A(p):                    # punto (x, y, z) in cm -> disegno: z si accorcia di RID
        return (k * (p[0] * AX[0] + p[1] * AY[0]), k * (p[0] * AX[1] + p[1] * AY[1] + p[2] * RID))

    x0, x1, y0, y1, h = 2, 6, 2, 4, 5
    fx, fy, fz, fs = A((7.6, 0, 0)), A((0, 5.8, 0)), A((0, 0, 6.6)), (7.4 * k, 0)
    f = figura_adattata([fx, fy, fz, fs, A((x1, y1, 0))], "Esercizio: pianta 4 × 2 cm, altezza 5 cm", [
        "La pianta resta in vera forma (lati 4 e 2 cm) e fa da base al solido.",
        "Le altezze si prendono su z* (5 cm) e si riducono su z′ con la parallela a s*.",
        "Prospetti assonometrici: la pianta si proietta su x′ e su y′ e si alza fino a h′."], 40, 620)
    # assi
    f.retta(A((0, 0, 0)), fx, "nero", 1.6)
    f.retta(A((0, 0, 0)), fy, "nero", 1.6)
    f.retta(A((0, 0, 0)), fz, "nero", 1.6)
    f.retta(A((0, 0, 0)), fs, "rosso", 1.2)
    f.testo(fx, "x′ ≡ x*", -40, 22)
    f.testo(fy, "y′ ≡ y*", 8, 6)
    f.testo(fz, "z′", 6, 4)
    f.testo(fs, "z*", -4, 20, "rosso")
    f.punto((0, 0), "O′", 6, -8)
    # unita' (2 cm) e direzione s*
    u = 2
    f.punto(A((u, 0, 0)), "u", -16, 20)
    f.punto(A((0, u, 0)), "u", 8, 0)
    f.punto((u * k, 0), "u", -4, 20, "rosso")
    f.punto(A((0, 0, u)), "u′_z", 8, -6, "verde")
    arco(f, (0, 0), u * k, 210, 360)
    f.retta((u * k, 0), A((0, 0, u)), "verde", 1.6)
    f.testo(((u * k) / 2, A((0, 0, u))[1] / 2), "s*", 0, 18, "verde")
    # altezza 5 cm su z* -> h' su z'
    f.punto((h * k, 0), "h = 5 cm", -26, 20, "rosso")
    f.punto(A((0, 0, h)), "h′", -24, 4, "verde")
    f.retta((h * k, 0), A((0, 0, h)), "verde", 1.2)
    # seconda proiezione assonometrica (piano xz) e terza (piano yz)
    sec = [(x0, 0, 0), (x1, 0, 0), (x1, 0, h), (x0, 0, h)]
    ter = [(0, y0, 0), (0, y1, 0), (0, y1, h), (0, y0, h)]
    f.figura([A(p) for p in sec], "arancio")
    f.figura([A(p) for p in ter], "viola")
    for x in (x0, x1):
        f.costruzione(A((x, y0, 0)), A((x, 0, 0)))
    for y in (y0, y1):
        f.costruzione(A((x0, y, 0)), A((0, y, 0)))
    f.costruzione(A((0, 0, h)), A((x0, 0, h)))
    f.costruzione(A((0, 0, h)), A((0, y0, h)))
    f.testo(A((x1, 0, h)), "2ª proiezione", -6, -8, "arancio", 12)
    f.testo(A((0, y1, h)), "3ª proiezione", 6, -4, "viola", 12)
    # il solido: base = pianta in vera forma, spigoli verticali paralleli a z'
    base = [(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)]
    top = [(x, y, h) for x, y, _ in base]
    f.figura([A(p) for p in top], "blu")
    nascosto = (x0, y0, 0)       # l'unico vertice che non si vede (guardando da +x, +y e dall'alto)
    spigoli = list(zip(base, base[1:] + base[:1])) + list(zip(top, top[1:] + top[:1])) + list(zip(base, top))
    for a, b in spigoli:
        if nascosto in (a, b):
            tratteggio(f, A(a), A(b), "blu", 1.3)
        else:
            f.retta(A(a), A(b), "blu", 2.2)
    f.testo(A(((x0 + x1) / 2, y1, 0)), "pianta (1ª proiezione)", -10, 26, "blu", 12)
    f.salva(OUT + "11-esercizio-cavaliera-militare-prisma.svg")



if __name__ == "__main__":
    triangolo_tracce()
    spazio_cavaliera()
    ribaltamento()
    esercizio()
