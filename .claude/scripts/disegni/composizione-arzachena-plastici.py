#!/usr/bin/env python3
"""Casa ad Arzachena: i pezzi di Poliplat da 0,5 cm per i due plastici in scala 1:100.

Uso: python3 -I composizione-arzachena-plastici.py PERCORSO_PDF
Un foglio A4 per pezzo: il pezzo evidenziato in pianta e il rettangolo da tagliare a
grandezza vera, con i tagli. Coordinate in cm sul plastico: x dal bordo ovest, y dal bordo
nord, z dal pavimento. Regole: i muri sono spessi 0,5 invece di 0,6; il filo verso
l'esterno e verso il vuoto resta fermo, il millimetro in piu' va dentro le stanze; i muri
nord e sud sono interi, gli altri si fermano contro di loro.
"""
import importlib.util
import os
import sys

_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'composizione-arzachena.py')
_s = importlib.util.spec_from_file_location('arzachena', _p)
A = importlib.util.module_from_spec(_s)
_s.loader.exec_module(A)
A.W, A.H = 297.0, 210.0
Tavola, Vista, COL, GRIGIO, tabella, scrivi_pdf = A.Tavola, A.Vista, A.COL, A.GRIGIO, A.tabella, A.scrivi_pdf
ROSSO = '#c62828'
ROSA = '#f6c9c9'
SCURO = '#6f6f6f'
CHIARO = '#d9d9d9'
H_MURO = 3.3
T = 0.5


def num(v):
    s = ('%.2f' % v).rstrip('0').rstrip('.')
    return s.replace('.', ',')


class Pezzo:
    def __init__(self, nome, x1, y1, x2, y2, h=H_MURO, tagli=(), nota='', tipo='muro', dim=None):
        self.nome, self.x1, self.y1, self.x2, self.y2, self.h = nome, x1, y1, x2, y2, h
        self.tagli, self.nota, self.tipo, self.dim = list(tagli), nota, tipo, dim
        self.est_ovest = (x2 - x1) >= (y2 - y1)

    @property
    def lungo(self):
        return round((self.x2 - self.x1) if self.est_ovest else (self.y2 - self.y1), 3)

    @property
    def spesso(self):
        return round((self.y2 - self.y1) if self.est_ovest else (self.x2 - self.x1), 3)

    def inizio(self):
        return self.x1 if self.est_ovest else self.y1

    def misura(self):
        if self.dim:
            return self.dim
        if self.tipo == 'piano':
            return '%s × %s cm' % (num(self.x2 - self.x1), num(self.y2 - self.y1))
        return '%s × %s cm' % (num(self.lungo), num(self.h))


# ---------------------------------------------------------------- finestre e porte

def fin(a, b):
    return (a, b, 1.05, 1.7, 'finestra')


def porta_in_fondo(a, b):
    return (a, b, 0, 2.1, 'porta')


def zanuso():
    d = 'Il pezzo arriva fino all\'angolo della croce: in basso lascia il varco della porta, sopra prosegue.'
    return [
        Pezzo('Base del plastico', -2.2, -2.2, 17.8, 17.8, tipo='piano', nota='Misura libera: serve a tenere il plastico e a dare il terreno intorno alla casa. Ho scelto 20 cm per lasciare 2,2 cm per lato.'),
        Pezzo('Rialzo della casa', 0, 0, 15.6, 15.6, tipo='piano', nota='Si incolla al centro della base. È il pavimento: in realtà 0,40 m (4 mm), con il Poliplat diventa 5 mm. I muri si incollano sopra.'),
        Pezzo('Gradino dell\'apertura nord', 5.8, -.6, 9.8, 0, tipo='piano', nota='Sulla base, contro il lato nord del rialzo. In realtà i gradini sono due: con il Poliplat basta un solo gradino.'),
        Pezzo('Muro nord', 0, 0, 15.6, T, tagli=[fin(2.45, 2.95), (5.8, 9.8, 0, 2.0, 'apertura nord'), fin(13, 13.5)], nota='Sul bordo nord del rialzo, intero da un angolo all\'altro. Si guarda da fuori con l\'ovest a sinistra.'),
        Pezzo('Muro sud', 0, 15.1, 15.6, 15.6, tagli=[fin(12.7, 13.3)], nota='Sul bordo sud del rialzo, intero da un angolo all\'altro.'),
        Pezzo('Muro est', 15.1, T, 15.6, 15.1, tagli=[(6.3, 9.3, 1, 2, 'finestra grande')], nota='Sul bordo est, tra il muro nord e il muro sud.'),
        Pezzo('Muro ovest, parte nord', 0, T, T, 7.15, tagli=[fin(5.5, 6.1)], nota='Sul bordo ovest: parte dal muro nord e si ferma alla nicchia esterna del camino.'),
        Pezzo('Muro ovest, parte sud', 0, 8.45, T, 15.1, tagli=[fin(9.4, 10), fin(13, 13.6)], nota='Sul bordo ovest: dalla nicchia esterna fino al muro sud.'),
        Pezzo('Fondo della nicchia esterna', T, 6.75, 1.0, 8.85, nota='Subito dietro i due pezzi del muro ovest, che lasciano una fessura di 1,3 cm. La nicchia vera è tonda e profonda 0,85: qui è dritta e profonda 0,5.'),
        Pezzo('Muro del camino verso la corte', 2.9, 5.2, 3.4, 10.4, tagli=[(5.45, 6.3, 0, 2.1, 'cucina'), (7.3, 8.3, 0, 1.46, 'bocca'), (9.3, 10.15, 0, 2.1, 'bagno')], nota='Tiene le tre aperture sulla corte. La faccia verso la corte sta a 3,4 cm dal bordo ovest. Le altezze di cucina e bagno sono un\'ipotesi.'),
        Pezzo('Fianco del camino verso la cucina', 1.0, 6.75, 2.9, 7.25, nota='Tra il fondo della nicchia e il muro del camino.'),
        Pezzo('Fianco del camino verso il bagno', 1.0, 8.35, 2.9, 8.85, nota='Tra il fondo della nicchia e il muro del camino.'),
        Pezzo('Pilastro nord-ovest', 4.7, T, 5.2, 5.2, tagli=[porta_in_fondo(3.7, 5.2)], nota=d),
        Pezzo('Muro tra stanza nord-ovest e corte', 1.85, 4.7, 4.7, 5.2, tagli=[porta_in_fondo(3.7, 4.7)], nota='A sinistra lascia il passaggio libero verso la cucina. A destra si ferma contro il pilastro, lasciando il varco della porta.'),
        Pezzo('Pilastro nord-est', 10.4, T, 10.9, 5.2, tagli=[porta_in_fondo(3.7, 5.2)], nota=d),
        Pezzo('Muro tra stanza nord-est e corte', 10.9, 4.7, 15.1, 5.2, tagli=[porta_in_fondo(10.9, 11.9)], nota='Dal pilastro nord-est al muro est.'),
        Pezzo('Pilastro sud-ovest', 4.7, 10.4, 5.2, 15.1, tagli=[porta_in_fondo(10.4, 11.9)], nota=d),
        Pezzo('Muro tra stanza sud-ovest e bagno', T, 10.4, 4.7, 10.9, tagli=[porta_in_fondo(3.7, 4.7)], nota='Dal muro ovest al pilastro sud-ovest. La piccola nicchia del bagno è dentro questo muro e non si vede: non serve farla.'),
        Pezzo('Pilastro sud-est', 10.4, 10.4, 10.9, 15.1, tagli=[porta_in_fondo(10.4, 11.9)], nota=d),
        Pezzo('Muro tra stanza sud-est e corte', 10.9, 10.4, 15.1, 10.9, tagli=[porta_in_fondo(10.9, 11.9)], nota='Dal pilastro sud-est al muro est.'),
        Pezzo('Canna fumaria', 2.9, 7.5, 3.4, 8.1, h=1.85, tipo='canna', nota='Si incolla in piedi sopra il muro del camino verso la corte, a metà. Sta sopra i 3,3 cm del muro. La profondità di 0,6 cm è un\'ipotesi.'),
        Pezzo('Tavolo', 7.125, 7.125, 8.475, 8.475, tipo='piano', dim='cerchio, diametro 1,35 cm', nota='Un dischetto di Poliplat incollato al centro della corte. L\'altezza vera non è sulla scheda: lo spessore del Poliplat va bene.'),
        Pezzo('Tetto della stanza nord-ovest', 0, 0, 5.2, 5.2, tipo='piano', nota='Appoggiato sui muri, senza colla. Meglio cartone sottile (cartonlegno 2 mm o cartoncino): con il Poliplat la casa si alza di 5 mm.'),
        Pezzo('Tetto della fascia ovest', 0, 5.2, 3.4, 10.4, tipo='piano', nota='Appoggiato. Copre cucina, camino e bagno. Sul lato est fai una tacca di 0,6 × 0,5 cm a 2,3 cm dall\'estremità nord per la canna fumaria.'),
        Pezzo('Tetto della stanza nord-est', 10.4, 0, 15.6, 5.2, tipo='piano', nota='Appoggiato sui muri, senza colla. Stesso materiale degli altri tetti.'),
        Pezzo('Tetto della stanza sud-ovest', 0, 10.4, 5.2, 15.6, tipo='piano', nota='Appoggiato sui muri, senza colla. Stesso materiale degli altri tetti.'),
        Pezzo('Tetto della stanza sud-est', 10.4, 10.4, 15.6, 15.6, tipo='piano', nota='Appoggiato sui muri, senza colla. Stesso materiale degli altri tetti.'),
        Pezzo('Copertura di canne sulla corte', 4.3, 5.3, 11.3, 10.3, tipo='piano', nota='Cartoncino sottile, appoggiato: ai lati poggia sui muri delle stanze. Toglilo per la foto dall\'alto della croce.'),
    ]


def progetto():
    return [
        Pezzo('Base del plastico', -2.2, -2.2, 17.8, 17.8, tipo='piano', nota='Misura libera: serve a tenere il plastico e a dare il terreno intorno alla casa. Ho scelto 20 cm per lasciare 2,2 cm per lato.'),
        Pezzo('Rialzo della casa', 0, 0, 15.6, 15.6, tipo='piano', nota='Si incolla al centro della base. È il pavimento: i muri si incollano sopra.'),
        Pezzo('Gradino dell\'ingresso', 5.8, 15.6, 9.8, 16.2, tipo='piano', nota='Sulla base, contro il lato sud del rialzo. Con il Poliplat basta un solo gradino.'),
        Pezzo('Muro nord', 0, 0, 15.6, T, tagli=[fin(1.1, 1.7), fin(3.55, 4.15), fin(7.55, 8.05), fin(13, 13.5)], nota='Sul bordo nord del rialzo, intero da un angolo all\'altro. Le finestre sono, da sinistra: bagno, cucina e due stanze.'),
        Pezzo('Muro sud', 0, 15.1, 15.6, 15.6, tagli=[(5.8, 9.8, 0, 2.0, 'ingresso')], nota='Sul bordo sud del rialzo, intero. Ha l\'ingresso largo 4 cm.'),
        Pezzo('Muro est', 15.1, T, 15.6, 15.1, tagli=[fin(7.55, 8.05)], nota='Sul bordo est, tra il muro nord e il muro sud.'),
        Pezzo('Muro ovest', 0, T, T, 15.1, tagli=[(6.3, 9.3, 1, 2, 'finestra grande'), fin(13, 13.6)], nota='Sul bordo ovest, tra il muro nord e il muro sud. Ha la finestra grande sul vuoto e quella della stanza in basso a sinistra.'),
        Pezzo('Tramezzo tra bagno e cucina', 2.05, T, 2.55, 3.2, nota='Parte dal muro nord. Il bagno resta largo 1,55 cm.'),
        Pezzo('Muro sud del bagno', T, 2.7, 2.05, 3.2, tagli=[(.95, 1.8, 0, 2.1, 'bagno')], nota='Tra il muro ovest e il tramezzo. L\'apertura dà sul vuoto.'),
        Pezzo('Muro sud della cucina', 2.55, 2.05, 4.75, 2.55, tagli=[(3.225, 4.075, 0, 2.1, 'cucina')], nota='Tra il tramezzo e il muro est della cucina. L\'apertura dà sul vuoto.'),
        Pezzo('Muro est della cucina', 4.75, T, 5.25, 2.55, tagli=[(.9, 1.9, 0, 2.1, 'passaggio')], nota='Il passaggio deve coincidere con quello del pezzo successivo: i due muri stanno appiccicati.'),
        Pezzo('Muro ovest della stanza in alto al centro', 5.25, T, 5.75, 5.2, tagli=[(.9, 1.9, 0, 2.1, 'passaggio')], nota='Appiccicato al muro est della cucina, con il passaggio nello stesso punto. Prosegue fino al vuoto.'),
        Pezzo('Muro sud della stanza in alto al centro', 5.75, 4.7, 9.9, 5.2, tagli=[porta_in_fondo(8.9, 9.9)], nota='La faccia sul vuoto sta a 5,2 cm dal bordo nord. A destra lascia il varco della porta.'),
        Pezzo('Muro est della stanza in alto al centro', 9.9, T, 10.4, 5.2, tagli=[porta_in_fondo(3.7, 5.2)], nota='Arriva all\'angolo in cui si incontrano le tre stanze. In basso lascia il varco della porta, sopra prosegue.'),
        Pezzo('Muro ovest della stanza in alto a destra', 10.4, T, 10.9, 5.2, tagli=[porta_in_fondo(3.7, 5.2)], nota='Appiccicato al pezzo precedente. In basso lascia il varco della porta.'),
        Pezzo('Muro sud della stanza in alto a destra', 10.9, 4.7, 15.1, 5.2, tagli=[porta_in_fondo(10.9, 11.9)], nota='Dal muro ovest della stanza fino al muro est della casa.'),
        Pezzo('Muro nord della stanza sul lato est', 10.9, 5.2, 15.1, 5.7, tagli=[porta_in_fondo(10.9, 11.9)], nota='Appiccicato al pezzo precedente, sul lato sud.'),
        Pezzo('Muro ovest della stanza sul lato est', 10.4, 5.2, 10.9, 9.9, tagli=[porta_in_fondo(5.2, 6.7)], nota='Parte dall\'angolo delle tre stanze. Sotto, all\'inizio, lascia il varco della porta.'),
        Pezzo('Muro sud della stanza sul lato est', 10.4, 9.9, 15.1, 10.4, nota='Dal vuoto fino al muro est. Questo muro è senza aperture.'),
        Pezzo('Muro nord della stanza in basso a sinistra', T, 10.4, 4.7, 10.9, tagli=[porta_in_fondo(3.7, 4.7)], nota='Dal muro ovest fino al pezzo successivo. A destra lascia il varco della porta.'),
        Pezzo('Muro est della stanza in basso a sinistra', 4.7, 10.4, 5.2, 15.1, tagli=[porta_in_fondo(10.4, 11.9)], nota='Dal vuoto fino al muro sud. In alto lascia il varco della porta.'),
        Pezzo('Faccia del camino', 12.8, 12.9, 13.3, 15.1, h=2.7, tagli=[(13.45, 14.45, 0, 1.46, 'bocca')], nota='Guarda a ovest, verso l\'ingresso. È alta 2,7 cm perché sopra si appoggia il coperchio: in totale 3,2 cm.'),
        Pezzo('Fianco nord del camino', 13.3, 12.9, 15.1, 13.4, h=2.7, nota='Dalla faccia del camino fino al muro est.'),
        Pezzo('Coperchio del camino', 12.8, 12.9, 15.1, 15.1, tipo='piano', nota='Si incolla sopra faccia e fianco: il blocco arriva così a 3,2 cm. Il camino qui è più corto di quello vero: niente nicchia esterna.'),
        Pezzo('Canna fumaria', 12.8, 13.65, 13.3, 14.25, h=1.95, tipo='canna', nota='Si incolla in piedi sopra il coperchio, sul lato della bocca. La cima arriva a 5,15 cm dal pavimento. La profondità di 0,6 cm è un\'ipotesi.'),
        Pezzo('Tavolo', 7.125, 7.125, 8.475, 8.475, tipo='piano', dim='cerchio, diametro 1,35 cm', nota='Un dischetto di Poliplat incollato al centro del quadrato centrale della griglia.'),
        Pezzo('Tetto del bagno', 0, 0, 2.55, 3.2, tipo='piano', nota='Appoggiato sui muri, senza colla. Meglio cartone sottile: con il Poliplat la casa si alza di 5 mm.'),
        Pezzo('Tetto della cucina', 2.55, 0, 5.25, 2.55, tipo='piano', nota='Appoggiato sui muri, senza colla. Stesso materiale degli altri tetti.'),
        Pezzo('Tetto della stanza in alto al centro', 5.25, 0, 10.4, 5.2, tipo='piano', nota='Appoggiato sui muri. Copre anche un quarto dell\'ingresso comune.'),
        Pezzo('Tetto della stanza in alto a destra', 10.4, 0, 15.6, 5.2, tipo='piano', nota='Appoggiato sui muri. Copre anche un quarto dell\'ingresso comune.'),
        Pezzo('Tetto della stanza sul lato est', 10.4, 5.2, 15.6, 10.4, tipo='piano', nota='Appoggiato sui muri. Copre anche un quarto dell\'ingresso comune.'),
        Pezzo('Tetto della stanza in basso a sinistra', 0, 10.4, 5.2, 15.6, tipo='piano', nota='Appoggiato sui muri, senza colla. Stesso materiale degli altri tetti.'),
    ]


def controlla(pezzi, nome):
    muri = [p for p in pezzi if p.tipo == 'muro']
    errori = []
    for p in muri:
        if abs(p.spesso - T) > 1e-6:
            errori.append('%s: spessore %s' % (p.nome, p.spesso))
        if p.x1 < 0 or p.y1 < 0 or p.x2 > 15.6 + 1e-9 or p.y2 > 15.6 + 1e-9:
            errori.append('%s: fuori dal perimetro' % p.nome)
        a0, a1 = (p.x1, p.x2) if p.est_ovest else (p.y1, p.y2)
        for t in p.tagli:
            if t[0] < a0 - 1e-9 or t[1] > a1 + 1e-9 or t[2] < 0 or t[3] > p.h:
                errori.append('%s: taglio fuori dal rettangolo %s' % (p.nome, t))
    for i, a in enumerate(muri):
        for b in muri[i + 1:]:
            if min(a.x2, b.x2) - max(a.x1, b.x1) > 1e-6 and min(a.y2, b.y2) - max(a.y1, b.y1) > 1e-6:
                errori.append('%s si sovrappone a %s' % (a.nome, b.nome))
    if errori:
        raise SystemExit(nome + ':\n' + '\n'.join(errori))


# ---------------------------------------------------------------- disegno

def pianta(t, v, pezzi, attivo=None):
    v.piena(0, 0, 15.6, 15.6, '#f4f4f4')
    t.linea(v.pts([(0, 0), (15.6, 0), (15.6, 15.6), (0, 15.6)]), GRIGIO, .15, None, True)

    def disegna(p, pieno, sopra):
        if p.tipo != 'muro':
            v.piena(p.x1, p.y1, p.x2, p.y2, pieno)
            return
        vuoti = sorted((c[0], c[1]) for c in p.tagli if c[2] == 0)
        ini, fine = (p.x1, p.x2) if p.est_ovest else (p.y1, p.y2)
        cur = ini
        for a, b in vuoti + [(fine, fine)]:
            if a > cur:
                v.piena(cur, p.y1, a, p.y2, pieno) if p.est_ovest else v.piena(p.x1, cur, p.x2, a, pieno)
            if b > a:
                v.piena(a, p.y1, b, p.y2, sopra) if p.est_ovest else v.piena(p.x1, a, p.x2, b, sopra)
            cur = b
    for p in pezzi:
        if p.tipo == 'muro':
            disegna(p, SCURO, CHIARO)
    if attivo:
        if attivo.tipo == 'piano':
            x1, y1, x2, y2 = max(attivo.x1, -1.5), max(attivo.y1, -1.5), min(attivo.x2, 17.1), min(attivo.y2, 17.1)
            if attivo.dim:
                v.cerchio((x1 + x2) / 2, (y1 + y2) / 2, (x2 - x1) / 2, ROSSO, ROSSO, .2)
            else:
                v.rect(x1, y1, x2, y2, ROSSO, .5, None, None)
                t.op.insert(len(t.op) - 1, ('p', v.pts([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), ROSA, .01, None, True, ROSA))
                for p in pezzi:
                    if p.tipo == 'muro':
                        disegna(p, SCURO, CHIARO)
                v.rect(x1, y1, x2, y2, ROSSO, .5)
        else:
            disegna(attivo, ROSSO, ROSA)
            if attivo.tipo == 'canna':
                v.rect(attivo.x1 - .25, attivo.y1 - .25, attivo.x2 + .25, attivo.y2 + .25, ROSSO, .4)


def piede(t, n, tot, casa):
    t.testo(287, 203, '%s. Foglio %d di %d.' % (casa, n, tot), 2.4, GRIGIO, 'end')
    t.testo(10, 203, 'Stampa in A4 al 100%: il rettangolo è a grandezza vera, se non è indicato altro.', 2.4, GRIGIO)


def a_capo(testo, massimo):
    righe, riga = [], ''
    for par in testo.split(' '):
        if len(riga) + len(par) + 1 > massimo:
            righe.append(riga)
            riga = par
        else:
            riga = (riga + ' ' + par).strip()
    righe.append(riga)
    return righe


def foglio_pezzo(p, i, pezzi, n, tot, casa, sigla):
    t = Tavola('')
    t.testo(10, 14, '%s%02d  %s' % (sigla, i, p.nome), 7, bold=True)
    t.testo(10, 20.5, casa, 3, GRIGIO)
    v = Vista(t, 6, 16, 44)
    if p.y1 < 0 or p.y2 > 15.6 or p.x1 < 0:
        v = Vista(t, 5.4, 22, 44)
    pianta(t, v, pezzi, p)
    t.linea([(100, 150), (98, 155), (100, 154), (102, 155)], '#000000', .2, None, True, '#000000')
    t.testo(100, 148.5, 'N', 2.6, bold=True, anchor='middle')
    t.rett(14, 150, 19, 153, ROSSO)
    t.testo(21, 152.8, 'questo pezzo', 2.7)
    t.rett(14, 155, 19, 158, SCURO)
    t.testo(21, 157.8, 'muri già fatti o da fare', 2.7)
    t.rett(14, 160, 19, 163, CHIARO)
    t.testo(21, 162.8, 'muro solo in alto (sopra la porta)', 2.7)
    x0 = 124
    t.testo(x0, 30, 'Rettangolo da tagliare:', 3.6, GRIGIO)
    t.testo(x0, 39, p.misura(), 9, ROSSO, bold=True)
    if p.tipo == 'piano':
        w, h = p.x2 - p.x1, p.y2 - p.y1
        k = min(10, 150 / w, 66 / h)
        d = Vista(t, k, x0, 50)
        if p.dim:
            d.cerchio(w / 2, w / 2, w / 2, ROSA, ROSSO, .4)
        else:
            d.t.rett(d.x(0), d.y(0), d.x(w), d.y(h), ROSA, ROSSO, .4)
        if not p.dim:
            d.catena_h([0, w], d.y(0) - 2.5, 'q', None, 2.8)
            d.catena_v([0, h], d.x(w) + 3, 'q', None, 2.8, True)
        if k < 9.99:
            t.testo(x0, d.y(h) + 5, 'Disegno ridotto: taglia con le misure scritte (cm).', 2.8, GRIGIO)
        y = 50 + h * k + 11
    else:
        lungh = p.h if p.tipo == 'canna' else p.lungo
        larg_d = p.y2 - p.y1 if p.tipo == 'canna' else p.lungo
        h = p.h
        d = Vista(t, 10, x0, 50 + h * 10, 1, -1)
        d.t.rett(d.x(0), d.y(0), d.x(larg_d), d.y(h), ROSA, ROSSO, .4)
        ini = p.inizio()
        uu = {0.0, round(larg_d, 3)}
        zz = {0.0, h}
        for a, b, z1, z2, et in p.tagli:
            u1, u2 = a - ini, b - ini
            d.t.rett(d.x(u1), d.y(z1), d.x(u2), d.y(z2), '#ffffff', ROSSO, .25)
            d.t.linea(d.pts([(u1, z1), (u2, z2)]), ROSSO, .1, (1, 1))
            d.t.linea(d.pts([(u1, z2), (u2, z1)]), ROSSO, .1, (1, 1))
            uu |= {round(u1, 3), round(u2, 3)}
            zz |= {z1, z2}
            t.testo(d.x((u1 + u2) / 2), d.y((z1 + z2) / 2) + 1, et, 2.3 if (u2 - u1) > .85 else 1.8, '#000000', 'middle')
        d.catena_h(sorted(uu), d.y(0) + 5, 'q' * len(uu), d.y(0), 2.6)
        d.catena_v(sorted(zz), d.x(larg_d) + 3, 'q' * len(zz), d.x(larg_d), 2.6, True)
        lato = 'ovest' if p.est_ovest else 'nord'
        if p.tagli:
            t.testo(x0, d.y(0) + 10.5, 'Sinistra del disegno = estremità %s. Le zone crociate si tolgono. Misure in cm.' % lato, 2.7, GRIGIO)
        y = d.y(0) + 16
        tes = 'Spessore: 0,5 cm (il Poliplat). Va in piedi, con la base sul pavimento.' if p.tipo == 'muro' else 'Spessore: 0,5 cm. Va in piedi, sopra il pezzo indicato.'
        t.testo(x0, y, tes, 3)
        y += 6
    y = max(y, 118)
    t.testo(x0, y, 'Dove va', 3.6, bold=True)
    y += 5.5
    if p.tipo != 'piano' or p.y1 >= 0 and p.x1 >= 0 and not p.dim:
        pos = 'A %s-%s cm dal bordo ovest, %s-%s cm dal bordo nord.' % (num(p.x1), num(p.x2), num(p.y1), num(p.y2))
        t.testo(x0, y, pos, 3.1)
        y += 5
    for r in a_capo(p.nota, 82):
        t.testo(x0, y, r, 3.1)
        y += 4.6
    piede(t, n, tot, casa)
    return t


def copertina(pezzi, casa, sigla, n, tot):
    t = Tavola('')
    t.testo(10, 16, casa, 8, bold=True)
    t.testo(10, 23, 'I pezzi di Poliplat da 0,5 cm per il plastico in scala 1:100. Le misure sono in cm sul plastico.', 3.2, GRIGIO)
    v = Vista(t, 5, 16, 34)
    pianta(t, v, pezzi)
    t.testo(10, 120, 'Cosa ho cambiato per lo spessore', 3.4, bold=True)
    regole = ['I muri sono spessi 0,5 cm invece di 0,6.',
              'Il perimetro resta 15,6 × 15,6 cm: è sempre scala 1:100.',
              'La faccia verso l\'esterno e verso il vuoto resta al suo posto.',
              'Quel millimetro va dentro le stanze: sono 4,2 cm invece di 4.',
              'I muri nord e sud sono interi, gli altri si fermano contro di loro.',
              'Le porte sono varchi senza anta: sopra 2,1 cm il muro prosegue.',
              'I muri sono dritti: in realtà quelli esterni sono inclinati.']
    for i, r in enumerate(regole):
        t.testo(10, 126 + i * 4.6, r, 2.9)
    t.testo(10, 163, 'Ordine di montaggio', 3.4, bold=True)
    for i, r in enumerate(['Segui i numeri: base, rialzo, muri esterni, muri interni, poi i tetti.',
                           'Prima di incollare ogni muro, controlla la posizione sulla pianta.',
                           'Le quote sono al millimetro: se un pezzo balla di 0,5 mm va bene.']):
        t.testo(10, 169 + i * 4.6, r, 2.9)
    righe = []
    for i, p in enumerate(pezzi, 1):
        righe.append((['%s%02d' % (sigla, i), p.nome, p.misura()], 'qqq'))
    meta = (len(righe) + 1) // 2
    tabella(t, 104, 34, [('Pezzo', 11), ('Nome', 60), ('Misura', 22)], righe[:meta], 'Elenco dei pezzi', 2.15)
    tabella(t, 200, 38.5, [('Pezzo', 9), ('Nome', 56), ('Misura', 22)], righe[meta:], None, 2.15)
    piede(t, n, tot, casa)
    return t


if __name__ == '__main__':
    pdf = sys.argv[1]
    case = [('Casa di Zanuso', 'Z', zanuso()), ('La tua nuova disposizione', 'N', progetto())]
    tot = sum(len(c[2]) + 1 for c in case)
    tavole = []
    n = 1
    for nome, sigla, pezzi in case:
        controlla(pezzi, nome)
        tavole.append(copertina(pezzi, nome, sigla, n, tot))
        n += 1
        for i, p in enumerate(pezzi, 1):
            tavole.append(foglio_pezzo(p, i, pezzi, n, tot, nome, sigla))
            n += 1
    scrivi_pdf(tavole, pdf)
    print('ok', tot, 'fogli')
    for nome, sigla, pezzi in case:
        print(nome, len(pezzi), 'pezzi; muri:', sum(p.tipo == 'muro' for p in pezzi))
