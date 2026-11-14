---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-11-05
tags: [geometria-descrittiva, bozza]
---

# Intersezione tra retta e piano, distanza punto–piano e segno di sezione

> [!info] Note collegate
> Sbobina: [[10-intersezione-retta-figura-e-sezioni]]
>
> Bozza precedente: [[09-ribaltamento-del-piano-generico]] · Successiva: [[11-assonometria-cavaliera-e-sezioni-dei-solidi]]
>
> Argomenti collegati: [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]] · [[05-appartenenza-e-rette-ausiliarie]] · [[03-proiezioni-ortogonali-punto-e-rette]]

La lezione di giovedì 5 novembre affronta un problema che torna in quasi tutti gli esercizi di geometria descrittiva: trovare il punto in cui una retta incontra un piano.

Il procedimento è sempre lo stesso, sia quando il piano è dato con le sue tracce sia quando è dato con una figura piana. Da qui la docente costruisce due esercizi per casa, da risolvere mettendo insieme le cose già studiate:

- la distanza di un punto da un piano dato con una figura;
- il segmento lungo 3 cm, perpendicolare a una figura, che esce da un suo punto e si costruisce con il procedimento a ritroso.

La seconda parte della lezione è dedicata alle piante di un progetto distribuito in aula, al modo in cui si legge una scala tagliata dal piano di sezione e al segno di sezione a baionetta.

La registrazione comincia a lezione avviata: la prima parte, con il procedimento in forma canonica, qui è ricostruita a partire da ciò che la docente richiama subito dopo. Il progetto commentato in aula non lo abbiamo, quindi quella parte è riportata solo per i principi generali.

Questi argomenti fanno parte della Prova n. 2 di geometria descrittiva, che il calendario aggiornato fissa a giovedì 26 novembre.

## L'INTERSEZIONE TRA UNA RETTA E UN PIANO

### Il procedimento: un piano ausiliario per la retta

Che il piano sia rappresentato in forma canonica, cioè con le tracce, o in forma tecnica, cioè con una figura, concettualmente il procedimento non cambia (la differenza tra le due forme è spiegata anche nel manuale).

Per trovare il punto in cui la retta r incontra un piano si fanno tre passaggi:

1. per la retta si fa passare un piano ausiliario γ, e il più comodo è il piano proiettante in prima;
2. si trova la retta n di intersezione tra γ e il piano dato;
3. r e n stanno tutte e due su γ, quindi si incontrano: il loro punto comune è il punto di intersezione cercato.

Il piano proiettante in prima è comodo perché tutto ciò che gli appartiene ha la prima proiezione sulla prima traccia.

Quindi su γ₁ coincidono più cose:

- la prima proiezione della retta, r₁, perché γ contiene r;
- e la prima proiezione della retta di intersezione, n₁, perché anche n sta su γ.

La docente insiste su questo punto: bisogna mettere insieme le cose. Sapere che n₁ coincide con γ₁ e con r₁ significa avere già, senza provare altro, la prima proiezione della retta di intersezione tra i due piani.

### In forma canonica: il piano dato con le tracce

Quando il piano α è dato con le tracce, il procedimento è sequenziale, una cosa dopo l'altra.

Il piano γ proiettante in prima che contiene r ha la prima traccia coincidente con r₁, prolungata fino alla linea di terra; la seconda traccia è perpendicolare alla linea di terra e parte dal punto in cui t₁γ la incontra.

La retta n = α ∩ γ ha le tracce sulle tracce di tutti e due i piani:

- la prima traccia T₁ₙ è il punto in cui t₁α incontra t₁γ;
- la seconda traccia T₂ₙ è il punto in cui t₂α incontra t₂γ.

La prima proiezione n₁ coincide con t₁γ, e quindi con r₁. La seconda proiezione n₂ unisce T₂ₙ con (T₁ₙ)₂, la seconda proiezione della prima traccia, che sta sulla linea di terra.

Il punto di intersezione P si legge in seconda proiezione: P₂ è dove n₂ incontra r₂. Con la linea di richiamo si trova P₁ su r₁.

> [!example] Disegno 1 (ricostruito: questa parte della lezione non è registrata) · Il disegno
> ![[b10-intersezione-retta-piano-tracce.svg|620]]
>
> 1. Il piano α è dato con le tracce t₁α e t₂α; la retta r con r₁ e r₂.
> 2. Per r fai passare γ proiettante in prima: t₁γ coincide con r₁ prolungata fino alla LT; t₂γ è perpendicolare alla LT.
> 3. T₁ₙ è il punto in cui t₁α incontra t₁γ; T₂ₙ è il punto in cui t₂α incontra t₂γ.
> 4. Da T₁ₙ sali con il richiamo fino alla LT: (T₁ₙ)₂. n₂ unisce (T₁ₙ)₂ e T₂ₙ; n₁ coincide con t₁γ.
> 5. Dove n₂ incontra r₂ c'è P₂; con il richiamo trovi P₁ su r₁.

> [!example] Disegno 2 (proposto, non fatto a lezione) · Il disegno nello spazio
> ![[b10-spazio-intersezione-retta-piano-tracce.svg|620]]
>
> 1. Il piano γ è verticale e contiene r: la sua traccia su π₁ è r₁.
> 2. γ taglia α lungo la retta n, che va da T₁ₙ (su π₁) a T₂ₙ (su π₂).
> 3. r e n stanno sullo stesso piano γ, quindi si incontrano in P, il punto in cui r buca α.

### In forma tecnica: il piano dato con una figura

L'esercizio svolto in aula chiede il punto di intersezione tra una retta e un piano dato con una figura, il triangolo ABC.

In questa forma il piano non si rappresenta neanche con le sue tracce. Il procedimento però è sempre lo stesso: per la retta si fa passare un piano proiettante in prima, e la figura, anche se non è data con le tracce, si taglia comunque con questo piano.

Questa volta si scrive γ₁, la prima proiezione del piano, e non t₁γ, perché le tracce non si disegnano.

Su γ₁ coincidono r₁ e n₁, la prima proiezione della retta n di intersezione tra γ e il piano della figura. Si procede così:

1. si fa coincidere γ₁ con r₁: γ è un piano proiettante in prima e contiene la retta;
2. n₁ coincide con γ₁ e incontra i lati del triangolo in due punti, che si chiamano per esempio L₁ (sul lato A₁B₁) e M₁ (sul lato B₁C₁);
3. i punti sono allineati lungo le linee di richiamo, quindi da L₁ si trova L₂ sul lato A₂B₂ e da M₁ si trova M₂ sul lato B₂C₂;
4. la retta L₂M₂ è la seconda proiezione n₂ della retta di intersezione;
5. il punto di intersezione sta dove si incontrano n₂ ed r₂: lì c'è P₂, esattamente come sul manuale;
6. con la linea di richiamo si trova anche P₁ su r₁.

> [!example] Disegno 3 · Il disegno
> ![[10-intersezione-retta-figura-piana.svg|620]]
>
> 1. Il piano è dato con il triangolo ABC; la retta r con r₁ e r₂.
> 2. Per r fai passare γ proiettante in prima: γ₁ coincide con r₁, e anche con n₁.
> 3. n₁ incontra i lati in L₁ (su A₁B₁) e M₁ (su B₁C₁).
> 4. Richiama L₂ su A₂B₂ e M₂ su B₂C₂: L₂M₂ è n₂.
> 5. Dove n₂ incontra r₂ c'è P₂; con il richiamo trovi P₁ su r₁.
> 6. Tratteggia la parte di r coperta dal triangolo.

> [!example] Disegno 4 · Il disegno nello spazio
> ![[10-spazio-intersezione-retta-figura-piana.svg|620]]
>
> 1. Il piano γ è verticale e contiene r: la sua prima traccia coincide con r₁.
> 2. γ taglia il triangolo lungo il segmento LM, che sta sulla retta n.
> 3. r e n stanno su γ e si incontrano in P, il punto in cui r buca il piano del triangolo.

### Le parti nascoste

Trovato il punto P, il disegno va concluso: la retta attraversa la figura, e da P in poi la parte che sta dietro (in seconda proiezione) o sotto (in prima proiezione) il triangolo non si vede.

Dove la figura la copre, quindi, la retta si tratteggia.

In seconda proiezione è nascosta la parte di r che ha l'aggetto minore di quello del piano, cioè che sta dietro il triangolo rispetto a chi guarda π₂; in prima proiezione è nascosta la parte che ha la quota minore, cioè che sta sotto il triangolo rispetto a chi guarda dall'alto.

### La retta n e la retta di massima pendenza

Si potrebbe dire che n è anche una retta di massima pendenza. La docente chiede però di riconoscere che cosa sia n di fatto: è la retta di intersezione tra il piano γ e il piano della figura.

In questo esercizio la retta di massima pendenza non c'entra, perché il piano γ non è perpendicolare al piano della figura: è semplicemente un piano proiettante in prima che contiene r.

La retta di massima pendenza di un piano si trova invece tagliandolo con un piano perpendicolare, come si è visto nel ribaltamento del piano generico (sbobina [[09-ribaltamento-piano-generico]]): un piano proiettante in prima è perpendicolare al piano α quando la sua prima traccia è perpendicolare a t₁α.

Questo succede, per esempio, quando la retta r è perpendicolare al piano, e allora la retta n diventa davvero una retta di massima pendenza. È proprio il caso della distanza di un punto da un piano.

> [!abstract] Da ricordare
> - Intersezione retta–piano: per la retta si fa passare un piano ausiliario γ proiettante in prima; si trova n = γ ∩ piano; il punto cercato è r ∩ n.
> - Su γ₁ coincidono r₁ e n₁; il punto si legge in seconda proiezione, dove n₂ incontra r₂.
> - Forma canonica: n ha le tracce T₁ₙ = t₁α ∩ t₁γ e T₂ₙ = t₂α ∩ t₂γ. Forma tecnica: n₁ taglia i lati della figura in L₁ e M₁, e n₂ = L₂M₂.
> - n è una retta di massima pendenza solo se γ è perpendicolare al piano.

## GLI ESERCIZI: LA DISTANZA PUNTO–PIANO E IL SEGMENTO PERPENDICOLARE

### La distanza di un punto da un piano

La distanza di un punto P da un piano α è il segmento PH che va da P al piede H della perpendicolare condotta da P al piano.

Il procedimento in avanti ha tre passaggi:

1. per P si costruisce la retta r perpendicolare ad α;
2. si trova il punto H in cui r incontra α, con il procedimento dell'intersezione appena visto;
3. si porta il segmento PH in vera grandezza, perché nelle proiezioni appare accorciato.

Con il piano dato con le tracce l'esercizio era già stato assegnato: bastava trovare le tracce del piano e costruire per il punto P la retta perpendicolare. Per il teorema di Monge la retta è perpendicolare al piano se le sue proiezioni sono perpendicolari alle tracce omonime, quindi:

- r₂ è perpendicolare a t₂α
- e r₁ è perpendicolare a t₁α.

Per trovare H si fa passare per r il piano γ proiettante in prima. Siccome t₁γ coincide con r₁, che è perpendicolare a t₁α, il piano γ è perpendicolare ad α: la retta n = α ∩ γ è quindi una retta di massima pendenza di α. H₂ sta dove n₂ incontra r₂, e H₁ sta su r₁.

Per la vera grandezza si ribalta γ su π₁ intorno alla sua prima traccia, come nel ribaltamento dei piani proiettanti in prima: ogni punto si porta sulla perpendicolare a t₁γ condotta dalla sua prima proiezione, a una distanza uguale alla sua quota. Il segmento P\*H\* che si ottiene è la distanza vera.

> [!example] Disegno 5 (proposto, non fatto a lezione) · Il disegno: la distanza di P da α in forma canonica
> ![[b10-distanza-punto-piano-tracce.svg|620]]
>
> 1. Per P costruisci r: r₂ perpendicolare a t₂α, r₁ perpendicolare a t₁α (segna gli angoli retti).
> 2. Il piano γ proiettante in prima per r ha t₁γ coincidente con r₁ e t₂γ perpendicolare alla LT.
> 3. T₁ₙ è dove t₁α incontra t₁γ, T₂ₙ è dove t₂α incontra t₂γ: n₂ unisce (T₁ₙ)₂ e T₂ₙ.
> 4. Dove n₂ incontra r₂ c'è H₂; con il richiamo trovi H₁ su r₁.
> 5. Ribalta γ su π₁: da P₁ e da H₁ traccia le perpendicolari a t₁γ e riporta le quote di P e di H (una e due lineette). P\*H\* è la distanza vera.

> [!example] Disegno 6 (proposto, non fatto a lezione) · Il disegno nello spazio
> ![[b10-spazio-distanza-punto-piano.svg|620]]
>
> 1. Il piano α è una falda poco inclinata, come un tetto; P sta sopra.
> 2. La retta r per P è perpendicolare ad α; il piano verticale γ che la contiene taglia α lungo n, una retta di massima pendenza.
> 3. H è il punto in cui r incontra n: il segmento PH, ad angolo retto con il piano, è la distanza.

### Esercizio 1: la distanza punto–piano con la figura piana

Il primo esercizio per casa è trovare la distanza punto–piano ponendo il punto esterno alla stessa figura piana, il triangolo, dell'esercizio fatto in aula. Bisogna lavorare finché le cose si sistemano in modo tale che il disegno sia vero.

Senza le tracce non si può usare il teorema di Monge nella forma con le tracce. Si torna allora alla definizione: una retta è perpendicolare a un piano quando è perpendicolare a due rette del piano, e le rette che aiutano sono l'orizzontale e la frontale del triangolo.

La perpendicolare r per P si costruisce quindi così:

- r₁ perpendicolare alla prima proiezione dell'orizzontale, o₁;
- r₂ perpendicolare alla seconda proiezione della frontale, f₂.

Poi si cerca il piede H esattamente come nell'esercizio in aula: γ₁ coincide con r₁, taglia i lati del triangolo in L₁ e M₁, si richiamano L₂ e M₂, si disegna n₂ = L₂M₂, e H₂ è dove n₂ incontra r₂.

> [!example] Disegno 7 (proposto, non fatto a lezione) · Esercizio 1: la perpendicolare e il suo piede
> ![[b10-es1-perpendicolare-dalla-figura.svg|620]]
>
> 1. Disegna l'orizzontale o del triangolo per B: o₂ parallela alla LT, che incontra A₂C₂; o₁ unisce B₁ con il punto richiamato su A₁C₁.
> 2. Disegna la frontale f per A: f₁ parallela alla LT, che incontra B₁C₁; f₂ unisce A₂ con il punto richiamato su B₂C₂.
> 3. Da P₁ traccia r₁ perpendicolare a o₁; da P₂ traccia r₂ perpendicolare a f₂ (segna gli angoli retti).
> 4. γ₁ coincide con r₁ e taglia i lati in L₁ e M₁; richiama L₂ e M₂ e disegna n₂.
> 5. Dove n₂ incontra r₂ c'è H₂; con il richiamo trovi H₁ su r₁. PH è la distanza, ancora accorciata.

Per la vera grandezza di PH si può ribaltare γ in forma tecnica, come nel ribaltamento del piano generico fatto con un'orizzontale (sbobina [[09-ribaltamento-piano-generico]]): l'asse di rotazione è l'orizzontale di γ che passa per H.

Così il punto H sta sull'asse e non si muove, e per P si riporta, sulla perpendicolare a γ₁ condotta da P₁, non la quota intera ma la differenza di quota tra P e H, cioè la distanza di P₂ dalla parallela alla linea di terra condotta per H₂.

> [!example] Disegno 8 (proposto, non fatto a lezione) · Esercizio 1: la distanza in vera grandezza
> ![[b10-es1-distanza-vera-grandezza.svg|620]]
>
> 1. Per H₂ traccia la parallela alla LT: è la seconda proiezione dell'orizzontale di γ alla quota di H, l'asse di rotazione.
> 2. Misura la distanza di P₂ da questa parallela (una lineetta).
> 3. Da P₁ traccia la perpendicolare a γ₁ e riportaci quella distanza: trovi P\*.
> 4. H sta sull'asse e resta fermo: H\* coincide con H₁. P\*H\* è la distanza vera di P dal triangolo.

### Esercizio 2: il segmento perpendicolare lungo 3 cm, a ritroso

La docente introduce il secondo esercizio con un esempio: se la figura fosse il tetto e si dovesse costruire un elemento perpendicolare al tetto, come si farebbe?

La consegna è questa:

1. disegnare le due proiezioni di una figura piana, per esempio un triangolo;
2. individuare un punto che appartiene alla figura, a piacere, ma che non sia uno dei vertici e che non stia su un lato;
3. da quel punto costruire un segmento perpendicolare alla figura, di lunghezza 3 cm.

La lunghezza la sceglie chi disegna, perché dipende da come è disegnata la figura: basta dichiararla, per esempio «segmento di lunghezza 3 cm».

Per il punto della figura si usa una retta del piano, come si è già fatto: si disegna un'orizzontale che attraversa il triangolo e si sceglie il punto Q su di essa, dentro la figura.

La docente lo presenta come un esercizio già fatto, in cui bisogna solo andare indietro.

Si tratta della costruzione di una perpendicolare passante per il punto, che questa volta è già il piede della perpendicolare, e deve andare su. La perpendicolare si costruisce come nell'esercizio 1: r₁ perpendicolare a o₁ e r₂ perpendicolare a f₂.

I 3 cm però non si possono misurare nelle proiezioni ortogonali, perché il segmento è inclinato rispetto a tutti e due i piani di proiezione e in entrambe le proiezioni appare accorciato.

Bisogna quindi ragionare sul procedimento in avanti e fare il procedimento a ritroso:

- in avanti, nell'esercizio della distanza, si aveva il segmento nelle proiezioni e se ne cercava la vera grandezza con il ribaltamento;
- a ritroso, si misura la lunghezza nel ribaltamento, dove le misure sono vere, e poi si riporta il segmento nelle proiezioni.

La docente lo considera un bell'esercizio proprio perché obbliga a mettere insieme le cose. Se gli esercizi arrivano sempre preparati, come pasticcini, non si impara niente: bisogna chiedersi com'è fatto il disegno, perché si sta facendo quel passaggio, qual è il procedimento in avanti e qual è il procedimento indietro, applicato alla figura piana.

La costruzione è questa:

1. si sceglie un punto qualunque S sulla perpendicolare r, con S₂ su r₂ e S₁ su r₁;
2. si ribalta il piano γ proiettante in prima che contiene r (t₁γ coincide con r₁) su π₁: Q\* e S\* stanno sulle perpendicolari a r₁ condotte da Q₁ e da S₁, alla distanza delle rispettive quote;
3. la retta Q\*S\* è la perpendicolare ribaltata, r\*, in vera grandezza: su di essa, a partire da Q\* e verso S\* (cioè verso l'alto), si misurano 3 cm e si trova E\*;
4. a ritroso, da E\* si torna su r₁ con la perpendicolare a r₁: lì c'è E₁;
5. con la linea di richiamo si trova E₂ su r₂.

Il segmento QE, disegnato con Q₁E₁ e Q₂E₂, è il segmento perpendicolare alla figura lungo 3 cm.

Come controllo, la distanza di E\* da E₁ deve essere uguale alla quota di E, cioè alla distanza di E₂ dalla linea di terra.

> [!example] Disegno 9 (proposto, non fatto a lezione) · Esercizio 2: il segmento QE lungo 3 cm
> ![[b10-es2-segmento-3-cm.svg|660]]
>
> 1. Nel triangolo disegna l'orizzontale o (o₂ parallela alla LT) e scegli Q su di essa, dentro la figura; disegna anche la frontale f per Q.
> 2. Da Q₁ traccia r₁ perpendicolare a o₁; da Q₂ traccia r₂ perpendicolare a f₂.
> 3. Scegli un punto qualunque S su r (S₂ su r₂, S₁ su r₁ con il richiamo).
> 4. Ribalta γ su π₁ intorno a t₁γ, che coincide con r₁: da Q₁ e da S₁ le perpendicolari a r₁ con le quote di Q e di S (una e due lineette). Q\*S\* è r\*.
> 5. Su r\* misura 3 cm da Q\*: trovi E\*.
> 6. Da E\* torna su r₁ con la perpendicolare: E₁. Con il richiamo trovi E₂ su r₂. Ripassa Q₁E₁ e Q₂E₂.

> [!example] Disegno 10 (proposto, non fatto a lezione) · Il disegno nello spazio
> ![[b10-spazio-es2-segmento-3-cm.svg|620]]
>
> 1. Il segmento QE esce dal triangolo ad angolo retto, ed è perpendicolare anche all'orizzontale o della figura.
> 2. Il piano verticale γ contiene QE: la sua traccia su π₁ contiene la prima proiezione Q₁E₁.
> 3. Q₁E₁ è più corto di 3 cm: per misurare il segmento bisogna ribaltare γ.

> [!abstract] Da ricordare
> - Distanza punto–piano: perpendicolare per il punto, piede H con il piano ausiliario, vera grandezza con il ribaltamento.
> - Con le tracce: r₁ ⊥ t₁α, r₂ ⊥ t₂α. Con la figura: r₁ ⊥ o₁, r₂ ⊥ f₂.
> - Nelle proiezioni le lunghezze dei segmenti inclinati non si misurano: si misurano nel ribaltamento e poi si riportano indietro (procedimento a ritroso).
> - Ribaltando γ intorno a un'orizzontale per un punto del segmento, quel punto resta fermo e si riportano le differenze di quota.

## LA PIANTA E IL SEGNO DI SEZIONE

### Leggere le piante di un progetto

Nella seconda parte della lezione la docente distribuisce un progetto e chiede di segnarvi sopra la sezione: c'è una sezione trasversale.

In un disegno di progetto si possono trovare, una accanto all'altra, piante diverse dello stesso edificio. Se l'edificio si dispone su tre piani, per esempio, si possono avere tre piante affiancate:

- una tagliata al seminterrato,
- una al piano terra
- e una al piano primo.

Non è un errore: basta dichiararlo. Chi guarda riconosce comunque di quale piano si tratta. Il seminterrato, per esempio, si capisce dai muri che a sinistra e a destra rinforzano questo assunto.

In pianta bisogna sempre immaginare che il volume sia tagliato da un piano orizzontale: il taglio orizzontale è quello che restituisce la pianta.

Guardando da vicino la pianta del seminterrato si vede che la scala sale e viene intercettata dal piano di sezione. Contando i gradini, uno dopo l'altro fino a dieci, si capisce più o meno a che quota taglia quella pianta.

La parte di scala sotto il piano di sezione è quella tagliata e vista; il resto della scala, che sta sopra, risulta tratteggiato, perché è la proiezione della scala che continua a salire.

Nella pianta si leggono anche gli elementi attraversati dal taglio:

- le porte, per esempio quella dell'ingresso e quella del bagno;
- i tramezzi, che di solito sono da 10 cm;
- e le pareti più spesse, per esempio quella da 15 cm verso la scala esterna.

Nella pianta del piano terra la sezione taglia tutta la scala e passa per la porta d'ingresso; al piano superiore la sezione si sposta un po' più su e non passa più dalla porta.

All'ultimo piano il corrimano della scala resta basso, mentre ai piani inferiori c'erano dei muri: le linee che in pianta sembrano il corrimano possono essere in realtà quelle di un armadio, che in parte sta nella camera da letto e in parte fuori, e che fa da tramezzo.

### La scala tagliata in pianta: uno o due segni

Dove il piano di sezione intercetta la scala, in pianta si interrompe il disegno dei gradini con un segno, una linea.

Secondo la norma si dovrebbero fare:

- un solo segno quando sotto non c'è un'altra rampa;
- due segni quando si taglia già a una quota superiore, e c'è una scala sopra e una scala sotto.

Questa sarebbe la norma, ma nei disegni se ne trovano spesso già due.

Il PDF della docente sul disegno della scala mostra le due situazioni. Convenzionalmente il disegno dei gradini si interrompe con una linea inclinata a 45° o a 60°, oltre la quale si può disegnare il sottoscala, se esiste, oppure, con un tratteggio, la proiezione dei gradini che proseguono verso il pianerottolo alla quota superiore. Nella pianta di un piano intermedio le linee trasversali di sezione sono due, e i gradini che salgono dal piano inferiore, visti dall'alto, non si tratteggiano.

> [!example] Disegno 11 (proposto, non fatto a lezione, dal PDF «Il disegno della scala») · Il disegno
> ![[b10-scala-uno-o-due-segni.svg|620]]
>
> 1. Piano terra: la prima rampa sale e viene tagliata; il segno inclinato interrompe i gradini.
> 2. Oltre il segno la scala continua sopra il piano di sezione: i gradini, il pianerottolo e la seconda rampa si tratteggiano.
> 3. Piano intermedio: c'è una scala sopra e una sotto, quindi i segni sono due; i gradini che salgono dal piano inferiore si disegnano pieni.

### Piante, prospetti e sezioni vanno insieme

Da questa lettura la docente ricava una regola di metodo: non è ammissibile trattare i prospetti e le sezioni separatamente dalle piante.

Non si lavora prendendo le misure sul foglio e copiandole. Prospetti e sezioni si ricostruiscono a partire dalla pianta, tirando su le linee della proiezione ortogonale.

Qualcosa si capirà e qualcosa no, ma bisogna capire come i disegni vanno insieme.

### Il segno di sezione a baionetta

La sezione che piega, passando da un piano verticale a un altro parallelo, si chiama sezione a baionetta.

La norma dice che il segno di sezione andrebbe disegnato per tutto il suo percorso; di fatto è talmente oneroso che non lo si fa mai, e non si disegna mai tutta la linea all'interno del disegno.

Nella pratica si disegnano:

- i tratti alle estremità, con le frecce nel senso della vista;
- e l'angolo dove la sezione gira, in modo che chi guarda il disegno ne percorra il tracciato.

L'angolo va disegnato sia in alto sia in basso: bisogna dire che la sezione gira qui, scende giù e gira là. In mezzo la continuità della linea è semplicemente interrotta, ma dove girano gli angoli va segnato l'angolo retto.

> [!example] Disegno 12 · Il disegno: il segno di sezione a baionetta
> ![[10-segno-sezione-a-baionetta.svg|560]]
>
> 1. La sezione a baionetta è fatta con piani verticali paralleli, collegati da un tratto che gira ad angolo retto.
> 2. Disegna i tratti alle due estremità, con le frecce nel senso della vista.
> 3. Disegna gli angoli dove la sezione gira, in basso e in alto, segnando l'angolo retto.
> 4. In mezzo la linea si interrompe; nello schema il puntinato grigio mostra solo il percorso del taglio.

Sono sezioni fatte con piani verticali, o frontali: il segno di sezione è infatti una traccia, quella del piano di sezione, che seziona tutti i muri trasversali.

Le sezioni possono presentare delle difficoltà, ma queste non ne presentano, perché sono tutte fatte con piani verticali e orizzontali.

Si può anche fare altrimenti. L'anno precedente uno studente ha disegnato la casa su un piano inclinato: di solito si parte dalla figura sul piano inclinato e se ne trova la vera grandezza e forma, mentre lui è partito dalla vera grandezza e forma e l'ha messa sul piano inclinato. È un esercizio al contrario, che mette in gioco molte cose e dà un disegno, dal punto di vista strettamente geometrico, interessante, una sorta di assonometria.

> [!tip] Avvisi e consegne
> - Esercizio 1 per la prossima volta: la distanza punto–piano, con il piano dato con la figura piana dell'esercizio in aula e il punto esterno alla figura.
> - Esercizio 2: le due proiezioni di un triangolo, un punto della figura che non sia un vertice né stia su un lato, e da quel punto il segmento perpendicolare lungo 3 cm (o un'altra misura scelta e dichiarata), con il procedimento a ritroso.
> - I fogli da consegnare devono essere A4, in una cartellina.
> - Segnare la sezione sul progetto distribuito e continuare le sezioni della casa scelta: si possono fare tutte le sezioni che si vogliono.
> - Il lavoro sui casi studio non va lasciato all'ultimo momento.
> - Dalla lezione successiva si va avanti con l'assonometria ortogonale.
> - La Prova n. 2 di geometria descrittiva è giovedì 26 novembre.

## Collegamenti

L'intersezione tra retta e piano usa tutti gli strumenti delle lezioni precedenti.

Il piano ausiliario proiettante in prima e la regola per cui tutto ciò che gli appartiene ha la prima proiezione sulla prima traccia vengono dai [[04-rette-e-piani-nelle-varie-posizioni|piani nelle varie posizioni]]; la ricerca di un punto della figura con l'orizzontale e la frontale viene dalle [[05-appartenenza-e-rette-ausiliarie|condizioni di appartenenza]]; la perpendicolare a un piano, con le tracce o con l'orizzontale e la frontale, è il teorema di Monge studiato in [[06-piani-ausiliari-e-perpendicolarita]].

La vera grandezza della distanza si ottiene con il [[07-il-ribaltamento|ribaltamento dei piani proiettanti]], e il ribaltamento intorno a un'orizzontale, con le differenze di quota, è quello del piano generico in forma tecnica ([[09-ribaltamento-del-piano-generico]], sbobina [[09-ribaltamento-piano-generico]]), dove compare anche la retta di massima pendenza. Il procedimento a ritroso rovescia lo stesso ragionamento, come lo studente che dalla vera grandezza è risalito alla figura sul piano inclinato.

Lo stesso schema, cioè un piano che ne taglia un altro lungo una retta e la retta che incontra gli spigoli, torna subito nella lezione successiva ([[11-assonometria-cavaliera-e-sezioni-dei-solidi]], sbobina [[11-assonometria-obliqua-cavaliera-militare]]): le sezioni dei solidi si risolvono cercando, una faccia alla volta, l'intersezione tra il piano secante e il piano della faccia.

La lettura della pianta come sezione orizzontale e il legame obbligato tra pianta, prospetti e sezioni riprendono le [[03-proiezioni-ortogonali-punto-e-rette|proiezioni ortogonali]] e gli appunti [[PO 1 - Il metodo di Monge]]; il disegno della scala e i segni di sezione servono direttamente per le sezioni e per le tavole della casa da studiare (Villa Tugendhat o Villa Le Lac).

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[il-disegno-della-scala.pdf]]: la scala in pianta e in sezione, con uno o due segni di interruzione
- [[linee guida per lo studio delle architetture proposte _2026-2027.pdf]]: sezioni, scale e dettagli da ridisegnare per la casa scelta
- [[2agg_Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: data della Prova n. 2 (26 novembre)
