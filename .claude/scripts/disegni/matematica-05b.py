"""Disegni aggiunti alla bozza di matematica 03 - I vettori (dalle foto della lavagna).

Uso: python3 -I .claude/scripts/disegni/matematica-05b.py
Scrive gli SVG in anno-1/semestre-1/matematica/bozze/img/ (prefisso 05-).
Nessuna dipendenza esterna: riusa le primitive di matematica-05.py.
"""
import importlib.util
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("m03", os.path.join(QUI, "matematica-05.py"))
m03 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m03)

Piano = m03.Piano
BLU, ROSSO, VERDE, GRIGIO = m03.BLU, m03.ROSSO, m03.VERDE, m03.GRIGIO
add, sub, mul = m03.add, m03.sub, m03.mul


def op1_p1p2_op2():
    """Triangolo O, P1, P2: OP1 + P1P2 = OP2, quindi P1P2 = OP2 - OP1."""
    P1, P2 = (4, 1), (2, 4)
    t = Piano(-0.8, 5.6, -0.8, 4.8, s=58)
    t.h += 30
    t.griglia()
    t.freccia((0, 0), P1, col=BLU)
    t.freccia((0, 0), P2, col=VERDE)
    t.freccia(P1, P2, col=ROSSO)
    t.punto(P1)
    t.punto(P2)
    t.testo(P1, "P_1_ = (x_1_, y_1_)", dx=8, dy=18, anchor="start", size=14)
    t.testo(P2, "P_2_ = (x_2_, y_2_)", dx=8, dy=-8, anchor="start", size=14)
    t.testo(mul(0.5, P1), "OP_1_", col=BLU, dx=6, dy=20, anchor="start", size=16)
    t.testo(mul(0.5, P2), "OP_2_", col=VERDE, dx=-10, dy=0, anchor="end", size=16)
    t.testo(mul(0.5, add(P1, P2)), "P_1_P_2_", col=ROSSO, dx=12, dy=0, anchor="start", size=16)
    t.testo_px(t.w / 2, t.h - 14, "OP₁ + P₁P₂ = OP₂, quindi P₁P₂ = OP₂ − OP₁ = (x₂ − x₁, y₂ − y₁)",
               col="#222", size=14)
    t.salva("05-op1-p1p2-op2.svg")


if __name__ == "__main__":
    op1_p1p2_op2()
