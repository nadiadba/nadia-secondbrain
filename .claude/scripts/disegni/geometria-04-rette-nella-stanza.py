"""Sette disegnini: le rette nelle varie posizioni dentro la «stanza» dei piani di proiezione.
pi1 = pavimento (y = 0), pi2 = parete di fronte (z = 0), pi3 = parete di lato (x = 160).
Immagini: bozze/img/b04-retta-stanza-N.svg"""
BZ = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"
W, H, D = 160, 120, 120
OX, OY = 75, 150


def s(x, y, z):
    return (OX + x - 0.5 * z, OY - y + 0.38 * z)


def poly(pts, fill, op=1):
    return (f'<polygon points="{" ".join("%.1f,%.1f" % s(*p) for p in pts)}" fill="{fill}" fill-opacity="{op}" '
            f'stroke="#777" stroke-width="1"/>')


def seg(a, b, col, sw, dash=None):
    (x1, y1), (x2, y2) = s(*a), s(*b)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{d}/>'


def txt(p, t, dx=0, dy=0, size=12, col="#666"):
    x, y = s(*p)
    return f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" fill="{col}">{t}</text>'


RETTE = [
    ("proiettante in prima", (60, 0, 60), (60, 112, 60)),
    ("proiettante in seconda", (80, 62, 0), (80, 62, 118)),
    ("parallela alla LT", (12, 55, 60), (150, 55, 60)),
    ("frontale", (20, 8, 40), (135, 105, 40)),
    ("orizzontale", (15, 40, 110), (145, 40, 15)),
    ("di profilo", (110, 8, 112), (110, 105, 8)),
    ("generica", (20, 12, 112), (145, 108, 18)),
]

for i, (nome, a, b) in enumerate(RETTE, 1):
    p = []
    p.append(poly([(0, 0, 0), (W, 0, 0), (W, 0, D), (0, 0, D)], "#e8e8e8"))          # pavimento pi1
    p.append(poly([(0, 0, 0), (W, 0, 0), (W, H, 0), (0, H, 0)], "#dfe8f3"))          # parete di fronte pi2
    p.append(poly([(W, 0, 0), (W, 0, D), (W, H, D), (W, H, 0)], "#efe4d2", 0.55))     # parete di lato pi3
    p.append(txt((8, 0, D), "π₁", 2, -4)); p.append(txt((8, H, 0), "π₂", 2, 14)); p.append(txt((W, 0, D), "π₃", 4, -10))
    # ombra sul pavimento (prima proiezione) per far capire la posizione
    p.append(seg((a[0], 0, a[2]), (b[0], 0, b[2]), "#999", 1.4, "4,3"))
    p.append(seg(a, b, "#c0392b", 3.2))
    if i in (1, 2):                                   # il punto in cui la retta tocca il piano
        x, y = s(*a)
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#c0392b"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 225" width="260" height="225">'
           f'<rect width="100%" height="100%" fill="#fff"/>' + "".join(p) +
           f'<text x="125" y="216" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#c0392b">{nome}</text></svg>')
    open(BZ + f"b04-retta-stanza-{i}.svg", "w").write(svg)
print("ok")
