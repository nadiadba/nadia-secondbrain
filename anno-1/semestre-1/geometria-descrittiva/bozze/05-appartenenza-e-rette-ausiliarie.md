---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-15
tags: [geometria-descrittiva, bozza]
---

# Piano proiettante in seconda, retta e piano generico, appartenenza e rette ausiliarie

> [!info] Note collegate
> Sbobina: [[05-piani-rette-e-appartenenza]]
>
> Bozza precedente: [[04-rette-e-piani-nelle-varie-posizioni]] · Successiva: [[06-piani-ausiliari-e-perpendicolarita]]

La lezione di giovedì 15 ottobre completa il quadro dei piani e delle rette nel metodo di Monge e lo mette al servizio di un'unica domanda: quando un elemento appartiene a un altro? Nella lezione del 13 ottobre si erano viste le rette e i piani nelle posizioni particolari, il piano proiettante in prima e le condizioni di appartenenza; qui si aggiunge il piano proiettante in seconda, si arriva alla retta generica e al piano generico, che non hanno nessuna posizione particolare, e si impara a riconoscere quali piani possono contenere una retta data. L'ultimo passo è il punto: un punto appartiene a un piano se sta su una retta del piano, e le rette più comode per dimostrarlo sono le due ausiliarie, l'orizzontale e la frontale. Tutto va verificato sul modello tridimensionale: la docente insiste che queste regole non si imparano a memoria, si vedono, e poi restano in testa.

## IL PIANO PROIETTANTE IN SECONDA

### Com'è fatto e come si costruisce nel modello

I piani si nominano a seconda della posizione che assumono rispetto ai tre piani di proiezione. Il piano proiettante in prima, visto la volta scorsa, è perpendicolare a π₁; il piano proiettante in seconda è invece perpendicolare a π₂ e inclinato rispetto a π₁ e a π₃. Nel modello si costruisce con un cartoncino che stia in piedi da solo e che entri nel modello, in modo da poterlo portare sempre a lezione. Guardandolo si vede subito la sua caratteristica: la prima traccia t₁α è perpendicolare alla linea di terra, mentre la seconda traccia t₂α è inclinata quanto è inclinato il piano; la terza traccia t₃α, sul piano laterale, è parallela alla linea di terra e incontra t₂α sull'asse verticale.

Quando si apre il modello, i tre piani di proiezione finiscono sovrapposti sul foglio. Per questo non si scrive π₁, π₂ e π₃ come se fossero tre zone separate, ma π₁ ≡ π₂ ≡ π₃.

> [!example] Il disegno: le tre tracce del piano proiettante in seconda
> ![[05-piano-proiettante-in-seconda-tre-tracce.svg|620]]
>
> 1. Si disegnano la linea di terra e l'asse verticale (a destra c'è π₃, ribaltato quando si apre il modello).
> 2. t₁α parte da un punto della LT ed è perpendicolare alla LT (segnare l'angolo retto).
> 3. t₂α parte dallo stesso punto della LT, inclinata come il piano.
> 4. t₃α è parallela alla LT e parte dal punto in cui t₂α incontra l'asse.
> 5. Si scrive π₁ ≡ π₂ ≡ π₃.

> [!example] Il disegno nello spazio
> ![[05-spazio-piano-proiettante-in-seconda.svg|620]]
>
> 1. Il piano α è perpendicolare a π₂: contiene tutte le rette perpendicolari a π₂, come AB.
> 2. Ogni punto del triangolo, proiettato su π₂, cade sulla seconda traccia t₂α; per questo A₂ coincide con B₂.
> 3. Sul pavimento π₁ la prima traccia t₁α è perpendicolare alla LT.

### Una figura sul piano: la seconda proiezione sta sulla seconda traccia

Se si disegna un triangolo sul cartoncino e lo si guarda di taglio, come lo vedrebbe π₂, non si vede più un triangolo ma una linea. Lo stesso accade con un cerchio messo perpendicolare alla lavagna. Mandando dai vertici della figura le perpendicolari al secondo piano di proiezione, tutte finiscono sulla seconda traccia: nel piano proiettante in seconda la seconda proiezione di tutti gli elementi che stanno sul piano coincide con la seconda traccia. Si ricordi che la traccia è sempre una retta, l'intersezione tra il piano e un piano di proiezione.

È esattamente quello che accade nel piano proiettante in prima, dove tutto ciò che sta sul piano ha la prima proiezione sulla prima traccia, e vale anche per gli altri piani verticali (il frontale e quello di profilo), mentre nel piano orizzontale tutto ciò che sta sul piano ha la seconda proiezione sulla seconda traccia.

> [!abstract] Da ricordare
> - Piani verticali (proiettante in prima, frontale, di profilo): la prima proiezione di tutto ciò che sta sul piano coincide con la prima traccia.
> - Piano proiettante in seconda e piano orizzontale: la seconda proiezione di tutto ciò che sta sul piano coincide con la seconda traccia.
> - Sono cose sperimentali: si verificano sul modello, non si imparano a memoria.

### Esercizio: dalla prima proiezione del triangolo alla seconda e alla terza

L'esercizio tipico della docente dà la prima proiezione di una figura e chiede la seconda e la terza (si potrebbe anche partire dalla terza e risalire alla prima, ma di solito si dà la prima). Guardando il cartoncino dall'alto si capisce che la prima proiezione esiste ma non è la figura vera: è più piccola, gli angoli non sono gli stessi, come un quaderno inclinato che, proiettato, si accorcia. La sola prima proiezione, però, non dice che la figura appartiene al piano: un triangolo sollevato sopra il piano avrebbe la stessa prima proiezione. Servono le condizioni di appartenenza, e in questo caso basta quella più immediata, cioè che la seconda proiezione stia sulla seconda traccia. Non serve nemmeno passare per le rette, anche se si potrebbe.

Le linee di richiamo vanno tenute più leggere della figura, ma devono vedersi, perché alla docente interessa il processo e non solo il risultato. Sulla traccia del piano si calca più scuro il tratto della figura, per dire che lì c'è il triangolo.

> [!example] Il disegno
> ![[05-triangolo-piano-proiettante-in-seconda.svg|620]]
>
> 1. È data la prima proiezione A₁B₁C₁; il lato A₁B₁ è perpendicolare alla LT.
> 2. Da ogni vertice si sale con la linea di richiamo fino a t₂α: lì ci sono A₂, B₂ e C₂. A₂ ≡ B₂, perché A e B stanno sulla stessa perpendicolare a π₂.
> 3. La seconda proiezione è il segmento A₂C₂, calcato sopra t₂α.
> 4. Terza proiezione: da ogni punto della prima proiezione si va in orizzontale fino all'asse, si gira con l'arco fino alla LT a destra e si sale; dalla seconda proiezione si va in orizzontale verso destra; dove le due linee si incontrano c'è il punto in π₃.
> 5. Controllo: A₃B₃ è parallelo alla LT, perché A e B hanno la stessa quota; la retta AB è una retta proiettante in seconda che sta sul piano.

Se in tutte le costruzioni dentro il modello si conserva il parallelismo, si sta già disegnando un'assonometria usando solo la logica: lo si vedrà più avanti. E se una figura si presenta in questo modo, la risposta alla domanda «che piano è?» è immediata: un piano proiettante in seconda.

### Un quadrato in un piano parallelo alla linea di terra

Nel quaderno di Marta, accanto al piano proiettante in seconda, c'è anche il quadrato appartenente a un piano parallelo alla linea di terra, collegato all'esercizio per casa assegnato il 13 ottobre. I lati AB e CD sono paralleli alla LT, le due proiezioni sono rettangoli e nella terza proiezione il quadrato si riduce a un segmento sulla terza traccia: è il segno che il piano è parallelo alla LT. Per disegnare le tracce del piano si trovano prima le tracce delle rette dei lati.

> [!example] Il disegno
> ![[05-quadrato-piano-parallelo-alla-lt.svg|620]]
>
> 1. Prima e seconda proiezione del quadrato sono due rettangoli, con i lati AB e CD paralleli alla LT.
> 2. In terza proiezione A₃ ≡ B₃ e C₃ ≡ D₃: il quadrato diventa un segmento inclinato.
> 3. Le tracce t₁α e t₂α sono parallele alla LT; t₃α è inclinata e contiene la terza proiezione del quadrato.

## LA RETTA GENERICA

### Le proiezioni a partire dalle tracce

La retta generica non ha condizioni di particolarità: è quella che ha tutte le tracce proprie, cioè buca sia π₁ sia π₂. Nel disegno nello spazio le parti nascoste dietro un piano si tratteggiano: il tratteggio serve per le viste virtuali, perché in architettura si disegna anche ciò che sta dietro un'altra cosa e non si vede.

Le proiezioni si costruiscono a partire dai due punti che si conoscono, le due tracce. Proiettando la prima traccia su π₂ si ottiene un punto della linea di terra, perché tutto ciò che sta su π₁, proiettato su π₂, finisce sulla LT: è la seconda proiezione della prima traccia, (T₁ᵣ)₂. La seconda traccia invece sta già su π₂ e non si riproietta. Quindi r₂ passa per la sua seconda traccia e per la seconda proiezione della prima. Allo stesso modo, la seconda traccia proiettata su π₁ cade sulla LT in (T₂ᵣ)₁, e r₁ passa per la sua prima traccia e per la prima proiezione della seconda.

La docente chiede di fare attenzione alle parole: le tracce sono punti, e «la seconda proiezione della prima traccia» non è un gioco di parole ma un'azione, proiettare quel punto su π₂.

> [!example] Il disegno
> ![[05-retta-generica-proiezioni.svg|560]]
>
> 1. Si segnano le due tracce: T₁ᵣ su π₁ (sotto la LT) e T₂ᵣ su π₂ (sopra la LT).
> 2. Da T₁ᵣ si sale con il richiamo fino alla LT: è (T₁ᵣ)₂.
> 3. r₂ è la retta per T₂ᵣ e (T₁ᵣ)₂.
> 4. Da T₂ᵣ si scende con il richiamo fino alla LT: è (T₂ᵣ)₁.
> 5. r₁ è la retta per T₁ᵣ e (T₂ᵣ)₁.

> [!example] Il disegno nello spazio
> ![[05-spazio-retta-generica.svg|620]]
>
> r₁ è come l'ombra della retta sul pavimento e va da T₁ᵣ a (T₂ᵣ)₁; r₂ è la sua immagine sulla parete e va da T₂ᵣ a (T₁ᵣ)₂.

> [!abstract] Da ricordare
> - La prima proiezione di una retta passa per la sua prima traccia e per la prima proiezione delle altre tracce.
> - La seconda proiezione passa per la sua seconda traccia e per la seconda proiezione delle altre.
> - La terza proiezione passa per la sua terza traccia e per la terza proiezione delle altre.
> - Le proiezioni delle tracce cadono sulla linea di terra, perché le tracce stanno sui piani di proiezione.

### La terza traccia

La retta generica ha anche una terza traccia, il punto in cui buca π₃. Per disegnare la terza proiezione non serve: bastano le terze proiezioni della prima e della seconda traccia, e per due punti passa una retta. Il problema è trovare la terza traccia, perché la retta buca π₃ non dentro il primo diedro ma dietro, dove nel modello il piano non c'è: i piani però sono infiniti.

Ci sono due modi. Il primo è immediato: la terza proiezione passa per la terza traccia, quindi si prolunga r₃, tratteggiandola perché la retta sta andando dietro. Graficamente però a mano potrebbe non tornare, e la docente suggerisce un secondo modo, più sicuro: pensare la retta su un piano ausiliario. I piani ausiliari sono proprio i piani proiettanti in prima e in seconda, e aiutano molto. Se per r si fa passare un piano proiettante in prima, cioè si fa coincidere r₁ con t₁α, per le condizioni di appartenenza la terza traccia della retta deve stare sulla terza traccia del piano, anche se sta dietro. Guardando tutto dall'alto si prolunga t₁α fino alla retta di intersezione tra π₁ e π₃; quel punto si ruota con l'arco e si sale in verticale: quella verticale è la terza traccia del piano, e T₃ᵣ sta lì sopra.

> [!example] Il disegno
> ![[05-retta-generica-terza-traccia.svg|620]]
>
> 1. Terze proiezioni delle tracce: da T₁ᵣ in orizzontale fino all'asse, arco fino alla LT a destra: (T₁ᵣ)₃. T₂ᵣ in orizzontale fino all'asse: (T₂ᵣ)₃.
> 2. r₃ passa per (T₁ᵣ)₃ e (T₂ᵣ)₃; oltre T₂ᵣ la retta va dietro π₂ e si tratteggia.
> 3. Primo modo: prolungare r₃ oltre (T₂ᵣ)₃.
> 4. Secondo modo: piano ausiliario α proiettante in prima con t₁α ≡ r₁ e t₂α verticale per (T₂ᵣ)₁. Si prolunga r₁ fino all'asse e si trova (T₃ᵣ)₁, sopra la LT perché è dietro π₂.
> 5. Si gira (T₃ᵣ)₁ con l'arco fino alla LT e si sale: è t₃α, e T₃ᵣ deve stare su di essa.
> 6. Verifica: r₂ prolungata incontra l'asse in (T₃ᵣ)₂; portando quel punto in orizzontale su t₃α si ritrova T₃ᵣ.

> [!example] Il disegno nello spazio
> ![[05-spazio-retta-generica-terza-traccia.svg|620]]
>
> 1. Oltre T₂ᵣ la retta passa dietro π₂ (tratteggio).
> 2. Il piano α proiettante in prima contiene r: t₁α ≡ r₁, che prolungata arriva in (T₃ᵣ)₁ dietro π₂.
> 3. Da (T₃ᵣ)₁ sale t₃α, e la retta buca π₃ prolungato in T₃ᵣ, proprio su t₃α.

Rispetto ai quattro quadranti (primo, secondo, terzo e quarto), la terza traccia di questa retta sta dietro: non è uno spazio occulto, ma una posizione dello spazio. Per esercitarsi a trovarla si può costruire anche un modello apposito, meglio in plexiglass che in cartoncino, perché si vede di più.

### La retta generica nei piani ausiliari

Una retta generica appartiene sempre a un piano proiettante: se si appoggia una retta sul cartoncino, ci sta. Per costruire un piano che la contenga bisogna rispettare le condizioni di appartenenza, cioè le tracce della retta devono stare sulle rispettive tracce del piano. Non basta far passare le tracce del piano per una sola delle tracce della retta: un piano che contiene T₁ᵣ ma non T₂ᵣ non contiene la retta.

Il modo più comodo sfrutta la proprietà dei piani proiettanti. Nel piano proiettante in prima la prima proiezione di tutto ciò che vi sta coincide con la prima traccia: quindi si fa coincidere r₁ con t₁α, e t₂α, perpendicolare alla LT, conterrà T₂ᵣ. Nel piano proiettante in seconda vale lo stesso con la seconda proiezione: r₂ coincide con t₂β, e t₁β, perpendicolare alla LT, passa per T₁ᵣ.

> [!example] Il disegno
> ![[05-retta-generica-piani-proiettanti.svg|620]]
>
> 1. Piano α proiettante in prima: t₁α ≡ r₁ (quindi contiene T₁ᵣ); t₂α parte da (T₂ᵣ)₁, è perpendicolare alla LT e passa per T₂ᵣ.
> 2. Piano β proiettante in seconda: t₂β ≡ r₂ (quindi contiene T₂ᵣ); t₁β parte da (T₁ᵣ)₂, è perpendicolare alla LT e passa per T₁ᵣ.
> 3. In tutti e due i casi le tracce della retta stanno sulle tracce del piano.

> [!example] Il disegno nello spazio
> ![[05-spazio-retta-generica-piani-ausiliari.svg|620]]
>
> 1. Il piano verticale α (blu) contiene r: la sua prima traccia è r₁.
> 2. Il piano β (verde), perpendicolare a π₂, contiene r: la sua seconda traccia è r₂.

> [!abstract] Da ricordare
> Una retta appartiene a un piano quando le tracce della retta giacciono sulle rispettive tracce del piano. I piani ausiliari sono i piani proiettanti in prima e in seconda: per una retta generica t₁α ≡ r₁ oppure t₂β ≡ r₂.

## IL PIANO GENERICO

### Il triangolo delle tracce

Il piano generico è in posizione generica rispetto a tutti e tre i piani di proiezione: forma un angolo con ciascuno, e li taglia lungo un triangolo, né più né meno. Con il cartoncino si può realizzare solo incidendo i piani verticali con due tagli che si incontrano in un punto sulla verticale, e infilandoci il cartoncino. Questo triangolo è molto importante perché in assonometria il piano generico diventerà il piano di quadro e il triangolo si chiamerà triangolo delle tracce.

Sul foglio le tre tracce si incontrano a due a due sulle rette di intersezione dei piani di proiezione: t₂α e t₁α partono dallo stesso punto della LT, e t₃α unisce il punto in cui t₂α incontra l'asse con il punto in cui t₁α, girato con l'arco, arriva sulla LT a destra.

> [!example] Il disegno nello spazio
> ![[05-spazio-piano-generico.svg|620]]
>
> 1. Il piano taglia π₁, π₂ e π₃ lungo t₁α, t₂α e t₃α, che formano un triangolo.
> 2. Un'orizzontale o del piano è parallela al pavimento: o₁ è parallela a t₁α.

### Le rette che appartengono al piano generico

Una retta appartiene a un piano quando tutti i suoi punti appartengono al piano: è la lezione numero uno, e in pratica se ne prendono due, che quando è possibile diventano le tracce. Sul piano generico può stare sicuramente una retta generica. Non può starci invece una retta proiettante in prima: è verticale, esce dal piano e lo buca in un solo punto.

Ci può stare l'orizzontale, che non è la parallela alla linea di terra (anche quella è orizzontale), ma la retta con la seconda proiezione parallela alla LT e la prima variamente inclinata. Essendo parallela a π₁, ha la prima traccia all'infinito; per appartenere al piano, anche quel punto all'infinito deve stare su t₁α, e questo succede solo se la retta ha la direzione di t₁α. Quindi l'orizzontale del piano è parallela alla prima traccia, e la sua prima proiezione o₁ si disegna parallela a t₁α; le sue tracce proprie T₂ₒ e T₃ₒ stanno su t₂α e su t₃α.

Allo stesso modo ci può stare la frontale, che ha la prima proiezione parallela alla LT e la seconda inclinata. È parallela a π₂, ha la seconda traccia all'infinito, e per rispettare la condizione di appartenenza deve essere parallela alla seconda traccia del piano: f₂ si disegna parallela a t₂α. Infine sul piano generico può stare anche una retta di profilo. Sul libro e sulle schede si trova l'esempio completo, con tutte le proiezioni, delle rette che possono appartenere al piano generico: generica, orizzontale, frontale e di profilo.

> [!example] Il disegno nello spazio
> ![[05-spazio-piano-generico-rette.svg|620]]
>
> 1. La retta generica r ha T₁ᵣ su t₁α e T₂ᵣ su t₂α.
> 2. L'orizzontale o è parallela a t₁α e ha T₂ₒ su t₂α e T₃ₒ su t₃α.
> 3. La frontale f è parallela a t₂α e ha T₁f su t₁α e T₃f su t₃α.
> 4. La proiettante in prima v non sta sul piano: lo buca in un punto.

> [!example] Il disegno: l'orizzontale del piano generico
> ![[05-piano-generico-orizzontale.svg|620]]
>
> 1. Si disegnano t₂α e t₁α dallo stesso punto della LT; t₃α unisce il punto di t₂α sull'asse con il punto di t₁α girato con l'arco.
> 2. o₂ parallela alla LT: dove incontra t₂α c'è T₂ₒ; si scende con il richiamo sulla LT e si trova (T₂ₒ)₁.
> 3. Da (T₂ₒ)₁ si traccia o₁ parallela a t₁α (T₁ₒ∞ sta su t₁α).
> 4. o₁ incontra l'asse in (T₃ₒ)₁; con l'arco si porta sulla LT e si sale fino all'altezza di o₂: T₃ₒ cade su t₃α. o₃ è parallela alla LT, alla stessa altezza di o₂.

> [!example] Il disegno: la frontale del piano generico
> ![[05-piano-generico-frontale.svg|620]]
>
> 1. f₁ parallela alla LT: dove incontra t₁α c'è T₁f; si sale con il richiamo sulla LT e si trova (T₁f)₂.
> 2. Da (T₁f)₂ si traccia f₂ parallela a t₂α (T₂f∞ sta su t₂α).
> 3. f₃ è verticale, alla distanza di f₁ dalla LT riportata con l'arco; f₂ incontra l'asse in (T₃f)₂, e portando quel punto in orizzontale su f₃ si trova T₃f, che cade su t₃α.

> [!abstract] Da ricordare
> - Orizzontale: seconda proiezione parallela alla LT; nel piano generico o₁ è parallela a t₁α.
> - Frontale: prima proiezione parallela alla LT; nel piano generico f₂ è parallela a t₂α.
> - Se una traccia della retta è all'infinito, la proiezione della retta e la traccia del piano corrispondente devono essere parallele.

## I PIANI CHE CONTENGONO UNA RETTA

### Il metodo

Data una retta, quanti piani possono contenerla? Per una retta passano infiniti piani: per una retta verticale, per esempio, passano infiniti piani verticali, ma solo quelli. Ogni piano ha le sue caratteristiche, e ogni retta le sue a seconda di come è posizionata. Per rispondere si colloca la retta nel modello e si guardano i piani su cui si appoggia, partendo dall'associazione più immediata tra il nome della retta e il nome del piano (una retta proiettante in seconda sta sicuramente in un piano proiettante in seconda). Poi si disegnano i piani con colori diversi rispettando la condizione di appartenenza: le tracce del piano passano per le tracce della retta. Per questo, nel disegno delle condizioni, contano le tracce della retta più che le sue proiezioni.

Sul foglio si fanno sei disegni, non più di sei, abbastanza grandi, a mano libera ma con cura, seguendo con lo sguardo la mano che traccia la linea. Lo schema del triedro si disegna senza lettere sugli assi: non è propriamente un'assonometria, ma una trasposizione grafica del modello.

### Retta proiettante in prima

La retta verticale è perpendicolare a π₁ e lo buca in T₁ᵣ. Un piano orizzontale non può contenerla, perché la retta lo buca in un solo punto. La contengono i piani verticali: il piano di profilo, il piano frontale e i piani proiettanti in prima, che ruotano attorno alla retta. In tutti la prima traccia passa per T₁ᵣ.

> [!example] Il disegno
> ![[05-piani-per-retta-proiettante-in-prima.svg|620]]
>
> 1. r₂ perpendicolare alla LT; r₁ è un punto, che coincide con T₁ᵣ.
> 2. Piano di profilo γ (viola): t₁γ e t₂γ sulla stessa perpendicolare alla LT, con t₂γ che contiene r₂.
> 3. Piano frontale α (verde): t₁α per T₁ᵣ parallela alla LT; t₂α all'infinito.
> 4. Piano proiettante in prima β (blu): t₁β per T₁ᵣ con l'inclinazione che si vuole; t₂β perpendicolare alla LT.

> [!example] Il disegno nello spazio
> ![[05-spazio-piani-retta-proiettante-in-prima.svg|620]]

### Retta proiettante in seconda

La retta perpendicolare a π₂ lo buca in T₂ᵣ: r₂ è un punto e la prima traccia è all'infinito. La contiene il piano proiettante in seconda; mettendola nel modello si vede che si appoggia anche su un piano orizzontale e, girando il modello, anche su un piano di profilo. In tutti la seconda traccia passa per T₂ᵣ.

> [!example] Il disegno
> ![[05-piani-per-retta-proiettante-in-seconda.svg|620]]
>
> 1. r₂ ≡ T₂ᵣ è un punto; r₁ è perpendicolare alla LT (T₁ᵣ∞).
> 2. Piano proiettante in seconda β: t₂β passa per T₂ᵣ, inclinata; t₁β perpendicolare alla LT.
> 3. Piano orizzontale γ: t₂γ parallela alla LT per T₂ᵣ; t₁γ all'infinito.
> 4. Piano di profilo δ: t₂δ per T₂ᵣ e t₁δ ≡ r₁, tutte e due perpendicolari alla LT.

> [!example] Il disegno nello spazio
> ![[05-spazio-piani-retta-proiettante-in-seconda.svg|620]]

### Retta parallela alla linea di terra

Le proiezioni r₁ e r₂ sono parallele alla LT; la retta non buca né π₁ né π₂, e l'unica traccia propria è la terza, T₃ᵣ, che coincide con r₃. Una retta parallela alla linea di terra sta per forza in un piano parallelo alla linea di terra; la contiene anche il piano frontale e, nel quaderno di Marta, il piano orizzontale.

> [!example] Il disegno
> ![[05-piani-per-retta-parallela-alla-lt.svg|620]]
>
> 1. Si trova T₃ᵣ ≡ r₃ portando r₁ sul terzo piano con l'arco e salendo fino all'altezza di r₂.
> 2. Piano α parallelo alla LT: t₂α e t₁α parallele alla LT; t₃α passa per T₃ᵣ.
> 3. Piano frontale φ: t₁φ ≡ r₁, t₂φ all'infinito, t₃φ verticale per T₃ᵣ.

> [!example] Il disegno: il piano orizzontale (dal quaderno di Marta)
> ![[05-retta-parallela-alla-lt-piano-orizzontale.svg|620]]
>
> Il piano orizzontale ha t₂α ≡ r₂, parallela alla LT, e la prima traccia all'infinito.

> [!example] Il disegno nello spazio
> ![[05-spazio-piani-retta-parallela-alla-lt.svg|620]]

### Retta orizzontale

L'orizzontale è parallela a π₁: i suoi punti stanno tutti alla stessa altezza, la prima traccia è all'infinito e la seconda è T₂ₒ. La contiene prima di tutto il piano orizzontale. La contiene poi un piano generico: si è liberi di sceglierlo, ma una volta fissati gli elementi di partenza il piano è determinato. Si parte dalla seconda traccia t₂β per T₂ₒ; perché la retta appartenga al piano, la prima traccia del piano deve essere parallela alla prima proiezione della retta, e siccome le tracce si incontrano sulla LT, t₁β si disegna dal punto in cui t₂β incontra la LT, parallela a o₁. Infine la contiene il piano verticale, il proiettante in prima.

> [!example] Il disegno
> ![[05-piani-per-retta-orizzontale.svg|620]]
>
> 1. o₂ parallela alla LT, o₁ inclinata; T₂ₒ è la seconda traccia, la prima è all'infinito.
> 2. Piano orizzontale α: t₂α ≡ o₂; t₁α all'infinito.
> 3. Piano generico β: t₂β per T₂ₒ; dal punto sulla LT, t₁β parallela a o₁.
> 4. Piano proiettante in prima γ: t₁γ ≡ o₁; t₂γ perpendicolare alla LT per T₂ₒ.

> [!example] Il disegno nello spazio
> ![[05-spazio-piani-retta-orizzontale.svg|620]]

### Retta frontale

La frontale è parallela a π₂ e ha la prima proiezione parallela alla LT: conviene disegnare comunque f₁, per essere certi del parallelismo. La contiene il piano frontale, che è verticale, e infatti f₁ coincide con la prima traccia. La contiene un piano generico: la seconda traccia della retta è all'infinito nella direzione di f₂, quindi la seconda traccia del piano si disegna parallela a f₂. La contiene infine il piano proiettante in seconda, scelto perché tutto ciò che vi sta ha la seconda proiezione sulla seconda traccia: si fa coincidere subito f₂ con t₂γ. La docente sottolinea che l'orizzontale e la frontale sono le rette che servono a risolvere i problemi.

> [!example] Il disegno
> ![[05-piani-per-retta-frontale.svg|620]]
>
> 1. f₁ parallela alla LT, f₂ inclinata; T₁f è la prima traccia, la seconda è all'infinito.
> 2. Piano frontale β: t₁β ≡ f₁; t₂β all'infinito.
> 3. Piano generico α: t₁α per T₁f; dal punto sulla LT, t₂α parallela a f₂.
> 4. Piano proiettante in seconda γ: t₂γ ≡ f₂; t₁γ perpendicolare alla LT per T₁f.

> [!example] Il disegno nello spazio
> ![[05-spazio-piani-retta-frontale.svg|620]]

### Retta di profilo

La retta di profilo m appartiene per definizione a un piano di profilo, che è il primo da disegnare. Appoggiando un cartoncino sulla retta viene fuori anche un piano parallelo alla linea di terra. Infine c'è il piano generico: la terza traccia di m è all'infinito, quindi la terza traccia del piano deve essere necessariamente parallela a m₃.

> [!example] Il disegno
> ![[05-piani-per-retta-di-profilo.svg|620]]
>
> 1. m₁ e m₂ sulla stessa perpendicolare alla LT; tracce T₁ₘ e T₂ₘ; m₃ si trova portando T₁ₘ con l'arco e T₂ₘ in orizzontale.
> 2. Piano di profilo δ: t₂δ ≡ m₂, t₁δ ≡ m₁.
> 3. Piano ε parallelo alla LT: t₂ε per T₂ₘ e t₁ε per T₁ₘ, parallele alla LT; t₃ε ≡ m₃.
> 4. Piano generico α: t₂α per T₂ₘ e t₁α per T₁ₘ, che si incontrano sulla LT; t₃α risulta parallela a m₃.

> [!example] Il disegno nello spazio
> ![[05-spazio-piani-retta-di-profilo.svg|620]]

> [!abstract] Da ricordare: i piani che contengono le rette
> - Proiettante in prima: frontale, di profilo, proiettanti in prima (non l'orizzontale).
> - Proiettante in seconda: proiettante in seconda, orizzontale, di profilo.
> - Parallela alla LT: parallelo alla LT, frontale, orizzontale.
> - Orizzontale: orizzontale, generico (t₁ parallela a o₁), proiettante in prima (t₁ ≡ o₁).
> - Frontale: frontale, generico (t₂ parallela a f₂), proiettante in seconda (t₂ ≡ f₂).
> - Di profilo: di profilo, parallelo alla LT, generico (t₃ parallela a m₃).

## IL PUNTO CHE APPARTIENE A UN PIANO

### La regola e le rette ausiliarie

Un punto appartiene a un piano se appartiene a una retta del piano, e un punto appartiene a una retta se le sue proiezioni giacciono sulle proiezioni della retta. Si può usare qualunque retta del piano, anche una generica, ma quelle che aiutano di più sono le due ausiliarie, le uniche che hanno un nome: l'orizzontale e la frontale. Le condizioni vanno rispettate tutte: il punto sulla retta, e la retta sul piano con le sue tracce sulle tracce del piano.

Bisogna anche non confondere le tracce con le proiezioni. Tranne nei casi particolari dei piani proiettanti, la proiezione di un punto del piano non va a finire sulla traccia: la traccia è soltanto l'intersezione del piano con un piano di proiezione.

> [!abstract] Da ricordare
> - P ∈ α se P sta su una retta r di α (P ∈ r ⊂ α).
> - P ∈ r se P₁ sta su r₁ e P₂ sta su r₂.
> - r ⊂ α se le tracce di r stanno sulle tracce di α; se una traccia di r è all'infinito, la proiezione di r è parallela alla traccia di α corrispondente.

### Disegnare un punto del piano con l'orizzontale

Si disegna un'orizzontale del piano: la sua seconda proiezione è parallela alla LT e la sua seconda traccia deve stare sulla seconda traccia del piano. Un'orizzontale qualunque avrebbe una o₁ qualsiasi; quella del piano no, perché anche T₁ₒ deve stare su t₁α, e siccome T₁ₒ è all'infinito, o₁ deve essere parallela a t₁α. In questo modo la retta lascia la sua traccia proprio lì, sulla traccia del piano. Fatto questo, si prende un punto qualunque della retta.

> [!example] Il disegno
> ![[05-punto-piano-generico-orizzontale.svg|620]]
>
> 1. È dato il piano generico α con t₂α e t₁α, che si incontrano sulla LT.
> 2. Si disegna o₂ parallela alla LT: dove incontra t₂α c'è T₂ₒ (T₂ₒ ∈ t₂α).
> 3. Da T₂ₒ si scende con il richiamo, leggero, fino alla LT: (T₂ₒ)₁.
> 4. Da (T₂ₒ)₁ si traccia o₁ parallela a t₁α (T₁ₒ∞ ∈ t₁α).
> 5. Si sceglie P₂ su o₂ e si scende fino a o₁: lì c'è P₁. P sta su una retta di α, quindi P ∈ α.

### Disegnare un punto del piano con la frontale

Per la frontale la seconda traccia è all'infinito: T₁f deve stare su t₁α e T₂f su t₂α. Si comincia da f₁, parallela alla LT; poi la seconda proiezione deve avere la direzione che porta il suo punto all'infinito sulla traccia del piano, quindi f₂ si costruisce parallela a t₂α. Si dimostra così che P appartiene a f e che f appartiene ad α.

> [!example] Il disegno
> ![[05-frontale-piano-generico.svg|620]]
>
> 1. f₁ parallela alla LT: dove incontra t₁α c'è T₁f (T₁f ∈ t₁α).
> 2. Da T₁f si sale con il richiamo fino alla LT: (T₁f)₂.
> 3. Da (T₁f)₂ si traccia f₂ parallela a t₂α (T₂f∞ ∈ t₂α).
> 4. Si sceglie P₂ su f₂ e si scende fino a f₁: lì c'è P₁. P ∈ f ⊂ α.

### Il problema al contrario: il punto appartiene al piano?

Si possono dare le tracce di α e le due proiezioni P₂ e P₁, e chiedere se P appartiene ad α. A lezione la docente lo risolve con una retta generica: si è liberi di sceglierla, ma deve passare per il punto e deve appartenere al piano. Si disegna r₂ per P₂, segnando T₂ᵣ dove incontra t₂α; da quel momento la prima proiezione non è più libera. Dove r₂ incontra la LT c'è (T₁ᵣ)₂; scendendo si trova T₁ᵣ su t₁α. La prima proiezione r₁ passa per T₁ᵣ e per (T₂ᵣ)₁. Se P₁ cade su r₁ il punto appartiene al piano; nell'esempio della lavagna non ci cade, e la risposta è no.

In questo esercizio si fanno due cose insieme: si verifica la condizione di appartenenza e si impara a disegnare una retta che appartiene al piano. Serve per quando si avranno figure triangolari su piani generici e bisognerà capire che piano è e dove sono le tracce, per poterlo poi ribaltare.

> [!example] Il disegno
> ![[05-verifica-punto-con-retta-generica.svg|620]]
>
> 1. Sono dati t₂α, t₁α, P₂ e P₁.
> 2. Si disegna r₂ per P₂; dove incontra t₂α c'è T₂ᵣ.
> 3. Si prolunga r₂ fino alla LT: (T₁ᵣ)₂. Si scende fino a t₁α: T₁ᵣ.
> 4. Da T₂ᵣ si scende alla LT: (T₂ᵣ)₁. r₁ passa per (T₂ᵣ)₁ e T₁ᵣ: r ⊂ α.
> 5. Da P₂ si scende con il richiamo: P₁ non cade su r₁, quindi P ∉ α.

### Esercizio: disegnare P ∈ α dimostrando che P ∈ r ⊂ α

L'ultimo esercizio della lezione, nel quaderno di Marta, riguarda un piano proiettante in prima. Durante l'esercizio la docente ricorda: pensate al modello, nel piano proiettante in prima tutto ciò che sta sul piano ha la prima proiezione sulla prima traccia. La ricostruzione è probabile, perché la foto è poco leggibile.

> [!example] Il disegno
> ![[05-esercizio-punto-nel-piano-proiettante.svg|620]]
>
> 1. Il piano α è proiettante in prima: t₂α perpendicolare alla LT, t₁α inclinata.
> 2. Si sceglie P₁ su t₁α e P₂ sulla stessa linea di richiamo.
> 3. Per P passa la retta r proiettante in prima: r₂ perpendicolare alla LT, r₁ ≡ T₁ᵣ ≡ P₁ su t₁α. Quindi r ⊂ α e P ∈ α.
> 4. Controllo con l'orizzontale o per P: o₂ parallela alla LT incontra t₂α in T₂ₒ; o₁ ≡ t₁α.

## ESERCIZI TIPO DELLE SCHEDE

Le schede di esercizi della docente (PO, proiezioni ortogonali) usano tutto quello che si è visto: trovare le tracce di una retta, dire se una retta o un punto appartengono a un piano, disegnare la proiezione mancante di una figura che sta su un piano. I procedimenti qui sotto seguono le soluzioni delle schede; a lezione non sono stati svolti alla lavagna.

### Dalla prima proiezione e dalle tracce, la seconda proiezione della figura

È la versione generale dell'esercizio fatto sul piano proiettante in seconda. Su un piano generico la seconda proiezione non cade più sulla traccia, quindi bisogna passare per le rette: ogni lato del triangolo sta su una retta del piano, e le tracce di quella retta stanno sulle tracce del piano. Nella soluzione della scheda si prolungano i lati della prima proiezione fino alle tracce.

> [!example] Disegno proposto (non fatto a lezione): la seconda proiezione di un triangolo su un piano generico
> ![[b05-proposto-seconda-proiezione-triangolo.svg|620]]
>
> 1. Si prolunga il lato A₁C₁: è r₁. Dove incontra t₁α c'è T₁ᵣ; dove incontra la LT c'è (T₂ᵣ)₁.
> 2. Da (T₂ᵣ)₁ si sale fino a t₂α: T₂ᵣ. Da T₁ᵣ si sale fino alla LT: (T₁ᵣ)₂.
> 3. r₂ è la retta per T₂ᵣ e (T₁ᵣ)₂. Da A₁ e C₁ si sale con il richiamo fino a r₂: A₂ e C₂.
> 4. Si ripete con il lato B₁C₁ (retta s, in verde): s₂ passa per T₂ₛ e (T₁ₛ)₂; da B₁ si sale fino a s₂: B₂. C₂ deve cadere anche su s₂, ed è un controllo.
> 5. Si uniscono A₂, B₂ e C₂.

Lo stesso disegno, letto al contrario, risolve l'esercizio «data la figura in prima e seconda proiezione, individuare il piano»: si trovano le tracce delle rette di due lati, e t₁α passa per le due prime tracce, t₂α per le due seconde; le due tracce del piano devono incontrarsi sulla LT. E risolve anche quello «data la seconda proiezione, trovare la prima», scendendo invece di salire. Quando il piano è parallelo alla LT, come in una delle schede, si procede allo stesso modo con le rette dei lati.

### La retta r appartiene al piano?

Sono date r₁, r₂ e le tracce del piano. Prima si trovano le tracce della retta, poi si controlla se stanno sulle tracce del piano. La seconda traccia si trova dove r₁ incontra la LT, salendo fino a r₂; la prima dove r₂ incontra la LT, scendendo fino a r₁. Nelle soluzioni della scheda a volte le tracce cadono negli altri quadranti, per esempio T₁ᵣ sopra la LT: in quel caso si prolunga anche la traccia del piano oltre la LT.

> [!example] Disegno proposto (non fatto a lezione): la retta appartiene al piano?
> ![[b05-proposto-retta-appartiene.svg|620]]
>
> 1. Dove r₁ incontra la LT c'è (T₂ᵣ)₁: si sale fino a r₂ e si trova T₂ᵣ.
> 2. Dove r₂ incontra la LT c'è (T₁ᵣ)₂: si scende fino a r₁ e si trova T₁ᵣ.
> 3. A sinistra T₂ᵣ non sta su t₂α (e T₁ᵣ non sta su t₁α): r non appartiene ad α.
> 4. A destra T₂ᵣ ∈ t₂α e T₁ᵣ ∈ t₁α: r appartiene ad α.

### La falda di un tetto: dalla prima proiezione la seconda e la terza

La scheda «data la prima proiezione della falda appartenente a un piano inclinato e le tracce di questo, determinare la seconda e la terza proiezione» ha uno svolgimento in tre passaggi: si disegnano le tre tracce del piano generico, poi si costruisce un'orizzontale del piano. Nella figura il lato A₁B₁ è parallelo a t₁α, quindi AB sta su un'orizzontale; per il terzo vertice se ne traccia un'altra.

> [!example] Disegno proposto (non fatto a lezione): la falda con le orizzontali
> ![[b05-proposto-falda-seconda-e-terza.svg|620]]
>
> 1. Tracce del piano generico: t₂α e t₁α dalla LT; t₃α unisce il punto di t₂α sull'asse con il punto di t₁α girato con l'arco.
> 2. Orizzontale o: o₁ è il prolungamento di A₁B₁ (parallelo a t₁α) fino alla LT; da lì si sale a t₂α e si trova T₂ₒ; o₂ è parallela alla LT per T₂ₒ.
> 3. Da A₁ e B₁ si sale con il richiamo fino a o₂: A₂ e B₂ (stessa quota).
> 4. Orizzontale o' per C: o'₁ per C₁ parallela a t₁α fino alla LT, si sale a t₂α (T₂ₒ'), o'₂ parallela alla LT; da C₁ si sale fino a o'₂: C₂.
> 5. Terza proiezione: da ogni punto della prima proiezione in orizzontale fino all'asse, arco fino alla LT a destra e su; dalla seconda proiezione in orizzontale verso destra. A₃B₃ viene parallelo alla LT.

### Le altre schede

La scheda di riepilogo chiede anche di trovare le tracce di rette date per proiezioni (anche con le tracce negli altri quadranti), di indicare un punto di un piano proiettante in prima (con l'orizzontale: o₁ ≡ t₁α, T₂ₒ su t₂α), di dire se P o r appartengono ad α, e di trovare un punto su una retta di profilo, che richiede la terza proiezione. La scheda sulle proiezioni dei solidi chiede, date le piante di tre solidi con le altezze, di disegnare le proiezioni con i prospetti frontali e laterali, di individuare per ogni solido un piano e una retta verificando le condizioni di appartenenza (piano frontale anteriore e retta orizzontale; piano di profilo e retta proiettante in prima; piano proiettante in seconda e retta frontale) e di fare uno schema assonometrico a mano libera.

> [!tip] Consegne e avvisi
> - Foglio delle rette e dei piani che le contengono: sei disegni grandi, a mano libera ma con cura, con i piani a colori.
> - Linee di richiamo più leggere della figura ma visibili; nel modello segnare bene l'angolo retto; a casa si possono rifare i disegni con le squadrette.
> - Esercitarsi a trovare la terza traccia di una retta generica, anche con un modello (meglio in plexiglass).
> - Assegno «rette e piani e modello» (la data non è indicata sul foglio): per ogni retta e piano, una fotografia del modello con l'elemento geometrico e le proiezioni, una fotografia del modello aperto con le proiezioni e il disegno nella stessa posizione del modello; nel modello le rette si fanno con un'asta di legno. Il foglio porta nome e cognome (e l'anno accademico per chi è di altri anni).
> - Nel quaderno di Marta, accanto al quadrato nel piano parallelo alla LT, c'è l'annotazione «Omologia e proiezioni ortogonali, giovedì 23»: probabilmente una consegna, da chiarire con la docente.
> - La lezione successiva introduce le architetture (le case) da studiare, da portare poi sulle tavole.

## Collegamenti

Questa lezione chiude il discorso iniziato con [[03-proiezioni-ortogonali-punto-e-rette|le proiezioni ortogonali del punto e delle rette]] e proseguito con [[04-rette-e-piani-nelle-varie-posizioni|le rette e i piani nelle varie posizioni]], da cui riprende le condizioni di appartenenza applicandole al piano proiettante in seconda e ai casi generici. Le rette orizzontale e frontale, presentate qui come rette ausiliarie, sono gli strumenti con cui si risolvono i problemi della lezione successiva sui [[06-piani-ausiliari-e-perpendicolarita|piani ausiliari e la perpendicolarità]], e la ricerca delle tracce del piano di una figura serve a preparare [[07-il-ribaltamento|il ribaltamento]], che permette di vedere la figura in vera forma. Il triangolo delle tracce del piano generico tornerà nell'assonometria come triangolo delle tracce del piano di quadro, e il rigore delle linee di richiamo leggere ma visibili è quello chiesto fin dalle [[01-strumenti-materiali-e-regole|regole del disegno]]. Il testo completo della lezione è nella sbobina [[05-piani-rette-e-appartenenza]].
