"""Disegni per la bozza di matematica 06 - Le matrici e il determinante.

Uso: python3 -I .claude/scripts/disegni/matematica-04.py
Scrive gli SVG in anno-1/semestre-1/matematica/bozze/img/ (prefisso 04-).
Nessuna dipendenza esterna: riusa le primitive di matematica-05.py.
"""
import importlib.util
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("m03", os.path.join(QUI, "matematica-05.py"))
m03 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m03)

Tela, Piano = m03.Tela, m03.Piano
BLU, ROSSO, VERDE, VIOLA, ARANCIO = m03.BLU, m03.ROSSO, m03.VERDE, m03.VIOLA, m03.ARANCIO
GRIGIO, GRIGIO_CHIARO = m03.GRIGIO, m03.GRIGIO_CHIARO
add, mul = m03.add, m03.mul

CELLA_W, CELLA_H = 54, 40


def m(s):
    """Meno tipografico."""
    return str(s).replace("-", "−")


def matrice(t, x0, y0, righe, cw=CELLA_W, ch=CELLA_H, size=18, bordi="tonde", col="#222",
            colori=None, nome=None):
    """Disegna una matrice con l'angolo in alto a sinistra delle celle in (x0, y0) (pixel).
    colori: dict {(i, j): colore} per colorare singoli elementi. Ritorna (larghezza, altezza)."""
    nr, nc = len(righe), len(righe[0])
    W, H = nc * cw, nr * ch
    for i, r in enumerate(righe):
        for j, v in enumerate(r):
            c = (colori or {}).get((i, j), col)
            t.testo_px(x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch + size * 0.36, m(v), col=c, size=size)
    if bordi == "tonde":
        for xe, xc in ((x0 - 2, x0 - 20), (x0 + W + 2, x0 + W + 20)):
            t.el.append('<path d="M %.1f,%.1f Q %.1f,%.1f %.1f,%.1f" fill="none" stroke="#222" stroke-width="2"/>'
                        % (xe, y0 - 2, xc, y0 + H / 2, xe, y0 + H + 2))
    elif bordi == "barre":
        for xb in (x0 - 4, x0 + W + 4):
            t.el.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#222" stroke-width="2"/>'
                        % (xb, y0 - 2, xb, y0 + H + 2))
    if nome:
        t.testo_px(x0 - 22, y0 + H / 2 + 7, nome, size=20, anchor="end")
    return W, H


def rett(t, x, y, w, h, col, op=0.15, sw=2, dash=None, rx=8):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    t.el.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="%s" fill-opacity="%s" '
                'stroke="%s" stroke-width="%s"%s/>' % (x, y, w, h, rx, col, op, col, sw, d))


def linea_px(t, x1, y1, x2, y2, col, sw=2.2, op=1, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    t.el.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" '
                'stroke-linecap="round" opacity="%s"%s/>' % (x1, y1, x2, y2, col, sw, op, d))


# ---------------------------------------------------------------- disegni

def prodotto_riga_colonna():
    """A·B con 1a riga di A, 2a colonna di B e l'elemento (1,2) del risultato evidenziati."""
    t = Tela(760, 250)
    A = [[1, 2], [1, 0]]
    B = [[1, -1], [2, 1]]
    C = [[5, 1], [1, -1]]
    y0 = 60
    xa, xb, xc = 90, 330, 590
    # evidenziazioni
    rett(t, xa - 4, y0 + 2, 2 * CELLA_W + 8, CELLA_H - 4, BLU)
    rett(t, xb + CELLA_W + 4, y0 - 4, CELLA_W - 8, 2 * CELLA_H + 8, ARANCIO)
    rett(t, xc + CELLA_W + 4, y0 + 2, CELLA_W - 8, CELLA_H - 4, VIOLA)
    matrice(t, xa, y0, A, nome="A =", colori={(0, 0): BLU, (0, 1): BLU})
    matrice(t, xb, y0, B, nome="B =", colori={(0, 1): ARANCIO, (1, 1): ARANCIO})
    matrice(t, xc, y0, C, nome="A·B =", colori={(0, 1): VIOLA})
    t.testo_px(xa + CELLA_W, y0 - 16, "1ª riga di A", col=BLU, size=14)
    t.testo_px(xb + 1.5 * CELLA_W, y0 - 16, "2ª colonna di B", col=ARANCIO, size=14)
    t.testo_px(xc + 1.5 * CELLA_W, y0 - 16, "riga 1, colonna 2", col=VIOLA, size=14)
    t.testo_px(380, 190, "1ª riga × 2ª colonna:  1·(−1) + 2·1 = −1 + 2 = 1", col="#222", size=17)
    t.testo_px(380, 222, "primo con primo, secondo con secondo, poi si somma (come un prodotto scalare)",
               col=GRIGIO, size=13)
    t.salva("04-prodotto-riga-colonna.svg")


def tipi_prodotto():
    """(m×n)·(n×p) = m×p: i numeri interni devono coincidere."""
    t = Tela(620, 190)

    def blocco(x, y, w, h, col, etichetta):
        rett(t, x, y, w, h, col, op=0.12, rx=4)
        t.testo_px(x + w / 2, y + h / 2 + 6, etichetta, col=col, size=17)

    s = 22
    # A: 2x3, B: 3x4, AB: 2x4
    blocco(40, 40, 3 * s, 2 * s, BLU, "A")
    blocco(160, 40 - s / 2, 4 * s, 3 * s, ARANCIO, "B")
    t.testo_px(138, 70, "·", size=26)
    t.testo_px(270, 69, "=", size=22)
    blocco(300, 40, 4 * s, 2 * s, VIOLA, "A·B")
    t.testo_px(40 + 1.5 * s, 120, "2 × 3", col=BLU, size=16)
    t.testo_px(160 + 2 * s, 120, "3 × 4", col=ARANCIO, size=16)
    t.testo_px(300 + 2 * s, 120, "2 × 4", col=VIOLA, size=16)
    # archi che legano i numeri interni
    t.el.append('<path d="M 92,128 Q 141,156 190,128" fill="none" stroke="%s" stroke-width="1.6"/>' % VERDE)
    t.testo_px(141, 168, "uguali", col=VERDE, size=13)
    t.testo_px(420, 60, "colonne di A = righe di B", col=VERDE, size=14, anchor="start")
    t.testo_px(420, 84, "il risultato ha le righe di A", col=VIOLA, size=14, anchor="start")
    t.testo_px(420, 104, "e le colonne di B", col=VIOLA, size=14, anchor="start")
    t.salva("04-tipi-prodotto.svg")


def sarrus():
    """Matrice 3x3 con le prime due colonne ricopiate, diagonali + e -."""
    t = Tela(640, 290)
    cw, ch = 70, 50
    x0, y0 = 70, 50
    el = [["a₁₁", "a₁₂", "a₁₃"], ["a₂₁", "a₂₂", "a₂₃"], ["a₃₁", "a₃₂", "a₃₃"]]
    righe = [r + r[:2] for r in el]
    # sfondo colonne ripetute
    rett(t, x0 + 3 * cw + 4, y0 - 6, 2 * cw - 8, 3 * ch + 12, GRIGIO, op=0.08, sw=1, dash="4,3")
    centro = lambda i, j: (x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch)
    # diagonali discendenti (+)
    for k in range(3):
        a, b = centro(0, k), centro(2, k + 2)
        linea_px(t, a[0] - 12, a[1] - 9, b[0] + 12, b[1] + 9, VERDE, sw=2.4, op=0.75)
    # diagonali ascendenti (-)
    for k in range(3):
        a, b = centro(2, k), centro(0, k + 2)
        linea_px(t, a[0] - 12, a[1] + 9, b[0] + 12, b[1] - 9, ROSSO, sw=2.4, op=0.75, dash="7,4")
    for i, r in enumerate(righe):
        for j, v in enumerate(r):
            cx, cy = centro(i, j)
            # alone bianco per leggere sopra le linee
            t.el.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="19" text-anchor="middle" '
                        'stroke="white" stroke-width="6" stroke-linejoin="round" fill="white">%s</text>'
                        % (cx, cy + 7, m03.FONT, v))
            t.testo_px(cx, cy + 7, v, size=19, col="#222" if j < 3 else GRIGIO)
    for xb in (x0 - 4, x0 + 3 * cw + 4):
        linea_px(t, xb, y0 - 4, xb, y0 + 3 * ch + 4, "#222", sw=2)
    t.testo_px(x0 + 4 * cw, y0 - 14, "prime due colonne ricopiate", col=GRIGIO, size=13)
    t.testo_px(x0 + 5 * cw + 20, y0 + 40, "+", col=VERDE, size=26, anchor="start")
    t.testo_px(x0 + 5 * cw + 44, y0 + 38, "verso il basso", col=VERDE, size=14, anchor="start")
    t.testo_px(x0 + 5 * cw + 20, y0 + 120, "−", col=ROSSO, size=26, anchor="start")
    t.testo_px(x0 + 5 * cw + 44, y0 + 118, "verso l'alto", col=ROSSO, size=14, anchor="start")
    t.testo_px(320, 248, "det A = a₁₁a₂₂a₃₃ + a₁₂a₂₃a₃₁ + a₁₃a₂₁a₃₂", col=VERDE, size=16)
    t.testo_px(320, 274, "− a₃₁a₂₂a₁₃ − a₃₂a₂₃a₁₁ − a₃₃a₂₁a₁₂", col=ROSSO, size=16)
    t.salva("04-sarrus.svg")


def diagonali_2x2():
    """Determinante 2x2: diagonale principale meno l'altra."""
    t = Tela(420, 150)
    cw, ch = 60, 46
    x0, y0 = 50, 28
    linea_px(t, x0 + 18, y0 + 12, x0 + 2 * cw - 18, y0 + 2 * ch - 12, VERDE, sw=2.6, op=0.8)
    linea_px(t, x0 + 18, y0 + 2 * ch - 12, x0 + 2 * cw - 18, y0 + 12, ROSSO, sw=2.6, op=0.8, dash="7,4")
    for i, r in enumerate([["a", "b"], ["c", "d"]]):
        for j, v in enumerate(r):
            cx, cy = x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch + 7
            t.el.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="21" font-style="italic" '
                        'text-anchor="middle" stroke="white" stroke-width="7" fill="white">%s</text>'
                        % (cx, cy, m03.FONT, v))
            t.testo_px(cx, cy, v, size=21, italic=True)
    for xb in (x0 - 2, x0 + 2 * cw + 2):
        linea_px(t, xb, y0 - 2, xb, y0 + 2 * ch + 2, "#222", sw=2)
    t.testo_px(x0 + 2 * cw + 24, y0 + ch + 7, "=", size=22, anchor="start")
    t.testo_px(x0 + 2 * cw + 54, y0 + ch + 7, "a·d", col=VERDE, size=21, anchor="start")
    t.testo_px(x0 + 2 * cw + 98, y0 + ch + 7, "−", size=21, anchor="start")
    t.testo_px(x0 + 2 * cw + 120, y0 + ch + 7, "b·c", col=ROSSO, size=21, anchor="start")
    t.testo_px(210, 140, "diagonale principale meno l'altra diagonale", col=GRIGIO, size=13)
    t.salva("04-diagonali-2x2.svg")


def segni():
    """Schema dei segni (-1)^(i+j) e posizioni."""
    t = Tela(560, 230)
    cw, ch = 62, 50
    x0, y0 = 60, 40
    for i in range(3):
        for j in range(3):
            pos = (i + j) % 2 == 0
            col = VERDE if pos else ROSSO
            rett(t, x0 + j * cw + 3, y0 + i * ch + 3, cw - 6, ch - 6, col, op=0.12, sw=1, rx=6)
            t.testo_px(x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch + 9, "+" if pos else "−", col=col, size=26)
    for j in range(3):
        t.testo_px(x0 + (j + 0.5) * cw, y0 - 12, "j = %d" % (j + 1), col=GRIGIO, size=12)
    for i in range(3):
        t.testo_px(x0 - 10, y0 + (i + 0.5) * ch + 5, "i = %d" % (i + 1), col=GRIGIO, size=12, anchor="end")
    xt = x0 + 3 * cw + 40
    t.testo_px(xt, y0 + 20, "segno = (−1)^i+j^", size=17, anchor="start")
    t.testo_px(xt, y0 + 56, "i + j pari  →  +", col=VERDE, size=15, anchor="start")
    t.testo_px(xt, y0 + 82, "i + j dispari  →  −", col=ROSSO, size=15, anchor="start")
    t.testo_px(xt, y0 + 118, "es. posto (1, 2): 1 + 2 = 3", col=GRIGIO, size=14, anchor="start")
    t.testo_px(xt, y0 + 140, "(−1)^3^ = −1", col=GRIGIO, size=14, anchor="start")
    t.testo_px(280, 215, "si parte con + in alto a sinistra e si alterna, come una scacchiera", col=GRIGIO, size=13)
    t.salva("04-schema-segni.svg")


def minori():
    """Esempio della lavagna: A11 e A22, riga e colonna cancellate."""
    A = [[1, 3, -5], [5, 0, 2], [-1, 0, 0]]
    t = Tela(820, 300)
    cw, ch = 50, 40

    def pannello(x0, y0, ri, cj, titolo, minore, conto, colore):
        matrice(t, x0, y0, A, cw=cw, ch=ch, colori={(ri, cj): colore,
                **{(i, j): GRIGIO for i in range(3) for j in range(3) if (i == ri or j == cj) and (i, j) != (ri, cj)}})
        # barre di cancellazione
        linea_px(t, x0 - 4, y0 + (ri + 0.5) * ch, x0 + 3 * cw + 4, y0 + (ri + 0.5) * ch, colore, sw=2, op=0.4)
        linea_px(t, x0 + (cj + 0.5) * cw, y0 - 4, x0 + (cj + 0.5) * cw, y0 + 3 * ch + 4, colore, sw=2, op=0.4)
        t.testo_px(x0 + 1.5 * cw, y0 - 18, titolo, col=colore, size=15)
        # minore
        xm, ym = x0 + 3 * cw + 70, y0 + ch / 2
        t.testo_px(xm - 28, ym + ch / 2 + 6, "→", size=22)
        matrice(t, xm, ym, minore, cw=40, ch=ch, bordi="barre", colori=None)
        for k, riga in enumerate(conto):
            t.testo_px(x0 + 1.5 * cw + 95, y0 + 3 * ch + 40 + 24 * k, riga, col=colore if k == len(conto) - 1 else "#222",
                       size=15)

    pannello(50, 60, 0, 0, "togli riga 1 e colonna 1", [[0, 2], [0, 0]],
             ["A₁₁ = (−1)^1+1^ · (0·0 − 2·0)", "A₁₁ = +1 · 0 = 0"], BLU)
    pannello(450, 60, 1, 1, "togli riga 2 e colonna 2", [[1, -5], [-1, 0]],
             ["A₂₂ = (−1)^2+2^ · (1·0 − (−5)(−1))", "A₂₂ = +1 · (0 − 5) = −5"], VIOLA)
    t.salva("04-minori.svg")


def area_determinante():
    u, v = (3, 1), (1, 2)
    t = Piano(-2.0, 4.8, -0.6, 3.6, s=60)
    t.h += 34
    t.griglia()
    t.poligono([(0, 0), u, add(u, v), v], fill=BLU, op=0.13, stroke=BLU, sw=1, dash="4,3")
    t.freccia((0, 0), u, col=BLU)
    t.freccia((0, 0), v, col=ROSSO)
    t.testo(u, "*u* = (3, 1)", col=BLU, dx=8, dy=14, anchor="start", size=15)
    t.testo((0, 1.5), "*v* = (1, 2)", col=ROSSO, dx=-14, dy=5, anchor="end", size=15)
    t.testo(mul(0.5, add(u, v)), "area = 5", dx=10, dy=6, size=16, bg=True)
    t.testo_px(t.w / 2, t.h - 14, "det (3 1 ; 1 2) = 3·2 − 1·1 = 5 = area del parallelogramma", size=14)
    t.salva("04-area-determinante.svg")


if __name__ == "__main__":
    prodotto_riga_colonna()
    tipi_prodotto()
    diagonali_2x2()
    sarrus()
    segni()
    minori()
    area_determinante()
