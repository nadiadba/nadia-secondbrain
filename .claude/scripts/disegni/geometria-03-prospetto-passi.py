"""Disegno in tre passaggi: perché il prospetto del lato in alto della pianta si disegna a testa in giù.
Coordinate SVG (y verso il basso). Immagine: anno-1/.../appunti/../bozze/img/b03-prospetto-tre-passi.svg"""
BZ = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"
P = []


def poly(pts, ox, fill="#e6e7ea", stroke="#222", sw=2):
    P.append(f'<polygon points="{" ".join(f"{x+ox:.0f},{y:.0f}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(a, b, ox, stroke="#222", sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    P.append(f'<line x1="{a[0]+ox}" y1="{a[1]}" x2="{b[0]+ox}" y2="{b[1]}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def text(x, y, s, ox, size=13, col="#333", anchor="middle", bold=False):
    w = ' font-weight="bold"' if bold else ""
    P.append(f'<text x="{x+ox}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" fill="{col}" text-anchor="{anchor}"{w}>{s}</text>')


def omino(x, y, ox, giu=True):
    """Persona vista dall'alto: testa e freccia nella direzione in cui guarda."""
    P.append(f'<circle cx="{x+ox}" cy="{y}" r="9" fill="#2e7d32"/>')
    d = 1 if giu else -1
    line((x, y + 12 * d), (x, y + 48 * d), ox, "#2e7d32", 2.5)
    line((x - 7, y + 40 * d), (x, y + 48 * d), ox, "#2e7d32", 2.5)
    line((x + 7, y + 40 * d), (x, y + 48 * d), ox, "#2e7d32", 2.5)


PIANTA = [(0, 340), (95, 340), (95, 300), (270, 300), (270, 450), (0, 450)]   # rientranza in alto a sinistra
ROSSO = "#c0392b"
W, H = 980, 640

# ---------- 1. chi guarda
ox = 25
text(135, 70, "1. Chi guarda il lato in alto", ox, 15, "#222", bold=True)
text(135, 90, "sta fuori, sopra la pianta, e guarda verso il basso", ox, 12)
omino(135, 170, ox, True)
text(135, 150, "chi guarda", ox, 12, "#2e7d32")
text(20, 250, "← la sua destra", ox, 12, ROSSO, "start")
text(250, 250, "la sua sinistra →", ox, 12, "#555", "end")
poly(PIANTA, ox)
text(135, 400, "pianta", ox, 14)
text(47, 330, "rientranza", ox, 11, ROSSO)
text(135, 490, "La rientranza, per lui, è a destra", ox, 12, ROSSO)
text(135, 508, "(sul foglio sembra a sinistra perché", ox, 12, "#555")
text(135, 524, "lui è girato verso di te)", ox, 12, "#555")

# ---------- 2. si disegna dalla sua parte
ox = 350
text(135, 70, "2. Si disegna dalla sua parte", ox, 15, "#222", bold=True)
text(135, 90, "LT in alto, prospetto appeso alla LT", ox, 12)
line((-10, 150), (290, 150), ox, "#222", 2.4); text(-10, 142, "LT", ox, 13, "#222", "start")
poly([(0, 150), (95, 150), (95, 230), (0, 230)], ox, "#ffffff")
poly([(95, 150), (270, 150), (270, 285), (95, 285)], ox, "#ffffff")
poly([(30, 165), (65, 165), (65, 195), (30, 195)], ox, "#d6e4f0", "#222", 1)
poly([(160, 180), (215, 180), (215, 220), (160, 220)], ox, "#d6e4f0", "#222", 1)
for x in (0, 95, 270):
    line((x, 150), (x, 300 if x else 340), ox, "#999", 1, "5,4")
text(47, 245, "rientranza", ox, 11, ROSSO)
poly(PIANTA, ox)
text(135, 400, "pianta", ox, 14)
text(135, 490, "Dal tuo posto il prospetto", ox, 12, "#555")
text(135, 506, "è a testa in giù: è giusto così", ox, 12, "#555")

# ---------- 3. gira il foglio
ox = 675
text(135, 70, "3. Gira il foglio", ox, 15, "#222", bold=True)
text(135, 90, "ora sei tu al posto di chi guarda", ox, 12)
def g(p):   # rotazione di 180° del disegno 2 intorno al centro (135, 300)
    return (270 - p[0], 600 - p[1])
poly([g(p) for p in PIANTA], ox)
text(135, 220, "pianta", ox, 14)
for x in (0, 95, 270):
    a, b = g((x, 150)), g((x, 300 if x else 340))
    line(a, b, ox, "#999", 1, "5,4")
poly([g(p) for p in [(0, 150), (95, 150), (95, 230), (0, 230)]], ox, "#ffffff")
poly([g(p) for p in [(95, 150), (270, 150), (270, 285), (95, 285)]], ox, "#ffffff")
poly([g(p) for p in [(30, 165), (65, 165), (65, 195), (30, 195)]], ox, "#d6e4f0", "#222", 1)
poly([g(p) for p in [(160, 180), (215, 180), (215, 220), (160, 220)]], ox, "#d6e4f0", "#222", 1)
line((-10, 450), (290, 450), ox, "#222", 2.4); text(290, 470, "LT", ox, 13, "#222", "end")
text(223, 362, "rientranza", ox, 11, ROSSO)
omino(135, 560, ox, False)
text(135, 600, "tu", ox, 12, "#2e7d32")
text(135, 620, "Il prospetto è dritto e la rientranza è a destra:", ox, 12, ROSSO)
text(135, 636, "è proprio quello che vede chi guarda quel lato", ox, 12, ROSSO)

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H+10}" width="{W}" height="{H+10}">'
       f'<rect width="100%" height="100%" fill="#ffffff"/>'
       f'<text x="12" y="28" font-family="Helvetica, Arial, sans-serif" font-size="16" font-weight="bold" fill="#333">'
       f'Perché il prospetto del lato in alto si disegna a testa in giù</text>' + "".join(P) + "</svg>")
open(BZ + "b03-prospetto-tre-passi.svg", "w").write(svg)
print("ok")
