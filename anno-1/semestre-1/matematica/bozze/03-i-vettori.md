---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# I vettori

Un vettore è una freccia: ha una lunghezza, una direzione e un verso, e serve a descrivere tutto ciò che non basta dire "quanto", ma bisogna dire anche "verso dove" (uno spostamento, una forza, il lato di una figura). In questa pagina si parte dalla freccia, si arriva a scriverla con i numeri (le componenti) e si impara a fare i conti: somma, prodotto per un numero, lunghezza. Poi vengono i tre "prodotti" che il professore usa negli esercizi: il prodotto scalare, che misura gli angoli e dice quando due vettori sono perpendicolari; il prodotto vettoriale, che dà un vettore perpendicolare a due vettori e misura le aree; il prodotto triplo, che misura i volumi. Tutti gli esempi svolti vengono dai due fogli di esercizi del professore.

> [!info] Note collegate
> Teoria: [[01-equazioni-e-disequazioni]] · [[02-retta-e-circonferenza]] · [[04-le-funzioni]] · [[05-funzioni-elementari]] · Ripasso: [[00-ripasso-esonero-1]]

## PUNTI E VETTORI

### La freccia: modulo, direzione e verso

Un punto è una posizione: nel piano si indica con due coordinate, $A = (1, 1)$; nello spazio con tre, $A = (1, 1, 2)$.

Un *vettore* invece è uno spostamento: dice di quanto e in che modo ci si muove. Si disegna come una freccia (un *segmento orientato*) che va da un punto iniziale, la *coda*, a un punto finale, la *punta*. La freccia da $A$ a $B$ si scrive $\overrightarrow{AB}$. I vettori si indicano anche con una lettera in grassetto, $\mathbf{u}$, $\mathbf{v}$, $\mathbf{a}$ (scrivendo a mano si mette una freccetta sopra la lettera: $\vec{u}$).

Una freccia è determinata da tre informazioni:

1. il *modulo* (o *norma*, o *intensità*): la lunghezza della freccia;
2. la *direzione*: la retta su cui giace la freccia (o qualunque retta parallela a essa);
3. il *verso*: su quella retta, da che parte punta la freccia. Ogni direzione ha due versi.

> [!abstract] Definizione: vettori uguali
> Due frecce rappresentano lo stesso vettore se hanno lo stesso modulo, la stessa direzione e lo stesso verso, anche se partono da punti diversi.

Questo è il punto che all'inizio sorprende di più: un vettore non "abita" in un posto preciso. Se si trasla una freccia (la si sposta parallelamente a se stessa, senza ruotarla e senza allungarla), si ottiene lo stesso vettore. Nella figura, $\overrightarrow{AB}$ e $\overrightarrow{CD}$ sono lo stesso vettore $\mathbf{v}$.

![[03-vettore-freccia.svg|560]]

Proprio perché si può spostare, conviene quasi sempre disegnare un vettore con la coda nell'origine $O$ degli assi. È questa scelta che permette di descriverlo con i numeri.

### Le componenti nel piano e nello spazio

Se la coda del vettore $\mathbf{u}$ sta nell'origine, la sua punta è un punto del piano, con due coordinate. Queste due coordinate si chiamano *componenti* del vettore e si scrive

$$
\mathbf{u} = (u_1, u_2).
$$

La prima componente $u_1$ dice di quanto ci si sposta in orizzontale (lungo l'asse $x$), la seconda $u_2$ di quanto ci si sposta in verticale (lungo l'asse $y$). Il segno conta: una componente negativa vuol dire spostarsi verso sinistra o verso il basso.

![[03-componenti-piano.svg|460]]

Nella figura $\mathbf{u} = (4, 3)$: quattro passi a destra e tre in alto. Le due componenti e la freccia formano un triangolo rettangolo, e questo tornerà utile per calcolare la lunghezza.

Nello spazio si aggiunge la terza direzione, l'asse $z$ (l'altezza), e il vettore ha tre componenti:

$$
\mathbf{u} = (u_1, u_2, u_3).
$$

Si immagina una scatola con uno spigolo nell'origine: le tre componenti sono le misure dei tre spigoli lungo gli assi, e il vettore è la diagonale della scatola, dall'origine al vertice opposto.

![[03-componenti-spazio.svg|500]]

Gli assi nello spazio si disegnano sempre nello stesso modo: $x$ verso chi guarda (obliquo, in basso a sinistra), $y$ verso destra, $z$ verso l'alto. Questa disposizione si chiama *destrorsa* e servirà per il prodotto vettoriale.

Il piano si indica con $\mathbb{R}^2$ (le coppie di numeri reali) e lo spazio con $\mathbb{R}^3$ (le terne): "un vettore di $\mathbb{R}^3$" vuol dire semplicemente un vettore con tre componenti.

### Il vettore tra due punti

Se la freccia non parte dall'origine ma da un punto $A$ e arriva a un punto $B$, le sue componenti si trovano sottraendo le coordinate: punta meno coda.

> [!abstract] Vettore da $A$ a $B$
> Se $A = (a_1, a_2)$ e $B = (b_1, b_2)$, allora
> $$
> \overrightarrow{AB} = B - A = (b_1 - a_1,\ b_2 - a_2).
> $$
> Nello spazio si fa lo stesso con tre coordinate.

Il perché è semplice: le componenti dicono di quanto ci si sposta per andare da $A$ a $B$, e lo spostamento orizzontale è la differenza delle ascisse, quello verticale la differenza delle ordinate.

![[03-vettore-tra-punti.svg|460]]

> [!example] Esempio (esercizio 14 del foglio sui vettori)
> Siano $A = (1, -1)$, $B = (5, 1)$, $C = (2, 4)$.
>
> 1. $\overrightarrow{AB} = B - A = (5-1,\ 1-(-1)) = (4, 2)$.
> 2. $\overrightarrow{AC} = C - A = (2-1,\ 4-(-1)) = (1, 5)$.
> 3. Il punto medio di $AB$ si trova facendo la media delle coordinate: $M = \left(\frac{1+5}{2}, \frac{-1+1}{2}\right) = (3, 0)$.
> 4. Si cerca $D$ tale che $A, B, D, C$, in quest'ordine, siano i vertici di un parallelogramma. In un parallelogramma i lati opposti sono lo stesso vettore: il lato $AB$ e il lato $CD$ sono uguali e con lo stesso verso, quindi $\overrightarrow{AB} = \overrightarrow{CD}$, cioè $B - A = D - C$. Da qui $D = C + (B - A) = (2, 4) + (4, 2) = (6, 6)$.
> 5. Le diagonali sono $AD$ e $BC$. Punto medio di $AD$: $\left(\frac{1+6}{2}, \frac{-1+6}{2}\right) = \left(\frac72, \frac52\right)$. Punto medio di $BC$: $\left(\frac{5+2}{2}, \frac{1+4}{2}\right) = \left(\frac72, \frac52\right)$. È lo stesso punto: le diagonali di un parallelogramma si tagliano a metà.

> [!warning] Attenzione all'ordine
> $\overrightarrow{AB}$ e $\overrightarrow{BA}$ non sono lo stesso vettore: hanno la stessa lunghezza e la stessa direzione, ma verso opposto. $\overrightarrow{BA} = A - B = -\overrightarrow{AB}$. Si fa sempre punta meno coda.

## LE OPERAZIONI CON I VETTORI

### La somma: regola punta-coda e regola del parallelogramma

Sommare due vettori vuol dire fare i due spostamenti uno dopo l'altro. Se prima ci si sposta di $\mathbf{u}$ e poi di $\mathbf{v}$, lo spostamento complessivo è $\mathbf{u} + \mathbf{v}$.

Graficamente ci sono due modi equivalenti di costruirlo.

1. Regola *punta-coda* (o del triangolo): si sposta $\mathbf{v}$ in modo che la sua coda stia sulla punta di $\mathbf{u}$; la somma è la freccia che va dalla coda di $\mathbf{u}$ alla punta di $\mathbf{v}$.
2. Regola del *parallelogramma*: si disegnano $\mathbf{u}$ e $\mathbf{v}$ con la coda nello stesso punto e si completa il parallelogramma che hanno come lati; la somma è la diagonale che parte dalla coda comune.

Le due regole danno lo stesso risultato: nel parallelogramma, il lato opposto a $\mathbf{u}$ è una copia di $\mathbf{u}$ e il lato opposto a $\mathbf{v}$ è una copia di $\mathbf{v}$, quindi la diagonale si raggiunge sia facendo "prima $\mathbf{u}$ poi $\mathbf{v}$", sia facendo "prima $\mathbf{v}$ poi $\mathbf{u}$". Questo mostra anche che $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$: l'ordine non conta.

![[03-somma.svg|680]]

Con le componenti la somma è ancora più semplice: si sommano le componenti corrispondenti, la prima con la prima e la seconda con la seconda. Infatti gli spostamenti orizzontali si sommano tra loro, e così quelli verticali.

> [!abstract] Somma in componenti
> $$
> (u_1, u_2) + (v_1, v_2) = (u_1 + v_1,\ u_2 + v_2)
> $$
> e nello spazio $(u_1, u_2, u_3) + (v_1, v_2, v_3) = (u_1 + v_1,\ u_2 + v_2,\ u_3 + v_3)$.

> [!example] Esempio (esercizio 1, prima parte)
> Siano $\mathbf{u} = (2, -1)$ e $\mathbf{v} = (-3, 4)$.
>
> $\mathbf{u} + \mathbf{v} = (2 + (-3),\ -1 + 4) = (-1, 3)$.
>
> È proprio il vettore disegnato nella figura sopra: la diagonale del parallelogramma arriva nel punto $(-1, 3)$.

### Il vettore nullo e l'opposto

Il *vettore nullo* $\mathbf{0} = (0, 0)$ (nello spazio $(0, 0, 0)$) è lo spostamento "fermo": ha lunghezza zero ed è l'unico vettore che non ha né direzione né verso. Sommato a qualunque vettore, lo lascia com'è: $\mathbf{u} + \mathbf{0} = \mathbf{u}$.

L'*opposto* di $\mathbf{u}$, scritto $-\mathbf{u}$, è il vettore che annulla $\mathbf{u}$: ha la stessa lunghezza e la stessa direzione, ma verso opposto. In componenti si cambia segno a tutte le componenti, e vale $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$: andare e tornare indietro è come stare fermi.

> [!example] Esempio (esercizio 2)
> Si cerca $\mathbf{w}$ tale che $\mathbf{w} + (5, -2) = \mathbf{0}$.
>
> $\mathbf{w}$ deve essere l'opposto di $(5, -2)$, quindi $\mathbf{w} = (-5, 2)$.
>
> Verifica: $(5, -2) + (-5, 2) = (0, 0) = \mathbf{0}$.

### La differenza

La differenza $\mathbf{u} - \mathbf{v}$ si definisce come somma con l'opposto: $\mathbf{u} - \mathbf{v} = \mathbf{u} + (-\mathbf{v})$. In componenti si sottraggono le componenti corrispondenti:

$$
(u_1, u_2) - (v_1, v_2) = (u_1 - v_1,\ u_2 - v_2).
$$

Graficamente c'è un modo comodo per vederla. Se $\mathbf{u}$ e $\mathbf{v}$ partono dallo stesso punto, $\mathbf{u} - \mathbf{v}$ è la freccia che va dalla punta di $\mathbf{v}$ alla punta di $\mathbf{u}$. Infatti partendo dalla punta di $\mathbf{v}$ e facendo $\mathbf{u} - \mathbf{v}$ si arriva a $\mathbf{v} + (\mathbf{u} - \mathbf{v}) = \mathbf{u}$. È la stessa idea di "punta meno coda" del vettore tra due punti.

![[03-differenza.svg|440]]

Nel parallelogramma costruito su $\mathbf{u}$ e $\mathbf{v}$, quindi, la somma è una diagonale e la differenza è l'altra.

### Il prodotto per uno scalare

In questo contesto un numero reale si chiama *scalare*, per distinguerlo dai vettori. Moltiplicare un vettore per uno scalare $k$ vuol dire allungarlo o accorciarlo:

- la lunghezza viene moltiplicata per $|k|$ (il valore assoluto di $k$);
- la direzione resta la stessa;
- il verso resta lo stesso se $k > 0$, si inverte se $k < 0$;
- se $k = 0$ si ottiene il vettore nullo.

In componenti si moltiplica ogni componente per $k$: $k\,(u_1, u_2) = (k u_1,\ k u_2)$. Il nome "scalare" viene proprio da qui: il numero cambia la scala del vettore.

![[03-multipli.svg|440]]

> [!example] Esempio (esercizio 1, seconda parte)
> Con $\mathbf{u} = (2, -1)$ e $\mathbf{v} = (-3, 4)$:
>
> - $\mathbf{u} - \mathbf{v} = (2 - (-3),\ -1 - 4) = (5, -5)$;
> - $2\mathbf{u} = (4, -2)$;
> - $-\frac12\mathbf{v} = \left(-\frac12 \cdot (-3),\ -\frac12 \cdot 4\right) = \left(\frac32, -2\right)$.

> [!example] Esempio (esercizio 13)
> Siano $\mathbf{u} = (1, -2, 3)$ e $\mathbf{v} = (2, 1, -1)$.
>
> 1. $2\mathbf{u} - 3\mathbf{v} = (2, -4, 6) - (6, 3, -3) = (-4, -7, 9)$.
> 2. Si cerca $\mathbf{w}$ tale che $2\mathbf{w} + \mathbf{u} = \mathbf{v}$. Si risolve come un'equazione: $2\mathbf{w} = \mathbf{v} - \mathbf{u} = (1, 3, -4)$, quindi $\mathbf{w} = \frac12 (1, 3, -4) = \left(\frac12, \frac32, -2\right)$.

### Combinazioni lineari e base standard

Mettendo insieme somma e prodotto per uno scalare si ottengono le *combinazioni lineari*.

> [!abstract] Definizione: combinazione lineare
> Una combinazione lineare dei vettori $\mathbf{u}$ e $\mathbf{v}$ è un vettore della forma
> $$
> \alpha\,\mathbf{u} + \beta\,\mathbf{v}
> $$
> dove $\alpha$ e $\beta$ sono due numeri reali (i *coefficienti*).

Nel piano ci sono due vettori speciali, lunghi 1 e diretti lungo gli assi:

$$
\mathbf{e}_1 = (1, 0), \qquad \mathbf{e}_2 = (0, 1).
$$

Si chiamano *base standard* (o base canonica). Ogni vettore del piano si scrive come loro combinazione lineare, e i coefficienti sono proprio le componenti:

$$
(u_1, u_2) = u_1\,\mathbf{e}_1 + u_2\,\mathbf{e}_2.
$$

Il motivo si vede nel disegno: per arrivare alla punta di $(u_1, u_2)$ si fanno $u_1$ passi lunghi 1 in orizzontale e $u_2$ passi lunghi 1 in verticale. Nello spazio si aggiunge $\mathbf{e}_3 = (0, 0, 1)$ e vale $(u_1, u_2, u_3) = u_1\mathbf{e}_1 + u_2\mathbf{e}_2 + u_3\mathbf{e}_3$. (Nello Stewart questi tre vettori si chiamano $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$.)

![[03-base-standard.svg|440]]

> [!example] Esempio (esercizio 3)
> $\mathbf{a} = (7, -5) = 7\,\mathbf{e}_1 - 5\,\mathbf{e}_2$.
>
> Al contrario, $3\mathbf{e}_1 - 4\mathbf{e}_2 = (3, 0) + (0, -4) = (3, -4)$.

Il problema diventa più interessante quando i due vettori non sono quelli della base standard. Allora si scrive l'uguaglianza componente per componente e si risolve un sistema.

> [!example] Esempio (esercizio 15)
> Siano $\mathbf{u} = (1, 1)$, $\mathbf{v} = (2, -1)$, $\mathbf{a} = (7, 1)$. Si cercano $\alpha$ e $\beta$ tali che $\mathbf{a} = \alpha\mathbf{u} + \beta\mathbf{v}$.
>
> 1. $\alpha(1, 1) + \beta(2, -1) = (\alpha + 2\beta,\ \alpha - \beta)$.
> 2. Uguagliando a $(7, 1)$ si ha il sistema: $\alpha + 2\beta = 7$ e $\alpha - \beta = 1$.
> 3. Sottraendo la seconda equazione dalla prima: $3\beta = 6$, quindi $\beta = 2$; poi $\alpha = 1 + \beta = 3$.
> 4. Verifica: $3(1, 1) + 2(2, -1) = (3 + 4,\ 3 - 2) = (7, 1)$.
>
> La coppia è unica perché $\mathbf{u}$ e $\mathbf{v}$ non sono paralleli: con due direzioni diverse si raggiunge ogni punto del piano in un modo solo. Se fossero paralleli, le loro combinazioni starebbero tutte su una stessa retta.

### Il parallelismo

Due vettori non nulli sono *paralleli* se hanno la stessa direzione, cioè se uno si ottiene dall'altro moltiplicandolo per un numero.

> [!abstract] Vettori paralleli
> $\mathbf{u}$ e $\mathbf{v}$ (non nulli) sono paralleli se esiste un numero $k$ tale che $\mathbf{v} = k\,\mathbf{u}$, cioè se le componenti sono proporzionali.
> - Se $k > 0$ hanno lo stesso verso.
> - Se $k < 0$ hanno verso opposto.

> [!example] Esempio (esercizio 16)
> Per quali $t$ i vettori $\mathbf{u} = (t, 2, -1)$ e $\mathbf{v} = (6, 4, -2)$ sono paralleli?
>
> 1. Si guardano le componenti che non contengono $t$: $4 = 2 \cdot 2$ e $-2 = 2 \cdot (-1)$. Quindi l'unico $k$ possibile è $k = 2$, cioè $\mathbf{v} = 2\mathbf{u}$.
> 2. Anche la prima componente deve rispettarlo: $6 = 2t$, quindi $t = 3$.
> 3. Per $t = 3$ si ha $\mathbf{v} = 2\mathbf{u}$ con $k = 2 > 0$: i due vettori hanno lo stesso verso.

## NORMA E VERSORE

### La norma

La *norma* (o modulo) di un vettore è la sua lunghezza e si scrive $\|\mathbf{u}\|$. Si calcola con il teorema di Pitagora: nel piano le componenti $u_1$ e $u_2$ sono i cateti di un triangolo rettangolo e la freccia è l'ipotenusa (si riguardi la figura con $\mathbf{u} = (4, 3)$).

> [!abstract] Norma di un vettore
> $$
> \|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2} \qquad \text{nel piano,}
> $$
> $$
> \|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2 + u_3^2} \qquad \text{nello spazio.}
> $$

Nello spazio si usa Pitagora due volte: prima nel pavimento della scatola (la diagonale della base è lunga $\sqrt{u_1^2 + u_2^2}$), poi nel triangolo verticale che ha per cateti quella diagonale e l'altezza $u_3$.

Alcune conseguenze:

- la norma non è mai negativa, ed è $0$ solo per il vettore nullo;
- $\|k\,\mathbf{u}\| = |k|\,\|\mathbf{u}\|$: raddoppiando un vettore si raddoppia la lunghezza, e cambiare il verso non la cambia;
- la *distanza* tra due punti è la norma del vettore che li unisce: $d(A, B) = \|\overrightarrow{AB}\| = \|B - A\|$. È la formula della distanza vista in [[02-retta-e-circonferenza]].

> [!example] Esempio (esercizio 4, prima parte)
> - $\|(3, 4)\| = \sqrt{9 + 16} = \sqrt{25} = 5$;
> - $\|(-5, 12)\| = \sqrt{25 + 144} = \sqrt{169} = 13$;
> - $\|(1, 2, 2)\| = \sqrt{1 + 4 + 4} = \sqrt9 = 3$.
>
> Nessuno dei tre è unitario (cioè lungo 1).

### Il versore e la normalizzazione

Un *versore* (o vettore unitario) è un vettore di norma 1. Serve a indicare una direzione e un verso senza "portarsi dietro" una lunghezza. $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ sono versori.

Da qualunque vettore non nullo si ottiene il versore con la stessa direzione e lo stesso verso dividendolo per la sua norma. Questa operazione si chiama *normalizzare*.

> [!abstract] Normalizzazione
> $$
> \text{versore di } \mathbf{u} = \frac{\mathbf{u}}{\|\mathbf{u}\|} = \frac{1}{\|\mathbf{u}\|}\,\mathbf{u}
> $$
> Funziona perché moltiplicare per il numero positivo $\frac{1}{\|\mathbf{u}\|}$ non cambia direzione e verso, e divide la lunghezza per $\|\mathbf{u}\|$: la nuova lunghezza è $\frac{\|\mathbf{u}\|}{\|\mathbf{u}\|} = 1$.

![[03-versore.svg|400]]

> [!example] Esempio (esercizio 4, seconda parte)
> Normalizzare $(3, 4)$. La norma è $5$, quindi il versore è
> $$
> \frac{1}{5}(3, 4) = \left(\frac35, \frac45\right).
> $$
> Verifica: $\left(\frac35\right)^2 + \left(\frac45\right)^2 = \frac{9}{25} + \frac{16}{25} = 1$. Nella figura il versore è la freccia corta che arriva sulla circonferenza di raggio 1.

## IL PRODOTTO SCALARE

### La definizione in coordinate

Il *prodotto scalare* di due vettori è un numero: si moltiplicano le componenti corrispondenti e si sommano i risultati.

> [!abstract] Definizione: prodotto scalare (in coordinate)
> $$
> \mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 \qquad \text{nel piano,}
> $$
> $$
> \mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 \qquad \text{nello spazio.}
> $$
> Il risultato è un numero (uno scalare), non un vettore: da qui il nome.

Per esempio $(1, 2) \cdot (3, 1) = 1 \cdot 3 + 2 \cdot 1 = 5$.

> [!warning] Il prodotto scalare è un numero
> $\mathbf{u} \cdot \mathbf{v}$ non ha componenti. Quindi scritture come $(\mathbf{u} \cdot \mathbf{v}) \cdot \mathbf{w}$ (un numero "scalare" un vettore) non hanno senso, mentre $(\mathbf{u} \cdot \mathbf{v})\,\mathbf{w}$ sì: è il vettore $\mathbf{w}$ moltiplicato per il numero $\mathbf{u} \cdot \mathbf{v}$.

### La definizione geometrica

Lo stesso numero si può calcolare guardando la figura invece delle componenti. Si disegnano $\mathbf{u}$ e $\mathbf{v}$ con la coda nello stesso punto e si chiama $\theta$ l'angolo tra loro (quello compreso tra $0$ e $\pi$, cioè tra $0°$ e $180°$).

> [!abstract] Definizione geometrica del prodotto scalare
> $$
> \mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta
> $$
> Se uno dei due vettori è nullo, il prodotto scalare vale $0$.

Le due definizioni danno sempre lo stesso numero: è questo il fatto importante, perché permette di passare dai numeri agli angoli e viceversa.

### Perché le due definizioni coincidono

Il ponte tra le due definizioni è il *teorema del coseno* (o di Carnot), che generalizza Pitagora ai triangoli qualunque. Si guarda il triangolo che ha per lati $\mathbf{u}$, $\mathbf{v}$ e la differenza $\mathbf{u} - \mathbf{v}$ (che va dalla punta di $\mathbf{v}$ alla punta di $\mathbf{u}$).

![[03-teorema-coseno.svg|400]]

1. Il teorema del coseno dice che il lato opposto all'angolo $\theta$ misura:
$$
\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\,\|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta.
$$
2. Lo stesso lato si può calcolare con le componenti (nel piano, per semplicità):
$$
\|\mathbf{u} - \mathbf{v}\|^2 = (u_1 - v_1)^2 + (u_2 - v_2)^2 = (u_1^2 + u_2^2) + (v_1^2 + v_2^2) - 2(u_1 v_1 + u_2 v_2).
$$
3. Cioè $\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2(u_1 v_1 + u_2 v_2)$.
4. Confrontando le due espressioni, le parti $\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$ sono uguali, quindi devono essere uguali anche le parti rimaste: $u_1 v_1 + u_2 v_2 = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$.

Nello spazio il conto è identico, con una componente in più.

### L'angolo tra due vettori

Dalla definizione geometrica si ricava il coseno dell'angolo, e quindi l'angolo:

> [!abstract] Angolo tra due vettori non nulli
> $$
> \cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}, \qquad \theta = \arccos\left(\frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}\right)
> $$
> con $0 \leq \theta \leq \pi$.

L'arcocoseno, $\arccos$, è la funzione che "torna indietro" dal coseno all'angolo (è la funzione inversa del coseno, vedi [[04-le-funzioni]] e [[05-funzioni-elementari]]). Il professore accetta il risultato in forma esatta, per esempio $\arccos\left(-\frac{1}{\sqrt{78}}\right)$, con un'approssimazione in gradi.

![[03-angolo.svg|420]]

> [!example] Esempio (esercizio 5)
> Siano $\mathbf{u} = (1, 2)$ e $\mathbf{v} = (3, 1)$.
>
> 1. $\mathbf{u} \cdot \mathbf{v} = 1 \cdot 3 + 2 \cdot 1 = 5$.
> 2. $\|\mathbf{u}\| = \sqrt{1 + 4} = \sqrt5$ e $\|\mathbf{v}\| = \sqrt{9 + 1} = \sqrt{10}$.
> 3. $\cos\theta = \dfrac{5}{\sqrt5\,\sqrt{10}} = \dfrac{5}{\sqrt{50}} = \dfrac{5}{5\sqrt2} = \dfrac{1}{\sqrt2}$.
> 4. L'angolo con coseno $\frac{1}{\sqrt2} = \frac{\sqrt2}{2}$ è $\theta = \frac{\pi}{4}$, cioè $45°$, come nella figura.

> [!example] Esempio (esercizio 9, nello spazio)
> Siano $\mathbf{a} = (1, 2, -1)$ e $\mathbf{b} = (2, 0, 3)$.
>
> 1. $\mathbf{a} \cdot \mathbf{b} = 2 + 0 - 3 = -1$.
> 2. $\|\mathbf{a}\| = \sqrt{1 + 4 + 1} = \sqrt6$ e $\|\mathbf{b}\| = \sqrt{4 + 0 + 9} = \sqrt{13}$.
> 3. $\cos\theta = \dfrac{-1}{\sqrt6\,\sqrt{13}} = -\dfrac{1}{\sqrt{78}}$, quindi $\theta = \arccos\left(-\frac{1}{\sqrt{78}}\right) \approx 96{,}5°$.
>
> Il coseno è negativo, quindi l'angolo è (di poco) ottuso.

> [!example] Esempio (esercizio 10, problema geometrico)
> Siano $A = (1, 1)$, $B = (5, 2)$, $C = (3, 6)$. L'angolo $\widehat{BAC}$ del triangolo è l'angolo tra i vettori che partono da $A$:
>
> 1. $\overrightarrow{AB} = (4, 1)$ e $\overrightarrow{AC} = (2, 5)$.
> 2. $\overrightarrow{AB} \cdot \overrightarrow{AC} = 8 + 5 = 13$.
> 3. $\|\overrightarrow{AB}\| = \sqrt{17}$ e $\|\overrightarrow{AC}\| = \sqrt{29}$.
> 4. $\cos\widehat{BAC} = \dfrac{13}{\sqrt{17}\,\sqrt{29}} = \dfrac{13}{\sqrt{493}}$, quindi $\widehat{BAC} = \arccos\dfrac{13}{\sqrt{493}} \approx 54{,}2°$.
> 5. Il prodotto scalare è positivo, quindi l'angolo in $A$ è acuto: il triangolo è acutangolo in $A$.

> [!warning] I vettori devono partire dallo stesso punto
> Per l'angolo in $A$ si usano $\overrightarrow{AB}$ e $\overrightarrow{AC}$, entrambi con la coda in $A$. Usando per esempio $\overrightarrow{AB}$ e $\overrightarrow{CA}$ si otterrebbe l'angolo supplementare ($180°$ meno quello giusto).

### Il segno del prodotto scalare e l'ortogonalità

Nella formula $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta$ le due norme sono positive, quindi il segno del prodotto scalare è il segno di $\cos\theta$. E il coseno è positivo per gli angoli acuti, zero per l'angolo retto, negativo per gli angoli ottusi.

> [!abstract] Il segno dice com'è l'angolo
> Per $\mathbf{u}$, $\mathbf{v}$ non nulli:
> - $\mathbf{u} \cdot \mathbf{v} > 0$: angolo acuto ($0 \leq \theta < 90°$);
> - $\mathbf{u} \cdot \mathbf{v} = 0$: angolo retto ($\theta = 90°$), i vettori sono *ortogonali* (perpendicolari);
> - $\mathbf{u} \cdot \mathbf{v} < 0$: angolo ottuso ($90° < \theta \leq 180°$).

![[03-segno-prodotto-scalare.svg|620]]

Questo è il modo più rapido per riconoscere due vettori perpendicolari: non serve disegnare né calcolare angoli, basta un prodotto scalare. Per convenzione il vettore nullo si considera ortogonale a tutti.

> [!example] Esempio (esercizi 6 e 7)
> Ortogonalità (esercizio 6):
> - $(1, 2) \cdot (2, -1) = 2 - 2 = 0$: ortogonali;
> - $(3, 4) \cdot (-4, 3) = -12 + 12 = 0$: ortogonali;
> - $(1, 1, 1) \cdot (1, -1, 0) = 1 - 1 + 0 = 0$: ortogonali.
>
> Segno, senza calcolare l'angolo (esercizio 7):
> - $(2, 1) \cdot (1, 3) = 2 + 3 = 5 > 0$: angolo acuto;
> - $(1, 0) \cdot (-2, 1) = -2 < 0$: angolo ottuso;
> - $(2, -1) \cdot (1, 2) = 2 - 2 = 0$: angolo retto.

Un trucco utile nel piano: il vettore $(a, b)$ è sempre ortogonale a $(-b, a)$ e a $(b, -a)$, perché $a \cdot (-b) + b \cdot a = 0$. Basta scambiare le componenti e cambiare un segno.

> [!example] Esempio (esercizio 18, con parametro)
> Siano $\mathbf{u} = (t, 1)$ e $\mathbf{v} = (2, -1)$. Il prodotto scalare è $\mathbf{u} \cdot \mathbf{v} = 2t - 1$.
>
> - Angolo acuto se $2t - 1 > 0$, cioè $t > \frac12$;
> - angolo retto se $t = \frac12$;
> - angolo ottuso se $t < \frac12$.
>
> Il problema sui vettori diventa una disequazione di primo grado (vedi [[01-equazioni-e-disequazioni]]).

> [!example] Esempio (esercizio 17, versori ortogonali)
> Dato $\mathbf{u} = (3, -4)$, si cercano i vettori unitari ortogonali a $\mathbf{u}$.
>
> 1. Con il trucco di prima, $(4, 3)$ è ortogonale a $\mathbf{u}$: $3 \cdot 4 + (-4) \cdot 3 = 0$.
> 2. Tutti i vettori ortogonali a $\mathbf{u}$ sono i multipli di $(4, 3)$.
> 3. $\|(4, 3)\| = 5$, quindi i versori sono $\left(\frac45, \frac35\right)$ e il suo opposto $\left(-\frac45, -\frac35\right)$. Sono due, uno per ciascun verso.

> [!example] Esempio (esercizio 19, ortogonalità nello spazio)
> Si cercano i vettori $\mathbf{w} = (x, y, z)$ ortogonali sia a $(1, 1, 0)$ sia a $(0, 1, 1)$.
>
> 1. $\mathbf{w} \cdot (1, 1, 0) = x + y = 0$, quindi $y = -x$.
> 2. $\mathbf{w} \cdot (0, 1, 1) = y + z = 0$, quindi $z = -y = x$.
> 3. Quindi $\mathbf{w} = (x, -x, x) = x\,(1, -1, 1)$, con $x$ qualunque: tutti i multipli di $(1, -1, 1)$.
> 4. $\|(1, -1, 1)\| = \sqrt3$, quindi quelli di norma $\sqrt3$ sono $(1, -1, 1)$ e $(-1, 1, -1)$.

> [!example] Esempio (esercizio 20, un angolo assegnato)
> Per quali $t$ i vettori $\mathbf{u} = (1, t)$ e $\mathbf{v} = (1, 0)$ formano un angolo di $60°$?
>
> 1. $\mathbf{u} \cdot \mathbf{v} = 1$, $\|\mathbf{u}\| = \sqrt{1 + t^2}$, $\|\mathbf{v}\| = 1$.
> 2. Serve $\cos\theta = \cos 60° = \frac12$, quindi $\dfrac{1}{\sqrt{1 + t^2}} = \dfrac12$.
> 3. $\sqrt{1 + t^2} = 2$, cioè $1 + t^2 = 4$, $t^2 = 3$, $t = \pm\sqrt3$.
> 4. Le soluzioni sono $(1, \sqrt3)$ e $(1, -\sqrt3)$: due frecce simmetriche rispetto all'asse $x$, una sopra e una sotto, entrambe a $60°$ da $\mathbf{v}$.

### Le proprietà del prodotto scalare

Il prodotto scalare si comporta in gran parte come il prodotto tra numeri:

- è commutativo: $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$;
- è distributivo: $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$;
- i numeri si portano fuori: $(k\,\mathbf{u}) \cdot \mathbf{v} = k\,(\mathbf{u} \cdot \mathbf{v})$.

La proprietà più usata lega il prodotto scalare alla norma. Facendo il prodotto scalare di un vettore con se stesso si ottiene $u_1^2 + u_2^2$, che è il quadrato della lunghezza (oppure, con la formula geometrica, l'angolo è $0$ e $\cos 0 = 1$).

> [!abstract] Prodotto scalare e norma
> $$
> \mathbf{u} \cdot \mathbf{u} = \|\mathbf{u}\|^2
> $$

Grazie a questa proprietà e alla distributività, la norma di una somma si sviluppa come il quadrato di un binomio:

$$
\|\mathbf{u} + \mathbf{v}\|^2 = (\mathbf{u} + \mathbf{v}) \cdot (\mathbf{u} + \mathbf{v}) = \|\mathbf{u}\|^2 + 2\,\mathbf{u} \cdot \mathbf{v} + \|\mathbf{v}\|^2.
$$

Allo stesso modo $\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 - 2\,\mathbf{u} \cdot \mathbf{v} + \|\mathbf{v}\|^2$.

Se $\mathbf{u}$ e $\mathbf{v}$ sono ortogonali, il termine di mezzo è zero e resta il teorema di Pitagora scritto con i vettori.

> [!abstract] Teorema di Pitagora in forma vettoriale
> Se $\mathbf{u} \cdot \mathbf{v} = 0$, allora
> $$
> \|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2.
> $$
> Infatti $\mathbf{u}$, $\mathbf{v}$ e $\mathbf{u} + \mathbf{v}$ formano un triangolo rettangolo: $\mathbf{u}$ e $\mathbf{v}$ sono i cateti, $\mathbf{u} + \mathbf{v}$ l'ipotenusa.

> [!example] Esempio (esercizio 11)
> $\mathbf{u}$ e $\mathbf{v}$ sono ortogonali, con $\|\mathbf{u}\| = 6$ e $\|\mathbf{v}\| = 8$.
>
> $\|\mathbf{u} + \mathbf{v}\|^2 = 36 + 64 = 100$, quindi $\|\mathbf{u} + \mathbf{v}\| = 10$.
>
> Geometricamente è il rettangolo di lati 6 e 8: la sua diagonale è lunga 10.

> [!example] Esempio (esercizio 23, calcoli senza coordinate)
> $\|\mathbf{u}\| = 3$, $\|\mathbf{v}\| = 4$, $\mathbf{u} \cdot \mathbf{v} = 6$.
>
> 1. Angolo: $\cos\theta = \frac{6}{3 \cdot 4} = \frac12$, quindi $\theta = 60°$.
> 2. $\|\mathbf{u} + \mathbf{v}\|^2 = 9 + 2 \cdot 6 + 16 = 37$, quindi $\|\mathbf{u} + \mathbf{v}\| = \sqrt{37}$.
> 3. $\|\mathbf{u} - \mathbf{v}\|^2 = 9 - 2 \cdot 6 + 16 = 13$, quindi $\|\mathbf{u} - \mathbf{v}\| = \sqrt{13}$.
> 4. $(2\mathbf{u} - \mathbf{v}) \cdot \mathbf{v} = 2\,\mathbf{u} \cdot \mathbf{v} - \mathbf{v} \cdot \mathbf{v} = 12 - 16 = -4$.

> [!example] Esempio (esercizio 24, diagonali del rombo)
> 1. Sviluppando: $(\mathbf{u} + \mathbf{v}) \cdot (\mathbf{u} - \mathbf{v}) = \mathbf{u} \cdot \mathbf{u} - \mathbf{u} \cdot \mathbf{v} + \mathbf{v} \cdot \mathbf{u} - \mathbf{v} \cdot \mathbf{v} = \|\mathbf{u}\|^2 - \|\mathbf{v}\|^2$ (i termini di mezzo si cancellano perché il prodotto scalare è commutativo).
> 2. Quindi $\mathbf{u} + \mathbf{v}$ e $\mathbf{u} - \mathbf{v}$ sono ortogonali se e solo se $\|\mathbf{u}\|^2 = \|\mathbf{v}\|^2$, cioè $\|\mathbf{u}\| = \|\mathbf{v}\|$.
> 3. Significato: $\mathbf{u} + \mathbf{v}$ e $\mathbf{u} - \mathbf{v}$ sono le due diagonali del parallelogramma di lati $\mathbf{u}$ e $\mathbf{v}$. Se i lati sono uguali il parallelogramma è un rombo: le diagonali di un rombo sono perpendicolari (e un parallelogramma con le diagonali perpendicolari è un rombo).

> [!warning] Vero o falso (esercizio 12)
> - "Se $\mathbf{u} \cdot \mathbf{v} = 0$, uno dei due vettori è nullo": falso. Per esempio $(1, 0) \cdot (0, 1) = 0$, e nessuno dei due è nullo: sono ortogonali. Con i numeri un prodotto zero vuol dire un fattore zero; con il prodotto scalare no.
> - "$\mathbf{u} \cdot \mathbf{u} = \|\mathbf{u}\|^2$": vero (vedi sopra).
> - "Se $\mathbf{u} \cdot \mathbf{v} < 0$, l'angolo è ottuso": vero, perché il segno è quello di $\cos\theta$.
> - "$\|\mathbf{u} + \mathbf{v}\| = \|\mathbf{u}\| + \|\mathbf{v}\|$ sempre": falso. Vale solo se i due vettori sono paralleli e con lo stesso verso (o uno è nullo). Per esempio $\|(1, 0) + (0, 1)\| = \sqrt2$, mentre $1 + 1 = 2$. In generale vale solo $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$ (*disuguaglianza triangolare*: in un triangolo un lato è più corto della somma degli altri due).

### Proiezione scalare e proiezione vettoriale

Proiettare $\mathbf{u}$ sulla direzione di $\mathbf{v}$ vuol dire trovare "l'ombra" di $\mathbf{u}$ sulla retta di $\mathbf{v}$, come se una luce cadesse perpendicolarmente su quella retta. Dalla punta di $\mathbf{u}$ si abbassa la perpendicolare alla retta di $\mathbf{v}$: il piede della perpendicolare individua la proiezione.

![[03-proiezione.svg|700]]

Si distinguono due cose.

1. La *proiezione scalare* è un numero: la lunghezza dell'ombra, con il segno. Nel triangolo rettangolo della figura, l'ombra è il cateto adiacente all'angolo $\theta$, quindi misura $\|\mathbf{u}\|\cos\theta$. Usando la definizione geometrica del prodotto scalare, $\|\mathbf{u}\|\cos\theta = \dfrac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}$. È positiva se l'angolo è acuto e negativa se è ottuso (l'ombra cade dalla parte opposta a $\mathbf{v}$).
2. La *proiezione vettoriale* $\mathbf{p}$ è il vettore-ombra: ha per lunghezza (con il segno) la proiezione scalare e per direzione quella di $\mathbf{v}$. Si ottiene quindi moltiplicando la proiezione scalare per il versore di $\mathbf{v}$.

> [!abstract] Proiezione di $\mathbf{u}$ sulla direzione di $\mathbf{v}$
> $$
> \text{proiezione scalare} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}
> $$
> $$
> \mathbf{p} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|} \cdot \frac{\mathbf{v}}{\|\mathbf{v}\|} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\,\mathbf{v}
> $$
> Nello Stewart si scrivono $\mathrm{comp}_{\mathbf{v}}\,\mathbf{u}$ e $\mathrm{proj}_{\mathbf{v}}\,\mathbf{u}$.

Il pezzo che avanza, $\mathbf{q} = \mathbf{u} - \mathbf{p}$, è il cateto verticale del triangolo, ed è perpendicolare a $\mathbf{v}$. Così $\mathbf{u}$ si spezza in due pezzi:

> [!abstract] Scomposizione di un vettore
> $$
> \mathbf{u} = \mathbf{p} + \mathbf{q}
> $$
> con $\mathbf{p}$ parallelo a $\mathbf{v}$ e $\mathbf{q}$ ortogonale a $\mathbf{v}$ ($\mathbf{q} \cdot \mathbf{v} = 0$). Per Pitagora, $\|\mathbf{u}\|^2 = \|\mathbf{p}\|^2 + \|\mathbf{q}\|^2$.

> [!example] Esempio (esercizio 8)
> $\mathbf{u} = (4, 2)$, $\mathbf{v} = (1, 0)$.
>
> 1. $\mathbf{u} \cdot \mathbf{v} = 4$, $\|\mathbf{v}\| = 1$.
> 2. Proiezione scalare: $\frac{4}{1} = 4$. Proiezione vettoriale: $\mathbf{p} = \frac{4}{1}(1, 0) = (4, 0)$.
> 3. Interpretazione: $\mathbf{v}$ è il versore dell'asse $x$, quindi proiettare su $\mathbf{v}$ vuol dire tenere solo la parte orizzontale di $\mathbf{u}$. L'ombra di $(4, 2)$ sull'asse $x$ è $(4, 0)$. Si noti che $\mathbf{p}$ è più lungo di $\mathbf{v}$: la proiezione dipende dalla direzione di $\mathbf{v}$, non dalla sua lunghezza.

> [!example] Esempio (esercizio 21, proiezione e scomposizione)
> $\mathbf{u} = (3, 1)$, $\mathbf{v} = (1, 2)$.
>
> 1. $\mathbf{u} \cdot \mathbf{v} = 3 + 2 = 5$ e $\|\mathbf{v}\| = \sqrt5$, quindi $\|\mathbf{v}\|^2 = 5$.
> 2. Proiezione scalare: $\frac{5}{\sqrt5} = \sqrt5$.
> 3. Proiezione vettoriale: $\mathbf{p} = \frac55(1, 2) = (1, 2)$. (Qui per caso $\mathbf{p}$ coincide con $\mathbf{v}$.)
> 4. $\mathbf{q} = \mathbf{u} - \mathbf{p} = (3, 1) - (1, 2) = (2, -1)$, e $\mathbf{q} \cdot \mathbf{v} = 2 - 2 = 0$: è davvero ortogonale.
> 5. Verifica di Pitagora: $\|\mathbf{u}\|^2 = 9 + 1 = 10$, $\|\mathbf{p}\|^2 + \|\mathbf{q}\|^2 = 5 + 5 = 10$.

La stessa idea serve a calcolare la distanza di un punto da una retta, che è la lunghezza del segmento perpendicolare.

> [!example] Esempio (esercizio 22, distanza di un punto da una retta)
> $P = (4, 1)$ e la retta $r$: $X = A + s(1, 2)$ con $A = (1, 0)$, cioè i punti $(1 + s,\ 2s)$ al variare di $s$.
>
> 1. Un punto generico della retta è $H = (1 + s,\ 2s)$, e $\overrightarrow{HP} = P - H = (3 - s,\ 1 - 2s)$.
> 2. Il piede della perpendicolare è il punto $H$ per cui $\overrightarrow{HP}$ è ortogonale alla direzione $(1, 2)$ della retta: $(3 - s) \cdot 1 + (1 - 2s) \cdot 2 = 5 - 5s = 0$, quindi $s = 1$.
> 3. $H = (2, 2)$ e $\overrightarrow{HP} = (2, -1)$.
> 4. La distanza è $\|\overrightarrow{HP}\| = \sqrt{4 + 1} = \sqrt5$.

## DETERMINANTI, PRODOTTO VETTORIALE E PRODOTTO TRIPLO

### Il determinante 2×2 e l'area orientata

Un *determinante* è un numero che si calcola a partire da una tabella quadrata di numeri (una *matrice*). Per una tabella 2×2 si fa il prodotto della diagonale principale meno il prodotto dell'altra diagonale:

> [!abstract] Determinante 2×2
> $$
> \det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
> $$

Per esempio $\begin{vmatrix} 4 & 1 \\ 2 & 3 \end{vmatrix} = 4 \cdot 3 - 1 \cdot 2 = 10$.

Il determinante ha un significato geometrico preciso. Se nelle righe si mettono le componenti di due vettori del piano $\mathbf{u} = (u_1, u_2)$ e $\mathbf{v} = (v_1, v_2)$, si ottiene

$$
\begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix} = u_1 v_2 - u_2 v_1
$$

e questo numero è l'*area orientata* del parallelogramma costruito su $\mathbf{u}$ e $\mathbf{v}$:

- il valore assoluto $|u_1 v_2 - u_2 v_1|$ è l'area del parallelogramma;
- il segno dice il verso di rotazione: è positivo se per andare da $\mathbf{u}$ a $\mathbf{v}$ (con l'angolo minore di $180°$) si gira in senso antiorario, negativo se si gira in senso orario;
- è zero se e solo se $\mathbf{u}$ e $\mathbf{v}$ sono paralleli (il parallelogramma è "schiacciato" e non ha area).

Il perché dell'area si vedrà tra poco con il prodotto vettoriale.

![[03-area-orientata.svg|440]]

> [!example] Esempio (esercizio 6 del foglio sul prodotto vettoriale)
> $\mathbf{u} = (4, 1)$, $\mathbf{v} = (2, 3)$.
>
> 1. $u_1 v_2 - u_2 v_1 = 4 \cdot 3 - 1 \cdot 2 = 12 - 2 = 10$.
> 2. Il valore assoluto, $10$, è l'area del parallelogramma di lati $\mathbf{u}$ e $\mathbf{v}$.
> 3. Il segno è positivo: per sovrapporre $\mathbf{u}$ a $\mathbf{v}$ si ruota in senso antiorario (nella figura $\mathbf{v}$ è "più in alto" di $\mathbf{u}$). Scambiando i due vettori si otterrebbe $-10$: stessa area, verso di rotazione opposto.

### Il determinante 3×3

Il determinante di una tabella 3×3 si riporta a tre determinanti 2×2 (*sviluppo lungo la prima riga*, o regola di Laplace):

> [!abstract] Determinante 3×3
> $$
> \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix} = a_1 \begin{vmatrix} b_2 & b_3 \\ c_2 & c_3 \end{vmatrix} - a_2 \begin{vmatrix} b_1 & b_3 \\ c_1 & c_3 \end{vmatrix} + a_3 \begin{vmatrix} b_1 & b_2 \\ c_1 & c_2 \end{vmatrix}
> $$

Come si costruisce, passo passo:

1. si prende il primo elemento della prima riga, $a_1$;
2. si cancellano la riga e la colonna di $a_1$: resta una tabella 2×2, di cui si calcola il determinante;
3. si moltiplica $a_1$ per quel determinante;
4. si fa lo stesso con $a_2$ (cancellando la prima riga e la seconda colonna) e con $a_3$ (prima riga e terza colonna);
5. si sommano i tre pezzi con i segni alterni $+\,-\,+$.

> [!warning] Il segno meno del termine centrale
> L'errore più frequente è dimenticare il $-$ davanti al secondo termine. I segni sono sempre $+\,-\,+$.

In alternativa si può usare la *regola di Sarrus*: si ricopiano le prime due colonne a destra della tabella, si sommano i prodotti delle tre diagonali che scendono verso destra e si sottraggono i prodotti delle tre diagonali che salgono. Il risultato è lo stesso; Sarrus vale solo per le tabelle 3×3.

> [!example] Esempio (dall'esercizio 7 del foglio sul prodotto vettoriale)
> $$
> \begin{vmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & -1 & 1 \end{vmatrix} = 1 \cdot \begin{vmatrix} 1 & 3 \\ -1 & 1 \end{vmatrix} - 2 \cdot \begin{vmatrix} 0 & 3 \\ 2 & 1 \end{vmatrix} + 0 \cdot \begin{vmatrix} 0 & 1 \\ 2 & -1 \end{vmatrix}
> $$
> $= 1 \cdot (1 + 3) - 2 \cdot (0 - 6) + 0 = 4 + 12 = 16$.

### Il prodotto vettoriale: la definizione

Il *prodotto vettoriale* esiste solo nello spazio e, a differenza del prodotto scalare, dà come risultato un vettore. Si scrive $\mathbf{u} \times \mathbf{v}$ (si legge "u vettore v").

> [!abstract] Definizione: prodotto vettoriale (in coordinate)
> Se $\mathbf{u} = (u_1, u_2, u_3)$ e $\mathbf{v} = (v_1, v_2, v_3)$,
> $$
> \mathbf{u} \times \mathbf{v} = \big(u_2 v_3 - u_3 v_2,\ \ u_3 v_1 - u_1 v_3,\ \ u_1 v_2 - u_2 v_1\big).
> $$

La formula sembra difficile da ricordare, ma si ricava da un determinante "simbolico", in cui nella prima riga si mettono i versori della base standard:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} = \begin{vmatrix} u_2 & u_3 \\ v_2 & v_3 \end{vmatrix}\mathbf{e}_1 - \begin{vmatrix} u_1 & u_3 \\ v_1 & v_3 \end{vmatrix}\mathbf{e}_2 + \begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix}\mathbf{e}_3.
$$

Non è un vero determinante (nella prima riga ci sono vettori, non numeri), ma sviluppandolo come se lo fosse si ottiene esattamente la formula. Il procedimento pratico è quindi:

1. prima componente: si coprono le prime colonne e si fa il determinante 2×2 delle colonne 2 e 3, $u_2 v_3 - u_3 v_2$;
2. seconda componente: si fa il determinante delle colonne 1 e 3, $u_1 v_3 - u_3 v_1$, e si cambia segno;
3. terza componente: il determinante delle colonne 1 e 2, $u_1 v_2 - u_2 v_1$.

> [!example] Esempio (esercizio 1 del foglio sul prodotto vettoriale)
> $\mathbf{u} = (1, 2, -1)$, $\mathbf{v} = (3, -1, 2)$.
>
> 1. Prima componente: $u_2 v_3 - u_3 v_2 = 2 \cdot 2 - (-1)(-1) = 4 - 1 = 3$.
> 2. Seconda componente: $u_3 v_1 - u_1 v_3 = (-1) \cdot 3 - 1 \cdot 2 = -3 - 2 = -5$.
> 3. Terza componente: $u_1 v_2 - u_2 v_1 = 1 \cdot (-1) - 2 \cdot 3 = -1 - 6 = -7$.
>
> Quindi $\mathbf{u} \times \mathbf{v} = (3, -5, -7)$, e rifacendo il conto con i vettori scambiati $\mathbf{v} \times \mathbf{u} = (-3, 5, 7)$: è l'opposto.
>
> Controllo con il prodotto scalare: $(3, -5, -7) \cdot \mathbf{u} = 3 - 10 + 7 = 0$ e $(3, -5, -7) \cdot \mathbf{v} = 9 + 5 - 14 = 0$. Il risultato è ortogonale a entrambi.

> [!tip] Controllo veloce
> Dopo aver calcolato $\mathbf{u} \times \mathbf{v}$, fai sempre il prodotto scalare del risultato con $\mathbf{u}$ e con $\mathbf{v}$: devono venire entrambi $0$. Se no, c'è un errore di conto (di solito un segno).

### Direzione, verso e regola della mano destra

Il vettore $\mathbf{u} \times \mathbf{v}$ è descritto geometricamente da tre proprietà:

1. direzione: è perpendicolare sia a $\mathbf{u}$ sia a $\mathbf{v}$, quindi perpendicolare al piano che contiene i due vettori;
2. verso: è dato dalla *regola della mano destra*. Si mettono le dita della mano destra lungo $\mathbf{u}$ e le si chiude verso $\mathbf{v}$ (dalla parte dell'angolo minore di $180°$): il pollice indica il verso di $\mathbf{u} \times \mathbf{v}$;
3. modulo: $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\|\,\|\mathbf{v}\|\sin\theta$, dove $\theta$ è l'angolo tra $\mathbf{u}$ e $\mathbf{v}$.

![[03-prodotto-vettoriale.svg|500]]

Nella figura $\mathbf{u}$ e $\mathbf{v}$ stanno nel piano orizzontale $xy$. Chiudendo la mano destra da $\mathbf{u}$ verso $\mathbf{v}$ il pollice punta in alto: $\mathbf{u} \times \mathbf{v}$ è verticale verso l'alto. Con i vettori scambiati la mano gira al contrario e il pollice punta in basso.

L'esempio più semplice sono i versori della base standard: $\mathbf{e}_1 \times \mathbf{e}_2 = \mathbf{e}_3$, $\mathbf{e}_2 \times \mathbf{e}_3 = \mathbf{e}_1$, $\mathbf{e}_3 \times \mathbf{e}_1 = \mathbf{e}_2$ (si gira in ordine $1 \to 2 \to 3 \to 1$). È proprio per questo che gli assi si disegnano in disposizione destrorsa.

### Il modulo è un'area

Il modulo $\|\mathbf{u}\|\,\|\mathbf{v}\|\sin\theta$ ha un significato semplice. Nel parallelogramma di lati $\mathbf{u}$ e $\mathbf{v}$, la base è $\|\mathbf{u}\|$ e l'altezza è $\|\mathbf{v}\|\sin\theta$ (il cateto opposto all'angolo $\theta$ nel triangolo rettangolo che ha per ipotenusa $\mathbf{v}$). Base per altezza dà proprio $\|\mathbf{u}\|\,\|\mathbf{v}\|\sin\theta$.

> [!abstract] Area con il prodotto vettoriale
> $$
> \text{area del parallelogramma di lati } \mathbf{u}, \mathbf{v} = \|\mathbf{u} \times \mathbf{v}\|
> $$
> $$
> \text{area del triangolo di lati } \mathbf{u}, \mathbf{v} = \tfrac12\,\|\mathbf{u} \times \mathbf{v}\|
> $$
> (il triangolo è metà del parallelogramma, tagliato dalla diagonale).

Ora si capisce anche il determinante 2×2 nel piano. Se si guardano due vettori del piano come vettori dello spazio con terza componente zero, $(u_1, u_2, 0)$ e $(v_1, v_2, 0)$, il loro prodotto vettoriale è $(0,\ 0,\ u_1 v_2 - u_2 v_1)$: un vettore verticale, la cui lunghezza (l'area) è $|u_1 v_2 - u_2 v_1|$. Il segno dice se punta in alto (rotazione antioraria, regola della mano destra) o in basso (rotazione oraria).

> [!example] Esempio (esercizio 2: area di un parallelogramma e di un triangolo)
> $\mathbf{a} = (2, 1, 0)$, $\mathbf{b} = (1, 3, 2)$.
>
> 1. $\mathbf{a} \times \mathbf{b} = (1 \cdot 2 - 0 \cdot 3,\ \ 0 \cdot 1 - 2 \cdot 2,\ \ 2 \cdot 3 - 1 \cdot 1) = (2, -4, 5)$.
> 2. $\|\mathbf{a} \times \mathbf{b}\| = \sqrt{4 + 16 + 25} = \sqrt{45} = 3\sqrt5$: è l'area del parallelogramma.
> 3. L'area del triangolo con gli stessi due lati uscenti da un vertice è la metà: $\frac{3\sqrt5}{2}$.

> [!example] Esempio (esercizio 3: angolo con il prodotto vettoriale)
> $\mathbf{u} = (1, 0, 1)$, $\mathbf{v} = (1, 1, 0)$.
>
> 1. $\mathbf{u} \times \mathbf{v} = (0 \cdot 0 - 1 \cdot 1,\ \ 1 \cdot 1 - 1 \cdot 0,\ \ 1 \cdot 1 - 0 \cdot 1) = (-1, 1, 1)$, con norma $\sqrt3$.
> 2. $\|\mathbf{u}\| = \|\mathbf{v}\| = \sqrt2$, quindi $\sin\theta = \dfrac{\sqrt3}{\sqrt2\,\sqrt2} = \dfrac{\sqrt3}{2}$.
> 3. Con il seno solo, $\theta$ potrebbe essere $60°$ o $120°$ (hanno lo stesso seno). Il prodotto scalare scioglie il dubbio: $\mathbf{u} \cdot \mathbf{v} = 1 > 0$, quindi $\cos\theta = \frac12$ e l'angolo è acuto: $\theta = 60°$.
>
> Per trovare un angolo, il prodotto scalare è più comodo: dà il coseno, che distingue gli angoli acuti dagli ottusi.

### Anticommutatività e parallelismo

Due proprietà del prodotto vettoriale lo distinguono da quello tra numeri.

> [!abstract] Proprietà del prodotto vettoriale
> 1. Anticommutatività: $\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v})$. Scambiando l'ordine il risultato cambia verso (la mano destra gira al contrario).
> 2. Parallelismo: $\mathbf{u} \times \mathbf{v} = \mathbf{0}$ se e solo se $\mathbf{u}$ e $\mathbf{v}$ sono paralleli (o uno dei due è nullo). In particolare $\mathbf{u} \times \mathbf{u} = \mathbf{0}$.

Il parallelismo si spiega con l'area: due vettori paralleli formano un parallelogramma schiacciato, di area zero (infatti $\theta = 0°$ o $180°$ e $\sin\theta = 0$).

> [!warning] L'ordine conta
> $\mathbf{u} \times \mathbf{v}$ e $\mathbf{v} \times \mathbf{u}$ sono opposti, non uguali. Negli esercizi bisogna rispettare l'ordine scritto nel testo.

> [!example] Esempio (esercizio 4: quali coppie sono parallele)
> - $(1, 2, 3)$ e $(2, 4, 6)$: il secondo è il doppio del primo, quindi il prodotto vettoriale è $\mathbf{0}$. Paralleli.
> - $(1, -1, 2)$ e $(2, -2, 5)$: il prodotto vettoriale è $\big((-1) \cdot 5 - 2 \cdot (-2),\ \ 2 \cdot 2 - 1 \cdot 5,\ \ 1 \cdot (-2) - (-1) \cdot 2\big) = (-1, -1, 0) \neq \mathbf{0}$. Non paralleli.
> - $(3, 0, -1)$ e $(-6, 0, 2)$: il secondo è $-2$ volte il primo, il prodotto vettoriale è $\mathbf{0}$. Paralleli (con verso opposto).

> [!example] Esempio (esercizio 5: un parametro)
> Per quali $t$ i vettori $\mathbf{u} = (1, t, 2)$ e $\mathbf{v} = (2, 4, 4)$ sono paralleli?
>
> 1. $\mathbf{u} \times \mathbf{v} = (t \cdot 4 - 2 \cdot 4,\ \ 2 \cdot 2 - 1 \cdot 4,\ \ 1 \cdot 4 - t \cdot 2) = (4t - 8,\ 0,\ 4 - 2t)$.
> 2. Deve essere il vettore nullo: $4t - 8 = 0$ e $4 - 2t = 0$, entrambe danno $t = 2$.
> 3. Infatti per $t = 2$ si ha $\mathbf{v} = 2\mathbf{u}$.

### Il prodotto triplo

Il *prodotto triplo* (o prodotto misto) di tre vettori dello spazio è il numero

$$
\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}):
$$

prima si fa il prodotto vettoriale $\mathbf{v} \times \mathbf{w}$ (che è un vettore), poi il prodotto scalare di $\mathbf{u}$ con quel vettore (che dà un numero).

Svolgendo i conti si scopre che è il determinante della tabella che ha per righe i tre vettori, nell'ordine:

> [!abstract] Prodotto triplo come determinante
> $$
> \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det(\mathbf{u}, \mathbf{v}, \mathbf{w}) = \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix}
> $$

Il motivo: sviluppando il determinante lungo la prima riga, i tre determinanti 2×2 che moltiplicano $u_1$, $u_2$, $u_3$ (con i segni $+\,-\,+$) sono esattamente le tre componenti di $\mathbf{v} \times \mathbf{w}$. Quindi lo sviluppo è $u_1 (\mathbf{v} \times \mathbf{w})_1 + u_2 (\mathbf{v} \times \mathbf{w})_2 + u_3 (\mathbf{v} \times \mathbf{w})_3$, cioè il prodotto scalare.

> [!example] Esempio (esercizio 7)
> $\mathbf{u} = (1, 2, 0)$, $\mathbf{v} = (0, 1, 3)$, $\mathbf{w} = (2, -1, 1)$.
>
> 1. Con i due prodotti: $\mathbf{v} \times \mathbf{w} = \big(1 \cdot 1 - 3 \cdot (-1),\ \ 3 \cdot 2 - 0 \cdot 1,\ \ 0 \cdot (-1) - 1 \cdot 2\big) = (4, 6, -2)$, poi $\mathbf{u} \cdot (4, 6, -2) = 4 + 12 + 0 = 16$.
> 2. Con il determinante: è quello calcolato nell'esempio del determinante 3×3, e vale $16$.
>
> I due metodi danno lo stesso numero.

### Il volume del parallelepipedo e del tetraedro

Tre vettori $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ che partono dallo stesso vertice sono i tre spigoli di un *parallelepipedo* (una "scatola storta", con le facce a forma di parallelogramma). Il prodotto triplo ne misura il volume.

![[03-altezza-parallelepipedo.svg|460]]

Il perché, passo passo:

1. il volume di un parallelepipedo è area della base per altezza;
2. la base è il parallelogramma di lati $\mathbf{b}$ e $\mathbf{c}$, quindi la sua area è $\|\mathbf{b} \times \mathbf{c}\|$;
3. il vettore $\mathbf{b} \times \mathbf{c}$ è perpendicolare alla base, quindi l'altezza $h$ è la proiezione di $\mathbf{a}$ sulla direzione di $\mathbf{b} \times \mathbf{c}$: $h = \dfrac{|\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})|}{\|\mathbf{b} \times \mathbf{c}\|}$ (in valore assoluto, perché un'altezza è positiva);
4. moltiplicando base per altezza, $\|\mathbf{b} \times \mathbf{c}\|$ si semplifica e resta $|\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})|$.

> [!abstract] Volumi con il prodotto triplo
> $$
> V_{\text{parallelepipedo}} = |\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})| = |\det(\mathbf{a}, \mathbf{b}, \mathbf{c})|
> $$
> $$
> V_{\text{tetraedro}} = \tfrac16\,|\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})|
> $$
> Il tetraedro è quello che ha per spigoli gli stessi tre vettori uscenti da un vertice.

Il $\frac16$ del tetraedro viene da due passaggi: la sua base è il triangolo di lati $\mathbf{b}$ e $\mathbf{c}$, metà del parallelogramma; e il volume di una piramide è un terzo di base per altezza. $\frac12 \cdot \frac13 = \frac16$.

![[03-parallelepipedo.svg|500]]

> [!example] Esempio (esercizio 8)
> $\mathbf{a} = (2, 0, 1)$, $\mathbf{b} = (1, 3, 0)$, $\mathbf{c} = (0, 2, 4)$.
>
> $$
> \det(\mathbf{a}, \mathbf{b}, \mathbf{c}) = \begin{vmatrix} 2 & 0 & 1 \\ 1 & 3 & 0 \\ 0 & 2 & 4 \end{vmatrix} = 2 \cdot (12 - 0) - 0 \cdot (4 - 0) + 1 \cdot (2 - 0) = 24 + 2 = 26.
> $$
>
> Volume del parallelepipedo: $26$. Volume del tetraedro: $\frac{26}{6} = \frac{13}{3}$.

### Complanarità e orientazione

Tre vettori si dicono *complanari* se stanno in uno stesso piano (disegnati con la coda nello stesso punto). In quel caso il parallelepipedo è schiacciato, ha volume zero.

> [!abstract] Criterio di complanarità
> $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ sono complanari se e solo se
> $$
> \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 0.
> $$
> Quattro punti $A$, $B$, $C$, $D$ stanno sullo stesso piano se e solo se $\overrightarrow{AB} \cdot (\overrightarrow{AC} \times \overrightarrow{AD}) = 0$.

Lo si può leggere anche così: $\mathbf{v} \times \mathbf{w}$ è perpendicolare al piano di $\mathbf{v}$ e $\mathbf{w}$, e il prodotto scalare con $\mathbf{u}$ è zero quando $\mathbf{u}$ è perpendicolare a $\mathbf{v} \times \mathbf{w}$, cioè quando $\mathbf{u}$ sta in quel piano.

Il segno del prodotto triplo, invece, dice l'*orientazione* della terna:

- positivo: $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ sono disposti come $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ (terna *destrorsa*: $\mathbf{u}$ sta dalla stessa parte di $\mathbf{v} \times \mathbf{w}$ rispetto al piano di $\mathbf{v}$ e $\mathbf{w}$);
- negativo: terna *sinistrorsa*, come in uno specchio;
- scambiando due vettori il segno cambia, il valore assoluto (il volume) no.

> [!example] Esempio (esercizio 9: complanarità)
> $\mathbf{u} = (1, 2, 3)$, $\mathbf{v} = (2, 1, 0)$, $\mathbf{w} = (3, 3, 3)$.
>
> $$
> \begin{vmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ 3 & 3 & 3 \end{vmatrix} = 1 \cdot (3 - 0) - 2 \cdot (6 - 0) + 3 \cdot (6 - 3) = 3 - 12 + 9 = 0.
> $$
>
> I tre vettori sono complanari. Infatti $\mathbf{w} = \mathbf{u} + \mathbf{v}$: $\mathbf{w}$ è la diagonale del parallelogramma di $\mathbf{u}$ e $\mathbf{v}$, quindi sta nel loro piano.

> [!example] Esempio (esercizio 10: parametro e complanarità)
> Per quale $k$ i vettori $\mathbf{u} = (1, 0, 2)$, $\mathbf{v} = (2, 1, -1)$, $\mathbf{w} = (3, k, 1)$ sono complanari?
>
> $$
> \begin{vmatrix} 1 & 0 & 2 \\ 2 & 1 & -1 \\ 3 & k & 1 \end{vmatrix} = 1 \cdot (1 + k) - 0 + 2 \cdot (2k - 3) = 1 + k + 4k - 6 = 5k - 5.
> $$
>
> Si pone $5k - 5 = 0$: i vettori sono complanari per $k = 1$.

> [!example] Esempio (esercizio 11: orientazione)
> - $\mathbf{e}_1 \cdot (\mathbf{e}_2 \times \mathbf{e}_3) = \mathbf{e}_1 \cdot \mathbf{e}_1 = 1$: è il volume del cubo di lato 1, con segno positivo (terna destrorsa).
> - $\mathbf{e}_2 \cdot (\mathbf{e}_1 \times \mathbf{e}_3)$: per l'anticommutatività $\mathbf{e}_1 \times \mathbf{e}_3 = -(\mathbf{e}_3 \times \mathbf{e}_1) = -\mathbf{e}_2$, quindi il prodotto vale $\mathbf{e}_2 \cdot (-\mathbf{e}_2) = -1$.
>
> Scambiando due vettori il volume resta 1, ma il segno cambia: la terna $\mathbf{e}_2, \mathbf{e}_1, \mathbf{e}_3$ è sinistrorsa.

> [!example] Esempio (esercizio 12: esercizio di sintesi)
> $A = (1, 0, 0)$, $B = (3, 1, 2)$, $C = (2, 4, 1)$, $D = (4, 2, 5)$.
>
> 1. Vettori: $\overrightarrow{AB} = (2, 1, 2)$, $\overrightarrow{AC} = (1, 4, 1)$, $\overrightarrow{AD} = (3, 2, 5)$.
> 2. $\overrightarrow{AB} \times \overrightarrow{AC} = (1 \cdot 1 - 2 \cdot 4,\ \ 2 \cdot 1 - 2 \cdot 1,\ \ 2 \cdot 4 - 1 \cdot 1) = (-7, 0, 7)$, di norma $\sqrt{49 + 49} = 7\sqrt2$: è l'area del parallelogramma su $\overrightarrow{AB}$ e $\overrightarrow{AC}$.
> 3. Area del triangolo $ABC$: $\frac{7\sqrt2}{2}$.
> 4. $\overrightarrow{AC} \times \overrightarrow{AD} = (4 \cdot 5 - 1 \cdot 2,\ \ 1 \cdot 3 - 1 \cdot 5,\ \ 1 \cdot 2 - 4 \cdot 3) = (18, -2, -10)$, e $\overrightarrow{AB} \cdot (18, -2, -10) = 36 - 2 - 20 = 14$.
> 5. Volume del parallelepipedo generato dai tre vettori: $|14| = 14$.
> 6. Il prodotto triplo non è zero, quindi i quattro punti non sono complanari (formano un tetraedro, di volume $\frac{14}{6} = \frac73$).

## Collegamenti

I vettori riprendono e mettono in ordine molte cose della geometria analitica vista in [[02-retta-e-circonferenza]]. La distanza tra due punti è la norma del vettore $B - A$, il punto medio è la media delle coordinate, e una retta si può scrivere in forma parametrica come $X = A + s\,\mathbf{v}$: un punto di partenza più tutti i multipli di un vettore che dà la direzione. Due rette sono perpendicolari quando i loro vettori direzione hanno prodotto scalare zero, e la distanza di un punto da una retta si trova con la perpendicolare, come nell'esercizio 22.

Gli esercizi con il parametro ($t$ o $k$) si risolvono sempre riducendoli a un'equazione o a una disequazione, con le tecniche di [[01-equazioni-e-disequazioni]]: una disequazione di primo grado per l'angolo acuto o ottuso, un'equazione di secondo grado per l'angolo assegnato. L'angolo tra due vettori si ricava con l'arcocoseno, che è la funzione inversa del coseno: le funzioni inverse sono in [[04-le-funzioni]], seno, coseno e le loro inverse in [[05-funzioni-elementari]].

Per un futuro architetto i vettori sono il linguaggio dello spazio. In Geometria descrittiva un punto si dà con tre numeri (distanza, aggetto, quota) e le [[03-proiezioni-ortogonali-punto-e-rette|proiezioni ortogonali]] sui piani del triedro sono proprio proiezioni di vettori, come la proiezione vettoriale di questa pagina, fatta sugli assi e sui piani coordinati. La [[06-piani-ausiliari-e-perpendicolarita|perpendicolarità tra rette e piani]] si traduce nel prodotto scalare nullo, e il prodotto vettoriale dà la direzione perpendicolare a un piano. Anche i disegni nello spazio di questa pagina sono assonometrie cavaliere: un punto $(x, y, z)$ si disegna sommando, con la regola punta-coda, i tre vettori $x\,\mathbf{e}_1$, $y\,\mathbf{e}_2$, $z\,\mathbf{e}_3$ disegnati lungo gli assi.

## Per approfondire

- [[Capitolo_Vettori.pdf]] (Stewart, *Calcolo. Funzioni di più variabili*, capitolo 2): paragrafo 2.2 "Vettori" alle pagine 64-72 (somma, multipli, componenti, base standard, versori); paragrafo 2.3 "Il prodotto scalare" alle pagine 73-78 (definizione, angolo, ortogonalità, proiezioni a pagina 77); paragrafo 2.4 "Il prodotto vettoriale" alle pagine 79-86 (mano destra a pagina 80, determinanti a pagina 82, prodotto triplo e volumi alle pagine 84-85). Le pagine sono quelle stampate sul libro.
- [[Esercizi_vettori.pdf]]: i due fogli del professore su vettori e prodotto scalare (esercizi 1-24), usati per gli esempi di questa pagina.
- [[esercizi prodotto vettoriale e prodotto triplo.pdf]]: il foglio del professore su determinanti, prodotto vettoriale e prodotto triplo (esercizi 1-12), con le formule utili in alto.
- [[Giuffrida Ragusa - Determinanti_compressed.pdf]]: per chi vuole vedere i determinanti in modo più completo.
- Ripasso veloce delle formule: [[00-ripasso-esonero-1]], sezioni 1-3.
