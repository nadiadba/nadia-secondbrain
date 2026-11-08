"""Disegni aggiunti alla bozza di matematica 06 - Le matrici e il determinante.

La regola di Sarrus come la fa il professore: linee disegnate direttamente sulla
matrice 3x3, senza ricopiare le colonne (appunti di Nadia, foto 05).

Uso: python3 -I .claude/scripts/disegni/matematica-04b.py
Scrive gli SVG in anno-1/semestre-1/matematica/bozze/img/ (prefisso 04-).
Nessuna dipendenza esterna: riusa le primitive di matematica-04.py.
"""
import importlib.util
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("m06", os.path.join(QUI, "matematica-04.py"))
m06 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m06)

Tela, linea_px = m06.Tela, m06.linea_px
FONT = m06.m03.FONT
ROSA = "#d6336c"
SCURO = "#34495e"

def nome(i, j):
    return "a_%d,%d_" % (i, j)


def mini_matrice(t, x0, y0, termine, colore, titolo):
    """Matrice 3x3 di elementi a_ij; i tre elementi del termine sono cerchiati e uniti
    da linee nell'ordine in cui il professore li scrive (termine = lista di (i, j))."""
    cw, ch = 66, 50
    centro = lambda i, j: (x0 + (j - 0.5) * cw, y0 + (i - 0.5) * ch)
    # linee: spezzata chiusa (triangolo) o retta (diagonale) attraverso i tre elementi
    pts = [centro(i, j) for i, j in termine]
    allineati = abs((pts[1][0] - pts[0][0]) * (pts[2][1] - pts[0][1])
                    - (pts[1][1] - pts[0][1]) * (pts[2][0] - pts[0][0])) < 1e-6
    if allineati:
        ordinati = sorted(pts)
        linea_px(t, ordinati[0][0], ordinati[0][1], ordinati[-1][0], ordinati[-1][1], colore, sw=3, op=0.75)
    else:
        p = " ".join("%.1f,%.1f" % q for q in pts)
        t.el.append('<polygon points="%s" fill="%s" fill-opacity="0.08" stroke="%s" stroke-width="3" '
                    'stroke-opacity="0.75" stroke-linejoin="round"/>' % (p, colore, colore))
    scelti = set(termine)
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            cx, cy = centro(i, j)
            if (i, j) in scelti:
                t.el.append('<ellipse cx="%.1f" cy="%.1f" rx="26" ry="17" fill="white" stroke="%s" '
                            'stroke-width="2.4"/>' % (cx, cy, colore))
                col, peso = colore, ' font-weight="bold"'
            else:
                col, peso = "#aaaaaa", ""
            t.el.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="17" text-anchor="middle" '
                        'fill="%s"%s>%s</text>' % (cx - 2, cy + 4, FONT, col, peso, m06.m03.fmt_label(nome(i, j))))
    # parentesi tonde
    W, H = 3 * cw, 3 * ch
    for xe, xc in ((x0 - 4, x0 - 20), (x0 + W + 4, x0 + W + 20)):
        t.el.append('<path d="M %.1f,%.1f Q %.1f,%.1f %.1f,%.1f" fill="none" stroke="#222" stroke-width="2"/>'
                    % (xe, y0 - 4, xc, y0 + H / 2, xe, y0 + H + 4))
    t.testo_px(x0 + W / 2, y0 + H + 34, titolo, col=colore, size=17)


def sarrus_sulla_matrice():
    """Le sei moltiplicazioni di Sarrus disegnate sulla matrice, nell'ordine del professore."""
    t = Tela(900, 580)
    piu = [
        ([(1, 1), (2, 2), (3, 3)], "+ a_1,1_ a_2,2_ a_3,3_"),
        ([(2, 3), (1, 2), (3, 1)], "+ a_2,3_ a_1,2_ a_3,1_"),
        ([(2, 1), (3, 2), (1, 3)], "+ a_2,1_ a_3,2_ a_1,3_"),
    ]
    meno = [
        ([(1, 3), (2, 2), (3, 1)], "− a_1,3_ a_2,2_ a_3,1_"),
        ([(2, 1), (1, 2), (3, 3)], "− a_2,1_ a_1,2_ a_3,3_"),
        ([(3, 2), (2, 3), (1, 1)], "− a_3,2_ a_2,3_ a_1,1_"),
    ]
    t.testo_px(450, 30, "Segno +: la diagonale principale e i due triangoli «paralleli» a lei",
               col=ROSA, size=17)
    for k, (term, tit) in enumerate(piu):
        mini_matrice(t, 70 + k * 290, 55, term, ROSA, tit)
    t.testo_px(450, 318, "Segno −: l'altra diagonale e i due triangoli «paralleli» a lei",
               col=SCURO, size=17)
    for k, (term, tit) in enumerate(meno):
        mini_matrice(t, 70 + k * 290, 343, term, SCURO, tit)
    t.salva("04-sarrus-sulla-matrice.svg")


if __name__ == "__main__":
    sarrus_sulla_matrice()
