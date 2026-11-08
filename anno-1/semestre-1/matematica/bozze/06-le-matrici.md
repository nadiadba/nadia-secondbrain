---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Le matrici e il determinante

Una matrice è una tabella di numeri ordinati in righe e colonne. Il professore l'ha introdotta in classe seguendo questo percorso: prima come si indicano gli elementi, poi la somma, poi il prodotto riga per colonna con le sue proprietà (e un esempio svolto), infine il determinante di una matrice quadrata, calcolato per le matrici 2×2 e 3×3 con la regola di Sarrus e con i complementi algebrici. La pagina segue lo stesso ordine e usa la stessa notazione della lavagna. Qua e là ci sono alcuni complementi (tipi di matrici, proprietà del determinante, significato geometrico), segnalati come tali: servono a capire meglio, e in fondo c'è un cenno a matrice inversa e sistemi lineari per chi vuole andare oltre. Il determinante non è del tutto nuovo: è già comparso in [[03-i-vettori]] per calcolare aree, prodotto vettoriale e volumi.

> [!info] Note collegate
> Teoria: [[01-equazioni-e-disequazioni]] · [[02-retta-e-circonferenza]] · [[03-i-vettori]] · [[04-le-funzioni]] · [[05-funzioni-elementari]] · [[07-insiemi-e-intervalli]] · Ripasso: [[00-ripasso-esonero-1]]

## LE MATRICI

### Righe, colonne e la notazione $a_{ij}$

Una *matrice* è una tabella rettangolare di numeri, chiusa tra parentesi tonde. Si indica con una lettera maiuscola ($A$, $B$, ...) e i suoi numeri, gli *elementi*, con la stessa lettera minuscola e due indici:

$$
a_{ij}
$$

Il professore l'ha scritto così alla lavagna:

- il primo indice, $i$, dice la riga (si contano dall'alto: $i = 1, \dots, m$);
- il secondo indice, $j$, dice la colonna (si contano da sinistra: $j = 1, \dots, n$).

Quindi $a_{21}$ è l'elemento che sta nella seconda riga e nella prima colonna. L'ordine conta sempre: prima la riga, poi la colonna.

Nella lezione del 15 ottobre il professore ha separato i due indici con una virgola: $a_{1,1}$, $a_{2,3}$, $a_{3,1}$. È la stessa cosa, scritta in modo più chiaro: $a_{2,3}$ e $a_{23}$ indicano entrambi l'elemento della seconda riga e della terza colonna. La virgola diventa indispensabile nelle matrici grandi, dove senza di essa $a_{123}$ potrebbe voler dire riga 12 e colonna 3 oppure riga 1 e colonna 23.

Una matrice con due righe e due colonne si scrive

$$
A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}
$$

e in breve si scrive anche $A = (a_{ij})$: "la matrice che al posto $(i, j)$ ha l'elemento $a_{ij}$".

> [!example] Esempio: leggere gli indici
> $$
> A = \begin{pmatrix} 1 & 3 & -5 \\ 5 & 0 & 2 \\ -1 & 0 & 0 \end{pmatrix}
> $$
> - $a_{11} = 1$ (prima riga, prima colonna);
> - $a_{13} = -5$ (prima riga, terza colonna);
> - $a_{21} = 5$ (seconda riga, prima colonna);
> - $a_{31} = -1$ (terza riga, prima colonna).
>
> È la matrice che il professore ha usato alla lavagna per i complementi algebrici: la ritroveremo più avanti.

### Tipi di matrici (complemento)

Una matrice con $m$ righe e $n$ colonne si dice *di tipo* $m \times n$ (si legge "m per n"). Prima si dicono le righe, poi le colonne, come negli indici. Per esempio $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ è di tipo $2 \times 3$.

Alcuni tipi hanno un nome:

- una matrice è *quadrata* se ha tante righe quante colonne ($n \times n$). Il determinante si calcola solo per le matrici quadrate;
- la *matrice nulla*, che il professore indica con $\Omega$ (omega maiuscola), ha tutti gli elementi uguali a zero. Fa la parte dello zero tra i numeri;
- la *matrice identità* $I$ è quadrata, ha $1$ sulla *diagonale principale* (quella che scende da in alto a sinistra a in basso a destra, cioè gli elementi $a_{11}, a_{22}, \dots$) e $0$ altrove. Fa la parte del numero $1$:

$$
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix};
$$

- la *matrice diagonale* (il professore l'ha scritta il 15 ottobre) è una matrice quadrata che ha zeri dappertutto tranne, al più, sulla diagonale principale. Gli elementi della diagonale, $a_{1,1}, a_{2,2}, a_{3,3}$, possono essere numeri qualsiasi (anche zero):

$$
A = \begin{pmatrix} a_{1,1} & 0 & 0 \\ 0 & a_{2,2} & 0 \\ 0 & 0 & a_{3,3} \end{pmatrix}, \qquad \text{per esempio} \quad \begin{pmatrix} 2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 5 \end{pmatrix}.
$$

In formula: $a_{ij} = 0$ ogni volta che $i \neq j$. La matrice identità è la matrice diagonale con tutti $1$ sulla diagonale.

- la *trasposta* di $A$, che il professore scrive ${}^{T}\!A$ con la $T$ in alto a sinistra (in molti libri si trova $A^T$, a destra: è la stessa cosa), si ottiene scambiando le righe con le colonne: la prima riga di $A$ diventa la prima colonna di ${}^{T}\!A$, e così via. Se $A$ è $m \times n$, ${}^{T}\!A$ è $n \times m$.

> [!example] Esempio: la trasposta
> $$
> A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \quad\Longrightarrow\quad A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}
> $$
> In formula: l'elemento al posto $(i, j)$ di $A^T$ è l'elemento al posto $(j, i)$ di $A$.

> [!example] Esempio del professore (15 ottobre)
> $$
> A = \begin{pmatrix} 2 & 1 & 0 \\ -2 & 0 & -1 \end{pmatrix} \ (2 \times 3) \quad\Longrightarrow\quad {}^{T}\!A = \begin{pmatrix} 2 & -2 \\ 1 & 0 \\ 0 & -1 \end{pmatrix} \ (3 \times 2)
> $$
> La prima riga $(2, 1, 0)$ è diventata la prima colonna, la seconda riga $(-2, 0, -1)$ la seconda colonna. Le proprietà della trasposta, che coinvolgono anche il prodotto, sono più avanti, alla fine della parte sul prodotto riga per colonna.

Un vettore si può vedere come una matrice con una sola riga, $(1 \ \ 2 \ \ {-1})$, o con una sola colonna. È il legame tra questa pagina e [[03-i-vettori]].

### La somma

Due matrici dello stesso tipo si sommano elemento per elemento: si sommano i due numeri che stanno nello stesso posto. Il professore l'ha scritto in una riga:

> [!abstract] Somma di due matrici
> $$
> A + B = (a_{ij} + b_{ij})
> $$
> La somma si può fare solo se $A$ e $B$ hanno lo stesso numero di righe e lo stesso numero di colonne.

È la stessa regola della somma di vettori in componenti: la prima con la prima, la seconda con la seconda.

> [!example] Esempio
> $$
> \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 1+1 & 2+(-1) \\ 1+2 & 0+1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 3 & 1 \end{pmatrix}
> $$

Sommare la matrice nulla non cambia niente: $A + \Omega = A$.

### Il prodotto per uno scalare (complemento)

Moltiplicare una matrice per un numero $k$ (uno *scalare*) vuol dire moltiplicare per $k$ ogni suo elemento:

$$
k\,A = (k\,a_{ij}).
$$

Per esempio $3 \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 3 & 0 \end{pmatrix}$. Di nuovo, è come per i vettori: $k\,(u_1, u_2) = (k u_1, k u_2)$.

## IL PRODOTTO RIGA PER COLONNA

### Come si calcola

Il prodotto tra due matrici non si fa elemento per elemento. Si fa *riga per colonna*: ogni elemento del risultato nasce da una riga della prima matrice e da una colonna della seconda.

> [!abstract] Prodotto riga per colonna
> L'elemento del prodotto $A \cdot B$ che sta nella riga $i$ e nella colonna $j$ si ottiene così:
> 1. si prende la riga $i$ di $A$ e la colonna $j$ di $B$;
> 2. si moltiplicano il primo elemento della riga con il primo della colonna, il secondo con il secondo, e così via;
> 3. si sommano tutti questi prodotti.

Il conto del punto 2 e 3 è lo stesso del prodotto scalare di [[03-i-vettori]]: "primo per primo, più secondo per secondo, più ...". Quindi ogni elemento di $A \cdot B$ è il prodotto scalare di una riga di $A$ per una colonna di $B$.

Per due matrici 2×2 il professore ha scritto lo schema dei quattro posti:

$$
A \cdot B = \begin{pmatrix} (\text{1ª riga})(\text{1ª colonna}) & (\text{1ª riga})(\text{2ª colonna}) \\ (\text{2ª riga})(\text{1ª colonna}) & (\text{2ª riga})(\text{2ª colonna}) \end{pmatrix}
$$

Il numero della riga del risultato è quello della riga di $A$ che si usa; il numero della colonna è quello della colonna di $B$.

![[06-prodotto-riga-colonna.svg|640]]

> [!example] Esempio della lavagna
> $$
> A = \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix}
> $$
> 1. 1ª riga × 1ª colonna: $(1, 2)$ con $(1, 2)$, cioè $1 \cdot 1 + 2 \cdot 2 = 5$.
> 2. 1ª riga × 2ª colonna: $(1, 2)$ con $(-1, 1)$, cioè $1 \cdot (-1) + 2 \cdot 1 = 1$.
> 3. 2ª riga × 1ª colonna: $(1, 0)$ con $(1, 2)$, cioè $1 \cdot 1 + 0 \cdot 2 = 1$.
> 4. 2ª riga × 2ª colonna: $(1, 0)$ con $(-1, 1)$, cioè $1 \cdot (-1) + 0 \cdot 1 = -1$.
>
> $$
> A \cdot B = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 & 1 \cdot (-1) + 2 \cdot 1 \\ 1 \cdot 1 + 0 & -1 \cdot 1 + 0 \end{pmatrix} = \begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix}
> $$

> [!tip] Un trucco per non sbagliare
> Con la mano sinistra si scorre la riga di $A$ da sinistra a destra, con la destra si scende lungo la colonna di $B$ dall'alto in basso: le due dita toccano ogni volta i due numeri da moltiplicare.

### Quando il prodotto si può fare (complemento)

Perché "primo per primo, secondo per secondo" funzioni, la riga di $A$ e la colonna di $B$ devono avere la stessa lunghezza. Una riga di $A$ ha tanti elementi quante sono le colonne di $A$; una colonna di $B$ ha tanti elementi quante sono le righe di $B$.

> [!abstract] Condizione per il prodotto
> $A \cdot B$ si può fare solo se il numero di colonne di $A$ è uguale al numero di righe di $B$:
> $$
> (m \times n) \cdot (n \times p) = (m \times p).
> $$
> Il risultato ha tante righe quante $A$ e tante colonne quante $B$.

![[06-tipi-prodotto.svg|560]]

Un modo semplice di ricordarlo: si scrivono i due tipi uno accanto all'altro, $2 \times \underline{3} \cdot \underline{3} \times 4$. I due numeri interni devono essere uguali, i due esterni danno il tipo del risultato ($2 \times 4$).

Per le matrici quadrate dello stesso tipo il problema non si pone: due matrici $2 \times 2$ si possono sempre moltiplicare, e il risultato è ancora $2 \times 2$.

> [!example] Esempio: matrici di tipo diverso
> $$
> \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \cdot 3 + 0 \cdot 1 + 2 \cdot 2 \\ -1 \cdot 3 + 3 \cdot 1 + 1 \cdot 2 \end{pmatrix} = \begin{pmatrix} 7 \\ 2 \end{pmatrix}
> $$
> Tipi: $(2 \times 3) \cdot (3 \times 1) = (2 \times 1)$. Il prodotto nell'ordine opposto, $(3 \times 1) \cdot (2 \times 3)$, non si può fare: $1 \neq 2$.

### Le proprietà del prodotto

Alla lavagna il professore ha elencato le proprietà del prodotto riga per colonna, segnando quali valgono e quali no.

> [!abstract] Proprietà del prodotto riga per colonna
> - Associativa: sì. $(A \cdot B) \cdot C = A \cdot (B \cdot C)$.
> - Distributiva: sì. $A \cdot (B + C) = A \cdot B + A \cdot C$ e $(A + B) \cdot C = A \cdot C + B \cdot C$.
> - Commutativa: no. In generale $A \cdot B \neq B \cdot A$.

L'associativa permette di scrivere $A \cdot B \cdot C$ senza parentesi. La distributiva permette di "svolgere" i prodotti come con i numeri, ma rispettando l'ordine: la matrice che sta a sinistra resta a sinistra.

La proprietà che manca è la più importante da ricordare: con le matrici l'ordine dei fattori conta. Lo si vede rifacendo l'esempio della lavagna con i fattori scambiati.

> [!example] Esempio: $B \cdot A$ è diverso da $A \cdot B$
> Con le stesse matrici di prima:
> $$
> B \cdot A = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 + (-1) \cdot 1 & 1 \cdot 2 + (-1) \cdot 0 \\ 2 \cdot 1 + 1 \cdot 1 & 2 \cdot 2 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 3 & 4 \end{pmatrix}
> $$
> Invece $A \cdot B = \begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix}$. Sono due matrici diverse: il prodotto non è commutativo.

Con le matrici di tipo diverso le cose vanno anche peggio: come nell'esempio precedente, può succedere che $A \cdot B$ si possa fare e $B \cdot A$ no.

La matrice identità si comporta come il numero $1$: $A \cdot I = I \cdot A = A$ (per $A$ quadrata dello stesso tipo). La matrice nulla come lo zero: $A \cdot \Omega = \Omega \cdot A = \Omega$.

### Prodotto uguale a $\Omega$

Tra i numeri vale la *legge di annullamento del prodotto*: se $a \cdot b = 0$, allora $a = 0$ oppure $b = 0$ (è quella che si usa per risolvere le equazioni scomposte, vedi [[01-equazioni-e-disequazioni]]). Con le matrici vale solo in una direzione.

> [!abstract] Prodotto nullo
> - Se $A = \Omega$ oppure $B = \Omega$, allora $A \cdot B = \Omega$.
> - Il contrario non vale: $A \cdot B = \Omega$ non implica che $A = \Omega$ oppure $B = \Omega$.
> $$
> A \cdot B = \Omega \quad \not\Longrightarrow \quad A = \Omega \ \text{oppure} \ B = \Omega
> $$

Ci sono cioè due matrici entrambe diverse da $\Omega$ il cui prodotto è la matrice nulla.

> [!example] Esempio: due matrici non nulle con prodotto nullo
> $$
> A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}
> $$
> $$
> A \cdot B = \begin{pmatrix} 1 \cdot 1 + 1 \cdot (-1) & 1 \cdot (-1) + 1 \cdot 1 \\ 1 \cdot 1 + 1 \cdot (-1) & 1 \cdot (-1) + 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = \Omega
> $$
> Né $A$ né $B$ sono la matrice nulla, eppure il prodotto lo è. Il motivo: ogni riga di $A$, $(1, 1)$, è perpendicolare a ogni colonna di $B$, $(1, -1)$ e $(-1, 1)$, e il loro prodotto scalare è zero.

> [!warning] Non "semplificare" le matrici
> Da $A \cdot B = \Omega$ non si può concludere che una delle due è nulla, e da $A \cdot B = A \cdot C$ non si può concludere che $B = C$. È lo stesso fenomeno del prodotto scalare in [[03-i-vettori]]: $(1, 0) \cdot (0, 1) = 0$ senza che nessuno dei due vettori sia nullo.

### Le proprietà della trasposta

Il 15 ottobre, dopo aver definito la trasposta ${}^{T}\!A$ (vedi i tipi di matrici, all'inizio della pagina), il professore ne ha scritto tre proprietà.

> [!abstract] Proprietà della trasposta
> 1. ${}^{T}({}^{T}\!A) = A$: trasponendo due volte si torna alla matrice di partenza.
> 2. ${}^{T}(A + B) = {}^{T}\!A + {}^{T}\!B$: la trasposta di una somma è la somma delle trasposte.
> 3. ${}^{T}(A \cdot B) = {}^{T}\!B \cdot {}^{T}\!A$: la trasposta di un prodotto è il prodotto delle trasposte, ma in ordine inverso.

Le prime due si capiscono subito. Scambiare righe e colonne due volte rimette ogni elemento al suo posto. E siccome la somma si fa posto per posto, non importa se si scambiano righe e colonne prima o dopo aver sommato.

La terza è quella da ricordare bene, perché l'ordine si inverte. Il motivo si vede dai tipi: se $A$ è $2 \times 3$ e $B$ è $3 \times 4$, allora ${}^{T}\!B$ è $4 \times 3$ e ${}^{T}\!A$ è $3 \times 2$. Il prodotto ${}^{T}\!B \cdot {}^{T}\!A$ si può fare ($4 \times \underline{3} \cdot \underline{3} \times 2$), mentre ${}^{T}\!A \cdot {}^{T}\!B$ in generale no ($3 \times \underline{2} \cdot \underline{4} \times 3$).

> [!example] Esempio: la proprietà 3 con le matrici della lavagna
> $A = \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix}$, e si è calcolato $A \cdot B = \begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix}$.
>
> 1. Le trasposte: ${}^{T}\!A = \begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix}$, ${}^{T}\!B = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix}$.
> 2. Nell'ordine giusto:
>
> $$
> {}^{T}\!B \cdot {}^{T}\!A = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 & 1 \cdot 1 + 2 \cdot 0 \\ -1 \cdot 1 + 1 \cdot 2 & -1 \cdot 1 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix} = {}^{T}(A \cdot B).
> $$
>
> 3. Nell'ordine sbagliato:
>
> $$
> {}^{T}\!A \cdot {}^{T}\!B = \begin{pmatrix} 1 \cdot 1 + 1 \cdot (-1) & 1 \cdot 2 + 1 \cdot 1 \\ 2 \cdot 1 + 0 & 2 \cdot 2 + 0 \end{pmatrix} = \begin{pmatrix} 0 & 3 \\ 2 & 4 \end{pmatrix},
> $$
>
> che non è ${}^{T}(A \cdot B)$: è invece la trasposta di $B \cdot A = \begin{pmatrix} 0 & 2 \\ 3 & 4 \end{pmatrix}$.

## IL DETERMINANTE

### Che cos'è; le matrici 1×1 e 2×2

Il *determinante* è un numero che si associa a una matrice quadrata. Il professore l'ha indicato con due notazioni equivalenti:

$$
A \ \longmapsto \ |A| \qquad \text{oppure} \qquad \det A.
$$

Le sbarre verticali $|\ |$ al posto delle parentesi tonde vogliono dire "il determinante di questa tabella". Non è un valore assoluto: il determinante può essere negativo.

Si costruisce partendo dalle matrici più piccole.

> [!abstract] Determinante delle matrici 1×1 e 2×2
> - $1 \times 1$: se $A = (a)$, allora $\det A = a$.
> - $2 \times 2$: se $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, allora
> $$
> \det A = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc.
> $$

Per la 2×2 il professore ha disegnato l'incrocio delle due diagonali: il prodotto della diagonale principale ($a \cdot d$) meno il prodotto dell'altra diagonale ($b \cdot c$).

![[06-diagonali-2x2.svg|400]]

> [!example] Esempio
> Per le due matrici dell'esempio del prodotto:
> - $\det A = \begin{vmatrix} 1 & 2 \\ 1 & 0 \end{vmatrix} = 1 \cdot 0 - 2 \cdot 1 = -2$;
> - $\det B = \begin{vmatrix} 1 & -1 \\ 2 & 1 \end{vmatrix} = 1 \cdot 1 - (-1) \cdot 2 = 1 + 2 = 3$.

> [!warning] Il segno meno dei numeri negativi
> In $ad - bc$, se $b$ o $c$ sono negativi conviene scrivere il prodotto tra parentesi: $-(-1) \cdot 2 = +2$. È l'errore più frequente.

### Le matrici 3×3: la regola di Sarrus

Per una matrice 3×3 il professore ha usato la *regola di Sarrus*, che estende l'idea delle diagonali.

1. Si ricopiano a destra della matrice le sue prime due colonne.
2. Si moltiplicano gli elementi delle tre diagonali che scendono verso destra e si sommano i tre prodotti (segno $+$).
3. Si moltiplicano gli elementi delle tre diagonali che salgono verso destra e si sottraggono i tre prodotti (segno $-$).

![[06-sarrus.svg|600]]

Scritto per esteso, come alla lavagna:

> [!abstract] Determinante 3×3 (regola di Sarrus)
> $$
> \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{31}a_{22}a_{13} - a_{32}a_{23}a_{11} - a_{33}a_{21}a_{12}
> $$

Si osservi che in ogni prodotto c'è esattamente un elemento per ogni riga e uno per ogni colonna. È questo che rende il determinante "equilibrato" e che sta dietro alle sue proprietà.

Negli appunti di lezione c'è anche un secondo modo, quello del professore: le linee si tracciano direttamente sulla matrice, senza ricopiare le due colonne. Le diagonali che con le colonne ricopiate "uscivano" dalla matrice qui diventano dei triangoli.

- Segno $+$: la diagonale principale ($a_{1,1}$, $a_{2,2}$, $a_{3,3}$) e i due triangoli che hanno un lato parallelo a lei. Il primo unisce $a_{1,2}$ e $a_{2,3}$ (un lato parallelo alla diagonale, appena sopra) con l'angolo opposto $a_{3,1}$; il secondo unisce $a_{2,1}$ e $a_{3,2}$ (appena sotto) con l'angolo opposto $a_{1,3}$.
- Segno $-$: l'altra diagonale ($a_{1,3}$, $a_{2,2}$, $a_{3,1}$) e i due triangoli con un lato parallelo a questa. Il primo unisce $a_{1,2}$ e $a_{2,1}$ con l'angolo $a_{3,3}$; il secondo unisce $a_{2,3}$ e $a_{3,2}$ con l'angolo $a_{1,1}$.

Negli appunti le linee del $+$ sono di un colore e quelle del $-$ di un altro, tutte sulla stessa matrice. Qui sotto le sei moltiplicazioni sono separate, per vederle meglio.

![[06-sarrus-sulla-matrice.svg|700]]

> [!abstract] Sarrus sulla matrice, nell'ordine del professore
> $$
> \det A = (a_{1,1}a_{2,2}a_{3,3}) + (a_{2,3}a_{1,2}a_{3,1}) + (a_{2,1}a_{3,2}a_{1,3}) - (a_{1,3}a_{2,2}a_{3,1}) - (a_{2,1}a_{1,2}a_{3,3}) - (a_{3,2}a_{2,3}a_{1,1})
> $$
> I sei prodotti sono gli stessi della regola con le colonne ricopiate, solo scritti in un altro ordine (nella moltiplicazione l'ordine dei fattori non conta): il risultato è identico.

> [!example] Esempio: Sarrus sulla matrice della lavagna
> $$
> A = \begin{pmatrix} 1 & 3 & -5 \\ 5 & 0 & 2 \\ -1 & 0 & 0 \end{pmatrix}
> $$
> Segno $+$:
> - $a_{1,1}a_{2,2}a_{3,3} = 1 \cdot 0 \cdot 0 = 0$;
> - $a_{2,3}a_{1,2}a_{3,1} = 2 \cdot 3 \cdot (-1) = -6$;
> - $a_{2,1}a_{3,2}a_{1,3} = 5 \cdot 0 \cdot (-5) = 0$.
>
> Segno $-$:
> - $a_{1,3}a_{2,2}a_{3,1} = (-5) \cdot 0 \cdot (-1) = 0$;
> - $a_{2,1}a_{1,2}a_{3,3} = 5 \cdot 3 \cdot 0 = 0$;
> - $a_{3,2}a_{2,3}a_{1,1} = 0 \cdot 2 \cdot 1 = 0$.
>
> $\det A = (0 - 6 + 0) - (0 + 0 + 0) = -6$, lo stesso risultato che si trova più avanti con Laplace.

> [!warning] Copiare bene i segni degli elementi
> Se nel ricopiare la matrice si perdono i segni meno, scrivendo $5$ al posto di $-5$ e $1$ al posto di $-1$, il prodotto $a_{2,3}a_{1,2}a_{3,1}$ diventa $2 \cdot 3 \cdot 1 = +6$ e il determinante viene $+6$ invece di $-6$. Prima di cominciare i conti conviene controllare la matrice elemento per elemento, e nei prodotti mettere sempre tra parentesi i numeri negativi.

> [!example] Esempio
> $$
> \begin{vmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & -1 & 1 \end{vmatrix}
> $$
> Diagonali verso il basso (con le colonne ricopiate):
> - $a_{11}a_{22}a_{33} = 1 \cdot 1 \cdot 1 = 1$;
> - $a_{12}a_{23}a_{31} = 2 \cdot 3 \cdot 2 = 12$;
> - $a_{13}a_{21}a_{32} = 0 \cdot 0 \cdot (-1) = 0$.
>
> Diagonali verso l'alto:
> - $a_{31}a_{22}a_{13} = 2 \cdot 1 \cdot 0 = 0$;
> - $a_{32}a_{23}a_{11} = (-1) \cdot 3 \cdot 1 = -3$;
> - $a_{33}a_{21}a_{12} = 1 \cdot 0 \cdot 2 = 0$.
>
> Risultato: $(1 + 12 + 0) - (0 + (-3) + 0) = 13 + 3 = 16$. È lo stesso determinante calcolato con lo sviluppo lungo la prima riga in [[03-i-vettori]].

> [!warning] Sarrus vale solo per le 3×3
> Per le matrici 4×4 o più grandi le "diagonali" non danno il determinante. Lì serve lo sviluppo con i complementi algebrici (qui sotto), che vale per tutte le matrici quadrate.

### Minori e complementi algebrici

Il secondo metodo riporta il determinante di una matrice grande a determinanti di matrici più piccole. Servono due ingredienti.

Il primo è il *minore* dell'elemento $a_{ij}$: il determinante della matrice che resta quando si cancellano la riga $i$ e la colonna $j$. Per una 3×3 resta una 2×2, e il suo determinante si fa con le diagonali.

Il secondo è un segno, $(-1)^{i+j}$. Siccome $-1$ elevato a un numero pari dà $+1$ e elevato a un numero dispari dà $-1$:

- se $i + j$ è pari, il segno è $+$;
- se $i + j$ è dispari, il segno è $-$.

Alla lavagna il professore ha scritto lo schema dei segni per una 3×3, che si ricorda come una scacchiera che parte con $+$ in alto a sinistra:

$$
(-1)^{i+j}: \qquad \begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}
$$

![[06-schema-segni.svg|520]]

Per esempio al posto $(1, 2)$ si ha $(-1)^{1+2} = (-1)^3 = -1$, come alla lavagna.

> [!abstract] Definizione: complemento algebrico
> Il *complemento algebrico* (o *cofattore*) dell'elemento $a_{ij}$ è
> $$
> A_{ij} = (-1)^{i+j} \cdot \big(\text{determinante che resta togliendo la riga } i \text{ e la colonna } j\big).
> $$
> Cioè: il minore, con il segno della scacchiera.

> [!example] Esempio della lavagna
> $$
> A = \begin{pmatrix} 1 & 3 & -5 \\ 5 & 0 & 2 \\ -1 & 0 & 0 \end{pmatrix}
> $$
> 1. $A_{11}$: si tolgono la riga 1 e la colonna 1, resta $\begin{vmatrix} 0 & 2 \\ 0 & 0 \end{vmatrix} = 0 \cdot 0 - 2 \cdot 0 = 0$. Il segno è $(-1)^{1+1} = +1$, quindi $A_{11} = 0$.
> 2. $A_{22}$: si tolgono la riga 2 e la colonna 2, resta $\begin{vmatrix} 1 & -5 \\ -1 & 0 \end{vmatrix} = 1 \cdot 0 - (-5)(-1) = 0 - 5 = -5$. Il segno è $(-1)^{2+2} = +1$, quindi $A_{22} = -5$.
> 3. $A_{12}$: si tolgono la riga 1 e la colonna 2, resta $\begin{vmatrix} 5 & 2 \\ -1 & 0 \end{vmatrix} = 5 \cdot 0 - 2 \cdot (-1) = 2$. Il segno è $(-1)^{1+2} = -1$, quindi $A_{12} = -2$.

![[06-minori.svg|720]]

### Lo sviluppo di Laplace

Con i complementi algebrici il determinante si calcola così.

> [!abstract] Sviluppo di Laplace
> Si sceglie una riga (o una colonna) qualunque. Il determinante è la somma dei prodotti di ogni elemento di quella riga per il proprio complemento algebrico. Per esempio, lungo la riga $i$ di una 3×3:
> $$
> \det A = a_{i1}A_{i1} + a_{i2}A_{i2} + a_{i3}A_{i3}.
> $$
> Lungo la colonna $j$: $\det A = a_{1j}A_{1j} + a_{2j}A_{2j} + a_{3j}A_{3j}$. Qualunque riga o colonna si scelga, il risultato è lo stesso.

Il professore ha scritto lo stesso teorema, che chiama *teorema di Laplace*, in forma compatta:

$$
\det A = \sum_{j=1}^{n} a_{ij}A_{ij} .
$$

Il simbolo $\sum$ (la lettera greca sigma maiuscola) vuol dire "somma". La formula si legge così: si fissa la riga $i$; si fa variare $j$ da $1$ a $n$, cioè si percorrono tutte le colonne; per ogni posto si moltiplica l'elemento $a_{ij}$ per il suo complemento algebrico $A_{ij}$; si sommano tutti questi prodotti. Per una 3×3 ($n = 3$) e la prima riga ($i = 1$) diventa proprio $a_{11}A_{11} + a_{12}A_{12} + a_{13}A_{13}$.

Lo sviluppo lungo la prima riga è quello già usato in [[03-i-vettori]], con i segni $+\,-\,+$.

La libertà di scegliere la riga o la colonna è il vero vantaggio del metodo. Un elemento uguale a zero dà un prodotto uguale a zero, qualunque sia il suo complemento algebrico: non serve nemmeno calcolarlo. Quindi conviene scegliere la riga o la colonna con più zeri.

> [!example] Esempio della lavagna: $\det A$
> $$
> A = \begin{pmatrix} 1 & 3 & -5 \\ 5 & 0 & 2 \\ -1 & 0 & 0 \end{pmatrix}
> $$
> La seconda colonna, $(3, 0, 0)$, ha due zeri. Sviluppando lungo la seconda colonna:
> $$
> \det A = a_{12}A_{12} + a_{22}A_{22} + a_{32}A_{32} = 3 \cdot A_{12} + 0 \cdot A_{22} + 0 \cdot A_{32} = 3 \cdot A_{12}.
> $$
> Si è calcolato prima $A_{12} = -2$, quindi $\det A = 3 \cdot (-2) = -6$.
>
> Anche la terza riga, $(-1, 0, 0)$, ha due zeri: $\det A = a_{31}A_{31} = (-1) \cdot (-1)^{3+1}\begin{vmatrix} 3 & -5 \\ 0 & 2 \end{vmatrix} = (-1) \cdot (+1) \cdot 6 = -6$. Stesso risultato.

> [!example] Esempio degli appunti: Laplace lungo la prima riga
> Negli appunti lo sviluppo è fatto lungo la prima riga, scrivendo il segno della scacchiera in piccolo accanto a ogni elemento:
>
> $$
> \begin{vmatrix} 1^{+} & 3^{-} & -5^{+} \\ 5^{-} & 0^{+} & 2^{-} \\ -1^{+} & 0^{-} & 0^{+} \end{vmatrix}
> $$
>
> 1. $a_{1,1} = 1$, segno $+$: si tolgono la riga 1 e la colonna 1, resta $\begin{vmatrix} 0 & 2 \\ 0 & 0 \end{vmatrix} = 0$.
> 2. $a_{1,2} = 3$, segno $-$: resta $\begin{vmatrix} 5 & 2 \\ -1 & 0 \end{vmatrix} = 5 \cdot 0 - 2 \cdot (-1) = 2$.
> 3. $a_{1,3} = -5$, segno $+$: resta $\begin{vmatrix} 5 & 0 \\ -1 & 0 \end{vmatrix} = 0$.
>
> $$
> \det A = +1 \cdot 0 \; - \; 3 \cdot 2 \; + \; (-5) \cdot 0 = 0 - 6 + 0 = -6 .
> $$
>
> Attenzione al terzo termine: il segno della scacchiera è $+$ e l'elemento è $-5$, quindi si scrive $+(-5)$, cioè $-5$. Qui non cambia nulla perché il minore è zero, ma in generale è un punto dove si sbaglia facilmente.

> [!example] Verifica con la regola di Sarrus
> Con la stessa matrice:
> - verso il basso: $1 \cdot 0 \cdot 0 + 3 \cdot 2 \cdot (-1) + (-5) \cdot 5 \cdot 0 = 0 - 6 + 0 = -6$;
> - verso l'alto: $(-1) \cdot 0 \cdot (-5) + 0 \cdot 2 \cdot 1 + 0 \cdot 5 \cdot 3 = 0$.
>
> $\det A = -6 - 0 = -6$. I due metodi danno lo stesso numero, come deve essere.

> [!tip] Quale metodo usare
> Per una 3×3 senza zeri Sarrus è il più veloce. Se c'è una riga o una colonna con degli zeri, Laplace lungo quella riga è più rapido e si sbaglia meno. In entrambi i casi, se c'è tempo, si può controllare il risultato con l'altro metodo.

### Il determinante simbolico e il prodotto vettoriale

Alla lavagna il professore ha usato la regola di Sarrus anche per il prodotto vettoriale di [[03-i-vettori]]. Si scrive un determinante "simbolico" che nella prima riga ha i versori $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ (nello Stewart $\mathbf{i}, \mathbf{j}, \mathbf{k}$) e nelle altre due le componenti dei vettori:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}.
$$

Non è un vero determinante (nella prima riga ci sono vettori, non numeri), ma lo si calcola come se lo fosse, con Sarrus oppure con Laplace lungo la prima riga. Il risultato è un vettore.

> [!example] Esempio (esercizio 1 del foglio sul prodotto vettoriale)
> $\mathbf{u} = (1, 2, -1)$, $\mathbf{v} = (3, -1, 2)$.
> $$
> \begin{vmatrix} \mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\ 1 & 2 & -1 \\ 3 & -1 & 2 \end{vmatrix}
> $$
> Con Sarrus:
> - verso il basso: $\mathbf{e}_1 \cdot 2 \cdot 2 + \mathbf{e}_2 \cdot (-1) \cdot 3 + \mathbf{e}_3 \cdot 1 \cdot (-1) = 4\mathbf{e}_1 - 3\mathbf{e}_2 - \mathbf{e}_3$;
> - verso l'alto: $3 \cdot 2 \cdot \mathbf{e}_3 + (-1) \cdot (-1) \cdot \mathbf{e}_1 + 2 \cdot 1 \cdot \mathbf{e}_2 = 6\mathbf{e}_3 + \mathbf{e}_1 + 2\mathbf{e}_2$.
>
> Sottraendo: $(4 - 1)\mathbf{e}_1 + (-3 - 2)\mathbf{e}_2 + (-1 - 6)\mathbf{e}_3 = 3\mathbf{e}_1 - 5\mathbf{e}_2 - 7\mathbf{e}_3$, cioè $\mathbf{u} \times \mathbf{v} = (3, -5, -7)$, come in [[03-i-vettori]].

### Proprietà utili del determinante (complemento)

Queste proprietà non sono state scritte alla lavagna, ma aiutano molto nei conti e spiegano perché certi determinanti vengono zero "a colpo d'occhio".

> [!abstract] Proprietà del determinante
> 1. $\det A^T = \det A$: righe e colonne si comportano allo stesso modo, quindi tutto quello che si dice per le righe vale anche per le colonne.
> 2. Scambiando due righe il determinante cambia segno (il valore assoluto resta lo stesso).
> 3. Se una riga è tutta di zeri, il determinante è $0$.
> 4. Se due righe sono uguali o proporzionali (una è un multiplo dell'altra), il determinante è $0$.
> 5. Moltiplicando una riga per un numero $k$, il determinante viene moltiplicato per $k$.
> 6. Teorema di Binet: $\det(A \cdot B) = \det A \cdot \det B$.

Il perché delle prime, in breve:

- la 3 viene dal fatto che in ogni prodotto di Sarrus c'è un elemento di ogni riga: se una riga è nulla, ogni prodotto contiene uno zero;
- la 4 viene dalla 2: scambiando due righe uguali la matrice non cambia, ma il determinante dovrebbe cambiare segno; l'unico numero uguale al suo opposto è $0$.

> [!example] Esempio: Binet con le matrici della lavagna
> Si è visto che $\det A = -2$, $\det B = 3$ e $A \cdot B = \begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix}$.
>
> $\det(A \cdot B) = 5 \cdot (-1) - 1 \cdot 1 = -6$, e infatti $\det A \cdot \det B = (-2) \cdot 3 = -6$.
>
> Anche se $A \cdot B \neq B \cdot A$, i due prodotti hanno lo stesso determinante: $\det(B \cdot A) = \begin{vmatrix} 0 & 2 \\ 3 & 4 \end{vmatrix} = 0 - 6 = -6$.

> [!warning] Il determinante non va d'accordo con la somma
> In generale $\det(A + B) \neq \det A + \det B$. Con le stesse matrici: $A + B = \begin{pmatrix} 2 & 1 \\ 3 & 1 \end{pmatrix}$ ha determinante $2 - 3 = -1$, mentre $\det A + \det B = -2 + 3 = 1$.

### Il significato geometrico: aree e volumi (complemento)

Il determinante misura quanto è "grande" la figura costruita sulle righe della matrice. È ciò che si è visto in [[03-i-vettori]].

Per una 2×2, le due righe sono due vettori del piano $\mathbf{u}$ e $\mathbf{v}$. Il valore assoluto del determinante è l'area del parallelogramma che ha per lati $\mathbf{u}$ e $\mathbf{v}$; il segno dice se per andare da $\mathbf{u}$ a $\mathbf{v}$ si gira in senso antiorario ($+$) o orario ($-$).

![[06-area-determinante.svg|460]]

> [!abstract] Aree e volumi con il determinante
> - Nel piano: area del parallelogramma di lati $\mathbf{u}, \mathbf{v}$ $= \left|\begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix}\right|$.
> - Nello spazio: volume del parallelepipedo di spigoli $\mathbf{u}, \mathbf{v}, \mathbf{w}$ $= \left|\begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}\right| = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|$, il prodotto triplo.

Questa lettura spiega anche le proprietà:

- due righe proporzionali sono due vettori paralleli: il parallelogramma è schiacciato, l'area è zero, e il determinante è $0$;
- tre vettori nello stesso piano (complanari) danno un parallelepipedo schiacciato, di volume zero;
- moltiplicare una riga per $k$ vuol dire allungare un lato di $k$ volte, e l'area si moltiplica per $k$.

> [!example] Esempio
> $\mathbf{u} = (3, 1)$, $\mathbf{v} = (1, 2)$: $\begin{vmatrix} 3 & 1 \\ 1 & 2 \end{vmatrix} = 3 \cdot 2 - 1 \cdot 1 = 5$. Il parallelogramma della figura ha area $5$, e il segno positivo dice che da $\mathbf{u}$ a $\mathbf{v}$ si gira in senso antiorario.

## PER ANDARE OLTRE: MATRICE INVERSA E SISTEMI LINEARI

Questa parte non è stata fatta in classe: è solo un cenno, per vedere a che cosa servono matrici e determinanti.

### La matrice inversa

Tra i numeri, l'inverso di $a$ è il numero $a^{-1} = \frac1a$ tale che $a \cdot a^{-1} = 1$, ed esiste solo se $a \neq 0$. Con le matrici quadrate la parte dell'$1$ la fa l'identità $I$.

> [!abstract] Matrice inversa
> L'*inversa* di una matrice quadrata $A$ è la matrice $A^{-1}$ tale che
> $$
> A \cdot A^{-1} = A^{-1} \cdot A = I.
> $$
> Esiste se e solo se $\det A \neq 0$ (la matrice si dice allora *invertibile*). Per una 2×2:
> $$
> \begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
> $$

La formula per la 2×2 si ricorda così: si scambiano i due elementi della diagonale principale, si cambia segno agli altri due, e si divide tutto per il determinante. Si capisce anche perché il determinante non deve essere zero: altrimenti si dividerebbe per zero.

> [!example] Esempio
> $A = \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix}$, con $\det A = -2$.
> $$
> A^{-1} = \frac{1}{-2}\begin{pmatrix} 0 & -2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ \frac12 & -\frac12 \end{pmatrix}
> $$
> Verifica: $A \cdot A^{-1} = \begin{pmatrix} 1 \cdot 0 + 2 \cdot \frac12 & 1 \cdot 1 + 2 \cdot \left(-\frac12\right) \\ 1 \cdot 0 + 0 & 1 \cdot 1 + 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$.

Le matrici del prodotto nullo, $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ e $\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$, hanno entrambe determinante $0$: non sono invertibili. Non è un caso: se $A$ fosse invertibile, da $A \cdot B = \Omega$ si potrebbe moltiplicare a sinistra per $A^{-1}$ e ottenere $B = \Omega$.

### I sistemi lineari 2×2 e la regola di Cramer

Un sistema di due equazioni di primo grado in due incognite,

$$
\begin{cases} a x + b y = e \\ c x + d y = f \end{cases}
$$

si può scrivere con le matrici come $\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} e \\ f \end{pmatrix}$: facendo il prodotto riga per colonna si ritrovano proprio le due equazioni.

La matrice $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ si chiama *matrice dei coefficienti*. Il suo determinante dice se il sistema ha una e una sola soluzione.

> [!abstract] Regola di Cramer (sistemi 2×2)
> Se $D = \begin{vmatrix} a & b \\ c & d \end{vmatrix} \neq 0$, il sistema ha una sola soluzione:
> $$
> x = \frac{D_x}{D} = \frac{\begin{vmatrix} e & b \\ f & d \end{vmatrix}}{D}, \qquad y = \frac{D_y}{D} = \frac{\begin{vmatrix} a & e \\ c & f \end{vmatrix}}{D}.
> $$
> $D_x$ si ottiene sostituendo la colonna delle $x$ con i termini noti; $D_y$ sostituendo la colonna delle $y$.

> [!example] Esempio
> $$
> \begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}
> $$
> 1. $D = \begin{vmatrix} 2 & 1 \\ 1 & -1 \end{vmatrix} = -2 - 1 = -3 \neq 0$: c'è una sola soluzione.
> 2. $D_x = \begin{vmatrix} 5 & 1 \\ 1 & -1 \end{vmatrix} = -5 - 1 = -6$, quindi $x = \frac{-6}{-3} = 2$.
> 3. $D_y = \begin{vmatrix} 2 & 5 \\ 1 & 1 \end{vmatrix} = 2 - 5 = -3$, quindi $y = \frac{-3}{-3} = 1$.
> 4. Verifica: $2 \cdot 2 + 1 = 5$ e $2 - 1 = 1$.

Il significato geometrico si lega a [[02-retta-e-circonferenza]]: ogni equazione è una retta, e la soluzione è il loro punto d'intersezione. $D = 0$ vuol dire che le righe $(a, b)$ e $(c, d)$ sono proporzionali, cioè che le due rette hanno la stessa pendenza: sono parallele (nessuna soluzione) o coincidenti (infinite soluzioni).

## Collegamenti

Le matrici riprendono quasi tutto quello che si è visto in [[03-i-vettori]]. La somma di matrici e il prodotto per uno scalare sono le stesse operazioni dei vettori, fatte su una tabella invece che su una riga; ogni elemento del prodotto riga per colonna è un prodotto scalare tra una riga e una colonna. Il determinante era già comparso lì: il determinante 2×2 è l'area orientata del parallelogramma, il determinante simbolico con $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ dà il prodotto vettoriale, e il determinante 3×3 è il prodotto triplo, cioè il volume del parallelepipedo e il criterio di complanarità.

Il prodotto non commutativo e il prodotto nullo tra matrici non nulle mostrano che le regole dei numeri, usate in [[01-equazioni-e-disequazioni]] (come la legge di annullamento del prodotto), non si possono trasportare alle matrici senza controllare. La regola di Cramer è un altro modo di risolvere i sistemi di due equazioni, e il caso $D = 0$ corrisponde a due rette parallele o coincidenti, come in [[02-retta-e-circonferenza]].

Le matrici sono anche il linguaggio delle trasformazioni geometriche: rotazioni, simmetrie, ingrandimenti del piano e dello spazio si scrivono come prodotti di una matrice per un vettore, e il determinante dice di quanto la trasformazione moltiplica le aree o i volumi. È ciò che fanno, senza mostrarlo, i programmi di disegno e di modellazione 3D che si usano in Architettura; e le proiezioni della Geometria descrittiva, viste come trasformazioni dello spazio sul foglio, hanno determinante zero perché "schiacciano" i volumi su un piano.

## Per approfondire

- [[Giuffrida Ragusa - Determinanti_compressed.pdf]] (Giuffrida, Ragusa, capitolo 3, "Sistemi lineari", paragrafo 3.1): determinante delle matrici di ordine 1, 2, 3 e i due schemi della regola di Sarrus a pagina 144; proprietà del determinante (D1-D8, tra cui trasposta, riga nulla, scambio di righe) alle pagine 146-149; complemento algebrico (definizione 3.1.11) e sviluppo di Laplace (teorema 3.1.12) a pagina 153, con esempi svolti a pagina 154; teorema di Binet a pagina 155. Le pagine sono quelle stampate sul libro.
- [[esercizi prodotto vettoriale e prodotto triplo.pdf]]: il foglio del professore con le formule dei determinanti 2×2 e 3×3 e gli esercizi su prodotto vettoriale e prodotto triplo.
- [[Capitolo_Vettori.pdf]] (Stewart, capitolo 2): i determinanti 2×2 e 3×3 e il determinante simbolico per il prodotto vettoriale, a pagina 82.
- Le foto della lavagna in `materiale/` (da `lavagna-04` a `lavagna-08`): somma, prodotto riga per colonna, determinante, Sarrus, complementi algebrici.
- I tuoi appunti in `materiale/`: `appunti-nadia-04.jpeg` (15 ottobre: prodotto, matrice nulla, diagonale, trasposta e sue proprietà) e `appunti-nadia-05.jpeg` (Sarrus sulla matrice, complemento algebrico, teorema di Laplace).
