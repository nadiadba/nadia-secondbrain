#!/usr/bin/env python3
"""Trasforma un disegno (pianta, sezione, incisione al tratto) in bianco e nero puro,
senza grigi, pronto per gli appunti in PDF.

Uso:
  "$HOME/Library/Application Support/sbobine-whisper/.venv/bin/python" \
      .claude/scripts/bianconero.py ENTRATA USCITA.png [--soglia 170] [--larghezza 1400]
      [--ritaglio SINISTRA,ALTO,DESTRA,BASSO] [--inverti]

- ritaglia da solo i bordi bianchi (e prima l'eventuale ritaglio in pixel indicato);
- porta il disegno in scala di grigi, alza il contrasto e applica una soglia: ogni pixel
  diventa nero o bianco (con --soglia più alta si tengono più tratti chiari);
- --inverti per i disegni chiari su fondo scuro.
Serve Pillow, installato nel venv di sbobine-whisper.
"""
import argparse

from PIL import Image, ImageOps


def main():
    a = argparse.ArgumentParser()
    a.add_argument('entrata')
    a.add_argument('uscita')
    a.add_argument('--soglia', type=int, default=170)
    a.add_argument('--larghezza', type=int, default=1400)
    a.add_argument('--ritaglio', default='')
    a.add_argument('--inverti', action='store_true')
    o = a.parse_args()

    im = Image.open(o.entrata)
    if im.mode in ('RGBA', 'LA', 'P'):
        fondo = Image.new('RGBA', im.size, 'white')
        im = Image.alpha_composite(fondo, im.convert('RGBA'))
    im = im.convert('L')
    if o.ritaglio:
        s, al, d, b = (int(x) for x in o.ritaglio.split(','))
        im = im.crop((s, al, d, b))
    if o.inverti:
        im = ImageOps.invert(im)
    im = ImageOps.autocontrast(im, cutoff=1)
    if im.width > o.larghezza:
        im = im.resize((o.larghezza, round(im.height * o.larghezza / im.width)), Image.LANCZOS)
    bn = im.point(lambda p: 255 if p > o.soglia else 0, mode='1')
    # bordi bianchi via, poi un margine sottile
    scatola = ImageOps.invert(bn.convert('L')).getbbox()
    if scatola:
        bn = bn.crop(scatola)
    bn = ImageOps.expand(bn.convert('L'), border=12, fill=255).convert('1')
    bn.save(o.uscita, optimize=True)
    print(o.uscita, bn.size)


if __name__ == '__main__':
    main()
