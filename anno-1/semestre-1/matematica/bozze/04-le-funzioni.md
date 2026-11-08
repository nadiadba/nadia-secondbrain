---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Le funzioni: grafico, dominio, immagine, funzione inversa

Una funzione è una regola che a ogni numero di partenza fa corrispondere uno e un solo numero di arrivo. È l'idea più importante di tutto il corso: i limiti, le derivate e gli integrali che verranno dopo sono tutti modi di studiare le funzioni. Questa pagina parte dalla definizione, passa al grafico, al dominio e all'immagine, poi alle proprietà (iniettiva, suriettiva, pari, crescente...) e alla funzione inversa, e chiude con le operazioni che spostano e deformano i grafici. Gli esempi svolti seguono la prima pagina del foglio del professore, `Esercizi_funzioni_e_Logaritmi.pdf`.

> [!info] Note collegate
> Teoria: [[01-equazioni-e-disequazioni]] · [[02-retta-e-circonferenza]] · [[03-i-vettori]] · [[05-funzioni-elementari]] · [[06-le-matrici]] · Ripasso: [[00-ripasso-esonero-1]]

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

![[04-diagrammi-frecce.svg|700]]

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

![[04-area-quadrato.svg|500]]

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

![[04-retta-verticale.svg|700]]

La parabola $y = x^2$ supera il test: qualunque retta verticale la tocca una volta sola. La circonferenza $x^2 + y^2 = 4$ (quella di centro l'origine e raggio $2$, vista in [[02-retta-e-circonferenza]]) non lo supera: la retta $x = 1$ la incontra in $(1, \sqrt{3})$ e in $(1, -\sqrt{3})$. Al numero $1$ corrisponderebbero due valori, quindi la circonferenza non è il grafico di una funzione.

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

Il perché delle prime due regole si vede subito. Dividere $6$ per $0$ vorrebbe dire trovare un numero che moltiplicato per $0$ dia $6$, e non esiste. La radice quadrata di $-4$ dovrebbe essere un numero che al quadrato dà $-4$, ma un quadrato non è mai negativo. Il logaritmo è trattato in [[05-funzioni-elementari]].

Se nella formula ci sono più operazioni «delicate», le condizioni devono valere tutte insieme: si scrive un sistema e si prendono le $x$ che le soddisfano tutte. Le disequazioni che servono sono quelle di [[01-equazioni-e-disequazioni]].

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

![[04-dominio-esempi.svg|700]]

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

![[04-immagine-parabola.svg|500]]

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

![[04-immagine-radice.svg|500]]

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

![[04-retta-bucata.svg|460]]

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

![[04-retta-orizzontale.svg|700]]

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

![[04-restrizione-x2.svg|700]]

- $x^2: \mathbb{R} \to \mathbb{R}$ non è iniettiva ($(-1)^2 = 1^2$) e non è suriettiva (i numeri negativi del codominio non vengono mai raggiunti).
- $x^2: \mathbb{R} \to [0, +\infty)$ è suriettiva (ogni $y \ge 0$ è il quadrato di $\sqrt{y}$) ma non iniettiva.
- $x^2: [0, +\infty) \to [0, +\infty)$ è biettiva: tenendo solo le $x \ge 0 $ resta un solo ramo della parabola, che ogni retta orizzontale $y = k \ge 0$ incontra una volta sola.

> [!example] Esempio: classificare tre funzioni (esercizio 5)
> 1. $x^3: \mathbb{R} \to \mathbb{R}$. Iniettiva (test della retta orizzontale, figura sopra). Suriettiva: ogni numero reale $y$ è il cubo di $\sqrt[3]{y}$. Quindi biettiva.
> 2. $|x|: \mathbb{R} \to [0, +\infty)$. Non iniettiva: $|-3| = |3| = 3$. Suriettiva: ogni $y \ge 0$ è il valore assoluto di $y$ stesso. Quindi suriettiva ma non iniettiva.
> 3. $x^2: [-2, 2] \to [0, 4]$. Non iniettiva: $(-1)^2 = 1^2$, e $-1$ e $1$ stanno entrambi in $[-2, 2]$. Suriettiva: per $x \in [-2, 2]$ i quadrati vanno da $0$ (in $x = 0$) a $4$ (in $x = \pm 2$) e prendono tutti i valori intermedi, quindi l'immagine è $[0, 4]$, uguale al codominio.

> [!example] Esempio: costruire degli esempi (esercizio 13)
> - Iniettiva ma non suriettiva da $\mathbb{R}$ a $\mathbb{R}$: $f(x) = e^x$. È sempre crescente, quindi iniettiva, ma i suoi valori sono solo positivi: $0$ e i negativi non vengono mai raggiunti (si vede in [[05-funzioni-elementari]]).
> - Suriettiva ma non iniettiva da $\mathbb{R}$ a $[0, +\infty)$: $f(x) = x^2$ (oppure $|x|$). Raggiunge ogni $y \ge 0$, ma $x$ e $-x$ hanno lo stesso valore.

### La composizione di funzioni

Due funzioni si possono mettere «in fila», come due macchine: l'uscita della prima diventa l'entrata della seconda.

![[04-composizione.svg|620]]

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

![[04-tariffa.svg|500]]

Nel grafico l'inversa si legge al contrario: si parte da $10$ sull'asse verticale, si va in orizzontale fino alla retta e si scende sull'asse orizzontale, dove si legge $3$.

### Il grafico dell'inversa

Se il punto $(a, b)$ sta sul grafico di $f$, cioè $f(a) = b$, allora $f^{-1}(b) = a$, e quindi il punto $(b, a)$ sta sul grafico di $f^{-1}$. Le coordinate si scambiano.

Scambiare $x$ e $y$ ha un significato geometrico preciso: i punti $(a, b)$ e $(b, a)$ sono simmetrici rispetto alla bisettrice del primo e terzo quadrante, la retta $y = x$. Facendolo per tutti i punti si ottiene questa regola.

> [!abstract] Grafico della funzione inversa
> Il grafico di $f^{-1}$ si ottiene ribaltando il grafico di $f$ rispetto alla retta $y = x$ (come in uno specchio appoggiato su quella retta).

![[04-inversa-bisettrice.svg|700]]

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

![[04-restrizione-x-meno-1.svg|700]]

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

![[04-pari-dispari.svg|700]]

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

![[04-monotonia.svg|700]]

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

![[04-traslazioni.svg|700]]

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

![[04-riflessioni.svg|700]]

Con $-f(x)$ ogni valore cambia segno, quindi ogni punto $(x, y)$ diventa $(x, -y)$. Con $f(-x)$ quello che $f$ faceva in $3$ la nuova funzione lo fa in $-3$, quindi ogni punto $(x, y)$ diventa $(-x, y)$. Per $\sqrt{x}$: $-\sqrt{x}$ è lo stesso ramo capovolto verso il basso, $\sqrt{-x}$ è lo stesso ramo girato verso sinistra (il dominio diventa $x \le 0$).

Collegamento con la parità: una funzione è pari quando $f(-x) = f(x)$, cioè quando ribaltarla rispetto all'asse $y$ non la cambia.

### Valore assoluto e dilatazioni

Il valore assoluto rende positivo ciò che è negativo: $|5| = 5$, $|-5| = 5$. Applicato a tutta la funzione, lascia com'è la parte del grafico che sta sopra l'asse $x$ e ribalta verso l'alto quella che sta sotto.

> [!abstract] Valore assoluto e dilatazioni
> - $y = |f(x)|$: le parti del grafico sotto l'asse $x$ vengono ribaltate sopra; il resto non cambia. L'immagine non contiene mai numeri negativi.
> - $y = k\,f(x)$ con $k > 1$: il grafico si allunga in verticale (tutte le altezze vengono moltiplicate per $k$).
> - $y = k\,f(x)$ con $0 < k < 1$: il grafico si schiaccia in verticale.
> - $y = f(kx)$ con $k > 1$: il grafico si stringe in orizzontale verso l'asse $y$; con $0 < k < 1$ si allarga.

![[04-valore-assoluto-dilatazioni.svg|700]]

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

![[04-esercizio-11.svg|720]]

> [!example] Esempio: $y = -(x - 1)^2 + 4$ (esercizio 12)
> 1. Si parte da $y = x^2$.
> 2. $(x - 1)^2$: traslazione di $1$ a destra, vertice in $(1, 0)$.
> 3. $-(x - 1)^2$: riflessione rispetto all'asse $x$, la parabola si apre verso il basso.
> 4. $-(x - 1)^2 + 4$: traslazione di $4$ verso l'alto, vertice in $(1, 4)$.
>
> - Immagine: $(x-1)^2 \ge 0$, quindi $-(x-1)^2 \le 0$ e $-(x-1)^2 + 4 \le 4$. Il vertice $(1, 4)$ è il punto più alto e i rami scendono senza limite: immagine $(-\infty, 4]$.
> - Zeri: $-(x-1)^2 + 4 = 0 \Rightarrow (x-1)^2 = 4 \Rightarrow x - 1 = \pm 2$, cioè $x = 3$ e $x = -1$.

![[04-esercizio-12.svg|460]]

> [!warning] Errore tipico
> In $f(x - a)$ il segno inganna: $(x - 1)^2$ va a destra, $(x + 1)^2$ va a sinistra. Per non sbagliare, chiediti dove si annulla la parentesi: $(x - 1)$ si annulla in $x = 1$, quindi il vertice è in $x = 1$.

## Collegamenti

Il dominio naturale si trova risolvendo le equazioni e le disequazioni di [[01-equazioni-e-disequazioni|equazioni e disequazioni]]: ogni condizione (denominatore diverso da zero, radicando non negativo) è una disequazione, e quando le condizioni sono più di una si risolve un sistema. Anche gli zeri di una funzione e il calcolo dell'immagine si riducono a equazioni.

Molti grafici di questa pagina sono figure già incontrate in [[02-retta-e-circonferenza|retta e circonferenza]]. Le funzioni $f(x) = mx + q$ hanno per grafico una retta, con pendenza $m$; le funzioni di secondo grado hanno per grafico una parabola. La circonferenza invece non supera il test della retta verticale e non è il grafico di una funzione: è il primo esempio di curva descritta da un'equazione in $x$ e $y$ che non si può scrivere come $y = f(x)$. Le traslazioni sono le stesse che portano la circonferenza di centro l'origine in quella di centro $(a, b)$; in termini di [[03-i-vettori|vettori]], traslare un grafico vuol dire spostare ogni suo punto dello stesso vettore $(a, b)$.

La pagina successiva, [[05-funzioni-elementari|funzioni elementari]], applica tutti questi strumenti alle funzioni esponenziali, logaritmiche e trigonometriche: il logaritmo è l'inversa dell'esponenziale e le funzioni $\arcsin$, $\arccos$, $\arctan$ sono le inverse di seno, coseno e tangente ristrette a un intervallo, esattamente come $\sqrt{x}$ è l'inversa di $x^2$ ristretta a $[0, +\infty)$.

Per Architettura le funzioni sono il linguaggio con cui si descrive come una grandezza dipende da un'altra: l'area di un ambiente in funzione del lato, il costo in funzione del tempo, la pendenza di una rampa. In [[03-proiezioni-ortogonali-punto-e-rette|Geometria descrittiva]] la proiezione ortogonale su un piano è una funzione che a ogni punto dello spazio associa un solo punto del foglio, ma non è iniettiva: tutti i punti della stessa retta proiettante hanno la stessa proiezione. È per questo che una sola proiezione non basta a individuare un punto e il metodo di Monge ne usa due.

## Per approfondire

- `Esercizi_funzioni_e_Logaritmi.pdf` (in `materiale/`), prima pagina, «Funzioni e funzioni elementari»: esercizi 1-4 su dominio e immagine, 5-10 su proprietà e operazioni, 11-15 su grafici e ragionamento. Quasi tutti sono svolti in questa pagina come esempi.
- [[00-ripasso-esonero-1]], sezione 4 «Funzioni»: le formule e i procedimenti in forma breve, per il ripasso finale.
- James Stewart, *Calcolo. Funzioni di una variabile*, primo testo del programma del corso: il capitolo iniziale sulle funzioni tratta definizione, grafici, funzioni pari e dispari, trasformazioni dei grafici, composizione e funzioni inverse. Nella cartella `materiale/` del libro c'è solo il capitolo sui vettori, quindi questa parte va consultata sul libro.
