---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Le funzioni elementari

Le funzioni elementari sono i mattoni con cui si costruiscono quasi tutte le altre funzioni: la retta, le potenze, le radici, l'iperbole, il valore assoluto, la parabola, l'esponenziale, il logaritmo e le funzioni trigonometriche. In classe ci si è fermati proprio all'inizio di questo argomento, quindi questa pagina serve a prepararsi: per ogni funzione si guarda il grafico e si leggono le stesse informazioni (dominio, immagine, monotonia, parità, zeri, asintoti, inversa), e poi si imparano a risolvere le equazioni e le disequazioni che le contengono. Gli esempi svolti vengono quasi tutti dalla seconda pagina del foglio di esercizi del professore.

> [!info] Note collegate
> Teoria: [[01-equazioni-e-disequazioni]] · [[02-retta-e-circonferenza]] · [[03-i-vettori]] · [[04-le-funzioni]] · [[06-le-matrici]] · [[07-insiemi-e-intervalli]] · Ripasso: [[00-ripasso-esonero-1]]

## RETTE, POTENZE, RADICI E VALORE ASSOLUTO

### Come si studia una funzione elementare

Di ogni funzione elementare bisogna saper disegnare il grafico a memoria, almeno a grandi linee. Dal grafico poi si leggono sempre le stesse otto informazioni, che conviene imparare come una scheda fissa.

Le prime tre sono già note dalla pagina [[04-le-funzioni]]:

- il *dominio*: i valori di $x$ per cui la formula ha senso;
- l'*immagine*: i valori di $y$ che la funzione raggiunge davvero;
- la *parità*: se il grafico è simmetrico rispetto all'asse $y$ (funzione pari, $f(-x) = f(x)$) o rispetto all'origine (funzione dispari, $f(-x) = -f(x)$).

Le altre sono queste:

- la *monotonia*: dove la funzione sale e dove scende, leggendo il grafico da sinistra verso destra;
- gli *zeri*: i punti in cui il grafico tocca l'asse $x$, cioè le soluzioni di $f(x) = 0$;
- gli *asintoti*: le rette a cui il grafico si avvicina sempre di più senza mai toccarle;
- l'*inversa*: se esiste, e qual è.

> [!abstract] Funzione crescente e decrescente
> Una funzione è *crescente* su un intervallo se, quando $x$ aumenta, anche $f(x)$ aumenta:
> $$
> x_1 < x_2 \implies f(x_1) < f(x_2)
> $$
> È *decrescente* se, quando $x$ aumenta, $f(x)$ diminuisce: $x_1 < x_2 \implies f(x_1) > f(x_2)$.
> Una funzione sempre crescente (o sempre decrescente) è *monotona*, e una funzione monotona è iniettiva: quindi è invertibile sulla sua immagine.

L'ultima frase è il motivo per cui la monotonia è così importante. Se una funzione sale sempre, due valori diversi di $x$ non possono dare lo stesso $y$; quindi ogni retta orizzontale taglia il grafico al massimo una volta, e la funzione si può invertire.

> [!abstract] Asintoti verticali e orizzontali
> - La retta $x = c$ è un *asintoto verticale* se, avvicinandosi a $c$, il grafico sale verso $+\infty$ o scende verso $-\infty$. Di solito succede dove la funzione non è definita (un denominatore che si annulla, l'argomento di un logaritmo che tende a $0$).
> - La retta $y = \ell$ è un *asintoto orizzontale* se, andando molto a destra (o molto a sinistra), il grafico si avvicina sempre di più all'altezza $\ell$.

Gli asintoti si studieranno con precisione con i limiti, più avanti nel corso. Per ora basta riconoscerli sul grafico.

Infine, una regola che vale per tutte le inverse: il grafico di $f^{-1}$ è il simmetrico del grafico di $f$ rispetto alla bisettrice $y = x$. Infatti se il punto $(a, b)$ sta sul grafico di $f$, cioè $f(a) = b$, allora $f^{-1}(b) = a$ e il punto $(b, a)$ sta sul grafico dell'inversa. Scambiare le coordinate significa proprio riflettere rispetto alla bisettrice. Questa regola tornerà molte volte in questa pagina.

### La retta e la funzione lineare

La funzione più semplice è la *funzione lineare* $f(x) = mx + q$, il cui grafico è una retta (vista nella pagina [[02-retta-e-circonferenza]]).

- Il numero $m$ è il *coefficiente angolare* (o pendenza): dice di quanto sale $y$ quando $x$ aumenta di $1$.
- Il numero $q$ è l'*ordinata all'origine*: il punto in cui la retta taglia l'asse $y$, perché $f(0) = q$.

![[05-rette.svg|480]]

Nel disegno, la retta blu $y = 2x - 1$ ha $m = 2$: spostandosi di $1$ verso destra si sale di $2$ (il triangolino tratteggiato). La retta rossa ha $m = -\frac12$, quindi scende. La retta verde $y = 3$ ha $m = 0$ ed è orizzontale.

> [!abstract] Scheda della funzione lineare $f(x) = mx + q$ con $m \neq 0$
> - Dominio: $\mathbb{R}$. Immagine: $\mathbb{R}$.
> - Monotonia: crescente se $m > 0$, decrescente se $m < 0$.
> - Zero: $x = -\frac{q}{m}$ (si risolve $mx + q = 0$).
> - Parità: dispari solo se $q = 0$ (la retta passa per l'origine); altrimenti né pari né dispari.
> - Asintoti: nessuno.
> - Inversa: esiste ed è ancora una retta, $f^{-1}(y) = \dfrac{y - q}{m}$.
>
> Se $m = 0$ la funzione è costante, $f(x) = q$: l'immagine è il solo numero $q$, la funzione è pari e non è invertibile.

> [!example] Esempio: la tariffa (esercizio 15, prima pagina)
> Una tariffa costa $T(t) = 4 + 2t$ euro per $t \geq 0$ ore. È una retta con $q = 4$ (il costo fisso) e $m = 2$ (due euro all'ora).
>
> 1. Immagine: per $t \geq 0$ il costo parte da $T(0) = 4$ e cresce senza limite, quindi l'immagine è $[4, +\infty)$.
> 2. Inversa: da $y = 4 + 2t$ si ricava $t = \dfrac{y - 4}{2}$, quindi $T^{-1}(y) = \dfrac{y-4}{2}$, definita per $y \geq 4$.
> 3. $T^{-1}(10) = \dfrac{10 - 4}{2} = 3$: con $10$ euro si paga un servizio di $3$ ore.

### Le potenze con esponente pari

Le funzioni $f(x) = x^n$ con $n$ intero positivo si dividono in due famiglie, a seconda che $n$ sia pari o dispari. Cominciamo dalle pari: $x^2$, $x^4$, $x^6$, ...

![[05-potenze-pari.svg|380]]

Elevando a una potenza pari il segno sparisce: $(-2)^2 = 4 = 2^2$. Per questo il grafico è simmetrico rispetto all'asse $y$ e sta tutto sopra l'asse $x$.

Tutte le potenze pari passano per gli stessi tre punti: $(-1, 1)$, $(0, 0)$ e $(1, 1)$. Fra $-1$ e $1$ l'esponente più alto dà il grafico più schiacciato (per esempio $0{,}5^2 = 0{,}25$ ma $0{,}5^4 = 0{,}0625$); fuori da quell'intervallo l'esponente più alto dà il grafico più ripido.

> [!abstract] Scheda di $f(x) = x^n$ con $n$ pari
> - Dominio: $\mathbb{R}$. Immagine: $[0, +\infty)$.
> - Monotonia: decrescente su $(-\infty, 0]$, crescente su $[0, +\infty)$.
> - Zero: $x = 0$, che è anche il punto più basso (il minimo).
> - Parità: pari.
> - Asintoti: nessuno.
> - Inversa: su tutto $\mathbb{R}$ non esiste, perché $x$ e $-x$ danno lo stesso valore. Se si restringe il dominio a $[0, +\infty)$, l'inversa è la radice $n$-esima.

### Le potenze con esponente dispari

Le potenze dispari $x$, $x^3$, $x^5$, ... conservano il segno: $(-2)^3 = -8$. Il grafico quindi scende nel terzo quadrante ed è simmetrico rispetto all'origine.

![[05-potenze-dispari.svg|360]]

Passano tutte per $(-1, -1)$, $(0, 0)$ e $(1, 1)$, e anche qui l'esponente più alto schiaccia il grafico vicino all'origine e lo rende più ripido fuori da $[-1, 1]$.

> [!abstract] Scheda di $f(x) = x^n$ con $n$ dispari
> - Dominio: $\mathbb{R}$. Immagine: $\mathbb{R}$.
> - Monotonia: crescente su tutto $\mathbb{R}$.
> - Zero: $x = 0$.
> - Parità: dispari.
> - Asintoti: nessuno.
> - Inversa: esiste su tutto $\mathbb{R}$ ed è la radice $n$-esima (per esempio l'inversa di $x^3$ è $\sqrt[3]{x}$).

### Le radici

La radice quadrata $\sqrt{x}$ è il numero non negativo che, elevato al quadrato, dà $x$. Quindi $\sqrt{9} = 3$ (e non $-3$). È l'inversa di $x^2$ ristretta a $[0, +\infty)$, e infatti i due grafici sono simmetrici rispetto alla bisettrice.

![[05-radice-quadrata.svg|430]]

> [!abstract] Scheda di $f(x) = \sqrt{x}$
> - Dominio: $[0, +\infty)$, perché nessun numero reale al quadrato dà un risultato negativo.
> - Immagine: $[0, +\infty)$.
> - Monotonia: crescente.
> - Zero: $x = 0$.
> - Parità: non ha senso chiederla, perché il dominio non è simmetrico (c'è $4$ ma non $-4$).
> - Asintoti: nessuno; la curva cresce sempre, ma sempre più lentamente.
> - Inversa: $y^2$ con $y \geq 0$.
>
> Le radici con indice pari ($\sqrt[4]{x}$, $\sqrt[6]{x}$, ...) si comportano allo stesso modo.

La radice cubica invece è definita per ogni numero reale, perché anche un numero negativo ha la sua radice cubica: $\sqrt[3]{-8} = -2$, dato che $(-2)^3 = -8$.

![[05-radice-cubica.svg|500]]

> [!abstract] Scheda di $f(x) = \sqrt[3]{x}$
> - Dominio: $\mathbb{R}$. Immagine: $\mathbb{R}$.
> - Monotonia: crescente.
> - Zero: $x = 0$.
> - Parità: dispari.
> - Inversa: $y^3$.
>
> Lo stesso vale per tutte le radici con indice dispari.

> [!warning] La radice di un quadrato
> $\sqrt{x^2}$ non è $x$, ma $|x|$. Per esempio $\sqrt{(-3)^2} = \sqrt{9} = 3$, che non è $-3$. Questo errore torna anche con i logaritmi, più sotto.

### La funzione 1/x e l'iperbole

La funzione $f(x) = \dfrac{1}{x}$ associa a ogni numero il suo reciproco. Il grafico è un'*iperbole* (equilatera) formata da due rami separati.

![[05-iperbole.svg|460]]

Per capire la forma basta provare qualche valore. Per $x$ grande il reciproco è piccolo ($\frac{1}{100} = 0{,}01$): il grafico si schiaccia sull'asse $x$. Per $x$ vicino a $0$ il reciproco è enorme ($\frac{1}{0{,}01} = 100$): il grafico schizza verso l'alto. E siccome il reciproco di un numero negativo è negativo, il secondo ramo sta nel terzo quadrante.

> [!abstract] Scheda di $f(x) = \dfrac{1}{x}$
> - Dominio: $\mathbb{R} \setminus \{0\}$, cioè tutti i numeri tranne lo zero (non si divide per zero).
> - Immagine: $\mathbb{R} \setminus \{0\}$, perché una frazione con numeratore $1$ non vale mai zero.
> - Monotonia: decrescente su $(-\infty, 0)$ e decrescente su $(0, +\infty)$, presi separatamente.
> - Zeri: nessuno.
> - Parità: dispari, perché $\frac{1}{-x} = -\frac{1}{x}$.
> - Asintoti: verticale $x = 0$ e orizzontale $y = 0$.
> - Inversa: è l'inversa di se stessa. Da $y = \frac1x$ si ricava $x = \frac1y$.

> [!warning] Decrescente sui due rami, ma non su tutto il dominio
> Non si può dire che $\frac1x$ sia decrescente su tutto il suo dominio. Infatti $-1 < 1$ e anche $f(-1) = -1 < f(1) = 1$: passando da un ramo all'altro la funzione «sale». Si dice che è decrescente su ciascuno dei due intervalli.

### Il valore assoluto

Il *valore assoluto* di un numero è il numero senza segno, cioè la sua distanza dallo zero:

$$
|x| = \begin{cases} x & \text{se } x \geq 0 \\ -x & \text{se } x < 0 \end{cases}
$$

La seconda riga a prima vista spaventa, ma dice solo questo: se $x$ è negativo, cambiandogli segno diventa positivo. Per esempio $|-5| = -(-5) = 5$.

Il grafico è una «V» con il vertice nell'origine: per $x \geq 0$ è la retta $y = x$, per $x < 0$ è la retta $y = -x$.

> [!abstract] Scheda di $f(x) = |x|$
> - Dominio: $\mathbb{R}$. Immagine: $[0, +\infty)$.
> - Monotonia: decrescente su $(-\infty, 0]$, crescente su $[0, +\infty)$.
> - Zero: $x = 0$.
> - Parità: pari.
> - Inversa: su $\mathbb{R}$ non esiste ($|-2| = |2|$).

Spostando la «V» con le traslazioni (pagina [[04-le-funzioni]]) si ottengono tutte le funzioni del tipo $|x - a| + b$, con il vertice nel punto $(a, b)$.

> [!example] Esempio: $|x+1| - 2$ (esercizio 11, prima pagina)
> ![[05-valore-assoluto.svg|440]]
>
> 1. Si parte da $|x|$ (tratteggiata). Il $+1$ dentro il valore assoluto sposta il grafico di $1$ verso sinistra; il $-2$ fuori lo sposta di $2$ verso il basso. Il vertice va in $(-1, -2)$.
> 2. Zeri: $|x + 1| - 2 = 0$ significa $|x + 1| = 2$, cioè $x + 1 = 2$ oppure $x + 1 = -2$. Quindi $x = 1$ e $x = -3$.
> 3. Immagine: il punto più basso è il vertice, quindi $[-2, +\infty)$.
> 4. Monotonia: decrescente su $(-\infty, -1]$, crescente su $[-1, +\infty)$.

### La parabola e il vertice

Il grafico di una funzione di secondo grado $f(x) = ax^2 + bx + c$ (con $a \neq 0$) è una *parabola*. È la parabola $x^2$ allargata o stretta, magari capovolta, e traslata.

- Se $a > 0$ la parabola è rivolta verso l'alto (come un sorriso); se $a < 0$ è rivolta verso il basso.
- Il punto più basso (o più alto) si chiama *vertice*. La parabola è simmetrica rispetto alla retta verticale che passa per il vertice, detta *asse* della parabola.

> [!abstract] Vertice e immagine della parabola $y = ax^2 + bx + c$
> $$
> x_V = -\frac{b}{2a}, \qquad y_V = f(x_V)
> $$
> - Se $a > 0$: l'immagine è $[y_V, +\infty)$; decrescente prima del vertice, crescente dopo.
> - Se $a < 0$: l'immagine è $(-\infty, y_V]$; crescente prima del vertice, decrescente dopo.
> - Gli zeri sono le soluzioni dell'equazione di secondo grado $ax^2 + bx + c = 0$ (pagina [[01-equazioni-e-disequazioni]]): due, uno o nessuno a seconda del segno del discriminante $\Delta = b^2 - 4ac$.
>
> Se la funzione è già scritta nella forma $a(x - h)^2 + k$, il vertice si legge subito: è $(h, k)$.

> [!example] Esempio: $-(x-1)^2 + 4$ (esercizio 12, prima pagina)
> ![[05-parabola.svg|400]]
>
> 1. La funzione è nella forma $a(x - h)^2 + k$ con $a = -1$, $h = 1$, $k = 4$. Quindi il vertice è $V(1, 4)$ e, siccome $a < 0$, la parabola è rivolta verso il basso.
> 2. Immagine: il vertice è il punto più alto, quindi $(-\infty, 4]$.
> 3. Zeri: $-(x-1)^2 + 4 = 0 \iff (x-1)^2 = 4 \iff x - 1 = \pm 2$, quindi $x = 3$ e $x = -1$.
> 4. Intersezione con l'asse $y$: $f(0) = -1 + 4 = 3$.
> 5. Controllo con la formula: sviluppando, $f(x) = -x^2 + 2x + 3$, e $x_V = -\frac{2}{2 \cdot (-1)} = 1$. Torna.

## ESPONENZIALI E LOGARITMI

### Le potenze con esponente reale

Finora l'esponente era fisso e la base variava ($x^2$, $x^3$). Nella funzione esponenziale succede il contrario: la base è un numero fisso $a$ e l'esponente è la variabile, $a^x$. Prima di disegnarla conviene ricordare le regole delle potenze, che valgono per qualunque esponente reale (con base $a > 0$).

> [!abstract] Regole delle potenze (con $a > 0$)
> $$
> a^0 = 1 \qquad a^{-x} = \frac{1}{a^x} \qquad a^{\frac{1}{n}} = \sqrt[n]{a}
> $$
> $$
> a^x \cdot a^y = a^{x+y} \qquad \frac{a^x}{a^y} = a^{x-y} \qquad (a^x)^y = a^{x \cdot y}
> $$

Per esempio $2^{-3} = \frac{1}{8}$, $8^{\frac13} = 2$, $9^{\frac32} = (\sqrt{9})^3 = 27$.

La base deve essere positiva perché con una base negativa molte potenze non hanno senso: $(-4)^{\frac12}$ sarebbe $\sqrt{-4}$, che non esiste. E si esclude anche $a = 1$, perché $1^x = 1$ sempre: sarebbe solo una retta orizzontale.

### La funzione esponenziale

La *funzione esponenziale* di base $a$ (con $a > 0$ e $a \neq 1$) è $f(x) = a^x$.

![[05-esponenziali.svg|460]]

Si capisce la forma con qualche valore di $2^x$: $2^{-2} = \frac14$, $2^{-1} = \frac12$, $2^0 = 1$, $2^1 = 2$, $2^2 = 4$, $2^3 = 8$. Ogni passo verso destra raddoppia il valore: la crescita è lentissima a sinistra e velocissima a destra. Verso sinistra i valori si dimezzano sempre ma non arrivano mai a zero: l'asse $x$ è un asintoto.

Con una base minore di $1$, come $\left(\frac12\right)^x$, succede il contrario: ogni passo verso destra dimezza il valore. Infatti $\left(\frac12\right)^x = 2^{-x}$, quindi il suo grafico è quello di $2^x$ riflesso rispetto all'asse $y$.

> [!abstract] Scheda di $f(x) = a^x$
> - Dominio: $\mathbb{R}$. Immagine: $(0, +\infty)$: un esponenziale è sempre positivo.
> - Passa sempre per $(0, 1)$, perché $a^0 = 1$, e per $(1, a)$.
> - Monotonia: crescente se $a > 1$, decrescente se $0 < a < 1$.
> - Zeri: nessuno.
> - Parità: né pari né dispari.
> - Asintoti: orizzontale $y = 0$ (a sinistra se $a > 1$, a destra se $0 < a < 1$).
> - Inversa: esiste, perché la funzione è monotona. È il logaritmo in base $a$.

Dal fatto che l'esponenziale è monotono discende la regola che serve per risolvere le equazioni:

$$
a^{x_1} = a^{x_2} \iff x_1 = x_2
$$

Cioè: due potenze con la stessa base sono uguali solo se hanno lo stesso esponente.

### Il numero e

Fra tutte le basi possibili ce n'è una speciale, il *numero di Nepero* $e$:

$$
e \approx 2{,}718
$$

È un numero irrazionale, come $\pi$: le sue cifre decimali non finiscono mai e non si ripetono. Lo si può ottenere calcolando $\left(1 + \frac1n\right)^n$ con $n$ sempre più grande: con $n = 1000$ si ottiene già $2{,}7169$.

La funzione $e^x$ (nel disegno in verde) si chiama semplicemente *la* funzione esponenziale. Sta fra $2^x$ e $3^x$, e ha una proprietà che la rende la più comoda di tutte: nel punto $(0, 1)$ la retta tangente al suo grafico ha pendenza esattamente $1$. Il motivo per cui questo conta si vedrà con le derivate; per ora basta sapere che in matematica, in fisica e in biologia la base usata quasi sempre è $e$.

### Il logaritmo come inversa dell'esponenziale

La domanda che il logaritmo risolve è: «a quale numero devo elevare $a$ per ottenere $x$?».

> [!abstract] Definizione di logaritmo
> Con $a > 0$, $a \neq 1$ e $x > 0$:
> $$
> \log_a x = y \iff a^y = x
> $$
> Il numero $a$ si chiama *base*, il numero $x$ si chiama *argomento*. Il logaritmo è l'esponente.

Per esempio $\log_2 8 = 3$ perché $2^3 = 8$, e $\log_{10} 100 = 2$ perché $10^2 = 100$.

L'argomento deve essere positivo per un motivo preciso: $a^y$ è sempre positivo, quindi non esiste nessun esponente che dia $0$ o un numero negativo. Il logaritmo di $0$ o di un numero negativo non esiste.

Il logaritmo è l'inversa dell'esponenziale, quindi i due grafici sono simmetrici rispetto alla bisettrice $y = x$. Nel disegno ogni punto di $2^x$ ha il suo gemello su $\log_2 x$ con le coordinate scambiate: $(2, 4)$ e $(4, 2)$, $(1, 2)$ e $(2, 1)$, $(0, 1)$ e $(1, 0)$.

![[05-esp-log-simmetrici.svg|480]]

Tutta la scheda del logaritmo si ricava da quella dell'esponenziale scambiando $x$ con $y$: il dominio del logaritmo è l'immagine dell'esponenziale, l'asintoto orizzontale $y = 0$ diventa l'asintoto verticale $x = 0$, il punto $(0, 1)$ diventa $(1, 0)$.

![[05-logaritmi.svg|460]]

> [!abstract] Scheda di $f(x) = \log_a x$
> - Dominio: $(0, +\infty)$. Immagine: $\mathbb{R}$.
> - Passa sempre per $(1, 0)$, perché $\log_a 1 = 0$, e per $(a, 1)$, perché $\log_a a = 1$.
> - Monotonia: crescente se $a > 1$, decrescente se $0 < a < 1$.
> - Zero: $x = 1$.
> - Parità: non ha senso chiederla (il dominio non è simmetrico).
> - Asintoti: verticale $x = 0$.
> - Segno (con $a > 1$): negativo per $0 < x < 1$, positivo per $x > 1$.
> - Inversa: $a^x$. Valgono sempre $\log_a(a^x) = x$ per ogni $x$ e $a^{\log_a x} = x$ per ogni $x > 0$.

> [!example] Esempio: calcolare logaritmi (esercizio 1, seconda pagina)
> - $\log_3 27$: a quanto devo elevare $3$ per avere $27$? Siccome $3^3 = 27$, $\log_3 27 = 3$.
> - $\log_4 \frac12$: scrivo tutto come potenza di $2$. $4 = 2^2$ e $\frac12 = 2^{-1}$. Cerco $y$ con $4^y = \frac12$, cioè $2^{2y} = 2^{-1}$, quindi $2y = -1$ e $y = -\frac12$.
> - $\ln(e^5) = 5$, perché il logaritmo naturale e $e^x$ si annullano a vicenda.
> - $e^{\ln 7} = 7$, per lo stesso motivo.

### Le proprietà dei logaritmi

Siccome il logaritmo è un esponente, le regole delle potenze diventano regole dei logaritmi. Per esempio $a^x \cdot a^y = a^{x+y}$ dice che, moltiplicando due numeri, gli esponenti si sommano: quindi il logaritmo di un prodotto è la somma dei logaritmi.

> [!abstract] Proprietà dei logaritmi (con $x > 0$, $y > 0$)
> $$
> \log_a(x \cdot y) = \log_a x + \log_a y
> $$
> $$
> \log_a \frac{x}{y} = \log_a x - \log_a y
> $$
> $$
> \log_a(x^k) = k \cdot \log_a x
> $$
> E inoltre: $\log_a 1 = 0$, $\;\log_a a = 1$, $\;\log_a \frac1x = -\log_a x$.

Per esempio $\log_2 12 - \log_2 3 = \log_2 \frac{12}{3} = \log_2 4 = 2$.

> [!warning] Errori tipici con i logaritmi
> - $\log_a(x + y)$ non è $\log_a x + \log_a y$. Il logaritmo di una somma non si semplifica.
> - $\ln(x^2) = 2 \ln x$ è falso «per ogni $x \neq 0$» (esercizio 17): per $x = -3$ a sinistra c'è $\ln 9$, che esiste, mentre a destra c'è $2 \ln(-3)$, che non esiste. La formula giusta è $\ln(x^2) = 2 \ln |x|$.
> - Le proprietà valgono solo se tutti gli argomenti sono positivi. Per questo nelle equazioni si scrive sempre prima il dominio.

### Il cambio di base e il logaritmo naturale

Due basi hanno un nome proprio:

- il *logaritmo naturale* $\ln x$ è il logaritmo in base $e$: $\ln x = \log_e x$;
- il *logaritmo decimale* $\log_{10} x$ è il logaritmo in base $10$ (a volte scritto $\log x$, ma attenzione: in molti libri universitari $\log x$ senza base indica il logaritmo naturale).

La calcolatrice ha di solito solo il tasto $\ln$ (e quello in base $10$). Per un'altra base si usa la formula del cambio di base.

> [!abstract] Cambio di base
> $$
> \log_a x = \frac{\ln x}{\ln a}
> $$
> (Al posto di $\ln$ si può usare un logaritmo in qualunque base, purché sia la stessa sopra e sotto.)

Perché funziona: se $y = \log_a x$, allora $a^y = x$. Applicando $\ln$ ai due lati si ha $\ln(a^y) = \ln x$, cioè $y \ln a = \ln x$, e quindi $y = \frac{\ln x}{\ln a}$.

> [!example] Esempi di cambio di base
> - $\log_3 5 = \dfrac{\ln 5}{\ln 3} \approx \dfrac{1{,}609}{1{,}099} \approx 1{,}465$. Controllo: $3^{1{,}465} \approx 5$.
> - $\log_{\frac12} x = \dfrac{\ln x}{\ln \frac12} = \dfrac{\ln x}{-\ln 2} = -\log_2 x$. Ecco perché nel disegno il grafico di $\log_{\frac12} x$ (rosso) è quello di $\log_2 x$ capovolto rispetto all'asse $x$.

### Le equazioni esponenziali e logaritmiche

Per le equazioni esponenziali ci sono due strade.

1. Se si riesce, si scrivono i due lati come potenze della stessa base e si uguagliano gli esponenti.
2. Altrimenti si applica il logaritmo (di solito $\ln$) ai due lati, così l'incognita «scende» dall'esponente.

> [!example] Esempio: $3^{2x - 1} = 27$ (esercizio 2, seconda pagina)
> 1. $27 = 3^3$, quindi l'equazione diventa $3^{2x-1} = 3^3$.
> 2. Stessa base, quindi stessi esponenti: $2x - 1 = 3$.
> 3. $2x = 4$, cioè $x = 2$. Verifica: $3^{4-1} = 3^3 = 27$.

> [!example] Esempio: $e^{2x} = 7$ (esercizio 3, seconda pagina)
> 1. $7$ non è una potenza «comoda» di $e$, quindi si applica $\ln$ ai due lati: $\ln(e^{2x}) = \ln 7$.
> 2. $\ln(e^{2x}) = 2x$, quindi $2x = \ln 7$.
> 3. $x = \dfrac{\ln 7}{2} \approx 0{,}973$.

Per le equazioni logaritmiche il primo passo è sempre il dominio: tutti gli argomenti dei logaritmi devono essere positivi. Poi si usano le proprietà per arrivare a un solo logaritmo per lato, e si tolgono i logaritmi. Alla fine si controlla che le soluzioni stiano nel dominio.

> [!example] Esempio: $\ln(x - 2) = 3$ (esercizio 3, seconda pagina)
> 1. Dominio: $x - 2 > 0$, cioè $x > 2$.
> 2. Per la definizione di logaritmo, $\ln(x-2) = 3$ significa $e^3 = x - 2$.
> 3. Quindi $x = 2 + e^3 \approx 22{,}09$, che sta nel dominio.

> [!example] Esempio: $\ln x + \ln(x - 1) = \ln 6$ (esercizio 5, seconda pagina)
> 1. Dominio: servono $x > 0$ e $x - 1 > 0$, quindi $x > 1$.
> 2. Proprietà del prodotto: $\ln x + \ln(x - 1) = \ln\big(x(x-1)\big)$. L'equazione diventa $\ln\big(x(x-1)\big) = \ln 6$.
> 3. Il logaritmo è iniettivo, quindi $x(x - 1) = 6$, cioè $x^2 - x - 6 = 0$.
> 4. $\Delta = 1 + 24 = 25$, quindi $x = \dfrac{1 \pm 5}{2}$: $x = 3$ oppure $x = -2$.
> 5. Solo $x = 3$ sta nel dominio $x > 1$. La soluzione è $x = 3$.

> [!warning] Senza dominio si sbaglia
> Nell'esempio sopra $x = -2$ risolve l'equazione di secondo grado ma non quella di partenza: $\ln(-2)$ non esiste. Se non si scrive il dominio all'inizio, la soluzione sbagliata resta.

### Le disequazioni esponenziali e logaritmiche

Le disequazioni si risolvono come le equazioni, con un'attenzione in più: il verso.

Se la base è maggiore di $1$, la funzione è crescente: il numero più grande ha l'esponente (o l'argomento) più grande, e il verso resta com'è. Se la base è fra $0$ e $1$, la funzione è decrescente: il numero più grande ha l'esponente più piccolo, e il verso si inverte.

> [!abstract] La regola del verso
> - Base $a > 1$: $\;a^{f(x)} < a^{g(x)} \iff f(x) < g(x)$ e $\;\log_a f(x) < \log_a g(x) \iff f(x) < g(x)$.
> - Base $0 < a < 1$: $\;a^{f(x)} < a^{g(x)} \iff f(x) > g(x)$ e $\;\log_a f(x) < \log_a g(x) \iff f(x) > g(x)$.
>
> Con i logaritmi, prima di tutto si impone il dominio (argomenti positivi).

> [!example] Esempio: $\left(\frac12\right)^{x-2} \leq \frac18$ (esercizio 2, seconda pagina)
> 1. $\frac18 = \left(\frac12\right)^3$, quindi: $\left(\frac12\right)^{x-2} \leq \left(\frac12\right)^3$.
> 2. La base $\frac12$ è minore di $1$: togliendo la base il verso si inverte. $x - 2 \geq 3$.
> 3. Quindi $x \geq 5$.
> 4. Controllo con un numero: per $x = 6$ si ha $\left(\frac12\right)^4 = \frac{1}{16}$, che è davvero $\leq \frac18$.

> [!example] Esempio: $\log_{\frac13}(2x + 1) < -1$ (esercizio 6, seconda pagina)
> 1. Dominio: $2x + 1 > 0$, cioè $x > -\frac12$.
> 2. Scrivo $-1$ come logaritmo nella stessa base: $-1 = \log_{\frac13} 3$, perché $\left(\frac13\right)^{-1} = 3$.
> 3. La disequazione è $\log_{\frac13}(2x+1) < \log_{\frac13} 3$. La base è minore di $1$, quindi il verso si inverte: $2x + 1 > 3$.
> 4. $2x > 2$, cioè $x > 1$.
> 5. Si mette insieme al dominio: $x > 1$ e $x > -\frac12$ danno $x > 1$.

### I domini con logaritmi e radici

Gli esercizi sul dominio mettono insieme le condizioni già viste nella pagina [[04-le-funzioni]] con quella nuova del logaritmo.

> [!abstract] Condizioni per il dominio
> - Denominatore: diverso da $0$.
> - Radice di indice pari: argomento $\geq 0$.
> - Logaritmo: argomento $> 0$ (strettamente).
>
> Se ci sono più condizioni, devono valere tutte insieme: si risolve il sistema.

> [!example] Esempio: tre domini (esercizio 4, seconda pagina)
> - $\ln(9 - x^2)$: serve $9 - x^2 > 0$, cioè $x^2 < 9$, cioè $-3 < x < 3$. Dominio $(-3, 3)$.
> - $\dfrac{\ln(x+1)}{x-2}$: servono $x + 1 > 0$ (logaritmo) e $x - 2 \neq 0$ (denominatore). Quindi $x > -1$ e $x \neq 2$: dominio $(-1, 2) \cup (2, +\infty)$.
> - $\sqrt{\ln x}$: servono $x > 0$ (logaritmo) e $\ln x \geq 0$ (radice). Il logaritmo naturale è $\geq 0$ quando $x \geq 1$. Dominio $[1, +\infty)$.

> [!example] Esempio: grafici traslati (esercizio 9, seconda pagina)
> ![[05-esercizio-esp-log.svg|440]]
>
> $2^x - 1$ è il grafico di $2^x$ abbassato di $1$:
> - dominio $\mathbb{R}$, immagine $(-1, +\infty)$;
> - asintoto orizzontale $y = -1$;
> - passa per l'origine, perché $2^0 - 1 = 0$: è l'unico zero ed è anche l'intersezione con l'asse $y$.
>
> $\ln(x + 2)$ è il grafico di $\ln x$ spostato di $2$ verso sinistra:
> - dominio $x > -2$, immagine $\mathbb{R}$;
> - asintoto verticale $x = -2$;
> - zero: $\ln(x+2) = 0 \iff x + 2 = 1 \iff x = -1$;
> - intersezione con l'asse $y$: $\ln 2 \approx 0{,}69$.

> [!example] Esempio: $f(x) = 3 - e^{-x}$ (esercizio 7, seconda pagina)
> 1. Monotonia: $e^{-x}$ è decrescente (è $\left(\frac1e\right)^x$), quindi $-e^{-x}$ è crescente e anche $3 - e^{-x}$ è crescente.
> 2. Immagine: $e^{-x}$ assume tutti i valori di $(0, +\infty)$, quindi $3 - e^{-x}$ assume tutti i valori minori di $3$: immagine $(-\infty, 3)$.
> 3. Inversa: da $y = 3 - e^{-x}$ si ricava $e^{-x} = 3 - y$, poi $-x = \ln(3 - y)$, quindi $f^{-1}(y) = -\ln(3 - y)$, definita per $y < 3$ (cioè proprio sull'immagine).

### La crescita esponenziale e il tempo di raddoppio

Molti fenomeni crescono «a percentuale fissa»: una popolazione, un capitale in banca, una colonia di batteri. In tempi uguali aumentano dello stesso fattore, e il modello è una funzione esponenziale:

$$
N(t) = N_0 \, e^{kt}
$$

Qui $N_0 = N(0)$ è il valore iniziale e $k > 0$ è il tasso di crescita. Se $k < 0$ il fenomeno decresce (decadimento radioattivo, raffreddamento).

Il *tempo di raddoppio* è il tempo che serve perché il valore diventi il doppio. Ha una proprietà sorprendente: non dipende da quanto si ha all'inizio, e ogni volta che passa quel tempo il valore raddoppia di nuovo.

> [!abstract] Tempo di raddoppio
> $$
> N_0 \, e^{kT} = 2 N_0 \iff e^{kT} = 2 \iff T = \frac{\ln 2}{k}
> $$

> [!example] Esempio: la popolazione (esercizio 8, seconda pagina)
> $N(t) = 200 \, e^{0{,}04\, t}$. Il tempo di raddoppio è $T = \dfrac{\ln 2}{0{,}04} \approx \dfrac{0{,}693}{0{,}04} \approx 17{,}3$ anni.
>
> ![[05-crescita-raddoppio.svg|560]]
>
> Dopo $17{,}3$ anni la popolazione è $400$, dopo $34{,}7$ anni è $800$, dopo $52$ anni è $1600$.

> [!example] Esempio: il raffreddamento (esercizio 20, seconda pagina)
> Una temperatura segue $T(t) = 20 + 60\, e^{-0{,}1\, t}$ per $t \geq 0$.
>
> 1. Temperatura iniziale: $T(0) = 20 + 60 \cdot 1 = 80$ gradi.
> 2. Quando arriva a $50$ gradi? $20 + 60\, e^{-0{,}1 t} = 50 \iff e^{-0{,}1 t} = \frac12 \iff -0{,}1\, t = \ln \frac12 = -\ln 2 \iff t = 10 \ln 2 \approx 6{,}93$.
> 3. Immagine: l'esponenziale decrescente va da $1$ verso $0$ senza arrivarci, quindi la temperatura parte da $80$ e scende verso $20$ (la temperatura dell'ambiente) senza mai raggiungerla. Immagine $(20, 80]$.

## TRIGONOMETRIA

### Gli angoli in radianti

In geometria gli angoli si misurano in gradi; in analisi si usano i *radianti*. Un radiante è l'angolo che, in una circonferenza di raggio $r$, stacca un arco lungo esattamente $r$.

![[05-radiante.svg|420]]

In generale la misura in radianti di un angolo è il rapporto fra la lunghezza dell'arco e il raggio:

$$
\alpha = \frac{\text{arco}}{\text{raggio}}
$$

L'intera circonferenza è lunga $2\pi r$, quindi l'angolo giro misura $\frac{2\pi r}{r} = 2\pi$ radianti. Da qui la regola di conversione.

> [!abstract] Gradi e radianti
> $$
> 180° = \pi \text{ rad} \qquad\qquad \alpha_{\text{rad}} = \alpha_{\text{gradi}} \cdot \frac{\pi}{180}
> $$
> - $30° = \frac{\pi}{6}$, $\;45° = \frac{\pi}{4}$, $\;60° = \frac{\pi}{3}$, $\;90° = \frac{\pi}{2}$
> - $180° = \pi$, $\;270° = \frac{3\pi}{2}$, $\;360° = 2\pi$
> - $1$ rad $\approx 57{,}3°$

Il vantaggio dei radianti è che sono numeri puri (una lunghezza divisa per una lunghezza), e così si possono mettere sull'asse $x$ di un grafico come qualunque altro numero.

### La circonferenza goniometrica: seno, coseno e tangente

La *circonferenza goniometrica* è la circonferenza di centro l'origine e raggio $1$, di equazione $x^2 + y^2 = 1$ (pagina [[02-retta-e-circonferenza]]). Gli angoli si misurano partendo dal semiasse positivo delle $x$ e girando in senso antiorario; un angolo negativo gira in senso orario.

Ogni angolo $\alpha$ individua un punto $P$ sulla circonferenza.

![[05-circonferenza-goniometrica.svg|480]]

> [!abstract] Definizione di seno, coseno e tangente
> Se $P$ è il punto della circonferenza goniometrica corrispondente all'angolo $\alpha$:
> - il *coseno* $\cos\alpha$ è l'ascissa (la $x$) di $P$;
> - il *seno* $\sin\alpha$ è l'ordinata (la $y$) di $P$;
> - la *tangente* è il loro rapporto, definita quando $\cos\alpha \neq 0$:
> $$
> \tan\alpha = \frac{\sin\alpha}{\cos\alpha}
> $$

Da questa definizione seguono subito alcune conseguenze.

- Seno e coseno stanno sempre fra $-1$ e $1$, perché $P$ sta su una circonferenza di raggio $1$.
- Vale la *relazione fondamentale*, che è il teorema di Pitagora nel triangolo rettangolo del disegno (cateti $\cos\alpha$ e $\sin\alpha$, ipotenusa $1$):

$$
\sin^2\alpha + \cos^2\alpha = 1
$$

- La tangente è la pendenza della retta $OP$: si sale di $\sin\alpha$ mentre si avanza di $\cos\alpha$. Nel disegno è il segmento verde staccato sulla retta verticale $x = 1$. Quando $\alpha = \frac{\pi}{2}$ la retta $OP$ è verticale e la tangente non esiste.
- I segni dipendono dal quadrante: nel primo quadrante sono tutti positivi; nel secondo il seno è positivo e il coseno negativo; nel terzo seno e coseno sono negativi (e la tangente positiva); nel quarto il coseno è positivo e il seno negativo.

### I valori notevoli

Per alcuni angoli seno e coseno si calcolano esattamente.

- Per $\frac{\pi}{4}$ ($45°$) il triangolo rettangolo è metà di un quadrato di diagonale $1$: i due cateti sono uguali e valgono $\frac{\sqrt2}{2}$.
- Per $\frac{\pi}{6}$ ($30°$) e $\frac{\pi}{3}$ ($60°$) il triangolo è metà di un triangolo equilatero di lato $1$: il cateto corto è $\frac12$ e quello lungo, per Pitagora, $\frac{\sqrt3}{2}$.

| angolo | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ |
|---|---|---|---|---|---|---|---|
| gradi | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $270°$ |
| $\sin$ | $0$ | $\frac12$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ | $0$ | $-1$ |
| $\cos$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac12$ | $0$ | $-1$ | $0$ |
| $\tan$ | $0$ | $\frac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | non esiste | $0$ | non esiste |

Gli angoli negli altri quadranti si ricavano per simmetria dalla circonferenza: hanno gli stessi valori in valore assoluto, e cambia solo il segno.

![[05-angoli-notevoli.svg|500]]

> [!abstract] Simmetrie utili
> - $\sin(\pi - \alpha) = \sin\alpha$ e $\cos(\pi - \alpha) = -\cos\alpha$ (simmetria rispetto all'asse $y$)
> - $\sin(-\alpha) = -\sin\alpha$ e $\cos(-\alpha) = \cos\alpha$ (simmetria rispetto all'asse $x$)
> - $\sin(\alpha + \pi) = -\sin\alpha$ e $\cos(\alpha + \pi) = -\cos\alpha$ (simmetria rispetto all'origine)

Per esempio $\sin\frac{2\pi}{3} = \sin\left(\pi - \frac{\pi}{3}\right) = \frac{\sqrt3}{2}$ e $\cos\frac{2\pi}{3} = -\frac12$.

### La periodicità e i grafici

Se a un angolo si aggiunge un giro completo, $2\pi$, si torna nello stesso punto $P$. Quindi seno e coseno si ripetono ogni $2\pi$: si dice che sono *periodiche* di periodo $2\pi$.

$$
\sin(x + 2\pi) = \sin x \qquad \cos(x + 2\pi) = \cos x
$$

La tangente si ripete già dopo mezzo giro, perché $P$ e il punto opposto danno la stessa retta $OP$: il suo periodo è $\pi$, cioè $\tan(x + \pi) = \tan x$.

Mettendo l'angolo $x$ sull'asse orizzontale e il valore sull'asse verticale si ottengono i grafici. Il seno parte da $0$, sale fino a $1$ in $\frac{\pi}{2}$, torna a $0$ in $\pi$, scende a $-1$ in $\frac{3\pi}{2}$ e torna a $0$ in $2\pi$. Il coseno ha la stessa forma, spostata di $\frac{\pi}{2}$ verso sinistra.

![[05-seno-coseno.svg|600]]

> [!abstract] Schede di seno e coseno
> $f(x) = \sin x$:
> - dominio $\mathbb{R}$, immagine $[-1, 1]$, periodo $2\pi$;
> - dispari (grafico simmetrico rispetto all'origine);
> - zeri: $x = k\pi$ con $k$ intero;
> - crescente su $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, poi decrescente su $\left[\frac{\pi}{2}, \frac{3\pi}{2}\right]$, e così via.
>
> $f(x) = \cos x$:
> - dominio $\mathbb{R}$, immagine $[-1, 1]$, periodo $2\pi$;
> - pari (grafico simmetrico rispetto all'asse $y$);
> - zeri: $x = \frac{\pi}{2} + k\pi$;
> - decrescente su $[0, \pi]$, crescente su $[\pi, 2\pi]$.
>
> Nessuna delle due ha asintoti, e su tutto $\mathbb{R}$ nessuna delle due è invertibile (ogni valore viene ripetuto infinite volte).

![[05-tangente.svg|520]]

> [!abstract] Scheda della tangente
> - Dominio: tutti i numeri tranne $\frac{\pi}{2} + k\pi$ (dove il coseno vale $0$).
> - Immagine: $\mathbb{R}$. Periodo: $\pi$.
> - Dispari. Zeri: $x = k\pi$.
> - Crescente su ogni intervallo $\left(-\frac{\pi}{2} + k\pi, \frac{\pi}{2} + k\pi\right)$.
> - Asintoti verticali: $x = \frac{\pi}{2} + k\pi$.

### La funzione A cos(Bx) + C

Nelle applicazioni (onde, oscillazioni, temperature che variano nell'arco dell'anno) il coseno compare quasi sempre modificato da tre numeri:

$$
f(x) = A\cos(Bx) + C
$$

Ognuno dei tre numeri ha un effetto preciso sul grafico.

- $A$ stira il grafico in verticale. L'*ampiezza*, cioè quanto il grafico sale e scende rispetto al centro, è $|A|$.
- $B$ comprime il grafico in orizzontale. Il coseno compie un'oscillazione completa quando $Bx$ va da $0$ a $2\pi$, cioè quando $x$ va da $0$ a $\frac{2\pi}{|B|}$: questo è il *periodo*.
- $C$ sposta tutto in alto. La retta $y = C$ è la retta centrale attorno a cui il grafico oscilla.

> [!abstract] Ampiezza, periodo e immagine di $A\cos(Bx) + C$
> $$
> \text{ampiezza} = |A| \qquad \text{periodo} = \frac{2\pi}{|B|} \qquad \text{immagine} = \big[\,C - |A|,\; C + |A|\,\big]
> $$
> Le stesse formule valgono per $A\sin(Bx) + C$.

> [!example] Esempio: $h(x) = 3\cos(2x) + 2$ (esercizio 10, seconda pagina)
> ![[05-coseno-trasformato.svg|480]]
>
> 1. Ampiezza: $|A| = 3$.
> 2. Periodo: $\frac{2\pi}{2} = \pi$. Il grafico compie un'oscillazione completa fra $0$ e $\pi$, cioè due volte più in fretta di $\cos x$ (tratteggiato).
> 3. Immagine: $\cos(2x)$ varia fra $-1$ e $1$; moltiplicando per $3$ varia fra $-3$ e $3$; aggiungendo $2$ varia fra $-1$ e $5$. Quindi $[-1, 5]$.

### Le equazioni trigonometriche elementari

Un'equazione come $\sin x = k$ chiede: quali angoli hanno seno uguale a $k$? Sulla circonferenza goniometrica si traccia la retta orizzontale $y = k$ e si guarda dove taglia la circonferenza.

- Se $|k| > 1$ la retta non tocca la circonferenza: nessuna soluzione.
- Se $|k| < 1$ la retta taglia la circonferenza in due punti, simmetrici rispetto all'asse $y$: gli angoli $\alpha$ e $\pi - \alpha$.
- Se $k = 1$ o $k = -1$ la retta tocca la circonferenza in un punto solo.

Per $\cos x = k$ si usa invece la retta verticale $x = k$: i due punti sono simmetrici rispetto all'asse $x$, cioè gli angoli $\alpha$ e $-\alpha$ (che in $[0, 2\pi)$ si scrive $2\pi - \alpha$).

> [!abstract] Soluzioni delle equazioni elementari
> Se $\alpha$ è un angolo che risolve l'equazione:
> - $\sin x = k \;\Rightarrow\; x = \alpha + 2k\pi \;$ oppure $\; x = \pi - \alpha + 2k\pi$
> - $\cos x = k \;\Rightarrow\; x = \alpha + 2k\pi \;$ oppure $\; x = -\alpha + 2k\pi$
> - $\tan x = k \;\Rightarrow\; x = \alpha + k\pi \;$ (un solo punto ogni mezzo giro)
>
> Qui $k$ nella parte destra indica un numero intero qualunque. Su $[0, 2\pi]$ si prendono solo le soluzioni che cadono in quell'intervallo; su $\mathbb{R}$ si scrivono tutte, con il $+\,2k\pi$ (o $+\,k\pi$ per la tangente).

> [!example] Esempio: su $[0, 2\pi]$ (esercizio 14, seconda pagina)
> ![[05-equazione-seno.svg|340]] ![[05-equazione-coseno.svg|340]]
>
> $\sin x = \frac{\sqrt3}{2}$:
> 1. Dalla tabella, $\sin\frac{\pi}{3} = \frac{\sqrt3}{2}$: prima soluzione $x = \frac{\pi}{3}$.
> 2. L'altra è simmetrica rispetto all'asse $y$: $x = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$.
>
> $\cos x = -\frac12$:
> 1. Dalla tabella, $\cos\frac{\pi}{3} = \frac12$; il coseno negativo vuol dire secondo o terzo quadrante. $\cos\left(\pi - \frac{\pi}{3}\right) = -\frac12$: prima soluzione $x = \frac{2\pi}{3}$.
> 2. L'altra è simmetrica rispetto all'asse $x$: $x = 2\pi - \frac{2\pi}{3} = \frac{4\pi}{3}$.

> [!example] Esempio: su $\mathbb{R}$ (esercizio 15, seconda pagina)
> $\tan x = -1$:
> 1. $\tan\frac{\pi}{4} = 1$ e la tangente è dispari, quindi $\tan\left(-\frac{\pi}{4}\right) = -1$.
> 2. La tangente ha periodo $\pi$: $x = -\frac{\pi}{4} + k\pi$, con $k$ intero.
>
> $2\sin x - 1 = 0$:
> 1. Si isola il seno: $\sin x = \frac12$.
> 2. $\sin\frac{\pi}{6} = \frac12$, e l'angolo simmetrico è $\pi - \frac{\pi}{6} = \frac{5\pi}{6}$.
> 3. Su tutto $\mathbb{R}$: $x = \frac{\pi}{6} + 2k\pi$ oppure $x = \frac{5\pi}{6} + 2k\pi$.

> [!example] Esempio: un dominio con il seno (esercizio 13, seconda pagina)
> $\ln(\sin x)$ richiede $\sin x > 0$. Il seno è positivo quando $P$ sta sopra l'asse $x$, cioè per $0 < x < \pi$, e poi di nuovo a ogni giro. Dominio: $2k\pi < x < \pi + 2k\pi$.

### Le funzioni inverse: arcoseno, arcocoseno, arcotangente

Seno, coseno e tangente non sono invertibili su tutto $\mathbb{R}$, perché ripetono ogni valore infinite volte. Per avere un'inversa si fa come con $x^2$: si restringe il dominio a un intervallo su cui la funzione è monotona e prende tutti i suoi valori una volta sola.

> [!abstract] Le tre funzioni inverse
> - $\arcsin$ è l'inversa del seno ristretto a $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.
>   Dominio $[-1, 1]$, immagine $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$; crescente, dispari.
> - $\arccos$ è l'inversa del coseno ristretto a $[0, \pi]$.
>   Dominio $[-1, 1]$, immagine $[0, \pi]$; decrescente, né pari né dispari.
> - $\arctan$ è l'inversa della tangente ristretta a $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.
>   Dominio $\mathbb{R}$, immagine $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$; crescente, dispari; asintoti orizzontali $y = \frac{\pi}{2}$ e $y = -\frac{\pi}{2}$.
>
> In parole: $\arcsin y$ è l'angolo fra $-\frac{\pi}{2}$ e $\frac{\pi}{2}$ che ha seno $y$.

Come sempre, ogni grafico è il simmetrico della funzione ristretta rispetto alla bisettrice.

![[05-arcoseno.svg|420]]

![[05-arcocoseno.svg|440]]

![[05-arcotangente.svg|560]]

> [!example] Esempio: calcolare le inverse (esercizio 11, seconda pagina)
> - $\arcsin\left(-\frac12\right)$: cerco l'angolo in $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ con seno $-\frac12$. Siccome $\sin\frac{\pi}{6} = \frac12$ e il seno è dispari, è $-\frac{\pi}{6}$.
> - $\arccos\left(-\frac{\sqrt2}{2}\right)$: cerco l'angolo in $[0, \pi]$ con coseno $-\frac{\sqrt2}{2}$. Il coseno negativo vuol dire secondo quadrante: $\pi - \frac{\pi}{4} = \frac{3\pi}{4}$.
> - $\arctan\sqrt3 = \frac{\pi}{3}$, perché $\tan\frac{\pi}{3} = \sqrt3$.

> [!example] Esempio: domini con le inverse (esercizi 13 e 18, seconda pagina)
> - $\arccos(2x)$: serve $-1 \leq 2x \leq 1$, cioè $-\frac12 \leq x \leq \frac12$.
> - $\arcsin(x - 2)$: serve $-1 \leq x - 2 \leq 1$, cioè $1 \leq x \leq 3$.
> - $\arctan(\ln x)$: l'arcotangente accetta qualunque numero, quindi conta solo il logaritmo: dominio $x > 0$. Siccome $\ln x$ assume tutti i valori reali, l'immagine è tutta quella dell'arcotangente: $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.

> [!warning] Vero o falso (esercizio 17, seconda pagina)
> - «arccos è pari»: falso. Per esempio $\arccos(-1) = \pi$ ma $\arccos 1 = 0$. Vale invece $\arccos(-x) = \pi - \arccos x$.
> - «arctan x può valere $\frac{\pi}{2}$»: falso. $y = \frac{\pi}{2}$ è un asintoto: l'arcotangente ci si avvicina sempre di più ma non lo raggiunge mai, perché $\tan\frac{\pi}{2}$ non esiste.

> [!example] Esempio: l'arcocotangente (esercizio 19, seconda pagina)
> La *cotangente* è $\cot x = \dfrac{\cos x}{\sin x}$ e l'arcocotangente, con la convenzione dell'esercizio, va da $\mathbb{R}$ a $(0, \pi)$.
> - $\operatorname{arccot}(-1)$: cerco l'angolo in $(0, \pi)$ con $\frac{\cos x}{\sin x} = -1$, cioè con coseno e seno opposti. È $\frac{3\pi}{4}$ (coseno $-\frac{\sqrt2}{2}$, seno $\frac{\sqrt2}{2}$).
> - $\cot x = 0$: una frazione vale zero quando vale zero il numeratore, quindi $\cos x = 0$, cioè $x = \frac{\pi}{2} + k\pi$.

### Il problema di arcsin(sin x)

Siccome $\arcsin$ è l'inversa del seno, verrebbe da dire che $\arcsin(\sin x) = x$ sempre. Non è così, perché l'arcoseno restituisce solo angoli fra $-\frac{\pi}{2}$ e $\frac{\pi}{2}$.

> [!abstract] Quando inversa e funzione si annullano
> - $\sin(\arcsin y) = y$ per ogni $y \in [-1, 1]$: questo vale sempre.
> - $\arcsin(\sin x) = x$ solo se $x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.
> - $\arccos(\cos x) = x$ solo se $x \in [0, \pi]$.
> - $\arctan(\tan x) = x$ solo se $x \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.
>
> Se $x$ è fuori dall'intervallo, il risultato è l'angolo dentro l'intervallo che ha lo stesso seno (o coseno, o tangente).

> [!example] Esempio (esercizio 12, seconda pagina)
> - $\arcsin\left(\sin\frac{3\pi}{4}\right)$: $\frac{3\pi}{4}$ è fuori da $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$. Il suo seno è $\frac{\sqrt2}{2}$, e l'angolo dell'intervallo con quel seno è $\frac{\pi}{4}$. Risultato: $\frac{\pi}{4}$.
> - $\arccos\left(\cos\left(-\frac{\pi}{3}\right)\right)$: $-\frac{\pi}{3}$ è fuori da $[0, \pi]$. Il coseno è pari, quindi $\cos\left(-\frac{\pi}{3}\right) = \cos\frac{\pi}{3} = \frac12$, e l'angolo in $[0, \pi]$ con coseno $\frac12$ è $\frac{\pi}{3}$.
> - $\arctan\left(\tan\frac{3\pi}{4}\right)$: $\tan\frac{3\pi}{4} = -1$, e l'angolo in $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ con tangente $-1$ è $-\frac{\pi}{4}$.

### La pendenza in percentuale e l'angolo

Nelle strade, nelle rampe e nelle coperture la pendenza si indica in percentuale: dice di quanti metri si sale ogni $100$ metri percorsi in orizzontale. Una pendenza del $12\%$ significa $12$ metri di dislivello ogni $100$ metri in orizzontale.

Il rapporto fra dislivello e spostamento orizzontale è proprio la tangente dell'angolo di inclinazione (ed è anche il coefficiente angolare $m$ della retta che rappresenta la rampa).

![[05-pendenza.svg|560]]

> [!abstract] Dalla pendenza all'angolo
> $$
> \tan\alpha = \frac{\text{dislivello}}{\text{distanza orizzontale}} = \frac{p}{100} \qquad\Longrightarrow\qquad \alpha = \arctan\frac{p}{100}
> $$

> [!example] Esempio: la rampa al 12% (esercizio 16, seconda pagina)
> 1. $\tan\alpha = \frac{12}{100} = 0{,}12$.
> 2. $\alpha = \arctan 0{,}12 \approx 0{,}119$ radianti.
> 3. In gradi: $0{,}119 \cdot \frac{180}{\pi} \approx 6{,}8°$.

> [!warning] Il 100% non è un muro verticale
> Una pendenza del $100\%$ vuol dire $\tan\alpha = 1$, cioè $\alpha = 45°$. Una parete verticale avrebbe pendenza infinita, perché $\tan\frac{\pi}{2}$ non esiste. E la pendenza non è proporzionale all'angolo: raddoppiando la pendenza l'angolo non raddoppia: il $24\%$ corrisponde a circa $13{,}5°$, mentre il doppio di $6{,}8°$ sarebbe $13{,}7°$. Con le pendenze alte la differenza diventa grande: il $200\%$ non è $90°$, ma circa $63{,}4°$.

## Collegamenti

Questa pagina chiude la serie di teoria e ne usa quasi tutti gli strumenti. Le nozioni di dominio, immagine, iniettività, funzione inversa e traslazione dei grafici vengono da [[04-le-funzioni]]: qui vengono applicate una funzione alla volta, e la regola della simmetria rispetto alla bisettrice spiega in un colpo solo i grafici della radice, del logaritmo e delle funzioni arco. Gli zeri della parabola, i domini e le disequazioni logaritmiche si riducono alle equazioni e disequazioni di primo e secondo grado di [[01-equazioni-e-disequazioni]], con l'unica regola nuova del verso che si inverte quando la base è minore di $1$.

La funzione lineare è la [[02-retta-e-circonferenza|retta]] già studiata in geometria analitica, e la circonferenza goniometrica è la circonferenza $x^2 + y^2 = 1$ della stessa pagina; il legame più utile è che il coefficiente angolare di una retta è la tangente dell'angolo che la retta forma con l'asse $x$, ed è la stessa idea della pendenza in percentuale. Anche i [[03-i-vettori|vettori]] tornano qui: un versore del piano si scrive sempre come $(\cos\theta, \sin\theta)$, e l'angolo fra due vettori si trova con il prodotto scalare e poi con l'arcocoseno, ed è per questo che l'immagine di $\arccos$ è $[0, \pi]$, proprio l'insieme degli angoli possibili fra due vettori.

Nel resto del corso queste funzioni diventano la base per i limiti (gli asintoti), per le derivate (il numero $e$ si giustifica lì) e per lo studio di funzione. In Architettura la trigonometria serve ogni volta che si passa da una pendenza a un angolo (rampe, scale, falde dei tetti), e in Geometria descrittiva l'inclinazione di una retta o di un piano rispetto al piano orizzontale è proprio un angolo di cui la pendenza è la tangente.

## Per approfondire

- [[Esercizi_funzioni_e_Logaritmi.pdf]], seconda pagina («Esponenziali, logaritmi e trigonometria»): tutti e venti gli esercizi sono svolti come esempi in questa pagina (il 17, un vero o falso, è diviso fra l'avvertenza sugli errori con i logaritmi e quella sulle funzioni inverse).
- [[Esercizi_funzioni_e_Logaritmi.pdf]], prima pagina: esercizi 10, 11, 12 e 15 (monotonia, valore assoluto, parabola, tariffa lineare).
- Il [[Programma del corso_Istituzioni_di_matematiche_1_canale_1.pdf|programma del corso]] mette esponenziale e logaritmo nella parte sulla continuità: il professore li riprenderà dopo i limiti.
- Il libro di testo adottato è lo Stewart, *Calcolo. Funzioni di una variabile*: le funzioni elementari, l'esponenziale, le inverse e il logaritmo sono nel primo capitolo, e la trigonometria è ripassata nelle appendici. Nella cartella del materiale c'è solo il capitolo sui vettori.
