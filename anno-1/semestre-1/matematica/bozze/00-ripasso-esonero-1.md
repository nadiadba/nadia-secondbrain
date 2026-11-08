---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
data: 2026-11-11
tags: [matematica, bozza, ripasso]
---

# Ripasso per l'esonero di matematica (11 novembre)

Le formule e i procedimenti di tutti gli argomenti fatti in classe, con un esempio svolto per ogni tipo di esercizio. Il piano dei giorni è in [[00-piano-esonero-1|Piano di studio per l'esonero]].

> [!info] Note collegate
> Piano: [[00-piano-esonero-1]] · Teoria: [[01-insiemi-e-intervalli]] · [[02-equazioni-e-disequazioni]] · [[03-retta-e-circonferenza]] · [[04-le-matrici]] · [[05-i-vettori]] · [[06-le-funzioni]] · [[07-funzioni-elementari]]

## 1. Equazioni e disequazioni

- **Secondo grado** $ax^2+bx+c=0$: $\Delta = b^2-4ac$; se $\Delta>0$ due soluzioni $x = \dfrac{-b\pm\sqrt{\Delta}}{2a}$, se $\Delta=0$ una sola, se $\Delta<0$ nessuna (reale).
- **Frazionarie**: prima le condizioni di esistenza (denominatori $\neq 0$), alla fine si scartano le soluzioni che le violano.
- **Irrazionali** $\sqrt{A(x)} = B(x)$: servono $A(x)\geq 0$ e $B(x)\geq 0$, poi si eleva al quadrato; verificare le soluzioni.
- **Valore assoluto**: $|A(x)| = k$ con $k\geq0$ dà $A(x) = k$ oppure $A(x) = -k$; $|A(x)| < k$ dà $-k < A(x) < k$; $|A(x)| > k$ dà $A(x) < -k$ oppure $A(x) > k$.
- **Disequazioni**: moltiplicando o dividendo per un numero negativo il verso **si inverte**.
- **Secondo grado** $ax^2+bx+c>0$ con $a>0$ e $\Delta>0$: soluzioni **esterne** alle radici ($x<x_1$ o $x>x_2$); per $<0$ soluzioni **interne** ($x_1<x<x_2$). Disegna la parabola e guarda dove sta sopra o sotto l'asse $x$.
- **Prodotti e frazioni**: si studia il segno di ogni fattore e si fa la tabella dei segni. Nelle fratte il denominatore non è mai $=0$.
- **Sistemi di disequazioni**: si risolve ognuna e si prende la parte comune (intersezione).

## 2. Retta e circonferenza

- **Distanza** tra $A=(x_1,y_1)$ e $B=(x_2,y_2)$: $d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$. **Punto medio**: $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$.
- **Pendenza** (coefficiente angolare) della retta per $A$ e $B$: $m = \dfrac{y_2-y_1}{x_2-x_1}$ (se $x_1 = x_2$ la retta è verticale, $x = x_1$).
- **Retta per un punto con pendenza $m$**: $y - y_1 = m(x - x_1)$. **Retta per due punti**: si calcola $m$ e si usa la formula precedente, oppure $\dfrac{y-y_1}{y_2-y_1} = \dfrac{x-x_1}{x_2-x_1}$.
  Esempio: $A=(1,2)$, $B=(3,6)$: $m = \frac{4}{2} = 2$, retta $y - 2 = 2(x-1)$, cioè $y = 2x$.
- **Forma esplicita** $y = mx+q$ ($q$ = dove taglia l'asse $y$); **forma implicita** $ax+by+c = 0$, con $m = -\frac{a}{b}$.
- **Parallele**: $m_1 = m_2$. **Perpendicolari**: $m_1\cdot m_2 = -1$.
- **Intersezione di due rette**: si mette a sistema le due equazioni.
- **Distanza di un punto** $(x_0,y_0)$ dalla retta $ax+by+c=0$: $d = \dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$.
- **Circonferenza** di centro $(a,b)$ e raggio $r$: $(x-a)^2+(y-b)^2 = r^2$.
- **Forma sviluppata** $x^2+y^2+\alpha x+\beta y+\gamma = 0$: centro $\left(-\frac{\alpha}{2}, -\frac{\beta}{2}\right)$, raggio $r = \sqrt{\frac{\alpha^2}{4}+\frac{\beta^2}{4}-\gamma}$ (esiste solo se sotto radice c'è un numero $>0$).
  Esempio: $x^2+y^2-4x+6y-3=0$: centro $(2,-3)$, $r = \sqrt{4+9+3} = 4$.
- **Retta e circonferenza**: se la distanza del centro dalla retta è minore di $r$ la retta è secante (2 punti), uguale a $r$ tangente (1 punto), maggiore di $r$ esterna (nessun punto).
- **Nello spazio**: distanza $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$; sfera $(x-a)^2+(y-b)^2+(z-c)^2 = r^2$.

## 3. Vettori

Un vettore nel piano è una coppia $\mathbf{u} = (u_1, u_2)$, nello spazio una terna $\mathbf{u} = (u_1, u_2, u_3)$. Si disegna come una freccia che parte dall'origine.

- **Somma e differenza**: componente per componente. $(2,-1) + (-3,4) = (-1, 3)$. Graficamente $\mathbf{u}+\mathbf{v}$ è la diagonale del parallelogramma costruito su $\mathbf{u}$ e $\mathbf{v}$.
- **Multiplo**: $k\,\mathbf{u} = (k u_1, k u_2)$. Se $k<0$ il verso si inverte.
- **Vettore tra due punti**: $\overrightarrow{AB} = B - A$. Con $A=(1,-1)$, $B=(5,1)$: $\overrightarrow{AB} = (4, 2)$.
- **Punto medio** di $AB$: $\left(\frac{a_1+b_1}{2}, \frac{a_2+b_2}{2}\right)$.
- **Norma** (lunghezza): $\|\mathbf{u}\| = \sqrt{u_1^2+u_2^2}$ (nello spazio si aggiunge $u_3^2$). $\|(3,4)\| = 5$.
- **Distanza** tra due punti: $d(A,B) = \|B - A\|$.
- **Versore** (vettore unitario, norma 1) nella direzione di $\mathbf{u}$: $\dfrac{\mathbf{u}}{\|\mathbf{u}\|}$. Normalizzare $(3,4)$: $\left(\frac35, \frac45\right)$.
- **Combinazione lineare**: $\mathbf{a} = \alpha\mathbf{u} + \beta\mathbf{v}$. Si scrive componente per componente e si risolve il sistema in $\alpha$ e $\beta$.
- **Parallelogramma**: conta l'ordine dei vertici. Se il giro è $A, B, D, C$ (come nell'esercizio 14), i lati opposti $AB$ e $CD$ sono vettori uguali: $\overrightarrow{AB} = \overrightarrow{CD}$, cioè $B - A = D - C$, quindi $D = B + C - A$. Le diagonali ($AD$ e $BC$) hanno lo stesso punto medio.
- **Paralleli**: $\mathbf{u}$ e $\mathbf{v}$ sono paralleli se uno è multiplo dell'altro, cioè se le componenti sono proporzionali. Stesso verso se il multiplo è positivo, verso opposto se è negativo.

## 4. Prodotto scalare

$$
\mathbf{u}\cdot\mathbf{v} = u_1v_1 + u_2v_2 \;(+\,u_3v_3) = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta
$$

Il risultato è un **numero**, non un vettore.

- **Angolo tra due vettori**: $\cos\theta = \dfrac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$, poi $\theta = \arccos(\dots)$.
  Esempio: $\mathbf{u}=(1,2)$, $\mathbf{v}=(3,1)$. $\mathbf{u}\cdot\mathbf{v} = 3+2 = 5$; $\|\mathbf{u}\| = \sqrt5$, $\|\mathbf{v}\| = \sqrt{10}$; $\cos\theta = \frac{5}{\sqrt{50}} = \frac{1}{\sqrt2}$, quindi $\theta = \frac{\pi}{4}$ (45°).
- **Segno**: $\mathbf{u}\cdot\mathbf{v} > 0$ angolo acuto; $=0$ angolo retto; $<0$ angolo ottuso. Non serve calcolare l'angolo.
- **Ortogonali** (perpendicolari): $\mathbf{u}\cdot\mathbf{v} = 0$.
- **Proprietà**: $\mathbf{u}\cdot\mathbf{u} = \|\mathbf{u}\|^2$; $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + 2\,\mathbf{u}\cdot\mathbf{v} + \|\mathbf{v}\|^2$. Se sono ortogonali resta il teorema di Pitagora: con $\|\mathbf{u}\|=6$, $\|\mathbf{v}\|=8$ si ha $\|\mathbf{u}+\mathbf{v}\| = 10$.
- **Proiezione di $\mathbf{u}$ su $\mathbf{v}$**:
  - scalare (un numero, la lunghezza con segno): $\dfrac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|}$
  - vettoriale (un vettore lungo $\mathbf{v}$): $\mathbf{p} = \dfrac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|^2}\,\mathbf{v}$
  - e $\mathbf{q} = \mathbf{u}-\mathbf{p}$ è ortogonale a $\mathbf{v}$.
- **Triangolo acutangolo, rettangolo o ottusangolo in $A$**: segno di $\overrightarrow{AB}\cdot\overrightarrow{AC}$.
- **Vero o falso tipici**: $\mathbf{u}\cdot\mathbf{v}=0$ non vuol dire che uno dei due è nullo (possono essere ortogonali); $\|\mathbf{u}+\mathbf{v}\| = \|\mathbf{u}\|+\|\mathbf{v}\|$ vale solo se sono paralleli e con lo stesso verso.
- **Distanza di un punto $P$ da una retta** $X = A + s\,\mathbf{d}$: il piede $H = A + s\,\mathbf{d}$ si trova imponendo $\overrightarrow{HP}\cdot\mathbf{d} = 0$; la distanza è $\|\overrightarrow{HP}\|$.

## 5. Matrici, determinanti, prodotto vettoriale, prodotto triplo

**Matrici**: $a_{ij}$ è l'elemento nella riga $i$ e nella colonna $j$. Somma: $A+B = (a_{ij}+b_{ij})$. Prodotto riga per colonna: l'elemento di posto $ij$ di $A\cdot B$ è la riga $i$ di $A$ «per» la colonna $j$ di $B$ (prodotto scalare). Esempio della lavagna: $\begin{pmatrix}1&2\\1&0\end{pmatrix}\begin{pmatrix}1&-1\\2&1\end{pmatrix} = \begin{pmatrix}5&1\\1&-1\end{pmatrix}$. Il prodotto è associativo e distributivo ma **non commutativo** ($A\cdot B \neq B\cdot A$ in generale).

**Complemento algebrico**: $A_{ij} = (-1)^{i+j}\cdot$ (determinante che resta togliendo riga $i$ e colonna $j$); segni a scacchiera $+\,-\,+$. Il determinante si sviluppa lungo una riga o colonna (conviene quella con più zeri): somma degli elementi per i loro complementi algebrici.

**Determinante 2×2**:
$$
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc
$$
Con due vettori del piano, $|u_1v_2 - u_2v_1|$ è l'area del parallelogramma che generano. Il segno dice il verso: positivo se per andare da $\mathbf{u}$ a $\mathbf{v}$ si gira in senso antiorario.

**Determinante 3×3** (sviluppo lungo la prima riga, segni $+\,-\,+$):
$$
\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)
$$

**Prodotto vettoriale** (solo nello spazio; il risultato è un **vettore**):
$$
\mathbf{u}\times\mathbf{v} = (u_2v_3 - u_3v_2,\;\; u_3v_1 - u_1v_3,\;\; u_1v_2 - u_2v_1)
$$
Esempio: $\mathbf{u}=(1,2,-1)$, $\mathbf{v}=(3,-1,2)$: $\mathbf{u}\times\mathbf{v} = (4-1,\; -3-2,\; -1-6) = (3,-5,-7)$. Controllo: $(3,-5,-7)\cdot(1,2,-1) = 3-10+7 = 0$.

- È **perpendicolare** sia a $\mathbf{u}$ sia a $\mathbf{v}$ (verso con la regola della mano destra).
- $\mathbf{v}\times\mathbf{u} = -(\mathbf{u}\times\mathbf{v})$.
- $\|\mathbf{u}\times\mathbf{v}\| = \|\mathbf{u}\|\,\|\mathbf{v}\|\sin\theta$ = **area del parallelogramma**; il **triangolo** ha area metà.
- $\mathbf{u}\times\mathbf{v} = \mathbf{0}$ se e solo se $\mathbf{u}$ e $\mathbf{v}$ sono **paralleli**.
- Angolo: $\sin\theta = \dfrac{\|\mathbf{u}\times\mathbf{v}\|}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$ (attenzione: il seno non distingue un angolo acuto dal suo supplementare, il coseno sì).

**Prodotto triplo** (il risultato è un **numero**):
$$
\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w}) = \det\begin{pmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{pmatrix}
$$
- $|\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})|$ = **volume del parallelepipedo**; il **tetraedro** ha volume $\frac16$ di quello.
- È $0$ se e solo se i tre vettori sono **complanari**. Quattro punti $A, B, C, D$ sono complanari se $\overrightarrow{AB}\cdot(\overrightarrow{AC}\times\overrightarrow{AD}) = 0$.
- Scambiando due vettori il segno cambia (cambia l'orientazione), il valore assoluto no.
- Esercizi con il parametro ($t$ o $k$): si scrive il determinante con il parametro e si pone uguale a $0$ (complanari) oppure si pone il prodotto vettoriale uguale a $\mathbf{0}$ (paralleli).

## 6. Funzioni

- **Dominio naturale**: i valori di $x$ per cui la formula ha senso.
  - denominatore $\neq 0$
  - sotto radice quadrata $\geq 0$
  - argomento del logaritmo $> 0$
  - per $\arcsin$ e $\arccos$: argomento tra $-1$ e $1$
  Esempio: $\sqrt{x-1}/(x-4)$: $x \geq 1$ e $x \neq 4$.
- **Immagine**: i valori che la funzione assume davvero. $(x+1)^2 - 4$ ha immagine $[-4, +\infty)$ (vertice della parabola).
- **Iniettiva**: valori diversi di $x$ danno valori diversi di $y$ (ogni retta orizzontale taglia il grafico al massimo una volta). **Suriettiva**: ogni elemento del codominio viene raggiunto. **Biettiva**: tutte e due; solo allora esiste l'**inversa**.
- **Inversa**: si scrive $y = f(x)$ e si ricava $x$. $f(x) = 5 - 2x \Rightarrow f^{-1}(y) = \frac{5-y}{2}$. Verifica: $f(f^{-1}(y)) = y$ e $f^{-1}(f(x)) = x$.
- **Composizione**: $(f\circ g)(x) = f(g(x))$: prima $g$, poi $f$. Il dominio richiede che $x$ stia nel dominio di $g$ e $g(x)$ in quello di $f$.
- **Pari**: $f(-x) = f(x)$, grafico simmetrico rispetto all'asse $y$. **Dispari**: $f(-x) = -f(x)$, simmetrico rispetto all'origine. Una funzione può non essere né pari né dispari, e se il dominio non è simmetrico ($\sqrt{x}$) la domanda non ha senso.
- **Traslazioni dei grafici**: $f(x - a)$ sposta a destra di $a$; $f(x) + b$ sposta in alto di $b$; $-f(x)$ ribalta rispetto all'asse $x$; $|f(x)|$ ribalta in su le parti negative.
  Esempio: $|x+1| - 2$ è la «V» di $|x|$ spostata a sinistra di 1 e in basso di 2: vertice $(-1,-2)$, zeri $x=-3$ e $x=1$, immagine $[-2,+\infty)$.

## 7. Esponenziali, logaritmi, trigonometria

**Esponenziale e logaritmo** sono l'una l'inversa dell'altro: $\log_a b = c \iff a^c = b$. Il logaritmo naturale $\ln$ ha base $e \approx 2{,}718$.

- $\log_a(xy) = \log_a x + \log_a y$; $\;\log_a\frac{x}{y} = \log_a x - \log_a y$; $\;\log_a x^k = k\log_a x$
- $\ln(e^x) = x$, $\;e^{\ln x} = x$, $\;\log_a 1 = 0$, $\;\log_a a = 1$
- Esempi: $\log_3 27 = 3$; $\log_4\frac12 = -\frac12$ (perché $4^{-1/2} = \frac12$)
- $a^x$ con $a>1$ è crescente, con $0<a<1$ è decrescente; sempre positiva; asintoto orizzontale $y=0$. $\ln x$: dominio $x>0$, asintoto verticale $x=0$.
- **Equazioni**: si porta tutto alla stessa base o si applica $\ln$ ai due lati. $e^{2x} = 7 \Rightarrow x = \frac{\ln 7}{2}$.
- **Disequazioni**: con base minore di 1 il verso **si inverte**. $\left(\frac12\right)^{x-2} \leq \frac18 = \left(\frac12\right)^3 \Rightarrow x - 2 \geq 3 \Rightarrow x \geq 5$.
- **Prima il dominio**: $\ln x + \ln(x-1) = \ln 6$ richiede $x > 1$; diventa $x(x-1) = 6$, cioè $x = 3$ o $x = -2$, ma solo $x = 3$ sta nel dominio.
- **Tempo di raddoppio** di $N(t) = N_0 e^{kt}$: $e^{kt} = 2 \Rightarrow t = \frac{\ln 2}{k}$.
- **Attenzione**: $\ln(x^2) = 2\ln|x|$, non $2\ln x$ (per $x<0$ il secondo non esiste).

**Trigonometria** (angoli in radianti: $180° = \pi$).

| angolo | $0$ | $\frac{\pi}{6}$ (30°) | $\frac{\pi}{4}$ (45°) | $\frac{\pi}{3}$ (60°) | $\frac{\pi}{2}$ (90°) |
|---|---|---|---|---|---|
| $\sin$ | $0$ | $\frac12$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ |
| $\cos$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac12$ | $0$ |
| $\tan$ | $0$ | $\frac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | non esiste |

- $A\cos(Bx) + C$: ampiezza $|A|$, periodo $\frac{2\pi}{|B|}$, immagine $[C - |A|,\, C + |A|]$. Esempio: $3\cos(2x) + 2$ ha ampiezza 3, periodo $\pi$, immagine $[-1, 5]$.
- **Funzioni inverse** e loro immagini:
  - $\arcsin$: da $[-1,1]$ a $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
  - $\arccos$: da $[-1,1]$ a $[0, \pi]$
  - $\arctan$: da $\mathbb{R}$ a $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, quindi non vale mai $\frac{\pi}{2}$
- $\arcsin(\sin x) = x$ **solo** se $x$ sta in $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$. Esempio: $\arcsin\left(\sin\frac{3\pi}{4}\right) = \frac{\pi}{4}$.
- **Equazioni**: $\sin x = \frac{\sqrt3}{2}$ su $[0, 2\pi]$ dà $x = \frac{\pi}{3}$ e $x = \frac{2\pi}{3}$ (il seno è uguale per $x$ e $\pi - x$); su tutto $\mathbb{R}$ si aggiunge $+\,2k\pi$. Per la tangente si aggiunge $+\,k\pi$.
- **Pendenza**: una rampa al 12% ha $\tan\alpha = 0{,}12$, quindi $\alpha = \arctan 0{,}12 \approx 0{,}119$ rad $\approx 6{,}8°$.
