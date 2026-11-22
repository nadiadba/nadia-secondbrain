#!/usr/bin/env python3
"""Esercizio 4, punto 5: la nuova disposizione di Nadia della casa di Muuratsalo.
Pianta quotata, due sezioni con le altezze e i pezzi per la pagina 3D.

Uso: python3 -I composizione-muuratsalo-nadia.py [pezzi3d.json]
Coordinate come in composizione-muuratsalo.py: x verso est dal filo esterno ovest, y verso sud
dal filo esterno nord, z dal pavimento, in metri. Le stanze sono quelle della pagina interattiva
(23/11/2026), allineate sugli assi dei muri: i muri stanno a cavallo degli assi.
"""
import importlib.util
import json
import math
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("aalto", os.path.join(QUI, "composizione-muuratsalo.py"))
aalto = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aalto)
Disegno, num, FONT = aalto.Disegno, aalto.num, aalto.FONT
NERO, BLU, ROSSO, GRIGIO = aalto.NERO, aalto.BLU, aalto.ROSSO, aalto.GRIGIO

OUT = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/composizione-architettonica/bozze/img/"
VER = "v5"
LEGNO = "#6d4c2f"

# ---- il tetto: alto a nord sopra le camere, scende verso il lago. Come in Aalto il profilo
# ricomincia a salire a 2,15 m dal perimetro (da lui a 12,25 dal filo ovest, qui a 12,25 dal filo
# nord) e risale di 0,65 fino al perimetro: il tetto della casa finisce prima (10,53), quindi la
# risalita si vede sui muri del recinto a ovest e a est e sull'altezza del recinto sud -------------
H_N, Y_S = 6.30, 10.53                # estradosso sul filo nord; filo esterno sud del soggiorno
K_GIU = (6.30 - 4.50) / 10.53         # pendenza della falda che scende
Y_B = 14.40 - 2.15                    # punto piu' basso, alla stessa distanza dal perimetro di Aalto
RISALITA = 0.65                       # come Aalto: da 2,60 a 3,25
SP_TETTO = 0.30


def f2(v):
    return ("%.2f" % v).replace(".", ",")


def falda(y):
    """La linea della falda che scende, prolungata (serve anche per il recinto)."""
    return H_N - K_GIU * y


def ze(y):
    return falda(y) if y <= Y_B else falda(Y_B) + RISALITA / (14.40 - Y_B) * (y - Y_B)


def zi(y):
    return ze(y) - SP_TETTO


# i muri del recinto (ovest, est e sud) continuano la linea della falda fino al filo sud
MURETTO = 1.80                         # muretto sotto il graticcio
SOPP_SOTTO, SOPP_SP = 2.20, 0.20       # intradosso del soppalco e spessore del solaio
SOPP = (7.01, 4.05, 10.80, 7.84)       # soppalco dello studio (3,79 x 3,79)
SCALA = (10.10, 7.84, 10.70, 10.08)    # scaletta: sale verso nord fino al bordo del soppalco

# ---- le stanze (sugli assi dei muri) ----------------------------------------------------------
STANZE = [  # nome, zona, x1, y1, x2, y2
    ("Camera grande", "notte", 0.40, 0.40, 5.37, 3.05),
    ("Guardaroba", "notte", 5.37, 0.40, 7.82, 3.05),
    ("Camera", "notte", 7.82, 0.40, 11.33, 3.05),
    ("Bagno", "servizi", 11.33, 0.40, 14.00, 2.24),
    ("Disimpegno", "distr", 11.33, 2.24, 14.00, 4.00),
    ("Corridoio", "distr", 4.45, 3.05, 11.33, 4.00),
    ("Soggiorno, pranzo e atelier", "giorno", 4.45, 4.00, 10.85, 10.38),
    ("Cucina", "servizi", 10.85, 4.00, 14.00, 8.12),
    ("Ingresso (in legno)", "distr", 14.40, 2.24, 16.15, 8.07),
    ("Annesso degli ospiti", "notte", 14.40, 8.07, 18.65, 14.34),
]
AALTO = {"Camera grande": 12.96, "Guardaroba": 6.34, "Camera": 9.1, "Bagno": 4.88, "Disimpegno": 5.31,
         "Corridoio": 6.25, "Soggiorno, pranzo e atelier": 40.67, "Cucina": 12.96}


def patio_area():
    tot = 13.60 * 13.60
    for n, z, x1, y1, x2, y2 in STANZE:
        if x2 <= 14.0:
            tot -= (x2 - x1) * (y2 - y1)
    return tot


# ---- i muri -----------------------------------------------------------------------------------
# asse "x": il muro corre da est a ovest (a1..a2 lungo x, c1..c2 lungo y); asse "y": da nord a sud.
# top: "T" = sotto il tetto, oppure un numero. z0: quota del piede (architravi).
# ap: aperture (s1, s2, tipo, z1, z2, apre, cerniera) con s lungo l'asse del muro.
# pianta: "pieno", "finestra" (tutto il pezzo e' una finestra), "muretto" (graticcio), "no".
def M(asse, a1, a2, c1, c2, top="T", ap=(), pianta="pieno", legno=False, z0=0.0, nome=""):
    return dict(asse=asse, a1=a1, a2=a2, c1=c1, c2=c2, top=top, ap=list(ap), pianta=pianta, legno=legno, z0=z0, nome=nome)


def F(s1, s2, z1, z2):
    return (s1, s2, "finestra", z1, z2, None, None)


def P(s1, s2, apre, cern="a", z2=2.10, tipo="porta"):
    return (s1, s2, tipo, 0.0, z2, apre, cern)


def V(s1, s2, z2=2.20):
    return (s1, s2, "vuoto", 0.0, z2, None, None)


MURI = [
    # perimetro della casa e recinto (spessore 0,40)
    M("x", 0, 14.40, 0, 0.40, ap=[F(2.35, 3.30, 1.1, 2.1), F(6.10, 7.05, 1.1, 2.1), F(9.00, 10.20, 0.9, 2.1),
                                 F(12.25, 13.20, 1.4, 2.1)], top="F", nome="nord"),
    M("y", 0.40, 3.20, 0, 0.40, top="F", nome="ovest casa"),
    M("y", 3.20, 9.30, 0, 0.40, top="E", nome="recinto ovest"),
    M("y", 9.30, 11.75, 0, 0.40, top=MURETTO, pianta="muretto", nome="graticcio ovest"),
    M("x", 2.65, 5.10, 14.00, 14.40, top=MURETTO, pianta="muretto", nome="graticcio sud"),
    M("x", 5.10, 14.00, 14.00, 14.40, top="E", nome="recinto sud"),
    M("y", 0.40, 8.27, 14.00, 14.40, ap=[P(2.80, 3.90, "E", "b", 2.2)], top="F", nome="est casa"),
    M("y", 8.27, 14.40, 14.00, 14.40, top="E", nome="recinto est"),
    # muri della casa sul patio (0,30)
    M("x", 0.40, 4.30, 2.90, 3.20, ap=[F(1.40, 3.40, 0.9, 2.1)], nome="camera grande sul patio"),
    M("y", 2.90, 7.88, 4.30, 4.60, ap=[P(3.13, 3.93, "W", "a", tipo="portafinestra")], nome="ovest soggiorno"),
    M("y", 7.88, 10.23, 4.30, 4.60, top=1.10, pianta="finestra", nome="finestra d'angolo, ovest"),
    M("y", 7.88, 10.23, 4.30, 4.60, z0=2.10, pianta="no"),
    M("x", 4.30, 6.95, 10.23, 10.53, top=0.50, pianta="finestra", nome="finestra d'angolo, sud"),
    M("x", 4.30, 6.95, 10.23, 10.53, z0=2.10, pianta="no"),
    M("x", 6.95, 11.00, 10.23, 10.53, ap=[P(8.30, 9.50, "S", "a", tipo="portafinestra")], nome="sud soggiorno"),
    M("y", 8.27, 10.23, 10.70, 11.00, nome="est soggiorno"),
    M("x", 10.70, 14.00, 7.97, 8.27, ap=[F(11.60, 13.20, 1.0, 2.1)], nome="sud cucina"),
    # tramezzi (0,10)
    M("x", 4.60, 11.38, 3.00, 3.10, ap=[P(4.62, 5.30, "N", "b"), P(6.20, 6.90, "N", "b"), P(9.60, 10.40, "N", "a")]),
    M("y", 0.40, 3.00, 5.32, 5.42),
    M("y", 0.40, 3.00, 7.77, 7.87),
    M("y", 0.40, 3.10, 11.28, 11.38),
    M("x", 11.38, 14.00, 2.19, 2.29, ap=[P(13.20, 13.90, "N", "b")]),
    M("x", 4.60, 14.00, 3.95, 4.05, ap=[V(5.10, 6.30), P(12.50, 13.30, "S", "b")]),
    M("y", 4.05, 7.97, 10.80, 10.90, ap=[V(5.70, 6.80)]),
    # ingresso e annesso in legno (0,10, alti 2,60)
    M("x", 14.40, 16.15, 2.24, 2.34, top=2.60, legno=True, ap=[P(14.85, 15.85, "S", "b")]),
    M("y", 2.34, 8.02, 16.05, 16.15, top=2.60, legno=True, ap=[F(4.50, 6.00, 0.9, 2.0)]),
    M("x", 14.40, 18.65, 8.02, 8.12, top=2.60, legno=True, ap=[P(14.70, 15.60, "S", "a")]),
    M("y", 8.12, 14.24, 18.55, 18.65, top=2.60, legno=True, ap=[F(10.50, 11.70, 1.0, 1.9)]),
    M("x", 14.40, 18.65, 14.24, 14.34, top=2.60, legno=True, ap=[F(15.30, 17.20, 1.0, 1.9)]),
]

# i muri del perimetro della casa salgono fino all'estradosso, a filo con il tetto e con il recinto:
# il tetto sta tra i loro fili interni
TETTI = [(0.40, 0.40, 14.00, 3.20), (4.30, 3.20, 14.00, 8.27), (4.30, 8.27, 11.00, 10.53)]
TETTI_LEGNO = [(14.40, 2.24, 16.15, 8.12), (14.40, 8.12, 18.65, 14.34)]


def rec(y):
    """Altezza del recinto: lo stesso profilo del tetto, che scende e poi risale."""
    return ze(y)


RECINTO = rec(14.40)                   # recinto sud


def top_at(m, y):
    if m["top"] == "F":
        return ze(m["c1"]) if m["asse"] == "x" else ze(y)
    if m["top"] == "E":
        return rec(14.40) if m["asse"] == "x" else rec(y)
    return zi(y) if m["top"] == "T" else m["top"]


# =====================================================================================
# Pianta quotata
# =====================================================================================
def arco(d, h, a, b, col="#777"):
    """Quarto di cerchio con centro nella cerniera h, dalla punta dell'anta a fino allo stipite b."""
    H, A, B = d.P(*h), d.P(*a), d.P(*b)
    R = math.hypot(A[0] - H[0], A[1] - H[1])
    cr = (A[0] - H[0]) * (B[1] - H[1]) - (A[1] - H[1]) * (B[0] - H[0])
    d.parti.append(f'<path d="M {A[0]:.1f} {A[1]:.1f} A {R:.1f} {R:.1f} 0 0 {1 if cr > 0 else 0} {B[0]:.1f} {B[1]:.1f}" '
                   f'fill="none" stroke="{col}" stroke-width="0.8"/>')


def disegna_muro(d, m):
    if m["pianta"] == "no":
        return
    col = LEGNO if m["legno"] else (NERO if m["c2"] - m["c1"] > 0.2 else "#444")
    X = m["asse"] == "x"

    def R(s1, s2, fill=col):
        if X:
            d.rect(s1, m["c1"], s2, m["c2"], fill)
        else:
            d.rect(m["c1"], s1, m["c2"], s2, fill)

    def L(s1, s2, c, colr="#777", sw=0.7):
        if X:
            d.line(s1, c, s2, c, colr, sw)
        else:
            d.line(c, s1, c, s2, colr, sw)

    c1, c2, cm = m["c1"], m["c2"], (m["c1"] + m["c2"]) / 2
    if m["pianta"] == "finestra":
        L(m["a1"], m["a2"], c1), L(m["a1"], m["a2"], c2), L(m["a1"], m["a2"], cm, "#777", 0.9)
        return
    if m["pianta"] == "muretto":
        R(m["a1"], m["a2"], "#d9d4cc")
        n = int((m["a2"] - m["a1"]) / 0.5)
        for i in range(n + 1):
            s = m["a1"] + 0.12 + i * (m["a2"] - m["a1"] - 0.24) / n
            R(s - 0.06, s + 0.06, LEGNO)
        return
    a = m["a1"]
    for s1, s2, tipo, z1, z2, apre, cern in sorted(m["ap"]):
        R(a, s1)
        a = s2
        if tipo in ("finestra", "portafinestra"):
            L(s1, s2, c1), L(s1, s2, c2), L(s1, s2, cm, "#777", 0.9)
        if tipo in ("porta", "portafinestra"):
            w = s2 - s1
            h, altro = (s1, s2) if cern == "a" else (s2, s1)
            if X:
                cy, sg = (c2, 1) if apre == "S" else (c1, -1)
                d.line(h, cy, h, cy + sg * w, "#555", 1.0)
                arco(d, (h, cy), (h, cy + sg * w), (altro, cy))
            else:
                cx, sg = (c2, 1) if apre == "E" else (c1, -1)
                d.line(cx, h, cx + sg * w, h, "#555", 1.0)
                arco(d, (cx, h), (cx + sg * w, h), (cx, altro))
    R(a, m["a2"])


def etichetta(d, x, y, nome, sotto, size=12):
    d.text(x, y, nome, "#222", size, bold=True)
    d.text(x, y + 0.42, sotto, "#444", size - 2)


def pianta_quotata(path):
    d = Disegno(-2.8, -2.5, 21.6, 17.0, 46, "Pianta quotata della nuova disposizione (misure in metri)")
    ZONA = {"giorno": "#f6dcc4", "notte": "#d9e3f3", "servizi": "#e8dcf1", "distr": "#e9e9e2"}
    d.rect(0.40, 0.40, 14.00, 14.00, "#eef3e8")
    for n, z, x1, y1, x2, y2 in STANZE:
        d.rect(x1, y1, x2, y2, ZONA[z])
    x1, y1, x2, y2 = SOPP
    d.rect(x1, y1, x2, y2, "none", BLU, 1.2, 'stroke-dasharray="6,4"')
    # scaletta: 10 alzate da 0,24
    sx1, sy1, sx2, sy2 = SCALA
    d.rect(sx1, sy1, sx2, sy2, "#ffffff", "#666", 0.8)
    for i in range(1, 10):
        yy = sy2 - i * (sy2 - sy1) / 10
        d.line(sx1, yy, sx2, yy, "#777", 0.6)
    d.line((sx1 + sx2) / 2, sy2 - 0.15, (sx1 + sx2) / 2, sy1 + 0.15, "#555", 0.8)
    a, b = d.P((sx1 + sx2) / 2, sy1 + 0.10)
    d.parti.append(f'<path d="M {a:.1f} {b:.1f} l -4 8 l 8 0 Z" fill="#555"/>')
    d.text(sx1 - 0.12, (sy1 + sy2) / 2 + 0.4, "scaletta", "#444", 10, anchor="end", rot=-90)
    for m in MURI:
        disegna_muro(d, m)
    # nomi
    lab = {"Camera grande": (2.9, 1.55), "Guardaroba": (6.6, 1.4), "Camera": (9.55, 1.55), "Bagno": (12.3, 1.25),
           "Disimpegno": (12.45, 2.80), "Corridoio": (7.9, 3.48), "Soggiorno, pranzo e atelier": (6.9, 8.6),
           "Cucina": (12.35, 5.75), "Ingresso (in legno)": (15.27, 5.0), "Annesso degli ospiti": (16.52, 11.0)}
    for n, z, x1, y1, x2, y2 in STANZE:
        w, h = x2 - x1, y2 - y1
        x, y = lab[n]
        if n == "Ingresso (in legno)":
            d.text(x - 0.1, y, "Ingresso", "#222", 12, bold=True, rot=-90)
            d.text(x + 0.35, y, "(legno) %s m² · %s × %s" % (num(w * h, 1), num(w), num(h)), "#444", 10, rot=-90)
            continue
        if n == "Corridoio":
            d.text(x, y + 0.1, "Corridoio · %s m² · %s × %s" % (num(w * h, 1), num(w), num(h)), "#222", 11)
            continue
        if n in ("Guardaroba", "Bagno", "Disimpegno", "Cucina"):
            d.text(x, y, n, "#222", 12, bold=True)
            d.text(x, y + 0.40, "%s m²" % num(w * h, 1), "#444", 10)
            d.text(x, y + 0.75, "%s × %s" % (num(w), num(h)), "#444", 10)
            continue
        etichetta(d, x, y, n, "%s m² · %s × %s" % (num(w * h, 1), num(w), num(h)))
    d.text(9.0, 5.0, "soppalco dello studio (+2,40)", BLU, 11)
    d.text(9.0, 5.42, "%s m² · %s × %s" % (num((SOPP[2] - SOPP[0]) * (SOPP[3] - SOPP[1]), 1),
                                             num(SOPP[2] - SOPP[0]), num(SOPP[3] - SOPP[1])), BLU, 10)
    d.text(2.4, 7.6, "PATIO", "#333", 15, bold=True)
    d.text(2.4, 8.05, "%s m² (Aalto 86,5)" % num(patio_area(), 1), "#444", 10)
    d.text(1.3, 15.25, "porta del patio", "#333", 11)
    d.text(-0.75, 10.55, "graticcio", "#333", 11, rot=-90)
    d.text(3.9, 15.25, "graticcio", "#333", 11)
    d.text(-0.75, 13.1, "porta del patio", "#333", 11, rot=-90)
    # quote esterne
    d.catena([0, 2.35, 3.30, 6.10, 7.05, 9.00, 10.20, 12.25, 13.20, 14.40], None, "x", -0.55, [BLU] * 9)
    d.catena([0, 14.40], None, "x", -1.25, [NERO])
    d.catena([0, 2.65, 5.10, 14.40], None, "x", 15.85, [BLU] * 3)
    d.catena([0, 3.20, 9.30, 11.75, 14.40], None, "y", -1.45, [BLU] * 4)
    d.catena([0, 14.40], None, "y", -2.15, [NERO])
    d.catena([0, 2.80, 3.90, 8.27], None, "y", 17.0, [BLU] * 3)
    d.catena([0, 2.24, 8.07, 14.34], None, "y", 19.5, [BLU] * 3)
    d.catena([14.40, 16.15], None, "x", 1.55, [BLU])
    d.catena([14.40, 18.65], None, "x", 15.0, [BLU])
    # quote interne (assi dei muri)
    d.catena([0.40, 5.37, 7.82, 11.33, 14.00], None, "x", 0.85, [BLU] * 4, 10)
    d.catena([0.40, 4.45, 10.85, 14.00], None, "x", 11.4, [BLU] * 3, 10)
    d.catena([0.40, 2.24, 4.00, 8.12, 14.00], None, "y", 13.7, [BLU] * 4, 10)
    d.catena([0.40, 3.05], None, "y", 0.85, [BLU], 10)
    d.catena([3.05, 4.00, 10.38, 14.00], None, "y", 6.0, [BLU] * 3, 10)
    d.text(8.6, 16.65, "Muri: recinto 0,40, muri sul patio 0,30, tramezzi 0,10, legno 0,10 (marrone). "
           "Le quote interne sono sugli assi dei muri.", "#333", 12)
    a, b = d.P(-1.9, -1.6)
    d.parti.append(f'<path d="M {a:.0f} {b - 16:.0f} L {a - 7:.0f} {b + 6:.0f} L {a:.0f} {b:.0f} L {a + 7:.0f} {b + 6:.0f} Z" fill="#333"/>')
    d.text(-1.9, -1.15, "N", "#333", 13, bold=True)
    d.text(7.2, 16.25, "verso il lago ↓", "#333", 12)
    d.salva(path)


# =====================================================================================
# Le altezze: sezione nord-sud e sezione ovest-est
# =====================================================================================
def sezioni(path):
    s = 40
    W, H = 19.5 * s + 300, 2 * 8.0 * s + 120
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="14" y="26" {FONT} font-size="17" font-weight="bold" fill="#333">Le altezze: due sezioni della nuova casa</text>']

    def blocco(oy, titolo, poligoni, quote, note, lx=-0.8, rx=19.0, sinistra="", destra="", altezze=(), linee=()):
        Pt = lambda u, z: (60 + u * s, oy - z * s)
        out.append(f'<text x="14" y="{oy - 7.2 * s:.0f}" {FONT} font-size="14" font-weight="bold" fill="#333">{titolo}</text>')
        a, b = Pt(lx, 0)
        c, _ = Pt(rx, 0)
        out.append(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{b}" stroke="#333" stroke-width="1.5"/>')
        for pts, fill in poligoni:
            dd = "M " + " L ".join("%.1f %.1f" % Pt(*q) for q in pts) + " Z"
            out.append(f'<path d="{dd}" fill="{fill}" stroke="#333" stroke-width="1"/>')
        for u, z, t, col in quote:
            a, b = Pt(u, z)
            out.append(f'<line x1="{a - 5}" y1="{b}" x2="{a + 5}" y2="{b}" stroke="{col}" stroke-width="1.2"/>')
            out.append(f'<text x="{a + 7}" y="{b + 4}" {FONT} font-size="12" fill="{col}">{t}</text>')
        for u1, z1, u2, z2 in linee:
            a, b = Pt(u1, z1)
            c, e = Pt(u2, z2)
            out.append(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{e}" stroke="#777" stroke-width="1.2" stroke-dasharray="6,4"/>')
        for u, za, zb, t in altezze:
            a, b = Pt(u, za)
            _, c = Pt(u, zb)
            out.append(f'<line x1="{a}" y1="{b}" x2="{a}" y2="{c}" stroke="{ROSSO}" stroke-width="1.2" stroke-dasharray="4,3"/>')
            out.append(f'<text x="{a - 6}" y="{(b + c) / 2 + 4}" {FONT} font-size="12" fill="{ROSSO}" text-anchor="end">{t}</text>')
        for i, t in enumerate(note):
            out.append(f'<text x="{60 + rx * s - 70}" y="{oy - 6.4 * s + i * 17:.0f}" {FONT} font-size="12" fill="#444">{t}</text>')
        a, b = Pt(lx, -0.45)
        out.append(f'<text x="{a}" y="{b}" {FONT} font-size="12" fill="#666">{sinistra}</text>')
        a, b = Pt(14.4, -0.45)
        out.append(f'<text x="{a}" y="{b}" {FONT} font-size="12" fill="#666" text-anchor="end">{destra}</text>')

    MW, MT, LG = "#555", "#bbb", "#9cc0e8"
    # 1. nord-sud a x = 9,00: camera, corridoio, soggiorno con il soppalco, patio, recinto sud
    tetto = [(0.40, ze(0.40)), (Y_S, ze(Y_S)), (Y_S, zi(Y_S)), (0.40, zi(0.40))]
    blocco(7.6 * s + 50, "1. Sezione nord-sud (a 9 m dal filo ovest): la falda scende verso il lago",
           [([(0, 0), (0.40, 0), (0.40, 0.9), (0, 0.9)], MW), ([(0, 2.1), (0.40, 2.1), (0.40, ze(0)), (0, ze(0))], MW),
            ([(3.00, 0), (3.10, 0), (3.10, zi(3.10)), (3.00, zi(3.0))], MW),
            ([(3.95, 0), (4.05, 0), (4.05, zi(4.05)), (3.95, zi(3.95))], MW),
            ([(10.23, 2.1), (10.53, 2.1), (10.53, zi(10.53)), (10.23, zi(10.23))], MW),
            ([(14.00, 0), (14.40, 0), (14.40, RECINTO), (14.00, RECINTO)], MW),
            (tetto, MT),
            ([(SOPP[1], SOPP_SOTTO), (SOPP[3], SOPP_SOTTO), (SOPP[3], SOPP_SOTTO + SOPP_SP), (SOPP[1], SOPP_SOTTO + SOPP_SP)], LG)],
           [(0, ze(0), "+%s" % f2(ze(0)), NERO), (Y_S, ze(Y_S), "+%s" % f2(ze(Y_S)), NERO), (Y_B, rec(Y_B) - 0.45, "+%s" % f2(ze(Y_B)), GRIGIO),
            (SOPP[3], SOPP_SOTTO + SOPP_SP, "+%s" % f2(SOPP_SOTTO + SOPP_SP), NERO),
            (14.40, RECINTO, "+%s recinto sud" % f2(RECINTO), NERO), (0.40, 0, "±0,00", NERO)],
           ["Il tetto è alto %s sopra le camere" % f2(ze(0)), "e scende fino a %s sul muro" % f2(ze(Y_S)),
            "sud del soggiorno. Spessore 0,30.", "Il profilo (tratteggio) continua sui", "muri del recinto: scende fino a %s" % f2(ze(Y_B)),
            "a 2,15 m dal perimetro, come Aalto,", "e risale a %s sul recinto sud."  % f2(RECINTO), "Nel punto più basso del soppalco", "restano %s m sopra la testa." % f2(zi(SOPP[3]) - SOPP_SOTTO - SOPP_SP),
            ],
           sinistra="nord (camera)", destra="sud (lago)", linee=[(Y_S, rec(Y_S), Y_B, rec(Y_B)), (Y_B, rec(Y_B), 14.40, rec(14.40))],
           altezze=[(SOPP[3] - 0.25, SOPP_SOTTO + SOPP_SP, zi(SOPP[3] - 0.25), "%s sopra il soppalco" % f2(zi(SOPP[3]) - SOPP_SOTTO - SOPP_SP)),
                    (SOPP[3] - 0.25, 0, SOPP_SOTTO, "%s sotto" % f2(SOPP_SOTTO))])
    # 2. ovest-est a y = 6,30: patio, soggiorno con il soppalco, cucina, ingresso
    y0 = 6.30
    blocco(2 * 7.6 * s + 100, "2. Sezione ovest-est (a 6,30 m dal filo nord): patio, soggiorno, cucina, ingresso",
           [([(0, 0), (0.40, 0), (0.40, rec(y0)), (0, rec(y0))], MW),
            ([(4.30, 0), (4.60, 0), (4.60, zi(y0)), (4.30, zi(y0))], MW),
            ([(10.80, 2.2), (10.90, 2.2), (10.90, zi(y0)), (10.80, zi(y0))], MW),
            ([(14.00, 0), (14.40, 0), (14.40, ze(y0)), (14.00, ze(y0))], MW),
            ([(16.05, 0), (16.15, 0), (16.15, 2.60), (16.05, 2.60)], "#8d6e4f"),
            ([(4.30, zi(y0)), (14.00, zi(y0)), (14.00, ze(y0)), (4.30, ze(y0))], MT),
            ([(14.40, 2.60), (16.15, 2.60), (16.15, 2.75), (14.40, 2.75)], "#c9b49a"),
            ([(SOPP[0], SOPP_SOTTO), (SOPP[2], SOPP_SOTTO), (SOPP[2], SOPP_SOTTO + SOPP_SP), (SOPP[0], SOPP_SOTTO + SOPP_SP)], LG)],
           [(0, rec(y0), "+%s recinto" % f2(rec(y0)), NERO), (4.30, ze(y0), "+%s" % f2(ze(y0)), NERO),
            (SOPP[0] - 2.2, SOPP_SOTTO + SOPP_SP + 0.15, "soppalco +%s" % f2(SOPP_SOTTO + SOPP_SP), NERO),
            (16.15, 2.75, "+2,75 legno", NERO), (0.40, 0, "±0,00", NERO)],
           ["Qui il tetto è orizzontale:", "la falda scende solo", "da nord verso sud.", "L'ingresso in legno è basso,",
            "come quello di Aalto."], rx=19.0, sinistra="ovest (patio)", destra="est",
           altezze=[(SOPP[0] + 0.6, SOPP_SOTTO + SOPP_SP, zi(y0), "%s sopra" % f2(zi(y0) - SOPP_SOTTO - SOPP_SP))])
    out.append("</svg>")
    with open(path, "w") as fh:
        fh.write("\n".join(out))


# =====================================================================================
# Pezzi per la pagina 3D (stessa forma dei pezzi del plastico di Aalto)
# =====================================================================================
def spigolo(m):
    """Lato alto di un muro nord-sud sotto il tetto: [fine, (punto di cambio pendenza)], in coordinate del pezzo."""
    L = m["a2"] - m["a1"]
    h = {"T": zi, "F": ze}.get(m["top"], rec)
    out = [[L, h(m["a2"]) - m["z0"]]]
    if m["asse"] == "y" and m["a1"] < Y_B < m["a2"]:
        out.append([Y_B - m["a1"], h(Y_B) - m["z0"]])
    return out


def pezzi3d():
    out = []
    for m in MURI:
        L = m["a2"] - m["a1"]
        t = m["c2"] - m["c1"]
        if m["z0"]:
            if m["asse"] == "x":
                forma = [[0, 0], [L, 0], [L, zi(m["c1"]) - m["z0"]], [0, zi(m["c1"]) - m["z0"]]]
            else:
                forma = [[0, 0], [L, 0]] + spigolo(m) + [[0, zi(m["a1"]) - m["z0"]]]
                forma[2][1] = zi(m["a2"]) - m["z0"]
        else:
            h1 = top_at(m, m["c1"] if m["asse"] == "x" else m["a1"])
            h2 = top_at(m, m["c1"] if m["asse"] == "x" else m["a2"])
            fondo = [[0, 0]]
            buchi = []
            for s1, s2, tipo, z1, z2, apre, cern in sorted(m["ap"]):
                u1, u2 = s1 - m["a1"], s2 - m["a1"]
                if z1 == 0:
                    fondo += [[u1, 0], [u1, z2], [u2, z2], [u2, 0]]
                else:
                    buchi.append([u1, z1, u2, z2])
            forma = fondo + [[L, 0], [L, h2]] + (spigolo(m)[1:] if m["top"] in ("T", "E", "F") else []) + [[0, h1]]
        p = {"cod": m["nome"] or "muro", "kind": m["asse"], "passo": 1, "t": t, "z0": m["z0"], "forma": forma,
             "buchi": [] if m["z0"] else buchi, "legno": m["legno"]}
        if m["asse"] == "x":
            p.update(x0=m["a1"], y0=m["c1"])
        else:
            p.update(x0=m["c1"], y0=m["a1"])
        out.append(p)
    # graticci: montanti 0,12 x 0,12 ogni 0,5 circa, e due traversi
    for m in MURI:
        if m["pianta"] != "muretto":
            continue
        n = int((m["a2"] - m["a1"]) / 0.5)
        cm = (m["c1"] + m["c2"]) / 2
        for i in range(n + 1):
            s = m["a1"] + 0.12 + i * (m["a2"] - m["a1"] - 0.24) / n
            hz = rec(s if m["asse"] == "y" else m["c1"]) - MURETTO
            q = {"cod": "G", "kind": m["asse"], "passo": 1, "t": 0.12, "z0": MURETTO, "legno": True, "buchi": [],
                 "forma": [[0, 0], [0.12, 0], [0.12, hz], [0, hz]]}
            if m["asse"] == "x":
                q.update(x0=s - 0.06, y0=cm - 0.06)
            else:
                q.update(x0=cm - 0.06, y0=s - 0.06)
            out.append(q)
        L = m["a2"] - m["a1"]
        r1, r2 = (rec(m["a1"]), rec(m["a2"])) if m["asse"] == "y" else (rec(14.40),) * 2
        for forma in ([[0, 2.90], [L, 2.90], [L, 3.02], [0, 3.02]], [[0, r1 - 0.12], [L, r2 - 0.12], [L, r2], [0, r1]]):
            q = {"cod": "G", "kind": m["asse"], "passo": 1, "t": 0.12, "z0": 0.0, "legno": True, "buchi": [], "forma": forma}
            if m["asse"] == "x":
                q.update(x0=m["a1"], y0=cm + 0.06)
            else:
                q.update(x0=cm + 0.06, y0=m["a1"])
            out.append(q)
    for x1, y1, x2, y2 in TETTI:
        out.append({"cod": "tetto", "kind": "piano", "passo": 10, "t": SP_TETTO,
                    "d3": [[x1, y1, zi(y1)], [x2, y1, zi(y1)], [x2, y2, zi(y2)], [x1, y2, zi(y2)]]})
    for x1, y1, x2, y2 in TETTI_LEGNO:
        out.append({"cod": "tetto legno", "kind": "piano", "passo": 10, "t": 0.15, "legno": True,
                    "d3": [[x1, y1, 2.60], [x2, y1, 2.60], [x2, y2, 2.60], [x1, y2, 2.60]]})
    x1, y1, x2, y2 = SOPP
    out.append({"cod": "soppalco", "kind": "piano", "passo": 7, "t": SOPP_SP,
                "d3": [[x1, y1, SOPP_SOTTO], [x2, y1, SOPP_SOTTO], [x2, y2, SOPP_SOTTO], [x1, y2, SOPP_SOTTO]]})
    return out


def controlli():
    print("patio %.2f m2 (Aalto 86,5, -5%% = 82,2)" % patio_area())
    for n, z, x1, y1, x2, y2 in STANZE:
        a = (x2 - x1) * (y2 - y1)
        if n in AALTO:
            print("%-28s %5.2f  Aalto %5.2f  %+.1f%%" % (n, a, AALTO[n], 100 * (a / AALTO[n] - 1)))
    print("soppalco %.2f m2" % ((SOPP[2] - SOPP[0]) * (SOPP[3] - SOPP[1])))
    print("sopra il soppalco nel punto piu' basso: %.2f m" % (zi(SOPP[3]) - SOPP_SOTTO - SOPP_SP))
    print("alzata scaletta: %.3f, pedata %.3f" % ((SOPP_SOTTO + SOPP_SP) / 10, (SCALA[3] - SCALA[1]) / 10))


if __name__ == "__main__":
    controlli()
    pianta_quotata(OUT + "muuratsalo-nadia-%s-1-pianta-quotata.svg" % VER)
    sezioni(OUT + "muuratsalo-nadia-%s-2-altezze.svg" % VER)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as fh:
            json.dump(pezzi3d(), fh)
