"""Tutorial grafico del Disegno 11 della bozza 02 (omologia: dai due centri S e S1 al centro U).

Un'immagine per ogni passaggio: l'elemento nuovo e' in arancione e piu' spesso, quelli gia' fatti
restano nei loro colori. Stessa geometria di omologia_due_centri() in geometria-02.py.

Immagini: bozze/img/b02-pp-NN.svg  -  Nota: bozze/02-omologia-dai-due-centri-passo-passo.md
"""
import importlib.util
import os

QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("g02", os.path.join(QUI, "geometria-02.py"))
g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g)          # (rigenera anche le immagini di geometria-02, identiche)

F, su_piano3, direzione, lungo, allineati = g.F, g.su_piano3, g.direzione, g.lungo, g.allineati
BZ = g.BZ
NUOVO = "arancio"

ox, oy = 140, 60


def s(p):
    return (ox + p[0] + 0.42 * p[2], oy + p[1] + 0.3 * p[2])


S, S1 = (250, 350, -260), (270, 210, -110)
A0, B0 = (120, 80, 0), (220, 140, 0)
A, B = su_piano3(S, A0, 1, 0), su_piano3(S, B0, 1, 0)
A1, B1 = su_piano3(S1, A0, 1, 0), su_piano3(S1, B0, 1, 0)
U = su_piano3(S, S1, 1, 0)
K = su_piano3(A0, B0, 1, 0)
a2 = lambda p: (p[0], p[2])  # noqa: E731
assert allineati(a2(U), a2(A), a2(A1)) and allineati(a2(U), a2(B), a2(B1))
assert allineati(a2(A), a2(B), a2(K)) and allineati(a2(A1), a2(B1), a2(K))


def per_punti(f, pts, colore, sp, tratt, oltre=28):
    """Linea che copre tutti i punti (allineati) e li supera di 'oltre' px da tutte e due le parti."""
    P = [s(p) for p in pts]
    d = direzione(P[0], P[1])
    t = [(q[0] - P[0][0]) * d[0] + (q[1] - P[0][1]) * d[1] for q in P]
    a, b = lungo(P[0], d, min(t) - oltre), lungo(P[0], d, max(t) + oltre)
    f.linea(a, b, colore, sp, tratt)


def col(nuovo, c):
    return NUOVO if nuovo else c


def sp(nuovo, x):
    return x + 1.6 if nuovo else x


# ogni passo: (testo, funzione che disegna l'elemento)
PASSI = []


def passo(testo):
    def dec(fn):
        PASSI.append((testo, fn))
        return fn
    return dec


@passo("Disegna il piano α come un parallelogramma steso: lato davanti orizzontale, lati di fianco inclinati.")
def _(f, n):
    f.poligono([s(p) for p in [(-80, 0, -60), (360, 0, -60), (360, 0, 300), (-80, 0, 300)]],
               col(n, "grigio"), 0.08, sp(n, 1))
    f.testo(s((-80, 0, -60)), "α ≡ α′", 40, 16, col(n, "grigio"), 15)


@passo("Disegna il piano α₀ come un rettangolo in piedi, con il lato di sotto appoggiato su α.")
def _(f, n):
    f.poligono([s(p) for p in [(-80, 0, 0), (360, 0, 0), (360, 190, 0), (-80, 190, 0)]],
               col(n, "grigio"), 0.10, sp(n, 1))
    f.testo(s((-80, 190, 0)), "α_0", 6, 20, col(n, "grigio"), 15)


@passo("Ripassa il lato di sotto di α₀ e prolungalo: è l'asse u, dove i due piani si tagliano.")
def _(f, n):
    f.linea(s((-100, 0, 0)), s((380, 0, 0)), col(n, "nero"), sp(n, 2.4))
    f.testo(s((380, 0, 0)), "u", 4, 4, col(n, "nero"), 16)


@passo("Dentro α₀ disegna il segmento A₀B₀, inclinato, che sale verso destra.")
def _(f, n):
    f.linea(s(A0), s(B0), col(n, "nero"), sp(n, 2.4))
    f.punto(s(A0), "A_0", -26, -4, col(n, "nero")); f.punto(s(B0), "B_0", 6, -6, col(n, "nero"))


@passo("Prolunga A₀B₀ verso il basso a sinistra fino all'asse u: lì metti il cerchietto (punto unito).")
def _(f, n):
    f.linea(s(K), s(A0), col(n, "nero"), sp(n, 1.2), "6,4")
    f.unito(s(K))


@passo("Metti il primo centro S, in alto, fuori dai due piani.")
def _(f, n):
    f.punto(s(S), "S", 8, -4, col(n, "nero"))


@passo("Da S tira il raggio che passa per A₀ e prolungalo verso il basso, dentro α.")
def _(f, n):
    per_punti(f, [S, A0, A], col(n, "blu"), sp(n, 0.9), "5,4")


@passo("Da S tira il raggio che passa per B₀ e prolungalo verso il basso, dentro α.")
def _(f, n):
    per_punti(f, [S, B0, B], col(n, "blu"), sp(n, 0.9), "5,4")


@passo("Scegli tu il punto A sul primo raggio, sotto A₀, dentro α. È uno dei due soli punti liberi.")
def _(f, n):
    f.punto(s(A), "A", 4, 18, col(n, "blu"))


@passo("Tira la retta che parte dal cerchietto, passa per A e prosegue verso destra.")
def _(f, n):
    per_punti(f, [K, A, B], col(n, "blu"), sp(n, 1), "3,3")


@passo("B NON si sceglie: è l'incrocio tra questa retta e il raggio da S per B₀.")
def _(f, n):
    f.punto(s(B), "B", 8, 4, col(n, "blu"))


@passo("Ripassa il segmento AB: è la prima proiezione di A₀B₀ (da S).")
def _(f, n):
    f.linea(s(A), s(B), col(n, "blu"), sp(n, 2.4))


@passo("Metti il secondo centro S₁, più in basso di S, sempre fuori dai piani.")
def _(f, n):
    f.punto(s(S1), "S_1", 8, -2, col(n, "nero"))


@passo("Da S₁ tira il raggio che passa per A₀ e prolungalo verso il basso, dentro α.")
def _(f, n):
    per_punti(f, [S1, A0, A1], col(n, "verde"), sp(n, 0.9), "5,4")


@passo("Da S₁ tira il raggio che passa per B₀ e prolungalo verso il basso, dentro α.")
def _(f, n):
    per_punti(f, [S1, B0, B1], col(n, "verde"), sp(n, 0.9), "5,4")


@passo("Scegli tu il punto A′ sul raggio verde che passa per A₀. È l'altro punto libero.")
def _(f, n):
    f.punto(s(A1), "A′", -26, 2, col(n, "verde"))


@passo("Tira la retta che parte dal cerchietto, passa per A′ e prosegue verso destra.")
def _(f, n):
    per_punti(f, [K, A1, B1], col(n, "verde"), sp(n, 1), "3,3")


@passo("B′ NON si sceglie: è l'incrocio tra questa retta e il raggio da S₁ per B₀.")
def _(f, n):
    f.punto(s(B1), "B′", 8, -4, col(n, "verde"))


@passo("Ripassa il segmento A′B′: è la seconda proiezione di A₀B₀ (da S₁).")
def _(f, n):
    f.linea(s(A1), s(B1), col(n, "verde"), sp(n, 2.4))


@passo("Tira la retta che passa per S e per S₁ e prolungala molto verso il basso.")
def _(f, n):
    per_punti(f, [S, S1, U], col(n, "rosso"), sp(n, 1.4), "7,4")


@passo("Tira la retta che passa per A e per A′ e prolungala molto, verso destra.")
def _(f, n):
    per_punti(f, [A1, A, U], col(n, "grigio"), sp(n, 1), "2,3")


@passo("U NON si sceglie: è l'incrocio tra la retta S S₁ e la retta A A′. Non sta sull'asse.")
def _(f, n):
    f.punto(s(U), "U", 12, 4, col(n, "rosso"))


@passo("Verifica: la retta per B e B′, prolungata, passa anche lei per U. Se ci passa, è giusto.")
def _(f, n):
    per_punti(f, [B1, B, U], col(n, "grigio"), sp(n, 1), "2,3")


TOT = len(PASSI)
# ordine di disegno: sotto i piani, poi le linee, poi i punti sopra a tutto
for k in range(TOT):
    f = F(700, 430, f"Passo {k + 1} di {TOT}")
    fatti = list(range(k + 1))
    PUNTI = {4, 5, 8, 10, 12, 15, 17, 21}          # passi che mettono un punto: vanno sopra alle linee
    piani = [i for i in fatti if i < 2]
    linee = [i for i in fatti if i >= 2 and i not in PUNTI]
    punti = [i for i in fatti if i in PUNTI]
    for i in piani + linee + punti:
        PASSI[i][1](f, i == k)
    f.didascalia(PASSI[k][0], 12)
    f.salva(BZ + f"b02-pp-{k + 1:02d}.svg")
print(TOT, "passi")
