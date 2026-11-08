#!/usr/bin/env python3
"""Disegni aggiunti alla bozza di matematica 04-le-funzioni.

L'esercizio del professore f(x) = sqrt(x^2 - x) - x (appunti di Nadia, foto 11):
grafico con dominio, immagine e asintoto orizzontale.

Uso: python3 -I .claude/scripts/disegni/matematica-06b.py
Le immagini SVG vanno in anno-1/semestre-1/matematica/bozze/img/ (prefisso 06-).
Nessuna dipendenza esterna: riusa le primitive di matematica-06.py.
"""
import importlib.util
import math
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("m04", os.path.join(QUI, "matematica-06.py"))
m04 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m04)

SVG, Grafico = m04.SVG, m04.Grafico
BLU, VERDE, ARANCIO, GRIGIO, ROSSO = m04.BLU, m04.VERDE, m04.ARANCIO, m04.GRIGIO, m04.ROSSO


def f(x):
    r = x * x - x
    if r < 0:
        return None
    return math.sqrt(r) - x


def esercizio_radice():
    s = SVG(760, 540)
    g = Grafico(s, 60, 30, 640, 470, (-3, 6.5), (-1.8, 5.2))
    # asintoto orizzontale y = -1/2 (solo dove serve, a destra)
    g.tratteggio(0.4, -0.5, 6.5, -0.5, GRIGIO)
    g.scritta(6.4, -0.5, "asintoto y = −1/2", GRIGIO, "end", dy=26, size=13, italic=True)
    # dominio sull'asse x, immagine sull'asse y
    g.banda_x(-3, 0, VERDE, freccia_a=True)
    g.banda_x(1, 6.5, VERDE, freccia_b=True)
    g.banda_y(-1, -0.5, ARANCIO, chiusoa=True, chiusob=False)
    g.banda_y(0, 5.2, ARANCIO, freccia_b=True)
    # il grafico
    g.curva(f, -3, 0, BLU, n=1500)
    g.curva(f, 1, 6.5, BLU, n=1500)
    g.punto(0, 0, BLU)
    g.punto(1, -1, BLU)
    g.tratteggio(1, 0, 1, -1)
    g.tratteggio(0, -1, 1, -1)
    g.scritta(1, -1, "(1, −1)", BLU, "start", dx=8, dy=16, size=14)
    g.scritta(-1, f(-1), "(−1, 1 + √2)", BLU, "end", dx=-10, dy=8, size=13)
    g.punto(-1, f(-1), BLU, r=4)
    g.scritta(2.2, 3.6, "f(x) = √(x² − x) − x", BLU, "start", size=16, italic=True)
    # didascalie
    g.scritta(-1.6, 0, "dominio (−∞, 0]", VERDE, "middle", dy=-12, size=13, bold=True)
    g.scritta(5.2, 0, "dominio [1, +∞)", VERDE, "middle", dy=-12, size=13, bold=True)
    g.scritta(0, 4.4, "immagine [0, +∞)", ARANCIO, "start", dx=12, size=13, bold=True)
    g.scritta(0, -0.75, "immagine [−1, −1/2)", ARANCIO, "end", dx=-12, dy=5, size=13, bold=True)
    s.save("06-esercizio-radice.svg")


if __name__ == "__main__":
    esercizio_radice()
