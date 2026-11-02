#!/usr/bin/env python3
"""Nuova disposizione della casa ad Arzachena (esercizio 3, punto 5): pianta quotata.

Uso: python3 -I composizione-arzachena-progetto.py CARTELLA_IMMAGINI PERCORSO_PDF
Riusa le primitive di composizione-arzachena.py. Coordinate: X da ovest a est,
Y da nord a sud (metri). Colore delle quote: q = misura della casa vera,
m = posizione presa dallo schizzo di Nadia, h = scelta di Claude (non e' nello schizzo).
"""
import importlib.util
import math
import os
import sys

_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'composizione-arzachena.py')
_s = importlib.util.spec_from_file_location('arzachena', _p)
A = importlib.util.module_from_spec(_s)
_s.loader.exec_module(A)
Tavola, Vista, COL, GRIGIO, tabella, scrivi_pdf = A.Tavola, A.Vista, A.COL, A.GRIGIO, A.tabella, A.scrivi_pdf
VUOTO = '#eeeeee'
B = '#ffffff'


def intestazione(t, titolo, sotto, n):
    t.rett(10, 10, 410, 287, B, '#000000', 0.25)
    t.testo(16, 19, titolo, 5, bold=True)
    t.testo(16, 25, sotto, 3)
    t.testo(404, 283, 'Nuova disposizione della casa ad Arzachena di Marco Zanuso. Tavola %d di 2. Esercizio n. 3, punto 5.' % n, 2.4, GRIGIO, 'end')


def legenda(t, x, y):
    t.testo(x, y, 'Come leggere le quote (in metri)', 3, bold=True)
    for i, (k, s) in enumerate([('q', 'nero: misura della casa vera'), ('m', 'blu: posizione presa dal tuo schizzo'),
                                ('h', 'rosso: scelta mia, nello schizzo non c\'è: puoi cambiarla')]):
        t.testo(x, y + 4.5 + i * 4, s, 2.7, COL[k])
    t.testo(x, y + 16.5, 'Sul plastico in scala 1:100: moltiplica per 10 e leggi millimetri (1,50 m = 15 mm).', 2.7)


def vuoto(v):
    for r in [(.6, 3.4, 5.2, 10.4), (2.75, 2.75, 5.2, 3.4), (5.2, 5.2, 10.4, 15), (10.4, 10.4, 15, 15)]:
        v.piena(*r, VUOTO)
    v.poli([(8.9, 5.2), (10.4, 3.7), (11.9, 5.2), (10.4, 6.7)], VUOTO, VUOTO, .01)
    v.poli([(3.7, 10.4), (5.2, 10.4), (5.2, 11.9)], VUOTO, VUOTO, .01)


def muri(v):
    for r in [
        # perimetro: nord, est, sud, ovest
        (0, 0, 1.1, .6), (1.7, 0, 3.55, .6), (4.15, 0, 7.55, .6), (8.05, 0, 13, .6), (13.5, 0, 15.6, .6),
        (15, 0, 15.6, 7.55), (15, 8.05, 15.6, 15.6),
        (0, 15, 5.8, 15.6), (9.8, 15, 15.6, 15.6),
        (0, 0, .6, 13), (0, 13.6, .6, 15.6),
        # bagno e cucina
        (2.15, .6, 2.75, 3.4), (.6, 2.8, .95, 3.4), (1.8, 2.8, 2.15, 3.4),
        (2.75, 2.15, 3.425, 2.75), (4.275, 2.15, 5.2, 2.75),
        (4.95, .6, 5.2, .9), (4.95, 1.9, 5.2, 2.15),
        # stanza in alto al centro
        (5.2, 0, 5.8, .9), (5.2, 1.9, 5.8, 5.2), (5.2, 4.6, 8.9, 5.2), (9.8, 0, 10.4, 3.7),
        # stanza in alto a destra
        (10.4, 0, 11, 3.7), (11.9, 4.6, 15, 5.2),
        # stanza sul lato est
        (11.9, 5.2, 15, 5.8), (10.4, 6.7, 11, 10.4), (10.4, 9.8, 15, 10.4),
        # stanza in basso a sinistra
        (.6, 10.4, 3.7, 11), (4.6, 11.9, 5.2, 15),
        # blocco del camino
        (12.8, 12.9, 15, 15),
    ]:
        v.piena(*r)
    v.cerchio(14.2, 13.95, .8, B, B, .01)
    v.piena(13.3, 13.65, 13.5, 14.25, B)
    v.piena(12.8, 13.45, 13.35, 14.45, B)


def porte(v):
    r = .9 * math.sqrt(2)
    for h, ch, a0, a1 in [((9.8, 3.7), (8.9, 4.6), 135, 270), ((11, 3.7), (11.9, 4.6), 45, -90),
                          ((11.9, 5.8), (11, 6.7), 135, 0), ((4.6, 11.9), (3.7, 11), -135, -270)]:
        ap = (h[0] + r * math.cos(math.radians(a1)), h[1] + r * math.sin(math.radians(a1)))
        v.seg(h, ap, '#000000', .25)
        v.seg(h, ch, GRIGIO, .13, (1, .8))
        v.cerchio(h[0], h[1], r, None, GRIGIO, .13, a0, a1)


def tav_pianta():
    t = Tavola('arzachena-progetto-v2-1-pianta')
    intestazione(t, 'Nuova disposizione: pianta quotata, scala 1:100', 'Stessi ambienti e stesso perimetro della casa di Zanuso. Stampa in A3 al 100% e il lato della casa misura 156 mm.', 1)
    v = Vista(t, 10, 62, 66)
    vuoto(v)
    muri(v)
    porte(v)
    v.cerchio(7.8, 7.8, .675, B, '#000000', .15)
    v.rect(5.8, 15.6, 9.8, 16.2, '#000000', .15)
    v.seg((5.8, 15.9), (9.8, 15.9), '#000000', .1)
    v.seg((5.8, 13), (5.8, 15), '#000000', .25)
    v.seg((9.8, 13), (9.8, 15), '#000000', .25)
    v.rect(12.8, 13.65, 13.4, 14.25, '#c62828', .25, (1, .6))
    v.rect(.23, .23, 15.37, 15.37, GRIGIO, .13, (2, 1))
    for x_, y_ in [(7.8, 2.6), (13, 2.6), (13, 7.8), (2.6, 13)]:
        t.testo(v.x(x_), v.y(y_), 'stanza', 2.6, GRIGIO, 'middle')
        t.testo(v.x(x_), v.y(y_) + 3.2, '4,00 × 4,00', 2.5, COL['q'], 'middle')
    t.testo(v.x(1.375), v.y(1.6), 'bagno', 2.3, GRIGIO, 'middle')
    t.testo(v.x(3.85), v.y(1.3), 'cucina', 2.3, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(8.75), 'tavolo', 2.2, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(9.3), 'diam. 1,35', 2.3, COL['q'], 'middle')
    t.testo(v.x(10.4), v.y(5.32), 'ingresso', 1.9, GRIGIO, 'middle')
    t.testo(v.x(10.4), v.y(5.32) + 2.2, 'comune', 1.9, GRIGIO, 'middle')
    t.testo(v.x(3), v.y(7.2), 'vuoto scoperto', 2.6, GRIGIO, 'middle')
    t.testo(v.x(13.9), v.y(12.65), 'camino', 2.3, GRIGIO, 'middle')
    t.testo(v.x(7.8), v.y(16.2) + 3.2, 'ingresso', 2.3, GRIGIO, 'middle')
    ref_n, ref_s = v.y(0), v.y(15.6)
    # catene: nord
    v.catena_h([0, 1.1, 1.7, 3.55, 4.15, 7.55, 8.05, 13, 13.5, 15.6], ref_n - 5, 'hhhhhhhqq', ref_n)
    v.catena_h([0, .6, 5.2, 5.8, 9.8, 10.4, 11, 15, 15.6], ref_n - 12, 'qmqqqqqq')
    v.catena_h([0, 5.2, 10.4, 15.6], ref_n - 18, 'qqq')
    v.catena_h([0, 15.6], ref_n - 24, 'q')
    # sud
    y0 = v.y(16.2) + 8
    v.catena_h([0, .6, 3.7, 4.6, 5.2, 5.8, 9.8, 10.4, 12.8, 15, 15.6], y0, 'qqqqqqqhqq', ref_s)
    v.catena_h([0, 5.2, 10.4, 15.6], y0 + 7, 'qqq')
    v.catena_h([0, 15.6], y0 + 13, 'q')
    # ovest
    xl, xr = v.x(0), v.x(15.6)
    v.catena_v([0, .6, 2.8, 3.4, 5.2, 10.4, 11, 11.9, 13, 13.6, 15, 15.6], xl - 7, 'qqmmqqqqqqq', xl)
    v.catena_v([0, 5.2, 10.4, 15.6], xl - 16, 'qqq')
    v.catena_v([0, 15.6], xl - 23, 'q')
    # est
    v.catena_v([0, .6, 3.7, 4.6, 5.2, 5.8, 6.7, 7.55, 8.05, 9.8, 10.4, 12.9, 15, 15.6], xr + 8, 'qqqqqqhhhqhqq', xr)
    v.catena_v([0, 5.2, 10.4, 15.6], xr + 18, 'qqq')
    t.linea([(44, 48), (41, 58), (44, 56), (47, 58)], '#000000', .25, None, True, '#000000')
    t.testo(44, 63.5, 'N', 3.5, anchor='middle', bold=True)

    # tabelle a destra
    y = tabella(t, 266, 40, [('Porta', 44), ('Muro che si interrompe', 34), ('Altro muro', 30), ('Larghezza', 22)], [
        (['In alto al centro', 'sud a X = 8,90', 'est a Y = 3,70', '1,27'], 'qqqq'),
        (['In alto a destra', 'sud a X = 11,90', 'ovest a Y = 3,70', '1,27'], 'qqqq'),
        (['Sul lato est', 'nord a X = 11,90', 'ovest a Y = 6,70', '1,27'], 'qqqq'),
        (['In basso a sinistra', 'nord a X = 3,70', 'est a Y = 11,90', '1,27'], 'qqqq'),
    ], 'Le quattro porte delle stanze (X da ovest, Y da nord)')
    y = tabella(t, 266, y + 6, [('Finestra', 44), ('Posizione', 42), ('Larg.', 14), ('Da / a sul pav.', 24)], [
        (['Bagno, muro nord', 'X da 1,10 a 1,70', '0,60', '1,05 - 1,70'], 'qhqq'),
        (['Cucina, muro nord', 'X da 3,55 a 4,15', '0,60', '1,05 - 1,70'], 'qhqq'),
        (['Stanza in alto al centro, nord', 'X da 7,55 a 8,05', '0,50', '1,05 - 1,70'], 'qhqq'),
        (['Stanza in alto a destra, nord', 'X da 13,00 a 13,50', '0,50', '1,05 - 1,70'], 'qqqq'),
        (['Stanza sul lato est, est', 'Y da 7,55 a 8,05', '0,50', '1,05 - 1,70'], 'qhqq'),
        (['Stanza in basso a sin., ovest', 'Y da 13,00 a 13,60', '0,60', '1,05 - 1,70'], 'qqqq'),
    ], 'Le sei finestre')
    y = tabella(t, 266, y + 6, [('Altezze', 74), ('Metri', 24), ('Plastico (mm)', 26)], [
        (['Muri, sul pavimento', '3,30', '33'], 'qqq'),
        (['Rialzo della casa sul terreno', '0,40', '4'], 'qqq'),
        (['Porte delle stanze', '2,10', '21'], 'qqq'),
        (['Ingresso a sud, larghezza × altezza', '4,00 × 2,00', '40 × 20'], 'qqq'),
        (['Architrave dell\'ingresso, lungo × alto', '5,70 × 0,45', '57 × 4,5'], 'qqq'),
        (['Due gradini fuori dall\'ingresso, alti e profondi', '0,20 e 0,30', '2 e 3'], 'qhh'),
    ], 'Altezze e ingresso')
    legenda(t, 266, y + 8)
    t.testo(16, 270, 'Tratteggio esterno: filo del muro in cima (i muri esterni sono inclinati). Grigio: vuoto scoperto. Tratteggio rosso sul camino: canna fumaria.', 2.4, GRIGIO)
    t.testo(16, 274, 'I muri tra stanze vicine sono doppi (0,60 + 0,60 = 1,20), perché ogni stanza tiene i suoi muri come nella griglia di Zanuso.', 2.4, GRIGIO)
    return t


def tav_dettagli():
    t = Tavola('arzachena-progetto-v2-2-dettagli')
    intestazione(t, 'Nuova disposizione: i dettagli', 'Ingresso comune delle tre stanze 1:25, bagno e cucina 1:50, camino 1:50.', 2)
    # rombo 1:25
    t.testo(16, 36, 'Ingresso comune delle tre stanze, 1:25', 3.2, bold=True)
    r = Vista(t, 40, 30 - 8.2 * 40, 52 - 3.2 * 40)
    r.poli([(8.2, 5.2), (8.9, 5.2), (10.4, 6.7), (10.4, 7.2), (8.2, 7.2)], VUOTO, VUOTO, .01)
    r.poli([(8.9, 5.2), (10.4, 3.7), (11.9, 5.2), (10.4, 6.7)], VUOTO, VUOTO, .01)
    r.piena(8.2, 4.6, 8.9, 5.2)
    r.piena(9.8, 3.2, 10.4, 3.7)
    r.piena(10.4, 3.2, 11, 3.7)
    r.piena(11.9, 4.6, 12.6, 5.2)
    r.piena(11.9, 5.2, 12.6, 5.8)
    r.piena(10.4, 6.7, 11, 7.2)
    for a, b in [((9.8, 3.7), (8.9, 4.6)), ((11, 3.7), (11.9, 4.6)), ((11.9, 5.8), (11, 6.7))]:
        r.seg(a, b, '#000000', .3, (1.5, 1))
    r.t.linea(r.pts([(8.9, 5.2), (10.4, 3.7), (11.9, 5.2), (10.4, 6.7)]), GRIGIO, .13, (1, 1), True)
    t.testo(r.x(10.4), r.y(5.25), 'ingresso comune', 2.5, GRIGIO, 'middle')
    t.testo(r.x(9.1), r.y(6.6), 'vuoto', 2.6, GRIGIO, 'middle')
    t.testo(r.x(8.75), r.y(3.45), 'stanza alto centro', 2.3, GRIGIO, 'middle')
    t.testo(r.x(12.05), r.y(3.45), 'stanza alto destra', 2.3, GRIGIO, 'middle')
    t.testo(r.x(12.05), r.y(7.0), 'stanza lato est', 2.3, GRIGIO, 'middle')
    t.testo(r.x(9.2), r.y(4.0), 'porta 1,27', 2.3, COL['q'], 'middle', -45)
    t.testo(r.x(11.6), r.y(4.0), 'porta 1,27', 2.3, COL['q'], 'middle', 45)
    t.testo(r.x(11.6), r.y(6.6), 'porta 1,27', 2.3, COL['q'], 'middle', -45)
    r.catena_h([8.9, 9.8, 10.4, 11, 11.9], r.y(3.2) - 4, 'qqqq', r.y(3.7))
    r.catena_h([8.9, 10.4, 11.9], r.y(3.2) - 11, 'qq')
    r.catena_v([3.7, 4.6, 5.2, 5.8, 6.7], r.x(12.6) + 5, 'qqqq', r.x(11.9))
    r.catena_v([3.7, 5.2, 6.7], r.x(12.6) + 12, 'qq')
    for i, s in enumerate(['Ogni muro si ferma a 1,50 m dall\'angolo in cui si incontrano le tre stanze,',
                           'come nella casa vera. L\'angolo sta a X = 10,40 e Y = 5,20: sul plastico a 104 mm',
                           'dal bordo ovest e 52 mm dal bordo nord. Le porte sono alte 2,10 m: sopra, i muri',
                           'continuano fino all\'angolo, quindi l\'ingresso comune resta coperto.']):
        t.testo(16, 240 + i * 4, s, 2.6)

    # bagno e cucina 1:50
    t.testo(232, 36, 'Bagno e cucina, 1:50', 3.2, bold=True)
    v = Vista(t, 20, 252, 58)
    v.piena(.6, 3.4, 5.2, 4.2, VUOTO)
    v.piena(2.75, 2.75, 5.2, 3.4, VUOTO)
    for a in [(0, 0, 1.1, .6), (1.7, 0, 3.55, .6), (4.15, 0, 5.8, .6), (0, 0, .6, 4.2),
              (2.15, .6, 2.75, 3.4), (.6, 2.8, .95, 3.4), (1.8, 2.8, 2.15, 3.4),
              (2.75, 2.15, 3.425, 2.75), (4.275, 2.15, 5.2, 2.75), (4.95, .6, 5.2, .9), (4.95, 1.9, 5.2, 2.15),
              (5.2, 0, 5.8, .9), (5.2, 1.9, 5.8, 4.2)]:
        v.piena(*a)
    t.testo(v.x(1.375), v.y(1.6), 'bagno', 2.5, GRIGIO, 'middle')
    t.testo(v.x(1.375), v.y(1.95), '1,55 × 2,20', 2.3, COL['q'], 'middle')
    t.testo(v.x(3.85), v.y(1.25), 'cucina', 2.5, GRIGIO, 'middle')
    t.testo(v.x(3.85), v.y(1.6), '2,20 × 1,55', 2.3, COL['q'], 'middle')
    v.catena_h([0, 1.1, 1.7, 2.15, 2.75, 3.55, 4.15, 5.2, 5.8], v.y(0) - 4, 'hhhqhhhq', v.y(0))
    v.catena_h([0, .6, 2.15, 2.75, 4.95, 5.2, 5.8], v.y(4.2) + 6, 'qqqqqq', v.y(3.4))
    v.catena_h([.95, 1.8, 3.425, 4.275], v.y(4.2) + 13, 'qhq')
    xr = v.x(5.8)
    v.catena_v([0, .6, .9, 1.9, 2.15, 2.75], xr + 6, 'qhqhq', v.x(5.2))
    v.catena_v([0, .6, 2.8, 3.4], v.x(0) - 5, 'qqq', v.x(.6))

    # camino 1:50
    t.testo(232, 160, 'Camino, 1:50 (senza la nicchia esterna, nell\'angolo sud-est)', 3.2, bold=True)
    c = Vista(t, 20, 252 - 12.4 * 20, 172 - 12.5 * 20)
    c.piena(12.4, 12.5, 15, 12.9, VUOTO)
    c.piena(12.4, 12.9, 12.8, 15, VUOTO)
    c.piena(15, 12.5, 15.6, 15.6)
    c.piena(12.4, 15, 15.6, 15.6)
    c.piena(12.8, 12.9, 15, 15)
    c.cerchio(14.2, 13.95, .8, B, B, .01)
    c.piena(13.3, 13.65, 13.5, 14.25, B)
    c.piena(12.8, 13.45, 13.35, 14.45, B)
    c.rect(12.8, 13.65, 13.4, 14.25, '#c62828', .3, (2, 1))
    t.testo(c.x(14.2), c.y(14.0), 'diam. 1,60', 2.3, COL['q'], 'middle')
    t.testo(c.x(12.6), c.y(13.95), 'vuoto', 2.2, GRIGIO, 'middle', -90)
    c.catena_h([12.8, 13.35, 13.4, 15, 15.6], c.y(12.5) - 3, 'qqqq', c.y(12.9))
    c.catena_h([12.8, 15.6], c.y(15.6) + 5, 'q', c.y(15.6))
    c.catena_v([12.9, 13.45, 13.65, 14.25, 14.45, 15], c.x(15.6) + 6, 'qqqqq', c.x(12.8))
    c.catena_v([12.5, 12.9, 15, 15.6], c.x(15.6) + 13, 'qqq')
    y = tabella(t, 348, 176, [('Camino', 28), ('Metri', 19), ('mm', 11)], [
        (['Blocco largo', '2,10', '21'], 'qqq'),
        (['Dal bordo est', '2,80', '28'], 'qhh'),
        (['Altezza blocco', '3,20', '32'], 'qqq'),
        (['Bocca, larga', '1,00', '10'], 'qqq'),
        (['Canna fumaria', '0,60 × 0,60', '6 × 6'], 'qhh'),
        (['Sopra il tetto', '1,85', '18,5'], 'qqq'),
    ])
    for i, r_ in enumerate(['La bocca guarda a ovest, verso l\'ingresso. Il blocco tocca i muri est e sud: da 129 a 150 mm dal bordo nord.',
                            'Ho tolto nicchia esterna e muro dietro: le altezze restano quelle della tavola 4 della casa vera.',
                            'Bagno e cucina hanno le misure della casa vera. Nel tuo schizzo il bagno era più profondo: con le misure vere',
                            'davanti resta una striscia di vuoto. Il muro est della cucina è spesso 0,85: sul plastico bastano 2 strati di Poliplat.',
                            'Il passaggio tra cucina e stanza è largo 1,00, con altezza 2,10 (scelta mia).']):
        t.testo(232, 246 + i * 4, r_, 2.4, COL['h'] if i == 4 else '#000000')
    legenda(t, 16, 258)
    return t


if __name__ == '__main__':
    cartella, pdf = sys.argv[1], sys.argv[2]
    tavole = [tav_pianta(), tav_dettagli()]
    for t in tavole:
        t.svg(os.path.join(cartella, t.nome + '.svg'))
    scrivi_pdf(tavole, pdf)
    print('ok', len(tavole))
