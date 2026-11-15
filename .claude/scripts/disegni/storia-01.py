#!/usr/bin/env python3
"""Disegni al tratto (bianco e nero puro) per gli appunti in PDF della lezione 01 di
Storia dell'architettura 1: il tempio greco e gli ordini architettonici.

Uso: python3 -I .claude/scripts/disegni/storia-01.py
Scrive gli SVG in anno-1/semestre-1/storia-architettura/materiale/appunti-pdf/figure/.

Scala: le figure «di margine» hanno larghezza 260 unita' (stampate a 52 mm: 1 unita' =
0,2 mm, quindi un testo da 11 unita' e' alto circa 6,2 pt); la tavola dei tipi di tempio
e' larga 880 unita' (176 mm, stessa scala).
"""
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(QUI, '..', '..', '..'))
USCITA = os.path.join(VAULT, 'anno-1', 'semestre-1', 'storia-architettura', 'materiale',
                      'appunti-pdf', 'figure')
FONT = "Avenir Next, Helvetica Neue, sans-serif"
TRATTEGGIO = ('<pattern id="tr" width="4" height="4" patternUnits="userSpaceOnUse" '
              'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="4" '
              'stroke="#000" stroke-width="1.1"/></pattern>')


def salva(nome, w, h, corpo):
    os.makedirs(USCITA, exist_ok=True)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
           f'<defs>{TRATTEGGIO}</defs><rect width="{w}" height="{h}" fill="#fff"/>'
           f'<g fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round">'
           + ''.join(corpo) + '</g></svg>')
    with open(os.path.join(USCITA, nome), 'w', encoding='utf-8') as f:
        f.write(svg)
    print('scritto', nome)


def f(x):
    return f'{x:.2f}'.rstrip('0').rstrip('.')


def linea(x1, y1, x2, y2, s=1.0, tratt=False):
    d = ' stroke-dasharray="3 2.5"' if tratt else ''
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke-width="{s}"{d}/>'


def rett(x, y, w, h, s=1.0, pieno=False, motivo=None):
    fill = '#000' if pieno else ('url(#tr)' if motivo else 'none')
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" stroke-width="{s}" fill="{fill}"/>'


def cerchio(x, y, r, s=1.0, pieno=True):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" stroke-width="{s}" fill="{"#000" if pieno else "none"}"/>'


def percorso(d, s=1.0, pieno=False, motivo=False, tratt=False):
    fill = '#000' if pieno else ('url(#tr)' if motivo else 'none')
    da = ' stroke-dasharray="3 2.5"' if tratt else ''
    return f'<path d="{d}" stroke-width="{s}" fill="{fill}"{da}/>'


def poli(punti, s=1.0, chiuso=False, pieno=False):
    p = ' '.join(f'{f(x)},{f(y)}' for x, y in punti)
    tag = 'polygon' if chiuso else 'polyline'
    return f'<{tag} points="{p}" stroke-width="{s}" fill="{"#000" if pieno else "none"}"/>'


def testo(x, y, t, size=11, ancora='start', corsivo=False, peso=400):
    st = ' font-style="italic"' if corsivo else ''
    return (f'<text x="{f(x)}" y="{f(y)}" font-family="{FONT}" font-size="{size}" font-weight="{peso}" '
            f'text-anchor="{ancora}" fill="#000" stroke="none"{st}>{t}</text>')


def etichetta(px, py, tx, ty, t, ancora='start', size=11, corsivo=False):
    """Linea di richiamo dal punto (px,py) al testo in (tx,ty), con un pallino sul punto."""
    dx = -3 if ancora == 'start' else 3
    return (linea(px, py, tx + dx, ty - size * 0.35, 0.5) + cerchio(px, py, 1.1)
            + testo(tx, ty, t, size, ancora, corsivo))


# ---------------------------------------------------------------- piante dei templi
def colonna_p(x, y, r):
    return cerchio(x, y, r)


def semicolonna(x, y, r, lato):
    """semicolonna addossata a una parete; lato = direzione verso cui sporge (dx, dy)."""
    dx, dy = lato
    r = r * 1.2
    a = math.atan2(dy, dx)
    x1, y1 = x + r * math.cos(a + math.pi / 2), y + r * math.sin(a + math.pi / 2)
    x2, y2 = x + r * math.cos(a - math.pi / 2), y + r * math.sin(a - math.pi / 2)
    return percorso(f'M{f(x1)},{f(y1)} A{f(r)},{f(r)} 0 0 0 {f(x2)},{f(y2)} Z', 0.6, pieno=True)


def muro(x1, y1, x2, y2, sp):
    """muro pieno nero dallo spigolo (x1,y1) a (x2,y2) (orizzontale o verticale), spessore sp."""
    if abs(y1 - y2) < 1e-6:
        return rett(min(x1, x2), y1 - sp / 2, abs(x2 - x1), sp, 0, pieno=True)
    return rett(x1 - sp / 2, min(y1, y2), sp, abs(y2 - y1), 0, pieno=True)


def nucleo(cx, y0, L, W, sp, r, fronte='antis', retro='antis', porta=True):
    """cella con pronao (in basso, ingresso) e, se retro='antis', opistodomo (in alto).
    cx: asse; y0: estremita' superiore; L: lunghezza; W: larghezza esterna."""
    out = []
    xl, xr = cx - W / 2 + sp / 2, cx + W / 2 - sp / 2
    y1 = y0 + L
    prof = W * 0.55  # profondita' di pronao e opistodomo
    out.append(muro(xl, y0, xl, y1, sp))
    out.append(muro(xr, y0, xr, y1, sp))
    # pronao: muro della porta
    yp = y1 - prof
    if porta:
        out.append(muro(xl, yp, cx - W * 0.12, yp, sp))
        out.append(muro(cx + W * 0.12, yp, xr, yp, sp))
    else:
        out.append(muro(xl, yp, xr, yp, sp))
    if fronte == 'antis':
        for x in (cx - W * 0.17, cx + W * 0.17):
            out.append(colonna_p(x, y1 - sp / 2, r))
    if retro == 'antis':
        yo = y0 + prof
        out.append(muro(xl, yo, xr, yo, sp))
        for x in (cx - W * 0.17, cx + W * 0.17):
            out.append(colonna_p(x, y0 + sp / 2, r))
    elif retro == 'chiuso':
        out.append(muro(xl - sp / 2, y0 + sp / 2, xr + sp / 2, y0 + sp / 2, sp))
    return out


def anello(cx, cy, nx, ny, s, r):
    """colonne sul perimetro di un rettangolo di nx x ny colonne, interasse s, centrato."""
    out = []
    x0, y0 = cx - (nx - 1) * s / 2, cy - (ny - 1) * s / 2
    for i in range(nx):
        for j in range(ny):
            if i in (0, nx - 1) or j in (0, ny - 1):
                out.append(colonna_p(x0 + i * s, y0 + j * s, r))
    return out, (x0, y0, x0 + (nx - 1) * s, y0 + (ny - 1) * s)


def stilobate(x0, y0, x1, y1, m):
    return rett(x0 - m, y0 - m, x1 - x0 + 2 * m, y1 - y0 + 2 * m, 0.7)


def fig_parti():
    W, H = 260, 268
    c = []
    s, r = 20, 4.6
    cx, cy = 70, 122
    col, (x0, y0, x1, y1) = anello(cx, cy, 6, 11, s, r)
    c.append(stilobate(x0, y0, x1, y1, 10))
    c += col
    sp, Wn, L = 4, 56, 164
    yt = cy - L / 2
    c += nucleo(cx, yt, L, Wn, sp, 3.6)
    # etichette a destra
    tx = 150
    yb = yt + L
    prof = Wn * 0.55
    c.append(etichetta(cx + 8, yt + prof / 2 + 2, tx, 52, 'opistodomo'))
    c.append(etichetta(cx + 10, cy, tx, cy - 6, 'cella'))
    c.append(testo(tx, cy + 7, '(<tspan font-style="italic">naos</tspan>)'))
    c.append(etichetta(cx + 8, yb - prof / 2 + 2, tx, 186, 'pronao'))
    c.append(etichetta(cx + Wn / 2, yb - 1, tx, 204, 'anta'))
    c.append(etichetta(cx + Wn / 2 + 9, 86, tx, 86, 'peristasi'))
    c.append(etichetta(x1, y0 + 2 * s, tx, 28, 'colonnato'))
    c.append(etichetta(x1 + 10, y1 + 6, tx, 232, 'stilobate'))
    # ingresso
    c.append(poli([(cx, y1 + 30), (cx, y1 + 15)], 0.8))
    c.append(poli([(cx - 3.5, y1 + 20), (cx, y1 + 14), (cx + 3.5, y1 + 20)], 0.8))
    c.append(testo(cx, y1 + 42, 'ingresso', 10, 'middle', corsivo=True))
    salva('s01-parti-del-tempio.svg', W, H, c)


def fig_tipi():
    W, H = 880, 402
    c = []
    s, r, sp = 12, 2.9, 3
    Wn = 34      # larghezza del nucleo (cella con pronao e opistodomo)
    cols = [88 + 176 * i for i in range(5)]
    # ---- prima fila: ingombri piccoli, base allineata a y=118
    base1 = 116
    lab1 = 140
    # in antis
    cx = cols[0]
    L = 62
    c += nucleo(cx, base1 - L, L, Wn, sp, r, fronte='antis', retro='chiuso')
    c.append(stilobate(cx - Wn / 2, base1 - L, cx + Wn / 2, base1, 6))
    c.append(testo(cx, lab1, 'in antis', 12, 'middle', corsivo=True))
    # doppiamente in antis
    cx = cols[1]
    L = 76
    c += nucleo(cx, base1 - L, L, Wn, sp, r, fronte='antis', retro='antis')
    c.append(stilobate(cx - Wn / 2, base1 - L, cx + Wn / 2, base1, 6))
    c.append(testo(cx, lab1, 'doppiamente <tspan font-style="italic">in antis</tspan>', 12, 'middle'))
    # prostilo: cella con pronao, fila di 4 colonne su tutta la fronte
    cx = cols[2]
    L = 62
    yc = base1 - 14
    c += nucleo(cx, yc - L, L, Wn, sp, r, fronte='nessuna', retro='chiuso')
    for i in range(4):
        c.append(colonna_p(cx - Wn / 2 + sp / 2 + i * (Wn - sp) / 3, base1 - sp / 2, r))
    c.append(stilobate(cx - Wn / 2, yc - L, cx + Wn / 2, base1, 6))
    c.append(testo(cx, lab1, 'prostilo', 12, 'middle'))
    # anfiprostilo
    cx = cols[3]
    L = 62
    yc = base1 - 14
    c += nucleo(cx, yc - L, L, Wn, sp, r, fronte='nessuna', retro='nessuno', porta=True)
    c.append(muro(cx - Wn / 2 + sp / 2, yc - L + sp / 2, cx + Wn / 2 - sp / 2, yc - L + sp / 2, sp))
    for yy in (base1 - sp / 2, yc - L - 14 + sp / 2):
        for i in range(4):
            c.append(colonna_p(cx - Wn / 2 + sp / 2 + i * (Wn - sp) / 3, yy, r))
    c.append(stilobate(cx - Wn / 2, yc - L - 14, cx + Wn / 2, base1, 6))
    c.append(testo(cx, lab1, 'anfiprostilo', 12, 'middle'))
    # monoptero: giro di colonne senza cella
    cx = cols[4]
    R = 30
    cyy = base1 - R - 6
    c.append(cerchio(cx, cyy, R + 7, 0.7, pieno=False))
    for k in range(10):
        a = 2 * math.pi * k / 10
        c.append(colonna_p(cx + R * math.cos(a), cyy + R * math.sin(a), r))
    c.append(testo(cx, lab1, 'monoptero', 12, 'middle'))

    # ---- seconda fila: periptero e derivati, base a y=360
    base2 = 366
    lab2 = 390
    # periptero 6 x 11
    cx = cols[0]
    col, (x0, y0, x1, y1) = anello(cx, base2 - 6 - 5 * s, 6, 11, s, r)
    c.append(stilobate(x0, y0, x1, y1, 6))
    c += col
    Ln = 84
    c += nucleo(cx, (y0 + y1) / 2 - Ln / 2, Ln, Wn, sp, r)
    c.append(testo(cx, lab2, 'periptero', 12, 'middle'))
    # pseudoperiptero: muri della cella portati sulla linea delle colonne, con semicolonne;
    # colonne libere solo nel portico d'ingresso
    cx = cols[1]
    nx, ny = 6, 11
    xa, xb = cx - (nx - 1) * s / 2, cx + (nx - 1) * s / 2
    ya, yb = base2 - 6 - (ny - 1) * s, base2 - 6
    yport = yb - 2 * s          # fronte della cella: dietro due intercolumni di portico
    c.append(stilobate(xa, ya, xb, yb, 6))
    for xx in (xa, xb):
        c.append(muro(xx, ya, xx, yport, sp))
    c.append(muro(xa, ya, xb, ya, sp))
    c.append(muro(xa, yport, cx - 5, yport, sp))
    c.append(muro(cx + 5, yport, xb, yport, sp))
    c.append(muro(xa, ya + 2 * s, xb, ya + 2 * s, sp))
    for j in range(ny - 2):
        yy = ya + j * s
        c.append(semicolonna(xa - sp / 2, yy, r, (-1, 0)))
        c.append(semicolonna(xb + sp / 2, yy, r, (1, 0)))
    for i in range(1, nx - 1):
        c.append(semicolonna(xa + i * s, ya - sp / 2, r, (0, -1)))
    for i in range(nx):
        c.append(colonna_p(xa + i * s, yb, r))
    for xx in (xa, xb):
        c.append(colonna_p(xx, yb - s, r))
    c.append(testo(cx, lab2, 'pseudoperiptero', 12, 'middle'))
    # diptero 8 x 15
    cx = cols[2]
    cyy = base2 - 6 - 7 * s
    col, (x0, y0, x1, y1) = anello(cx, cyy, 8, 15, s, r)
    col2, _ = anello(cx, cyy, 6, 13, s, r)
    c.append(stilobate(x0, y0, x1, y1, 6))
    c += col + col2
    c += nucleo(cx, cyy - Ln / 2, Ln, Wn, sp, r)
    c.append(testo(cx, lab2, 'diptero', 12, 'middle'))
    # pseudodiptero: giro esterno di colonne libere; il giro interno diventa una parete
    # con semicolonne addossate
    cx = cols[3]
    col, (x0, y0, x1, y1) = anello(cx, cyy, 8, 15, s, r)
    c.append(stilobate(x0, y0, x1, y1, 6))
    c += col
    xa, xb = cx - 2.5 * s, cx + 2.5 * s
    ya, yb = cyy - 6 * s, cyy + 6 * s
    for xx in (xa, xb):
        c.append(muro(xx, ya, xx, yb, sp))
    c.append(muro(xa, ya, xb, ya, sp))
    c.append(muro(xa, yb, cx - 5, yb, sp))
    c.append(muro(cx + 5, yb, xb, yb, sp))
    c.append(muro(xa, ya + 3 * s, xb, ya + 3 * s, sp))
    c.append(muro(xa, yb - 3 * s, cx - 5, yb - 3 * s, sp))
    c.append(muro(cx + 5, yb - 3 * s, xb, yb - 3 * s, sp))
    for j in range(13):
        yy = ya + j * s
        c.append(semicolonna(xa - sp / 2, yy, r, (-1, 0)))
        c.append(semicolonna(xb + sp / 2, yy, r, (1, 0)))
    for i in range(1, 5):
        c.append(semicolonna(xa + i * s, ya - sp / 2, r, (0, -1)))
        c.append(semicolonna(xa + i * s, yb + sp / 2, r, (0, 1)))
    c.append(testo(cx, lab2, 'pseudodiptero', 12, 'middle'))
    # ipetro: grande diptero 8 x 17, cella con colonnati interni, centro scoperto
    cx = cols[4]
    cyy = base2 - 6 - 8 * s
    col, (x0, y0, x1, y1) = anello(cx, cyy, 8, 17, s, r)
    col2, _ = anello(cx, cyy, 6, 15, s, r)
    c.append(stilobate(x0, y0, x1, y1, 6))
    c += col + col2
    Wi, Li = 2 * s + 12, 12 * s
    xl, xr = cx - Wi / 2, cx + Wi / 2
    yt, yb = cyy - Li / 2, cyy + Li / 2
    c.append(rett(cx - 6, yt + 34, 12, Li - 68, 0.6, motivo=True))
    c.append(muro(xl, yt, xl, yb, sp))
    c.append(muro(xr, yt, xr, yb, sp))
    c.append(muro(xl, yt + 18, xr, yt + 18, sp))
    c.append(muro(xl, yb - 18, cx - 5, yb - 18, sp))
    c.append(muro(cx + 5, yb - 18, xr, yb - 18, sp))
    for yy in range(int(yt + 30), int(yb - 26), 12):
        c.append(colonna_p(cx - 9, yy, 2.2))
        c.append(colonna_p(cx + 9, yy, 2.2))
    for xx in (cx - 6, cx + 6):
        c.append(colonna_p(xx, yb - sp / 2, r))
        c.append(colonna_p(xx, yt + sp / 2, r))
    c.append(testo(cx, lab2, 'ipetro', 12, 'middle'))
    salva('s01-tipi-di-tempio.svg', W, H, c)


# ---------------------------------------------------------------- intercolumni
def fig_intercolumni():
    W, H = 260, 352
    c = []
    d = 10.0
    righe = [('picnostilo', 1.5, '1½ d'), ('sistilo', 2, '2 d'), ('eustilo', 2.25, '2¼ d'),
             ('diastilo', 3, '3 d'), ('areostilo', 4, 'oltre 3 d')]
    y = 14
    hcol = 40
    for nome, k, mis in righe:
        c.append(testo(8, y, nome, 11, peso=600))
        c.append(testo(252, y, mis, 11, 'end'))
        top = y + 8
        x = 8
        xs = []
        for i in range(4):
            xs.append(x)
            x += d + k * d
        xend = xs[-1] + d
        c.append(rett(xs[0] - 3, top, xend - xs[0] + 6, 6, 0.8))           # architrave
        for xx in xs:
            c.append(rett(xx - 1.5, top + 6, d + 3, 3, 0.8))              # abaco
            c.append(rett(xx, top + 9, d, hcol - 9, 0.8))                 # fusto
        c.append(linea(xs[0] - 6, top + hcol, xend + 6, top + hcol, 1.0))  # stilobate
        # quota del primo intercolumnio
        yq = top + hcol + 6
        xa, xb = xs[0] + d, xs[1]
        c.append(linea(xa, yq, xb, yq, 0.5))
        c.append(linea(xa, yq - 3, xa, yq + 3, 0.5))
        c.append(linea(xb, yq - 3, xb, yq + 3, 0.5))
        y += 70
    salva('s01-intercolumni.svg', W, H, c)


# ---------------------------------------------------------------- sistema trilitico
def fig_trilitico():
    W, H = 260, 268
    c = []
    # trilite
    c.append(rett(70, 30, 18, 66, 1.0))
    c.append(rett(152, 30, 18, 66, 1.0))
    c.append(rett(58, 14, 124, 16, 1.0))
    c.append(linea(40, 96, 200, 96, 1.2))
    c.append(etichetta(120, 22, 196, 14, 'elemento', ancora='start'))
    c.append(testo(196, 26, 'orizzontale'))
    c.append(etichetta(161, 70, 196, 64, 'elementi'))
    c.append(testo(196, 76, 'verticali'))
    # fronte del tempio
    y0 = 128
    xs = [30 + i * 40 for i in range(6)]
    cw = 14
    ytrab = y0 + 30
    c.append(poli([(14, y0 + 24), (130, y0), (246, y0 + 24)], 1.0, chiuso=True))   # frontone
    c.append(rett(14, y0 + 24, 232, 6, 1.0))                                      # cornice
    c.append(rett(18, ytrab, 224, 10, 1.0))                                      # fregio
    c.append(rett(18, ytrab + 10, 224, 10, 1.0))                                 # architrave
    for x in xs:
        c.append(rett(x - cw / 2 + 7, ytrab + 20, cw, 64, 1.0))
    ys = ytrab + 84
    for k in range(3):
        c.append(rett(14 - k * 5, ys + k * 6, 232 + k * 10, 6, 0.8))
    salva('s01-sistema-trilitico.svg', W, H, c)


# ---------------------------------------------------------------- ordine dorico
def fusto(cx, ybase, ytop, rb, rt, s=1.0, scan=6):
    out = [poli([(cx - rb, ybase), (cx - rt, ytop), (cx + rt, ytop), (cx + rb, ybase)], s, chiuso=True)]
    for i in range(1, scan):
        t = -1 + 2 * i / scan
        out.append(linea(cx + t * rb * 0.98, ybase, cx + t * rt * 0.98, ytop, 0.45))
    return out


def triglifo(x, y, w, h, s=0.8):
    out = [rett(x, y, w, h, s)]
    g = w / 6
    for k in (1.5, 3.5):
        out.append(rett(x + k * g, y + h * 0.1, g, h * 0.9, 0, pieno=True))
    out.append(rett(x, y + h * 0.1, g * 0.5, h * 0.9, 0, pieno=True))
    out.append(rett(x + w - g * 0.5, y + h * 0.1, g * 0.5, h * 0.9, 0, pieno=True))
    return out


def fig_dorico():
    W, H = 260, 282
    c = []
    D = 28.0          # diametro inferiore
    ia = 66.0         # interasse = 2 x (triglifo + metopa)
    tw, mw = 13.0, 20.0
    c1, c2 = 44.0, 44.0 + ia
    yst = 252.0       # piano dello stilobate
    hcol = 150.0
    ycap = yst - hcol
    hab, hech = 6.0, 9.0
    ytop_f = ycap + hab + hech   # sommita' del fusto
    rt, rb = D * 0.39, D / 2
    xL, xR = c1 - 33, c2 + 33
    # crepidoma (3 gradini)
    for k in range(3):
        c.append(rett(xL - 4 - k * 6, yst + k * 8, (xR - xL) + 8 + k * 12, 8, 0.9))
    for cx in (c1, c2):
        c += fusto(cx, yst, ytop_f, rb, rt)
        # collarino (anelli)
        for k in range(3):
            c.append(linea(cx - rt - 1, ytop_f + 1.5 + k * 1.8 - 6, cx + rt + 1, ytop_f + 1.5 + k * 1.8 - 6, 0.5))
        # echino
        c.append(percorso(f'M{f(cx - rt)},{f(ytop_f)} C{f(cx - rt - 2)},{f(ytop_f - 4)} {f(cx - D * 0.62)},{f(ycap + hab + 2)} '
                          f'{f(cx - D * 0.62)},{f(ycap + hab)} L{f(cx + D * 0.62)},{f(ycap + hab)} '
                          f'C{f(cx + D * 0.62)},{f(ycap + hab + 2)} {f(cx + rt + 2)},{f(ytop_f - 4)} {f(cx + rt)},{f(ytop_f)} Z', 0.9))
        c.append(rett(cx - D * 0.64, ycap, D * 1.28, hab, 0.9))      # abaco
    # trabeazione
    ha, hf, hc = 22.0, 20.0, 12.0
    ya = ycap - ha
    yf = ya - hf
    yc = yf - hc
    c.append(rett(xL, ya, xR - xL, ha, 0.9))                         # architrave
    c.append(rett(xL, ya, xR - xL, 3, 0.6))                          # tenia
    c.append(rett(xL, yf, xR - xL, hf, 0.9))                         # fregio
    for xx in (c1, (c1 + c2) / 2, c2):
        c += triglifo(xx - tw / 2, yf, tw, hf)
        c.append(rett(xx - tw / 2, ya + 3, tw, 2, 0, pieno=True))   # regula
    for xx in (c1 - ia / 2,):
        pass
    c.append(rett(xL - 6, yc, xR - xL + 12, hc, 0.9))                # cornice
    c.append(linea(xL - 6, yc + 4, xR + 6, yc + 4, 0.5))
    # taglio a sinistra e a destra del frammento (linea di rottura)
    # etichette
    tx = 170
    c.append(etichetta(xR + 4, yc + 6, tx, 36, 'cornice'))
    c.append(etichetta(c2 + tw / 2 - 2, yf + 10, tx, 54, 'triglifo'))
    c.append(etichetta((c1 + c2) / 2 + tw / 2 + 12, yf + 14, tx, 72, 'metopa'))
    c.append(etichetta(xR - 3, ya + 11, tx, 90, 'architrave'))
    c.append(etichetta(c2 + D * 0.55, ycap + 3, tx, 108, 'abaco'))
    c.append(etichetta(c2 + D * 0.48, ycap + hab + 4, tx, 125, 'echino'))
    c.append(etichetta(c2 + rt, ytop_f - 3, tx, 142, 'collarino'))
    c.append(etichetta(c2 + 4, 180, tx, 180, 'fusto con'))
    c.append(testo(tx, 192, 'scanalature'))
    c.append(etichetta(xR + 4, yst + 4, tx, yst + 3, 'stilobate'))
    # graffe a sinistra: trabeazione / colonna
    def graffa(x, y1, y2, t1, t2=None):
        out = [percorso(f'M{f(x + 4)},{f(y1)} Q{f(x)},{f(y1)} {f(x)},{f(y1 + 4)} L{f(x)},{f((y1 + y2) / 2 - 3)} '
                        f'Q{f(x)},{f((y1 + y2) / 2)} {f(x - 4)},{f((y1 + y2) / 2)} Q{f(x)},{f((y1 + y2) / 2)} '
                        f'{f(x)},{f((y1 + y2) / 2 + 3)} L{f(x)},{f(y2 - 4)} Q{f(x)},{f(y2)} {f(x + 4)},{f(y2)}', 0.6)]
        return out
    gx = xR + 0  # (le graffe sono a destra delle etichette? no: a sinistra del disegno)
    c += graffa(xL - 12, yc, ya + ha, '')
    c.append(testo(xL - 18, (yc + ya + ha) / 2 + 3, 'trabeazione', 10, 'middle', corsivo=True)
             .replace('<text ', f'<text transform="rotate(-90 {f(xL - 18)} {f((yc + ya + ha) / 2 + 3)})" '))
    c += graffa(xL - 12, ycap, yst, '')
    c.append(testo(xL - 18, (ycap + yst) / 2, 'colonna', 10, 'middle', corsivo=True)
             .replace('<text ', f'<text transform="rotate(-90 {f(xL - 18)} {f((ycap + yst) / 2)})" '))
    # spostamento: tutto il disegno a destra per far posto alle graffe
    c = [f'<g transform="translate(14,0)">'] + c + ['</g>']
    salva('s01-ordine-dorico.svg', W, H, c)


# ---------------------------------------------------------------- triglifi dal legno
def fig_legno():
    W, H = 260, 236
    c = []
    xL, xR = 14, 160
    # in alto: struttura in legno
    y = 26
    c.append(testo(8, 12, 'in legno', 11, peso=600))
    c.append(rett(xL, y + 26, xR - xL, 16, 0.9))                       # trave di architrave
    for k in range(4):                                                # venature
        c.append(linea(xL + 4, y + 30 + k * 3, xR - 4, y + 30 + k * 3, 0.35))
    xs = [xL + 8 + i * 40 for i in range(4)]
    for x in xs:
        c.append(rett(x, y + 4, 14, 22, 0.9))                         # testata
        c.append(cerchio(x + 7, y + 15, 5, 0.5, pieno=False))
        c.append(cerchio(x + 7, y + 15, 2.5, 0.5, pieno=False))
    c.append(linea(xL - 4, y + 4, xR + 4, y + 4, 0.9))                 # tavolato del tetto
    c.append(etichetta(xs[3] + 14, y + 12, 172, y + 4, 'testate'))
    c.append(testo(172, y + 16, 'delle travi'))
    c.append(etichetta(xs[2] + 27, y + 18, 172, y + 34, 'vuoto tra'))
    c.append(testo(172, y + 46, 'le travi'))
    # freccia
    c.append(linea(87, 84, 87, 108, 0.9))
    c.append(poli([(82, 101), (87, 109), (92, 101)], 0.9))
    c.append(testo(96, 100, 'litizzazione', 10, corsivo=True))
    # in basso: in pietra
    y = 130
    c.append(testo(8, y - 4, 'in pietra', 11, peso=600))
    yf = y + 10
    c.append(rett(xL - 4, yf - 10, xR - xL + 8, 10, 0.9))             # cornice
    c.append(rett(xL, yf, xR - xL, 22, 0.9))                          # fregio
    for x in xs:
        c += triglifo(x, yf, 14, 22)
    c.append(rett(xL, yf + 22, xR - xL, 18, 0.9))                     # architrave
    c.append(etichetta(xs[3] + 10, yf + 12, 172, yf + 8, 'triglifo'))
    c.append(etichetta(xs[2] + 27, yf + 15, 172, yf + 30, 'metopa'))
    c.append(etichetta(xR - 10, yf + 33, 172, yf + 52, 'architrave'))
    salva('s01-triglifi-dal-legno.svg', W, H, c)


# ---------------------------------------------------------------- conflitto angolare
def fig_conflitto():
    W, H = 260, 326
    c = []
    D, tw, mw = 28.0, 12.0, 20.5
    ia = 2 * (tw + mw)          # 65
    edge = 228.0                 # spigolo del tempio
    au = D * 0.5               # semilarghezza dell'architrave oltre l'asse della colonna d'angolo

    def riga(y0, titolo, sotto, modo):
        out = [testo(8, y0, titolo, 11, peso=600), testo(8, y0 + 13, sotto, 10, corsivo=True)]
        yf = y0 + 22
        hf, ha, hcol = 18.0, 16.0, 26.0
        xL = 6
        if modo == 'contratto':
            ca = edge - tw / 2 - (au - tw / 2) * 0 - au + (au - tw / 2) * 0  # placeholder
        # assi delle colonne
        cang = edge - au                        # asse della colonna d'angolo (posizione normale)
        if modo == 'contratto':
            cang = edge - tw / 2 - 0.0          # triglifo sullo spigolo: la colonna ...
            cang = edge - au                    # ... resta sotto lo spigolo
        assi = [cang - k * ia for k in range(3)]
        if modo == 'contratto':
            # l'ultimo interasse si accorcia: le altre colonne restano dove sono
            sh = (au - tw / 2)
            assi = [edge - au] + [edge - au - sh - k * ia + 0 for k in range(1, 3)]
            # spostiamo invece tutte le colonne non d'angolo verso lo spigolo: interasse d'angolo ridotto
            assi = [edge - au, edge - au - (ia - sh), edge - au - (ia - sh) - ia]
        out.append(rett(xL, yf, edge - xL, hf, 0.9))
        out.append(rett(xL, yf + hf, edge - xL, ha, 0.9))
        out.append(linea(edge, yf - 6, edge, yf + hf + ha + hcol + 4, 0.0))
        # triglifi
        if modo == 'regola':
            pos = []
            for a in assi:
                pos += [a, a - ia / 2]
        elif modo == 'metopa':
            pos = [edge - tw / 2, assi[0] - ia / 2, assi[1], assi[1] - ia / 2, assi[2], assi[2] - ia / 2]
        else:
            pos = [edge - tw / 2, edge - tw / 2 - ia / 2, edge - tw / 2 - ia, edge - tw / 2 - 1.5 * ia,
                   edge - tw / 2 - 2 * ia, edge - tw / 2 - 2.5 * ia]
        for p in pos:
            if p - tw / 2 > xL:
                out += triglifo(p - tw / 2, yf, tw, hf, 0.7)
        if modo == 'regola':
            out.append(rett(assi[0] + tw / 2, yf + 0.5, edge - assi[0] - tw / 2 - 0.5, hf - 1, 0, motivo=True))
        if modo == 'metopa':
            out.append(rett(assi[0] - ia / 2 + tw / 2, yf + 0.5, edge - tw - (assi[0] - ia / 2 + tw / 2), hf - 1, 0, motivo=True))
        # colonne (sotto l'architrave)
        yc = yf + hf + ha
        for a in assi:
            out.append(rett(a - D * 0.6, yc, D * 1.2, 3, 0.7))
            out.append(poli([(a - D * 0.4, yc + 3), (a - D * 0.47, yc + hcol), (a + D * 0.47, yc + hcol), (a + D * 0.4, yc + 3)], 0.8))
            out.append(linea(a, yf - 4, a, yc + hcol + 2, 0.5, tratt=True))
        # spigolo
        out.append(linea(edge, yf - 6, edge, yc + hcol + 2, 0.4))
        return out

    c += riga(12, 'La regola', 'triglifo in asse con la colonna: spazio di risulta', 'regola')
    c += riga(118, 'Ultima metopa ampliata', 'triglifo sullo spigolo, metopa più larga', 'metopa')
    c += riga(224, 'Interasse d\'angolo contratto', 'triglifo sullo spigolo, metope uguali', 'contratto')
    salva('s01-conflitto-angolare.svg', W, H, c)


# ---------------------------------------------------------------- capitello ionico
def spirale(cx, cy, R, giri=2.6, verso=1, r_occhio=None):
    """voluta: spirale logaritmica che parte in alto (angolo -90 gradi) e si avvolge verso
    l'interno; verso=+1 orario (voluta destra vista di fronte), -1 antiorario."""
    pts = []
    n = 220
    k = math.log(R / (R * 0.16)) / (giri * 2 * math.pi)
    for i in range(n + 1):
        t = giri * 2 * math.pi * i / n
        rr = R * math.exp(-k * t)
        a = -math.pi / 2 + verso * t
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    out = [poli(pts, 1.0)]
    out.append(cerchio(cx, cy, r_occhio or R * 0.15, 0.6, pieno=True))
    return out


def fig_ionico():
    W, H = 260, 272
    c = []
    cx = 100
    # --- fronte
    y0 = 20
    wa = 128                      # larghezza dell'abaco
    c.append(rett(cx - wa / 2, y0, wa, 6, 0.9))                    # abaco
    yc = y0 + 6                    # canale
    R = 17
    xv = wa / 2 - 4                # centri delle volute rispetto all'asse
    c.append(linea(cx - xv, yc, cx + xv, yc, 0.9))
    c.append(linea(cx - xv, yc + 8, cx + xv, yc + 8, 0.9))
    c.append(percorso(f'M{f(cx - xv)},{f(yc + 8)} Q{f(cx)},{f(yc + 13)} {f(cx + xv)},{f(yc + 8)}', 0.0))
    for verso, sx in ((-1, -1), (1, 1)):
        c += spirale(cx + sx * xv, yc + R, R, 2.4, verso)
    # echino con ovoli e dardi
    ye = yc + 9
    he = 14
    xe = 32
    c.append(percorso(f'M{f(cx - xe - 6)},{f(ye)} L{f(cx + xe + 6)},{f(ye)} Q{f(cx + xe)},{f(ye + he)} {f(cx + xe - 6)},{f(ye + he)} '
                      f'L{f(cx - xe + 6)},{f(ye + he)} Q{f(cx - xe)},{f(ye + he)} {f(cx - xe - 6)},{f(ye)} Z', 0.8))
    for i in range(-2, 3):
        x = cx + i * 12
        c.append(f'<ellipse cx="{f(x)}" cy="{f(ye + 7)}" rx="4.2" ry="5.2" stroke-width="0.7" fill="none"/>')
        if i < 2:
            c.append(linea(x + 6, ye + 2, x + 6, ye + 12, 0.6))
            c.append(poli([(x + 4.5, ye + 10), (x + 6, ye + 13), (x + 7.5, ye + 10)], 0.6))
    # astragalo e fusto
    yfu = ye + he + 2
    c.append(rett(cx - 30, ye + he, 60, 4, 0.8))
    c += fusto(cx, yfu + 44, yfu + 4, 29, 28, 0.9, scan=8)
    c.append(etichetta(cx + 30, y0 + 3, 188, y0 + 4, 'abaco'))
    c.append(etichetta(cx + xv + R * 0.7, yc + R - 8, 188, yc + 16, 'voluta'))
    c.append(etichetta(cx + 12, ye + 7, 188, ye + 32, 'ovoli e dardi'))
    c.append(etichetta(cx + 20, yfu + 30, 188, yfu + 34, 'fusto'))
    c.append(testo(8, 12, 'di fronte', 11, peso=600))
    # --- fianco
    y1 = 150
    c.append(testo(8, y1 - 8, 'di fianco', 11, peso=600))
    c.append(rett(cx - wa / 2, y1, wa, 6, 0.9))
    yb = y1 + 6
    Rh = R + 1
    # sagoma del balaustro: alto quanto la voluta agli estremi, strozzato al centro
    xl, xr = cx - wa / 2 + 3, cx + wa / 2 - 3
    c.append(percorso(f'M{f(xl)},{f(yb)} L{f(xr)},{f(yb)} '
                      f'C{f(xr + 3)},{f(yb + Rh * 1.4)} {f(xr - 6)},{f(yb + 2 * Rh)} {f(xr - 14)},{f(yb + 2 * Rh)} '
                      f'C{f(cx + 30)},{f(yb + 2 * Rh)} {f(cx + 14)},{f(yb + Rh * 1.05)} {f(cx)},{f(yb + Rh * 1.05)} '
                      f'C{f(cx - 14)},{f(yb + Rh * 1.05)} {f(cx - 30)},{f(yb + 2 * Rh)} {f(xl + 14)},{f(yb + 2 * Rh)} '
                      f'C{f(xl + 6)},{f(yb + 2 * Rh)} {f(xl - 3)},{f(yb + Rh * 1.4)} {f(xl)},{f(yb)} Z', 0.9))
    # scanalature del balaustro
    for t in (0.35, 0.62):
        for sx in (-1, 1):
            xa = cx + sx * 12
            xb = cx + sx * (wa / 2 - 10)
            c.append(percorso(f'M{f(xa)},{f(yb + Rh * (0.5 + t * 0.4))} Q{f((xa + xb) / 2)},{f(yb + Rh * (0.55 + t * 0.9))} {f(xb)},{f(yb + Rh * (0.4 + t * 1.2))}', 0.45))
    # balteo
    c.append(rett(cx - 6, yb, 12, Rh * 1.05 + 1, 0.8))
    for k in (0.3, 0.55, 0.8):
        c.append(linea(cx - 6, yb + Rh * k, cx + 6, yb + Rh * k, 0.5))
    c.append(rett(cx - 30, yb + 2 * Rh - 6, 60, 4, 0.8))
    c += fusto(cx, yb + 2 * Rh + 40, yb + 2 * Rh - 2, 29, 28, 0.9, scan=8)
    c.append(etichetta(cx + 3, yb + 6, 188, y1 + 6, 'balteo'))
    c.append(etichetta(cx + 44, yb + Rh * 1.3, 188, yb + 32, 'balaustro'))
    salva('s01-capitello-ionico.svg', W, H, c)


# ---------------------------------------------------------------- basi
def profilo_base(cx, ybase, elementi, rf):
    """elementi dal basso: (tipo, altezza, sporgenza); tipo: 'plinto', 'toro', 'scozia',
    'listello'. Disegna il profilo simmetrico; restituisce (out, y dei centri)."""
    out, centri = [], []
    y = ybase
    for tipo, h, sp in elementi:
        yt = y - h
        if tipo in ('plinto', 'listello'):
            out.append(rett(cx - rf - sp, yt, 2 * (rf + sp), h, 0.9))
        elif tipo == 'toro':
            for sx in (-1, 1):
                x0 = cx + sx * (rf + sp - h / 2)
                out.append(percorso(f'M{f(x0)},{f(y)} A{f(h / 2)},{f(h / 2)} 0 0 {0 if sx < 0 else 1} {f(x0)},{f(yt)}', 0.9))
            out.append(linea(cx - (rf + sp - h / 2), y, cx + (rf + sp - h / 2), y, 0.9))
            out.append(linea(cx - (rf + sp - h / 2), yt, cx + (rf + sp - h / 2), yt, 0.9))
        elif tipo == 'scozia':
            for sx in (-1, 1):
                xa = cx + sx * (rf + sp)
                out.append(percorso(f'M{f(xa)},{f(y)} Q{f(cx + sx * (rf + sp - h * 0.9))},{f(y - h * 0.5)} {f(xa)},{f(yt)}', 0.9))
            out.append(linea(cx - rf - sp, y, cx + rf + sp, y, 0.9))
        centri.append((tipo, (y + yt) / 2, rf + sp))
        y = yt
    out += fusto(cx, y - 26, y, rf, rf, 0.9, scan=6)[:1]
    out.append(linea(cx - rf, y - 34, cx + rf, y - 34, 0.0))
    return out, centri


def fig_basi():
    W, H = 260, 176
    c = []
    rf = 18
    cx = 44
    att, ca = profilo_base(cx, 132, [('plinto', 10, 8), ('toro', 11, 6), ('listello', 2, 1.5),
                                      ('scozia', 8, 0.5), ('listello', 2, 1.5), ('toro', 9, 3)], rf)
    c += att
    c.append(testo(cx, 152, 'base attica', 11, 'middle', peso=600))
    cx2 = 172
    vit, cv = profilo_base(cx2, 132, [('plinto', 9, 8), ('scozia', 8, 4), ('listello', 3, 5.5),
                                       ('scozia', 8, 4), ('listello', 2, 5), ('toro', 15, 7)], rf)
    c += vit
    c.append(testo(cx2, 152, 'base vitruviana', 11, 'middle', peso=600))
    c.append(testo(cx2, 165, '(efesina)', 10, 'middle'))
    xt = 86
    for tipo, y, sp in ca:
        if tipo in ('toro', 'scozia'):
            c.append(etichetta(cx + sp - (2 if tipo == 'toro' else 1), y, xt, y + 3.5, tipo, size=10))
    xt2 = 214
    tor = [y for t, y, s_ in cv if t == 'toro'][0]
    sco = [y for t, y, s_ in cv if t == 'scozia']
    c.append(etichetta(cx2 + rf + 5, tor, xt2, tor + 3.5, 'toro', size=10))
    ym = (sco[0] + sco[1]) / 2
    for y in sco:
        c.append(linea(cx2 + rf + 2, y, xt2 - 4, ym, 0.5))
        c.append(cerchio(cx2 + rf + 2, y, 1.1))
    c.append(testo(xt2, ym + 3.5, 'scozie', 10))
    salva('s01-basi.svg', W, H, c)


# ---------------------------------------------------------------- correttivi ottici
def fig_correttivi():
    W, H = 260, 210
    c = []
    # entasi: colonna con profilo rigonfio, tratteggio la rastremazione rettilinea
    cx, yb, yt = 34, 176, 30
    rb, rt = 16, 11
    bul = 6
    for sx in (-1, 1):
        c.append(linea(cx + sx * rb, yb, cx + sx * rt, yt, 0.6, tratt=True))
        ym = yb - (yb - yt) * 0.35
        xm = cx + sx * (rb - (rb - rt) * 0.35 + bul)
        c.append(percorso(f'M{f(cx + sx * rb)},{f(yb)} Q{f(xm + sx * 1)},{f(ym)} {f(cx + sx * rt)},{f(yt)}', 1.0))
    c.append(linea(cx - rb, yb, cx + rb, yb, 1.0))
    c.append(linea(cx - rt, yt, cx + rt, yt, 1.0))
    c.append(testo(cx, 196, 'entasi', 11, 'middle', peso=600))
    # fronte: stilobate convesso, colonne inclinate verso l'interno, colonne d'angolo piu' grosse
    x0, x1 = 80, 252
    ys = 166
    fr = 12        # freccia della curvatura (esagerata)
    c.append(linea(x0 - 4, ys, x1 + 4, ys, 0.6, tratt=True))
    c.append(percorso(f'M{f(x0 - 4)},{f(ys)} Q{f((x0 + x1) / 2)},{f(ys - 2 * fr)} {f(x1 + 4)},{f(ys)}', 1.1))
    c.append(percorso(f'M{f(x0 - 4)},{f(ys + 8)} Q{f((x0 + x1) / 2)},{f(ys + 8 - 2 * fr)} {f(x1 + 4)},{f(ys + 8)}', 0.8))
    c.append(linea(x0 - 4, ys, x0 - 4, ys + 8, 0.8))
    c.append(linea(x1 + 4, ys, x1 + 4, ys + 8, 0.8))
    n = 5
    hc = 92
    xs = [x0 + 8 + i * (x1 - x0 - 16) / (n - 1) for i in range(n)]
    ytr = ys - hc - fr
    for i, x in enumerate(xs):
        t = (x - (x0 - 4)) / (x1 - x0 + 8)
        yb_ = ys - 2 * fr * 2 * t * (1 - t)            # sulla curva (bezier quadratica)
        lean = (x - (x0 + x1) / 2) / ((x1 - x0) / 2) * (-6)
        w = 8.5 if i in (0, n - 1) else 6.5
        ytop = ytr + 2 * fr * 2 * t * (1 - t) * -0.0 - fr * 2 * t * (1 - t) * 2 + fr
        ytop = yb_ - hc
        c.append(poli([(x - w, yb_), (x - w * 0.8 + lean, ytop), (x + w * 0.8 + lean, ytop), (x + w, yb_)], 1.0, chiuso=True))
        c.append(linea(x, yb_ + 2, x, ytop - 4, 0.5, tratt=True))
    # architrave curvo come lo stilobate
    xa0, xa1 = xs[0] - 14, xs[-1] + 14
    ya = ys - hc
    c.append(percorso(f'M{f(xa0)},{f(ya)} Q{f((xa0 + xa1) / 2)},{f(ya - 2 * fr)} {f(xa1)},{f(ya)} '
                      f'L{f(xa1)},{f(ya - 12)} Q{f((xa0 + xa1) / 2)},{f(ya - 12 - 2 * fr)} {f(xa0)},{f(ya - 12)} Z', 1.0))
    c.append(testo((x0 + x1) / 2, 196, 'curvatura e inclinazioni', 11, 'middle', peso=600))
    c.append(testo(xs[0] - 6, 28, 'colonna', 9.5, 'start'))
    c.append(testo(xs[0] - 6, 39, 'd\'angolo', 9.5, 'start'))
    c.append(linea(xs[0] + 2, 42, xs[0] - 1, ya - 2 * fr * 0.1 - 16, 0.5))
    salva('s01-correttivi-ottici.svg', W, H, c)


if __name__ == '__main__':
    fig_parti()
    fig_tipi()
    fig_intercolumni()
    fig_trilitico()
    fig_dorico()
    fig_legno()
    fig_conflitto()
    fig_ionico()
    fig_basi()
    fig_correttivi()
