---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Le funzioni

Una funzione è una regola che a ogni numero di partenza fa corrispondere uno e un solo numero di arrivo. È l'idea più importante di tutto il corso: i limiti, le derivate e gli integrali che verranno dopo sono tutti modi di studiare le funzioni. Questa pagina parte dalla definizione, passa al grafico, al dominio e all'immagine, poi alle proprietà (iniettiva, suriettiva, pari, crescente...) e alla funzione inversa, e alle operazioni che spostano e deformano i grafici. La seconda parte presenta le funzioni elementari: potenze, radici, valore assoluto, parabola, esponenziali, logaritmi e trigonometria. Gli esempi svolti seguono le due pagine del foglio del professore, `Esercizi_funzioni_e_Logaritmi.pdf`.

> [!info] Note collegate
> Teoria: [[01-insiemi-e-intervalli]] · [[02-equazioni-e-disequazioni]] · [[03-retta-e-circonferenza]] · [[04-le-matrici]] · [[05-i-vettori]] · Ripasso: [[00-ripasso-esonero-1]]

## CHE COS'È UNA FUNZIONE

### Dominio, codominio e legge

Per dare una funzione servono tre ingredienti:

1. un insieme di partenza $A$, che si chiama *dominio*;
2. un insieme di arrivo $B$, che si chiama *codominio*;
3. una *legge* (una regola) che a ogni elemento $x$ di $A$ associa un elemento di $B$, che si indica con $f(x)$.

Si scrive $f: A \to B$, e si legge «$f$ va da $A$ a $B$». Il numero $f(x)$ si chiama *valore* della funzione in $x$, oppure *immagine* di $x$.

La parte decisiva della definizione è «uno e un solo». Ogni elemento del dominio deve avere un valore, e uno soltanto. Gli elementi del codominio invece possono essere raggiunti da una freccia, da molte frecce o da nessuna: la definizione non chiede niente su di loro.

> [!abstract] Definizione di funzione
> Una funzione $f: A \to B$ è una legge che a ogni elemento $x \in A$ associa uno e un solo elemento $f(x) \in B$.
>
> - $A$ è il dominio, $B$ il codominio.
> - Ogni $x$ di $A$ deve avere un valore (nessuno resta senza).
> - Ogni $x$ di $A$ ha un solo valore (nessuno ne ha due).

Il modo più semplice per vedere se una corrispondenza è una funzione è disegnarla con le frecce: a sinistra gli elementi di $A$, a destra quelli di $B$, e una freccia da ogni $x$ al suo valore.

![[06-diagrammi-frecce.svg|700]]

- Nel primo disegno ogni elemento di $A$ ha esattamente una freccia. È una funzione, anche se $1$ e $2$ vanno entrambi in $a$ e nessuno va in $d$: questo è permesso.
- Nel secondo disegno da $1$ partono due frecce. Non è una funzione, perché $f(1)$ non sarebbe un numero solo.
- Nel terzo da $3$ non parte nessuna freccia. Non è una funzione da $A$ a $B$, perché $f(3)$ non esiste.

> [!example] Esempio: l'area del quadrato
> Il lato di un quadrato misura $s$ metri, con $s \in [1, 4]$ (esercizio 4 del foglio). L'area è
>
> $$
> A(s) = s^2 .
> $$
>
> È una funzione: dato il lato, l'area è una sola. Il dominio è l'insieme dei lati ammessi, $[1, 4]$ metri. Calcoliamo qualche valore: $A(1) = 1$, $A(2) = 4$, $A(3) = 9$, $A(4) = 16$. Le aree vanno quindi da $1$ a $16$ metri quadrati. Le unità di misura cambiano: il lato è in $\text{m}$, l'area in $\text{m}^2$.

> [!example] Esempio: una tariffa
> Un servizio costa $4$ euro fissi più $2$ euro per ogni ora di utilizzo (esercizio 15). Se $t$ è il numero di ore, il prezzo è
>
> $$
> T(t) = 4 + 2t, \qquad t \ge 0 .
> $$
>
> Per $3$ ore si paga $T(3) = 4 + 6 = 10$ euro. Anche qui a ogni durata corrisponde un solo prezzo.

### Variabile indipendente e variabile dipendente

Quando scriviamo $y = f(x)$, la lettera $x$ si chiama *variabile indipendente*: siamo noi a sceglierla, liberamente, dentro il dominio. La lettera $y$ si chiama *variabile dipendente*: il suo valore non si sceglie, dipende da $x$ attraverso la legge.

Nell'esempio del quadrato la variabile indipendente è il lato $s$ e quella dipendente è l'area $A$. Nella tariffa la variabile indipendente è il tempo $t$ e quella dipendente è il prezzo $T$. Il nome delle lettere non conta: conta chi decide e chi viene deciso.

### Il grafico di una funzione

Ogni coppia «numero di partenza, valore» si può pensare come un punto del piano cartesiano, con la $x$ in orizzontale e la $y$ in verticale.

> [!abstract] Definizione di grafico
> Il grafico di $f: A \to \mathbb{R}$ è l'insieme dei punti del piano
>
> $$
> G_f = \{\, (x, f(x)) \;:\; x \in A \,\}.
> $$
>
> Un punto $(a, b)$ sta sul grafico se e solo se $a$ è nel dominio e $b = f(a)$.

Il grafico è un disegno che contiene tutta la funzione. Per leggere un valore, per esempio $f(2)$, si parte da $x = 2$ sull'asse orizzontale, si sale (o si scende) in verticale fino a incontrare il grafico, e poi ci si sposta in orizzontale fino all'asse $y$: il numero che si legge è $f(2)$.

![[06-area-quadrato.svg|500]]

Nel grafico dell'area del quadrato si vede tutto quello che abbiamo detto. La curva blu è un pezzo di parabola, che parte dal punto $(1, 1)$ e arriva al punto $(4, 16)$. In verde, sull'asse orizzontale, c'è il dominio $[1, 4]$; in arancione, sull'asse verticale, ci sono i valori raggiunti, da $1$ a $16$. La parte tratteggiata della parabola non fa parte del grafico, perché quei lati non sono ammessi.

> [!example] Esempio: un punto sta sul grafico?
> Sia $f(x) = (x+1)^2 - 4$.
>
> - Il punto $(1, 0)$ sta sul grafico? Calcoliamo $f(1) = (1+1)^2 - 4 = 4 - 4 = 0$. Sì, perché $f(1) = 0$.
> - Il punto $(0, 1)$ sta sul grafico? $f(0) = 1 - 4 = -3 \neq 1$. No: sopra $x = 0$ il grafico passa per $(0, -3)$, non per $(0, 1)$.

### Il test della retta verticale

Dalla definizione segue un controllo molto pratico. Ogni $x$ del dominio ha un solo valore, quindi sopra (o sotto) ogni $x$ c'è un solo punto del grafico.

> [!abstract] Test della retta verticale
> Una curva del piano è il grafico di una funzione $y = f(x)$ se e solo se ogni retta verticale la incontra al massimo in un punto.

![[06-retta-verticale.svg|700]]

La parabola $y = x^2$ supera il test: qualunque retta verticale la tocca una volta sola. La circonferenza $x^2 + y^2 = 4$ (quella di centro l'origine e raggio $2$, vista in [[03-retta-e-circonferenza]]) non lo supera: la retta $x = 1$ la incontra in $(1, \sqrt{3})$ e in $(1, -\sqrt{3})$. Al numero $1$ corrisponderebbero due valori, quindi la circonferenza non è il grafico di una funzione.

> [!warning] Errore tipico
> La circonferenza non è una funzione, ma ciascuna delle sue due metà sì. La semicirconferenza superiore è il grafico di $y = \sqrt{4 - x^2}$, quella inferiore di $y = -\sqrt{4 - x^2}$. Una curva che non è un grafico si può spesso spezzare in pezzi che lo sono.

## DOMINIO E IMMAGINE

### Il dominio naturale

Spesso una funzione viene data solo con la formula, per esempio $f(x) = \sqrt{x - 1}$, senza dire quale sia il dominio. In questo caso si sottintende il dominio più grande possibile: l'insieme di tutti i numeri reali $x$ per cui la formula ha senso, cioè per cui si riesce a fare il conto. Questo insieme si chiama *dominio naturale* (o *campo di esistenza*).

Trovare il dominio naturale vuol dire cercare le operazioni che non si possono fare. Fino a questo punto del corso sono tre.

> [!abstract] Le regole del dominio naturale
> 1. Denominatori: non si divide per zero. Ogni denominatore deve essere $\neq 0$.
> 2. Radici di indice pari ($\sqrt{\;}$, $\sqrt[4]{\;}$...): non esiste la radice quadrata di un numero negativo. Il radicando (quello che sta sotto la radice) deve essere $\ge 0$.
> 3. Logaritmi: il logaritmo esiste solo per numeri positivi. L'argomento deve essere $> 0$ (strettamente: $\ln 0$ non esiste).
>
> Le radici di indice dispari ($\sqrt[3]{\;}$) non pongono condizioni: $\sqrt[3]{-8} = -2$. I polinomi sono definiti su tutto $\mathbb{R}$.

Il perché delle prime due regole si vede subito. Dividere $6$ per $0$ vorrebbe dire trovare un numero che moltiplicato per $0$ dia $6$, e non esiste. La radice quadrata di $-4$ dovrebbe essere un numero che al quadrato dà $-4$, ma un quadrato non è mai negativo. Il logaritmo è trattato più avanti in questa pagina, nella parte [[#ESPONENZIALI E LOGARITMI|esponenziali e logaritmi]].

Se nella formula ci sono più operazioni «delicate», le condizioni devono valere tutte insieme: si scrive un sistema e si prendono le $x$ che le soddisfano tutte. Le disequazioni che servono sono quelle di [[02-equazioni-e-disequazioni]].

### Esempi svolti sul dominio

> [!example] Esempio 1: una radice
> $f(x) = \sqrt{5 - 2x}$ (esercizio 1).
>
> 1. C'è una radice quadrata: il radicando deve essere $\ge 0$.
> 2. $5 - 2x \ge 0 \;\Rightarrow\; -2x \ge -5 \;\Rightarrow\; x \le \frac{5}{2}$ (dividendo per $-2$ il verso si gira).
> 3. Dominio: $(-\infty, \tfrac52]$.
>
> Il valore $x = \frac52$ è compreso, perché $\sqrt{0} = 0$ esiste.

> [!example] Esempio 2: una frazione
> $f(x) = \dfrac{1}{x^2 - 9}$ (esercizio 1).
>
> 1. C'è un denominatore: deve essere $\neq 0$.
> 2. $x^2 - 9 = 0 \;\Rightarrow\; x^2 = 9 \;\Rightarrow\; x = 3$ oppure $x = -3$.
> 3. Questi due valori vanno esclusi. Dominio: $\mathbb{R} \setminus \{-3, 3\}$, cioè $(-\infty, -3) \cup (-3, 3) \cup (3, +\infty)$.

![[06-dominio-esempi.svg|700]]

Nel disegno si vede che cosa succede nei punti esclusi. La radice si ferma esattamente in $x = \frac52$: a destra non c'è grafico. La frazione invece ha due «muri» in $x = -3$ e $x = 3$: avvicinandosi a quei valori il denominatore diventa piccolissimo e la frazione schizza verso $+\infty$ o $-\infty$, ma in quei punti non c'è nessun valore.

> [!example] Esempio 3: radice e frazione insieme
> $f(x) = \dfrac{\sqrt{x - 1}}{x - 4}$ (esercizio 1).
>
> Ci sono due condizioni, e devono valere tutte e due:
>
> $$
> \begin{cases} x - 1 \ge 0 & \text{(radice)} \\ x - 4 \neq 0 & \text{(denominatore)} \end{cases}
> \quad\Longrightarrow\quad
> \begin{cases} x \ge 1 \\ x \neq 4 \end{cases}
> $$
>
> Dominio: $[1, 4) \cup (4, +\infty)$. Si parte da $1$ (compreso), si salta il $4$ e si prosegue.

> [!warning] Errore tipico
> Non semplificare prima di aver trovato il dominio. Per $h(x) = \dfrac{x^2 - 4}{x - 2}$ viene voglia di scrivere subito $h(x) = x + 2$, ma il dominio si calcola sulla formula di partenza: $x - 2 \neq 0$, quindi $x \neq 2$. La semplificazione vale solo per $x \neq 2$ (lo vediamo più avanti con il grafico).

### L'insieme immagine

Il codominio è l'insieme in cui la funzione «potrebbe» arrivare. L'insieme dei valori che la funzione raggiunge davvero è un'altra cosa, e di solito è più piccolo.

> [!abstract] Definizione di immagine
> L'immagine (o insieme immagine) di $f: A \to B$ è l'insieme dei valori assunti:
>
> $$
> \operatorname{Im}(f) = f(A) = \{\, f(x) \;:\; x \in A \,\}.
> $$
>
> Un numero $y$ sta nell'immagine se esiste almeno una $x$ del dominio con $f(x) = y$. L'immagine è sempre contenuta nel codominio.

Per esempio, per $f(x) = x^2$ con codominio $\mathbb{R}$, l'immagine è $[0, +\infty)$: i numeri negativi stanno nel codominio, ma nessun quadrato li raggiunge.

### Trovare l'immagine dal grafico

Il dominio si legge sull'asse $x$, l'immagine sull'asse $y$. Per trovare l'immagine dal grafico si «schiaccia» il grafico in orizzontale sull'asse $y$: ogni punto del grafico viene portato sull'asse $y$ alla sua altezza, e l'insieme delle altezze raggiunte è l'immagine.

In pratica si guardano:

- il punto più basso e il punto più alto del grafico, se ci sono;
- se il grafico sale o scende senza fermarsi (allora l'immagine arriva a $+\infty$ o a $-\infty$);
- eventuali buchi o salti.

![[06-immagine-parabola.svg|500]]

> [!example] Esempio 4: la parabola $f(x) = (x+1)^2 - 4$
> (Esercizio 2.)
>
> Dominio: è un polinomio, quindi $\mathbb{R}$.
>
> Immagine, ragionando con i conti:
>
> 1. $(x+1)^2$ è un quadrato, quindi $(x+1)^2 \ge 0$ per ogni $x$, e vale $0$ solo per $x = -1$.
> 2. Togliendo $4$ a entrambi i lati: $(x+1)^2 - 4 \ge -4$. Quindi $f(x)$ non scende mai sotto $-4$, e vale $-4$ in $x = -1$.
> 3. Ogni valore $y \ge -4$ viene raggiunto: basta risolvere $(x+1)^2 - 4 = y$, cioè $(x+1)^2 = y + 4$, che ha soluzione $x = -1 + \sqrt{y + 4}$ perché $y + 4 \ge 0$.
>
> Immagine: $[-4, +\infty)$.
>
> Dal grafico si vede lo stesso risultato: la parabola ha il vertice in $(-1, -4)$, che è il punto più basso, e i rami salgono senza limite. Gli zeri (dove il grafico taglia l'asse $x$) sono $x = -3$ e $x = 1$, perché $(x+1)^2 = 4$ dà $x + 1 = \pm 2$.

> [!example] Esempio 5: la radice traslata $g(x) = \sqrt{x - 2} + 3$
> (Esercizio 2.)
>
> Dominio: il radicando deve essere $\ge 0$, quindi $x - 2 \ge 0$, cioè $x \ge 2$. Dominio $[2, +\infty)$.
>
> Immagine:
>
> 1. $\sqrt{x - 2} \ge 0$, e vale $0$ in $x = 2$.
> 2. Aggiungendo $3$: $g(x) \ge 3$, e $g(2) = 3$.
> 3. Quando $x$ cresce la radice cresce senza limite, quindi si raggiungono tutti i valori da $3$ in su. Per un $y \ge 3$ qualsiasi: $\sqrt{x-2} = y - 3$ dà $x = 2 + (y-3)^2$.
>
> Immagine: $[3, +\infty)$.

![[06-immagine-radice.svg|500]]

Il grafico di $g$ è il grafico di $\sqrt{x}$ (tratteggiato) spostato di $2$ verso destra e di $3$ verso l'alto: il punto di partenza passa da $(0, 0)$ a $(2, 3)$. Queste traslazioni sono spiegate nell'ultima parte della pagina.

### Una funzione con un buco

> [!example] Esempio 6: $h(x) = \dfrac{x^2 - 4}{x - 2}$
> (Esercizio 3.)
>
> 1. Dominio: $x - 2 \neq 0$, quindi $\mathbb{R} \setminus \{2\}$.
> 2. Semplificazione: il numeratore è una differenza di quadrati, $x^2 - 4 = (x-2)(x+2)$. Per $x \neq 2$ si può dividere per $x - 2$:
>
> $$
> h(x) = \frac{(x-2)(x+2)}{x-2} = x + 2 \qquad (x \neq 2).
> $$
>
> 3. Grafico: è la retta $y = x + 2$ senza il punto di ascissa $2$. Su quella retta, sopra $x = 2$, ci sarebbe il punto $(2, 4)$: è il buco.
> 4. Immagine: la retta $y = x + 2$ raggiunge tutti i numeri reali, tranne il valore che avrebbe preso in $x = 2$, cioè $4$. Immagine: $\mathbb{R} \setminus \{4\}$.

![[06-retta-bucata.svg|460]]

Nel disegno il buco si indica con un pallino vuoto. Il pallino vuoto verde sull'asse $x$ ricorda che $2$ non è nel dominio, quello arancione sull'asse $y$ che $4$ non è nell'immagine.

## INIETTIVITÀ, COMPOSIZIONE E FUNZIONE INVERSA

### Funzioni iniettive

La definizione di funzione impedisce a una $x$ di avere due valori. Non impedisce invece a due $x$ diverse di avere lo stesso valore: per $x^2$ si ha $(-2)^2 = 2^2 = 4$. Le funzioni in cui questo non succede hanno un nome.

> [!abstract] Funzione iniettiva
> $f: A \to B$ è iniettiva se a $x$ diverse corrispondono valori diversi:
>
> $$
> x_1 \neq x_2 \;\Longrightarrow\; f(x_1) \neq f(x_2).
> $$
>
> In modo equivalente: se $f(x_1) = f(x_2)$, allora $x_1 = x_2$. Nel diagramma a frecce, in ogni elemento di $B$ arriva al massimo una freccia.

Sul grafico c'è un test simile a quello della retta verticale, ma con le rette orizzontali. Una retta orizzontale $y = k$ incontra il grafico nei punti in cui $f(x) = k$; se li incontra in due punti, due $x$ diverse hanno lo stesso valore $k$.

> [!abstract] Test della retta orizzontale
> $f$ è iniettiva se e solo se ogni retta orizzontale incontra il suo grafico al massimo in un punto.

![[06-retta-orizzontale.svg|700]]

$x^3$ è iniettiva: ogni retta orizzontale la tocca una volta sola. $x^2$ su tutto $\mathbb{R}$ no: la retta $y = 2$ la tocca in $x = -\sqrt2$ e in $x = \sqrt2$.

> [!example] Esempio: dimostrare con i conti che $f(x) = 5 - 2x$ è iniettiva
> Si suppone $f(x_1) = f(x_2)$ e si vede se ne segue $x_1 = x_2$:
>
> $$
> 5 - 2x_1 = 5 - 2x_2 \;\Rightarrow\; -2x_1 = -2x_2 \;\Rightarrow\; x_1 = x_2 .
> $$
>
> Quindi è iniettiva. Lo stesso conto con $x^2$ darebbe $x_1^2 = x_2^2$, cioè $x_1 = \pm x_2$: non si arriva a $x_1 = x_2$, e infatti $x^2$ non è iniettiva.

### Funzioni suriettive

> [!abstract] Funzione suriettiva
> $f: A \to B$ è suriettiva se ogni elemento del codominio viene raggiunto: per ogni $y \in B$ esiste almeno una $x \in A$ con $f(x) = y$.
>
> In altre parole: $f$ è suriettiva quando l'immagine coincide con il codominio, $\operatorname{Im}(f) = B$. Nel diagramma a frecce, in ogni elemento di $B$ arriva almeno una freccia.

Per sapere se una funzione è suriettiva, quindi, si calcola l'immagine e la si confronta con il codominio dichiarato. Per questo è importante che il codominio venga scritto: la stessa formula può essere suriettiva o no a seconda di dove si dice che arriva.

### Funzioni biettive e il ruolo di dominio e codominio

> [!abstract] Funzione biettiva
> $f: A \to B$ è biettiva (o una *biezione*) se è sia iniettiva sia suriettiva. Ogni $y \in B$ è raggiunto da una e una sola $x \in A$. Nel diagramma a frecce, in ogni elemento di $B$ arriva esattamente una freccia.

Iniettività e suriettività non dipendono solo dalla formula. L'iniettività dipende dal dominio: togliendo dei punti dal dominio si possono eliminare le «coppie» con lo stesso valore. La suriettività dipende dal codominio: restringendo il codominio all'immagine, la funzione diventa suriettiva.

L'esempio da ricordare è $x^2$.

![[06-restrizione-x2.svg|700]]

- $x^2: \mathbb{R} \to \mathbb{R}$ non è iniettiva ($(-1)^2 = 1^2$) e non è suriettiva (i numeri negativi del codominio non vengono mai raggiunti).
- $x^2: \mathbb{R} \to [0, +\infty)$ è suriettiva (ogni $y \ge 0$ è il quadrato di $\sqrt{y}$) ma non iniettiva.
- $x^2: [0, +\infty) \to [0, +\infty)$ è biettiva: tenendo solo le $x \ge 0 $ resta un solo ramo della parabola, che ogni retta orizzontale $y = k \ge 0$ incontra una volta sola.

> [!example] Esempio: classificare tre funzioni (esercizio 5)
> 1. $x^3: \mathbb{R} \to \mathbb{R}$. Iniettiva (test della retta orizzontale, figura sopra). Suriettiva: ogni numero reale $y$ è il cubo di $\sqrt[3]{y}$. Quindi biettiva.
> 2. $|x|: \mathbb{R} \to [0, +\infty)$. Non iniettiva: $|-3| = |3| = 3$. Suriettiva: ogni $y \ge 0$ è il valore assoluto di $y$ stesso. Quindi suriettiva ma non iniettiva.
> 3. $x^2: [-2, 2] \to [0, 4]$. Non iniettiva: $(-1)^2 = 1^2$, e $-1$ e $1$ stanno entrambi in $[-2, 2]$. Suriettiva: per $x \in [-2, 2]$ i quadrati vanno da $0$ (in $x = 0$) a $4$ (in $x = \pm 2$) e prendono tutti i valori intermedi, quindi l'immagine è $[0, 4]$, uguale al codominio.

> [!example] Esempio: costruire degli esempi (esercizio 13)
> - Iniettiva ma non suriettiva da $\mathbb{R}$ a $\mathbb{R}$: $f(x) = e^x$. È sempre crescente, quindi iniettiva, ma i suoi valori sono solo positivi: $0$ e i negativi non vengono mai raggiunti (si vede più avanti, in [[#La funzione esponenziale|la funzione esponenziale]]).
> - Suriettiva ma non iniettiva da $\mathbb{R}$ a $[0, +\infty)$: $f(x) = x^2$ (oppure $|x|$). Raggiunge ogni $y \ge 0$, ma $x$ e $-x$ hanno lo stesso valore.

### La composizione di funzioni

Due funzioni si possono mettere «in fila», come due macchine: l'uscita della prima diventa l'entrata della seconda.

![[06-composizione.svg|620]]

> [!abstract] Funzione composta
> Date $g$ e $f$, la funzione composta $f \circ g$ (si legge «$f$ composto $g$») è
>
> $$
> (f \circ g)(x) = f(g(x)).
> $$
>
> Si applica prima $g$, poi $f$: l'ordine si legge da destra verso sinistra. Il dominio di $f \circ g$ è formato dalle $x$ che stanno nel dominio di $g$ e per cui $g(x)$ sta nel dominio di $f$.

In pratica, per scrivere $f(g(x))$ si prende la formula di $f$ e al posto di ogni $x$ si mette tutta la formula di $g$. In generale $f \circ g$ e $g \circ f$ sono diverse: l'ordine conta.

> [!example] Esempio: $f(x) = \sqrt{x}$ e $g(x) = x^2 - 1$ (esercizio 8)
> Composta $f \circ g$ (prima $g$, poi $f$):
>
> $$
> (f \circ g)(x) = f(x^2 - 1) = \sqrt{x^2 - 1}.
> $$
>
> Dominio: il radicando deve essere $\ge 0$, cioè $x^2 - 1 \ge 0$, quindi $x^2 \ge 1$: $x \le -1$ oppure $x \ge 1$. Dominio $(-\infty, -1] \cup [1, +\infty)$.
>
> Composta $g \circ f$ (prima $f$, poi $g$):
>
> $$
> (g \circ f)(x) = g(\sqrt{x}) = (\sqrt{x})^2 - 1 = x - 1 .
> $$
>
> Dominio: il primo passo è $\sqrt{x}$, che esiste solo per $x \ge 0$. Quindi il dominio è $[0, +\infty)$, non tutto $\mathbb{R}$, anche se la formula finale $x - 1$ sembrerebbe definita ovunque.

> [!warning] Errore tipico
> Il dominio della composta va calcolato guardando tutti i passaggi, non solo la formula semplificata. In $g \circ f$ qui sopra, $(\sqrt{x})^2 = x$ vale solo per $x \ge 0$: per $x = -4$ la macchina $f$ si blocca già al primo passo.

### La funzione inversa

Una funzione porta $x$ in $y$. La funzione inversa fa il cammino al contrario: riporta $y$ in $x$. Per poterlo fare, ogni $y$ del codominio deve venire da una sola $x$ (altrimenti non sapremmo dove tornare) e ogni $y$ deve venire da qualche $x$ (altrimenti non sapremmo dove mandarla). Le due richieste sono proprio iniettività e suriettività.

> [!abstract] Funzione inversa
> Se $f: A \to B$ è biettiva, esiste la funzione inversa $f^{-1}: B \to A$, definita da
>
> $$
> f^{-1}(y) = x \quad \Longleftrightarrow \quad f(x) = y .
> $$
>
> Componendo $f$ e $f^{-1}$ si torna al punto di partenza:
>
> $$
> f^{-1}(f(x)) = x \;\text{ per ogni } x \in A, \qquad f(f^{-1}(y)) = y \;\text{ per ogni } y \in B.
> $$
>
> Il dominio di $f^{-1}$ è l'immagine di $f$, e l'immagine di $f^{-1}$ è il dominio di $f$.

> [!warning] Errore tipico
> $f^{-1}(x)$ non vuol dire $\dfrac{1}{f(x)}$. L'esponente $-1$ qui indica la funzione inversa, non il reciproco: per $f(x) = 5 - 2x$ si ha $f^{-1}(x) = \frac{5-x}{2}$, mentre $\frac{1}{f(x)} = \frac{1}{5-2x}$.

Per calcolare l'inversa si segue sempre lo stesso procedimento:

1. si scrive $y = f(x)$;
2. si risolve l'equazione rispetto a $x$, cioè si ricava $x$ in funzione di $y$;
3. si scambiano i nomi delle lettere, per scrivere l'inversa con la variabile $x$ come al solito;
4. si controlla con le composizioni.

> [!example] Esempio: l'inversa di $f(x) = 5 - 2x$ (esercizio 6)
> $f: \mathbb{R} \to \mathbb{R}$ è biettiva (è una retta non orizzontale), quindi l'inversa esiste.
>
> 1. $y = 5 - 2x$.
> 2. $2x = 5 - y \;\Rightarrow\; x = \dfrac{5 - y}{2}$.
> 3. Scambiando le lettere: $f^{-1}(x) = \dfrac{5 - x}{2}$.
> 4. Verifica di entrambe le composizioni:
>
> $$
> f(f^{-1}(x)) = 5 - 2\cdot\frac{5-x}{2} = 5 - (5 - x) = x,
> $$
>
> $$
> f^{-1}(f(x)) = \frac{5 - (5 - 2x)}{2} = \frac{2x}{2} = x .
> $$
>
> Tutte e due danno $x$: l'inversa è giusta.

> [!example] Esempio: la tariffa al contrario (esercizio 15)
> $T(t) = 4 + 2t$ con $t \ge 0$.
>
> Immagine: $t \ge 0$ dà $2t \ge 0$ e quindi $T \ge 4$. Si raggiunge ogni prezzo da $4$ euro in su: immagine $[4, +\infty)$.
>
> Inversa: da $T = 4 + 2t$ si ricava $t = \dfrac{T - 4}{2}$, quindi
>
> $$
> T^{-1}(y) = \frac{y - 4}{2}, \qquad y \ge 4 .
> $$
>
> $T^{-1}(10) = \frac{10 - 4}{2} = 3$. Significato: la funzione $T$ risponde alla domanda «quanto pago per $t$ ore?», l'inversa alla domanda opposta «quante ore ho usato se ho pagato $y$ euro?». Con $10$ euro si sono usate $3$ ore.

![[06-tariffa.svg|500]]

Nel grafico l'inversa si legge al contrario: si parte da $10$ sull'asse verticale, si va in orizzontale fino alla retta e si scende sull'asse orizzontale, dove si legge $3$.

### Il grafico dell'inversa

Se il punto $(a, b)$ sta sul grafico di $f$, cioè $f(a) = b$, allora $f^{-1}(b) = a$, e quindi il punto $(b, a)$ sta sul grafico di $f^{-1}$. Le coordinate si scambiano.

Scambiare $x$ e $y$ ha un significato geometrico preciso: i punti $(a, b)$ e $(b, a)$ sono simmetrici rispetto alla bisettrice del primo e terzo quadrante, la retta $y = x$. Facendolo per tutti i punti si ottiene questa regola.

> [!abstract] Grafico della funzione inversa
> Il grafico di $f^{-1}$ si ottiene ribaltando il grafico di $f$ rispetto alla retta $y = x$ (come in uno specchio appoggiato su quella retta).

![[06-inversa-bisettrice.svg|700]]

A sinistra la retta $f(x) = 5 - 2x$ (blu) e la sua inversa (rossa): il punto $(1, 3)$ della prima corrisponde al punto $(3, 1)$ della seconda, e il segmento tratteggiato che li unisce è perpendicolare alla bisettrice. A destra il ramo di parabola $y = x^2$ con $x \ge 0$ e la sua inversa $y = \sqrt{x}$: $(2, 4)$ diventa $(4, 2)$.

### Restringere il dominio per invertire

Quando una funzione non è iniettiva non ha inversa, ma si può restringere il dominio a un pezzo in cui lo è. Si sceglie un tratto del grafico che superi il test della retta orizzontale e si inverte solo quello. Il codominio si prende uguale all'immagine, così la funzione è anche suriettiva.

È esattamente quello che si fa con $x^2$: su tutto $\mathbb{R}$ non è invertibile, ma su $[0, +\infty)$ sì, e la sua inversa è $\sqrt{x}$. Per questo $\sqrt{x}$ dà sempre il risultato positivo: è l'inversa del ramo «destro» della parabola.

> [!example] Esempio: due inverse per $f(x) = (x - 1)^2$ (esercizio 7)
> La parabola $(x-1)^2$ ha il vertice in $(1, 0)$: scende fino a $x = 1$ e poi sale. Non è iniettiva su $\mathbb{R}$ (per esempio $f(0) = f(2) = 1$). L'immagine è $[0, +\infty)$.
>
> Prima scelta: il ramo destro, $x \ge 1$. $f: [1, +\infty) \to [0, +\infty)$ è biettiva.
>
> 1. $y = (x-1)^2$, con $x - 1 \ge 0$.
> 2. $x - 1 = \sqrt{y}$ (si prende la radice positiva perché $x - 1 \ge 0$), quindi $x = 1 + \sqrt{y}$.
> 3. Inversa: $f^{-1}(x) = 1 + \sqrt{x}$, definita per $x \ge 0$.
>
> Seconda scelta: il ramo sinistro, $x \le 1$. $f: (-\infty, 1] \to [0, +\infty)$ è biettiva.
>
> 1. Ora $x - 1 \le 0$, quindi $x - 1 = -\sqrt{y}$.
> 2. Inversa: $f^{-1}(x) = 1 - \sqrt{x}$, definita per $x \ge 0$.
>
> Controllo: con la prima scelta $f^{-1}(4) = 1 + 2 = 3$, e infatti $f(3) = (3-1)^2 = 4$. Con la seconda $f^{-1}(4) = 1 - 2 = -1$, e $f(-1) = (-2)^2 = 4$.

![[06-restrizione-x-meno-1.svg|700]]

### Un esercizio completo del professore: $f(x) = \sqrt{x^2 - x} - x$

In classe il professore ha svolto un esercizio che mette insieme tutto quello che si è visto finora. Data la funzione

$$
f(x) = \sqrt{x^2 - x} - x
$$

bisogna trovare, in quest'ordine:

1. il dominio, che il professore indica con $D$;
2. l'immagine, che scrive semplicemente $\operatorname{Im} f$ (o anche solo $\operatorname{Im}$): è lo stesso insieme $\operatorname{Im}(f)$ definito sopra;
3. la funzione inversa $f^{-1}$;
4. la verifica $f \circ f^{-1}$, cioè che applicando prima $f^{-1}$ e poi $f$ si torna al punto di partenza.

È un esercizio tipico d'esame, quindi conviene seguirlo passo per passo.

> [!example] Passo 1: il dominio
> C'è una radice quadrata, quindi il radicando deve essere maggiore o uguale a zero:
>
> $$
> x^2 - x \ge 0 \quad\Longrightarrow\quad x\,(x - 1) \ge 0 .
> $$
>
> È il prodotto di due fattori, $x$ e $x - 1$. Un prodotto è positivo (o nullo) quando i due fattori hanno lo stesso segno. Ci sono quindi due casi:
>
> - tutti e due $\ge 0$: $x \ge 0$ e $x \ge 1$, cioè $x \ge 1$;
> - tutti e due $\le 0$: $x \le 0$ e $x \le 1$, cioè $x \le 0$.
>
> Lo stesso risultato si ottiene con la tabella dei segni di [[02-equazioni-e-disequazioni]]: $x$ cambia segno in $0$, $x - 1$ in $1$, e il prodotto è positivo fuori dall'intervallo $(0, 1)$.
>
> $$
> D = (-\infty, 0\,] \cup [\,1, +\infty) .
> $$
>
> Controllo con un numero: per $x = -1$ il radicando vale $1 + 1 = 2 \ge 0$, e infatti $f(-1) = \sqrt{2} + 1$ esiste.

> [!warning] Errore tipico: la disequazione prodotto
> $x\,(x - 1) \ge 0$ non si risolve facendo l'intersezione di «$x \ge 0$» e «$x \ge 1$» (che darebbe $D = [1, +\infty)$). Quelle due condizioni dicono solo quando ciascun fattore è positivo; il prodotto è positivo anche quando i due fattori sono entrambi negativi, cioè per $x \le 0$. Una disequazione prodotto si risolve sempre con lo studio del segno di ogni fattore (la tabella dei segni).
>
> Attenzione anche a dove si mette la condizione: si impone che il radicando sia $\ge 0$, cioè $x^2 - x \ge 0$. Scrivere $\sqrt{x^2 - x} \ge 0$ non dice niente, perché una radice, quando esiste, è sempre $\ge 0$.

Per l'immagine il professore usa il metodo «al contrario»: invece di chiedersi dove arriva $f$ partendo dalle $x$, si fissa un valore $y$ e ci si chiede se esiste una $x$ del dominio con $f(x) = y$. I valori $y$ per cui la risposta è sì formano l'immagine.

> [!example] Passo 2: l'immagine con il metodo del professore
> 1. Si pone $f(x) = y$:
>
> $$
> \sqrt{x^2 - x} - x = y .
> $$
>
> 2. Si isola la radice, lasciandola da sola a sinistra:
>
> $$
> \sqrt{x^2 - x} = x + y .
> $$
>
> 3. Si scrive la condizione. A sinistra c'è una radice, che è sempre $\ge 0$; quindi anche il membro di destra deve esserlo:
>
> $$
> x + y \ge 0 .
> $$
>
> 4. Ora i due membri sono entrambi $\ge 0$ e si può elevare al quadrato:
>
> $$
> x^2 - x = x^2 + 2xy + y^2 .
> $$
>
> 5. Gli $x^2$ si semplificano. Portando tutto a destra si ottiene $y^2 + 2xy + x = 0$, e raccogliendo la $x$:
>
> $$
> x\,(2y + 1) = -y^2 .
> $$
>
> 6. Se $y = -\frac12$ l'equazione diventa $0 = -\frac14$, impossibile: il valore $-\frac12$ non è nell'immagine. Per ogni altro $y$ si divide:
>
> $$
> x = -\frac{y^2}{2y + 1} .
> $$
>
> 7. Si impone la condizione del punto 3, sostituendo questa $x$:
>
> $$
> x + y = -\frac{y^2}{2y + 1} + y = \frac{-y^2 + 2y^2 + y}{2y + 1} = \frac{y\,(y + 1)}{2y + 1} \ge 0 .
> $$
>
> 8. Si studia il segno della frazione. Il numeratore si annulla in $y = -1$ e $y = 0$, il denominatore in $y = -\frac12$:
>
> - per $y < -1$: numeratore $+$, denominatore $-$, frazione negativa (no);
> - per $-1 \le y < -\frac12$: numeratore $\le 0$, denominatore $-$, frazione $\ge 0$ (sì);
> - per $-\frac12 < y < 0$: numeratore $-$, denominatore $+$, frazione negativa (no);
> - per $y \ge 0$: numeratore $\ge 0$, denominatore $+$, frazione $\ge 0$ (sì).
>
> 9. La condizione sul radicando è già a posto: dopo il punto 4 il radicando vale $x^2 - x = (x + y)^2$, che è un quadrato e quindi non è mai negativo.
>
> $$
> \operatorname{Im} f = [\,-1, -\tfrac12\,) \cup [\,0, +\infty) .
> $$

La condizione $x + y \ge 0$ non è un dettaglio. Elevando al quadrato si possono aggiungere soluzioni false, perché anche un numero negativo, elevato al quadrato, diventa positivo. Per esempio con $y = -2$ il punto 6 dà $x = -\frac{4}{-3} = \frac43$; ma $x + y = \frac43 - 2 = -\frac23 < 0$, e infatti $f\left(\frac43\right) = \sqrt{\frac{16}{9} - \frac{4}{3}} - \frac43 = \frac23 - \frac43 = -\frac23$, non $-2$. Senza la condizione si sarebbe concluso, sbagliando, che $-2$ sta nell'immagine.

![[06-esercizio-radice.svg|640]]

Il grafico conferma i conti. Il ramo di sinistra parte da $(0, 0)$ e sale senza limite quando $x$ va verso $-\infty$: dà l'immagine $[0, +\infty)$. Il ramo di destra parte da $(1, -1)$ e sale avvicinandosi sempre di più alla retta tratteggiata $y = -\frac12$ senza mai toccarla (una retta così si chiama *asintoto*): dà l'immagine $[-1, -\frac12)$, con $-1$ compreso e $-\frac12$ escluso.

> [!example] Passo 3: la funzione inversa
> Al punto 6 si è visto che per ogni $y$ dell'immagine c'è una sola $x$ che ci arriva: la funzione è iniettiva. Presa con codominio uguale all'immagine, $f: D \to \operatorname{Im} f$ è biettiva e quindi invertibile.
>
> La formula dell'inversa l'abbiamo già trovata: è proprio $x = -\frac{y^2}{2y+1}$. Scambiando i nomi delle lettere:
>
> $$
> f^{-1}(x) = -\frac{x^2}{2x + 1}, \qquad x \in [\,-1, -\tfrac12\,) \cup [\,0, +\infty) .
> $$
>
> Il dominio di $f^{-1}$ è l'immagine di $f$, e l'immagine di $f^{-1}$ è il dominio di $f$, cioè $(-\infty, 0\,] \cup [\,1, +\infty)$.
>
> Controllo con due numeri:
>
> - $f^{-1}(-1) = -\frac{1}{-1} = 1$, e infatti $f(1) = \sqrt{0} - 1 = -1$;
> - $f^{-1}(1) = -\frac13$, e infatti $f\left(-\frac13\right) = \sqrt{\frac19 + \frac13} + \frac13 = \frac23 + \frac13 = 1$.

> [!example] Passo 4: la verifica $f \circ f^{-1}$
> Bisogna controllare che $f(f^{-1}(x)) = x$ per ogni $x$ del dominio di $f^{-1}$. Per comodità si chiama $t = f^{-1}(x) = -\frac{x^2}{2x+1}$.
>
> 1. Il radicando:
>
> $$
> t^2 - t = \frac{x^4}{(2x+1)^2} + \frac{x^2}{2x+1} = \frac{x^4 + x^2(2x+1)}{(2x+1)^2} = \frac{x^2(x^2 + 2x + 1)}{(2x+1)^2} = \left(\frac{x\,(x+1)}{2x+1}\right)^2 .
> $$
>
> 2. La radice di un quadrato è il valore assoluto: $\sqrt{t^2 - t} = \left|\dfrac{x\,(x+1)}{2x+1}\right|$.
> 3. Sul dominio di $f^{-1}$ la frazione $\frac{x(x+1)}{2x+1}$ è $\ge 0$: è proprio la condizione trovata al punto 8 del passo 2. Quindi il valore assoluto si può togliere.
> 4. Si mette tutto insieme:
>
> $$
> f(f^{-1}(x)) = \frac{x\,(x+1)}{2x+1} - \left(-\frac{x^2}{2x+1}\right) = \frac{x^2 + x + x^2}{2x+1} = \frac{x\,(2x+1)}{2x+1} = x .
> $$
>
> La composizione dà $x$: l'inversa è giusta. Si vede anche perché la condizione $x + y \ge 0$ era indispensabile: senza di essa il valore assoluto non sparirebbe e la verifica non tornerebbe.

> [!warning] Il segno quando si raccoglie
> Da $y^2 + 2xy + x = 0$ si porta $y^2$ dall'altra parte e si raccoglie la $x$: $x\,(2y + 1) = -y^2$. Il segno meno davanti a $y^2$ si perde facilmente (scrivendo $y^2 = x(2y+1)$), e con il segno sbagliato tutta l'immagine e l'inversa vengono sbagliate. Un controllo veloce: con $y = -1$ deve tornare $x = 1$, perché $f(1) = -1$.

## SIMMETRIE, MONOTONIA E OPERAZIONI SUI GRAFICI

### Funzioni pari e dispari

Alcuni grafici sono simmetrici, e la simmetria si riconosce dalla formula confrontando $f(-x)$ con $f(x)$. Prima di tutto il dominio deve essere simmetrico rispetto a $0$: se $x$ sta nel dominio, deve starci anche $-x$. Altrimenti la domanda non ha senso.

> [!abstract] Funzioni pari e dispari
> Sia $f$ con dominio simmetrico rispetto a $0$.
>
> - $f$ è pari se $f(-x) = f(x)$ per ogni $x$ del dominio. Il grafico è simmetrico rispetto all'asse $y$.
> - $f$ è dispari se $f(-x) = -f(x)$ per ogni $x$ del dominio. Il grafico è simmetrico rispetto all'origine (ruotandolo di mezzo giro attorno a $(0,0)$ resta uguale).
>
> Una funzione può anche non essere né pari né dispari.

Il motivo della simmetria è semplice. Se $f$ è pari, i punti $(a, f(a))$ e $(-a, f(a))$ stanno tutti e due sul grafico: hanno la stessa altezza e sono uno lo specchio dell'altro rispetto all'asse $y$. Se $f$ è dispari, con $(a, f(a))$ c'è anche $(-a, -f(a))$, che è il punto opposto rispetto all'origine.

![[06-pari-dispari.svg|700]]

> [!example] Esempio: stabilire la parità (esercizio 9)
> 1. $f(x) = x^4 - 2x^2$. Dominio $\mathbb{R}$, simmetrico. $f(-x) = (-x)^4 - 2(-x)^2 = x^4 - 2x^2 = f(x)$. Pari.
> 2. $f(x) = x^3 + x$. Dominio $\mathbb{R}$. $f(-x) = (-x)^3 + (-x) = -x^3 - x = -(x^3 + x) = -f(x)$. Dispari.
> 3. $f(x) = x^2 + x + 1$. Dominio $\mathbb{R}$. $f(-x) = x^2 - x + 1$, che non è né $f(x)$ né $-f(x)$. Per esserne sicuri basta un numero: $f(1) = 3$ e $f(-1) = 1$, che non sono né uguali né opposti. Né pari né dispari.
> 4. $f(x) = \sqrt{x}$. Dominio $[0, +\infty)$, che non è simmetrico: $\sqrt{4}$ esiste, $\sqrt{-4}$ no. Né pari né dispari.
>
> Trucco per i polinomi: se ci sono solo potenze pari di $x$ (le costanti contano come $x^0$) il polinomio è pari; se ci sono solo potenze dispari è dispari; se sono mescolate non è né l'uno né l'altro.

> [!example] Esempio: «ogni funzione pari è non iniettiva» (esercizio 14)
> È vero, a patto di guardare il dominio. Se $f$ è pari e il dominio contiene un numero $a \neq 0$, allora contiene anche $-a$ (il dominio di una funzione pari è simmetrico), e $f(-a) = f(a)$ con $-a \neq a$: due $x$ diverse con lo stesso valore, quindi $f$ non è iniettiva.
>
> L'unica eccezione è il caso limite in cui il dominio è soltanto $\{0\}$. E attenzione: $x^2$ ristretta a $[0, +\infty)$ è iniettiva, ma non è più pari, perché il suo dominio non è più simmetrico.

### Funzioni crescenti e decrescenti

> [!abstract] Monotonia
> Sia $I$ un intervallo contenuto nel dominio di $f$.
>
> - $f$ è crescente su $I$ se, per $x_1 < x_2$ in $I$, si ha $f(x_1) < f(x_2)$: spostandosi verso destra il grafico sale.
> - $f$ è decrescente su $I$ se, per $x_1 < x_2$ in $I$, si ha $f(x_1) > f(x_2)$: spostandosi verso destra il grafico scende.
>
> Una funzione crescente o decrescente su un intervallo si dice *monotona* su quell'intervallo. Gli intervalli in cui è crescente o decrescente si chiamano *intervalli di monotonia*.

Una funzione sempre crescente (o sempre decrescente) su tutto il dominio è iniettiva: se $x_1 < x_2$ allora $f(x_1) < f(x_2)$, quindi i valori sono per forza diversi. È un modo comodo per dimostrare l'iniettività: $x^3$ e $5 - 2x$ sono iniettive perché sono monotone.

![[06-monotonia.svg|700]]

> [!example] Esempio: intervalli di monotonia (esercizio 10)
> 1. $(x + 2)^2$ è una parabola con il vertice in $(-2, 0)$ e i rami verso l'alto. Decrescente su $(-\infty, -2]$, crescente su $[-2, +\infty)$.
> 2. $|x - 3|$ è una «V» con il vertice in $(3, 0)$. Per $x < 3$ vale $3 - x$ (scende), per $x \ge 3$ vale $x - 3$ (sale). Decrescente su $(-\infty, 3]$, crescente su $[3, +\infty)$.

> [!warning] Errore tipico
> La monotonia si dice sugli intervalli, non su tutta la funzione. $(x+2)^2$ non è «né crescente né decrescente» in assoluto: è decrescente prima del vertice e crescente dopo.

### Traslazioni

Conoscendo il grafico di poche funzioni di base ($x^2$, $|x|$, $\sqrt{x}$, $x^3$...), si possono disegnare molte altre funzioni senza fare tabelle, spostando e deformando quei grafici. La prima operazione è la *traslazione*, cioè lo spostamento rigido, senza deformare.

> [!abstract] Traslazioni (con $a > 0$, $b > 0$)
> - $y = f(x - a)$: il grafico di $f$ si sposta di $a$ verso destra.
> - $y = f(x + a)$: si sposta di $a$ verso sinistra.
> - $y = f(x) + b$: si sposta di $b$ verso l'alto.
> - $y = f(x) - b$: si sposta di $b$ verso il basso.

![[06-traslazioni.svg|700]]

La traslazione verticale è intuitiva: aggiungere $b$ al valore alza ogni punto di $b$. Quella orizzontale sembra «al contrario» (con il meno si va a destra), ma c'è un motivo. Il grafico di $f(x - 2)$ in $x = 2$ vale $f(0)$: quello che $f$ faceva in $0$, la nuova funzione lo fa in $2$, cioè $2$ passi più a destra. Per $x^2$, il vertice che stava in $x = 0$ si trova ora in $x = 2$, dove $x - 2 = 0$.

> [!example] Esempio: leggere le traslazioni nella formula
> - $(x + 1)^2 - 4$ è $x^2$ spostata di $1$ a sinistra e di $4$ in basso: il vertice va da $(0,0)$ a $(-1, -4)$, come nel grafico dell'esempio 4.
> - $\sqrt{x - 2} + 3$ è $\sqrt{x}$ spostata di $2$ a destra e $3$ in alto: il punto iniziale va da $(0, 0)$ a $(2, 3)$, come nell'esempio 5.
>
> In generale il vertice di $(x - h)^2 + k$ è il punto $(h, k)$.

### Riflessioni

> [!abstract] Riflessioni
> - $y = -f(x)$: il grafico si ribalta rispetto all'asse $x$ (ciò che stava sopra va sotto e viceversa).
> - $y = f(-x)$: il grafico si ribalta rispetto all'asse $y$ (destra e sinistra si scambiano).

![[06-riflessioni.svg|700]]

Con $-f(x)$ ogni valore cambia segno, quindi ogni punto $(x, y)$ diventa $(x, -y)$. Con $f(-x)$ quello che $f$ faceva in $3$ la nuova funzione lo fa in $-3$, quindi ogni punto $(x, y)$ diventa $(-x, y)$. Per $\sqrt{x}$: $-\sqrt{x}$ è lo stesso ramo capovolto verso il basso, $\sqrt{-x}$ è lo stesso ramo girato verso sinistra (il dominio diventa $x \le 0$).

Collegamento con la parità: una funzione è pari quando $f(-x) = f(x)$, cioè quando ribaltarla rispetto all'asse $y$ non la cambia.

### Valore assoluto e dilatazioni

Il valore assoluto rende positivo ciò che è negativo: $|5| = 5$, $|-5| = 5$. Applicato a tutta la funzione, lascia com'è la parte del grafico che sta sopra l'asse $x$ e ribalta verso l'alto quella che sta sotto.

> [!abstract] Valore assoluto e dilatazioni
> - $y = |f(x)|$: le parti del grafico sotto l'asse $x$ vengono ribaltate sopra; il resto non cambia. L'immagine non contiene mai numeri negativi.
> - $y = k\,f(x)$ con $k > 1$: il grafico si allunga in verticale (tutte le altezze vengono moltiplicate per $k$).
> - $y = k\,f(x)$ con $0 < k < 1$: il grafico si schiaccia in verticale.
> - $y = f(kx)$ con $k > 1$: il grafico si stringe in orizzontale verso l'asse $y$; con $0 < k < 1$ si allarga.

![[06-valore-assoluto-dilatazioni.svg|700]]

A sinistra $x^2 - 4$ (tratteggiata) è negativa tra $-2$ e $2$; in $|x^2 - 4|$ quell'arco viene capovolto verso l'alto. A destra $3x^2$ è più stretta di $x^2$ perché ogni altezza è triplicata; $\frac{x^2}{2}$ è più larga perché ogni altezza è dimezzata. Per una parabola allungare in verticale e stringere in orizzontale danno lo stesso effetto: $3x^2 = (\sqrt3\, x)^2$.

### Costruire un grafico per passi

Quando la formula contiene più operazioni, si parte dalla funzione di base e si applicano le trasformazioni una alla volta, nell'ordine in cui si farebbero i conti partendo da $x$.

> [!example] Esempio: $y = |x + 1| - 2$ (esercizio 11)
> 1. Si parte da $y = |x|$: una «V» con il vertice nell'origine.
> 2. $|x + 1|$: traslazione di $1$ verso sinistra. Il vertice va in $(-1, 0)$.
> 3. $|x + 1| - 2$: traslazione di $2$ verso il basso. Il vertice va in $(-1, -2)$.
>
> Ora si leggono le informazioni richieste.
>
> - Vertice: $(-1, -2)$.
> - Zeri: $|x + 1| - 2 = 0 \Rightarrow |x + 1| = 2 \Rightarrow x + 1 = 2$ oppure $x + 1 = -2$, cioè $x = 1$ e $x = -3$.
> - Immagine: $|x+1| \ge 0$, quindi $|x+1| - 2 \ge -2$. Immagine $[-2, +\infty)$.
> - Monotonia: decrescente su $(-\infty, -1]$, crescente su $[-1, +\infty)$.

![[06-esercizio-11.svg|720]]

> [!example] Esempio: $y = -(x - 1)^2 + 4$ (esercizio 12)
> 1. Si parte da $y = x^2$.
> 2. $(x - 1)^2$: traslazione di $1$ a destra, vertice in $(1, 0)$.
> 3. $-(x - 1)^2$: riflessione rispetto all'asse $x$, la parabola si apre verso il basso.
> 4. $-(x - 1)^2 + 4$: traslazione di $4$ verso l'alto, vertice in $(1, 4)$.
>
> - Immagine: $(x-1)^2 \ge 0$, quindi $-(x-1)^2 \le 0$ e $-(x-1)^2 + 4 \le 4$. Il vertice $(1, 4)$ è il punto più alto e i rami scendono senza limite: immagine $(-\infty, 4]$.
> - Zeri: $-(x-1)^2 + 4 = 0 \Rightarrow (x-1)^2 = 4 \Rightarrow x - 1 = \pm 2$, cioè $x = 3$ e $x = -1$.

![[06-esercizio-12.svg|460]]

> [!warning] Errore tipico
> In $f(x - a)$ il segno inganna: $(x - 1)^2$ va a destra, $(x + 1)^2$ va a sinistra. Per non sbagliare, chiediti dove si annulla la parentesi: $(x - 1)$ si annulla in $x = 1$, quindi il vertice è in $x = 1$.

## LE FUNZIONI ELEMENTARI: RETTE, POTENZE, RADICI E VALORE ASSOLUTO

Le funzioni elementari sono i mattoni con cui si costruiscono quasi tutte le altre funzioni: la retta, le potenze, le radici, l'iperbole, il valore assoluto, la parabola, l'esponenziale, il logaritmo e le funzioni trigonometriche. In classe ci si è fermati proprio all'inizio di questo argomento, quindi questa parte serve a prepararsi: per ogni funzione si guarda il grafico e si leggono le stesse informazioni (dominio, immagine, monotonia, parità, zeri, asintoti, inversa), e poi si imparano a risolvere le equazioni e le disequazioni che le contengono. Gli esempi svolti vengono quasi tutti dalla seconda pagina del foglio di esercizi del professore.

### Come si studia una funzione elementare

Di ogni funzione elementare bisogna saper disegnare il grafico a memoria, almeno a grandi linee. Dal grafico poi si leggono sempre le stesse otto informazioni, che conviene imparare come una scheda fissa.

Le prime tre sono già note dalla prima parte della pagina:

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

La funzione più semplice è la *funzione lineare* $f(x) = mx + q$, il cui grafico è una retta (vista nella pagina [[03-retta-e-circonferenza]]).

- Il numero $m$ è il *coefficiente angolare* (o pendenza): dice di quanto sale $y$ quando $x$ aumenta di $1$.
- Il numero $q$ è l'*ordinata all'origine*: il punto in cui la retta taglia l'asse $y$, perché $f(0) = q$.

![[06-rette.svg|480]]

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

![[06-potenze-pari.svg|380]]

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

![[06-potenze-dispari.svg|360]]

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

![[06-radice-quadrata.svg|430]]

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

![[06-radice-cubica.svg|500]]

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

![[06-iperbole.svg|460]]

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

Spostando la «V» con le traslazioni (viste [[#Traslazioni|sopra]]) si ottengono tutte le funzioni del tipo $|x - a| + b$, con il vertice nel punto $(a, b)$.

> [!example] Esempio: $|x+1| - 2$ (esercizio 11, prima pagina)
> ![[06-valore-assoluto-grafico.svg|440]]
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
> - Gli zeri sono le soluzioni dell'equazione di secondo grado $ax^2 + bx + c = 0$ (pagina [[02-equazioni-e-disequazioni]]): due, uno o nessuno a seconda del segno del discriminante $\Delta = b^2 - 4ac$.
>
> Se la funzione è già scritta nella forma $a(x - h)^2 + k$, il vertice si legge subito: è $(h, k)$.

> [!example] Esempio: $-(x-1)^2 + 4$ (esercizio 12, prima pagina)
> ![[06-parabola.svg|400]]
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

![[06-esponenziali.svg|460]]

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

![[06-esp-log-simmetrici.svg|480]]

Tutta la scheda del logaritmo si ricava da quella dell'esponenziale scambiando $x$ con $y$: il dominio del logaritmo è l'immagine dell'esponenziale, l'asintoto orizzontale $y = 0$ diventa l'asintoto verticale $x = 0$, il punto $(0, 1)$ diventa $(1, 0)$.

![[06-logaritmi.svg|460]]

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

Gli esercizi sul dominio mettono insieme le condizioni già viste [[#Il dominio naturale|sopra]] con quella nuova del logaritmo.

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
> ![[06-esercizio-esp-log.svg|440]]
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
> ![[06-crescita-raddoppio.svg|560]]
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

![[06-radiante.svg|420]]

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

La *circonferenza goniometrica* è la circonferenza di centro l'origine e raggio $1$, di equazione $x^2 + y^2 = 1$ (pagina [[03-retta-e-circonferenza]]). Gli angoli si misurano partendo dal semiasse positivo delle $x$ e girando in senso antiorario; un angolo negativo gira in senso orario.

Ogni angolo $\alpha$ individua un punto $P$ sulla circonferenza.

![[06-circonferenza-goniometrica.svg|480]]

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

![[06-angoli-notevoli.svg|500]]

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

![[06-seno-coseno.svg|600]]

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

![[06-tangente.svg|520]]

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
> ![[06-coseno-trasformato.svg|480]]
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
> ![[06-equazione-seno.svg|340]] ![[06-equazione-coseno.svg|340]]
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

![[06-arcoseno.svg|420]]

![[06-arcocoseno.svg|440]]

![[06-arcotangente.svg|560]]

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

![[06-pendenza.svg|560]]

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

## ESERCIZI

Questa sezione serve per allenarsi in vista dell'esonero. Prima rifai da sola, su carta, gli esercizi del professore, che in questa pagina sono già svolti come esempi: copri la soluzione e confronta solo alla fine. Poi passa agli esercizi nuovi: leggi il testo, risolvilo per intero sul foglio e solo dopo apri la soluzione cliccando sul riquadro verde chiuso. Se il risultato non torna, cerca il passaggio in cui ti sei separata dalla soluzione e rileggi la parte di teoria corrispondente.

### Gli esercizi del professore

Il foglio del professore per questo argomento è [[Esercizi_funzioni_e_Logaritmi.pdf]], in `materiale/`. Ha due pagine e tutti gli esercizi sono già svolti come esempi in questa pagina.

La prima pagina, «Funzioni e funzioni elementari», ha 15 esercizi, tutti svolti:

- esercizi 1-4 (dominio e immagine): nella parte «Dominio e immagine» (esempi 1-6) e nell'esempio dell'area del quadrato all'inizio della pagina;
- esercizi 5-10 (iniettiva e suriettiva, inversa, restrizione del dominio, composizione, parità, monotonia): nelle parti «Iniettività, composizione e funzione inversa» e «Simmetrie, monotonia e operazioni sui grafici»;
- esercizi 11-15 (grafici e ragionamento): il 13 è con le funzioni suriettive, il 14 con le funzioni pari, l'11 e il 12 in «Costruire un grafico per passi», il 15 (la tariffa) all'inizio della pagina e nella funzione inversa.

La seconda pagina, «Esponenziali, logaritmi e trigonometria», ha 20 esercizi, anche questi tutti svolti nelle parti «Esponenziali e logaritmi» e «Trigonometria» (il 17, un vero o falso, è diviso tra l'avvertenza sulle proprietà dei logaritmi e quella sulle funzioni inverse).

Negli appunti di classe c'è un solo esercizio su questo argomento: quello su $f(x) = \sqrt{x^2 - x} - x$ (dominio, immagine, inversa e verifica), in `appunti-nadia-11.jpeg`, svolto per intero nella parte «Un esercizio completo del professore». In classe il professore si era fermato all'equazione per l'immagine; il resto lo trovi completato lì. L'esercizio 11 qui sotto è dello stesso tipo, con conti un po' più semplici.

### Esercizi per allenarti

Gli esercizi sono divisi in due gruppi. Il primo (esercizi 1-11) riguarda le funzioni in generale, cioè la parte spiegata in classe, e ha più peso. Il secondo (esercizi 12-16) riguarda le funzioni elementari, a cui in classe si è appena cominciato. Dentro ogni gruppo si va dal più facile al più difficile.

#### Primo gruppo: dominio e immagine

> [!question] Esercizio 1
> Determinare il dominio naturale di
>
> $$
> f(x) = \frac{\sqrt{x + 3}}{x^2 - 4x} .
> $$

> [!success]- Soluzione
> Risultato: $D = [-3, 0) \cup (0, 4) \cup (4, +\infty)$.
>
> Come si arriva:
> 1. Ci sono una radice quadrata e un denominatore, quindi servono due condizioni che devono valere insieme:
>
> $$
> \begin{cases} x + 3 \ge 0 & \text{(radice)} \\ x^2 - 4x \neq 0 & \text{(denominatore)} \end{cases}
> $$
>
> 2. Radice: il radicando non può essere negativo, quindi $x + 3 \ge 0$, cioè $x \ge -3$.
> 3. Denominatore: non può essere zero. $x^2 - 4x = x(x - 4) = 0$ per $x = 0$ e per $x = 4$, che vanno esclusi.
> 4. Si mettono insieme: si parte da $-3$ (compreso) e si saltano $0$ e $4$:
>
> $$
> D = [-3, 0) \cup (0, 4) \cup (4, +\infty) .
> $$

> [!question] Esercizio 2
> Determinare il dominio naturale di
>
> $$
> f(x) = \sqrt{\frac{x - 1}{3 - x}} .
> $$

> [!success]- Soluzione
> Risultato: $D = [1, 3)$.
>
> Come si arriva:
> 1. Il radicando deve essere $\ge 0$ e, siccome è una frazione, il suo denominatore deve essere $\neq 0$:
>
> $$
> \frac{x - 1}{3 - x} \ge 0, \qquad x \neq 3 .
> $$
>
> 2. Segno del numeratore: $x - 1 \ge 0$ per $x \ge 1$.
> 3. Segno del denominatore: $3 - x > 0$ per $x < 3$.
> 4. Tabella dei segni, intervallo per intervallo:
>
> - per $x < 1$: numeratore $-$, denominatore $+$, frazione negativa (no);
> - per $1 \le x < 3$: numeratore $\ge 0$, denominatore $+$, frazione $\ge 0$ (sì);
> - per $x > 3$: numeratore $+$, denominatore $-$, frazione negativa (no).
>
> 5. Estremi: $x = 1$ è compreso (la frazione vale $0$ e $\sqrt{0} = 0$), $x = 3$ no (denominatore nullo). Quindi:
>
> $$
> D = [1, 3) .
> $$

> [!question] Esercizio 3
> Determinare dominio e immagine di
>
> $$
> f(x) = 2 - (x - 3)^2 \qquad \text{e} \qquad g(x) = 1 - \sqrt{x + 4} .
> $$

> [!success]- Soluzione
> Risultato: $f$ ha dominio $\mathbb{R}$ e immagine $(-\infty, 2]$; $g$ ha dominio $[-4, +\infty)$ e immagine $(-\infty, 1]$.
>
> Come si arriva, funzione $f$:
> 1. Dominio: $f$ è un polinomio, quindi è definita ovunque: dominio $\mathbb{R}$.
> 2. Valore massimo: $(x - 3)^2 \ge 0$, quindi $-(x - 3)^2 \le 0$ e $2 - (x - 3)^2 \le 2$. Il valore $2$ si raggiunge in $x = 3$.
> 3. Valori sotto: è una parabola con il vertice in $(3, 2)$ rivolta verso il basso; i rami scendono senza limite, quindi si raggiungono tutti i valori sotto $2$. Immagine $(-\infty, 2]$.
>
> Come si arriva, funzione $g$:
> 1. Dominio: il radicando non può essere negativo, $x + 4 \ge 0$: dominio $[-4, +\infty)$.
> 2. Valore massimo: $\sqrt{x + 4} \ge 0$, quindi $-\sqrt{x + 4} \le 0$ e $g(x) \le 1$, con $g(-4) = 1$.
> 3. Valori sotto: quando $x$ cresce la radice cresce senza limite e $g$ scende senza limite (per esempio $g(12) = 1 - 4 = -3$). Immagine $(-\infty, 1]$.

#### Primo gruppo: iniettività, composizione e inversa

> [!question] Esercizio 4
> Dire se le funzioni seguenti sono iniettive, suriettive, biettive:
>
> 1. $f(x) = 2x + 1$, da $\mathbb{R}$ a $\mathbb{R}$;
> 2. $g(x) = x^2 - 1$, da $\mathbb{R}$ a $[-1, +\infty)$;
> 3. $h(x) = x^2$, da $[0, 2]$ a $[0, 5]$.

> [!success]- Soluzione
> Risultato: 1) $f$ è biettiva (iniettiva e suriettiva); 2) $g$ è suriettiva ma non iniettiva; 3) $h$ è iniettiva ma non suriettiva.
>
> Come si arriva:
> 1. $f(x) = 2x + 1$ è una retta non orizzontale, sempre crescente: valori diversi di $x$ danno valori diversi, quindi è iniettiva. Ogni $y$ reale si raggiunge con $x = \frac{y - 1}{2}$, quindi è suriettiva. Essendo tutte e due le cose, è biettiva.
> 2. $g(x) = x^2 - 1$ non è iniettiva, perché due $x$ diverse danno lo stesso valore: $g(-1) = g(1) = 0$. È suriettiva su $[-1, +\infty)$: $x^2 \ge 0$ dà $g(x) \ge -1$, e ogni $y \ge -1$ si raggiunge con $x = \sqrt{y + 1}$.
> 3. Su $[0, 2]$ la funzione $h(x) = x^2$ è crescente, quindi iniettiva. Non è suriettiva perché l'immagine va da $h(0) = 0$ a $h(2) = 4$, cioè $[0, 4]$, che è più piccola del codominio $[0, 5]$: il valore $5$ non viene mai raggiunto.

> [!question] Esercizio 5
> Date $f(x) = \dfrac{1}{x - 1}$ e $g(x) = x^2$, scrivere $f \circ g$ e $g \circ f$ con i loro domini, e calcolare $(f \circ g)(2)$ e $(g \circ f)(3)$.

> [!success]- Soluzione
> Risultato: $(f \circ g)(x) = \dfrac{1}{x^2 - 1}$ con dominio $\mathbb{R} \setminus \{-1, 1\}$; $(g \circ f)(x) = \dfrac{1}{(x - 1)^2}$ con dominio $\mathbb{R} \setminus \{1\}$; $(f \circ g)(2) = \frac13$ e $(g \circ f)(3) = \frac14$.
>
> Come si arriva:
> 1. $f \circ g$ vuol dire prima $g$, poi $f$: al posto della $x$ di $f$ si mette $x^2$:
>
> $$
> (f \circ g)(x) = f(x^2) = \frac{1}{x^2 - 1} .
> $$
>
> 2. Dominio di $f \circ g$: il denominatore non può essere zero, $x^2 - 1 \neq 0$, cioè $x \neq 1$ e $x \neq -1$. Dominio $\mathbb{R} \setminus \{-1, 1\}$.
> 3. $g \circ f$ vuol dire prima $f$, poi $g$: si eleva al quadrato tutta la $f$:
>
> $$
> (g \circ f)(x) = \left(\frac{1}{x - 1}\right)^2 = \frac{1}{(x - 1)^2} .
> $$
>
> 4. Dominio di $g \circ f$: il primo passo, $f$, richiede $x \neq 1$; poi $g$ non pone condizioni. Dominio $\mathbb{R} \setminus \{1\}$.
> 5. Valori: si sostituisce il numero nella formula trovata. $(f \circ g)(2) = \frac{1}{4 - 1} = \frac13$ e $(g \circ f)(3) = \frac{1}{(3 - 1)^2} = \frac14$. Le due composte sono diverse: l'ordine conta.

> [!question] Esercizio 6
> Sia $f(x) = \dfrac{x + 1}{x - 2}$. Trovare dominio e immagine, la funzione inversa, e verificare che $f(f^{-1}(x)) = x$.

> [!success]- Soluzione
> Risultato: dominio $\mathbb{R} \setminus \{2\}$, immagine $\mathbb{R} \setminus \{1\}$, inversa $f^{-1}(x) = \dfrac{2x + 1}{x - 1}$ con $x \neq 1$; la verifica dà $f(f^{-1}(x)) = x$.
>
> Come si arriva:
> 1. Dominio: il denominatore non può essere zero, $x - 2 \neq 0$, cioè $\mathbb{R} \setminus \{2\}$.
> 2. Per trovare immagine e inversa si pone $f(x) = y$ e si ricava $x$:
>
> $$
> \frac{x + 1}{x - 2} = y \;\Rightarrow\; x + 1 = y(x - 2) \;\Rightarrow\; x + 1 = xy - 2y \;\Rightarrow\; x - xy = -2y - 1 .
> $$
>
> 3. Si raccoglie la $x$: $x(1 - y) = -(2y + 1)$, cioè
>
> $$
> x = \frac{2y + 1}{y - 1} \qquad (y \neq 1) .
> $$
>
> 4. Immagine: per $y = 1$ l'equazione diventa $x + 1 = x - 2$, impossibile, quindi il valore $1$ non viene raggiunto. Per ogni altro $y$ c'è una e una sola $x$ (ed è $\neq 2$, perché sostituendo $x = 2$ si avrebbe $2y + 1 = 2y - 2$, impossibile). Immagine $\mathbb{R} \setminus \{1\}$, e la funzione è iniettiva.
> 5. Inversa: si scambiano le lettere $x$ e $y$:
>
> $$
> f^{-1}(x) = \frac{2x + 1}{x - 1}, \qquad x \neq 1 .
> $$
>
> 6. Verifica: si mette $f^{-1}(x)$ al posto della $x$ di $f$:
>
> $$
> f(f^{-1}(x)) = \frac{\frac{2x + 1}{x - 1} + 1}{\frac{2x + 1}{x - 1} - 2} = \frac{\frac{2x + 1 + x - 1}{x - 1}}{\frac{2x + 1 - 2x + 2}{x - 1}} = \frac{3x}{3} = x .
> $$
>
> 7. Controllo con un numero: $f(0) = \frac{1}{-2} = -\frac12$, e infatti $f^{-1}\left(-\frac12\right) = \frac{-1 + 1}{-\frac32} = 0$.

> [!question] Esercizio 7
> La funzione $f(x) = x^2 + 4x + 1$ non è iniettiva su $\mathbb{R}$. Restringere il dominio per ottenere una biezione con la sua immagine e scrivere l'inversa. Quale sarebbe l'inversa scegliendo l'altro ramo?

> [!success]- Soluzione
> Risultato: restringendo a $[-2, +\infty)$ si ha la biezione $f: [-2, +\infty) \to [-3, +\infty)$ con inversa $f^{-1}(x) = -2 + \sqrt{x + 3}$, $x \ge -3$. Con l'altro ramo, $(-\infty, -2]$, l'inversa è $f^{-1}(x) = -2 - \sqrt{x + 3}$, $x \ge -3$.
>
> Come si arriva:
> 1. Si completa il quadrato per trovare il vertice: $x^2 + 4x + 1 = (x^2 + 4x + 4) - 3 = (x + 2)^2 - 3$. È una parabola con il vertice in $(-2, -3)$ rivolta verso l'alto, quindi l'immagine è $[-3, +\infty)$.
> 2. Non è iniettiva perché è simmetrica rispetto al vertice: per esempio $f(-4) = f(0) = 1$.
> 3. Si sceglie il ramo destro, $x \ge -2$: qui la funzione è crescente, quindi $f: [-2, +\infty) \to [-3, +\infty)$ è biettiva.
> 4. Si ricava $x$: da $y = (x + 2)^2 - 3$ si ha $(x + 2)^2 = y + 3$; siccome sul ramo destro $x + 2 \ge 0$, si prende la radice positiva: $x + 2 = \sqrt{y + 3}$, cioè $x = -2 + \sqrt{y + 3}$.
> 5. Si scambiano le lettere e si ottiene l'inversa:
>
> $$
> f^{-1}(x) = -2 + \sqrt{x + 3}, \qquad x \ge -3 .
> $$
>
> 6. Ramo sinistro, $x \le -2$: ora $x + 2 \le 0$, quindi si prende la radice negativa, $x + 2 = -\sqrt{y + 3}$, e l'inversa è $f^{-1}(x) = -2 - \sqrt{x + 3}$, sempre per $x \ge -3$.
> 7. Controllo: con il ramo destro $f^{-1}(6) = -2 + 3 = 1$ e $f(1) = 1 + 4 + 1 = 6$; con il sinistro $f^{-1}(6) = -2 - 3 = -5$ e $f(-5) = 25 - 20 + 1 = 6$.

#### Primo gruppo: parità e grafici

> [!question] Esercizio 8
> Stabilire se sono pari, dispari o né pari né dispari:
>
> $$
> f(x) = x^3 - 4x, \qquad g(x) = \frac{x^2}{x^2 + 1}, \qquad h(x) = (x + 1)^2, \qquad k(x) = \frac{1}{x - 1} .
> $$

> [!success]- Soluzione
> Risultato: $f$ è dispari; $g$ è pari; $h$ non è né pari né dispari; $k$ non è né pari né dispari.
>
> Come si arriva (per ogni funzione si controlla che il dominio sia simmetrico e poi si calcola $f(-x)$):
> 1. $f$: dominio $\mathbb{R}$, simmetrico. $f(-x) = (-x)^3 - 4(-x) = -x^3 + 4x = -(x^3 - 4x) = -f(x)$, quindi è dispari (ci sono solo potenze dispari).
> 2. $g$: il denominatore $x^2 + 1$ non è mai zero, dominio $\mathbb{R}$. $g(-x) = \frac{(-x)^2}{(-x)^2 + 1} = \frac{x^2}{x^2 + 1} = g(x)$, quindi è pari.
> 3. $h$: dominio $\mathbb{R}$. $h(-x) = (1 - x)^2$, che in generale non è né $h(x)$ né $-h(x)$. Con un numero: $h(1) = 4$ e $h(-1) = 0$, né uguali né opposti. Quindi né pari né dispari. (Sviluppando, $h(x) = x^2 + 2x + 1$ mescola potenze pari e dispari.)
> 4. $k$: dominio $\mathbb{R} \setminus \{1\}$, che non è simmetrico: $-1$ c'è ma $1$ no. Quindi né pari né dispari, senza bisogno di fare conti.

> [!question] Esercizio 9
> Disegnare $y = 2 - |x + 1|$ a partire da $y = |x|$, indicando vertice, zeri, immagine e intervalli di monotonia.

> [!success]- Soluzione
> Risultato: è una «V» capovolta con il vertice in $(-1, 2)$ (il punto più alto); zeri $x = -3$ e $x = 1$; immagine $(-\infty, 2]$; crescente su $(-\infty, -1]$ e decrescente su $[-1, +\infty)$.
>
> Come si arriva (il grafico si costruisce per passi):
> 1. Si parte da $|x|$: una «V» con il vertice nell'origine.
> 2. $|x + 1|$: il $+1$ dentro sposta il grafico di $1$ verso sinistra, vertice in $(-1, 0)$.
> 3. $-|x + 1|$: il segno meno davanti riflette rispetto all'asse $x$, la «V» si capovolge e si apre verso il basso.
> 4. $2 - |x + 1|$: il $+2$ fuori sposta di $2$ verso l'alto, vertice in $(-1, 2)$, che è il punto più alto.
> 5. Zeri: si pone $y = 0$. $2 - |x + 1| = 0 \Rightarrow |x + 1| = 2 \Rightarrow x + 1 = 2$ oppure $x + 1 = -2$, cioè $x = 1$ e $x = -3$.
> 6. Immagine: $|x + 1| \ge 0$, quindi $2 - |x + 1| \le 2$, e i rami scendono senza limite. Immagine $(-\infty, 2]$.
> 7. Monotonia: a sinistra del vertice il grafico sale, a destra scende: crescente su $(-\infty, -1]$, decrescente su $[-1, +\infty)$.

> [!question] Esercizio 10
> Disegnare $y = |x^2 - 4x|$ e indicarne zeri, immagine e intervalli di monotonia.

> [!success]- Soluzione
> Risultato: zeri $x = 0$ e $x = 4$; immagine $[0, +\infty)$; decrescente su $(-\infty, 0]$, crescente su $[0, 2]$, decrescente su $[2, 4]$, crescente su $[4, +\infty)$.
>
> Come si arriva:
> 1. Si parte da $x^2 - 4x$. Completando il quadrato: $x^2 - 4x = (x - 2)^2 - 4$, parabola con il vertice in $(2, -4)$, rivolta verso l'alto, che taglia l'asse $x$ dove $x(x - 4) = 0$, cioè in $x = 0$ e $x = 4$.
> 2. Il valore assoluto rende positivi i valori negativi: tra $0$ e $4$ la parabola sta sotto l'asse $x$, e quell'arco viene ribaltato verso l'alto; il vertice $(2, -4)$ diventa $(2, 4)$. Fuori da $[0, 4]$ il grafico non cambia.
> 3. Zeri: sono gli stessi della parabola, $x = 0$ e $x = 4$.
> 4. Immagine: un valore assoluto non è mai negativo, vale $0$ negli zeri e i rami esterni salgono senza limite. Immagine $[0, +\infty)$.
> 5. Monotonia: si legge dal grafico, da sinistra a destra: decrescente su $(-\infty, 0]$, crescente su $[0, 2]$, decrescente su $[2, 4]$, crescente su $[4, +\infty)$.
> 6. Il punto $(2, 4)$ è il più alto dell'arco centrale, ma non di tutto il grafico: i rami esterni vanno più in alto.

#### Primo gruppo: un esercizio completo come quello del professore

> [!question] Esercizio 11
> Data $f(x) = \sqrt{x^2 + 1} - x$, trovare il dominio, l'immagine, la funzione inversa e verificare che $f(f^{-1}(x)) = x$.

> [!success]- Soluzione
> Risultato: dominio $\mathbb{R}$; immagine $(0, +\infty)$; inversa $f^{-1}(x) = \dfrac{1 - x^2}{2x}$ con $x > 0$; la verifica dà $f(f^{-1}(x)) = x$.
>
> Come si arriva, dominio:
> 1. Il radicando $x^2 + 1$ è sempre $\ge 1 > 0$, quindi non ci sono condizioni: $D = \mathbb{R}$.
>
> Come si arriva, immagine (con il metodo del professore):
> 1. Si pone $f(x) = y$ e si isola la radice: $\sqrt{x^2 + 1} = x + y$.
> 2. Condizione: la radice è $\ge 0$, quindi anche $x + y \ge 0$.
> 3. Si eleva al quadrato per togliere la radice: $x^2 + 1 = x^2 + 2xy + y^2$.
> 4. Gli $x^2$ si semplificano: $1 = 2xy + y^2$, cioè $2xy = 1 - y^2$.
> 5. Si ricava $x$. Se $y = 0$ si ottiene $0 = 1$, impossibile. Per $y \neq 0$:
>
> $$
> x = \frac{1 - y^2}{2y} .
> $$
>
> 6. Si impone la condizione del punto 2:
>
> $$
> x + y = \frac{1 - y^2}{2y} + y = \frac{1 - y^2 + 2y^2}{2y} = \frac{1 + y^2}{2y} \ge 0 .
> $$
>
> 7. Il numeratore $1 + y^2$ è sempre positivo, quindi la frazione è $\ge 0$ solo quando il denominatore è positivo: $y > 0$.
>
> $$
> \operatorname{Im} f = (0, +\infty) .
> $$
>
> 8. Senza la condizione si sbaglierebbe: con $y = -1$ il punto 5 darebbe $x = 0$, ma $f(0) = 1$, non $-1$.
>
> Come si arriva, inversa:
> 1. Per ogni $y > 0$ c'è una sola $x$, quindi $f: \mathbb{R} \to (0, +\infty)$ è biettiva.
> 2. Si scambiano le lettere nella formula del punto 5:
>
> $$
> f^{-1}(x) = \frac{1 - x^2}{2x}, \qquad x > 0 .
> $$
>
> 3. Controllo: $f^{-1}(1) = 0$ e $f(0) = 1$; $f^{-1}(2) = -\frac34$ e $f\left(-\frac34\right) = \sqrt{\frac{9}{16} + 1} + \frac34 = \frac54 + \frac34 = 2$.
>
> Come si arriva, verifica di $f \circ f^{-1}$ (si chiama $t = \frac{1 - x^2}{2x}$, con $x > 0$):
> 1. Si calcola il radicando:
>
> $$
> t^2 + 1 = \frac{(1 - x^2)^2 + 4x^2}{4x^2} = \frac{1 + 2x^2 + x^4}{4x^2} = \left(\frac{1 + x^2}{2x}\right)^2 .
> $$
>
> 2. La radice di un quadrato è il valore assoluto, ma $\frac{1 + x^2}{2x} > 0$ perché $x > 0$: $\sqrt{t^2 + 1} = \frac{1 + x^2}{2x}$.
> 3. Quindi
>
> $$
> f(f^{-1}(x)) = \frac{1 + x^2}{2x} - \frac{1 - x^2}{2x} = \frac{2x^2}{2x} = x .
> $$

#### Secondo gruppo: esponenziali e logaritmi

> [!question] Esercizio 12
> Calcolare esattamente
>
> $$
> \log_2 \frac18, \qquad \log_9 27, \qquad \ln \frac{1}{e^2}, \qquad e^{2 \ln 3} .
> $$

> [!success]- Soluzione
> Risultato: $\log_2 \frac18 = -3$; $\log_9 27 = \frac32$; $\ln \frac{1}{e^2} = -2$; $e^{2 \ln 3} = 9$.
>
> Come si arriva (il logaritmo è l'esponente da dare alla base, quindi si scrive l'argomento come potenza della base):
> 1. $\frac18 = 2^{-3}$, quindi $\log_2 \frac18 = -3$.
> 2. Si scrivono $9$ e $27$ come potenze di $3$: $9 = 3^2$, $27 = 3^3$. Si cerca $a$ con $9^a = 27$, cioè $3^{2a} = 3^3$: $2a = 3$, $a = \frac32$. Quindi $\log_9 27 = \frac32$.
> 3. $\frac{1}{e^2} = e^{-2}$, quindi $\ln \frac{1}{e^2} = -2$.
> 4. Si porta il $2$ dentro il logaritmo: $2 \ln 3 = \ln 3^2 = \ln 9$, e $e^{\ln 9} = 9$ perché esponenziale e logaritmo si annullano.

> [!question] Esercizio 13
> Risolvere:
>
> 1. $2^{x + 1} = 16$;
> 2. $4^x = 8$;
> 3. $\log_2(x + 1) + \log_2(x - 1) = 3$, indicando prima il dominio.

> [!success]- Soluzione
> Risultato: 1) $x = 3$; 2) $x = \frac32$; 3) dominio $x > 1$, soluzione $x = 3$ ($x = -3$ si scarta).
>
> Come si arriva:
> 1. Si scrive $16$ come potenza di $2$: $16 = 2^4$, quindi $2^{x + 1} = 2^4$; con la stessa base gli esponenti sono uguali, $x + 1 = 4$: $x = 3$.
> 2. Si porta tutto in base $2$: $4^x = (2^2)^x = 2^{2x}$ e $8 = 2^3$. Quindi $2x = 3$: $x = \frac32$.
> 3. Dominio: gli argomenti dei logaritmi devono essere positivi, $x + 1 > 0$ e $x - 1 > 0$, cioè $x > 1$.
> 4. Con la proprietà del prodotto si uniscono i due logaritmi e si toglie il logaritmo:
>
> $$
> \log_2\big((x + 1)(x - 1)\big) = 3 \;\Rightarrow\; x^2 - 1 = 2^3 = 8 \;\Rightarrow\; x^2 = 9 \;\Rightarrow\; x = \pm 3 .
> $$
>
> 5. Si confronta con il dominio: $x = -3$ non è nel dominio e si scarta. Soluzione $x = 3$.
> 6. Controllo: $\log_2 4 + \log_2 2 = 2 + 1 = 3$.

> [!question] Esercizio 14
> Risolvere le disequazioni
>
> $$
> \left(\frac13\right)^x > 9 \qquad \text{e} \qquad \ln(2x - 1) \le 0 .
> $$

> [!success]- Soluzione
> Risultato: la prima ha soluzione $x < -2$, cioè $(-\infty, -2)$; la seconda ha soluzione $\frac12 < x \le 1$, cioè $\left(\frac12, 1\right]$.
>
> Come si arriva, prima disequazione:
> 1. Si scrive $9$ come potenza di $\frac13$: $9 = 3^2 = \left(\frac13\right)^{-2}$, quindi $\left(\frac13\right)^x > \left(\frac13\right)^{-2}$.
> 2. La base $\frac13$ è minore di $1$, la funzione è decrescente e il verso si gira: $x < -2$.
>
> Come si arriva, seconda disequazione:
> 1. Dominio: l'argomento del logaritmo deve essere positivo, $2x - 1 > 0$, cioè $x > \frac12$.
> 2. Si scrive $0$ come logaritmo: $0 = \ln 1$, quindi $\ln(2x - 1) \le \ln 1$.
> 3. La base $e$ è maggiore di $1$ e il verso resta: $2x - 1 \le 1$, cioè $x \le 1$.
> 4. Si mettono insieme dominio e disequazione: $\frac12 < x \le 1$, cioè $\left(\frac12, 1\right]$.

> [!question] Esercizio 15
> Per $f(x) = 2 + e^{x - 1}$ determinare dominio, immagine, monotonia, asintoto e la funzione inversa.

> [!success]- Soluzione
> Risultato: dominio $\mathbb{R}$; immagine $(2, +\infty)$; crescente su tutto $\mathbb{R}$; asintoto orizzontale $y = 2$ per $x \to -\infty$; inversa $f^{-1}(x) = 1 + \ln(x - 2)$ con $x > 2$.
>
> Come si arriva:
> 1. Dominio: l'esponenziale è definito ovunque, quindi $\mathbb{R}$.
> 2. Grafico: è quello di $e^x$ traslato di $1$ verso destra e di $2$ verso l'alto.
> 3. Immagine: $e^{x - 1} > 0$ per ogni $x$, quindi $f(x) > 2$, e si raggiungono tutti i valori sopra $2$. Immagine $(2, +\infty)$.
> 4. Monotonia: $e^x$ è crescente e le traslazioni non cambiano la monotonia, quindi $f$ è crescente su tutto $\mathbb{R}$ (e dunque iniettiva).
> 5. Asintoto orizzontale: per $x \to -\infty$ l'esponenziale tende a $0$ e il grafico si avvicina alla retta $y = 2$.
> 6. Inversa: si pone $f(x) = y$ e si ricava $x$, togliendo l'esponenziale con il logaritmo: $y = 2 + e^{x - 1} \Rightarrow e^{x - 1} = y - 2 \Rightarrow x - 1 = \ln(y - 2) \Rightarrow x = 1 + \ln(y - 2)$. Scambiando le lettere:
>
> $$
> f^{-1}(x) = 1 + \ln(x - 2), \qquad x > 2 .
> $$
>
> 7. Controllo: $f(1) = 2 + e^0 = 3$ e $f^{-1}(3) = 1 + \ln 1 = 1$.

#### Secondo gruppo: trigonometria

> [!question] Esercizio 16
> 1. Risolvere su $[0, 2\pi]$: $2\cos x - 1 = 0$ e $\sin x = -\dfrac{\sqrt2}{2}$.
> 2. Calcolare $\arcsin \dfrac{\sqrt3}{2}$ e $\arctan(-1)$.

> [!success]- Soluzione
> Risultato: 1) $2\cos x - 1 = 0$ ha soluzioni $x = \frac{\pi}{3}$ e $x = \frac{5\pi}{3}$; $\sin x = -\frac{\sqrt2}{2}$ ha soluzioni $x = \frac{5\pi}{4}$ e $x = \frac{7\pi}{4}$. 2) $\arcsin \frac{\sqrt3}{2} = \frac{\pi}{3}$ e $\arctan(-1) = -\frac{\pi}{4}$.
>
> Come si arriva:
> 1. $2\cos x - 1 = 0$ vuol dire $\cos x = \frac12$. Sulla circonferenza goniometrica il coseno vale $\frac12$ nel primo quadrante, in $x = \frac{\pi}{3}$, e nel quarto, nel punto simmetrico rispetto all'asse $x$: $x = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}$.
> 2. $\sin x = -\frac{\sqrt2}{2}$: il seno è negativo nel terzo e nel quarto quadrante, e l'angolo di riferimento è $\frac{\pi}{4}$. Soluzioni $x = \pi + \frac{\pi}{4} = \frac{5\pi}{4}$ e $x = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4}$.
> 3. $\arcsin \frac{\sqrt3}{2}$ è l'angolo di $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ con seno $\frac{\sqrt3}{2}$: $\frac{\pi}{3}$.
> 4. $\arctan(-1)$ è l'angolo di $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ con tangente $-1$: $-\frac{\pi}{4}$ (non $\frac{3\pi}{4}$, che ha anch'esso tangente $-1$ ma sta fuori dall'intervallo).

## Collegamenti

Il dominio naturale si trova risolvendo le equazioni e le disequazioni di [[02-equazioni-e-disequazioni|equazioni e disequazioni]]: ogni condizione (denominatore diverso da zero, radicando non negativo) è una disequazione, e quando le condizioni sono più di una si risolve un sistema. Anche gli zeri di una funzione e il calcolo dell'immagine si riducono a equazioni.

Molti grafici di questa pagina sono figure già incontrate in [[03-retta-e-circonferenza|retta e circonferenza]]. Le funzioni $f(x) = mx + q$ hanno per grafico una retta, con pendenza $m$; le funzioni di secondo grado hanno per grafico una parabola. La circonferenza invece non supera il test della retta verticale e non è il grafico di una funzione: è il primo esempio di curva descritta da un'equazione in $x$ e $y$ che non si può scrivere come $y = f(x)$. Le traslazioni sono le stesse che portano la circonferenza di centro l'origine in quella di centro $(a, b)$; in termini di [[05-i-vettori|vettori]], traslare un grafico vuol dire spostare ogni suo punto dello stesso vettore $(a, b)$.

Gli zeri della parabola, i domini e le disequazioni logaritmiche si riducono alle equazioni e disequazioni di primo e secondo grado di [[02-equazioni-e-disequazioni]], con l'unica regola nuova del verso che si inverte quando la base è minore di $1$.

Nella seconda parte della pagina questi strumenti si applicano alle funzioni elementari: il logaritmo è l'inversa dell'esponenziale e le funzioni $\arcsin$, $\arccos$, $\arctan$ sono le inverse di seno, coseno e tangente ristrette a un intervallo, esattamente come $\sqrt{x}$ è l'inversa di $x^2$ ristretta a $[0, +\infty)$.

Per Architettura le funzioni sono il linguaggio con cui si descrive come una grandezza dipende da un'altra: l'area di un ambiente in funzione del lato, il costo in funzione del tempo, la pendenza di una rampa. In [[03-proiezioni-ortogonali-punto-e-rette|Geometria descrittiva]] la proiezione ortogonale su un piano è una funzione che a ogni punto dello spazio associa un solo punto del foglio, ma non è iniettiva: tutti i punti della stessa retta proiettante hanno la stessa proiezione. È per questo che una sola proiezione non basta a individuare un punto e il metodo di Monge ne usa due.

La funzione lineare è la [[03-retta-e-circonferenza|retta]] già studiata in geometria analitica, e la circonferenza goniometrica è la circonferenza $x^2 + y^2 = 1$ della stessa pagina; il legame più utile è che il coefficiente angolare di una retta è la tangente dell'angolo che la retta forma con l'asse $x$, ed è la stessa idea della pendenza in percentuale. Anche i [[05-i-vettori|vettori]] tornano qui: un versore del piano si scrive sempre come $(\cos\theta, \sin\theta)$, e l'angolo fra due vettori si trova con il prodotto scalare e poi con l'arcocoseno, ed è per questo che l'immagine di $\arccos$ è $[0, \pi]$, proprio l'insieme degli angoli possibili fra due vettori.

Nel resto del corso queste funzioni diventano la base per i limiti (gli asintoti), per le derivate (il numero $e$ si giustifica lì) e per lo studio di funzione. In Architettura la trigonometria serve ogni volta che si passa da una pendenza a un angolo (rampe, scale, falde dei tetti), e in Geometria descrittiva l'inclinazione di una retta o di un piano rispetto al piano orizzontale è proprio un angolo di cui la pendenza è la tangente.

## Per approfondire

- `Esercizi_funzioni_e_Logaritmi.pdf` (in `materiale/`), prima pagina, «Funzioni e funzioni elementari»: esercizi 1-4 su dominio e immagine, 5-10 su proprietà e operazioni, 11-15 su grafici e ragionamento. Quasi tutti sono svolti in questa pagina come esempi.
- I tuoi appunti in `materiale/`: `appunti-nadia-11.jpeg` (l'esercizio del professore su $\sqrt{x^2 - x} - x$, svolto per intero in questa pagina) e `appunti-nadia-02.jpeg` (la prima idea di funzione con il diagramma a frecce).
- La sezione [[#ESERCIZI|Esercizi]] di questa pagina: l'elenco degli esercizi del professore e dove sono svolti, più 16 esercizi nuovi con soluzione (11 sulle funzioni in generale, 5 sulle funzioni elementari).
- [[00-ripasso-esonero-1]], sezioni 6 e 7 («Funzioni» ed «Esponenziali, logaritmi, trigonometria»): le formule e i procedimenti in forma breve, per il ripasso finale.
- [[Esercizi_funzioni_e_Logaritmi.pdf]], seconda pagina («Esponenziali, logaritmi e trigonometria»): tutti e venti gli esercizi sono svolti come esempi in questa pagina (il 17, un vero o falso, è diviso fra l'avvertenza sugli errori con i logaritmi e quella sulle funzioni inverse).
- [[Esercizi_funzioni_e_Logaritmi.pdf]], prima pagina: esercizi 10, 11, 12 e 15 (monotonia, valore assoluto, parabola, tariffa lineare).
- Il [[Programma del corso_Istituzioni_di_matematiche_1_canale_1.pdf|programma del corso]] mette esponenziale e logaritmo nella parte sulla continuità: il professore li riprenderà dopo i limiti.
- Il libro di testo adottato è lo Stewart, *Calcolo. Funzioni di una variabile*: le funzioni, i grafici, le funzioni elementari, l'esponenziale, le inverse e il logaritmo sono nel primo capitolo, e la trigonometria è ripassata nelle appendici. Nella cartella del materiale c'è solo il capitolo sui vettori.
