#!/usr/bin/env python3
"""Casa ad Arzachena (Zanuso): pianta e sezioni quotate in scala vera.

Uso: python3 -I composizione-arzachena.py CARTELLA_IMMAGINI PERCORSO_PDF
Scrive un SVG per tavola (Obsidian) e un unico PDF A3 (stampa al 100%).
Coordinate: X da ovest a est, Y da nord a sud, Z dal pavimento (metri).
Colore delle quote: q = scritta sulla scheda, m = misurata sulla scheda,
h = ipotesi (la scheda non la da').
"""
import math
import os
import sys

W, H = 420.0, 297.0
COL = {'q': '#000000', 'm': '#0b5cad', 'h': '#c62828'}
GRIGIO = '#8a8a8a'
AFM = {' ': 278, ',': 278, '.': 278, '-': 333, ':': 278, "'": 191, '(': 333, ')': 333, '/': 278,
       'i': 222, 'l': 222, 'j': 222, 't': 278, 'f': 278, 'r': 333, 'I': 278, 'm': 833, 'w': 722,
       'M': 833, 'W': 944, '×': 584}


def larghezza(s, size):
    tot = 0
    for c in s:
        tot += AFM.get(c, 667 if c.isupper() else 556)
    return tot / 1000 * size


def q(v):
    return ('%.2f' % abs(v)).replace('.', ',')


class Tavola:
    def __init__(self, nome):
        self.nome = nome
        self.op = []

    def linea(self, pts, col='#000000', w=0.2, dash=None, chiudi=False, fill=None):
        self.op.append(('p', [tuple(p) for p in pts], col, w, dash, chiudi, fill))

    def rett(self, x1, y1, x2, y2, fill='#000000', col=None, w=0.2):
        self.linea([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col or fill, w, None, True, fill)

    def testo(self, x, y, s, size=2.5, col='#000000', anchor='start', rot=0, bold=False):
        self.op.append(('t', x, y, s, size, col, anchor, rot, bold))

    def svg(self, path):
        o = ['<svg xmlns="http://www.w3.org/2000/svg" width="%gmm" height="%gmm" viewBox="0 0 %g %g">' % (W, H, W, H),
             '<rect width="%g" height="%g" fill="#ffffff"/>' % (W, H)]
        for e in self.op:
            if e[0] == 'p':
                _, pts, col, w, dash, chiudi, fill = e
                a = ' '.join('%.3f,%.3f' % p for p in pts)
                tag = 'polygon' if chiudi else 'polyline'
                d = ' stroke-dasharray="%s"' % ' '.join(str(x) for x in dash) if dash else ''
                o.append('<%s points="%s" fill="%s" stroke="%s" stroke-width="%g"%s/>' % (tag, a, fill or 'none', col, w, d))
            else:
                _, x, y, s, size, col, anchor, rot, bold = e
                s = s.replace('&', '&amp;').replace('<', '&lt;')
                r = ' transform="rotate(%g %.3f %.3f)"' % (rot, x, y) if rot else ''
                b = ' font-weight="bold"' if bold else ''
                o.append('<text x="%.3f" y="%.3f" font-family="Helvetica, Arial, sans-serif" font-size="%g" fill="%s" text-anchor="%s"%s%s>%s</text>' % (x, y, size, col, anchor, b, r, s))
        o.append('</svg>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(o))

    def stream(self):
        k = 72 / 25.4
        o = []

        def rgb(c):
            return ' '.join('%.3f' % (int(c[i:i + 2], 16) / 255) for i in (1, 3, 5))
        for e in self.op:
            if e[0] == 'p':
                _, pts, col, w, dash, chiudi, fill = e
                o.append('%s RG %.3f w %s d' % (rgb(col), w * k, '[%s] 0' % ' '.join('%.2f' % (x * k) for x in dash) if dash else '[] 0'))
                if fill:
                    o.append(rgb(fill) + ' rg')
                for i, (x, y) in enumerate(pts):
                    o.append('%.2f %.2f %s' % (x * k, (H - y) * k, 'm' if i == 0 else 'l'))
                o.append(('b' if fill else 's') if chiudi else 'S')
            else:
                _, x, y, s, size, col, anchor, rot, bold = e
                lw = larghezza(s, size)
                sh = {'start': 0, 'middle': lw / 2, 'end': lw}[anchor]
                a = math.radians(-rot)
                c, n = math.cos(a), math.sin(a)
                px, py = x - sh * c, y + sh * n
                t = s.encode('cp1252', 'replace').replace(b'\\', b'\\\\').replace(b'(', b'\\(').replace(b')', b'\\)')
                o.append('BT /%s %.2f Tf %s rg %.4f %.4f %.4f %.4f %.2f %.2f Tm (%s) Tj ET' % (
                    'F2' if bold else 'F1', size * k, rgb(col), c, n, -n, c, px * k, (H - py) * k, t.decode('latin-1')))
        return '\n'.join(o).encode('latin-1')


def scrivi_pdf(tavole, path):
    pag = len(tavole)
    objs = {1: b'<< /Type /Catalog /Pages 2 0 R >>',
            3: b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
            4: b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>'}
    kids = []
    for i, t in enumerate(tavole):
        pid, cid = 5 + 2 * i, 6 + 2 * i
        kids.append('%d 0 R' % pid)
        objs[pid] = ('<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.2f %.2f] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents %d 0 R >>' % (W * 72 / 25.4, H * 72 / 25.4, cid)).encode()
        s = t.stream()
        objs[cid] = b'<< /Length %d >>\nstream\n' % len(s) + s + b'\nendstream'
    objs[2] = ('<< /Type /Pages /Kids [%s] /Count %d >>' % (' '.join(kids), pag)).encode()
    out = bytearray(b'%PDF-1.4\n')
    pos = {}
    for n in sorted(objs):
        pos[n] = len(out)
        out += b'%d 0 obj\n' % n + objs[n] + b'\nendobj\n'
    xref = len(out)
    out += b'xref\n0 %d\n0000000000 65535 f \n' % (len(objs) + 1)
    for n in sorted(objs):
        out += b'%010d 00000 n \n' % pos[n]
    out += b'trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objs) + 1, xref)
    with open(path, 'wb') as f:
        f.write(out)


class Vista:
    """Porta i metri (u orizzontale, v verticale) sul foglio in mm. s = mm per metro."""

    def __init__(self, t, s, x0, y0, su=1, sv=1):
        self.t, self.s, self.x0, self.y0, self.su, self.sv = t, s, x0, y0, su, sv

    def x(self, u):
        return self.x0 + self.su * u * self.s

    def y(self, v):
        return self.y0 + self.sv * v * self.s

    def pts(self, lista):
        return [(self.x(u), self.y(v)) for u, v in lista]

    def piena(self, u1, v1, u2, v2, fill='#000000'):
        self.t.rett(self.x(u1), self.y(v1), self.x(u2), self.y(v2), fill)

    def poli(self, lista, fill=None, col='#000000', w=0.2, dash=None):
        self.t.linea(self.pts(lista), col, w, dash, bool(fill), fill)

    def seg(self, a, b, col='#000000', w=0.2, dash=None):
        self.t.linea(self.pts([a, b]), col, w, dash)

    def rect(self, u1, v1, u2, v2, col='#000000', w=0.2, dash=None, fill=None):
        self.poli([(u1, v1), (u2, v1), (u2, v2), (u1, v2)], fill or None, col, w, dash) if fill else \
            self.t.linea(self.pts([(u1, v1), (u2, v1), (u2, v2), (u1, v2)]), col, w, dash, True)

    def cerchio(self, cu, cv, r, fill=None, col='#000000', w=0.2, a0=0, a1=360):
        n = 72
        p = [(cu + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cv + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
        if fill:
            self.poli(p, fill, col, w)
        else:
            self.t.linea(self.pts(p), col, w)

    def catena_h(self, valori, y, stati, ref=None, size=2.5):
        """Catena di quote orizzontale all'altezza y (mm sul foglio); ref = y fino a cui scendono le linee di richiamo."""
        t = self.t
        liv = 0
        for i in range(len(valori) - 1):
            a, b = valori[i], valori[i + 1]
            xa, xb = self.x(a), self.x(b)
            c = COL[stati[i]] if i < len(stati) else COL['m']
            t.linea([(xa, y), (xb, y)], c, 0.13)
            s = q(b - a)
            lw = larghezza(s, size)
            if abs(xb - xa) < lw + 0.5:
                liv = (liv + 1) % 2
                dy = 0.7 + liv * (size + 0.2)
            else:
                dy = 0.7
                liv = 0
            t.testo((xa + xb) / 2, y - dy, s, size, c, 'middle')
        for v in valori:
            xx = self.x(v)
            if ref is not None:
                t.linea([(xx, y), (xx, ref)], GRIGIO, 0.07)
            t.linea([(xx - 0.7, y + 0.7), (xx + 0.7, y - 0.7)], '#000000', 0.25)

    def catena_v(self, valori, x, stati, ref=None, size=2.5, testo_dx=False):
        t = self.t
        liv = 0
        for i in range(len(valori) - 1):
            a, b = valori[i], valori[i + 1]
            ya, yb = self.y(a), self.y(b)
            c = COL[stati[i]] if i < len(stati) else COL['m']
            t.linea([(x, ya), (x, yb)], c, 0.13)
            s = q(b - a)
            lw = larghezza(s, size)
            if abs(yb - ya) < lw + 0.5:
                liv = (liv + 1) % 2
                dx = 0.7 + liv * (size + 0.2)
            else:
                dx = 0.7
                liv = 0
            if testo_dx:
                t.testo(x + dx + size * 0.72, (ya + yb) / 2, s, size, c, 'middle', -90)
            else:
                t.testo(x - dx, (ya + yb) / 2, s, size, c, 'middle', -90)
        for v in valori:
            yy = self.y(v)
            if ref is not None:
                t.linea([(x, yy), (ref, yy)], GRIGIO, 0.07)
            t.linea([(x - 0.7, yy + 0.7), (x + 0.7, yy - 0.7)], '#000000', 0.25)


def intestazione(t, titolo, sotto, n):
    t.rett(10, 10, 410, 287, '#ffffff', '#000000', 0.25)
    t.testo(16, 19, titolo, 5, bold=True)
    t.testo(16, 25, sotto, 3)
    t.testo(404, 283, 'Casa ad Arzachena (1962-64), Marco Zanuso. Tavola %d di 7. Ricostruzione dalla scheda dell\'esercizio n. 3.' % n, 2.4, GRIGIO, 'end')


def legenda(t, x, y):
    t.testo(x, y, 'Come leggere le quote (in metri)', 3, bold=True)
    voci = [('q', 'nero: scritta sulla scheda del prof'),
            ('m', 'blu: misurata sul disegno della scheda (margine circa 5-10 cm)'),
            ('h', 'rosso: ipotesi, la scheda non la dice: da chiedere al prof')]
    for i, (k, s) in enumerate(voci):
        t.testo(x, y + 4.5 + i * 4, s, 2.7, COL[k])
    t.testo(x, y + 4.5 + 3 * 4, 'Sul plastico in scala 1:100: moltiplica per 10 e leggi millimetri (1,50 m = 15 mm).', 2.7)


def tabella(t, x, y, colonne, righe, titolo=None, size=2.5):
    if titolo:
        t.testo(x, y, titolo, 3, bold=True)
        y += 4.5
    xx = x
    for nome, lar in colonne:
        t.testo(xx, y, nome, size, bold=True)
        xx += lar
    tot = sum(c[1] for c in colonne)
    t.linea([(x, y + 1), (x + tot - 2, y + 1)], '#000000', 0.15)
    for r, (celle, st) in enumerate(righe):
        yy = y + 4.2 * (r + 1)
        xx = x
        for j, c in enumerate(celle):
            k = st[j] if j < len(st) else 'q'
            t.testo(xx, yy, c, size, COL[k])
            xx += colonne[j][1]
    return y + 4.2 * (len(righe) + 1)


# ---------------------------------------------------------------- geometria

def muri(v):
    """Tutti i muri in pianta, tagliati all'altezza delle finestre."""
    r = [
        # nord
        (0, 0, 2.45, .6), (2.95, 0, 5.8, .6), (9.8, 0, 13, .6), (13.5, 0, 15.6, .6),
        # est
        (15, 0, 15.6, 6.3), (15, 9.3, 15.6, 15.6),
        # sud
        (0, 15, 12.7, 15.6), (13.3, 15, 15.6, 15.6),
        # ovest
        (0, 0, .6, 5.5), (0, 6.1, .6, 9.4), (0, 10, .6, 13), (0, 13.6, .6, 15.6),
        # pilastri dei bracci nord e sud della croce
        (4.6, 0, 5.2, 3.7), (10.4, 0, 11, 3.7), (4.6, 11.9, 5.2, 15.6), (10.4, 11.9, 11, 15.6),
        # muri tra stanze e braccio est/ovest
        (1.85, 4.6, 3.7, 5.2), (11.9, 4.6, 15, 5.2), (.6, 10.4, 3.7, 11), (11.9, 10.4, 15, 11),
        # muro della fascia ovest verso la corte
        (2.8, 5.2, 3.4, 5.45), (2.8, 6.3, 3.4, 7.3), (2.8, 8.3, 3.4, 9.3), (2.8, 10.15, 3.4, 10.4),
        # massa del camino
        (.6, 6.75, 3.4, 8.85),
    ]
    for a in r:
        v.piena(*a)
    b = '#ffffff'
    # nicchia esterna a ovest, camera rotonda, gola e bocca del camino, nicchia del bagno
    v.cerchio(.1765, 7.8, .6735, b, b, .01)
    v.piena(-.03, 7.1, 0, 8.5, b)
    v.cerchio(2.0, 7.8, .8, b, b, .01)
    v.piena(2.65, 7.5, 2.85, 8.1, b)
    v.piena(2.85, 7.3, 3.4, 8.3, b)
    v.cerchio(1.0, 10.4, .4, b, b, .01, 0, 180)


def porte(v):
    for h, chiusa, a0, a1 in [((3.7, 4.6), (4.6, 3.7), -45, -180), ((11, 3.7), (11.9, 4.6), 45, -90),
                              ((4.6, 11.9), (3.7, 11), -135, -270), ((11.9, 11), (11, 11.9), 135, 0)]:
        r = 0.9 * math.sqrt(2)
        ap = (h[0] + r * math.cos(math.radians(a1)), h[1] + r * math.sin(math.radians(a1)))
        v.seg(h, ap, '#000000', .25)
        v.seg(h, chiusa, GRIGIO, .13, (1, .8))
        v.cerchio(h[0], h[1], r, None, GRIGIO, .13, a0, a1)


def profilo_esterno(z):
    """Rientro del filo esterno alla quota z: 0 a terra, 0,23 m in cima al muro."""
    return .23 * (z + .4) / 3.7


# ---------------------------------------------------------------- tavola 1

def tav_pianta():
    t = Tavola('arzachena-v2-1-pianta')
    intestazione(t, 'Pianta quotata, scala 1:100', 'Pianta tagliata all\'altezza delle finestre. Stampa in A3 al 100% e il lato della casa misura 156 mm.', 1)
    v = Vista(t, 10, 62, 72)
    # corte, gradini, pavimentazione e copertura leggera
    v.piena(5.2, .6, 10.4, 15, '#eeeeee')
    v.piena(3.4, 5.2, 15, 10.4, '#eeeeee')
    muri(v)
    porte(v)
    v.rect(5.8, -.6, 9.8, 0, '#000000', .15)
    v.seg((5.8, -.3), (9.8, -.3), '#000000', .1)
    v.seg((5.8, .6), (5.8, 2.6), '#000000', .25)
    v.seg((9.8, .6), (9.8, 2.6), '#000000', .25)
    v.rect(5.5, 5.5, 10.1, 10.1, GRIGIO, .13)
    v.cerchio(7.8, 7.8, .675, '#ffffff', '#000000', .15)
    v.rect(4.3, 5.3, 11.3, 10.3, GRIGIO, .13, (2, 1))
    v.rect(.23, .23, 15.37, 15.37, GRIGIO, .13, (2, 1))
    v.t.testo(v.x(7.8), v.y(2.4), 'corte', 2.6, GRIGIO, 'middle')
    for x_, y_, s in [(2.6, 2.6, 'stanza'), (13, 2.6, 'stanza'), (2.6, 13, 'stanza'), (13, 13, 'stanza')]:
        t.testo(v.x(x_), v.y(y_), s, 2.6, GRIGIO, 'middle')
        t.testo(v.x(x_), v.y(y_) + 3.2, '4,00 × 4,00', 2.5, COL['q'], 'middle')
    t.testo(v.x(1.7), v.y(6.1), 'cucina', 2.3, GRIGIO, 'middle')
    t.testo(v.x(1.7), v.y(9.7), 'bagno', 2.3, GRIGIO, 'middle')
    t.testo(v.x(2.0), v.y(7.9), 'camino', 2.2, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(8.75), 'tavolo', 2.2, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(9.35), 'diam. 1,35', 2.3, COL['m'], 'middle')
    # catene
    ref_n, ref_s = v.y(0), v.y(15.6)
    v.catena_h([0, 2.45, 2.95, 5.8, 9.8, 13, 13.5, 15.6], v.y(-.6) - 5, 'mmmqmmm', ref_n)
    v.catena_h([0, .6, 4.6, 5.2, 5.8, 9.8, 10.4, 11, 15, 15.6], v.y(-.6) - 12, 'qqqqqqqqq')
    v.catena_h([0, 5.2, 10.4, 15.6], v.y(-.6) - 18, 'qqq')
    v.catena_h([0, 15.6], v.y(-.6) - 24, 'q')
    v.catena_h([0, .6, 3.7, 4.6, 5.2, 10.4, 11, 11.9, 15, 15.6], ref_s + 8, 'qmmqqqmmq', ref_s)
    v.catena_h([0, 12.7, 13.3, 15.6], ref_s + 15, 'mmm')
    v.catena_h([0, .6, 4.6, 5.2, 10.4, 11, 15, 15.6], ref_s + 21, 'qqqqqqq')
    v.catena_h([0, 5.2, 10.4, 15.6], ref_s + 27, 'qqq')
    v.catena_h([0, 15.6], ref_s + 33, 'q')
    xl, xr = v.x(0), v.x(15.6)
    v.catena_v([0, 5.5, 6.1, 7.15, 8.45, 9.4, 10, 13, 13.6, 15.6], xl - 9, 'mmmmmmmmm', xl)
    v.catena_v([0, .6, 3.7, 4.6, 5.2, 10.4, 11, 11.9, 15, 15.6], xl - 17, 'qmmqqqmmq')
    v.catena_v([0, 5.2, 10.4, 15.6], xl - 24, 'qqq')
    v.catena_v([0, 15.6], xl - 30, 'q')
    v.catena_v([0, .6, 3.7, 4.6, 5.2, 6.3, 9.3, 10.4, 11, 11.9, 15, 15.6], xr + 9, 'qmmqqqqqmmq', xr)
    v.catena_v([0, .6, 4.6, 5.2, 10.4, 11, 15, 15.6], xr + 16, 'qqqqqqq')
    v.catena_v([0, 5.2, 10.4, 15.6], xr + 22, 'qqq')
    # tracce delle sezioni e nord
    t.linea([(v.x(7.8), v.y(-.6) - 4.3), (v.x(7.8), v.y(-.6) - .3)], '#000000', .4)
    t.linea([(v.x(7.8), v.y(15.6) + .5), (v.x(7.8), v.y(15.6) + 5)], '#000000', .4)
    t.testo(v.x(7.8) + 1.2, v.y(-.6) - 1.2, 'A', 3, bold=True)
    t.testo(v.x(7.8) + 1.2, v.y(15.6) + 4.5, "A'", 3, bold=True)
    t.linea([(xl - 6, v.y(7.8)), (xl - 1, v.y(7.8))], '#000000', .4)
    t.linea([(xr + 1, v.y(7.8)), (xr + 6, v.y(7.8))], '#000000', .4)
    t.testo(xl - 5, v.y(7.8) - 1, "C'", 3, bold=True)
    t.testo(xr + 5.5, v.y(7.8) - 1, 'C', 3, bold=True, anchor='end')
    t.testo(v.x(1.0), v.y(-.25), 'Sezione BB\' = facciata nord', 2.3, GRIGIO)
    nx, ny = 28, 45
    v2 = t
    v2.linea([(nx, ny - 7), (nx - 3, ny + 3), (nx, ny + 1), (nx + 3, ny + 3)], '#000000', .25, None, True, '#000000')
    v2.testo(nx, ny + 7.5, 'N', 3.5, anchor='middle', bold=True)

    # dettaglio di una porta
    d = Vista(t, 40, 292 - 3 * 40, 50 - 3 * 40)
    t.testo(266, 36, 'Dettaglio di una porta (angolo nord-ovest), 1:25', 3.2, bold=True)
    d.piena(3.0, 3.0, 5.8, 5.8, '#ffffff')
    d.piena(5.2, 3.0, 5.8, 5.8, '#eeeeee')
    d.piena(3.0, 5.2, 5.8, 5.8, '#eeeeee')
    d.piena(4.6, 3.0, 5.2, 3.7)
    d.piena(3.0, 4.6, 3.7, 5.2)
    d.seg((3.7, 4.6), (2.43 + .57, 4.6), '#000000', .35)
    d.seg((3.7, 4.6), (4.6, 3.7), '#000000', .3, (1.5, 1))
    d.cerchio(3.7, 4.6, .9 * math.sqrt(2), None, GRIGIO, .13, -45, -152)
    d.poli([(4.6, 3.7), (5.2, 3.7), (5.2, 5.2), (3.7, 5.2), (3.7, 4.6)], None, GRIGIO, .13, (1, 1))
    t.testo(d.x(4.34), d.y(4.3), 'porta 1,27', 2.5, COL['m'], 'middle', -45)
    t.testo(d.x(5.5), d.y(4.3), 'corte', 2.6, GRIGIO, 'middle')
    t.testo(d.x(3.5), d.y(3.5), 'stanza', 2.6, GRIGIO, 'middle')
    d.catena_h([3.7, 4.6, 5.2], d.y(3.0) - 3, 'mq', d.y(4.6))
    d.catena_h([3.7, 5.2], d.y(3.0) - 9, 'm')
    d.catena_v([3.7, 4.6, 5.2], d.x(3.0) - 3, 'mq', d.x(4.6))
    d.catena_v([3.7, 5.2], d.x(3.0) - 9, 'm')
    t.testo(266, 174, 'Ogni muro si ferma a 1,50 m dall\'angolo della croce: 0,90 m', 2.6)
    t.testo(266, 178, 'liberi dentro la stanza + 0,60 m di spessore. La porta è in diagonale', 2.6)
    t.testo(266, 182, 'tra le due punte di muro, larga 1,27 m, anta verso la stanza. Sopra 2,10 m', 2.6)
    t.testo(266, 186, 'il muro continua fino all\'angolo della croce (linea sottile tratteggiata).', 2.6)

    y = tabella(t, 266, 193, [('Porta', 22), ('Il muro est-ovest finisce', 40), ('Il pilastro nord-sud finisce', 40), ('Cardine', 38)], [
        (['NO', 'a X = 3,70', 'a Y = 3,70', 'sulla punta del muro'], 'qmmq'),
        (['NE', 'a X = 11,90', 'a Y = 3,70', 'sulla punta del pilastro'], 'qmmq'),
        (['SO', 'a X = 3,70', 'a Y = 11,90', 'sulla punta del pilastro'], 'qmmq'),
        (['SE', 'a X = 11,90', 'a Y = 11,90', 'sulla punta del muro'], 'qmmq'),
    ], 'Le quattro porte (X da ovest, Y da nord)')
    tabella(t, 266, y + 4, [('Finestra', 30), ('Posizione', 42), ('Larg.', 14), ('Da / a sul pavimento', 44)], [
        (['Nord, stanza NO', 'X da 2,45 a 2,95', '0,50', '1,05 - 1,70'], 'qmmm'),
        (['Nord, stanza NE', 'X da 13,00 a 13,50', '0,50', '1,05 - 1,70'], 'qmmm'),
        (['Sud, stanza SE', 'X da 12,70 a 13,30', '0,60', '1,05 - 1,70'], 'qmmh'),
        (['Ovest, cucina', 'Y da 5,50 a 6,10', '0,60', '1,05 - 1,70'], 'qmmh'),
        (['Ovest, bagno', 'Y da 9,40 a 10,00', '0,60', '1,05 - 1,70'], 'qmmh'),
        (['Ovest, stanza SO', 'Y da 13,00 a 13,60', '0,60', '1,05 - 1,70'], 'qmmh'),
    ], 'Le sei finestre')
    legenda(t, 266, 262)
    t.testo(16, 272, 'Tratteggio esterno: filo del muro in cima (i muri esterni sono inclinati).', 2.4, GRIGIO)
    t.testo(16, 276, 'Tratteggio nella corte: copertura leggera. Linee spesse nel braccio nord: le due ante aperte.', 2.4, GRIGIO)
    t.testo(16, 280, 'Il quadrato sottile nella corte è la pavimentazione (4,60 × 4,60), il cerchio è il tavolo.', 2.4, COL['m'])
    return t


# ---------------------------------------------------------------- tavola 2

def camino_sezione(v):
    """Taglio del camino lungo l'asse: u = X da ovest (la vista ha l'ovest a destra), v = -Z."""
    n = '#000000'
    v.piena(.85, 0, 1.2, -3.3)          # muro di fondo
    v.piena(1.2, -.9, 3.4, -1.2)        # soletta sotto il focolare
    v.piena(1.2, -1.2, 3.12, -3.2)      # massa piena
    v.piena(3.12, -1.46, 3.21, -5.15)   # setto tra le due canne
    v.piena(3.32, -1.46, 3.4, -5.15)    # parete davanti
    v.piena(2.8, -3.2, 2.88, -5.15)     # parete dietro
    v.piena(2.8, -5.04, 3.21, -5.15)    # cappello
    v.piena(-1.2, .4, .85, .95)
    v.piena(.85, 0, 5.0, .95)
    b = '#ffffff'
    v.poli([(3.4, -1.2), (3.4, -1.46), (2.84, -1.46), (2.65, -1.55), (2.43, -1.61), (2.2, -1.6), (1.91, -1.55), (1.7, -1.42), (1.52, -1.2)], b, b, .01)


def tav_camino():
    t = Tavola('arzachena-v2-2-camino-pianta')
    intestazione(t, 'Fascia ovest e camino, scale 1:50 e 1:25', 'Dove stanno cucina, camino e bagno, e tutte le misure del camino in pianta. Cucina e bagno nel dettaglio: tavola 3.', 2)
    # fascia 1:50
    v = Vista(t, 20, 50, 62 - 4.4 * 20)
    t.testo(16, 38, 'Pianta della fascia ovest, 1:50', 3.2, bold=True)
    v.piena(3.4, 4.4, 5.2, 11.2, '#eeeeee')
    v.piena(0, 4.4, .6, 5.5)
    v.piena(0, 6.1, .6, 9.4)
    v.piena(0, 10, .6, 11.2)
    v.piena(1.85, 4.6, 3.7, 5.2)
    v.piena(2.8, 5.2, 3.4, 5.45)
    v.piena(2.8, 6.3, 3.4, 7.3)
    v.piena(2.8, 8.3, 3.4, 9.3)
    v.piena(2.8, 10.15, 3.4, 10.4)
    v.piena(.6, 6.75, 3.4, 8.85)
    v.piena(.6, 10.4, 3.7, 11)
    b = '#ffffff'
    v.cerchio(.1765, 7.8, .6735, b, b, .01)
    v.piena(-.03, 7.1, 0, 8.5, b)
    v.cerchio(2.0, 7.8, .8, b, b, .01)
    v.piena(2.65, 7.5, 2.85, 8.1, b)
    v.piena(2.85, 7.3, 3.4, 8.3, b)
    v.cerchio(1.0, 10.4, .4, b, b, .01, 0, 180)
    t.testo(v.x(1.7), v.y(6.1), 'cucina', 2.6, GRIGIO, 'middle')
    t.testo(v.x(1.7), v.y(9.7), 'bagno', 2.6, GRIGIO, 'middle')
    t.testo(v.x(1.0), v.y(5.0), 'stanza NO', 2.4, GRIGIO, 'middle')
    t.testo(v.x(4.3), v.y(7.8), 'corte', 2.6, GRIGIO, 'middle')
    v.catena_h([0, .6, 1.85, 2.8, 3.4], v.y(4.4) - 4, 'qmmm', v.y(4.6))
    v.catena_h([0, .6, 1.4, 2.8, 3.4], v.y(11.2) + 7, 'qmmm', v.y(11))
    xl, xr = v.x(0), v.x(5.2)
    v.catena_v([4.6, 5.2, 5.5, 6.1, 6.75, 7.15, 8.45, 8.85, 9.4, 10, 10.4, 11], xl - 8, 'qmmmmmmmmmq', xl)
    v.catena_v([5.2, 5.45, 6.3, 7.3, 8.3, 9.3, 10.15, 10.4], xr + 8, 'mmmmmmm', v.x(3.4))
    v.catena_v([5.2, 10.4], xr + 18, 'q')
    t.testo(v.x(1.7), v.y(11.2) + 12, 'Aperture sulla corte: cucina 0,85; camino 1,00; bagno 0,85.', 2.4, anchor='middle')
    t.testo(v.x(1.7), v.y(11.2) + 15.5, 'Altezza di cucina e bagno: 2,10 (ipotesi, come le porte).', 2.4, COL['h'], 'middle')
    t.testo(v.x(1.7), v.y(11.2) + 19, 'Nicchia nel bagno: larga 0,80, profonda 0,40.', 2.4, COL['m'], 'middle')

    # camino in pianta 1:25
    p = Vista(t, 40, 195, 62 - 6.7 * 40)
    t.testo(178, 38, 'Camino in pianta, 1:25', 3.2, bold=True)
    p.piena(0, 6.75, 3.4, 8.85)
    p.piena(3.4, 6.7, 3.65, 8.9, '#eeeeee')
    p.cerchio(.1765, 7.8, .6735, b, b, .01)
    p.piena(-.03, 7.1, 0, 8.5, b)
    p.cerchio(2.0, 7.8, .8, b, b, .01)
    p.piena(2.65, 7.5, 2.85, 8.1, b)
    p.piena(2.85, 7.3, 3.4, 8.3, b)
    p.rect(2.8, 7.5, 3.4, 8.1, '#c62828', .3, (2, 1))
    p.seg((-.2, 7.8), (3.65, 7.8), GRIGIO, .1, (4, 1, 1, 1))
    t.testo(p.x(2.0), p.y(7.75), 'camera rotonda', 2.3, GRIGIO, 'middle')
    t.testo(p.x(2.0), p.y(8.13), 'diam. 1,60', 2.5, COL['m'], 'middle')
    t.testo(p.x(.32), p.y(7.75), 'nicchia', 2.3, GRIGIO, 'middle')
    t.testo(p.x(.32), p.y(8.05), 'esterna', 2.3, GRIGIO, 'middle')
    ytop, ybot = p.y(6.75), p.y(8.85)
    p.catena_h([0, .85, 1.2, 2.8, 2.85, 3.4], ytop - 4, 'mmmmm', ytop)
    p.catena_h([0, 2.0, 3.4], ytop - 11, 'mm')
    p.catena_h([2.8, 3.4], ybot + 6, 'm', ybot)
    t.testo(p.x(3.1), ybot + 10, 'canna fumaria', 2.3, GRIGIO, 'middle')
    xr = p.x(3.65)
    p.catena_v([7.3, 7.5, 8.1, 8.3], xr + 7, 'mmm', p.x(3.4))
    p.catena_v([6.75, 7.3, 7.8, 8.3, 8.85], xr + 15, 'mmmm')
    p.catena_v([7.15, 8.45], p.x(0) - 6, 'm', p.x(0))
    p.catena_v([6.75, 7.0, 8.6, 8.85], p.x(0) - 13, 'mmm', p.x(1.5))
    p.catena_v([6.75, 8.85], p.x(0) - 20, 'm')
    t.testo(178, ybot + 16, 'Rosso tratteggiato: canna fumaria in pianta. La scheda la mostra solo da un lato (0,60); la profondità', 2.4, COL['h'])
    t.testo(178, ybot + 19.5, 'nord-sud 0,60 è un\'ipotesi: canna quadrata, centrata sull\'asse del camino.', 2.4, COL['h'])

    tabella(t, 178, 176, [('Camino: cosa', 86), ('Metri', 42), ('Plastico (mm)', 30)], [
        (['Blocco, dal filo ovest alla corte × nord-sud', '3,40 × 2,10', '34 × 21'], 'qmm'),
        (['Altezza del blocco sul pavimento', '3,20', '32'], 'qmm'),
        (['Muro tra nicchia esterna e camera', '0,35', '3,5'], 'qmm'),
        (['Camera rotonda, diametro (centro a 2,00 dal filo ovest)', '1,60', '16'], 'qmm'),
        (['Nicchia esterna, larga × profonda', '1,30 × 0,85', '13 × 8,5'], 'qmm'),
        (['Bocca verso la corte, larga × profonda', '1,00 × 0,55', '10 × 5,5'], 'qmm'),
        (['Gola tra bocca e camera, larga × lunga', '0,60 × 0,15', '6 × 1,5'], 'qmm'),
        (['Vano sotto il focolare, altezza', '0,90', '9'], 'qmm'),
        (['Soletta del focolare, spessore', '0,30', '3'], 'qmm'),
        (['Bocca del focolare, da / a sul pavimento', '1,20 - 1,46', '12 - 14,6'], 'qmm'),
        (['Canna fumaria, est-ovest × nord-sud', '0,60 × 0,60', '6 × 6'], 'qhh'),
        (['Canna fumaria, altezza sopra il tetto', '1,85', '18,5'], 'qmm'),
    ])
    legenda(t, 178, 244)
    return t


def tav_cucina_bagno():
    t = Tavola('arzachena-v2-3-cucina-bagno')
    intestazione(t, 'Cucina e bagno in pianta, scala 1:25', 'Le misure interne, i muri, le aperture, le finestre e gli arredi leggibili sulla scheda. Nord in alto, ovest a sinistra.', 3)
    b = '#ffffff'
    # cucina
    c = Vista(t, 40, 44, 58 - 4.4 * 40)
    t.testo(16, 36, 'Cucina', 3.4, bold=True)
    c.piena(3.4, 4.4, 3.7, 6.9, '#eeeeee')
    c.piena(0, 4.4, .6, 6.9)
    c.piena(-.02, 5.5, .25, 6.1, b)
    c.piena(.25, 5.45, .6, 6.15, b)
    c.piena(.6, 6.75, 3.4, 6.9)
    c.piena(1.85, 4.6, 3.7, 5.2)
    c.piena(2.8, 5.2, 3.4, 5.45)
    c.piena(2.8, 6.3, 3.4, 6.9)
    c.rect(.6, 6.25, 2.8, 6.75, GRIGIO, .15)
    t.testo(c.x(1.7), c.y(6.54), 'piano della cucina 2,20 × 0,50', 2.5, COL['m'], 'middle')
    t.testo(c.x(1.7), c.y(5.85), 'cucina 2,20 × 1,55', 2.8, COL['m'], 'middle')
    t.testo(c.x(1.2), c.y(4.9), 'stanza NO', 2.5, GRIGIO, 'middle')
    t.testo(c.x(3.55), c.y(5.85), 'corte', 2.2, GRIGIO, 'middle', -90)
    c.catena_h([0, .6, 1.85, 3.7], c.y(4.4) - 4, 'qmm', c.y(4.6))
    c.catena_h([0, .25, .6, 2.8, 3.4], c.y(6.9) + 7, 'mmmm', c.y(6.75))
    xl, xr = c.x(0), c.x(3.7)
    c.catena_v([5.2, 5.45, 5.5, 6.1, 6.15, 6.75], xl - 6, 'mmmmm', xl)
    c.catena_v([5.2, 6.75], xl - 16, 'm')
    c.catena_v([4.6, 5.2, 5.45, 6.3, 6.75], xr + 6, 'qmmm', c.x(3.4))
    # bagno
    v = Vista(t, 40, 244, 58 - 8.6 * 40)
    t.testo(216, 36, 'Bagno', 3.4, bold=True)
    v.piena(3.4, 8.6, 3.7, 11, '#eeeeee')
    v.piena(0, 8.6, .6, 11)
    v.piena(-.02, 9.4, .25, 10, b)
    v.piena(.25, 9.3, .6, 10.1, b)
    v.piena(.6, 8.6, 3.4, 8.85)
    v.piena(2.8, 8.85, 3.4, 9.3)
    v.piena(2.8, 10.15, 3.4, 10.4)
    v.piena(.6, 10.4, 3.7, 11)
    v.cerchio(1.0, 10.4, .4, b, b, .01, 0, 180)
    v.cerchio(1.0, 10.55, .2, None, GRIGIO, .15)
    v.seg((1.4, 8.85), (1.4, 10.4), GRIGIO, .25)
    t.testo(v.x(2.1), v.y(9.65), 'bagno 2,20 × 1,55', 2.8, COL['m'], 'middle')
    t.testo(v.x(3.55), v.y(9.7), 'corte', 2.2, GRIGIO, 'middle', -90)
    v.catena_h([0, .6, 1.4, 2.8, 3.4], v.y(8.6) - 4, 'qmmm', v.y(8.85))
    v.catena_h([0, .25, .6, 1.4, 2.8, 3.7], v.y(11) + 7, 'mmmmm', v.y(11))
    xl, xr = v.x(0), v.x(3.7)
    v.catena_v([8.85, 9.3, 9.4, 10, 10.1, 10.4, 10.8, 11], xl - 6, 'mmmmmmm', xl)
    v.catena_v([8.85, 10.4], xl - 16, 'm')
    v.catena_v([8.85, 9.3, 10.15, 10.4, 11], xr + 6, 'mmmq', v.x(3.4))
    # tabelle
    tabella(t, 16, 170, [('Cucina: cosa', 84), ('Metri', 40), ('Plastico (mm)', 30)], [
        (['Interno, est-ovest × nord-sud', '2,20 × 1,55', '22 × 15,5'], 'qmm'),
        (['Altezza dei muri sul pavimento', '3,30', '33'], 'qmm'),
        (['Passaggio verso la stanza NO, senza muro né porta', '1,25', '12,5'], 'qmm'),
        (['Muro verso la stanza NO, lungo × spesso', '1,85 × 0,60', '18,5 × 6'], 'qmm'),
        (['Muro verso la corte, spessore', '0,60', '6'], 'qmm'),
        (['Apertura sulla corte, larga', '0,85', '8,5'], 'qmm'),
        (['Apertura sulla corte, altezza', '2,10', '21'], 'qhh'),
        (['Muro tra stanza NO e apertura', '0,25', '2,5'], 'qmm'),
        (['Finestra ovest, larga fuori / dentro', '0,60 / 0,70', '6 / 7'], 'qmm'),
        (['Finestra ovest, da / a sul pavimento', '1,05 - 1,70', '10,5 - 17'], 'qhh'),
        (['Piano della cucina, altezza: la scheda non la dà', '-', '-'], 'hqq'),
    ])
    tabella(t, 216, 170, [('Bagno: cosa', 84), ('Metri', 40), ('Plastico (mm)', 30)], [
        (['Interno, est-ovest × nord-sud', '2,20 × 1,55', '22 × 15,5'], 'qmm'),
        (['Altezza dei muri sul pavimento', '3,30', '33'], 'qmm'),
        (['Tramezzo sottile a 0,80 dal muro ovest', '0,80 + 1,40', '8 + 14'], 'qmm'),
        (['Nicchia a sud, larga × profonda', '0,80 × 0,40', '8 × 4'], 'qmm'),
        (['Elemento rotondo nella nicchia, diametro', '0,40', '4'], 'qmm'),
        (['Muro verso il camino: massa del blocco', 'vedi tavola 2', ''], 'qqq'),
        (['Muro verso la stanza SO, spessore', '0,60', '6'], 'qqq'),
        (['Apertura sulla corte, larga', '0,85', '8,5'], 'qmm'),
        (['Apertura sulla corte, altezza', '2,10', '21'], 'qhh'),
        (['Finestra ovest, larga fuori / dentro', '0,60 / 0,80', '6 / 8'], 'qmm'),
        (['Finestra ovest, da / a sul pavimento', '1,05 - 1,70', '10,5 - 17'], 'qhh'),
    ])
    t.testo(216, 233, 'Le linee sottili degli arredi sulla scheda sono sfocate: il tramezzo e il cerchio sono quello', 2.5, GRIGIO)
    t.testo(216, 237, 'che si riesce a leggere. Sul plastico chiuso non si vedono e puoi non farli.', 2.5, GRIGIO)
    legenda(t, 16, 240)
    return t


def tav_camino_sez():
    t = Tavola('arzachena-v2-4-camino-sezione')
    intestazione(t, "Camino in sezione CC', scala 1:30", 'Taglio lungo l\'asse della casa, guardando verso sud (ovest a destra). Quote in metri, pavimento = 0,00.', 4)
    s = Vista(t, 100 / 3, 290, 228, -1, 1)
    camino_sezione(s)
    s.seg((.23, -3.3), (0, .4), '#000000', .15)
    s.seg((.23, -3.3), (.85, -3.3), '#000000', .15)
    s.seg((3.4, 0), (3.4, -.9), '#000000', .15)
    s.seg((3.4, -3.3), (5.0, -3.3), GRIGIO, .1)
    t.testo(s.x(2.3), s.y(-.45), 'vano sotto il focolare', 2.6, GRIGIO, 'middle')
    t.testo(s.x(2.15), s.y(-1.33), 'focolare', 2.3, GRIGIO, 'middle')
    t.testo(s.x(.45), s.y(-1.5), 'nicchia esterna', 2.3, GRIGIO, 'middle', -90)
    t.testo(s.x(4.2), s.y(-1.0), 'corte', 2.6, GRIGIO, 'middle')
    yb = s.y(.95) + 6
    s.catena_h([0, .85, 1.2, 3.4], yb, 'mmm', s.y(0))
    s.catena_h([1.52, 2.8, 3.4], yb + 7, 'mm')
    ytt = s.y(-5.15) - 7
    s.catena_h([2.8, 2.88, 3.12, 3.21, 3.32, 3.4], ytt, 'mmmmm', s.y(-5.15))
    s.catena_v([-5.15, -3.3, -3.2, -1.62, -1.46, -1.2, -.9, 0, .4], s.x(-.3) + 8, 'mmmmmmmm', s.x(.85))
    s.catena_v([-5.15, .4], s.x(-.3) + 18, 'm')
    s.catena_v([-5.15, -5.04, -3.2], s.x(5.0) - 6, 'mm', s.x(2.8))
    s.catena_v([-3.3, 0], s.x(5.0) - 14, 'm', s.x(3.4))
    s.catena_v([-5.15, 0], s.x(5.0) - 22, 'm')
    t.testo(16, 45, 'Il camino, da sotto in su', 3, bold=True)
    tabella(t, 16, 51, [('Parte', 44), ('Quota', 22), ('X da ovest', 22)], [
        (['Vano sotto', '0,00 - 0,90', '1,20 - 3,40'], 'qmm'),
        (['Soletta', '0,90 - 1,20', '0,85 - 3,40'], 'qmm'),
        (['Bocca del focolare', '1,20 - 1,46', '2,80 - 3,40'], 'qmm'),
        (['Cupola del focolare', '1,20 - 1,62', '1,52 - 2,80'], 'qmm'),
        (['Massa piena', 'fino a 3,20', '1,20 - 3,12'], 'qmm'),
        (['Muro di fondo', 'fino a 3,30', '0,85 - 1,20'], 'qmm'),
        (['Canna fumaria', '3,30 - 5,15', '2,80 - 3,40'], 'qmm'),
    ])
    for i, r in enumerate(['Le due canne, dalla corte verso ovest: parete 0,08,', 'canna aperta in cima 0,11 (scende fino al focolare),',
                           'setto 0,09, vuoto chiuso 0,24, parete 0,08;', 'cappello alto 0,11 sopra setto e vuoto.']):
        t.testo(16, 100 + i * 4, r, 2.6)
    for i, r in enumerate(['La canna è alta 1,85 sopra il tetto: 1,80 in questa', 'sezione, 1,92 nella facciata BB\'. Ho preso la media.',
                           'Sul plastico 18-19 mm vanno bene.']):
        t.testo(16, 122 + i * 4, r, 2.6, COL['m'])
    for i, r in enumerate(['Le canne e la cupola stanno dentro il blocco:', 'sul plastico chiuso non si vedono. Da fuori si vedono', 'il blocco, la canna e la bocca verso la corte.']):
        t.testo(16, 140 + i * 4, r, 2.6)
    legenda(t, 16, 250)
    return t


# ---------------------------------------------------------------- tavole 4-6

def tav_aa():
    t = Tavola('arzachena-v2-5-sezione-aa')
    intestazione(t, "Sezione AA', scala 1:50", 'Taglio nord-sud lungo l\'asse della casa, guardando verso est (nord a sinistra). Quote in metri, pavimento = 0,00.', 5)
    v = Vista(t, 20, 54, 118)
    n = '#000000'
    # terreno e pavimento
    v.piena(-1.2, .4, 16.8, 1.0)
    v.piena(0, 0, 15.6, .4)
    v.piena(-.6, .2, 0, .4)
    # muro nord sopra l'architrave, muro sud pieno
    pts = [(profilo_esterno(2.45), -2.45), (.6, -2.45), (.6, -3.3), (profilo_esterno(3.3), -3.3)]
    v.poli(pts, n, n)
    v.poli([(15.6 - profilo_esterno(-.4), .4), (15, .4), (15, -3.3), (15.6 - profilo_esterno(3.3), -3.3)], n, n)
    # architrave nord e profilo oltre il taglio
    v.rect(profilo_esterno(2.0), -2.45, .6, -2.0, n, .2)
    v.seg((0, 0), (profilo_esterno(2.0), -2.0), n, .13)
    v.seg((.6, 0), (.6, -2.0), n, .13)
    # visto oltre: tetto, spigoli della croce, porte, finestra est
    v.seg((.6, -3.3), (15, -3.3), n, .13)
    v.seg((5.2, 0), (5.2, -3.3), n, .13)
    v.seg((10.4, 0), (10.4, -3.3), n, .13)
    for a, b in [(3.7, 5.2), (10.4, 11.9)]:
        v.rect(a, 0, b, -2.1, n, .15)
    v.rect(4.0, 0, 4.65, -2.0, GRIGIO, .1)
    v.rect(10.95, 0, 11.6, -2.0, GRIGIO, .1)
    v.rect(6.3, -1, 9.3, -2, n, .15)
    v.rect(5.6, -2, 10, -2.45, n, .15)
    # copertura leggera
    v.rect(5.3, -3.07, 10.3, -3.25, n, .13)
    for c in (5.75, 7.8, 9.85):
        v.piena(c - .075, -3.07, c + .075, -2.93)
    v.rect(4.22, -2.8, 11.38, -2.93, n, .13)
    for c in (4.75, 10.85):
        v.rect(c - .1, -2.62, c + .1, -2.8, n, .13)
    t.testo(v.x(4.45), v.y(-2.2), 'porta NE', 2.4, GRIGIO, 'middle')
    t.testo(v.x(11.15), v.y(-2.2), 'porta SE', 2.4, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(-1.5), 'finestra est', 2.5, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(-2.18), 'architrave', 2.4, GRIGIO, 'middle')
    t.testo(v.x(.32), v.y(-1.0), 'apertura', 2.2, GRIGIO, 'middle', -90)
    t.testo(v.x(-.3), v.y(.75) + 7, 'gradino', 2.3, GRIGIO, 'middle')
    # catene sotto
    yb = v.y(1.0) + 8
    v.catena_h([-.6, 0, .6, 3.7, 5.2, 6.3, 9.3, 10.4, 11.9, 15, 15.6], yb, 'mqmmqqqmmq', v.y(.4))
    v.catena_h([0, 5.2, 10.4, 15.6], yb + 7, 'qqq')
    v.catena_h([0, 15.6], yb + 13, 'q')
    # catene sopra
    yt = v.y(-3.3) - 5
    v.catena_h([.23, .6, 15, 15.37], yt, 'mqm', v.y(-3.3))
    v.catena_h([4.22, 5.3, 5.6, 10, 10.3, 11.38], yt - 8, 'mmmmm')
    # catene in altezza
    xl = v.x(-1.2) - 3
    v.catena_v([-3.3, -2.45, -2, 0, .2, .4], xl, 'mmmmm', v.x(.0))
    xr = v.x(16.8) + 3
    v.catena_v([-3.3, -2.45, -2, -1, 0, .4], xr, 'mmmmm', v.x(10))
    v.catena_v([-3.3, -2.1, 0], xr + 8, 'mm', v.x(11.9))
    v.catena_v([-3.3, .4], xr + 15, 'm')
    # dettaglio copertura 1:25 (metà nord)
    t.testo(16, 176, 'Dettaglio della copertura leggera, 1:25 (lato nord, il lato sud è uguale e simmetrico rispetto a Y = 7,80)', 3, bold=True)
    o = 3.9
    dd = Vista(t, 40, 54 - o * 40, 188 + 3.3 * 40)
    dd.rect(5.3, -3.07, 8.1, -3.25, n, .15)
    for c in (5.75, 7.8):
        dd.piena(c - .075, -3.07, c + .075, -2.93)
    dd.rect(4.22, -2.8, 8.1, -2.93, n, .15)
    dd.rect(4.65, -2.62, 4.85, -2.8, n, .15)
    dd.seg((3.9, -3.3), (5.2, -3.3), n, .13)
    dd.seg((5.2, -2.5), (5.2, -3.3), n, .13)
    # quota del tetto e catene
    dd.catena_v([-3.3, -3.25, -3.07, -2.93, -2.8, -2.62], 40, 'mmmmm', dd.x(4.22))
    dd.catena_h([4.22, 4.65, 4.85, 5.3, 5.675, 5.825, 7.725, 7.875], dd.y(-2.62) + 6, 'mmmmmmm', dd.y(-2.8))
    t.testo(240, 200, 'Dall\'alto in basso: telo di canne (spessore 0,18), travi est-ovest', 2.7)
    t.testo(240, 204, 'nere (0,15 × 0,14, passo 2,05), travi nord-sud (spessore 0,13),', 2.7)
    t.testo(240, 208, 'mensole sotto le travi nord-sud (0,20 × 0,18).', 2.7)
    t.testo(240, 214, 'In pianta il telo è 7,00 (est-ovest) × 5,00 (nord-sud).', 2.7, COL['m'])
    t.testo(240, 218, 'Le travi nord-sud sono lunghe 7,15; distano 4,90 (X = 5,35 e 10,25).', 2.7, COL['m'])
    t.testo(240, 224, 'Queste quote possono variare di 5-7 cm: AA\' e CC\' non coincidono', 2.7, GRIGIO)
    t.testo(240, 228, 'perfettamente. Sul plastico basta un cartoncino a quota 3,10.', 2.7, GRIGIO)
    legenda(t, 16, 258)
    t.testo(240, 258, 'Spessore del tetto delle stanze: la scheda non lo mostra.', 2.7, COL['h'])
    t.testo(240, 262, 'Sul plastico usa lo spessore del materiale, a filo del muro in cima.', 2.7, COL['h'])
    t.testo(240, 268, 'Il terreno sotto la linea di taglio è solo grafico, non è una misura.', 2.7, GRIGIO)
    return t


def tav_cc():
    t = Tavola('arzachena-v2-6-sezione-cc')
    intestazione(t, "Sezione CC', scala 1:50", 'Taglio est-ovest lungo l\'asse della casa, guardando verso sud (est a sinistra, ovest a destra). Quote in metri, pavimento = 0,00.', 6)
    v = Vista(t, 20, 372, 170, -1, 1)
    n = '#000000'
    camino_sezione(v)
    v.piena(-1.2, .4, 15.6 + 1.2, 1.0)
    v.piena(.85, 0, 15.6, .4)
    # muro est con la finestra
    v.poli([(15.6, 0.4), (15, .4), (15, -1), (15.6 - profilo_esterno(1), -1)], n, n)
    v.poli([(15.6 - profilo_esterno(2.0), -2.0), (15, -2.0), (15, -3.3), (15.6 - profilo_esterno(3.3), -3.3)], n, n)
    v.seg((15.6 - profilo_esterno(1), -1), (15.6 - profilo_esterno(2), -2), n, .13)
    v.seg((15, -1), (15, -2), n, .13)
    # ovest oltre il taglio
    v.seg((0, .4), (.23, -3.3), n, .13)
    v.seg((.23, -3.3), (.85, -3.3), n, .13)
    # oltre il taglio: tetto, spigoli, porte
    v.seg((3.4, -3.3), (15, -3.3), n, .13)
    v.seg((3.4, 0), (3.4, -.9), n, .13)
    v.seg((5.2, 0), (5.2, -3.3), n, .13)
    v.seg((10.4, 0), (10.4, -3.3), n, .13)
    for a, b in [(3.7, 5.2), (10.4, 11.9)]:
        v.rect(a, 0, b, -2.1, n, .15)
    v.rect(4.0, 0, 4.65, -2.0, GRIGIO, .1)
    v.rect(10.95, 0, 11.6, -2.0, GRIGIO, .1)
    # copertura
    v.rect(4.3, -3.07, 11.3, -3.25, n, .13)
    for c in (5.35, 10.25):
        v.piena(c - .08, -2.8, c + .08, -2.93)
        v.rect(c - .1, -2.62, c + .1, -2.8, n, .1)
    t.testo(v.x(11.15), v.y(-2.2), 'porta SE', 2.4, GRIGIO, 'middle')
    t.testo(v.x(4.45), v.y(-2.2), 'porta SO', 2.4, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(-1.5), 'muro sud (pieno)', 2.5, GRIGIO, 'middle')
    t.testo(v.x(15.3), v.y(-1.5), 'finestra', 2.2, GRIGIO, 'middle', -90)
    t.testo(v.x(2.1), v.y(-.45), 'vano sotto', 2.2, GRIGIO, 'middle')
    t.testo(v.x(2.1), v.y(-1.28), 'focolare', 1.9, GRIGIO, 'middle')
    # catene sotto: i valori sono X, l'est sta a sinistra
    yb = v.y(1.0) + 8
    v.catena_h([0, .85, 1.2, 3.4, 3.7, 5.2, 10.4, 11.9, 15, 15.6], yb, 'mmmmmqmmq', v.y(.4))
    v.catena_h([0, 5.2, 10.4, 15.6], yb + 7, 'qqq')
    v.catena_h([0, 15.6], yb + 13, 'q')
    yt = v.y(-3.3) - 5
    v.catena_h([4.3, 5.2, 10.4, 11.3], v.y(-3.25) - 3.5, 'mqm', v.y(-3.25))
    v.catena_h([.23, .85, 2.8, 3.4, 15, 15.37], v.y(-5.15) - 5, 'mmmmm', v.y(-5.15))
    xl = v.x(16.8) - 3
    v.catena_v([-3.3, -2, -1, 0, .4], xl, 'mmmm', v.x(15.6))
    v.catena_v([-3.3, -2.1, 0], xl - 8, 'mm', v.x(11.9))
    xr = v.x(-1.2) + 3
    v.catena_v([-5.15, -3.3, 0, .4], xr, 'mmm', v.x(.23))
    v.catena_v([-5.15, .4], xr + 8, 'm')
    t.testo(16, 232, 'Il camino è disegnato con tutte le sue misure nella tavola 4.', 2.7)
    t.testo(16, 238, 'Il muro esterno è inclinato: 0,60 a terra, 0,37 in cima. Sul plastico puoi farlo', 2.7)
    t.testo(16, 242, 'dritto (5-6 mm) e tenere l\'altezza totale di 37 mm dal terreno.', 2.7)
    legenda(t, 16, 256)
    return t


def tav_bb():
    t = Tavola('arzachena-v2-7-sezione-bb')
    intestazione(t, "Sezione BB' (facciata nord), scala 1:50", 'Vista da fuori, guardando verso sud (est a sinistra, ovest a destra). Quote in metri, terreno = -0,40, pavimento = 0,00.', 7)
    v = Vista(t, 20, 372, 190, -1, 1)
    n = '#000000'
    v.seg((-1.2, .4), (16.8, .4), n, .3)
    v.t.linea(v.pts([(0, .4), (.23, -3.3), (15.37, -3.3), (15.6, .4)]), n, .25)
    v.rect(5.8, -2, 9.8, .4, n, .2)
    v.seg((7.8, -2), (7.8, 0), n, .15)
    v.seg((5.8, 0), (9.8, 0), n, .15)
    v.seg((5.8, .2), (9.8, .2), n, .15)
    v.rect(4.95, -2.45, 10.65, -2, n, .2)
    v.rect(2.45, -1.05, 2.95, -1.7, n, .2)
    v.rect(13, -1.05, 13.5, -1.7, n, .2)
    v.rect(2.8, -3.3, 3.4, -5.15, n, .2)
    t.testo(v.x(6.8), v.y(-1), 'anta', 2.5, GRIGIO, 'middle')
    t.testo(v.x(8.8), v.y(-1), 'anta', 2.5, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(-2.18), 'architrave', 2.5, GRIGIO, 'middle')
    t.testo(v.x(3.1), v.y(-5.15) - 6, 'canna fumaria', 2.5, GRIGIO, 'middle')
    yb = v.y(.4) + 8
    v.catena_h([0, 2.45, 2.95, 5.8, 9.8, 13, 13.5, 15.6], yb, 'mmmqmmm', v.y(.4))
    v.catena_h([0, 2.8, 3.4, 4.95, 10.65, 15.6], yb + 7, 'mmmmm')
    v.catena_h([0, 15.6], yb + 13, 'q')
    yt = v.y(-5.15) - 12
    v.catena_h([.23, 2.8, 3.4, 15.37], yt, 'mmm', v.y(-3.3))
    v.catena_h([.23, 15.37], yt - 7, 'm')
    xl = v.x(16.8) - 3
    v.catena_v([-3.3, -2.45, -2, 0, .2, .4], xl, 'mmmmm', v.x(9.8))
    v.catena_v([-3.3, .4], xl - 8, 'm')
    xr = v.x(-1.2) + 3
    v.catena_v([-5.15, -3.3, -1.7, -1.05, 0, .4], xr, 'mmmmm', v.x(2.45))
    v.catena_v([-5.15, .4], xr + 8, 'm')
    t.testo(16, 240, 'L\'apertura nord è larga 4,00 e ha due ante da 2,00, alte fino a 2,00 sul pavimento.', 2.8)
    t.testo(16, 245, 'Due gradini (0,20 ciascuno) portano dal terreno al pavimento; il gradino basso è profondo 0,60.', 2.8)
    t.testo(16, 250, 'L\'architrave di 5,70 sporge 0,85 per parte oltre l\'apertura.', 2.8)
    legenda(t, 16, 258)
    return t


if __name__ == '__main__':
    cartella, pdf = sys.argv[1], sys.argv[2]
    tavole = [tav_pianta(), tav_camino(), tav_cucina_bagno(), tav_camino_sez(), tav_aa(), tav_cc(), tav_bb()]
    for t in tavole:
        t.svg(os.path.join(cartella, t.nome + '.svg'))
    scrivi_pdf(tavole, pdf)
    print('ok', len(tavole))
