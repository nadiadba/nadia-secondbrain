"""Disegni per la pagina «PO 1b - I prospetti, spiegati bene».

Edificio a L: blocco alto (x 95-270, profondita' 0-150, altezza 135) e blocco basso arretrato
(x 0-95, profondita' 40-150 dal lato nord, altezza 80). In pianta il nord e' in alto.
1) l'edificio in 3D con i quattro lati;  2) la pianta con chi guarda ogni lato;
3) i quattro prospetti intorno alla pianta, ognuno dalla parte di chi lo guarda (LT dalla sua parte,
   prospetto appeso alla LT verso la pianta), come vuole la docente.
"""
BZ = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/bozze/img/"
VERDE, ROSSO, BLU, GRIGIO = "#2e7d32", "#c0392b", "#2b5c9e", "#888"
COL = {"alto": "#c0392b", "basso": "#2e7d32", "sinistra": "#2b5c9e", "destra": "#b7791f"}


class Svg:
    def __init__(self, w, h, titolo):
        self.w, self.h, self.p = w, h, []
        self.t(12, 28, titolo, 16, "#333", "start", True)

    def poly(self, pts, fill="#fff", stroke="#222", sw=2, op=1):
        self.p.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" '
                      f'fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')

    def line(self, a, b, stroke="#222", sw=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.p.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def t(self, x, y, s, size=13, col="#333", anchor="middle", bold=False, rot=0):
        w = ' font-weight="bold"' if bold else ""
        r = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot else ""
        self.p.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" '
                      f'fill="{col}" text-anchor="{anchor}"{w}{r}>{s}</text>')

    def omino(self, x, y, dx, dy, col=VERDE):
        """Persona vista dall'alto (pallino) con la freccia nella direzione in cui guarda."""
        self.p.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{col}"/>')
        a, b = (x + dx * 12, y + dy * 12), (x + dx * 42, y + dy * 42)
        self.line(a, b, col, 2.5)
        px, py = -dy, dx
        self.line((b[0] - dx * 8 + px * 6, b[1] - dy * 8 + py * 6), b, col, 2.5)
        self.line((b[0] - dx * 8 - px * 6, b[1] - dy * 8 - py * 6), b, col, 2.5)

    def salva(self, nome):
        open(BZ + nome, "w").write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">'
            f'<rect width="100%" height="100%" fill="#fff"/>' + "".join(self.p) + "</svg>")


# pianta: x verso destra (est), y verso il basso (sud); nord in alto
PIANTA = [(0, 40), (95, 40), (95, 0), (270, 0), (270, 150), (0, 150)]

# ---------------------------------------------------------------- 1. l'edificio in 3D
def edificio_3d():
    f = Svg(760, 470, "1. L'edificio: ogni lato della pianta è una facciata")
    ox, oy = 250, 400

    def s(x, n, h):            # n = distanza dal lato sud (0 = sud, 150 = nord); vista da sud-ovest, dall'alto
        return (ox + x - 0.55 * n, oy - h - 0.45 * n)

    def blocco(x0, x1, n0, n1, h, colsud, colovest):
        f.poly([s(x0, n0, 0), s(x1, n0, 0), s(x1, n0, h), s(x0, n0, h)], colsud, "#222", 2)       # sud
        f.poly([s(x0, n0, 0), s(x0, n1, 0), s(x0, n1, h), s(x0, n0, h)], colovest, "#222", 2)    # ovest
        f.poly([s(x0, n0, h), s(x1, n0, h), s(x1, n1, h), s(x0, n1, h)], "#eee", "#222", 2)           # tetto

    blocco(95, 270, 0, 150, 135, "#cfe6d1", "#d3dff0")
    blocco(0, 95, 0, 110, 80, "#cfe6d1", "#d3dff0")
    f.poly([s(160, 0, 0), s(190, 0, 0), s(190, 0, 50), s(160, 0, 50)], "#fff", "#222", 1.5)          # porta
    f.t(*s(180, 0, -22), "lato in basso (sud): lo vedi tu", 13, COL["basso"])
    f.t(*s(-35, 55, 40), "lato a sinistra", 13, COL["sinistra"], "end")
    f.t(*s(-35, 55, 22), "(ovest)", 12, COL["sinistra"], "end")
    a = s(180, 150, 135)
    f.t(a[0], a[1] - 30, "lato in alto (nord): dietro, non si vede", 13, COL["alto"])
    b = s(270, 75, 135)
    f.t(b[0] + 60, b[1] + 40, "lato a destra (est):", 13, COL["destra"], "start")
    f.t(b[0] + 60, b[1] + 56, "dall'altra parte", 13, COL["destra"], "start")
    f.t(*s(30, 135, 92), "rientranza", 12, "#555")
    f.salva("b03-prospetti-1-edificio.svg")


# ---------------------------------------------------------------- 2. la pianta con chi guarda
def pianta_osservatori():
    f = Svg(760, 520, "2. La pianta e le quattro persone che guardano i quattro lati")
    ox, oy = 245, 185

    def s(p):
        return (ox + p[0], oy + p[1])

    f.poly([s(p) for p in PIANTA], "#e6e7ea")
    f.poly([s(p) for p in [(160, 150), (190, 150), (190, 146), (160, 146)]], "#fff", "#222", 1)
    f.t(*s((150, 90)), "pianta", 15)
    f.t(*s((47, 30)), "rientranza", 11, "#555")
    lati = [("alto", [(0, 40), (95, 40), (95, 0), (270, 0)]), ("basso", [(0, 150), (270, 150)]),
            ("sinistra", [(0, 40), (0, 150)]), ("destra", [(270, 0), (270, 150)])]
    for nome, pts in lati:
        for a, b in zip(pts, pts[1:]):
            f.line(s(a), s(b), COL[nome], 5)
    f.omino(ox + 182, oy - 95, 0, 1, COL["alto"]);   f.t(ox + 182, oy - 108, "chi guarda il lato in alto", 13, COL["alto"])
    f.t(ox + 182, oy - 124, "(sta dall'altra parte del foglio)", 12, COL["alto"])
    f.omino(ox + 135, oy + 245, 0, -1, COL["basso"]); f.t(ox + 135, oy + 275, "chi guarda il lato in basso: tu", 13, COL["basso"])
    f.omino(ox - 95, oy + 95, 1, 0, COL["sinistra"]); f.t(ox - 95, oy + 130, "chi guarda il lato", 13, COL["sinistra"]); f.t(ox - 95, oy + 146, "a sinistra", 13, COL["sinistra"])
    f.omino(ox + 365, oy + 75, -1, 0, COL["destra"]); f.t(ox + 365, oy + 110, "chi guarda il lato", 13, COL["destra"]); f.t(ox + 365, oy + 126, "a destra", 13, COL["destra"])
    f.t(380, 505, "Ognuno sta fuori dall'edificio, davanti al suo lato, e guarda verso la pianta.", 13, "#333")
    f.salva("b03-prospetti-2-chi-guarda.svg")


# ---------------------------------------------------------------- 3. i quattro prospetti intorno alla pianta
# ogni prospetto in coordinate di chi guarda: u da sinistra a destra (per lui), v in altezza
PROSPETTI = {
    "basso": dict(W=270, parti=[((0, 95), 80), ((95, 270), 135)], foro=((160, 190), (0, 50))),        # porta
    "alto": dict(W=270, parti=[((0, 175), 135), ((175, 270), 80)], foro=((60, 110), (70, 100))),
    "sinistra": dict(W=150, parti=[((0, 150), 135), ((40, 150), 80)], foro=((80, 110), (35, 60))),
    "destra": dict(W=150, parti=[((0, 150), 135)], foro=((50, 100), (70, 100))),
}


def quattro_prospetti():
    f = Svg(900, 900, "3. I quattro prospetti: ognuno dalla parte di chi lo guarda")
    px0, py0, g, H = 315, 375, 30, 135
    px1, py1 = px0 + 270, py0 + 150

    def mappa(nome, u, v):
        if nome == "basso":
            return (px0 + u, py1 + g + H - v)
        if nome == "alto":
            return (px1 - u, py0 - g - H + v)
        if nome == "sinistra":
            return (px0 - g - H + v, py0 + u)
        return (px1 + g + H - v, py1 - u)            # destra

    f.poly([(px0 + x, py0 + y) for x, y in PIANTA], "#e6e7ea")
    f.t(px0 + 150, py0 + 95, "pianta", 15)
    for nome, d in PROSPETTI.items():
        c = COL[nome]
        for (u0, u1), h in d["parti"]:
            f.poly([mappa(nome, u0, 0), mappa(nome, u1, 0), mappa(nome, u1, h), mappa(nome, u0, h)], "#fff", c, 2)
        (u0, u1), (v0, v1) = d["foro"]
        f.poly([mappa(nome, u0, v0), mappa(nome, u1, v0), mappa(nome, u1, v1), mappa(nome, u0, v1)], "#d6e4f0", c, 1.2)
        a, b = mappa(nome, -25, 0), mappa(nome, d["W"] + 25, 0)
        f.line(a, b, "#222", 2.4)                                   # LT, dalla parte di chi guarda
    # linee di richiamo dalla pianta
    for x in (0, 95, 270):
        f.line((px0 + x, py1), (px0 + x, py1 + g), GRIGIO, 1, "4,4")
        f.line((px0 + x, py0 if x else py0 + 40), (px0 + x, py0 - g), GRIGIO, 1, "4,4")
    for y in (0, 40, 150):
        f.line((px0, py0 + y), (px0 - g, py0 + y), GRIGIO, 1, "4,4")
    for y in (0, 150):
        f.line((px1, py0 + y), (px1 + g, py0 + y), GRIGIO, 1, "4,4")
    # chi guarda, oltre la LT
    f.omino(px0 + 135, py1 + g + H + 45, 0, -1, COL["basso"]);  f.t(px0 + 135, py1 + g + H + 120, "tu: il prospetto in basso è dritto", 13, COL["basso"])
    f.omino(px0 + 135, py0 - g - H - 45, 0, 1, COL["alto"]);    f.t(px0 + 135, py0 - g - H - 62, "per chi sta di là è dritto; per te è a testa in giù", 13, COL["alto"])
    f.omino(px0 - g - H - 45, py0 + 75, 1, 0, COL["sinistra"]); f.t(px0 - g - H - 50, py0 + 120, "giralo verso", 12, COL["sinistra"]); f.t(px0 - g - H - 50, py0 + 136, "sinistra", 12, COL["sinistra"])
    f.omino(px1 + g + H + 45, py0 + 75, -1, 0, COL["destra"]);  f.t(px1 + g + H + 50, py0 + 120, "giralo verso", 12, COL["destra"]); f.t(px1 + g + H + 50, py0 + 136, "destra", 12, COL["destra"])
    f.t(450, 880, "Regola: la LT sta sempre dalla parte di chi guarda, e il prospetto «pende» dalla LT verso la pianta.", 13, "#333")
    f.salva("b03-prospetti-3-intorno-alla-pianta.svg")


edificio_3d()
pianta_osservatori()
quattro_prospetti()
print("ok")
