---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Insiemi, numeri e intervalli

Con gli insiemi il professore ha aperto il corso, nella prima lezione: dopo aver presentato il programma ha introdotto l'appartenenza, l'inclusione, le operazioni tra insiemi con le loro proprietà, e ha chiuso con un esercizio sugli intervalli della retta reale. Questa pagina riprende quella lezione, con la stessa notazione, e la completa con quello che il programma ufficiale mette all'inizio: i quantificatori e i simboli logici, gli insiemi numerici $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, la dimostrazione che $\sqrt{2}$ è irrazionale, il valore assoluto e gli intervalli. È il linguaggio con cui sono scritte tutte le altre pagine: le soluzioni di una disequazione, il dominio di una funzione, la condizione di parallelismo tra vettori.

> [!info] Note collegate
> Teoria: [[02-equazioni-e-disequazioni]] · [[03-retta-e-circonferenza]] · [[04-le-matrici]] · [[05-i-vettori]] · [[06-le-funzioni]] · Ripasso: [[00-ripasso-esonero-1]]

## PROGRAMMA DEL CORSO

### Il programma presentato a lezione

Nella prima lezione il professore ha presentato il corso con uno schema ad albero, che negli appunti di Nadia è copiato così.

> [!note] Il programma come l'ha presentato il professore (prima lezione)
> Due esoneri: negli appunti il primo è segnato per il 4 novembre (la data attuale è in [[00-piano-esonero-1]]).
>
> - Insiemi
> - Funzioni elementari
>     - algebriche: razionali, irrazionali, fratte
>     - trascendenti: esponenziali, logaritmiche, goniometriche
> - Equazioni e disequazioni
> - Algebra lineare: i vettori, con prodotto scalare, prodotto vettoriale e modulo
> - Calcolo differenziale: limiti, derivate, integrali

Il programma ufficiale del corso (Istituzioni di Matematiche I) comincia con le stesse cose, scritte in modo più tecnico: "Quantificatori. I numeri: naturali, interi, razionali, reali. Assiomi dei numeri reali. Irrazionalità di $\sqrt{2}$", e subito dopo "Valore assoluto. Densità di $\mathbb{Q}$ in $\mathbb{R}$".

Questa pagina copre proprio quella prima parte. Le altre voci dello schema hanno ciascuna la sua pagina: le equazioni e disequazioni in [[02-equazioni-e-disequazioni]], la geometria del piano in [[03-retta-e-circonferenza]], i vettori in [[05-i-vettori]], le funzioni in [[06-le-funzioni]] e [[06-le-funzioni#LE FUNZIONI ELEMENTARI: RETTE, POTENZE, RADICI E VALORE ASSOLUTO|funzioni elementari]], le matrici in [[04-le-matrici]].

## IL LINGUAGGIO: SIMBOLI LOGICI E QUANTIFICATORI

### Proposizioni e connettivi

In matematica una *proposizione* è una frase di cui si può dire con certezza se è vera o falsa. "$3 < 5$" è una proposizione vera; "$7$ è pari" è una proposizione falsa; "$x > 2$" invece non è né vera né falsa finché non si sa quanto vale $x$ (si chiama *predicato*, o proposizione aperta).

Le proposizioni si combinano con i *connettivi logici*, che hanno un simbolo ciascuno:

- $\neg P$ (non $P$): la *negazione*, vera quando $P$ è falsa;
- $P \wedge Q$ ($P$ e $Q$): la *congiunzione*, vera solo quando sono vere entrambe;
- $P \vee Q$ ($P$ o $Q$): la *disgiunzione*, vera quando è vera almeno una delle due (non è un "o" esclusivo: possono essere vere tutte e due);
- $P \Rightarrow Q$ (se $P$ allora $Q$, oppure "$P$ implica $Q$"): l'*implicazione*;
- $P \iff Q$ ($P$ se e solo se $Q$): la *doppia implicazione*, o equivalenza: $P$ e $Q$ sono vere o false insieme.

I connettivi sono legati alle operazioni tra insiemi che si vedranno tra poco: la "e" corrisponde all'intersezione, la "o" all'unione. Per questo $\wedge$ e $\cap$ si somigliano anche nel disegno, e alla lavagna capita di usarli quasi come sinonimi (negli appunti dell'esercizio sugli intervalli l'intersezione è scritta con $\wedge$).

> [!example] Esempio: leggere un'implicazione
> "Se $A \subseteq B$, allora $A \cap B = A$" si scrive $A \subseteq B \Rightarrow A \cap B = A$: è una delle proprietà dell'intersezione che il professore ha scritto alla lavagna.
>
> Attenzione al verso: $x = 2 \Rightarrow x^2 = 4$ è vera, ma $x^2 = 4 \Rightarrow x = 2$ è falsa (potrebbe essere $x = -2$). Invece $x^2 = 4 \iff x = 2 \vee x = -2$ è vera in tutti e due i versi.

### I quantificatori $\forall$ ed $\exists$

Un predicato come "$x^2 \geq 0$" diventa una proposizione vera o falsa quando si dice per quali $x$ vale. Per farlo si usano i *quantificatori*:

- $\forall$ si legge "per ogni" (è una A rovesciata, da *all*): $\forall x \in \mathbb{R},\ x^2 \geq 0$ vuol dire "ogni numero reale ha quadrato maggiore o uguale a zero", ed è vera;
- $\exists$ si legge "esiste" (una E rovesciata): $\exists x \in \mathbb{R} \mid x^2 = 2$ vuol dire "esiste almeno un numero reale il cui quadrato è $2$", ed è vera ($x = \sqrt{2}$);
- $\exists !$ si legge "esiste un unico": $\exists !\, x \in \mathbb{R} \mid 2x + 1 = 7$ è vera, perché l'unica soluzione è $x = 3$.

Il simbolo $\mid$ (oppure i due punti, oppure "t.c." o "t/c") si legge "tale che".

> [!abstract] Simboli da riconoscere
> $\forall$ per ogni · $\exists$ esiste · $\exists!$ esiste un unico · $\mid$ oppure t/c tale che · $\in$ appartiene · $\notin$ non appartiene · $\Rightarrow$ implica · $\iff$ se e solo se · $\wedge$ e · $\vee$ o · $\neg$ non

Il professore ha usato il quantificatore "esiste" per la condizione di parallelismo tra vettori, che si trova in [[05-i-vettori]]:

$$
\vec v \parallel \vec w \iff \exists\, \lambda \in \mathbb{R}^* \text{ t/c } \vec v = \lambda \vec w
$$

Si legge: "$\vec v$ è parallelo a $\vec w$ se e solo se esiste un numero reale $\lambda$, diverso da zero, tale che $\vec v = \lambda \vec w$". Il simbolo $\mathbb{R}^*$ (i reali senza lo zero) è spiegato più avanti.

### Come si nega una frase con i quantificatori

Negare una frase con "per ogni" non vuol dire dire "per nessuno": basta un solo caso in cui non vale. Per questo, negando, i quantificatori si scambiano.

> [!abstract] Negazione dei quantificatori
> $$
> \neg\,(\forall x,\ P(x)) \iff \exists x \mid \neg P(x) \qquad\qquad \neg\,(\exists x \mid P(x)) \iff \forall x,\ \neg P(x)
> $$

> [!example] Esempio: il controesempio
> "Tutti i numeri reali sono positivi" ($\forall x \in \mathbb{R},\ x > 0$) è falsa. La sua negazione è "esiste un numero reale non positivo" ($\exists x \in \mathbb{R} \mid x \leq 0$), e basta mostrarne uno: $x = -1$. Un caso così si chiama *controesempio*.

## GLI INSIEMI

### Elementi e appartenenza

Un *insieme* è una collezione di oggetti, detti *elementi*, per la quale è sempre chiaro se un oggetto ne fa parte o no. "I numeri pari" è un insieme; "i numeri grandi" no, perché non si sa dove finisca "grande".

Gli insiemi si indicano di solito con lettere maiuscole ($A$, $B$, $C$) e gli elementi con lettere minuscole. Per dire che un elemento sta o non sta in un insieme si usano due simboli:

- $a \in A$ si legge "$a$ appartiene ad $A$";
- $a \notin A$ si legge "$a$ non appartiene ad $A$".

Alla lavagna il professore ha accompagnato ogni simbolo con un disegno: l'insieme è una linea chiusa, gli elementi sono punti dentro o fuori. Questi disegni si chiamano *diagrammi di Eulero-Venn*.

![[01-appartenenza-inclusione.svg|560]]

### Come si descrive un insieme

Un insieme si può descrivere in due modi.

1. Per *elencazione*: si scrivono tutti gli elementi tra parentesi graffe. Per esempio $A = \{1, 2, 3, 4\}$. L'ordine non conta e ogni elemento si scrive una volta sola.
2. Con una *proprietà caratteristica*: si scrive la proprietà che hanno tutti e soli gli elementi dell'insieme. È il modo che il professore usa di più:
$$
\{x \in \mathbb{R} \mid x < 3\}
$$
si legge "l'insieme degli $x$ appartenenti a $\mathbb{R}$ tali che $x$ è minore di $3$". Prima della sbarra c'è da dove si prendono gli elementi (qui i numeri reali), dopo la sbarra la condizione che devono rispettare.

Il secondo modo è indispensabile quando gli elementi sono infiniti e non si possono elencare, come i numeri reali minori di $3$.

L'insieme che non ha nessun elemento si chiama *insieme vuoto* e si indica con $\emptyset$. Per esempio $\{x \in \mathbb{R} \mid x^2 = -1\} = \emptyset$, perché nessun numero reale ha quadrato negativo.

> [!example] Esempio: dalle parole ai simboli
> - "I numeri naturali minori di $5$": per elencazione $\{0, 1, 2, 3, 4\}$, con la proprietà $\{n \in \mathbb{N} \mid n < 5\}$.
> - "I numeri reali compresi tra $1$ e $2$, estremi inclusi": $\{x \in \mathbb{R} \mid 1 \leq x \leq 2\}$. Qui l'elencazione è impossibile.
> - "Le soluzioni di $x^2 - 5x + 6 = 0$": $\{x \in \mathbb{R} \mid x^2 - 5x + 6 = 0\} = \{2, 3\}$.

### Sottoinsiemi e uguaglianza

Un insieme $B$ è *sottoinsieme* di $A$, e si scrive $B \subseteq A$ ("$B$ è contenuto in $A$"), quando ogni elemento di $B$ è anche elemento di $A$. Nel diagramma, $B$ è disegnato tutto dentro $A$.

Con i quantificatori:

$$
B \subseteq A \iff \forall x\, (x \in B \Rightarrow x \in A)
$$

Due insiemi sono *uguali* quando hanno esattamente gli stessi elementi, cioè quando ciascuno è contenuto nell'altro: $A = B \iff A \subseteq B \wedge B \subseteq A$.

Se $B \subseteq A$ ma $B \neq A$ (in $A$ c'è almeno un elemento che non sta in $B$) si dice che $B$ è un sottoinsieme *proprio* e si scrive $B \subset A$. L'insieme vuoto è sottoinsieme di qualunque insieme.

### Le operazioni tra insiemi

Come con i numeri si fanno somme e prodotti, con gli insiemi si fanno operazioni che producono nuovi insiemi. Il professore le ha disegnate una per una con i diagrammi di Venn, colorando la parte che si ottiene.

> [!abstract] Operazioni tra insiemi
> - *Unione*: $A \cup B = \{x \mid x \in A \vee x \in B\}$, gli elementi che stanno in almeno uno dei due.
> - *Intersezione*: $A \cap B = \{x \mid x \in A \wedge x \in B\}$, gli elementi che stanno in tutti e due.
> - *Differenza*: $A \setminus B = \{x \mid x \in A \wedge x \notin B\}$, gli elementi di $A$ che non stanno in $B$ (alla lavagna è stata chiamata "sottrazione").
> - *Complementare*: fissato un insieme "ambiente" $U$ che contiene tutto (l'*universo*, spesso $\mathbb{R}$), il complementare di $A$ è $A^c = U \setminus A$, cioè tutto ciò che non sta in $A$.

![[01-operazioni-venn.svg|680]]

Due insiemi che non hanno elementi in comune, cioè con $A \cap B = \emptyset$, si dicono *disgiunti*.

La differenza non è simmetrica: $A \setminus B$ e $B \setminus A$ sono in genere insiemi diversi, come $5 - 3$ e $3 - 5$ sono numeri diversi. Negli appunti la differenza è scritta $B \setminus A$: si toglie da $B$ ciò che sta in $A$.

> [!example] Esempio svolto: le quattro operazioni
> Siano $A = \{1, 2, 3, 4\}$ e $B = \{3, 4, 5\}$, nell'universo $U = \{1, 2, 3, 4, 5, 6\}$.
>
> 1. Unione: metto insieme tutti gli elementi, senza ripetere: $A \cup B = \{1, 2, 3, 4, 5\}$.
> 2. Intersezione: tengo solo quelli comuni: $A \cap B = \{3, 4\}$.
> 3. Differenze: $A \setminus B = \{1, 2\}$ (tolgo da $A$ il $3$ e il $4$); $B \setminus A = \{5\}$.
> 4. Complementare: $A^c = U \setminus A = \{5, 6\}$.

### Le proprietà delle operazioni

Le operazioni tra insiemi hanno proprietà simili a quelle di somma e prodotto. Il professore le ha scritte così, prima per l'intersezione e poi per l'unione.

> [!abstract] Proprietà dell'intersezione (come alla lavagna)
> - $A \cap \emptyset = \emptyset$
> - $A \cap B = B \cap A$ (commutativa)
> - $(A \cap B) \cap C = (A \cap C) \cap B$ (associativa)
> - se $A \subseteq B \Rightarrow A \cap B = A$

> [!abstract] Proprietà dell'unione (come alla lavagna)
> - $A \cup \emptyset = A$
> - $A \cup B = B \cup A$ (commutativa)
> - $(A \cup B) \cup C = (A \cup C) \cup B$ (associativa)
> - se $A \subseteq B \Rightarrow A \cup B = B$

Ognuna si capisce guardando la definizione o un diagramma.

- Con l'insieme vuoto: nessun elemento sta in $\emptyset$, quindi nessun elemento sta "in $A$ e in $\emptyset$" (l'intersezione è vuota), mentre "in $A$ o in $\emptyset$" vuol dire semplicemente "in $A$" (l'unione è $A$).
- Commutativa: "stare in $A$ e in $B$" è lo stesso che "stare in $B$ e in $A$"; l'ordine non conta.
- Associativa: quando si intersecano (o si uniscono) tre insiemi, non importa in che ordine si fanno le operazioni a due a due. Il risultato è sempre l'insieme degli elementi comuni a tutti e tre (o che stanno in almeno uno dei tre). Per questo si può scrivere anche $(A \cap B) \cap C = A \cap (B \cap C)$, e alla fine semplicemente $A \cap B \cap C$, senza parentesi.
- Con l'inclusione: se $A$ sta tutto dentro $B$, gli elementi comuni ad $A$ e $B$ sono tutti quelli di $A$, quindi $A \cap B = A$; e mettendo insieme $A$ e $B$ non si aggiunge nulla a $B$, quindi $A \cup B = B$.

> [!example] Esempio: verificare le proprietà con l'inclusione
> $A = \{1, 2\}$, $B = \{1, 2, 3, 4\}$: $A \subseteq B$.
>
> $A \cap B = \{1, 2\} = A$ e $A \cup B = \{1, 2, 3, 4\} = B$, come dicono le proprietà.

Unione e intersezione insieme hanno altre due proprietà utili (complemento alla lezione): la *distributiva*, $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$, e le *leggi di De Morgan*, $(A \cup B)^c = A^c \cap B^c$ e $(A \cap B)^c = A^c \cup B^c$. Le leggi di De Morgan sono la versione per insiemi della negazione: "non (in $A$ o in $B$)" vuol dire "non in $A$ e non in $B$".

## GLI INSIEMI NUMERICI

### Naturali, interi, razionali, reali

I numeri che si usano nel corso formano quattro insiemi, ognuno contenuto nel successivo. Ogni nuovo insieme nasce perché nel precedente un'operazione non si può sempre fare.

1. I *numeri naturali* $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ servono a contare. Somma e prodotto di due naturali sono ancora naturali, ma la sottrazione no: $3 - 5$ non è un naturale.
2. Gli *interi* $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$ aggiungono i negativi, e così la sottrazione si può fare sempre. La divisione invece no: $1 : 2$ non è un intero.
3. I *razionali* $\mathbb{Q}$ sono le frazioni $\dfrac{p}{q}$ con $p, q$ interi e $q \neq 0$. Con loro si può sempre dividere (tranne che per zero). In forma decimale un razionale ha un numero finito di cifre ($\frac{3}{4} = 0{,}75$) oppure cifre che si ripetono all'infinito, un *periodo* ($\frac{1}{3} = 0{,}333\ldots$).
4. I *reali* $\mathbb{R}$ comprendono i razionali e gli *irrazionali*, i numeri che non si possono scrivere come frazione: $\sqrt{2}$, $\sqrt{3}$, $\pi$. In forma decimale hanno infinite cifre senza periodo.

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}
$$

![[01-insiemi-numerici.svg|560]]

Il programma parla anche di "assiomi dei numeri reali": sono le regole di base da cui si parte senza dimostrarle. In parole semplici dicono che in $\mathbb{R}$ valgono le solite regole di somma e prodotto (commutativa, associativa, distributiva, esistenza dello zero, dell'uno, dell'opposto e dell'inverso dei numeri non nulli), che i numeri sono ordinati (dati due numeri diversi, uno è più piccolo dell'altro) e che la retta reale non ha "buchi" (*completezza*). È quest'ultima proprietà a distinguere $\mathbb{R}$ da $\mathbb{Q}$: in $\mathbb{Q}$ manca, per esempio, il numero il cui quadrato è $2$.

### Le notazioni $\mathbb{R}^*$, $\mathbb{R}^+$ e simili

Per indicare in fretta alcuni sottoinsiemi si aggiunge un simbolo alla lettera.

- L'asterisco toglie lo zero: $\mathbb{R}^* = \mathbb{R} \setminus \{0\}$ sono i reali diversi da zero (è quello che compare nella condizione di parallelismo dei vettori). Allo stesso modo $\mathbb{Z}^*$, $\mathbb{N}^*$, $\mathbb{Q}^*$.
- Il segno più tiene solo i positivi: $\mathbb{R}^+ = \{x \in \mathbb{R} \mid x > 0\}$, e $\mathbb{R}^-$ i negativi. Alcuni libri includono lo zero in $\mathbb{R}^+$: nel dubbio conviene scrivere la condizione per esteso.

Perché in $\vec v = \lambda \vec w$ si chiede $\lambda \in \mathbb{R}^*$ e non semplicemente $\lambda \in \mathbb{R}$? Perché con $\lambda = 0$ si otterrebbe $\vec v = \vec 0$, il vettore nullo, che non ha una direzione: escludendo lo zero si parla solo di vettori veri e propri.

### La retta reale

I numeri reali si rappresentano su una retta: si fissano un punto per lo $0$, un verso (di solito verso destra) e un'unità di misura. Allora a ogni numero reale corrisponde un punto, e a ogni punto un numero reale. I numeri più grandi stanno a destra.

![[01-retta-reale.svg|620]]

Sulla retta i razionali sono "dappertutto": tra due numeri reali qualsiasi, per quanto vicini, c'è sempre un razionale (e anzi infiniti). Questa è la *densità di $\mathbb{Q}$ in $\mathbb{R}$*, citata nel programma. Eppure i razionali da soli non riempiono la retta: restano i punti irrazionali, come $\sqrt{2}$.

> [!example] Esempio: un razionale tra due numeri
> Tra $\frac{1}{3}$ e $\frac{1}{2}$ c'è la loro media, $\dfrac{\frac{1}{3} + \frac{1}{2}}{2} = \dfrac{5}{12}$, che è ancora una frazione. Ripetendo il procedimento se ne trovano quante se ne vogliono.

Per collocare un irrazionale sulla retta, come ha fatto il professore nell'esercizio sugli intervalli, se ne usa un valore approssimato: $\sqrt{2} \approx 1{,}41$, $\pi \approx 3{,}14$, $\sqrt{17} \approx 4{,}12$. Il valore approssimato serve solo a disegnare; nelle risposte si scrive il numero esatto.

### L'irrazionalità di $\sqrt{2}$

Che $\sqrt{2}$ non sia una frazione non si vede dalle cifre decimali (sono infinite, non si possono controllare tutte): si dimostra. La dimostrazione è *per assurdo*: si suppone il contrario e si arriva a una contraddizione.

> [!abstract] Teorema
> $\sqrt{2}$ non è un numero razionale: non esistono due interi $p$ e $q$ tali che $\dfrac{p}{q} = \sqrt{2}$.

La dimostrazione usa un fatto semplice sui numeri pari: se il quadrato di un intero è pari, l'intero stesso è pari. Infatti il quadrato di un dispari è dispari: $(2k + 1)^2 = 4k^2 + 4k + 1$, che è un pari più uno.

> [!example] Dimostrazione passo passo
> 1. Supponiamo per assurdo che $\sqrt{2} = \dfrac{p}{q}$, con $p$ e $q$ interi, $q \neq 0$, e con la frazione già ridotta ai minimi termini (cioè $p$ e $q$ non hanno divisori comuni, in particolare non sono tutti e due pari).
> 2. Elevo al quadrato: $2 = \dfrac{p^2}{q^2}$, cioè $p^2 = 2q^2$.
> 3. Quindi $p^2$ è pari (è il doppio di qualcosa), e per il fatto appena visto anche $p$ è pari: $p = 2k$ per qualche intero $k$.
> 4. Sostituisco: $(2k)^2 = 2q^2$, cioè $4k^2 = 2q^2$, cioè $q^2 = 2k^2$.
> 5. Allora anche $q^2$ è pari, e quindi $q$ è pari.
> 6. Ma $p$ e $q$ pari tutti e due contraddicono il punto 1, dove la frazione era ridotta ai minimi termini.
>
> L'ipotesi di partenza porta a una contraddizione, quindi è falsa: $\sqrt{2}$ è irrazionale.

Il ragionamento ha anche un significato geometrico, noto già ai Greci: la diagonale di un quadrato di lato $1$ è lunga $\sqrt{2}$ (per il teorema di Pitagora, $\sqrt{1^2 + 1^2}$), quindi lato e diagonale di un quadrato non hanno una misura comune, per quanto piccola la si scelga.

### Il valore assoluto

Il *valore assoluto* (o *modulo*) di un numero reale è il numero senza il suo segno.

> [!abstract] Definizione di valore assoluto
> $$
> |x| = \begin{cases} x & \text{se } x \geq 0 \\ -x & \text{se } x < 0 \end{cases}
> $$
> Per esempio $|5| = 5$, $|-5| = 5$, $|0| = 0$.

Il segno meno nella seconda riga spaventa, ma serve proprio a togliere il segno: se $x$ è negativo, $-x$ è positivo. Per esempio $|-3| = -(-3) = 3$.

Geometricamente $|x|$ è la distanza del punto $x$ dallo $0$ sulla retta reale, e $|a - b|$ è la distanza tra i punti $a$ e $b$. Una distanza non è mai negativa, e infatti $|x| \geq 0$ sempre.

![[01-valore-assoluto-insiemi.svg|620]]

> [!abstract] Proprietà del valore assoluto
> - $|x| \geq 0$, e $|x| = 0 \iff x = 0$
> - $|-x| = |x|$
> - $|x \cdot y| = |x| \cdot |y|$
> - $|x + y| \leq |x| + |y|$ (*disuguaglianza triangolare*)
> - con $r > 0$: $|x| < r \iff -r < x < r$ e $|x| > r \iff x < -r \vee x > r$
> - $\sqrt{x^2} = |x|$

La disuguaglianza triangolare si chiama così perché, nel piano, dice che un lato di un triangolo non è mai più lungo della somma degli altri due. Sulla retta dice che, sommando un positivo e un negativo, una parte si cancella e il risultato è più vicino allo zero.

L'ultima proprietà evita un errore frequente: $\sqrt{(-3)^2} = \sqrt{9} = 3$, non $-3$.

> [!example] Esempio: valore assoluto e distanze
> - $|2 - 7| = |-5| = 5$: i punti $2$ e $7$ distano $5$.
> - $\{x \in \mathbb{R} \mid |x| < 2\}$ sono i punti a distanza minore di $2$ dallo zero: $-2 < x < 2$.
> - $\{x \in \mathbb{R} \mid |x - 1| \leq 3\}$ sono i punti a distanza al massimo $3$ da $1$: $-2 \leq x \leq 4$.
>
> Le equazioni e disequazioni con il valore assoluto sono svolte in [[02-equazioni-e-disequazioni]]; la distanza nel piano, che generalizza $|a - b|$, è in [[03-retta-e-circonferenza]].

## GLI INTERVALLI

### Intervalli e loro notazione

Gli insiemi di numeri reali che si incontrano più spesso sono i "pezzi di retta" senza buchi, gli *intervalli*. Dati due numeri $a < b$ (gli *estremi*), ci sono quattro intervalli limitati, a seconda che gli estremi siano compresi o no, e altri illimitati, che proseguono all'infinito da una parte.

La notazione segue una regola sola:

- la parentesi quadra $[\;]$ vuol dire che l'estremo è compreso (intervallo *chiuso* da quella parte);
- la parentesi tonda $(\;)$ vuol dire che l'estremo è escluso (intervallo *aperto* da quella parte);
- $+\infty$ e $-\infty$ vogliono sempre la tonda, perché non sono numeri e non possono essere "compresi".

![[01-intervalli.svg|680]]

> [!abstract] Intervalli
> - $[a, b] = \{x \in \mathbb{R} \mid a \leq x \leq b\}$ chiuso
> - $(a, b) = \{x \in \mathbb{R} \mid a < x < b\}$ aperto
> - $[a, b) = \{x \in \mathbb{R} \mid a \leq x < b\}$ e $(a, b] = \{x \in \mathbb{R} \mid a < x \leq b\}$
> - $[a, +\infty) = \{x \in \mathbb{R} \mid x \geq a\}$, $(a, +\infty) = \{x \in \mathbb{R} \mid x > a\}$
> - $(-\infty, b] = \{x \in \mathbb{R} \mid x \leq b\}$, $(-\infty, b) = \{x \in \mathbb{R} \mid x < b\}$
> - $(-\infty, +\infty) = \mathbb{R}$

Sulla retta, come nel disegno, l'estremo compreso si segna con un pallino pieno, quello escluso con un pallino vuoto, e l'infinito con una freccia.

In alcuni libri l'estremo escluso si indica con la quadra rovesciata: $]a, b[$ invece di $(a, b)$. Il significato è lo stesso.

> [!warning] Errore tipico
> Scrivere $[3, +\infty]$: l'infinito non è un numero, quindi la parentesi verso l'infinito è sempre tonda, $[3, +\infty)$. Un altro errore è invertire gli estremi: un intervallo si scrive sempre con il numero più piccolo a sinistra, $(-2, 5)$ e non $(5, -2)$.

### Unione e intersezione di intervalli

Gli intervalli sono insiemi, quindi si possono unire e intersecare. Il modo più sicuro è disegnarli uno sotto l'altro sulla stessa retta.

- L'*intersezione* è la parte in cui le righe si sovrappongono tutte: si trova in verticale, cercando i tratti dove ci sono tutti i colori. Corrisponde alla "e", ed è quello che si fa nei sistemi di disequazioni.
- L'*unione* è la parte coperta da almeno una riga. Corrisponde alla "o", ed è quello che si scrive quando una disequazione ha soluzioni in due pezzi separati, come $(-\infty, 2] \cup [3, +\infty)$.

> [!example] Esempio: unione e intersezione
> Siano $I = [-1, 3)$ e $J = (1, 5]$.
>
> 1. Gli elementi comuni sono quelli maggiori di $1$ (per stare in $J$) e minori di $3$ (per stare in $I$): $I \cap J = (1, 3)$. In $1$ la parentesi è tonda perché $1 \notin J$; in $3$ è tonda perché $3 \notin I$.
> 2. Insieme coprono tutto da $-1$ a $5$ senza buchi: $I \cup J = [-1, 5]$.
> 3. La differenza: $I \setminus J$ sono gli elementi di $I$ che non stanno in $J$, cioè $[-1, 1]$ (l'$1$ resta, perché non sta in $J$).

### L'esercizio del professore

Alla fine della prima lezione il professore ha proposto un esercizio che mette insieme tutto: insiemi descritti con una proprietà, numeri irrazionali da collocare sulla retta, intervalli e intersezione.

> [!example] Esercizio svolto: intersezione di tre insiemi
> Dati
> $$
> X = \{x \in \mathbb{R} \mid x \geq -\sqrt{2}\} \qquad Y = \{x \in \mathbb{R} \mid x < \tfrac{7}{2}\} \qquad Z = \{x \in \mathbb{R} \mid \pi \leq x < \sqrt{17}\}
> $$
> trovare $X \cap Y \cap Z$.
>
> 1. Riscrivo ogni insieme come intervallo: $X = [-\sqrt{2}, +\infty)$, $Y = (-\infty, \tfrac{7}{2})$, $Z = [\pi, \sqrt{17})$.
> 2. Per disegnarli uso i valori approssimati: $-\sqrt{2} \approx -1{,}41$; $\pi \approx 3{,}14$; $\tfrac{7}{2} = 3{,}5$; $\sqrt{17} \approx 4{,}12$ (infatti $4^2 = 16$ e $\sqrt{17}$ è appena più di $4$).
> 3. Disegno i tre intervalli uno sotto l'altro e cerco il tratto comune a tutti e tre.
> 4. A sinistra il limite più restrittivo è $\pi$ (sta a destra di $-\sqrt{2}$), ed è compreso sia in $X$ sia in $Z$: pallino pieno.
> 5. A destra il limite più restrittivo è $\tfrac{7}{2}$ (sta a sinistra di $\sqrt{17}$), ed è escluso perché in $Y$ c'è il minore stretto: pallino vuoto.
>
> Risultato:
> $$
> X \cap Y \cap Z = \{x \in \mathbb{R} \mid \pi \leq x < \tfrac{7}{2}\} = [\pi, \tfrac{7}{2})
> $$

![[01-esercizio-intervalli.svg|640]]

Il metodo vale per ogni intersezione di intervalli: a sinistra vince l'estremo sinistro più grande, a destra l'estremo destro più piccolo; per decidere se un estremo è compreso si guarda l'insieme da cui viene. Se l'estremo sinistro risultasse più grande di quello destro, le righe non si sovrapporrebbero e l'intersezione sarebbe vuota.

> [!warning] Errore tipico
> Confrontare gli irrazionali "a occhio". Per sapere se $\sqrt{17}$ sta prima o dopo $\tfrac{7}{2}$ conviene confrontare i quadrati, che sono numeri semplici: $(\sqrt{17})^2 = 17$ e $(\tfrac{7}{2})^2 = \tfrac{49}{4} = 12{,}25$. Poiché $17 > 12{,}25$ (e sono numeri positivi), $\sqrt{17} > \tfrac{7}{2}$.

## ESERCIZI

Questa sezione serve per allenarsi in vista dell'esonero. Conviene fare ogni esercizio da sola, su carta, disegnando la retta quando ci sono intervalli; solo dopo si apre la soluzione (il riquadro verde si apre con un clic) e si confrontano i passaggi, non solo il risultato.

### Gli esercizi del professore

Per questo argomento il professore non ha dato un foglio di esercizi: i fogli in `materiale/` riguardano i vettori ([[Esercizi_vettori.pdf]] ed [[esercizi prodotto vettoriale e prodotto triplo.pdf]]) e le funzioni, gli esponenziali, i logaritmi e la trigonometria ([[Esercizi_funzioni_e_Logaritmi.pdf]]).

L'unico esercizio dato dal professore su insiemi e intervalli è quello della prima lezione, negli appunti di Nadia ([[appunti-nadia-02.jpeg]]): l'intersezione $X \cap Y \cap Z$ con $-\sqrt{2}$, $\tfrac{7}{2}$, $\pi$ e $\sqrt{17}$. È già svolto in questa pagina, nella sezione [[#L'esercizio del professore]].

La notazione degli intervalli torna però nel foglio [[Esercizi_funzioni_e_Logaritmi.pdf]], pagina 1: negli esercizi 1 e 2 (il dominio e l'immagine si scrivono come intervalli), nell'esercizio 10 (gli intervalli di monotonia, anche di $|x - 3|$) e nell'esercizio 11 (il grafico di $|x + 1| - 2$). Sono esercizi sulle funzioni e si trovano in [[06-le-funzioni]]; per farli bene servono gli esercizi qui sotto sugli intervalli e sul valore assoluto.

### Esercizi per allenarti

#### Insiemi e operazioni

> [!question] Esercizio 1
> Nell'universo $U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ sono dati $A = \{1, 2, 3, 4, 5, 6\}$ e $B = \{2, 4, 6, 8\}$. Calcolare $A \cup B$, $A \cap B$, $A \setminus B$, $B \setminus A$ e il complementare $B^c$.

> [!success]- Soluzione
> Risultato: $A \cup B = \{1, 2, 3, 4, 5, 6, 8\}$; $A \cap B = \{2, 4, 6\}$; $A \setminus B = \{1, 3, 5\}$; $B \setminus A = \{8\}$; $B^c = \{1, 3, 5, 7, 9, 10\}$.
>
> Come si arriva:
> 1. Unione: prendo tutti gli elementi di $A$ e aggiungo quelli di $B$ che mancano (solo l'$8$): $A \cup B = \{1, 2, 3, 4, 5, 6, 8\}$.
> 2. Intersezione: tengo solo gli elementi che stanno in tutti e due: $A \cap B = \{2, 4, 6\}$.
> 3. $A \setminus B$: tolgo da $A$ gli elementi che stanno anche in $B$ ($2, 4, 6$): $A \setminus B = \{1, 3, 5\}$.
> 4. $B \setminus A$: tolgo da $B$ gli elementi che stanno in $A$: resta $B \setminus A = \{8\}$. Le due differenze sono diverse.
> 5. Complementare: prendo gli elementi di $U$ che non stanno in $B$: $B^c = \{1, 3, 5, 7, 9, 10\}$.

> [!question] Esercizio 2
> Con gli insiemi $A$ e $B$ dell'esercizio 1 e $C = \{1, 4, 9\}$, calcolare $(A \cap B) \cup C$, $A \cap (B \cup C)$ e $(A \cap B) \cup (A \cap C)$. Quali due risultati coincidono, e perché?

> [!success]- Soluzione
> Risultato: $(A \cap B) \cup C = \{1, 2, 4, 6, 9\}$; $A \cap (B \cup C) = \{1, 2, 4, 6\}$; $(A \cap B) \cup (A \cap C) = \{1, 2, 4, 6\}$. Coincidono il secondo e il terzo, per la proprietà distributiva.
>
> Come si arriva:
> 1. Primo insieme: calcolo prima la parentesi, $A \cap B = \{2, 4, 6\}$, poi unisco $C$: $(A \cap B) \cup C = \{2, 4, 6\} \cup \{1, 4, 9\} = \{1, 2, 4, 6, 9\}$.
> 2. Secondo insieme: calcolo prima la parentesi, $B \cup C = \{1, 2, 4, 6, 8, 9\}$, poi interseco con $A$: $A \cap (B \cup C) = \{1, 2, 4, 6\}$ (l'$8$ e il $9$ non stanno in $A$).
> 3. Terzo insieme: $A \cap C = \{1, 4\}$, quindi $(A \cap B) \cup (A \cap C) = \{2, 4, 6\} \cup \{1, 4\} = \{1, 2, 4, 6\}$.
> 4. Confronto: il secondo e il terzo coincidono perché vale la proprietà distributiva $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$. Il primo è diverso: le parentesi contano, perché unione e intersezione insieme non si possono spostare a piacere.

> [!question] Esercizio 3
> Nell'universo $U = \{1, 2, 3, 4, 5, 6, 7, 8\}$ sono dati $A = \{1, 2, 3, 4\}$ e $B = \{3, 4, 5, 6\}$. Verificare le due leggi di De Morgan calcolando separatamente i due membri di $(A \cup B)^c = A^c \cap B^c$ e di $(A \cap B)^c = A^c \cup B^c$.

> [!success]- Soluzione
> Risultato: tutte e due le leggi sono verificate: $(A \cup B)^c = A^c \cap B^c = \{7, 8\}$ e $(A \cap B)^c = A^c \cup B^c = \{1, 2, 5, 6, 7, 8\}$.
>
> Come si arriva:
> 1. Primo membro della prima legge: $A \cup B = \{1, 2, 3, 4, 5, 6\}$, quindi $(A \cup B)^c = \{7, 8\}$.
> 2. Secondo membro della prima legge: $A^c = \{5, 6, 7, 8\}$ e $B^c = \{1, 2, 7, 8\}$, quindi $A^c \cap B^c = \{7, 8\}$. I due membri sono uguali: la prima legge è verificata.
> 3. Primo membro della seconda legge: $A \cap B = \{3, 4\}$, quindi $(A \cap B)^c = \{1, 2, 5, 6, 7, 8\}$.
> 4. Secondo membro della seconda legge: $A^c \cup B^c = \{5, 6, 7, 8\} \cup \{1, 2, 7, 8\} = \{1, 2, 5, 6, 7, 8\}$. Anche la seconda è verificata.

> [!question] Esercizio 4
> Scrivere per elencazione i seguenti insiemi:
> $$
> A = \{n \in \mathbb{N} \mid n^2 < 20\} \qquad B = \{x \in \mathbb{Z} \mid -2 \leq x < 3\} \qquad C = \{x \in \mathbb{R} \mid x^2 - 4x + 3 = 0\} \qquad D = \{x \in \mathbb{R} \mid x^2 + 4 = 0\}
> $$

> [!success]- Soluzione
> Risultato: $A = \{0, 1, 2, 3, 4\}$; $B = \{-2, -1, 0, 1, 2\}$; $C = \{1, 3\}$; $D = \emptyset$.
>
> Come si arriva:
> 1. $A$: provo i naturali a partire da $0$ e ne calcolo il quadrato: $0, 1, 4, 9, 16$ sono minori di $20$, $5^2 = 25$ no. Quindi $A = \{0, 1, 2, 3, 4\}$.
> 2. $B$: prendo gli interi da $-2$ compreso a $3$ escluso: $B = \{-2, -1, 0, 1, 2\}$.
> 3. $C$: risolvo l'equazione. Due numeri con somma $4$ e prodotto $3$ sono $1$ e $3$, quindi $x^2 - 4x + 3 = (x - 1)(x - 3)$ e $C = \{1, 3\}$.
> 4. $D$: l'equazione diventa $x^2 = -4$, che non ha soluzioni reali, perché un quadrato non è mai negativo. Quindi $D = \emptyset$.

#### Quantificatori

> [!question] Esercizio 5
> Dire se ciascuna proposizione è vera o falsa, motivando:
> 1. $\forall x \in \mathbb{R},\ x^2 > 0$
> 2. $\exists x \in \mathbb{N} \mid x + 5 = 2$
> 3. $\forall x \in \mathbb{R},\ |x| \geq x$
> 4. $\exists!\, x \in \mathbb{R} \mid x^2 = 9$

> [!success]- Soluzione
> Risultato: 1. falsa; 2. falsa; 3. vera; 4. falsa.
>
> Come si arriva:
> 1. Falsa. Basta un controesempio: per $x = 0$ si ha $x^2 = 0$, che non è maggiore di $0$. (Con $\geq$ al posto di $>$ sarebbe vera.)
> 2. Falsa. L'unica soluzione di $x + 5 = 2$ è $x = -3$, che non è un numero naturale. In $\mathbb{Z}$ invece sarebbe vera.
> 3. Vera. Si guardano i due casi: se $x \geq 0$ allora $|x| = x$; se $x < 0$ allora $|x|$ è positivo e quindi maggiore di $x$, che è negativo.
> 4. Falsa. Le soluzioni esistono, ma non sono una sola: $x = 3$ e $x = -3$.

> [!question] Esercizio 6
> Scrivere la negazione di ciascuna proposizione, e dire quale tra la proposizione e la sua negazione è vera:
> 1. $\forall n \in \mathbb{N},\ n \geq 1$
> 2. $\exists x \in \mathbb{R} \mid x^2 = -4$
> 3. $\forall x \in \mathbb{R},\ x > 2 \Rightarrow x^2 > 4$

> [!success]- Soluzione
> Risultato:
> 1. negazione $\exists n \in \mathbb{N} \mid n < 1$: è vera la negazione;
> 2. negazione $\forall x \in \mathbb{R},\ x^2 \neq -4$: è vera la negazione;
> 3. negazione $\exists x \in \mathbb{R} \mid x > 2 \wedge x^2 \leq 4$: è vera la proposizione di partenza.
>
> Come si arriva (negando, $\forall$ diventa $\exists$ e viceversa, e la condizione si nega):
> 1. "Per ogni $n$, $n \geq 1$" si nega con "esiste un $n$ con $n < 1$". È vera la negazione: $n = 0$ è un naturale minore di $1$.
> 2. "Esiste $x$ con $x^2 = -4$" si nega con "per ogni $x$, $x^2 \neq -4$". È vera la negazione: nessun quadrato è negativo.
> 3. La negazione di "se $P$ allora $Q$" è "$P$ e non $Q$", quindi si ottiene $\exists x \in \mathbb{R} \mid x > 2 \wedge x^2 \leq 4$. È vera la proposizione di partenza: se $x > 2$, moltiplicando $x > 2$ per $x$ (positivo) si ha $x^2 > 2x > 4$.

#### Insiemi numerici

> [!question] Esercizio 7
> Per ciascun numero dire qual è il più piccolo tra gli insiemi $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ a cui appartiene, poi metterli in ordine crescente:
> $$
> 7 \qquad -4 \qquad \tfrac{3}{4} \qquad 0{,}333\ldots \qquad \sqrt{9} \qquad \sqrt{5} \qquad \pi
> $$

> [!success]- Soluzione
> Risultato: $7 \in \mathbb{N}$, $\sqrt{9} = 3 \in \mathbb{N}$, $-4 \in \mathbb{Z}$, $\tfrac{3}{4} \in \mathbb{Q}$, $0{,}333\ldots = \tfrac{1}{3} \in \mathbb{Q}$, $\sqrt{5}$ e $\pi$ solo in $\mathbb{R}$. In ordine crescente: $-4 < 0{,}333\ldots < \tfrac{3}{4} < \sqrt{5} < \sqrt{9} < \pi < 7$.
>
> Come si arriva:
> 1. Naturali e interi: $7 \in \mathbb{N}$; $-4 \in \mathbb{Z}$ (è negativo, quindi non è naturale); $\sqrt{9} = 3 \in \mathbb{N}$ (la radice si calcola esattamente).
> 2. Razionali: $\tfrac{3}{4} \in \mathbb{Q}$; $0{,}333\ldots = \tfrac{1}{3} \in \mathbb{Q}$ (ha un periodo, quindi è una frazione).
> 3. Irrazionali: $\sqrt{5}$ e $\pi$ non si scrivono come frazione, quindi stanno solo in $\mathbb{R}$.
> 4. Ordine: per collocare gli irrazionali uso i valori approssimati $\sqrt{5} \approx 2{,}24$ e $\pi \approx 3{,}14$:
> $$
> -4 < 0{,}333\ldots < \tfrac{3}{4} < \sqrt{5} < \sqrt{9} < \pi < 7
> $$

> [!question] Esercizio 8
> Senza calcolatrice, confrontare (dire quale è il maggiore):
> 1. $\sqrt{10}$ e $\tfrac{16}{5}$
> 2. $2\sqrt{3}$ e $\tfrac{7}{2}$
> 3. $3\sqrt{2}$ e $2\sqrt{5}$

> [!success]- Soluzione
> Risultato: 1. $\sqrt{10} < \tfrac{16}{5}$; 2. $2\sqrt{3} < \tfrac{7}{2}$; 3. $3\sqrt{2} < 2\sqrt{5}$ (in tutti e tre i casi è maggiore il secondo numero).
>
> Come si arriva (sono tutti numeri positivi, quindi confrontare i numeri equivale a confrontare i loro quadrati, che sono più semplici):
> 1. $(\sqrt{10})^2 = 10$ e $\left(\tfrac{16}{5}\right)^2 = \tfrac{256}{25} = 10{,}24$. Poiché $10 < 10{,}24$, $\sqrt{10} < \tfrac{16}{5}$.
> 2. $(2\sqrt{3})^2 = 4 \cdot 3 = 12$ e $\left(\tfrac{7}{2}\right)^2 = \tfrac{49}{4} = 12{,}25$. Poiché $12 < 12{,}25$, $2\sqrt{3} < \tfrac{7}{2}$.
> 3. $(3\sqrt{2})^2 = 9 \cdot 2 = 18$ e $(2\sqrt{5})^2 = 4 \cdot 5 = 20$. Poiché $18 < 20$, $3\sqrt{2} < 2\sqrt{5}$.

> [!question] Esercizio 9
> Trovare due numeri razionali compresi tra $\tfrac{2}{5}$ e $\tfrac{1}{2}$.

> [!success]- Soluzione
> Risultato: per esempio $\tfrac{17}{40}$ e $\tfrac{9}{20}$: $\tfrac{2}{5} < \tfrac{17}{40} < \tfrac{9}{20} < \tfrac{1}{2}$ (in decimali $0{,}4 < 0{,}425 < 0{,}45 < 0{,}5$).
>
> Come si arriva:
> 1. La media di due numeri sta sempre in mezzo a loro, e la media di due frazioni è ancora una frazione. Calcolo la media di $\tfrac{2}{5}$ e $\tfrac{1}{2}$:
> $$
> \dfrac{\frac{2}{5} + \frac{1}{2}}{2} = \dfrac{\frac{4}{10} + \frac{5}{10}}{2} = \dfrac{9}{20}
> $$
> 2. Ripeto il procedimento tra $\tfrac{2}{5} = \tfrac{16}{40}$ e $\tfrac{9}{20} = \tfrac{18}{40}$: la media è $\tfrac{17}{40}$.
> 3. Si può continuare all'infinito: è la densità di $\mathbb{Q}$.

#### Valore assoluto

> [!question] Esercizio 10
> Calcolare, togliendo le sbarrette:
> 1. $|-7| + |3 - 10|$
> 2. $|2 - \sqrt{5}|$
> 3. $|\pi - 4|$
> 4. $\sqrt{(-6)^2}$

> [!success]- Soluzione
> Risultato: 1. $14$; 2. $\sqrt{5} - 2$; 3. $4 - \pi$; 4. $6$.
>
> Come si arriva:
> 1. Calcolo i due valori assoluti separatamente: $|-7| = 7$ e $|3 - 10| = |-7| = 7$, quindi $7 + 7 = 14$.
> 2. Guardo il segno del contenuto: $\sqrt{5} \approx 2{,}24 > 2$, quindi $2 - \sqrt{5}$ è negativo e il valore assoluto ne cambia il segno: $|2 - \sqrt{5}| = \sqrt{5} - 2$.
> 3. Guardo il segno del contenuto: $\pi \approx 3{,}14 < 4$, quindi $\pi - 4 < 0$ e $|\pi - 4| = 4 - \pi$.
> 4. Prima il quadrato, poi la radice: $\sqrt{(-6)^2} = \sqrt{36} = 6 = |-6|$, non $-6$.

> [!question] Esercizio 11
> Scrivere come intervallo, o unione di intervalli, l'insieme dei numeri reali che soddisfano:
> 1. $|x| \leq 3$
> 2. $|x - 2| < 5$
> 3. $|x + 1| \geq 4$
> 4. $|x - 4| > 0$

> [!success]- Soluzione
> Risultato: 1. $[-3, 3]$; 2. $(-3, 7)$; 3. $(-\infty, -5] \cup [3, +\infty)$; 4. $\mathbb{R} \setminus \{4\} = (-\infty, 4) \cup (4, +\infty)$.
>
> Come si arriva:
> 1. Con $|x| \leq r$ il numero sta tra $-r$ e $r$: $-3 \leq x \leq 3$, cioè $[-3, 3]$.
> 2. Stessa regola: $-5 < x - 2 < 5$; sommo $2$ a tutti i membri: $-3 < x < 7$, cioè $(-3, 7)$. Sono i punti a distanza meno di $5$ da $2$.
> 3. Con $|\ldots| \geq r$ il contenuto sta fuori da $-r$ e $r$: $x + 1 \leq -4 \ \vee\ x + 1 \geq 4$, cioè $x \leq -5 \ \vee\ x \geq 3$: $(-\infty, -5] \cup [3, +\infty)$. Sono i punti a distanza almeno $4$ da $-1$.
> 4. Il valore assoluto è sempre $\geq 0$ e vale $0$ solo per $x = 4$: quindi $|x - 4| > 0$ vale per tutti i numeri tranne $4$, cioè $\mathbb{R} \setminus \{4\} = (-\infty, 4) \cup (4, +\infty)$.

> [!question] Esercizio 12
> 1. Calcolare la distanza sulla retta tra $-3$ e $5$, e tra $-\tfrac{1}{2}$ e $\tfrac{5}{2}$.
> 2. Trovare i numeri reali che distano $3$ da $-1$, scrivendo la condizione con il valore assoluto.

> [!success]- Soluzione
> Risultato: 1. la distanza tra $-3$ e $5$ è $8$; tra $-\tfrac{1}{2}$ e $\tfrac{5}{2}$ è $3$. 2. $|x + 1| = 3$, con soluzioni $x = -4$ e $x = 2$: l'insieme è $\{-4, 2\}$.
>
> Come si arriva:
> 1. La distanza tra due punti $a$ e $b$ è $|a - b|$: $|5 - (-3)| = |8| = 8$; $\left|\tfrac{5}{2} - \left(-\tfrac{1}{2}\right)\right| = \left|\tfrac{6}{2}\right| = 3$.
> 2. "Distare $3$ da $-1$" si scrive $|x - (-1)| = 3$, cioè $|x + 1| = 3$.
> 3. Il contenuto può valere $3$ oppure $-3$: $x + 1 = 3$ dà $x = 2$, $x + 1 = -3$ dà $x = -4$. Sulla retta sono tre passi a destra e tre a sinistra di $-1$.

#### Intervalli

> [!question] Esercizio 13
> Sono dati $I = [-2, 4)$, $J = (1, 6]$ e $K = (-\infty, 0]$. Calcolare $I \cap J$, $I \cup J$, $I \cap K$, $J \cap K$ e $I \setminus J$.

> [!success]- Soluzione
> Risultato: $I \cap J = (1, 4)$; $I \cup J = [-2, 6]$; $I \cap K = [-2, 0]$; $J \cap K = \emptyset$; $I \setminus J = [-2, 1]$.
>
> Come si arriva (disegno i tre intervalli uno sotto l'altro sulla stessa retta):
> 1. $I \cap J$: a sinistra vince l'estremo più grande, $1$ (escluso, perché $1 \notin J$); a destra il più piccolo, $4$ (escluso, perché $4 \notin I$): $I \cap J = (1, 4)$.
> 2. $I \cup J$: si sovrappongono, quindi coprono senza buchi da $-2$ (compreso) a $6$ (compreso): $I \cup J = [-2, 6]$.
> 3. $I \cap K$: va da $-2$ (compreso in $I$) a $0$ (compreso in $K$): $I \cap K = [-2, 0]$.
> 4. $J \cap K$: $J$ comincia dopo $1$, $K$ finisce in $0$: non si sovrappongono, quindi $J \cap K = \emptyset$.
> 5. $I \setminus J$: tolgo da $I$ la parte da $1$ in poi; l'$1$ resta, perché non sta in $J$: $I \setminus J = [-2, 1]$.

> [!question] Esercizio 14
> Dati
> $$
> X = \{x \in \mathbb{R} \mid x \geq -\sqrt{3}\} \qquad Y = \{x \in \mathbb{R} \mid x < \sqrt{10}\} \qquad Z = \{x \in \mathbb{R} \mid \tfrac{5}{2} < x \leq 4\}
> $$
> trovare $X \cap Y \cap Z$.

> [!success]- Soluzione
> Risultato: $X \cap Y \cap Z = \{x \in \mathbb{R} \mid \tfrac{5}{2} < x < \sqrt{10}\} = \left(\tfrac{5}{2}, \sqrt{10}\right)$.
>
> Come si arriva:
> 1. Riscrivo ogni insieme come intervallo: $X = [-\sqrt{3}, +\infty)$, $Y = (-\infty, \sqrt{10})$, $Z = (\tfrac{5}{2}, 4]$.
> 2. Per il disegno uso i valori approssimati: $-\sqrt{3} \approx -1{,}73$; $\tfrac{5}{2} = 2{,}5$; $\sqrt{10} \approx 3{,}16$; $4$.
> 3. Controllo con i quadrati dove cade $\sqrt{10}$, per non confrontare a occhio: $\left(\tfrac{5}{2}\right)^2 = 6{,}25 < 10 < 16 = 4^2$, quindi $\tfrac{5}{2} < \sqrt{10} < 4$.
> 4. A sinistra vince l'estremo più grande, $\tfrac{5}{2}$, che viene da $Z$ ed è escluso.
> 5. A destra vince l'estremo più piccolo, $\sqrt{10}$, che viene da $Y$ ed è escluso.

> [!question] Esercizio 15
> Calcolare, scrivendo il risultato come intervallo o unione di intervalli:
> 1. il complementare in $\mathbb{R}$ di $[1, 5]$
> 2. $\mathbb{R} \setminus (-2, 3]$
> 3. $[0, 6] \setminus (2, 4)$

> [!success]- Soluzione
> Risultato: 1. $(-\infty, 1) \cup (5, +\infty)$; 2. $(-\infty, -2] \cup (3, +\infty)$; 3. $[0, 2] \cup [4, 6]$.
>
> Come si arriva (quando si toglie un intervallo, gli estremi si scambiano: quelli che erano compresi diventano esclusi e viceversa):
> 1. Restano i numeri prima di $1$ e dopo $5$; $1$ e $5$ stavano nell'intervallo tolto, quindi ora sono esclusi: $(-\infty, 1) \cup (5, +\infty)$.
> 2. $-2$ non stava in $(-2, 3]$, quindi resta; $3$ stava, quindi se ne va: $(-\infty, -2] \cup (3, +\infty)$.
> 3. Da $[0, 6]$ tolgo la parte tra $2$ e $4$, estremi esclusi: $2$ e $4$ non vengono tolti, quindi restano: $[0, 2] \cup [4, 6]$.

## Collegamenti

Il linguaggio degli insiemi e degli intervalli è quello con cui si scrivono i risultati di tutto il corso. In [[02-equazioni-e-disequazioni|equazioni e disequazioni]] le soluzioni di una disequazione sono un intervallo o un'unione di intervalli, la "o" tra due pezzi diventa il simbolo $\cup$ e un sistema di disequazioni è un'intersezione, risolta con lo stesso disegno a righe sovrapposte dell'esercizio del professore; il valore assoluto, introdotto qui come distanza, diventa lo strumento per risolvere equazioni e disequazioni con le sbarrette. In [[03-retta-e-circonferenza|retta e circonferenza]] la distanza $|a - b|$ sulla retta si allarga alla distanza tra due punti del piano, e una circonferenza è l'insieme dei punti $\{P \mid \overline{PC} = r\}$, descritto proprio con una proprietà caratteristica.

Nei [[05-i-vettori|vettori]] la condizione di parallelismo $\vec v = \lambda \vec w$ con $\lambda \in \mathbb{R}^*$ usa il quantificatore "esiste" e la notazione dei reali senza lo zero. Nelle [[06-le-funzioni|funzioni]] dominio e insieme immagine sono insiemi, quasi sempre intervalli o unioni di intervalli, e la funzione stessa, che il professore ha disegnato già nella prima lezione come frecce da un insieme a un altro, è una corrispondenza tra insiemi; nelle [[06-le-funzioni#LE FUNZIONI ELEMENTARI: RETTE, POTENZE, RADICI E VALORE ASSOLUTO|funzioni elementari]] si vede che cosa succede alle potenze quando l'esponente passa dai naturali ai razionali e ai reali. Anche le [[04-le-matrici|matrici]] si descrivono come insiemi: le matrici $2 \times 2$ a elementi reali formano un insieme in cui somma e prodotto hanno proprietà simili, ma non identiche, a quelle dei numeri (il prodotto, per esempio, non è commutativo).

## Per approfondire

- [[appunti-nadia-01.jpeg]] e [[appunti-nadia-02.jpeg]]: gli appunti della prima lezione (programma, insiemi, operazioni e proprietà, esercizio sugli intervalli).
- [[Programma del corso_Istituzioni_di_matematiche_1_canale_1.pdf]]: pagina 1, prima parte del programma (quantificatori, numeri naturali, interi, razionali e reali, assiomi dei reali, irrazionalità di $\sqrt{2}$, valore assoluto, densità di $\mathbb{Q}$ in $\mathbb{R}$).
- [[Giuffrida - Ragusa Cap 1_compressed.pdf]]: capitolo 1, insiemi, operazioni tra insiemi e insiemi numerici.
- Per allenarsi: la sezione [[#ESERCIZI]] di questa pagina (il professore non ha dato un foglio di esercizi su questo argomento).
