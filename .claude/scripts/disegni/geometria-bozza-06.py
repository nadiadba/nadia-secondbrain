"""Schemi per la bozza di studio della lezione del 20 ottobre (piani ausiliari e perpendicolarita').

Due gruppi di immagini:
- costruzioni fatte alla lavagna che mancavano nella sbobina -> sbobine/img/06-*.svg (file nuovi);
- schemi della sola bozza (versioni ridisegnate, viste nello spazio, disegni proposti) -> bozze/img/b06-*.svg.
Non modifica la libreria ne' gli schemi gia' esistenti."""
import math
import os
import sys

sys.path.insert(0, "/Users/nadia/Documents/GitHub/nadia-secondbrain/.claude/scripts")
from disegni_monge import (Figura, Triedro, P1, P2, tracce_retta, piano, interseca,
                           direzione, perpendicolare, COLORI)

GEO = "/Users/nadia/Documents/GitHub/nadia-secondbrain/anno-1/semestre-1/geometria-descrittiva/"
SBOB = GEO + "sbobine/img/"
BOZ = GEO + "bozze/img/"
os.makedirs(BOZ, exist_ok=True)


def nuovo(percorso):
    """Per la sbobina: non sovrascrivere mai un'immagine che c'era gia' prima di questo script."""
    nome = os.path.basename(percorso)
    if percorso.startswith(SBOB) and nome not in NUOVI_SBOBINA:
        raise SystemExit("nome non previsto per la sbobina: " + nome)
    return percorso


NUOVI_SBOBINA = {
    "06-orizzontale-nel-triangolo.svg",
    "06-tracce-dal-triangolo-generico.svg",
    "06-triangolo-piano-proiettante-in-prima.svg",
    "06-solidi-piramide-prisma-parallelepipedo.svg",
    "06-solido-base-nel-piano-generico.svg",
    "06-spazio-piano-mobile.svg",
}


def lungo(p, d, l):
    return (p[0] + d[0] * l, p[1] + d[1] * l)


def pt_su(p, q, t):
    return tuple(p[i] + (q[i] - p[i]) * t for i in range(len(p)))


def piano_per(p, d1, d2):
    q = tuple(p[i] + d1[i] for i in range(3)); r = tuple(p[i] + d2[i] for i in range(3))
    return piano(p, q, r)


def polilinea3d(t, punti, colore="grigio", spessore=1, tratteggio="3,3"):
    pts = " ".join("{:.1f},{:.1f}".format(*t._p(p)) for p in punti)
    dash = f' stroke-dasharray="{tratteggio}"' if tratteggio else ""
    t.f.parti.append(f'<polyline points="{pts}" fill="none" stroke="{COLORI.get(colore, colore)}" '
                     f'stroke-width="{spessore}"{dash}/>')


def angolo_retto3d(t, v, d1, d2, lato=12):
    a = tuple(v[i] + d1[i] * lato for i in range(3))
    c = tuple(v[i] + d2[i] * lato for i in range(3))
    b = tuple(a[i] + d2[i] * lato for i in range(3))
    t.segmento(a, b, "nero", 1); t.segmento(b, c, "nero", 1)


def unit(v):
    l = math.sqrt(sum(x * x for x in v))
    return tuple(x / l for x in v)


# Il triangolo "generico" della lavagna: piano z = 0.6 (x - 30) - y, tracce che partono da K = (30, 0)
def zg(x, y):
    return 0.6 * (x - 30) - y


GA = (200, 55, zg(200, 55))     # quota 47 (vertice di mezzo)
GB = (250, 25, zg(250, 25))     # quota 107
GC = (300, 140, zg(300, 140))   # quota 22
KG = (30, 0)

# ======================================================================
# 1. L'orizzontale nella figura piana (forma tecnica) -> sbobina
# ======================================================================
f = Figura(560, 420, 190, "Forma tecnica: l'orizzontale o del triangolo ABC (per A e per H su BC)", x0=-70)
f.lt(90, 600)
f.figura([P2(GA), P2(GB), P2(GC)], "blu"); f.figura([P1(GA), P1(GB), P1(GC)], "blu")
tH = (GA[2] - GB[2]) / (GC[2] - GB[2])
H = pt_su(GB, GC, tH)
f.retta((130, GA[2]), (370, GA[2]), "arancio"); f.testo((370, GA[2]), "o₂", 6, 4, "arancio")
do = direzione(P1(GA), P1(H))
f.retta(lungo(P1(GA), do, -60), lungo(P1(GA), do, 190), "arancio"); f.testo(lungo(P1(GA), do, 190), "o₁", 6, 4, "arancio")
Pp = pt_su(GA, H, 0.5)
for p in (GA, GB, GC, H, Pp):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
f.punto(P2(GA), "A₂", -26, -6); f.punto(P1(GA), "A₁", -26, -4)
f.punto(P2(GB), "B₂", -8, -10); f.punto(P1(GB), "B₁", -10, -8)
f.punto(P2(GC), "C₂", 8, 6); f.punto(P1(GC), "C₁", 8, 14)
f.punto(P2(H), "H₂", 8, -8, "arancio"); f.punto(P1(H), "H₁", 10, 0, "arancio")
f.punto(P2(Pp), "P₂", -8, -8, "rosso"); f.punto(P1(Pp), "P₁", -8, 18, "rosso")
f.nota(16, 394, "o₂ ∥ LT per A₂; H₂ = o₂ ∩ B₂C₂; H₁ sta su B₁C₁ (richiamo); o₁ = A₁H₁.")
f.nota(16, 412, "Ogni punto dell'orizzontale, come P, appartiene al piano del triangolo.")
f.salva(nuovo(SBOB + "06-orizzontale-nel-triangolo.svg"))

# ======================================================================
# 2. Dalle proiezioni del triangolo alle tracce del piano -> sbobina
# ======================================================================
k = 1.3   # stesso triangolo, ingrandito per far stare le scritte
SA_, SB_, SC_ = [tuple(c * k for c in p) for p in (GA, GB, GC)]
KG2 = (30 * k, 0)
f = Figura(700, 610, 270, "Dal triangolo alle tracce del piano: le tracce dei lati stanno sulle tracce del piano", x0=10)
f.lt(0, 680)
lati = [("r", SA_, SB_, "rosso"), ("s", SB_, SC_, "verde"), ("m", SA_, SC_, "viola")]
T = {}
for nome, p, q, col in lati:
    T1, T2 = tracce_retta(p, q)
    T[nome] = (T1, T2)
# tracce del piano (sottili sotto i lati), da K fino oltre l'ultima traccia
t1_fine = (535, -0.6 * (535 - 39)); t2_fine = (445, 0.6 * (445 - 39))
f.traccia(KG2, t1_fine); f.testo(t1_fine, "t_1α", 6, 6)
f.traccia(KG2, t2_fine); f.testo(t2_fine, "t_2α", 4, 4)
for nome, p, q, col in lati:
    T1, T2 = T[nome]
    # seconda proiezione: da T2 (traccia vera, su pi2) a (T1)2 sulla LT
    f.retta(P2(T2), (T1[0], 0), col, 1.3)
    # prima proiezione: da T1 (su pi1) a (T2)1 sulla LT
    f.retta(P1(T1), (T2[0], 0), col, 1.3)
    f.richiamo(T1[0], 0, P1(T1)[1]); f.richiamo(T2[0], 0, P2(T2)[1])
f.figura([P2(SA_), P2(SB_), P2(SC_)], "blu"); f.figura([P1(SA_), P1(SB_), P1(SC_)], "blu")
for p in (SA_, SB_, SC_):
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
f.punto(P2(SA_), "A₂", -24, 14); f.punto(P1(SA_), "A₁", -26, 4)
f.punto(P2(SB_), "B₂", 8, 12); f.punto(P1(SB_), "B₁", 8, 14)
f.punto(P2(SC_), "C₂", 8, -10); f.punto(P1(SC_), "C₁", -26, -4)
# etichette delle tracce dei lati
T1r, T2r = T["r"]; T1s, T2s = T["s"]; T1m, T2m = T["m"]
f.punto(P1(T1r), "T_{1r}", -40, 6, "rosso"); f.punto((T1r[0], 0), "(T_{1r})₂", 0, 20, "rosso")
f.punto(P2(T2r), "T_{2r}", 8, 6, "rosso"); f.punto((T2r[0], 0), "(T_{2r})₁", -20, 20, "rosso")
f.punto(P1(T1s), "T_{1s}", -44, 18, "verde"); f.punto((T1s[0], 0), "(T_{1s})₂", 6, 20, "verde")
f.punto(P2(T2s), "T_{2s}", -42, -4, "verde"); f.punto((T2s[0], 0), "(T_{2s})₁", -50, 20, "verde")
f.punto(P1(T1m), "T_{1m}", -50, 20, "viola"); f.punto((T1m[0], 0), "(T_{1m})₂", 2, -8, "viola")
f.punto(P2(T2m), "T_{2m}", -44, -6, "viola"); f.punto((T2m[0], 0), "(T_{2m})₁", -64, 20, "viola")
f.punto(KG2, None)
f.nota(16, 584, "r ⊃ AB, s ⊃ BC, m ⊃ AC: tre rette generiche. t₁α unisce le prime tracce, t₂α le seconde;")
f.nota(16, 602, "le due tracce si incontrano sulla LT; la terza retta m serve da controllo.")
f.salva(nuovo(SBOB + "06-tracce-dal-triangolo-generico.svg"))

# ======================================================================
# 3. Il triangolo dell'esercizio (AB orizzontale, AC frontale, BC di profilo)
#    a) nel piano generico (versione per la bozza)   b) nel proiettante in prima (sbobina)
# ======================================================================
EA, EB, EC = (180, 40, 70), (300, 110, 70), (300, 40, 160)
T1o, T2o = tracce_retta(EA, EB)       # orizzontale: T1 all'infinito
T1f, T2f = tracce_retta(EA, EC)       # frontale: T2 all'infinito
f = Figura(600, 430, 220, "Esercizio: AB orizzontale, AC frontale, BC di profilo → le tracce del piano γ", x0=50)
f.lt(-40, 520)
dO = direzione(P1(EA), P1(EB)); dF = direzione(P2(EA), P2(EC))
K = interseca(P2(T2o), lungo(P2(T2o), dF, 1), (0, 0), (1, 0))
t2_fine = lungo(K, dF, 260); t1_fine = lungo(K, dO, 300)
f.traccia(K, t2_fine); f.testo(t2_fine, "t_2γ ∥ f₂", -84, -2)
f.traccia(K, t1_fine); f.testo(t1_fine, "t_1γ ∥ o₁", -4, 18)
f.figura([P2(EA), P2(EB), P2(EC)], "blu"); f.figura([P1(EA), P1(EB), P1(EC)], "blu")
# orizzontale o (per A e B)
f.retta(P2(T2o), (400, 70), "arancio"); f.testo((400, 70), "o₂", 6, 4, "arancio")
o1a = (T2o[0], 0)
f.retta(o1a, lungo(o1a, dO, 290), "arancio"); f.testo(lungo(o1a, dO, 290), "o₁  T_{1o}∞", 6, 4, "arancio")
f.richiamo(T2o[0], 0, 70)
f.punto(P2(T2o), "T_{2o}", -46, -6); f.punto(o1a, "(T_{2o})₁", 2, 18)
# frontale f (per A e C)
f.retta(P1(T1f), (400, -40), "verde"); f.testo((400, -40), "f₁", 6, 4, "verde")
f1a = (T1f[0], 0)
f.retta(f1a, lungo(f1a, dF, 310), "verde"); f.testo(lungo(f1a, dF, 310), "f₂  T_{2f}∞", 6, 2, "verde")
f.richiamo(T1f[0], 0, -40)
f.punto(f1a, "(T_{1f})₂", -40, -10); f.punto(P1(T1f), "T_{1f}", -38, 20)
for p, nome, dx2, dy2, dx1, dy1 in [(EA, "A", -10, -10, -8, 20), (EB, "B", 8, 16, 8, 14), (EC, "C", 10, 4, 8, -4)]:
    f.richiamo(p[0], P2(p)[1], P1(p)[1])
    f.punto(P2(p), nome + "₂", dx2, dy2); f.punto(P1(p), nome + "₁", dx1, dy1)
f.testo((300, 115), "retta di profilo", 8, 0, "grigio", 11, False)
f.nota(16, 422, "BC è di profilo: le sue tracce si trovano solo con la terza proiezione, ma bastano o e f.")
f.salva(BOZ + "b06-triangolo-lato-di-profilo.svg")

# b) lo stesso triangolo nel piano delta proiettante in prima
f = Figura(560, 400, 190, "La stessa figura nel piano δ proiettante in prima", x0=30)
f.lt(-10, 500)
Kd = (100, 0); dd = direzione(Kd, (460, -150))
f.traccia(Kd, (100, 175)); f.testo((100, 175), "t_2δ", 6, 6)
f.traccia(Kd, lungo(Kd, dd, 360)); f.testo(lungo(Kd, dd, 360), "t_1δ", 6, 6)
f.angolo_retto(Kd, (1, 0), (0, 1))
A1 = interseca(Kd, lungo(Kd, dd, 1), (180, 0), (180, 1)); B1 = interseca(Kd, lungo(Kd, dd, 1), (300, 0), (300, 1))
f.figura([P2(EA), P2(EB), P2(EC)], "blu")
f.retta(A1, B1, "blu", 3.2)
f.retta((130, 70), (380, 70), "arancio", 1.2); f.testo((380, 70), "o₂", 6, 4, "arancio")
for x, z, z1 in [(180, 70, A1[1]), (300, 160, B1[1])]:
    f.richiamo(x, z, z1)
f.punto(P2(EA), "A₂", -24, -6); f.punto(P2(EB), "B₂", 8, 16); f.punto(P2(EC), "C₂", 8, -2)
f.punto(A1, "A₁", -6, 22); f.punto(B1, "B₁ ≡ C₁", 10, -8)
f.nota(16, 374, "Tutta la figura ha la prima proiezione su t₁δ: B₁ ≡ C₁, e BC non è più")
f.nota(16, 392, "di profilo ma proiettante in prima. AB resta orizzontale (A₂B₂ ∥ LT).")
f.salva(nuovo(SBOB + "06-triangolo-piano-proiettante-in-prima.svg"))

# ======================================================================
# 4. I solidi: piramide triangolare, parallelepipedo rettangolo, prisma a base triangolare -> sbobina
# ======================================================================
f = Figura(780, 340, 0, "I solidi: facce, spigoli, diedri")


def schizzo(ox, oy):
    return Triedro(f, (ox, oy), X3=0, U=0, Y=0, Z=0, scala=1.0)


def solido(t, vertici, spigoli, nascosti, colore="blu"):
    for i, j in spigoli:
        t.segmento(vertici[i], vertici[j], colore, 1.8, "6,4" if (i, j) in nascosti else None)


# piramide a base triangolare
t = schizzo(150, 200)
V = {"A": (-120, 0, 0), "B": (0, 0, 0), "C": (-50, 100, 0), "V": (-55, 40, 160)}
t._poligono([V["A"], V["C"], V["V"]], "blu", 0.14)
solido(t, V, [("A", "B"), ("B", "C"), ("C", "A"), ("A", "V"), ("B", "V"), ("C", "V")], {("A", "B"), ("B", "C"), ("B", "V")})
t.testo(V["V"], "vertice", 8, 0, "grigio", 12)
t.testo(pt_su(V["A"], V["V"], 0.5), "spigolo", -54, 0, "grigio", 12)
t.testo(tuple((V["A"][i] + V["C"][i] + V["V"][i]) / 3 for i in range(3)), "faccia", -14, 4, "grigio", 12)
f.nota(50, 330, "piramide a base triangolare")
# parallelepipedo rettangolo
t = schizzo(420, 190)
a, b, h = 130, 70, 110
P = {"1": (-a, 0, 0), "2": (0, 0, 0), "3": (0, b, 0), "4": (-a, b, 0)}
P.update({k + "'": (v[0], v[1], h) for k, v in list(P.items())})
t._poligono([P["3"], P["4"], P["4'"], P["3'"]], "blu", 0.14)
t._poligono([P["1"], P["4"], P["4'"], P["1'"]], "blu", 0.06)
solido(t, P, [("1", "2"), ("2", "3"), ("3", "4"), ("4", "1"), ("1'", "2'"), ("2'", "3'"), ("3'", "4'"), ("4'", "1'"),
              ("1", "1'"), ("2", "2'"), ("3", "3'"), ("4", "4'")], {("1", "2"), ("2", "3"), ("2", "2'")})
t.testo(pt_su(P["4"], P["4'"], 0.5), "spigolo", -50, 4, "grigio", 12)
t.testo(pt_su(P["3"], P["4'"], 0.5), "faccia", -16, 4, "grigio", 12)
t.testo(P["3'"], "diedro tra due facce", -20, -12, "grigio", 12)
f.nota(330, 330, "parallelepipedo rettangolo")
# prisma a base triangolare
t = schizzo(700, 190)
Q = {"A": (-110, 0, 0), "B": (0, 0, 0), "C": (-30, 90, 0)}
Q.update({k + "'": (v[0], v[1], 120) for k, v in list(Q.items())})
t._poligono([Q["A'"], Q["B'"], Q["C'"]], "blu", 0.20)
t._poligono([Q["A"], Q["B"], Q["C"]], "blu", 0.08)
solido(t, Q, [("A", "B"), ("B", "C"), ("C", "A"), ("A'", "B'"), ("B'", "C'"), ("C'", "A'"),
              ("A", "A'"), ("B", "B'"), ("C", "C'")], {("A", "B"), ("B", "C"), ("B", "B'")})
t.testo(Q["A'"], "base superiore", -96, -2, "grigio", 12)
t.testo(Q["A"], "base inferiore", -20, 24, "grigio", 12)
f.nota(600, 330, "prisma a base triangolare")
f.salva(nuovo(SBOB + "06-solidi-piramide-prisma-parallelepipedo.svg"))

# ======================================================================
# 5. Esercizio sul solido: la base ABC sta in un piano generico -> sbobina
#    piano: z + y = 0.62 (x - 30)
# ======================================================================
def zs(x, y):
    return 0.62 * (x - 30) - y


SA = (250, 115, zs(250, 115))           # AB di profilo (stessa x)
SB = (250, 30, zs(250, 30))
SC = (330, 0.62 * 300 - SB[2], SB[2])   # BC orizzontale (stessa quota di B)
v = (60, 0, 110)                         # traslazione: spigoli laterali frontali
SD, SE, SF = [tuple(p[i] + v[i] for i in range(3)) for p in (SA, SB, SC)]
T1ac, T2ac = tracce_retta(SA, SC)
T1bc, T2bc = tracce_retta(SB, SC)
f = Figura(640, 520, 250, "Esercizio sul solido: la base ABC sta in un piano generico α", x0=20)
f.lt(-10, 600)
Ks = (30, 0)
dO = direzione(P1(SB), P1(SC))
t1_fine = lungo(Ks, dO, 400); t2_fine = (300, 0.62 * 270)
f.traccia(Ks, t1_fine); f.testo(t1_fine, "t_1α", -40, 4)
f.traccia(Ks, t2_fine); f.testo(t2_fine, "t_2α", -36, -4)
for proj in (P2, P1):
    for p, q in [(SD, SE), (SE, SF), (SF, SD), (SA, SD), (SB, SE), (SC, SF)]:
        f.retta(proj(p), proj(q), "grigio", 1.2)
    f.figura([proj(SA), proj(SB), proj(SC)], "blu")
# AC generica: prolungo A2C2 fino alla LT -> (T1)2, scendo su A1C1 prolungata -> T1
f.retta((T1ac[0], 0), P2(SA), "viola", 1.3)
f.retta(P1(SA), P1(T1ac), "viola", 1.3)
f.richiamo(T1ac[0], 0, P1(T1ac)[1])
f.punto((T1ac[0], 0), "(T_1)₂", -40, -8, "viola"); f.punto(P1(T1ac), "T_1 di AC", -78, 14, "viola")
# BC orizzontale: B2C2 parallelo alla LT, T2 propria, T1 all'infinito
f.retta(P2(T2bc), P2(SB), "arancio", 1.3)
f.retta((T2bc[0], 0), P1(SB), "arancio", 1.3)
f.retta(P1(SC), lungo(P1(SC), dO, 70), "arancio", 1.3)
f.richiamo(T2bc[0], 0, P2(T2bc)[1])
f.punto(P2(T2bc), "T_2 di BC", -74, -6, "arancio"); f.punto((T2bc[0], 0), "(T_2)₁", -46, 18, "arancio")
f.testo(lungo(P1(SC), dO, 70), "T_1∞ di BC", -10, 22, "arancio")
for p, nome, dx2, dy2, dx1, dy1 in [(SA, "A", 8, 12, 6, 18), (SB, "B", -24, -6, -24, -4), (SC, "C", 6, 16, 8, -6),
                                     (SD, "D", 8, 4, -8, 22), (SE, "E", -10, -8, -8, -8), (SF, "F", 8, 4, 8, 14)]:
    f.punto(P2(p), nome + "₂", dx2, dy2); f.punto(P1(p), nome + "₁", dx1, dy1)
f.richiamo(250, SB[2], -SA[1]); f.richiamo(330, SC[2], -SC[1])
f.testo((250, 60), "AB di profilo", -80, 0, "grigio", 11, False)
f.nota(16, 494, "AB di profilo, BC orizzontale, AC generica. t₁α passa per T₁ di AC ed è parallela a B₁C₁")
f.nota(16, 512, "(contiene T₁∞ di BC); t₂α passa per T₂ di BC e per il punto in cui t₁α incontra la LT.")
f.salva(nuovo(SBOB + "06-solido-base-nel-piano-generico.svg"))

# ======================================================================
# 6. Il modellino: il piano mobile ruota intorno alla prima traccia -> sbobina
# ======================================================================
def triedro(titolo, h=450, w=600):
    f = Figura(w, h, 0, titolo)
    t = Triedro(f, (262, 190), X3=400, U=360, Y=230, Z=220, scala=0.75)
    t.piani()
    return f, t


f, t = triedro("Il modellino: il piano γ proiettante in prima ruota intorno a t₁γ fino a π₁")
x0 = 300
dt = unit((-0.5, 1, 0))              # direzione di t1gamma su pi1 (dalla LT verso chi guarda)
nh = unit((1, 0.5, 0))               # orizzontale perpendicolare a t1gamma: verso di rotazione
ng, dg = piano_per((x0, 0, 0), dt, (0, 0, 1))
t.piano(ng, dg, "blu", 0.10); t.tracce(ng, dg, "nero")
def su_gamma(u, z):
    return (x0 + u * dt[0], u * dt[1], z)
t.testo(su_gamma(0, 200), "t_2γ", 6, 0); t.testo(su_gamma(250, 0), "t_1γ", -30, 10)
tri = [su_gamma(60, 50), su_gamma(190, 60), su_gamma(100, 140)]
rib = [(p[0] + p[2] * nh[0], p[1] + p[2] * nh[1], 0) for p in tri]
t._poligono(tri, "blu", 0.30, "blu")
t._poligono(rib, "rosso", 0.22, "rosso")
for p, q, nome, dxq, dyq in zip(tri, rib, "ABC", [8, 8, 8], [14, 14, 4]):
    piede = (p[0], p[1], 0)
    arco = [(piede[0] + p[2] * math.sin(a) * nh[0], piede[1] + p[2] * math.sin(a) * nh[1], p[2] * math.cos(a))
            for a in [i * math.pi / 2 / 24 for i in range(25)]]
    polilinea3d(t, arco, "arancio", 1.3, "4,3")
    t.richiamo(p, piede)
    t.punto(p, nome, -16, -6, "blu"); t.punto(q, "(" + nome + ")", dxq, dyq, "rosso")
    t.punto(piede, None)
t.segmento(su_gamma(60, 0), su_gamma(190, 0), "blu", 3)
t.testo(su_gamma(190, 0), "A₁B₁C₁ su t₁γ", -110, 20, "blu", 12)
f.nota(16, 424, "Ogni punto descrive un arco (arancio) in un piano perpendicolare a t₁γ, la cerniera;")
f.nota(16, 442, "a rotazione finita il triangolo (A)(B)(C) è su π₁ in vera forma.")
f.salva(nuovo(SBOB + "06-spazio-piano-mobile.svg"))

# ======================================================================
# 7. Bozza: retta perpendicolare a un piano, nello spazio (disegno proposto)
# ======================================================================
f, t = triedro("Nello spazio: la retta r perpendicolare al piano α")
n, d = piano((60, 0, 0), (400, 120, 0), (400, 0, 200))
t.piano(n, d, "blu", 0.14); tr_ = t.tracce(n, d, "nero")
t.testo(pt_su(*tr_[1], 0.75), "t_1α", -4, 18); t.testo(pt_su(*tr_[2], 0.55), "t_2α", -36, -4)
nu = unit(n)
if nu[1] < 0:
    nu = tuple(-x for x in nu)          # verso chi guarda
H = (270, 40, (d - n[0] * 270 - n[1] * 40) / n[2])   # piede su alfa
Pr = tuple(H[i] + nu[i] * 150 for i in range(3))
Q = tuple(H[i] - nu[i] * 45 for i in range(3))
t.segmento(Q, H, "rosso", 1.4, "4,3"); t.segmento(H, Pr, "rosso", 2.4); t.testo(Pr, "r", 10, 4, "rosso", 16)
t.punto(Pr, "P", 6, -8, "rosso"); t.punto(H, "H", -20, -6, "rosso")
pr1 = lambda p: (p[0], p[1], 0)
pr2 = lambda p: (p[0], 0, p[2])
t.segmento(pr1(H), pr1(Pr), "rosso", 1.3, "6,4"); t.testo(pr1(Pr), "r₁", 8, 8, "rosso", 13)
t.segmento(pr2(H), pr2(Pr), "rosso", 1.3, "6,4"); t.testo(pr2(H), "r₂", -22, -4, "rosso", 13)
for p in (H, Pr):
    t.richiamo(p, pr1(p)); t.richiamo(p, pr2(p))
f.nota(16, 424, "r è perpendicolare ad α (forma 90° con ogni retta di α per H). Le sue proiezioni")
f.nota(16, 442, "r₁ e r₂ risultano perpendicolari a t₁α e a t₂α: è il teorema di Monge.")
f.salva(BOZ + "b06-spazio-retta-perpendicolare-al-piano.svg")

# ======================================================================
# 8. Bozza: due piani proiettanti in prima perpendicolari (il quaderno aperto)
# ======================================================================
f, t = triedro("Nello spazio: due piani proiettanti in prima perpendicolari (il quaderno aperto)")
Qp = (250, 70, 0)
d1 = unit((1, 0.3, 0)); d2 = unit((-0.3, 1, 0))
ng, dg = piano_per(Qp, d1, (0, 0, 1)); nd, dd_ = piano_per(Qp, d2, (0, 0, 1))
t.piano(ng, dg, "verde", 0.12); tg = t.tracce(ng, dg, "verde")
t.piano(nd, dd_, "viola", 0.12); tdl = t.tracce(nd, dd_, "viola")
t.testo(tuple(Qp[i] + d1[i] * 120 for i in range(3)), "t_1γ", 0, 18, "verde")
t.testo(tuple(Qp[i] + d2[i] * 140 for i in range(3)), "t_1δ", 8, 10, "viola")
t.segmento(Qp, (Qp[0], Qp[1], 220), "nero", 1.4)
angolo_retto3d(t, Qp, d1, d2, 14)
h = 140
r0 = (Qp[0], Qp[1], h); r1 = tuple(r0[i] + d2[i] * 150 for i in range(3)); r_ = tuple(r0[i] - d2[i] * 50 for i in range(3))
t.segmento(r_, r1, "rosso", 2.6); t.testo(r1, "r", 6, 4, "rosso", 16)
angolo_retto3d(t, r0, d1, d2, 12)
f.nota(16, 424, "L'angolo retto si legge sul banco (π₁), tra le prime tracce. La retta r di δ, orizzontale,")
f.nota(16, 442, "è perpendicolare a γ: per questo i due piani sono perpendicolari.")
f.salva(BOZ + "b06-spazio-piani-perpendicolari.svg")

# ======================================================================
# 9. Bozza: due piani proiettanti in seconda perpendicolari (disegno proposto)
# ======================================================================
f = Figura(560, 400, 180, "Due piani proiettanti in seconda β e ε perpendicolari: t₂β ⊥ t₂ε", x0=20)
f.lt(0, 520)
Qs = (260, 110)
Kb = (Qs[0] - 110 / 0.8, 0)      # t2beta: direzione (1, 0.8)
Ke = (Qs[0] + 0.8 * 110, 0)       # t2eps: direzione (-0.8, 1)
f.traccia(Kb, lungo(Qs, direzione(Kb, Qs), 60)); f.testo(lungo(Qs, direzione(Kb, Qs), 60), "t_2β", 6, 4)
f.traccia(Ke, lungo(Qs, direzione(Ke, Qs), 60)); f.testo(lungo(Qs, direzione(Ke, Qs), 60), "t_2ε", -34, 0)
f.traccia(Kb, (Kb[0], -160)); f.testo((Kb[0], -160), "t_1β", 6, 4)
f.traccia(Ke, (Ke[0], -160)); f.testo((Ke[0], -160), "t_1ε", 6, 4)
f.angolo_retto(Qs, direzione(Qs, Kb), direzione(Qs, Ke))
y1 = -95
f.retta((Kb[0], y1), (Ke[0], y1), "rosso"); f.testo(((Kb[0] + Ke[0]) / 2, y1), "r₁", 0, 18, "rosso")
f.retta(Ke, Qs, "rosso", 3); f.testo(pt_su(Ke, Qs, 0.5), "r₂ ≡ t₂ε", 8, 4, "rosso")
f.angolo_retto((Kb[0], y1), (0, 1), (1, 0))
f.nota(16, 374, "In ε si prende la frontale r: r₂ ≡ t₂ε è perpendicolare a t₂β, r₁ ∥ LT è perpendicolare a t₁β.")
f.nota(16, 392, "Quindi r è perpendicolare a β, ed ε, che contiene r, è perpendicolare a β.")
f.salva(BOZ + "b06-piani-proiettanti-in-seconda-perpendicolari.svg")

# ======================================================================
# 10. Bozza: una retta con le due tracce sotto la LT (disegno proposto)
# ======================================================================
f = Figura(600, 340, 150, "Retta r con le due tracce sotto la linea di terra", x0=30)
f.lt(-10, 540)
T1 = (170, 80, 0); T2 = (390, 0, -70)
d2 = direzione(P2(T1), P2(T2)); d1 = direzione(P1(T1), P1(T2))
f.retta(lungo(P2(T1), d2, -150), lungo(P2(T2), d2, 60), "rosso"); f.testo(lungo(P2(T1), d2, -150), "r₂", -18, 0, "rosso")
f.retta(lungo(P1(T1), d1, -150), lungo(P1(T2), d1, 60), "rosso"); f.testo(lungo(P1(T1), d1, -150), "r₁", -18, 8, "rosso")
f.richiamo(170, 0, -80); f.richiamo(390, 0, -70)
f.punto((170, 0), "(T_{1r})₂", 8, -10); f.punto(P1(T1), "T_{1r}", 6, 22)
f.punto((390, 0), "(T_{2r})₁", -72, -10); f.punto(P2(T2), "T_{2r}", -44, 22)
f.nota(16, 314, "T₁ᵣ: prima traccia, davanti a π₂ · T₂ᵣ: seconda traccia, sotto π₁ (la retta \"viene da fuori\").")
f.nota(16, 332, "Il procedimento non cambia: si prolungano le proiezioni fino alla LT e si cercano i punti notevoli.")
f.salva(BOZ + "b06-retta-tracce-sotto-la-lt.svg")

print("ok")
