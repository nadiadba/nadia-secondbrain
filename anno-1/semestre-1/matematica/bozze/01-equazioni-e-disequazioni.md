---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Equazioni e disequazioni

Equazioni e disequazioni sono il primo argomento del corso e lo strumento che serve in tutti gli altri: per trovare dove una retta incontra una circonferenza, per calcolare il dominio di una funzione, per capire dove un grafico sta sopra o sotto l'asse $x$. Questa pagina parte da che cosa vuol dire "risolvere" e arriva ai tipi che compaiono negli esercizi: primo e secondo grado, frazionarie, con valore assoluto, irrazionali, e poi le disequazioni con i loro metodi (la parabola, la tabella dei segni, i sistemi).

> [!info] Note collegate
> Teoria: [[02-retta-e-circonferenza]] · [[03-i-vettori]] · [[04-le-funzioni]] · [[05-funzioni-elementari]] · [[06-le-matrici]] · [[07-insiemi-e-intervalli]] · Ripasso: [[00-ripasso-esonero-1]]

## POTENZE E RADICALI

Prima delle equazioni il professore ha ripassato il calcolo con potenze e radici, che serve continuamente per semplificare le espressioni prima di risolverle.

### Le proprietà delle potenze

Una *potenza* $a^n$ è il prodotto di $n$ fattori uguali ad $a$: $3^4 = 3 \cdot 3 \cdot 3 \cdot 3 = 81$. Il numero $a$ si chiama *base*, $n$ *esponente*.

Tutte le proprietà vengono da questa definizione: basta contare i fattori. Per esempio $3^2 \cdot 3^3 = (3 \cdot 3) \cdot (3 \cdot 3 \cdot 3) = 3^5$, perché in tutto i fattori $3$ sono cinque.

> [!abstract] Proprietà delle potenze (con la stessa base)
> - Prodotto: $a^m \cdot a^n = a^{m+n}$ (gli esponenti si sommano). Esempio: $3^2 \cdot 3^3 = 3^5$.
> - Quoziente: $\dfrac{a^m}{a^n} = a^{m-n}$ (gli esponenti si sottraggono). Esempio: $\dfrac{3^7}{3^4} = 3^3$.
> - Potenza di potenza: $(a^m)^n = a^{m \cdot n}$ (gli esponenti si moltiplicano). Esempio: $(3^3)^4 = 3^{12}$.
> - Esponente zero: $a^0 = 1$ (con $a \neq 0$). Esempio: $3^0 = 1$.
> - Esponente negativo: $a^{-n} = \dfrac{1}{a^n}$. Esempio: $3^{-2} = \dfrac{1}{9}$.

Le ultime due regole non sono arbitrarie: seguono dalla regola del quoziente. Infatti $\frac{3^4}{3^4} = 1$, ma per la regola è anche $3^{4-4} = 3^0$; e $\frac{3^2}{3^4} = \frac{1}{3^2}$, ma per la regola è anche $3^{2-4} = 3^{-2}$.

> [!warning] Errore tipico
> Le regole valgono solo per prodotti e quozienti con la stessa base. Non esiste una regola per la somma: $3^2 + 3^3 = 9 + 27 = 36$, che non è $3^5 = 243$.

### I radicali come potenze con esponente frazionario

La *radice* $n$-esima di un numero, $\sqrt[n]{a}$, è il numero che elevato alla $n$ dà $a$: $\sqrt[3]{27} = 3$ perché $3^3 = 27$.

Il passaggio chiave, quello che il professore ha usato alla lavagna, è che ogni radice si può scrivere come una potenza con esponente frazionario.

> [!abstract] Radicali e potenze
> $$
> \sqrt[n]{a^m} = a^{\frac{m}{n}} \qquad (a > 0)
> $$
> L'esponente che sta dentro la radice va al numeratore, l'indice della radice al denominatore. Esempi: $\sqrt[5]{3^2} = 3^{\frac{2}{5}}$, $\sqrt[6]{3^4} = 3^{\frac{4}{6}} = 3^{\frac{2}{3}}$.

Perché proprio così? Per la regola della potenza di potenza: $\left(3^{\frac{1}{2}}\right)^2 = 3^{\frac{1}{2} \cdot 2} = 3^1 = 3$, quindi $3^{\frac{1}{2}}$ è il numero che al quadrato dà $3$, cioè $\sqrt{3}$.

Il vantaggio è che, scritti come potenze, i radicali obbediscono alle stesse regole delle potenze: per moltiplicarli o dividerli basta sommare o sottrarre gli esponenti, anche se le radici hanno indici diversi.

Il metodo per semplificare un'espressione con potenze e radici è quindi:

1. scrivere ogni numero come potenza della stessa base (qui $27 = 3^3$, $9 = 3^2$, $81 = 3^4$);
2. trasformare le radici in potenze con esponente frazionario;
3. applicare le regole degli esponenti;
4. se serve, tornare alla scrittura con la radice.

> [!example] Esempio svolto dal professore
> Semplificare
> $$
> \frac{27^4 \cdot \sqrt[5]{9}}{3^7 \cdot \sqrt[6]{81}}
> $$
>
> 1. Scrivo tutto in base $3$: $27 = 3^3$, $9 = 3^2$, $81 = 3^4$:
> $$
> \frac{(3^3)^4 \cdot \sqrt[5]{3^2}}{3^7 \cdot \sqrt[6]{3^4}}
> $$
> 2. Potenza di potenza e radici come potenze: $(3^3)^4 = 3^{12}$, $\sqrt[5]{3^2} = 3^{\frac{2}{5}}$, $\sqrt[6]{3^4} = 3^{\frac{4}{6}} = 3^{\frac{2}{3}}$:
> $$
> \frac{3^{12} \cdot 3^{\frac{2}{5}}}{3^7 \cdot 3^{\frac{2}{3}}}
> $$
> 3. Prodotto di potenze, sopra e sotto: al numeratore $12 + \frac{2}{5} = \frac{62}{5}$, al denominatore $7 + \frac{2}{3} = \frac{23}{3}$:
> $$
> \frac{3^{\frac{62}{5}}}{3^{\frac{23}{3}}} = \frac{\sqrt[5]{3^{62}}}{\sqrt[3]{3^{23}}}
> $$
> 4. Quoziente di potenze: sottraggo gli esponenti, con denominatore comune $15$:
> $$
> 3^{\frac{62}{5} - \frac{23}{3}} = 3^{\frac{186 - 115}{15}} = 3^{\frac{71}{15}}
> $$
>
> Risultato: $3^{\frac{71}{15}}$, cioè $\sqrt[15]{3^{71}}$.

Le potenze e le radici come funzioni, con i loro grafici, sono in [[05-funzioni-elementari]].

## EQUAZIONI

### Che cos'è un'equazione

Un'*equazione* è un'uguaglianza tra due espressioni che contiene una lettera sconosciuta, l'*incognita* (di solito $x$).

Per esempio $2x + 1 = 7$ non è né vera né falsa finché non si sa quanto vale $x$: è vera se $x = 3$, falsa per qualunque altro numero.

Risolvere l'equazione vuol dire trovare tutti i numeri che, messi al posto di $x$, rendono vera l'uguaglianza. Questi numeri si chiamano *soluzioni* (o *radici*), e il loro insieme si chiama *insieme delle soluzioni*.

Un'equazione può avere:

- una sola soluzione ($2x + 1 = 7$ ha solo $x = 3$);
- più soluzioni ($x^2 = 4$ ha $x = 2$ e $x = -2$);
- nessuna soluzione: si dice *impossibile* ($x^2 = -1$, perché nessun quadrato è negativo);
- infinite soluzioni: si dice *indeterminata* o *identità* ($x + x = 2x$ è vera per ogni $x$).

Per controllare se un numero è soluzione basta sostituirlo: se i due lati vengono uguali, è soluzione. Questo controllo si chiama *verifica*, e in alcuni tipi di equazione (le irrazionali, più avanti) è obbligatorio.

### I principi di equivalenza

Due equazioni sono *equivalenti* se hanno esattamente le stesse soluzioni. Risolvere un'equazione vuol dire trasformarla, passo dopo passo, in equazioni equivalenti sempre più semplici, fino ad arrivare a una forma come $x = 3$, che si legge da sola.

Le trasformazioni permesse sono due, e si chiamano principi di equivalenza.

> [!abstract] Principi di equivalenza delle equazioni
> 1. Primo principio: si può aggiungere o togliere lo stesso numero (o la stessa espressione) a entrambi i lati.
> 2. Secondo principio: si possono moltiplicare o dividere entrambi i lati per lo stesso numero, purché diverso da zero.

Dal primo principio viene la regola pratica del "trasporto": un termine può passare da un lato all'altro cambiando segno. Infatti in $x + 5 = 9$ togliere $5$ da entrambi i lati dà $x = 9 - 5$: è come se il $+5$ fosse passato a destra diventando $-5$.

Dal secondo principio viene la possibilità di dividere per il coefficiente di $x$: da $3x = 12$, dividendo entrambi i lati per $3$, si ottiene $x = 4$.

Perché si esclude lo zero? Perché moltiplicando per zero ogni equazione diventa $0 = 0$, che è sempre vera: si perderebbe tutta l'informazione. E dividere per zero non ha senso.

> [!warning] Dividere per un'espressione con la $x$
> In $x^2 = 3x$ viene voglia di dividere per $x$ e scrivere $x = 3$. Ma $x$ potrebbe essere zero, e infatti $x = 0$ è una soluzione che così si perde. La strada giusta è portare tutto a sinistra e raccogliere: $x^2 - 3x = 0$, cioè $x(x - 3) = 0$, che dà $x = 0$ oppure $x = 3$.

### Equazioni di primo grado

Un'equazione è di *primo grado* quando, dopo aver svolto i calcoli, la $x$ compare solo alla prima potenza. Ogni equazione di primo grado si può ridurre alla forma

$$
ax = b
$$

Il procedimento è sempre lo stesso:

1. si eliminano le parentesi svolgendo i prodotti;
2. se ci sono frazioni numeriche, si moltiplicano entrambi i lati per il minimo comune multiplo dei denominatori, così le frazioni spariscono;
3. si portano i termini con la $x$ a sinistra e i numeri a destra (trasporto, cambiando segno);
4. si sommano i termini simili e si arriva a $ax = b$;
5. si divide per $a$.

Alla fine ci sono tre possibilità, a seconda dei numeri $a$ e $b$:

- se $a \neq 0$ c'è una sola soluzione, $x = \dfrac{b}{a}$;
- se $a = 0$ e $b \neq 0$ l'equazione diventa $0 = b$, falsa: è impossibile;
- se $a = 0$ e $b = 0$ diventa $0 = 0$, sempre vera: è indeterminata.

> [!example] Esempio svolto: primo grado
> Risolvere $3(x - 2) + 5 = 2x + 7$.
>
> 1. Tolgo la parentesi: $3x - 6 + 5 = 2x + 7$, cioè $3x - 1 = 2x + 7$.
> 2. Porto $2x$ a sinistra e $-1$ a destra, cambiando segno: $3x - 2x = 7 + 1$.
> 3. Sommo: $x = 8$.
>
> Verifica: a sinistra $3 \cdot 6 + 5 = 23$, a destra $16 + 7 = 23$. Uguali, quindi $x = 8$ è la soluzione.
>
> Con le frazioni: $\dfrac{x - 1}{2} + \dfrac{x}{3} = 2$. Il minimo comune multiplo di $2$ e $3$ è $6$; moltiplico tutto per $6$: $3(x - 1) + 2x = 12$, cioè $5x - 3 = 12$, $5x = 15$, $x = 3$.

In classe il professore ha fatto svolgere una serie di equazioni di primo grado, numerate dal 16 al 21. Sono tutte dello stesso tipo: si tolgono le parentesi, si porta la $x$ da una parte e i numeri dall'altra, si divide. Due di queste però sono impossibili, e conviene capire perché.

> [!example] Esercizi del professore 16, 18, 19, 20 (una soluzione)
> - Esercizio 16: $5x + 2(x + 1) - 3x = 4x - 3 + x$
>     - Tolgo la parentesi: $5x + 2x + 2 - 3x = 4x - 3 + x$, cioè $4x + 2 = 5x - 3$.
>     - Porto tutto a sinistra: $4x - 5x + 2 + 3 = 0$, cioè $-x + 5 = 0$.
>     - Soluzione: $x = 5$.
> - Esercizio 18: $2(5 + x) = 5x + 1$
>     - $10 + 2x = 5x + 1$, quindi $2x - 5x = 1 - 10$, cioè $-3x = -9$.
>     - Divido per $-3$: $x = 3$.
> - Esercizio 19: $3(3 + x) - x = 5x + 14$
>     - $9 + 3x - x = 5x + 14$, quindi $3x - x - 5x = 14 - 9$, cioè $-3x = 5$.
>     - Divido per $-3$: $x = -\dfrac{5}{3}$.
> - Esercizio 20: $4(x - 3) - 3(x - 5) = 3(x + 1)$
>     - $4x - 12 - 3x + 15 = 3x + 3$ (attenzione al segno: $-3 \cdot (-5) = +15$).
>     - $4x - 3x - 3x = 3 + 12 - 15$, cioè $-2x = 0$.
>     - Soluzione: $x = 0$. Una soluzione uguale a zero è una soluzione come le altre: l'equazione non è impossibile.

> [!example] Esercizi del professore 17 e 21 (impossibili)
> - Esercizio 17: $3x - 5 + 2(x - 3) = 1 + 5x$
>     - Tolgo la parentesi: $3x - 5 + 2x - 6 = 1 + 5x$, cioè $5x - 11 = 5x + 1$.
>     - Porto tutto a sinistra: $5x - 5x - 11 - 1 = 0$, cioè $-12 = 0$.
> - Esercizio 21: $8(x + 3) = 8x - 24$
>     - $8x + 24 = 8x - 24$, quindi $8x - 8x = -24 - 24$, cioè $0 = -48$.
>
> In tutti e due i casi i termini con la $x$ si cancellano, perché a sinistra e a destra c'è lo stesso numero di $x$ ($5x$ e $5x$, $8x$ e $8x$). Resta un'uguaglianza tra numeri falsa ($-12 = 0$, $0 = -48$). Nella forma $ax = b$ siamo nel caso $a = 0$, $b \neq 0$: qualunque numero si metta al posto di $x$, i due lati differiscono sempre della stessa quantità e non diventano mai uguali. Per esempio in 21 il lato sinistro supera il destro di $48$ per ogni $x$. L'equazione è impossibile: nessuna soluzione (negli appunti si scrive "IMP.").
>
> Se invece fosse rimasto $0 = 0$, l'equazione sarebbe stata indeterminata: vera per ogni $x$.

### Equazioni di secondo grado

Un'equazione è di *secondo grado* quando, dopo i calcoli, la potenza più alta della $x$ è $x^2$. Si porta tutto a sinistra e la si scrive nella *forma normale*

$$
ax^2 + bx + c = 0 \qquad (a \neq 0)
$$

dove $a$ è il coefficiente di $x^2$, $b$ quello di $x$ e $c$ il termine senza $x$ (il *termine noto*).

Prima di usare la formula conviene guardare se l'equazione è *incompleta*, cioè se manca $b$ o manca $c$: in quei casi si fa prima.

- Se manca $b$ ($ax^2 + c = 0$): si isola $x^2$. Per esempio $x^2 - 9 = 0$ dà $x^2 = 9$, quindi $x = 3$ oppure $x = -3$. Se invece $x^2$ risultasse uguale a un numero negativo, l'equazione sarebbe impossibile.
- Se manca $c$ ($ax^2 + bx = 0$): si raccoglie la $x$. Per esempio $x^2 - 4x = 0$ diventa $x(x - 4) = 0$, quindi $x = 0$ oppure $x = 4$.

Il secondo caso usa una proprietà che tornerà spesso, la *legge di annullamento del prodotto*.

> [!abstract] Legge di annullamento del prodotto
> Un prodotto è uguale a zero se e solo se almeno uno dei fattori è zero:
> $$
> A \cdot B = 0 \iff A = 0 \;\text{ oppure }\; B = 0
> $$

Per l'equazione completa si usa la formula risolutiva. Il numero sotto la radice si chiama *discriminante* e si indica con la lettera greca $\Delta$ (delta).

> [!abstract] Formula risolutiva dell'equazione di secondo grado
> $$
> x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a} \qquad \text{con} \qquad \Delta = b^2 - 4ac
> $$
> - $\Delta > 0$: due soluzioni distinte;
> - $\Delta = 0$: una sola soluzione (due soluzioni coincidenti), $x = -\dfrac{b}{2a}$;
> - $\Delta < 0$: nessuna soluzione reale, perché non esiste la radice quadrata di un numero negativo.

Il discriminante si chiama così proprio perché "discrimina", cioè distingue, i tre casi prima ancora di finire i conti.

> [!example] Esempio svolto: secondo grado
> Risolvere $2x^2 + 3x - 2 = 0$.
>
> 1. Leggo i coefficienti: $a = 2$, $b = 3$, $c = -2$.
> 2. Calcolo il discriminante: $\Delta = 3^2 - 4 \cdot 2 \cdot (-2) = 9 + 16 = 25$. È positivo: due soluzioni.
> 3. Applico la formula: $x = \dfrac{-3 \pm 5}{4}$, cioè $x_1 = \dfrac{2}{4} = \dfrac{1}{2}$ e $x_2 = \dfrac{-8}{4} = -2$.
>
> Verifica con $x = -2$: $2 \cdot 4 - 6 - 2 = 0$. Corretto.
>
> Altri due casi: $x^2 - 6x + 9 = 0$ ha $\Delta = 36 - 36 = 0$, una sola soluzione $x = 3$; $x^2 + x + 1 = 0$ ha $\Delta = 1 - 4 = -3 < 0$, nessuna soluzione.

Quando si conoscono le due soluzioni $x_1$ e $x_2$, il polinomio si può *scomporre*, cioè scrivere come prodotto:

$$
ax^2 + bx + c = a(x - x_1)(x - x_2)
$$

Per esempio $x^2 - 5x + 6$ ha soluzioni $2$ e $3$ (infatti $\Delta = 25 - 24 = 1$ e $x = \frac{5 \pm 1}{2}$), quindi $x^2 - 5x + 6 = (x - 2)(x - 3)$. La scomposizione si può anche fare al contrario: se si riconosce subito che due numeri hanno somma $5$ e prodotto $6$, si scrive la scomposizione e la legge di annullamento dà le soluzioni senza formula.

Quest'ultima osservazione è una regola generale, che il professore ha scritto alla lavagna subito dopo la scomposizione: somma e prodotto delle due soluzioni si leggono direttamente nei coefficienti, senza calcolarle.

> [!abstract] Somma e prodotto delle radici
> Se $x_1$ e $x_2$ sono le soluzioni di $ax^2 + bx + c = 0$, allora
> $$
> \begin{cases} x_1 + x_2 = -\dfrac{b}{a} \\[2mm] x_1 \cdot x_2 = \dfrac{c}{a} \end{cases}
> $$

Il perché viene dalla scomposizione. Svolgendo il prodotto $a(x - x_1)(x - x_2)$ si ottiene $a x^2 - a(x_1 + x_2)\,x + a\,x_1 x_2$. Questo deve essere lo stesso polinomio di $ax^2 + bx + c$, quindi i coefficienti devono coincidere:

- coefficiente di $x$: $-a(x_1 + x_2) = b$, cioè $x_1 + x_2 = -\dfrac{b}{a}$;
- termine noto: $a\,x_1 x_2 = c$, cioè $x_1 x_2 = \dfrac{c}{a}$.

> [!example] Esempio: controllare le soluzioni con somma e prodotto
> Per $2x^2 + 3x - 2 = 0$ (l'esempio svolto sopra) le soluzioni erano $\frac{1}{2}$ e $-2$.
>
> - Somma: $\frac{1}{2} + (-2) = -\frac{3}{2}$, e infatti $-\frac{b}{a} = -\frac{3}{2}$.
> - Prodotto: $\frac{1}{2} \cdot (-2) = -1$, e infatti $\frac{c}{a} = \frac{-2}{2} = -1$.
>
> Al contrario, per $x^2 - 7x + 10 = 0$ (qui $a = 1$) si cercano due numeri con somma $7$ e prodotto $10$: sono $2$ e $5$. Quindi $x^2 - 7x + 10 = (x - 2)(x - 5)$ e le soluzioni sono $x = 2$ e $x = 5$.

### Il legame con la parabola

Le equazioni di secondo grado hanno un significato geometrico, ed è quello che le rende facili da ricordare.

Il grafico di $y = ax^2 + bx + c$ è una *parabola*: una curva a forma di U, rivolta verso l'alto se $a > 0$ e verso il basso se $a < 0$.

Risolvere $ax^2 + bx + c = 0$ vuol dire cercare i punti della parabola in cui $y = 0$, cioè i punti in cui la parabola incontra l'asse $x$. Per questo i tre casi del discriminante corrispondono a tre figure.

![[01-parabola-discriminante.svg|620]]

- $\Delta > 0$: la parabola taglia l'asse $x$ in due punti, che sono le due soluzioni.
- $\Delta = 0$: la parabola tocca l'asse $x$ in un solo punto, il suo vertice.
- $\Delta < 0$: la parabola sta tutta sopra (o tutta sotto) l'asse $x$ e non lo incontra mai.

Questa immagine servirà di nuovo per le disequazioni di secondo grado, e la parabola come grafico di funzione torna in [[04-le-funzioni]].

## EQUAZIONI PARTICOLARI

### Equazioni frazionarie

Un'equazione è *frazionaria* quando la $x$ compare in un denominatore, come in $\dfrac{x+1}{x-3} = 2$.

Il problema nuovo è che una frazione con denominatore zero non esiste. Prima di tutto bisogna quindi escludere i valori di $x$ che annullano un denominatore: queste esclusioni si chiamano *condizioni di esistenza* (abbreviate C.E.).

Il procedimento è:

1. scrivere le condizioni di esistenza: ogni denominatore deve essere diverso da zero;
2. portare tutto allo stesso denominatore e poi eliminarlo (moltiplicando entrambi i lati);
3. risolvere l'equazione che resta, che di solito è di primo o di secondo grado;
4. confrontare le soluzioni con le condizioni di esistenza e scartare quelle escluse.

Il passo 4 è necessario perché, moltiplicando per un'espressione con la $x$, si può introdurre una soluzione che rende zero quell'espressione: per l'equazione semplificata va bene, per quella di partenza no.

> [!example] Esempio svolto: equazione frazionaria
> Risolvere $\dfrac{x^2}{x - 2} = \dfrac{4}{x - 2}$.
>
> 1. Condizioni di esistenza: $x - 2 \neq 0$, cioè $x \neq 2$.
> 2. I denominatori sono uguali: li elimino moltiplicando per $x - 2$, e resta $x^2 = 4$.
> 3. Le soluzioni di $x^2 = 4$ sono $x = 2$ e $x = -2$.
> 4. Confronto con le C.E.: $x = 2$ è escluso. Resta solo $x = -2$.
>
> Un caso più semplice: $\dfrac{x + 1}{x - 3} = 2$, con C.E. $x \neq 3$. Moltiplico per $x - 3$: $x + 1 = 2x - 6$, quindi $x = 7$, accettabile. Verifica: $\frac{8}{4} = 2$.

### Equazioni con il valore assoluto

Il *valore assoluto* di un numero è il numero senza il suo segno, e si indica con due sbarrette: $|5| = 5$, $|-5| = 5$, $|0| = 0$.

Geometricamente $|a|$ è la distanza del punto $a$ dallo zero sulla retta dei numeri; e $|a - b|$ è la distanza tra i punti $a$ e $b$. Per questo il valore assoluto non è mai negativo.

> [!abstract] Definizione di valore assoluto
> $$
> |A| = \begin{cases} A & \text{se } A \geq 0 \\ -A & \text{se } A < 0 \end{cases}
> $$
> Se il numero è già positivo (o zero) resta com'è; se è negativo gli si cambia segno.

Il caso più frequente è $|A(x)| = k$ con $k$ un numero:

- se $k > 0$, ci sono due possibilità: $A(x) = k$ oppure $A(x) = -k$;
- se $k = 0$, resta solo $A(x) = 0$;
- se $k < 0$, l'equazione è impossibile, perché un valore assoluto non può essere negativo.

Il perché è la definizione di distanza: $|x - 1| = 3$ chiede quali punti stanno a distanza $3$ dal punto $1$, e sono due, uno a destra e uno a sinistra.

![[01-valore-assoluto.svg|540]]

Il grafico di $y = |x - 1|$ è una V con la punta in $x = 1$: le soluzioni di $|x - 1| = 3$ sono le ascisse dei due punti in cui la V incontra la retta orizzontale $y = 3$.

Quando a destra dell'uguale c'è un'espressione con la $x$, invece di un numero, si usa la definizione e si studiano due casi separati: uno in cui l'argomento è positivo o nullo, uno in cui è negativo. In ciascun caso si tengono solo le soluzioni che rispettano la condizione del caso.

> [!example] Esempio svolto: valore assoluto
> Primo tipo: $|x - 1| = 3$. Due possibilità:
> - $x - 1 = 3$, cioè $x = 4$;
> - $x - 1 = -3$, cioè $x = -2$.
>
> Dagli esercizi del professore (foglio funzioni, es. 11): gli zeri di $|x + 1| - 2$ sono le soluzioni di $|x + 1| = 2$, cioè $x + 1 = 2$ oppure $x + 1 = -2$: $x = 1$ e $x = -3$.
>
> Secondo tipo: $|x - 3| = 2x$. Studio due casi.
> 1. Se $x - 3 \geq 0$, cioè $x \geq 3$, il valore assoluto si toglie così com'è: $x - 3 = 2x$, quindi $x = -3$. Ma $-3$ non è $\geq 3$: scartato.
> 2. Se $x - 3 < 0$, cioè $x < 3$, si cambia segno: $3 - x = 2x$, quindi $x = 1$. È $< 3$: accettato.
>
> Soluzione: $x = 1$. Verifica: $|1 - 3| = 2$ e $2 \cdot 1 = 2$.

### Equazioni irrazionali

Un'equazione è *irrazionale* quando la $x$ compare sotto una radice, come $\sqrt{x + 3} = x - 3$.

Qui ci sono due cose da sapere sulla radice quadrata:

- esiste solo se il numero sotto la radice (il *radicando*) è maggiore o uguale a zero;
- il suo risultato è sempre maggiore o uguale a zero: $\sqrt{9} = 3$, non $-3$.

L'idea per risolvere è eliminare la radice elevando al quadrato entrambi i lati. Ma elevare al quadrato non è un principio di equivalenza: $3 = -3$ è falso, eppure elevando al quadrato diventa $9 = 9$, vero. Quindi dopo il quadrato possono comparire soluzioni false, dette *soluzioni estranee*.

Ci sono due modi per non sbagliare.

1. Fare la verifica: si risolve l'equazione elevata al quadrato e poi si sostituisce ogni soluzione nell'equazione di partenza, scartando quelle che non funzionano.
2. Mettere prima le condizioni: per $\sqrt{A(x)} = B(x)$ serve $A(x) \geq 0$ (la radice esiste) e $B(x) \geq 0$ (il lato destro deve essere positivo o nullo come la radice). Con queste condizioni il quadrato non introduce soluzioni false.

> [!abstract] Equazione irrazionale con radice quadrata
> $$
> \sqrt{A(x)} = B(x) \iff \begin{cases} B(x) \geq 0 \\ A(x) = B(x)^2 \end{cases}
> $$
> La condizione $A(x) \geq 0$ è già compresa: se $A(x) = B(x)^2$, allora $A(x)$ è un quadrato e non può essere negativo.

> [!example] Esempio svolto: equazione irrazionale
> Risolvere $\sqrt{x + 3} = x - 3$.
>
> 1. Condizione: $x - 3 \geq 0$, cioè $x \geq 3$.
> 2. Elevo al quadrato: $x + 3 = (x - 3)^2 = x^2 - 6x + 9$.
> 3. Porto tutto a destra: $x^2 - 7x + 6 = 0$. $\Delta = 49 - 24 = 25$, quindi $x = \dfrac{7 \pm 5}{2}$: $x = 6$ oppure $x = 1$.
> 4. Confronto con la condizione $x \geq 3$: $x = 6$ va bene, $x = 1$ no.
>
> Verifica: con $x = 6$, $\sqrt{9} = 3$ e $6 - 3 = 3$, giusto. Con $x = 1$, $\sqrt{4} = 2$ ma $1 - 3 = -2$: diversi, quindi $x = 1$ è una soluzione estranea.

Il disegno spiega da dove viene la soluzione falsa. Elevando al quadrato si cercano i punti in cui la retta $y = x - 3$ incontra sia $y = \sqrt{x+3}$ sia $y = -\sqrt{x+3}$ (perché entrambe, al quadrato, danno $x + 3$). La soluzione vera è l'incontro con la curva piena; quella falsa è l'incontro con la curva tratteggiata, che non fa parte dell'equazione.

![[01-equazione-irrazionale.svg|540]]

## DISEQUAZIONI

### Intervalli e loro notazione

Una *disequazione* è come un'equazione, ma al posto dell'uguale ha uno dei segni $<$ (minore), $>$ (maggiore), $\leq$ (minore o uguale), $\geq$ (maggiore o uguale).

La differenza importante è che le soluzioni di solito non sono pochi numeri ma tratti interi della retta dei numeri reali: per esempio $x > 3$ è vera per $3{,}1$, per $4$, per $1000$, per infiniti numeri. Questi tratti si chiamano *intervalli*.

Un intervallo si scrive indicando i due estremi tra parentesi:

- la parentesi quadra $[\;]$ vuol dire che l'estremo è compreso (intervallo *chiuso* da quella parte);
- la parentesi tonda $(\;)$ vuol dire che l'estremo è escluso (intervallo *aperto* da quella parte);
- se l'intervallo continua senza fine si usa il simbolo $+\infty$ (più infinito) o $-\infty$ (meno infinito), sempre con la parentesi tonda, perché l'infinito non è un numero e non può essere "compreso".

Sulla retta reale l'intervallo si disegna come un tratto colorato: un pallino pieno all'estremo compreso, un pallino vuoto all'estremo escluso, una freccia se l'intervallo va all'infinito.

![[01-retta-reale-intervalli.svg|600]]

Quando le soluzioni sono formate da due pezzi separati si uniscono con il simbolo $\cup$ (si legge "unione"): per esempio $x \leq 2$ oppure $x \geq 3$ si scrive $(-\infty, 2] \cup [3, +\infty)$. L'insieme di tutti i numeri reali si scrive $\mathbb{R}$ oppure $(-\infty, +\infty)$.

Gli intervalli, l'unione e l'intersezione di insiemi, con l'esercizio del professore sull'intersezione di tre intervalli, sono spiegati per esteso in [[07-insiemi-e-intervalli]].

### La regola del verso

Per le disequazioni valgono gli stessi principi di equivalenza delle equazioni, con una differenza fondamentale nella moltiplicazione.

> [!abstract] Principi di equivalenza delle disequazioni
> 1. Aggiungendo o togliendo lo stesso numero a entrambi i lati, la disequazione resta equivalente (vale il trasporto con cambio di segno).
> 2. Moltiplicando o dividendo entrambi i lati per un numero positivo, la disequazione resta equivalente.
> 3. Moltiplicando o dividendo entrambi i lati per un numero negativo, bisogna invertire il verso: $<$ diventa $>$, $\leq$ diventa $\geq$, e viceversa.

Perché il verso si inverte? Si vede con i numeri: $2 < 5$ è vero. Moltiplicando per $-1$ si ottiene $-2$ e $-5$; ma sulla retta $-5$ sta più a sinistra di $-2$, quindi $-2 > -5$. Cambiare segno è come guardare la retta allo specchio rispetto allo zero: chi stava a sinistra finisce a destra, e l'ordine si rovescia.

> [!warning] Errore tipico
> Dimenticare di invertire il verso quando si divide per il coefficiente negativo della $x$. Da $-2x > 6$ si ottiene $x < -3$, non $x > -3$. Un controllo veloce: prova un numero. Con $x = -4$: $-2 \cdot (-4) = 8 > 6$, vero; e infatti $-4 < -3$.

### Disequazioni di primo grado

Si risolvono come le equazioni di primo grado, ricordando la regola del verso nell'ultimo passaggio. Si arriva a una forma come $ax > b$ e si divide per $a$: se $a$ è positivo il verso resta, se $a$ è negativo si inverte.

> [!example] Esempio svolto: primo grado
> Risolvere $3x - 2 > 7$.
> Trasporto: $3x > 9$. Divido per $3$ (positivo, il verso resta): $x > 3$. In intervalli: $(3, +\infty)$.
>
> Risolvere $-2x + 4 \geq 10$.
> Trasporto: $-2x \geq 6$. Divido per $-2$ (negativo, il verso si inverte): $x \leq -3$. In intervalli: $(-\infty, -3]$.
>
> Dagli esercizi del professore (foglio funzioni, es. 1): perché $\sqrt{5 - 2x}$ esista serve $5 - 2x \geq 0$, cioè $-2x \geq -5$, cioè $x \leq \dfrac{5}{2}$.

### Disequazioni di secondo grado

Per una disequazione come $ax^2 + bx + c > 0$ (o con $<$, $\geq$, $\leq$) non si "isola la $x$": si studia il segno del polinomio con l'aiuto della parabola.

Il ragionamento è questo. La disequazione $x^2 - 5x + 6 < 0$ chiede per quali $x$ il valore $y = x^2 - 5x + 6$ è negativo, cioè per quali $x$ la parabola sta sotto l'asse $x$. Basta quindi disegnare (anche a mano, in modo approssimato) la parabola e guardare.

Il procedimento:

1. si porta la disequazione alla forma $ax^2 + bx + c$ confrontato con $0$; conviene avere $a > 0$ (se $a$ è negativo, si moltiplica tutto per $-1$ e si inverte il verso);
2. si risolve l'equazione associata $ax^2 + bx + c = 0$, che dà i punti in cui la parabola incontra l'asse $x$;
3. si disegna la parabola (con $a > 0$ è rivolta verso l'alto) e si leggono gli intervalli in cui sta sopra o sotto l'asse.

![[01-parabola-segno.svg|540]]

Con $a > 0$ e $\Delta > 0$ il risultato si ricorda con due parole, *interno* ed *esterno*: la parabola è negativa tra le due radici (valori interni) e positiva fuori (valori esterni).

> [!abstract] Segno del trinomio di secondo grado (con $a > 0$)
> - $\Delta > 0$, radici $x_1 < x_2$: il trinomio è negativo per $x_1 < x < x_2$ (interno) e positivo per $x < x_1$ oppure $x > x_2$ (esterno).
> - $\Delta = 0$, radice $x_0$: il trinomio è positivo per ogni $x \neq x_0$ e vale zero in $x_0$; non è mai negativo.
> - $\Delta < 0$: il trinomio è positivo per ogni $x$; non è mai zero né negativo.

> [!example] Esempio svolto: secondo grado
> Risolvere $x^2 - 5x + 6 < 0$.
> 1. L'equazione associata $x^2 - 5x + 6 = 0$ ha radici $2$ e $3$.
> 2. $a = 1 > 0$: parabola verso l'alto. Il segno $<$ chiede dove è negativa: valori interni.
> 3. Soluzione: $2 < x < 3$, cioè $(2, 3)$.
>
> Con $x^2 - 5x + 6 \geq 0$ si prendono invece i valori esterni, radici comprese: $(-\infty, 2] \cup [3, +\infty)$.
>
> Risolvere $-x^2 + 4 > 0$. Qui $a = -1$: moltiplico per $-1$ e inverto il verso, $x^2 - 4 < 0$. Radici $\pm 2$, valori interni: $-2 < x < 2$.
>
> Casi senza radici distinte: $x^2 + x + 1 > 0$ ha $\Delta < 0$, quindi è vera per ogni $x$ ($\mathbb{R}$); $x^2 + x + 1 < 0$ non è mai vera (nessuna soluzione); $(x - 3)^2 > 0$ è vera per ogni $x \neq 3$.

> [!warning] Errore tipico
> Scrivere $x^2 < 4 \Rightarrow x < \pm 2$. Non ha senso: la soluzione è $-2 < x < 2$. Allo stesso modo $x^2 > 4$ dà $x < -2$ oppure $x > 2$. Nel dubbio, disegna la parabola $y = x^2 - 4$.

## DISEQUAZIONI CON PIÙ FATTORI E SISTEMI

### Prodotto e quoziente: la tabella dei segni

Quando la disequazione è un prodotto di fattori confrontato con zero, come $(x + 2)(x - 1)(x - 3) \geq 0$, non serve svolgere i prodotti. Si usa la *regola dei segni*: un prodotto è positivo se i fattori negativi sono in numero pari, negativo se sono in numero dispari. Vale lo stesso per un quoziente.

Il metodo della *tabella dei segni* organizza questo ragionamento.

1. Si porta tutto a sinistra, in modo che a destra ci sia $0$, e si scrive il lato sinistro come prodotto (o quoziente) di fattori semplici.
2. Per ogni fattore si studia quando è positivo, risolvendo "fattore $> 0$" (per i fattori al numeratore si può scrivere $\geq 0$).
3. Si disegna una riga per ogni fattore, sotto una retta con segnati i punti in cui ciascun fattore si annulla: linea continua dove il fattore è positivo, tratteggiata dove è negativo.
4. In ogni intervallo si contano i segni meno e si scrive il segno del risultato nell'ultima riga.
5. Si scelgono gli intervalli con il segno richiesto, decidendo a parte se gli estremi sono compresi.

![[01-tabella-segni.svg|600]]

> [!example] Esempio svolto: prodotto
> Risolvere $(x + 2)(x - 1)(x - 3) \geq 0$.
>
> 1. Segno dei fattori: $x + 2 > 0$ per $x > -2$; $x - 1 > 0$ per $x > 1$; $x - 3 > 0$ per $x > 3$.
> 2. I punti $-2$, $1$, $3$ dividono la retta in quattro intervalli. Contando i fattori negativi in ciascuno:
>    - per $x < -2$ sono negativi tutti e tre: il prodotto è negativo;
>    - per $-2 < x < 1$ sono negativi due: positivo;
>    - per $1 < x < 3$ è negativo uno: negativo;
>    - per $x > 3$ nessuno: positivo.
> 3. Il segno $\geq$ chiede i tratti positivi, con gli zeri compresi: $[-2, 1] \cup [3, +\infty)$.

### Disequazioni fratte

Una disequazione è *fratta* quando la $x$ compare al denominatore. Si studia esattamente con la tabella dei segni, con due attenzioni in più:

- il denominatore non può mai essere zero, quindi i punti in cui si annulla sono sempre esclusi (nella figura sono segnati con una crocetta);
- prima bisogna portare tutto a sinistra e fare un'unica frazione, con $0$ a destra.

Nel caso della figura, $\dfrac{(x + 2)(x - 1)}{x - 3} \geq 0$, i segni sono gli stessi del prodotto precedente, ma $x = 3$ va escluso perché annulla il denominatore. La soluzione diventa $[-2, 1] \cup (3, +\infty)$: tonda in $3$.

> [!warning] Non si moltiplica per il denominatore
> Nelle equazioni fratte si elimina il denominatore; nelle disequazioni no. Il denominatore contiene la $x$, quindi non si sa se è positivo o negativo, e di conseguenza non si sa se il verso va invertito. Per questo si porta tutto a sinistra e si studia il segno della frazione.

> [!example] Esempio svolto: disequazione fratta
> Risolvere $\dfrac{x + 1}{x - 2} \geq 2$.
>
> 1. Porto il $2$ a sinistra e faccio un'unica frazione:
> $$
> \frac{x + 1}{x - 2} - 2 \geq 0 \quad\Rightarrow\quad \frac{x + 1 - 2(x - 2)}{x - 2} \geq 0 \quad\Rightarrow\quad \frac{-x + 5}{x - 2} \geq 0
> $$
> 2. Numeratore: $-x + 5 \geq 0$ per $x \leq 5$. Denominatore: $x - 2 > 0$ per $x > 2$ (e $x \neq 2$).
> 3. Tabella:
>    - per $x < 2$: numeratore positivo, denominatore negativo, frazione negativa;
>    - per $2 < x < 5$: entrambi positivi, frazione positiva;
>    - per $x > 5$: numeratore negativo, denominatore positivo, frazione negativa.
> 4. Serve $\geq 0$: l'intervallo positivo, con $x = 5$ compreso (lì la frazione vale $0$) e $x = 2$ escluso.
>
> Soluzione: $(2, 5]$. Verifica con $x = 3$: $\frac{4}{1} = 4 \geq 2$, vero.

### Disequazioni con il valore assoluto

Il valore assoluto è una distanza, e questo dà le due regole principali. Con $k > 0$:

> [!abstract] Disequazioni con il valore assoluto ($k > 0$)
> $$
> |A| < k \iff -k < A < k \qquad\qquad |A| > k \iff A < -k \;\text{ oppure }\; A > k
> $$
> Minore: i valori interni. Maggiore: i valori esterni.

Il motivo si vede nella figura del valore assoluto: $|x - 1| < 3$ chiede i punti a distanza minore di $3$ dal punto $1$, cioè quelli tra $-2$ e $4$, dove la V sta sotto la retta $y = 3$. Al contrario $|x - 1| > 3$ chiede i punti lontani più di $3$, cioè quelli fuori.

Se $k$ è negativo il ragionamento è ancora più semplice, perché un valore assoluto non è mai negativo:

- $|A| < k$ con $k < 0$ non ha soluzioni;
- $|A| > k$ con $k < 0$ è vera per ogni $x$ in cui $A$ esiste.

> [!example] Esempio svolto: valore assoluto
> Risolvere $|x - 1| < 3$.
> Scrivo la doppia disequazione $-3 < x - 1 < 3$ e aggiungo $1$ a tutti e tre i membri: $-2 < x < 4$. Soluzione $(-2, 4)$.
>
> Risolvere $|x - 1| \geq 3$.
> Valori esterni: $x - 1 \leq -3$ oppure $x - 1 \geq 3$, cioè $x \leq -2$ oppure $x \geq 4$. Soluzione $(-\infty, -2] \cup [4, +\infty)$.
>
> Risolvere $|2x + 5| < -1$: impossibile, nessuna soluzione.

### Sistemi di disequazioni

Un *sistema di disequazioni* è un gruppo di disequazioni che devono essere vere tutte insieme. Si scrive con una parentesi graffa a sinistra:

$$
\begin{cases} 2x - 4 > 0 \\ x^2 - 3x - 4 \leq 0 \end{cases}
$$

Il procedimento è:

1. si risolve ogni disequazione da sola;
2. si disegnano le soluzioni una sotto l'altra, sulla stessa retta;
3. si prendono solo i tratti in cui le soluzioni si sovrappongono, cioè l'*intersezione* (simbolo $\cap$).

La differenza con la tabella dei segni è importante: nella tabella si moltiplicano i segni; nel sistema non si moltiplica nulla, si cerca solo dove valgono tutte le condizioni insieme.

![[01-sistema-disequazioni.svg|600]]

> [!example] Esempio svolto: sistema
> Risolvere il sistema scritto sopra.
>
> 1. Prima disequazione: $2x > 4$, quindi $x > 2$.
> 2. Seconda: l'equazione $x^2 - 3x - 4 = 0$ ha $\Delta = 9 + 16 = 25$ e radici $x = \frac{3 \pm 5}{2}$, cioè $-1$ e $4$. Con $\leq$ si prendono i valori interni, estremi compresi: $-1 \leq x \leq 4$.
> 3. Dove valgono entrambe: dopo $2$ (escluso) e fino a $4$ (compreso).
>
> Soluzione: $2 < x \leq 4$, cioè $(2, 4]$.
>
> Dagli esercizi del professore (foglio funzioni, es. 1): perché $\dfrac{\sqrt{x - 1}}{x - 4}$ esista servono insieme $x - 1 \geq 0$ (radice) e $x - 4 \neq 0$ (denominatore). Il sistema dà $x \geq 1$ e $x \neq 4$: $[1, 4) \cup (4, +\infty)$.

I sistemi sono il modo in cui si calcola il dominio di una funzione: ogni radice, denominatore o logaritmo aggiunge una condizione, e il dominio è l'insieme dei punti che le rispettano tutte. Se ne parla in [[04-le-funzioni]].

### Cenni: equazioni e disequazioni esponenziali e logaritmiche

Negli esercizi compaiono anche equazioni e disequazioni in cui la $x$ sta all'esponente ($3^{2x-1} = 27$) o dentro un logaritmo ($\ln(x - 2) = 3$). Si risolvono con le proprietà delle funzioni esponenziale e logaritmo, che sono spiegate in [[05-funzioni-elementari]]. Qui basta l'idea.

- Si cerca di scrivere i due lati come potenze della stessa base, e poi si confrontano gli esponenti: $3^{2x-1} = 27 = 3^3$ dà $2x - 1 = 3$, cioè $x = 2$.
- Nelle disequazioni conta la base: se è maggiore di $1$ il verso resta, se è tra $0$ e $1$ il verso si inverte. Per esempio $\left(\frac{1}{2}\right)^{x-2} \leq \frac{1}{8} = \left(\frac{1}{2}\right)^3$ dà $x - 2 \geq 3$, cioè $x \geq 5$.
- Con i logaritmi bisogna sempre mettere prima la condizione che l'argomento sia positivo, come le condizioni di esistenza delle frazionarie.

> [!example] Dagli esercizi del professore
> Foglio "Esponenziali, logaritmi e trigonometria", es. 6: $\log_{1/3}(2x + 1) < -1$.
>
> 1. Condizione: $2x + 1 > 0$, cioè $x > -\dfrac{1}{2}$.
> 2. Scrivo $-1$ come logaritmo in base $\frac{1}{3}$: $-1 = \log_{1/3} 3$.
> 3. La base $\frac{1}{3}$ è minore di $1$: il verso si inverte, $2x + 1 > 3$, cioè $x > 1$.
> 4. Metto insieme con la condizione: $x > 1$.
>
> I passaggi sulle basi e sui logaritmi sono spiegati in [[05-funzioni-elementari]].

## Collegamenti

Equazioni e disequazioni sono la grammatica di tutto il resto del corso. In [[02-retta-e-circonferenza|retta e circonferenza]] un punto appartiene a una retta se le sue coordinate soddisfano un'equazione di primo grado, e trovare dove una retta taglia una circonferenza vuol dire risolvere un'equazione di secondo grado, il cui discriminante dice se la retta è secante, tangente o esterna: è lo stesso schema dei tre casi della parabola. Nei [[03-i-vettori|vettori]] le condizioni di parallelismo e di ortogonalità diventano equazioni nelle componenti, e trovare una combinazione lineare vuol dire risolvere un piccolo sistema di equazioni di primo grado.

Nelle [[04-le-funzioni|funzioni]] le disequazioni servono a calcolare il dominio (sistemi di condizioni su radici, denominatori e logaritmi) e a studiare il segno di una funzione, cioè dove il grafico sta sopra o sotto l'asse $x$, con gli stessi metodi della parabola e della tabella dei segni; gli zeri di una funzione sono le soluzioni di un'equazione. Nelle [[05-funzioni-elementari|funzioni elementari]] si completano le equazioni e disequazioni esponenziali e logaritmiche accennate qui.

## Per approfondire

- [[Esercizi_funzioni_e_Logaritmi.pdf]]: foglio del professore. Nella prima pagina gli esercizi 1-4 (dominio) e 11-12 (zeri di $|x+1| - 2$ e di $-(x-1)^2 + 4$) sono equazioni e disequazioni applicate; nella seconda pagina gli esercizi 2, 3, 5 e 6 sono equazioni e disequazioni esponenziali e logaritmiche.
- [[Programma del corso_Istituzioni_di_matematiche_1_canale_1.pdf]]: il valore assoluto e i numeri reali sono nella prima parte del programma; i testi adottati (Stewart, *Calcolo*; Adams, *Calcolo differenziale I*; Bramanti, Pagani, Salsa, *Analisi Matematica 1*) trattano equazioni, disequazioni e valore assoluto nei capitoli introduttivi di richiamo.
- [[Giuffrida - Ragusa Cap 1_compressed.pdf]]: capitolo 1, insiemi e insiemi numerici ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$), con unione e intersezione, utili per leggere le soluzioni scritte come intervalli.
