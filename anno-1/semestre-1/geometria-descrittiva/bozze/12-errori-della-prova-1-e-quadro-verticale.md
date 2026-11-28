---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-11-12
tags: [geometria-descrittiva, bozza]
---

# Gli errori da evitare dopo la Prova n. 1 e l'assonometria obliqua con il quadro verticale

> [!info] Note collegate
> Sbobina: [[12-correzione-prova-1-e-assonometria-obliqua]]
>
> Bozza precedente: [[11-assonometria-cavaliera-e-sezioni-dei-solidi]] · Successiva: [[13-la-prospettiva-e-il-metodo-della-pianta]]
>
> Argomenti collegati: [[02-proiezioni-e-omologia-schema]] · [[02-omologia-dai-due-centri-passo-passo]] · [[02-affinita-ortogonale-passo-passo]] · [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]] · [[09-ribaltamento-del-piano-generico]] · [[00-ripasso-prova-1]]

La lezione di giovedì 12 novembre, registrata da una compagna in due parti, ha due argomenti.

Nella prima parte la docente restituisce e corregge la Prova n. 1, che conteneva esercizi di omologia e di proiezioni ortogonali. Dagli errori più frequenti viene fuori, in positivo, il modo giusto di risolvere ogni tipo di esercizio:

- nell'omologia, la regola dell'esercizio «madre», che basta per tutti i casi, anche quello con l'asse all'infinito;
- nelle proiezioni ortogonali, il ribaltamento dei piani proiettanti, il ribaltamento del piano generico intorno alla prima traccia, le tracce del piano trovate con un'orizzontale e una frontale, la retta perpendicolare al piano.

Nella seconda parte continua l'assonometria obliqua iniziata il 10 novembre, questa volta con il quadro verticale:

- che cosa resta vero e che cosa si deforma quando il quadro contiene gli assi x e z;
- come si trova la direzione di proiezione ribaltando l'asse y;
- come si costruisce un solido con il metodo della pianta, cioè con l'affinità tra la pianta ribaltata e la pianta assonometrica.

Tutto serve per la Prova n. 2, che il calendario aggiornato fissa a giovedì 26 novembre: l'assonometria è il suo argomento, e gli errori della prima prova sono quelli da non ripetere.

## GLI ERRORI DA EVITARE NELL'OMOLOGIA

### La regola che risolve tutti gli esercizi: l'esercizio «madre»

Un'omologia è definita da un centro U, da un asse u e da una coppia di elementi corrispondenti. Una volta definita, il corrispondente di ogni punto e di ogni retta è uno solo.

Tutti gli esercizi di omologia si risolvono con due regole soltanto:

1. i punti corrispondenti sono allineati con il centro;
2. le rette corrispondenti si incontrano sull'asse.

La docente chiama esercizio «madre» quello in cui sono dati il centro, l'asse e una coppia di punti corrispondenti A e A′, e si cerca il corrispondente di un altro punto B. Nell'esercizio guidato della docente è il caso in cui non ci sono più le rette, ma solo la coppia di punti.

Si risolve così.

Poiché i punti corrispondenti sono allineati con il centro, B′ sta sicuramente sulla retta che va da U a B: si traccia questo raggio.

Poi si costruisce la retta s che passa per A e per B e la si prolunga fino all'asse. Il punto in cui incontra l'asse, che conviene chiamare M, è un punto unito: corrisponde a se stesso.

Le rette corrispondenti si incontrano sull'asse, quindi la retta s′, corrispondente di s, passa per M; e poiché A appartiene a s, A′ appartiene a s′. La retta s′ è quindi la retta MA′.

Dove s′ incontra il raggio UB si trova B′.

> [!example] Disegno 1 · Il disegno: l'esercizio «madre»
> ![[12-omologia-esercizio-madre.svg|620]]
>
> 1. Sono dati il centro U, l'asse u e una coppia di punti corrispondenti A e A′, allineati con U. Si cerca il corrispondente di B.
> 2. Si traccia il raggio da U per B: B′ starà su questa retta.
> 3. Si traccia la retta s per A e B e la si prolunga fino all'asse, dove si trova il punto unito M.
> 4. La corrispondente s′ passa per M e per A′.
> 5. Dove s′ incontra il raggio UB c'è B′.

### Quando sono date due rette: cercare una coppia di punti

Negli altri esercizi l'omologia non è data con una coppia di punti, ma con una coppia di rette corrispondenti r e r′.

In questo caso la prima cosa da fare è sempre la stessa: trovare una coppia di punti corrispondenti sulle due rette. Si sceglie un punto A su r, si traccia il raggio da U per A, e dove il raggio incontra r′ si trova A′.

A questo punto ci si ritrova esattamente nella situazione dell'esercizio «madre», e si procede come sopra.

Conviene scegliere punti semplici. Nella prova alcuni hanno scelto punti molto complicati e si sono complicati la vita, mentre bastava prolungare le rette date. Prolungandole si vede anche che si incontrano davvero sull'asse: è la verifica che si tratta di due rette corrispondenti, cioè che l'omologia è ben definita.

### Il punto corrispondente sta sul raggio dal centro

Quando si costruisce la retta s per A e per M e la sua corrispondente s′, bisogna chiedersi dove si trova M′.

M′ non può stare su r. Sta necessariamente sulla retta che lo congiunge al centro: va allineato con il centro, e lo si trova dove questo raggio incontra s′.

Le costruzioni devono essere logiche: ogni punto si trova come intersezione di due rette di cui si sa perché passano di lì.

### L'omologia speciale con l'asse all'infinito

Quando le due rette corrispondenti r e r′ sono parallele e l'asse è indicato all'infinito, si tratta di un'omologia speciale, un'omotetia. L'asse c'è e il centro c'è; l'unica differenza è che l'asse sta all'infinito. Per il resto le regole sono sempre le stesse.

Dire che le rette corrispondenti si incontrano sull'asse, quando l'asse è all'infinito, vuol dire che si incontrano in un punto improprio: le rette corrispondenti sono parallele.

Per trovare la retta s′ corrispondente di una retta s data si procede così.

Prima si cerca la solita coppia di punti corrispondenti: si sceglie A su r e lo si allinea con il centro, trovando A′ su r′.

Su s, invece, non è dato nessun punto. Ma la retta proiettiva è piena di punti: se ne può prendere uno qualunque, a piacere, e chiamarlo M.

Si costruisce la retta AM; la sua corrispondente passa per A′ ed è parallela ad AM, perché l'asse è all'infinito.

Il punto M′ deve essere allineato con il centro: sta dove il raggio UM incontra la parallela condotta da A′.

L'esercizio non è finito finché non si disegna la retta: s′ passa per M′ ed è parallela a s. Nell'esercizio della prova s′ risulta alla destra di s, non alla sinistra.

Molti studenti hanno usato un metodo diverso, partendo dall'intersezione tra r e s: anche questo va benissimo.

Per verificare il risultato a casa si rifà l'esercizio prendendo un altro punto su s. La posizione di s′ deve essere la stessa, perché l'omologia è una e una sola: non esiste un'altra posizione possibile.

> [!example] Disegno 2 · Il disegno: trovare s′ con l'asse all'infinito
> ![[12-omologia-asse-all-infinito-retta.svg|620]]
>
> 1. Sono dati il centro U, la coppia di rette corrispondenti r e r′, parallele perché l'asse è all'infinito, e la retta s.
> 2. Si sceglie A su r e si traccia il raggio da U: dove incontra r′ c'è A′.
> 3. Su s si prende un punto qualunque M e si traccia la retta AM.
> 4. La retta corrispondente passa per A′ ed è parallela ad AM.
> 5. M′ sta sul raggio UM, dove incontra la parallela.
> 6. s′ passa per M′ ed è parallela a s. Con un altro punto M si deve trovare la stessa s′.

### Il triangolo con un punto unito

Un altro esercizio era molto semplice, perché il triangolo aveva un vertice sull'asse, cioè un punto unito.

Conviene sempre mettere le lettere ai vertici: A, B e C, dove C è il punto unito.

Si considera la retta m che passa per A e per B. La sua corrispondente m′ passa per A′ e per il punto in cui m incontra l'asse. Il punto B′ è allineato con il centro, quindi sta dove il raggio UB incontra m′.

A questo punto l'esercizio è finito davvero: C rimane dov'è e non si muove, perché sta sull'asse, e il triangolo corrispondente è A′B′C.

### Il segno e il tempo

Nei disegni d'esame i punti non si segnano con quadratini o pallini grossi: la docente li disegna alla lavagna solo per essere più chiara durante la spiegazione.

Le lettere, invece, si mettono sempre.

Un esercizio di omologia, se le regole sono chiare, non richiede più di 10 minuti.

Per allenarsi, il libro della docente ha dodici esercizi di omologia piana con la traccia e la soluzione (allegato, applicazioni 1-12, pp. 16-27): omotetia, affinità parallela, ortogonale e obliqua, omologia, omologia speciale e traslazione.

## GLI ERRORI DA EVITARE NELLE PROIEZIONI ORTOGONALI

### Il modello del diedro

L'errore che dispiace di più alla docente riguarda il ribaltamento dei piani proiettanti in prima e in seconda, che sono i piani più facili.

Per evitarlo bisogna costruire un modello tridimensionale del diedro, con un cartoncino, e ragionare con il modello davanti, almeno per queste posizioni del piano. Chi ha messo un cartoncino dentro il diedro non sbaglia la posizione dei punti, perché vede dove il piano c'è e dove non c'è.

### Il piano proiettante in prima ribaltato su π₁

Si guardi la proiezione ortogonale ricordando che quello che sta sopra la linea di terra è la proiezione su π₂, quello che sta sotto è la proiezione su π₁.

Se si guarda soltanto la parte sotto la linea di terra, cioè la prima proiezione, il piano proiettante in prima è un elemento verticale. Tutto quello che sta sul piano non si vede come figura, ma cade sulla traccia t₁α. Quindi i vertici A₁, B₁ e C₁ stanno tutti su t₁α, alle stesse verticali di A₂, B₂ e C₂.

Una volta capito questo, la rotazione diventa facile.

Si fa ruotare il piano intorno a t₁α finché non coincide con π₁. Durante la rotazione la quota di ogni punto non varia: il punto conserva sempre la stessa distanza dalla cerniera.

Da ogni punto A₁, B₁, C₁ si manda quindi la perpendicolare a t₁α, cioè ci si mette a 90 gradi, e su di essa si riporta la quota del punto, presa dalla seconda proiezione. Si trovano A\*, B\* e C\*: il triangolo in vera forma.

Nella prova alcuni studenti hanno individuato male la figura, ma hanno fatto bene il ribaltamento, ribaltando le quote come è giusto. Il punto da non sbagliare è proprio questo: B\* deve stare sulla perpendicolare a t₁α condotta da B₁, a una distanza uguale alla quota di B, non in una posizione in cui il piano non c'è.

> [!example] Disegno 3 · Il disegno nello spazio: il piano proiettante in prima si abbatte su π₁
> ![[07-spazio-ribaltamento-su-pi1.svg|620]]
>
> 1. Il piano α è verticale e contiene il triangolo ABC. Le prime proiezioni dei vertici cadono su t₁α.
> 2. Il piano ruota intorno a t₁α: ogni punto descrive un arco su un piano perpendicolare a t₁α, con il centro sulla traccia.
> 3. Il raggio di ogni arco è la quota del punto: per questo, a fine rotazione, ogni punto ribaltato sta sulla perpendicolare a t₁α, a una distanza uguale alla sua quota.

> [!example] Disegno 4 · Il disegno: il piano proiettante in prima ribaltato su π₁
> ![[12-ribaltamento-piano-proiettante-in-prima.svg|620]]
>
> 1. In seconda proiezione si vede il triangolo A₂B₂C₂; in prima proiezione tutto cade sulla traccia t₁α, in A₁, B₁, C₁.
> 2. Da ogni punto A₁, B₁, C₁ si manda la perpendicolare a t₁α.
> 3. Su ogni perpendicolare si riporta la quota del punto, presa dalla seconda proiezione (per B, le due lineette).
> 4. Si trovano A\*, B\*, C\*: il triangolo in vera forma.

### Riconoscere il piano: due figure non sono mai un piano proiettante

Alcuni studenti hanno trattato come proiettante in prima un piano che non poteva esserlo.

Le due proiezioni si vedono sempre. Se una delle due è una linea, il piano è proiettante. Se invece si vedono due figure, e nessuna delle due è una linea, il piano non può essere proiettante: è un piano generico, e si ribalta come tale.

### Il triangolo con un vertice su π₁: basta la prima traccia

Nel secondo esercizio di ribaltamento il triangolo stava in un piano generico, ma l'esercizio era fatto in modo da essere facile.

Si mettono prima di tutto le lettere: A₂, B₂, C₂ sopra la linea di terra, A₁, B₁, C₁ sotto.

Poi si cerca la retta intorno a cui far ruotare la figura. Conviene prendere la prima traccia del piano, cioè l'orizzontale a quota zero, perché il punto A si trova già a quota zero.

Lo si vede dalla seconda proiezione: A₂ sta sulla linea di terra. Se la seconda proiezione di un punto cade sulla linea di terra, il punto sta già sul piano π₁, e coincide con la sua prima proiezione. Quindi la prima traccia del piano passa per A₁.

Serve allora un solo altro punto della prima traccia. Si prende la retta r che contiene il lato BC e se ne cerca la prima traccia:

1. si prolunga r₂ fino alla linea di terra, dove si trova (T₁ᵣ)₂;
2. con la linea di richiamo si scende su r₁ e si trova T₁ᵣ.

La prima traccia del piano è la retta che passa per A₁ e per T₁ᵣ: è t₁α, ed è l'asse di rotazione.

Non serve nient'altro:

- non serve la seconda traccia del piano;
- non serve la retta di massima pendenza;
- la verifica fatta con la perpendicolarità è un di più.

Nel foglio della prova, del resto, le due tracce non si sarebbero nemmeno incontrate sulla linea di terra dentro il foglio: segno che non erano necessarie.

### Quale punto ruota, e il raggio di rotazione

Si ribalta il punto più lontano dall'asse di rotazione, cioè il più lontano nella direzione perpendicolare all'asse: qui è B.

1. Da B₁ si costruisce la perpendicolare a t₁α.
2. Si ribalta la quota del punto, cioè la distanza da cui B raggiunge il piano π₁: la si riporta da B₁, perpendicolarmente alla retta appena tracciata, a destra o a sinistra. Si trova B̄ (B soprallineato).
3. Il segmento che va dal piede della perpendicolare su t₁α fino a B̄ è il raggio di rotazione. Lo si riporta col compasso sulla perpendicolare, e si trova B\*.

Accanto a questo segmento conviene scrivere «raggio». La docente corregge centinaia di esercizi e non può verificare ogni misura con la squadra: se vede scritto «raggio», capisce che lo studente sa perfettamente che cosa sta facendo.

### Il resto della figura con l'affinità ortogonale

Il punto A non si muove, perché sta sull'asse: A₁ coincide con A\*.

Per C non si rifà il ribaltamento: si usa l'omologia, perché la prima traccia di α coincide con l'asse dell'omologia di ribaltamento. La direzione è perpendicolare all'asse, quindi si tratta di un'affinità ortogonale.

Le rette corrispondenti si incontrano sull'asse: r₁ incontra t₁α in T₁ᵣ, quindi r\* passa per T₁ᵣ e per B\*. C\* sta su r\*, allineato con il centro, cioè sulla perpendicolare all'asse condotta da C₁.

La figura ribaltata è A₁ ≡ A\*, B\*, C\*. Si può ribaltare indifferentemente a destra o a sinistra: nella prova entrambe le scelte erano giuste.

> [!example] Disegno 5 · Il disegno nello spazio: il triangolo ruota intorno alla prima traccia
> ![[09-spazio-ribaltamento-piano-generico.svg|620]]
>
> Lo schema viene dalla lezione del 29 ottobre: qui il vertice che sta su π₁ si chiama C, non A, ma la costruzione è la stessa.
> 1. Il vertice che sta su π₁ non si muove: la prima traccia t₁α passa per lui ed è la cerniera.
> 2. Il punto più lontano, B, ruota intorno a t₁α su un arco che sta in un piano perpendicolare a t₁α: il centro è il piede H della perpendicolare, il raggio è HB.
> 3. A fine rotazione B\* sta su π₁; il resto della figura si trova con l'affinità.

> [!example] Disegno 6 · Il disegno: il triangolo con A su π₁ ribaltato su π₁
> ![[12-ribaltamento-triangolo-con-a-su-pi1.svg|620]]
>
> 1. A₂ sta sulla LT, quindi A ha quota zero: la prima traccia del piano passa per A₁.
> 2. r è la retta del lato BC. Si prolunga r₂ fino alla LT, dove c'è (T₁ᵣ)₂; con la linea di richiamo si trova T₁ᵣ su r₁.
> 3. t₁α è la retta A₁T₁ᵣ: è l'asse di rotazione.
> 4. Da B₁ si manda la perpendicolare a t₁α; da B₁, perpendicolarmente a questa, si riporta la quota di B (le due lineette) e si trova B̄.
> 5. Il segmento dal piede della perpendicolare a B̄ è il raggio di rotazione: lo si riporta col compasso sulla perpendicolare, dalla parte opposta, e si trova B\*.
> 6. r\* passa per T₁ᵣ e per B\*; C\* sta dove r\* incontra la perpendicolare all'asse condotta da C₁. A₁ ≡ A\*.

### La traccia di una retta non è il punto sulla linea di terra

Alcuni studenti hanno indicato come traccia della retta il punto in cui la sua proiezione incontra la linea di terra.

Quel punto non è la traccia: è la proiezione della traccia. Se si porta r₂ fino alla linea di terra, si trova (T₁ᵣ)₂; la traccia T₁ᵣ si trova scendendo con la linea di richiamo fino a r₁.

Lo stesso vale per la seconda traccia: prolungando r₁ fino alla linea di terra si trova (T₂ᵣ)₁, e la traccia T₂ᵣ sta su r₂.

### La retta che appartiene al piano

Per verificare se una retta appartiene a un piano α si può far passare per essa un'orizzontale del piano, oppure, più semplicemente, cercare le tracce della retta.

Una retta appartiene a un piano se le sue tracce stanno sulle tracce del piano. Nell'esercizio della prova la traccia di r non stava sulla traccia di α: è evidente, quindi, che la retta era esterna al piano.

Chi ha lavorato con ordine, mettendo le proiezioni e scrivendo tutto, lo ha visto subito.

### Le tracce del piano da un'orizzontale e una frontale

Un altro esercizio chiedeva le tracce del piano di una figura che aveva un lato orizzontale e un lato frontale. Anche questo era facile: per fare le tracce di un piano, in questo caso, non serve quasi niente.

Come sempre, prima si mettono le lettere. Poi si riconoscono le due rette:

- il lato orizzontale o ha la seconda proiezione o₂ parallela alla linea di terra;
- il lato frontale f ha la prima proiezione f₁ parallela alla linea di terra.

Un'orizzontale del piano è parallela alla prima traccia, una frontale è parallela alla seconda traccia. Quindi:

1. per la prima traccia si cerca la prima traccia della frontale, T₁f, e da lì si va parallelamente all'orizzontale: t₁α passa per T₁f ed è parallela a o₁;
2. per la seconda traccia si cerca la seconda traccia dell'orizzontale, T₂o, e da lì si va parallelamente alla frontale: t₂α passa per T₂o ed è parallela a f₂;
3. le due tracce si incontrano sulla linea di terra.

La seconda traccia è parallela a f₂, non a un lato qualunque della figura. Un lato come DC o BC è una retta generica del piano: appartiene al piano, ma non è parallelo a nessuna delle due tracce. Nella prova qualcuno ha disegnato t₂α parallela al lato B₂C₂, che non c'entra niente.

> [!example] Disegno 7 · Il disegno nello spazio: le tracce sono parallele all'orizzontale e alla frontale
> ![[b12-spazio-tracce-orizzontale-frontale.svg|620]]
>
> 1. Il piano α (in azzurro) taglia π₁ lungo t₁α e π₂ lungo t₂α.
> 2. L'orizzontale o (in verde) passa per A, alla sua quota, ed è parallela a t₁α. Buca π₂ in T₂o, che sta su t₂α. La sua prima proiezione o₁ è parallela a t₁α.
> 3. La frontale f (in arancio) passa per A, al suo aggetto, ed è parallela a t₂α. Buca π₁ in T₁f, che sta su t₁α. La sua seconda proiezione f₂ è parallela a t₂α.
> 4. Per questo bastano T₁f, T₂o e le due direzioni o₁ e f₂ per avere le tracce.

> [!example] Disegno 8 · Il disegno: le tracce da un'orizzontale e una frontale, e la perpendicolare
> ![[12-tracce-da-orizzontale-e-frontale.svg|620]]
>
> Lo schema è una ricostruzione: la figura della prova non si conosce, qui è un quadrilatero ABCD con il lato AD orizzontale e il lato AB frontale.
> 1. AD è un'orizzontale: A₂D₂ è parallela alla LT. AB è una frontale: A₁B₁ è parallela alla LT.
> 2. Si prolunga f₂ fino alla LT e si scende su f₁: lì c'è T₁f. t₁α passa per T₁f ed è parallela a o₁.
> 3. Si prolunga o₁ fino alla LT e si sale su o₂: lì c'è T₂o. t₂α passa per T₂o ed è parallela a f₂, non a B₂C₂ o a D₂C₂.
> 4. La retta p perpendicolare al piano, qui condotta da C: p₁ è perpendicolare a t₁α e a o₁, p₂ è perpendicolare a t₂α e a f₂.

### La perpendicolare al piano: tutte e due le proiezioni

In molti compiti mancava la retta perpendicolare al piano, che l'esercizio chiedeva. Qualcuno ne ha disegnato la prima proiezione e non la seconda.

Una retta è perpendicolare a un piano se:

- la sua prima proiezione è perpendicolare alla prima traccia del piano, e quindi a tutte le orizzontali del piano, sia quella a terra sia le altre;
- la sua seconda proiezione è perpendicolare alla seconda traccia, e quindi a tutte le frontali del piano.

La seconda traccia, del resto, è la frontale ad aggetto zero, come la prima traccia è l'orizzontale a quota zero.

Il libro della docente lo scrive nella pagina sulla rappresentazione dei piani (allegato, p. 34): nel piano generico la prima traccia rappresenta l'orizzontale del piano a quota zero e la seconda traccia ne rappresenta la frontale ad aggetto zero, e queste considerazioni tornano utili negli esercizi in forma tecnica. Nella pagina sulla perpendicolarità retta-piano (p. 43) aggiunge che la prima proiezione della retta perpendicolare al piano è perpendicolare alla prima proiezione delle orizzontali del piano, e la seconda proiezione alla seconda proiezione delle frontali.

Per questo non c'era bisogno di trovare le tracce del piano: bastava fare la prima proiezione della perpendicolare perpendicolare all'orizzontale o₁, e la seconda perpendicolare alla frontale f₂. Ma le proiezioni da disegnare sono sempre due.

> [!example] Disegno 9 · Il disegno nello spazio: la retta perpendicolare al piano
> ![[b06-spazio-retta-perpendicolare-al-piano.svg|620]]
>
> 1. La retta r è perpendicolare al piano α: forma un angolo retto con ogni retta del piano che passa per il suo piede H.
> 2. Proiettata su π₁ e su π₂, dà r₁ perpendicolare a t₁α e r₂ perpendicolare a t₂α.
> 3. Le due condizioni servono insieme: una sola proiezione non basta a individuare la retta.

### Il piano proiettante in seconda: la figura non si restringe

L'ultimo esercizio, su un piano proiettante in seconda, è un caso che la docente ha anche nel programma e che tornerà nella prospettiva, dove si usa esattamente questa costruzione. Non era stato spiegato apposta, perché gli studenti cominciassero a ragionare, e qualcuno ha usato bene un piano ausiliario.

Un piano proiettante in seconda si può ribaltare in più modi:

1. si può far ruotare sul piano orizzontale, come se si accasciasse, intorno a una sua retta parallela a π₁, per esempio considerando un piano orizzontale un po' più alto: la dimensione della figura che si legge in pianta, in quella direzione, non varia;
2. si può costruire la seconda traccia e far ruotare il piano intorno alla prima traccia, con il centro di rotazione dove le tracce si incontrano sulla linea di terra: la dimensione è sempre la stessa, solo che la figura si sposta un po' in avanti;
3. si può far ruotare il piano intorno alla seconda traccia, fino a π₂: da ogni punto della seconda proiezione si costruisce il famoso angolo di 90 gradi con t₂α e si ribaltano le distanze.

Nel terzo caso bisogna avere cura che ogni lato della figura ribaltata sia uguale a quello vero.

In particolare, il lato perpendicolare a π₂ in seconda proiezione è un punto, mentre in pianta è già in vera lunghezza. Quando lo si ribalta deve restare lungo uguale. Quando si ruota una mano, il palmo non diventa più piccolo: la larghezza rimane quella.

Si possono prendere le distanze da una parte o dall'altra, ma bisogna sempre controllare che graficamente le cose tornino. Il ribaltamento è una rotazione, non una trasformazione che deforma: la figura ruota e non si restringe.

Il terzo modo è quello disegnato nel libro della docente per il piano proiettante in seconda (allegato, p. 44, fig. 48) e per la falda di un tetto in un piano proiettante in seconda (applicazione 5, p. 65): nel ribaltamento su π₂, spiega il libro, basta considerare la distanza da π₂ dei singoli vertici della falda, cioè il loro aggetto. Nella stessa applicazione c'è anche la falda in un piano parallelo alla linea di terra, che si ribalta sul terzo piano di proiezione considerando la distanza da questo dei singoli vertici.

> [!example] Disegno 10 · Il disegno nello spazio: il piano proiettante in seconda ruota su π₂
> ![[b12-spazio-proiettante-in-seconda-su-pi2.svg|620]]
>
> 1. Il piano α è perpendicolare a π₂: la seconda proiezione di tutta la figura cade su t₂α, e t₁α è perpendicolare alla LT.
> 2. Il lato AB è perpendicolare a π₂: A e B hanno la stessa seconda proiezione, A₂ ≡ B₂.
> 3. Il piano ruota intorno a t₂α. Ogni punto descrive un arco con centro nella sua seconda proiezione e raggio uguale al suo aggetto.
> 4. A fine rotazione A\*B\* è lungo come AB: la figura gira, ma non si restringe.

> [!example] Disegno 11 · Il disegno: il piano proiettante in seconda ribaltato su π₂
> ![[12-ribaltamento-piano-proiettante-in-seconda.svg|620]]
>
> Lo schema mostra il terzo modo, la rotazione intorno alla seconda traccia; la figura della prova non si conosce.
> 1. In seconda proiezione tutta la figura cade su t₂α; t₁α è perpendicolare alla LT.
> 2. Il lato AB è perpendicolare a π₂: in seconda proiezione è un punto (A₂ ≡ B₂), in prima proiezione A₁B₁ è perpendicolare alla LT ed è già in vera lunghezza.
> 3. Da ogni punto della seconda proiezione si manda la perpendicolare a t₂α e si riporta l'aggetto del punto. Si trovano A\*, B\*, C\*.
> 4. Controllo: A\*B\* deve essere uguale ad A₁B₁ (tre lineette).

### Quanto tempo ci vuole

Per gli esercizi di proiezioni ortogonali non servono quattro ore: al massimo due. Ma gli esercizi vanno fatti, prima, durante lo studio.

L'unico modo per risolvere i dubbi è risolverli adesso, durante il corso. Chi non li risolve ora rischia di non sostenere l'esame al primo anno, e di conseguenza di non poter seguire progettazione al secondo.

## L'ASSONOMETRIA OBLIQUA CON IL QUADRO VERTICALE

### Il quadro verticale: x e z restano veri, y si proietta

Come per ogni assonometria, bisogna sempre immaginare la terna ortogonale degli assi x, y, z che si proietta sul piano di quadro.

Questa volta il quadro è verticale e contiene gli assi x e z. Per questo:

- gli assi x e z coincidono con le loro proiezioni x′ e z′;
- l'angolo tra x′ e z′ resta di 90 gradi;
- le unità di misura su x′ e z′ restano vere.

Non coincide con la sua proiezione solo l'asse y, che sporge dal piano di quadro. Viene proiettato secondo la direzione di proiezione obliqua, e sul foglio appare come un asse y′ inclinato.

L'assonometria è obliqua, e nelle oblique le misure possono ridursi o anche aumentare: qui l'unità di misura cambia solo sull'asse y′.

Il risultato è che sul quadro il prospetto resta in vera forma, mentre la profondità si disegna lungo y′.

Nel libro della docente questa assonometria si chiama assonometria obliqua cavaliera frontale, o cavaliera propriamente detta (allegato, pp. 155 e 158-159): è quella in cui il piano di quadro coincide con il piano verticale π₂, così come nella cavaliera militare coincide con il piano orizzontale π₁.

> [!example] Disegno 12 · Il disegno nello spazio: il quadro verticale
> ![[12-spazio-assonometria-quadro-verticale.svg|620]]
>
> 1. Il quadro è verticale e contiene gli assi x e z: coincidono con x′ e z′, l'angolo tra loro resta retto e le unità restano vere.
> 2. L'asse y è perpendicolare al quadro. La direzione di proiezione è obliqua: il raggio che parte dall'unità Uy arriva sul quadro in un punto u′y dell'asse y′, che sul foglio è inclinato.
> 3. O, Uy e u′y formano un triangolo rettangolo in O: è la stessa squadretta della cavaliera militare, solo girata.

### I due metodi

Anche questa assonometria si può risolvere in due modi:

1. si cerca come si riduce o cresce l'unità di misura, in questo caso solo sull'asse y;
2. si costruisce l'assonometria usando anche la pianta, sfruttando la relazione di affinità tra la pianta ribaltata e la sua proiezione assonometrica sul quadro, esattamente come per l'altra assonometria obliqua.

Nel secondo metodo il disegno ha il prospetto sopra e la pianta sotto.

### La direzione di proiezione e il ribaltamento dell'asse y

Il problema è capire come la direzione di proiezione proietta l'asse y e la sua unità di misura.

Il triangolo che si forma tra l'origine O, l'unità Uy sull'asse y e la sua proiezione u′y è lo stesso triangolo che si formava con il quadro orizzontale della cavaliera militare: ora è soltanto girato, sta in verticale. È un po' più difficile da vedere, ma il ragionamento è lo stesso, e lo si vede bene sul modellino degli assi.

Il triangolo non sta sul quadro, quindi lo si ribalta sul quadro facendolo ruotare intorno a y′.

Nel ribaltamento l'asse y, ribaltato, si dispone a 90 gradi rispetto a y′: è l'asse y\*.

Nello spazio l'unità di misura è uguale su tutti e tre gli assi. Quindi su y\*, che è l'asse ribaltato sul quadro, si colloca la stessa unità di misura degli altri assi, riportandola col compasso. L'uguaglianza delle unità si segna sempre: non bisogna mai dimenticare questo segno.

Il segmento che unisce l'unità su y\* con l'unità scelta su y′ è l'ipotenusa del triangolo, cioè la direzione di proiezione assonometrica ribaltata. La docente la chiama s all'infinito e la disegna in azzurro.

Il libro della docente fa la stessa costruzione nella pagina «Cavaliera frontale. Ribaltamento della direzione di proiezione» (allegato, p. 158, fig. 14): la direzione di proiezione assonometrica, indicata S∞, si trova congiungendo l'unità di misura u′y con u\*y. Le profondità vere dei punti si prendono su y\* e si chiamano d\*, per esempio d\*(P) e d\*(Q); con le parallele alla direzione ribaltata si portano su y′.

Il libro ricorda anche un caso particolare (p. 159): se la direzione di proiezione è a 45° rispetto al quadro, l'unità su y′ resta uguale a quella vera, e né le lunghezze della pianta né le altezze del prospetto cambiano; pianta e alzato però si sovrappongono l'una all'altro.

Prima di disegnare l'oggetto, quindi, si disegna e si scrive che cosa avviene nello spazio; poi si fa il disegno su un'altra terna.

Per questo schema conviene prendere un'unità di misura un po' grande: la direzione di proiezione si vede meglio, e le parallele a essa vengono più precise.

> [!example] Disegno 13 · Il disegno: il ribaltamento dell'asse y
> ![[12-assonometria-quadro-verticale-ribaltamento-y.svg|620]]
>
> 1. Sul foglio, che è il quadro, si disegnano x′ orizzontale e z′ verticale, ad angolo retto, con l'unità vera u; y′ è inclinato e su y′ si sceglie l'unità u′y.
> 2. Il triangolo della squadretta si ribalta sul quadro intorno a y′: l'asse y ribaltato, y\*, è a 90 gradi rispetto a y′.
> 3. Su y\* si riporta col compasso l'unità vera, uguale a quella di x e z, e si segna l'uguaglianza.
> 4. Il segmento che unisce u su y\* con u′y su y′ è la direzione di proiezione ribaltata s\*, in azzurro.
> 5. Qualunque profondità vera h si prende su y\* e si porta su y′ con la parallela a s\*: si trova la profondità ridotta h′.

### Lo schema grafico libera dalla misura

Per il progetto ci sono alcuni suggerimenti. Il più importante è che l'unità assonometrica su y′ sia un po' più corta di quella vera, perché altrimenti l'edificio verrebbe troppo profondo.

Lo schema grafico della direzione di proiezione libera dalla misura. Non si deve ragionare in centimetri, contando un centimetro dopo l'altro: tutte le misure di profondità che si inseriscono vengono ridotte graficamente dalla direzione di proiezione. Si prende la misura vera su y\* e la si porta su y′ con la parallela a s\*.

### L'esercizio: il prospetto in vera forma

L'esercizio in aula parte da un solido semplice, di cui si conosce la pianta.

Prima si disegna il prospetto. Le misure del prospetto si prendono con lo strumento così come sono, perché sul quadro coincidono con le misure vere.

Il prospetto però non va calcato. Quando si costruisce il volume, la pianta, rispetto al piano di quadro, può stare un po' più avanti o essere attaccata: il solido starà davanti al prospetto e lo coprirà in parte.

### Dove collocare la pianta: il solido attaccato o staccato dal quadro

Di un parallelepipedo si sa subito una cosa: tutte le linee perpendicolari al piano di quadro, cioè gli spigoli di profondità, nel disegno sono parallele a y′.

L'unico punto delicato è capire dove sta la pianta, da dove inizia.

Il solido può essere:

- attaccato al piano di quadro, e allora la profondità parte da zero;
- staccato dal quadro, a una certa distanza, e allora la misura della profondità parte da quel punto.

La scelta è libera. Nelle tavole, per esempio, si può spostare il solido molto in avanti, per lasciare libero il prospetto da usare in un altro disegno ed evitare che si sovrappongano.

Se il solido non parte dal quadro, la distanza a cui inizia si prende su y\*, si misura lì la profondità e la si porta giù su y′ con la direzione di proiezione. Si fissa così la posizione del lato posteriore; poi, sempre su y\*, si aggiunge la profondità del solido e la si riporta su y′, fino al lato anteriore.

L'altezza rimane uguale: è quella vera del prospetto.

### La pianta assonometrica come affinità della pianta ribaltata

Resta da disegnare la pianta assonometrica.

Tra la pianta ribaltata sotto il prospetto e la pianta assonometrica c'è un'omologia, un'affinità:

- l'asse è la retta di intersezione tra il piano orizzontale e il piano di quadro, cioè x′;
- il centro è all'infinito, nella direzione di proiezione;
- y\* e y′ sono due rette corrispondenti, e infatti si incontrano sull'asse;
- i punti corrispondenti sono allineati con il centro, cioè stanno su rette tutte parallele tra loro.

Si comincia dalla retta che passa per A e per B. La retta della pianta, che nelle proiezioni ortogonali sta sul piano orizzontale, viene ribaltata giù e si chiama r\*₁.

Per trovare la sua corrispondente si tiene conto di y\* e y′: r\*₁ è parallela a y\*, quindi la sua corrispondente r′₁ è parallela a y′. Si costruisce la parallela a y′ da A′₁, e B′₁ si trova su di essa nella direzione del centro.

La retta che passa per B e per C, m\*₁, è parallela all'asse; quindi anche la sua corrispondente m′₁ è parallela all'asse. Si segna C′₁ e si chiude la figura.

Le cose devono tornare. La pianta assonometrica è il risultato dell'applicazione di un'omologia, e si disegna leggera, perché poi viene coperta dal solido.

Infine si alzano dai vertici della pianta assonometrica gli spigoli verticali, paralleli a z′: l'altezza non cambia.

Questa assonometria è molto usata.

Nel libro della docente questo secondo metodo è la pagina «Cavaliera frontale. Omologia di ribaltamento del piano π₁» (allegato, p. 159, fig. 15). Il libro scrive che la direzione dell'affinità obliqua, U∞, che lega la pianta ribaltata sul quadro alla sua immagine assonometrica, si trova unendo l'unità di misura assonometrica u′y con quella ribaltata u\*y.

Conviene fare attenzione a una cosa: nei due metodi y\* non è la stessa retta.

- Nel primo metodo si ribalta il triangolo della squadretta intorno a y′, e y\* è perpendicolare a y′.
- Nel secondo metodo si ribalta la pianta, cioè il piano orizzontale, intorno a x′, e y\* è perpendicolare a x′: è la y\* della pianta ribaltata sotto il prospetto. In questo caso il segmento che unisce u\*y e u′y non è più la direzione di proiezione S∞, ma la direzione U∞ dell'affinità.

Nella prima figura della p. 159 il libro mostra la stessa costruzione con il quadro che contiene gli assi y e z, e quindi con l'asse x proiettato obliquamente: cambiano solo i nomi, la pianta si ribalta intorno a y′ e l'asse ribaltato è x\*, perpendicolare a y′.

> [!example] Disegno 14 · Il disegno: il metodo con la pianta
> ![[12-assonometria-quadro-verticale-metodo-pianta.svg|620]]
>
> Lo schema è una ricostruzione: la forma del solido disegnato alla lavagna non si capisce dalla registrazione, qui è un parallelepipedo staccato dal quadro.
> 1. Si disegna il prospetto in vera forma sul quadro, con un segno leggero.
> 2. La pianta si ribalta sotto x′, girandola intorno alla retta comune al piano orizzontale e al quadro: è la pianta ribaltata A₁\*B₁\*C₁\*D₁\*, con y\* verso il basso. Il solido è staccato dal quadro: la profondità parte da y₀ su y\*.
> 3. Tra pianta ribaltata e pianta assonometrica c'è un'affinità di asse x′ con il centro all'infinito: y\* e y′ si incontrano sull'asse in O′, e i punti corrispondenti stanno sulle linee grigie tratteggiate, tutte parallele.
> 4. r₁\* = A₁\*B₁\* è parallela a y\*, quindi r₁′ è parallela a y′: su di essa, nella direzione del centro, si trova B₁′.
> 5. B₁\*C₁\* è parallela all'asse, quindi anche B₁′C₁′ è parallela all'asse: si trova C₁′ e si chiude la pianta assonometrica.
> 6. Dai vertici si alzano gli spigoli paralleli a z′, con l'altezza vera del prospetto. Lo spigolo nascosto si tratteggia.

### Esercitarsi da soli

Alla lavagna si disegna un solido semplice. Un solido più complesso spetta allo studente.

A casa bisogna porsi le domande da soli: questo lo so fare? E se aggiungo un pezzo al solido, se scavo qui, se tolgo una parte? Conviene inventare un solido e provare a farne l'assonometria, prima ancora di affrontarla nelle tavole.

> [!tip] Avvisi
> - La sessione di settembre è solo per chi a luglio ha finito le tavole: a settembre si riescono a fare al massimo due revisioni, e con due revisioni l'esame non si fa.
> - Prova n. 1: i voti sono a lettere; a parità di errori conta anche se il disegno è ordinato e preciso (senza il «più» non si arriva a B). Chi trova scritto «parliamone» deve andare dalla docente, rifare l'esercizio e mostrarle di averlo capito.
> - Costruire un modellino del diedro in cartoncino e rivedere la prima parte delle proiezioni ortogonali (il PDF, la sequenza delle operazioni): la docente farà altri esercizi sui ribaltamenti.
> - Venerdì 13 novembre alle 14, nell'aula dell'altro padiglione al piano di sopra, pomeriggio di domande (avviso su Teams): portare domande precise e gli appunti, «non ho capito niente» non è una domanda.
> - Prova n. 2: giovedì 26 novembre, secondo il calendario aggiornato.

## Collegamenti

La correzione della prova ripassa quasi tutto il programma delle prime settimane. Le regole dell'omologia, con il centro, l'asse e le coppie di elementi corrispondenti, sono quelle della [[02-proiezioni-e-omologia-schema|seconda lezione]], svolte passo per passo in [[02-omologia-dai-due-centri-passo-passo]]; il caso dell'asse all'infinito è un'omologia speciale, come l'omotetia e la traslazione viste allora. L'affinità ortogonale che completa il ribaltamento del triangolo è quella di [[02-affinita-ortogonale-passo-passo]], e il ripasso generale preparato per la prima prova è in [[00-ripasso-prova-1]].

Il ribaltamento dei piani proiettanti in prima e in seconda, con il modello del diedro, è l'argomento di [[07-il-ribaltamento]]; il ribaltamento del piano generico intorno alla prima traccia, con il raggio di rotazione e il punto B̄, è spiegato in [[09-ribaltamento-del-piano-generico]] e riassunto in [[PO 8 - Il ribaltamento]]. Le tracce di un piano ricavate dalle rette della figura, l'orizzontale e la frontale, e la retta perpendicolare al piano vengono da [[06-piani-ausiliari-e-perpendicolarita]] e da [[PO 6 - La perpendicolarità]].

L'assonometria con il quadro verticale è la sorella della [[11-assonometria-cavaliera-e-sezioni-dei-solidi|cavaliera militare]]: là il quadro coincideva con il piano orizzontale e restava vera la pianta, qui coincide con un piano verticale e resta vero il prospetto. In entrambi i casi la direzione di proiezione si trova ribaltando la stessa squadretta, e la pianta assonometrica nasce da un'affinità, la stessa trasformazione dell'omologia di ribaltamento. Il rapporto tra prospetto e pianta, uno sopra e l'altra sotto, è quello delle [[03-proiezioni-ortogonali-punto-e-rette|proiezioni ortogonali]], e i solidi da comporre e scavare richiamano i plastici dell'esercitazione di [[esercizio-3-casa-arzachena|Composizione architettonica]].

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[ES.GUIDATA_Omologia_01.pdf]]: l'esercizio guidato di omologia citato nella correzione, con il caso della coppia di punti corrispondenti (l'esercizio «madre») e quello della retta s con l'asse all'infinito
- [[2agg_Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: calendario aggiornato, con la Prova n. 2 il 26 novembre
- [[566_3.pdf]]: allegato multimediale del libro della docente. Per la correzione della prova: le applicazioni 1-12 di omologia piana (pp. 16-27); «Rappresentazione di piani» (p. 34), «Condizioni di perpendicolarità retta-piano» (p. 43), «Il ribaltamento dei piani proiettanti» (p. 44); applicazioni 4 e 5, vera grandezza di figure e falde in piani generici, proiettanti in seconda e paralleli alla linea di terra (pp. 59-65); applicazione 19, perpendicolare a una falda (pp. 112-113). Per l'assonometria: «Cavaliera frontale. Ribaltamento della direzione di proiezione» (p. 158) e «Omologia di ribaltamento del piano π₁» (p. 159); applicazioni 10 e 12, assonometria cavaliera frontale (pp. 197-199 e 204-206); applicazione 11, assonometria cavaliera associata alle proiezioni ortogonali (pp. 200-203)
