"""Schemi per la bozza 03 di Geometria descrittiva (lezione dell'8 ottobre) e schemi
aggiunti alla sbobina 03 (le costruzioni fatte alla lavagna che non avevano un disegno).

Notazione della docente: proiezioni con i pedici (P1, P2, P3, r1, r2, r3), tracce T1r, T2r, T3r.
Coordinate 3D: (x lungo la LT, aggetto, quota).
"""
import math
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import Figura, Triedro, COLORI, _etichetta  # noqa: E402

BASE = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/"
SBOB = BASE + "sbobine/img/"
BOZZ = BASE + "bozze/img/"

FONT = 'font-family="Helvetica, Arial, sans-serif"'


def rett(f, x, y, w, h, fill="#ffffff", stroke="#1f1f1f", sw=1.4, opacita=1):
    f.parti.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" '
                   f'fill-opacity="{opacita}" stroke="{stroke}" stroke-width="{sw}"/>')


def linea(f, a, b, colore="nero", sw=1.4, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f.parti.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                   f'stroke="{COLORI.get(colore, colore)}" stroke-width="{sw}"{d} stroke-linecap="round"/>')


def scritta(f, x, y, testo, colore="#333", dim=13, corsivo=False, ancora="start", grassetto=False):
    st = ' font-style="italic"' if corsivo else ""
    gr = ' font-weight="bold"' if grassetto else ""
    f.parti.append(f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{dim}" fill="{COLORI.get(colore, colore)}"'
                   f' text-anchor="{ancora}"{st}{gr}>{_etichetta(testo)}</text>')


def punta(f, a, b, colore="nero", sw=1.2):
    """Punta di freccia in b (coordinate SVG assolute), direzione da a verso b."""
    l = math.hypot(b[0] - a[0], b[1] - a[1])
    d = ((b[0] - a[0]) / l, (b[1] - a[1]) / l)
    n = (-d[1], d[0])
    for s in (1, -1):
        c = (b[0] - d[0] * 9 + n[0] * 4 * s, b[1] - d[1] * 9 + n[1] * 4 * s)
        linea(f, b, c, colore, sw)


def freccia(f, a, b, colore="nero", sw=1.2):
    linea(f, a, b, colore, sw)
    punta(f, a, b, colore, sw)


def arco_richiamo(f, X3, y):
    """Arco di riporto (coordinate di disegno della Figura): da (X3, -y) a (X3 + y, 0), centro (X3, 0)."""
    cx, cy = f._s((X3, 0))
    f.parti.append(f'<path d="M {cx:.1f} {cy + y:.1f} A {y:.1f} {y:.1f} 0 0 0 {cx + y:.1f} {cy:.1f}" '
                   f'fill="none" stroke="#8a8a8a" stroke-width="1" stroke-dasharray="5,4"/>')


# ====================== 1. sbobina: le scale di rappresentazione ======================
f = Figura(720, 430, 0, "Le scale: lo stesso muro di 50 cm disegnato in tre scale, e la scala grafica")
k = 4  # 1 mm sul foglio = 4 px nello schema (le proporzioni tra le scale sono quelle vere)
righe = [("1:50", "1 m = 2 cm", 10, "spessore disegnato 1 cm (le misure raddoppiano)"),
         ("1:100", "1 m = 1 cm", 5, "spessore disegnato 5 mm"),
         ("1:200", "1 m = 0,5 cm", 2.5, "spessore disegnato 2,5 mm (le misure si dimezzano)")]
y = 30
for scala, eq, mm, nota in righe:
    scritta(f, 20, y + 6, "scala " + scala, "nero", 15, grassetto=True)
    scritta(f, 20, y + 24, eq, "#555", 12)
    rett(f, 150, y - 8, 180, mm * k, fill="#9aa5b1", opacita=0.6)
    scritta(f, 350, y + 6, "muro reale: 50 cm", "#555", 12)
    scritta(f, 350, y + 22, nota, "blu", 12)
    y += 80
scritta(f, 20, 262, "scala grafica 1:100 (1 m = 1 cm)", "nero", 14, grassetto=True)
x0, yb, passo = 30, 282, 40
for i in range(6):
    rett(f, x0 + i * passo, yb, passo, 8, fill="#1f1f1f" if i % 2 == 0 else "#ffffff", sw=1)
    scritta(f, x0 + i * passo, yb + 26, str(i), "nero", 12, ancora="middle")
scritta(f, x0 + 6 * passo + 4, yb + 26, "m", "nero", 12)
linea(f, (x0, yb - 8), (x0 + passo, yb - 8), "rosso", 1.4)
linea(f, (x0, yb - 13), (x0, yb - 3), "rosso", 1.4); linea(f, (x0 + passo, yb - 13), (x0 + passo, yb - 3), "rosso", 1.4)
scritta(f, x0 + passo + 8, yb - 6, "leggo 1 cm sul righello = 1 m", "rosso", 12)
scritta(f, 20, 342, "scala grafica 1:200 (1 m = 0,5 cm)", "nero", 14, grassetto=True)
yb = 362
for i in range(10):
    rett(f, x0 + i * 20, yb, 20, 8, fill="#1f1f1f" if i % 2 == 0 else "#ffffff", sw=1)
for i in (0, 5, 10):
    scritta(f, x0 + i * 20, yb + 26, str(i), "nero", 12, ancora="middle")
scritta(f, x0 + 10 * 20 + 10, yb + 26, "m", "nero", 12)
linea(f, (x0, yb - 8), (x0 + 20, yb - 8), "rosso", 1.4)
linea(f, (x0, yb - 13), (x0, yb - 3), "rosso", 1.4); linea(f, (x0 + 20, yb - 13), (x0 + 20, yb - 3), "rosso", 1.4)
scritta(f, x0 + 30, yb - 6, "leggo 0,5 cm = 1 m", "rosso", 12)
scritta(f, 330, 300, "La scala grafica si disegna accanto", "#444", 12)
scritta(f, 330, 316, "al disegno: se il foglio viene ridotto", "#444", 12)
scritta(f, 330, 332, "o fotocopiato, si riduce insieme a lui", "#444", 12)
scritta(f, 330, 348, "e permette sempre di risalire", "#444", 12)
scritta(f, 330, 364, "alle misure reali.", "#444", 12)
f.salva(SBOB + "03-scale-di-rappresentazione.svg")


# ====================== 2. sbobina: il prospetto giusto e quello sbagliato ======================
f = Figura(740, 470, 0, "Il prospetto del lato in alto della pianta: giusto e sbagliato")
# pianta (unita' in px), nord in alto: il corpo arretrato (rientranza) sta a sinistra del lato nord
pianta = [(0, 0), (200, 0), (200, 110), (70, 110), (70, 80), (0, 80)]
H_ALTO, H_BASSO = 100, 60   # altezze dei due corpi (schema indicativo)


def disegna_pianta(f, ox, ysud):
    pts = " ".join(f"{ox + x:.1f},{ysud - y:.1f}" for x, y in pianta)
    f.parti.append(f'<polygon points="{pts}" fill="#9aa5b1" fill-opacity="0.25" stroke="#1f1f1f" stroke-width="2"/>')
    scritta(f, ox + 100, ysud - 40, "pianta", "#444", 13, ancora="middle")
    scritta(f, ox + 35, ysud - 88, "rientranza", "arancio", 11, ancora="middle")


for i, giusto in enumerate((True, False)):
    ox, ysud = 60 + 370 * i, 440
    ynord = ysud - 110
    disegna_pianta(f, ox, ysud)
    if giusto:
        ylt = 70
        titolo, col = "GIUSTO: LT in alto, prospetto a testa in giù", "verde"
        segno = 1   # il prospetto scende dalla LT verso la pianta
    else:
        ylt = ynord - 22
        titolo, col = "SBAGLIATO: LT sotto, prospetto specchiato", "rosso"
        segno = -1  # il prospetto sale dalla LT
    scritta(f, ox - 40, 20, titolo, col, 13, grassetto=True)
    linea(f, (ox - 30, ylt), (ox + 240, ylt), "nero", 1.6)
    scritta(f, ox - 30, ylt - 6 if giusto else ylt + 16, "LT", "nero", 13, corsivo=True)
    # linee di proiezione dagli spigoli del lato nord
    for x, yp in [(0, 80), (70, 110), (200, 110)]:
        linea(f, (ox + x, ysud - yp), (ox + x, ylt), "grigio", 0.9, "4,3")
    # i due corpi del prospetto
    hb, ha = H_BASSO * segno, H_ALTO * segno
    rett(f, ox, min(ylt, ylt + hb), 70, abs(hb), fill="#ffffff", sw=1.8)
    rett(f, ox + 70, min(ylt, ylt + ha), 130, abs(ha), fill="#ffffff", sw=1.8)
    # una finestra per corpo, per riconoscere il disegno
    rett(f, ox + 22, ylt + segno * 20 - (0 if segno > 0 else 22), 26, 22, fill="#d6e4f0", sw=1)
    rett(f, ox + 115, ylt + segno * 30 - (0 if segno > 0 else 30), 40, 30, fill="#d6e4f0", sw=1)
    scritta(f, ox + 35, ylt + segno * (H_BASSO + 14) + (4 if segno > 0 else 0), "rientranza", "arancio", 11, ancora="middle")
    if giusto:
        # chi guarda il lato nord sta in alto, oltre la LT, e guarda verso il basso
        freccia(f, (ox + 270, 38), (ox + 270, 90), "verde", 1.6)
        scritta(f, ox + 262, 34, "si guarda da qui", "verde", 11, ancora="end")
        scritta(f, ox + 252, 300, "girando il foglio la rientranza", "#444", 11, ancora="end")
        scritta(f, ox + 252, 314, "è a destra, come la vede chi guarda", "#444", 11, ancora="end")
    else:
        scritta(f, ox + 120, 150, "è come guardare l'edificio", "#444", 11, ancora="middle")
        scritta(f, ox + 120, 164, "da dentro: destra e sinistra", "#444", 11, ancora="middle")
        scritta(f, ox + 120, 178, "sono scambiate", "#444", 11, ancora="middle")
f.salva(SBOB + "03-prospetto-giusto-e-sbagliato.svg")


# ====================== triedri ======================
def triedro(titolo, h=430, w=600, origine=(262, 190), X3=400, U=360, Y=230, Z=220, scala=0.75):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, origine, X3=X3, U=U, Y=Y, Z=Z, scala=scala)
    t.piani()
    return f, t


# 3. sbobina: la retta proiettante in seconda nello spazio (dal quaderno di Marta)
f, t = triedro("Nello spazio: la retta m proiettante in seconda (perpendicolare a π₂)")
xm, zm, Y = 200, 120, 230
T2m = (xm, 0, zm)
fine = (xm, Y, zm)
t.segmento(T2m, fine, "rosso", 2.6); t.testo(fine, "m", 6, 4, "rosso", 16)
t.segmento((xm, 0, 0), (xm, Y, 0), "rosso", 1.6)
t.testo((xm, Y, 0), "m₁", -6, 20, "rosso"); t.testo((xm, Y, 0), "T_{1m}∞", 18, 20, "rosso")
t.segmento((400, 0, zm), (400, Y, zm), "rosso", 1.6)
t.testo((400, Y, zm), "m₃", 6, 4, "rosso"); t.testo((400, Y, zm), "T_{3m}∞", 6, 22, "rosso")
t.richiamo(T2m, (xm, 0, 0)); t.richiamo(fine, (xm, Y, 0)); t.richiamo(fine, (400, Y, zm))
t.richiamo(T2m, (400, 0, zm))
t.punto((xm, 0, 0)); t.punto((400, 0, zm))
t.punto(T2m, "m₂ ≡ T_{2m}", -96, 18, "rosso")
f.nota(16, 420, "m buca solo π₂ (in T₂ₘ); è parallela a π₁ e a π₃, quindi T₁ₘ e T₃ₘ sono all'infinito.")
f.salva(SBOB + "03-spazio-retta-proiettante-in-seconda.svg")

# 4. bozza (proposto): la retta proiettante in prima nello spazio, con un punto P
f, t = triedro("Nello spazio: la retta r proiettante in prima (perpendicolare a π₁) e un suo punto P")
xr, yr, zP, Zt = 200, 120, 100, 185
T1r = (xr, yr, 0); top = (xr, yr, Zt); P = (xr, yr, zP)
t.segmento(T1r, top, "rosso", 2.6); t.testo(top, "r", 6, 4, "rosso", 16)
t.segmento((xr, 0, 0), (xr, 0, Zt), "rosso", 1.6)
t.testo((xr, 0, Zt), "r₂", 6, 4, "rosso"); t.testo((xr, 0, Zt), "T_{2r}∞", -54, 4, "rosso")
t.segmento((400, yr, 0), (400, yr, Zt), "rosso", 1.6)
t.testo((400, yr, Zt), "r₃", 6, 4, "rosso"); t.testo((400, yr, Zt), "T_{3r}∞", -60, 4, "rosso")
t.richiamo(T1r, (xr, 0, 0)); t.richiamo(T1r, (400, yr, 0))
t.richiamo(P, (xr, 0, zP)); t.richiamo(P, (400, yr, zP))
t.punto((xr, 0, 0)); t.punto((400, yr, 0))
t.punto(P, "P", -20, -6, "rosso")
t.punto((xr, 0, zP), "P₂", -26, -4, "rosso"); t.punto((400, yr, zP), "P₃", 8, -4, "rosso")
t.punto(T1r, "r₁ ≡ T_{1r} ≡ P₁", 8, 18, "rosso")
f.nota(16, 420, "r buca solo π₁ (in T₁ᵣ); è parallela a π₂ e a π₃, quindi T₂ᵣ e T₃ᵣ sono all'infinito.")
f.salva(BOZZ + "b03-spazio-retta-proiettante-in-prima.svg")

# 5. bozza (proposto): come si ribaltano i piani sul foglio
f = Figura(760, 470, 0, "Come i tre piani finiscono sul foglio: π₃ ruota su π₂, poi π₁ ruota sotto la LT")
X3, Uu, Yy, Zz = 260, 220, 150, 150
t = Triedro(f, (220, 215), X3=X3, U=Uu, Y=Yy, Z=Zz, scala=0.62)
t.piani(etichette=False)
t.testo((X3 - Uu * 0.85, Yy * 0.8, 0), "π_1", colore="grigio")
t.testo((X3 - Uu * 0.85, 0, Zz * 0.85), "π_2", colore="grigio")
t.testo((X3, Yy * 0.75, Zz * 0.6), "π_3", -4, 0, colore="grigio")
t.testo((X3 - Uu, 0, 0), "LT", -22, 4, "nero")
x0 = X3 - Uu
# posizioni finali (tratteggiate)
for a, b in [((X3, 0, 0), (X3 + Yy, 0, 0)), ((X3 + Yy, 0, 0), (X3 + Yy, 0, Zz)), ((X3 + Yy, 0, Zz), (X3, 0, Zz))]:
    t.segmento(a, b, "blu", 1.2, "6,4")
for a, b in [((x0, 0, 0), (x0, 0, -Yy)), ((x0, 0, -Yy), (X3, 0, -Yy)), ((X3, 0, -Yy), (X3, 0, 0))]:
    t.segmento(a, b, "verde", 1.2, "6,4")
# archi di rotazione con la punta
def arco3d(pts, colore):
    sv = [t._p(p) for p in pts]
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in sv)
    f.parti.append(f'<path d="{d}" fill="none" stroke="{COLORI[colore]}" stroke-width="1.4"/>')
    punta(f, sv[-2], sv[-1], colore, 1.4)


arco3d([(X3 + Yy * math.sin(a), Yy * math.cos(a), Zz * 0.4) for a in [i * math.pi / 2 / 30 for i in range(31)]], "blu")
xa = x0 + 60
arco3d([(xa, Yy * math.cos(a), -Yy * math.sin(a)) for a in [i * math.pi / 2 / 30 for i in range(31)]], "verde")
t.testo((X3 + Yy, 0, Zz * 0.85), "π₃ ribaltato", 6, 0, "blu", 12)
t.testo((x0, 0, -Yy), "π₁ ribaltato", -20, 18, "verde", 12)
scritta(f, 16, 430, "1. π₃ ruota attorno allo spigolo verticale e si mette accanto a π₂ (freccia blu).", "#333", 12)
scritta(f, 16, 448, "2. π₁ ruota attorno alla LT e scende sotto π₂ (freccia verde): i tre piani diventano il foglio.", "#333", 12)
# a destra: il foglio
g = Figura(0, 0, 200, x0=570)
g.parti = f.parti
g.lt(-110, 180)
g._linea((40, 150), (40, -150), "nero", 1.2)
g.testo((-70, 90), "π₂", 0, 0, "grigio", 18)
g.testo((100, 90), "π₃", 0, 0, "grigio", 18)
g.testo((-70, -90), "π₁", 0, 0, "grigio", 18)
g.testo((-110, -150), "π₁ ≡ π₂ ≡ π₃", 0, 0, "nero", 13)
scritta(f, 570 - 110, 30, "sul foglio", "#333", 13, grassetto=True)
f.salva(BOZZ + "b03-ribaltamento-dei-piani.svg")
print("ok")
