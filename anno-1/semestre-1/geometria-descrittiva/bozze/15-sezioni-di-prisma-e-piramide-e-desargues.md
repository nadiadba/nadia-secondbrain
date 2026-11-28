---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-11-24
tags: [geometria-descrittiva, bozza]
---

# Le sezioni del prisma e della piramide e il teorema di Desargues

> [!info] Note collegate
> Sbobina: [[15-prospettiva-esercitazione-e-ripasso-sezioni]]
>
> Bozza precedente: [[14-altezze-e-punto-di-misura-in-prospettiva]] · Successiva: [[16-la-prospettiva-a-occhio-di-formica]]
>
> Argomenti collegati: [[10-intersezione-retta-piano-e-segno-di-sezione]] · [[11-assonometria-cavaliera-e-sezioni-dei-solidi]] · [[09-ribaltamento-del-piano-generico]] · [[02-proiezioni-e-omologia-schema]] · [[PO 7 - Figure piane e solidi]]

La lezione di martedì 24 novembre è registrata in due parti.

La prima parte è un'esercitazione in aula sulla prospettiva con il punto di misura: nella registrazione si sentono solo alcuni compagni che si spiegano i passaggi, e la costruzione è quella della lezione del 19 novembre (sbobina [[14-prospettiva-altezze-e-punto-di-misura]]).

La seconda parte, l'argomento di questa bozza, è il ripasso della docente per la Prova n. 2 di giovedì 26 novembre:

- l'assonometria obliqua con la pianta ribaltata;
- come si riconoscono i piani delle facce di un solido, nelle proiezioni ortogonali e in assonometria;
- la sezione di un prisma con un piano proiettante in seconda;
- la sezione di una piramide con un piano generico, usando i piani proiettanti che passano per gli spigoli;
- il teorema di Desargues nello spazio, cioè l'omologia tra la base della piramide e la sezione;
- il ribaltamento della sezione.

Alla fine la docente lascia un problema per la volta successiva: costruire un segmento di lunghezza data perpendicolare a un piano generico.

Il libro della docente dedica a questi argomenti le applicazioni 22-27 delle proiezioni ortogonali, «Sezioni di solidi» e «Sezione di un solido con un piano generico» (allegato, pp. 120-140), e la pagina sul teorema di Desargues (p. 12): da lì vengono le regole sulle rette di intersezione, il prisma tagliato da un piano generico e l'esercizio risolto sulla piramide.

## PRIMA DELLE SEZIONI: L'ASSONOMETRIA E I PIANI DELLE FACCE

### L'assonometria obliqua con la pianta ribaltata

La docente riprende l'assonometria obliqua con il quadro verticale e il metodo della pianta, spiegati nella [[12-errori-della-prova-1-e-quadro-verticale|lezione del 12 novembre]] (Disegno 14).

Sul quadro il prospetto è in vera forma: le unità di misura su x′ e su z′ sono uguali, e si riduce solo la misura in profondità.

Per la direzione di proiezione non si ribalta un piano, ma solo l'asse y. C'è un punto da cui bisogna cominciare, e la prima cosa da fare è proprio la direzione.

Poi bisogna trovare l'affinità che lega la pianta ribaltata alla pianta assonometrica:

- la pianta ribaltata è quella che si ottiene ribaltando il piano orizzontale, e quindi ha le misure uguali a quelle nello spazio;
- la direzione dell'affinità è la direzione assonometrica.

Per portare un punto A della pianta nella pianta assonometrica:

1. lo si proietta con la direzione assonometrica;
2. si stacca la profondità;
3. la si riporta in orizzontale e si trova il punto.

Dopo, per le altezze, basta costruire le parallele, perché le rette che sono parallele nella realtà sono parallele anche nella rappresentazione. È il contrario della prospettiva, dove le rette parallele perdono il parallelismo e concorrono nel loro punto di fuga.

La docente raccomanda di prepararsi un foglio A3 con tutte le assonometrie, svolte correttamente. Gli errori classici sono due: sbagliare le assonometrie, oppure averle studiate senza averle capite.

### Riconoscere i piani delle facce nelle proiezioni ortogonali

Le sezioni si risolvono trovando le intersezioni tra i piani. Ma per trovare le intersezioni bisogna prima saper costruire i piani: è la cosa da saper fare prima ancora della sezione.

La domanda da farsi è: quando vedo un disegno in proiezioni ortogonali, vedo già i vari piani? E in assonometria?

Il consiglio della docente è mettere sempre le lettere, perché aiuta moltissimo.

Si comincia dai piani verticali, cioè dalle facce laterali di un prisma:

- si prende il piano verticale della faccia e ci si appoggia la penna, immaginando di prolungarlo;
- lo spigolo di base della faccia, che sta su π₁, è la prima traccia di quel piano;
- se la faccia è perpendicolare a π₁, il piano è proiettante in prima: la seconda traccia è perpendicolare alla linea di terra.

Poi c'è il piano orizzontale, quello che passa per la faccia superiore. Nelle proiezioni ortogonali è facile: ha solo la seconda traccia, parallela alla linea di terra, alla quota della faccia.

### Gli stessi piani in assonometria

La stessa cosa si deve saper fare in assonometria, cercando in maniera molto semplice di capire il piano che passa per la faccia del solido.

Per un piano verticale si prende di nuovo lo spigolo di base, quello che sta a terra: il piano verticale lascia sul piano orizzontale la sua traccia, che sta proprio lì. Ogni faccia laterale di un prisma retto dà un piano proiettante in prima.

Per il piano orizzontale della faccia superiore si considerano gli spigoli superiori:

- ogni spigolo superiore appartiene al piano, quindi la sua traccia sta sulla traccia del piano;
- un piano orizzontale ha le tracce sui piani verticali di riferimento, e queste tracce sono parallele all'asse x e all'asse y;
- quindi basta trovare due sole tracce, prolungando gli spigoli superiori fino ai piani di riferimento, e da lì costruire le parallele agli assi.

Infine un avvertimento sul disegno del solido in assonometria: le rette verticali sono tutte parallele a z′, e il solido va ricostruito così.

## LA SEZIONE DEL PRISMA

### La sezione è una figura piana che appartiene al piano secante

La prima cosa da non dimenticare è questa: dopo aver affettato il solido con il piano, il risultato è una figura piana, e quella figura piana appartiene al piano secante.

La regola, già scritta nella [[11-assonometria-cavaliera-e-sezioni-dei-solidi|bozza del 10 novembre]], è che le sezioni si risolvono con le intersezioni tra il piano secante e i piani che contengono le facce del solido, una faccia alla volta.

Il libro la dice così (applicazione 22, p. 120): la sezione è una figura piana, che appartiene al piano secante ed ha i vertici sugli spigoli del solido. I vertici di questa figura sono i punti di intersezione tra i singoli spigoli del solido e le rette generate, di volta in volta, dall'intersezione tra il piano secante e i piani che contengono le facce del solido.

Ogni volta quindi si parte da un problema già noto, un esercizio di intersezione tra due piani, come nel PDF della docente:

1. si individua il piano della faccia che si sta considerando;
2. si trova la retta di intersezione tra questo piano e il piano secante;
3. si guarda dove questa retta incontra gli spigoli della faccia che si sta considerando: quelli, e solo quelli, sono i punti della sezione.

Il terzo passaggio è quello in cui si sbaglia più facilmente. Sul disegno la retta di intersezione può sembrare che incontri quattro spigoli, ma non è vero: contano solo gli spigoli della faccia che si sta considerando, cioè gli spigoli del solido a cui appartiene quella faccia.

### Le rette di intersezione da riconoscere

Per fare in fretta conviene riconoscere subito che tipo di retta nasce dall'intersezione di due piani. Il libro, accanto alle applicazioni 22 e 23 (pp. 121 e 123), ne fissa quattro:

- due piani verticali si incontrano in una retta verticale;
- un piano proiettante in seconda e un piano frontale si incontrano in una frontale;
- un piano orizzontale e un piano proiettante in seconda si incontrano in una retta proiettante in seconda;
- un piano proiettante in prima e un piano di profilo si incontrano in una retta verticale, quindi proiettante in prima.

In tutti i casi le tracce della retta di intersezione si trovano dove si incontrano le tracce dei due piani: la prima traccia della retta dove si incontrano le prime tracce, la seconda dove si incontrano le seconde.

### Il parallelepipedo tagliato da un piano proiettante in seconda

L'esempio della docente è un parallelepipedo con le facce parallele ai piani di proiezione, tagliato da un piano α proiettante in seconda.

Il piano α taglia due facce: il fianco destro e la faccia superiore. Si considerano una alla volta.

Il fianco destro sta in un piano di profilo, β, che la docente chiama «il piano β verticale». Si cerca l'intersezione tra il piano proiettante in seconda α e il piano di profilo β:

- la retta di intersezione r appartiene a entrambi i piani;
- è una retta proiettante in seconda, cioè parallela a π₁ e perpendicolare a π₂;
- quindi in seconda proiezione è un punto, r₂, che sta sulla seconda traccia di α: è la sua traccia T₂ᵣ.

Se proprio non si riesce a vederla, c'è la terza proiezione. Ma la retta di intersezione è questa.

La retta r taglia i due spigoli orizzontali del fianco nei punti 1 e 2: è la prima linea di sezione. In seconda proiezione i due punti coincidono, perché stanno su una retta proiettante in seconda.

La faccia superiore sta in un piano orizzontale, γ. Questa volta l'intersezione è tra un piano proiettante in seconda e un piano orizzontale:

- anche in questo caso la retta di intersezione, s, è una retta proiettante in seconda;
- si costruisce la retta e si guarda dove intercetta gli spigoli della faccia superiore, cioè del rettangolo superiore: sono i punti 3 e 4.

Le due rette danno due linee di sezione, e significa che del solido rimane una parte orizzontale della faccia superiore, mentre la sezione sta sul fianco, lateralmente.

La sezione 1-2-3-4 si tratteggia in maniera ordinata:

- in seconda proiezione è il segmento che sta su t₂α, perché α si vede di taglio;
- in prima proiezione si vede dall'alto, come un rettangolo, e si campisce.

Quello che porta a risolvere la sezione è quindi il principio dell'intersezione tra i piani: si individua la retta di intersezione e il punto in cui questa retta intercetta esclusivamente gli spigoli della faccia che si sta considerando.

La stessa cosa si può fare con un piano verticale, con l'intersezione tra piani verticali (Disegni 9 e 10 della [[11-assonometria-cavaliera-e-sezioni-dei-solidi|bozza 11]]). La docente consiglia di esercitarsi anche con un piano orizzontale.

> [!example] Disegno 1 · Il disegno: il parallelepipedo tagliato da un piano proiettante in seconda
> ![[15-ripasso-parallelepipedo-piano-proiettante-in-seconda.svg|620]]
>
> 1. Si disegnano le due proiezioni del parallelepipedo e le tracce di α: t₂α obliqua, t₁α perpendicolare alla LT.
> 2. Fianco destro: il piano di profilo β ha t₁β e t₂β perpendicolari alla LT. r = α ∩ β è proiettante in seconda: r₂ è il punto in cui t₂α incontra il fianco, r₁ è perpendicolare alla LT.
> 3. r taglia gli spigoli orizzontali del fianco in 1 e 2 (in seconda 1₂ ≡ 2₂); con le linee di richiamo si trovano 1₁ e 2₁.
> 4. Faccia superiore: il piano orizzontale γ ha t₂γ parallela alla LT alla quota della faccia. s = α ∩ γ è di nuovo proiettante in seconda: s₂ è un punto su t₂α, s₁ è perpendicolare alla LT.
> 5. s taglia gli spigoli della faccia superiore in 3 e 4 (a lezione la docente li chiama di nuovo 1 e 2).
> 6. La sezione 1-2-3-4: in seconda è il segmento su t₂α, in prima è il rettangolo che si campisce. Il pezzo di solido sopra α si toglie.

> [!example] Disegno 2 · Il disegno nello spazio: lo stesso parallelepipedo
> ![[b15-spazio-parallelepipedo-proiettante-in-seconda.svg|620]]
>
> 1. Il piano α (in rosa) è perpendicolare a π₂: per questo su π₂ si vede di taglio, come la retta t₂α, e t₁α è perpendicolare alla LT.
> 2. Il fianco destro sta nel piano di profilo β (tracce verdi t₁β e t₂β); la faccia superiore nel piano orizzontale γ (traccia t₂γ, parallela alla LT).
> 3. α taglia β lungo r e γ lungo s: sono due rette perpendicolari a π₂, che lo bucano nei punti r₂ e s₂, tutti e due su t₂α.
> 4. r incontra gli spigoli del fianco in 1 e 2, s quelli della faccia superiore in 3 e 4. Il rettangolo 1-2-3-4 è inclinato; la parte del solido sopra α (in grigio) si elimina.

### Il prisma tagliato da un piano generico (dal libro)

A lezione la docente ha fatto il prisma con il piano proiettante in seconda. Il libro risolve lo stesso tipo di solido con un piano generico, nelle applicazioni 24 e 25 (pp. 124-131), contemporaneamente in proiezioni ortogonali e in cavaliera militare. Il procedimento è lo stesso, con qualche passaggio in più.

1. I punti a terra. Si individuano prima i due punti della sezione che stanno a terra: sono le intersezioni tra la prima traccia del piano secante e gli spigoli di base, che sono a quota zero.
2. La faccia anteriore. Si considera il piano frontale ε che la contiene (t₁ε ≡ r₁) e si trova la retta di intersezione r tra questo piano e il piano secante. L'intersezione tra un piano generico e un piano frontale è una frontale: r₂ è parallela a t₂α e interseca uno spigolo verticale.
3. La faccia posteriore. Lo stesso con il piano frontale δ (t₁δ ≡ m₁): la retta di intersezione m è un'altra frontale, e la sua intersezione con gli spigoli della faccia dà altri punti della sezione.
4. Il fianco. Per valutare l'andamento della sezione lungo il piano laterale del solido, che è di profilo, occorre ribaltare questo piano e la retta di intersezione p tra il piano laterale e il piano secante: nel ribaltamento si trova il punto 5\* sullo spigolo, e lo si riporta nelle due proiezioni.

Il libro fa notare due scorciatoie.

La prima: lo stesso risultato si sarebbe potuto ottenere sul ribaltamento riportando i punti della sezione già trovati sugli spigoli del piano laterale.

La seconda (applicazione 25, p. 130): data la posizione del solido rispetto a π₂, le rette di intersezione sulle due facce laterali opposte, destra e sinistra, sono parallele tra loro, perché le due facce sono parallele. Quindi basta riportare sul ribaltamento laterale i punti trovati sulla faccia di sinistra e costruire la parallela sulla faccia destra.

Quando il prisma è ruotato in pianta (applicazione 26, pp. 132-135), le facce laterali stanno su piani proiettanti in prima. In questo caso la retta di intersezione tra la faccia e il piano secante incontra due spigoli della faccia, quello lungo la retta inclinata e quello lungo la retta di base; e i punti a terra si trovano facilmente, perché sono intersezioni tra rette che appartengono a π₁, cioè tra gli spigoli a terra e la traccia del piano secante.

Alla fine, in tutti gli esercizi del libro, l'ultima consegna è: completare il solido risultante.

## LA SEZIONE DELLA PIRAMIDE

### Perché nella piramide si usano i piani che passano per gli spigoli

Nel caso della piramide cambia una cosa sola: le facce appartengono a piani inclinati.

Trovare le tracce dei piani inclinati delle facce si può fare, ma è un'operazione lunga.

D'altra parte non si può fare come nel prisma, cioè dalla pianta costruire il piano verticale di una faccia: nella piramide non ci sono facce verticali, e quel piano non appartiene alla piramide.

Quali sono allora i piani verticali che si possono costruire in una piramide? Sono quelli che passano per il vertice e contengono uno spigolo:

- per esempio il piano che passa per lo spigolo VA è un piano proiettante in prima, con la prima traccia che passa per V₁ e A₁;
- un altro è il piano proiettante in prima che passa per V e per C;
- si possono usare anche i piani proiettanti in seconda, che contengono sempre gli spigoli, ma hanno la seconda traccia che passa per V₂ e per la seconda proiezione dello spigolo.

È la stessa indicazione del libro (applicazione 27, p. 136): per disegnare questa sezione non si considerano i piani inclinati delle facce, ma i piani verticali passanti per gli spigoli e per il vertice. Nella versione in assonometria (applicazione 3 delle proiezioni assonometriche, p. 167) il libro aggiunge il motivo: per costruire la sezione basta individuare i punti lungo gli spigoli, e questi piani contengono il vertice e la sua prima proiezione.

In questo caso, quando si cerca il punto della sezione, non si può più dire «gli spigoli della faccia»: si deve dire «lo spigolo che sto considerando», cioè lo spigolo per cui si è fatto passare il piano.

### Il teorema di Desargues nello spazio

C'è poi una cosa da tenere presente, che aiuta a risolvere le sezioni della piramide con l'omologia: il teorema di Desargues nello spazio.

Desargues definisce il teorema omologico proprio a partire dalla piramide: esiste un'omologia nello spazio.

Si prenda una piramide a base triangolare e la si tagli con un piano: si ottiene un altro triangolo. Allora:

- i vertici dei due triangoli sono allineati con un unico punto, il vertice della piramide: quel punto è il centro dell'omologia;
- i lati dei due triangoli, a due a due, si incontrano su una retta fissa: quella retta è l'asse dell'omologia.

Il motivo si vede bene nella piramide. Ogni punto della sezione sta su uno spigolo, quindi è allineato con il vertice. E ogni lato della sezione sta nella stessa faccia del lato di base corrispondente: i due lati sono complanari e si incontrano in un punto che appartiene sia al piano della base sia al piano secante.

L'asse dell'omologia, come sempre, è la retta di intersezione tra i due piani che si stanno considerando. Quando la base sta su π₁, l'asse è la prima traccia del piano secante.

Questo vale qualunque sia il piano con cui si taglia la piramide. Anche se la si taglia con un piano orizzontale si ottiene un triangolo, e quel triangolo è un'omotetia della base: l'asse va all'infinito, ma l'omologia c'è sempre.

Nel libro il teorema è illustrato a p. 12 (fig. 18): le due figure, su piani sovrapposti, sono considerate come la proiezione di una stessa figura, che appartiene a un terzo piano, da due centri di proiezione distinti; il disegno sul foglio mostra tutti gli elementi sui piani sovrapposti, così che si possa operare direttamente sul foglio da disegno. Il libro aggiunge che il teorema tornerà molto utile nella determinazione della prima proiezione delle sezioni di piramidi, sia nelle proiezioni ortogonali sia in quelle assonometriche.

> [!example] Disegno 3 · Il disegno nello spazio: il teorema di Desargues
> ![[15-ripasso-teorema-di-desargues-nello-spazio.svg|620]]
>
> 1. La piramide ha la base ABC sul piano orizzontale e il vertice V. Il piano secante la taglia lungo il triangolo A′B′C′, con A′ su VA, B′ su VB, C′ su VC.
> 2. I vertici corrispondenti sono allineati con V: V è il centro dell'omologia.
> 3. I lati corrispondenti (AB e A′B′, BC e B′C′, CA e C′A′) stanno nella stessa faccia, quindi si incontrano, in X, Y e Z. Questi punti stanno sia sul piano della base sia sul piano secante: sono tutti sulla retta in cui i due piani si tagliano, l'asse dell'omologia.
> 4. Se il piano secante è orizzontale, l'asse va all'infinito e il triangolo di sezione è un'omotetia della base.

### Dall'omologia nello spazio all'omologia sul foglio

Nelle proiezioni ortogonali l'omologia nello spazio diventa un'omologia sul foglio, in prima proiezione.

Proiettando tutto su π₁, infatti:

- la base ABC sta già su π₁ e non cambia;
- il vertice V va in V₁, e i punti della sezione restano allineati con V₁, perché stanno sugli spigoli, che in pianta sono le rette da V₁ ai vertici della base;
- l'asse, la prima traccia del piano secante, sta già su π₁ e non cambia.

Quindi la base della piramide e la prima proiezione della sezione sono omologhe: il centro è V₁ e l'asse è t₁α.

Il libro (applicazione 27, p. 138) dice che l'omologia è definita quando si conoscono l'asse, il centro e una coppia di elementi corrispondenti. L'asse è la prima traccia del piano secante, il centro è il vertice, V₁, e la coppia è data da un vertice della base e dal punto di sezione sul suo spigolo, che sono allineati con il centro.

Ne viene una conseguenza pratica molto comoda: per costruire la sezione in pianta basta trovare un solo punto di sezione lungo uno degli spigoli, e poi applicare il teorema di Desargues (p. 136).

Lo stesso vale in assonometria (applicazione 3 delle proiezioni assonometriche, p. 168): il teorema di Desargues, applicato sul piano e nello spazio, consente di completare il disegno rispettivamente nelle proiezioni ortogonali e in assonometria. In entrambi i casi la prima traccia del piano secante è anche l'asse dell'omologia, e il vertice della piramide ne è il centro.

### La piramide alla lavagna: i dati

La docente fa una sezione un po' particolare:

- la pianta della piramide ha il lato AC parallelo alla linea di terra;
- il prospetto non è molto alto, perché la parte alta si stringe;
- il piano secante α è generico, con la prima traccia parallela al lato AB.

Si comincia dalla cosa più facile, cioè dall'intersezione tra piani, facendo passare i piani per gli spigoli e quindi anche per i vertici.

> [!example] Disegno 4 · Il disegno nello spazio: la piramide, il piano α e i piani per gli spigoli
> ![[b15-spazio-piramide-piani-per-gli-spigoli.svg|620]]
>
> 1. La base ABC sta su π₁; il piano secante α (in rosa) è generico, con t₁α parallela ad AB.
> 2. Il piano β (tracce verdi) è verticale e contiene lo spigolo VC: t₁β passa per C e per la proiezione di V su π₁, t₂β è perpendicolare alla LT. α taglia β lungo la retta r, che va da T₁ᵣ (su t₁α) a T₂ᵣ (su t₂α) e incontra lo spigolo VC nel punto 1.
> 3. Il piano γ (tracce viola) è perpendicolare a π₂ e contiene lo spigolo VA: t₂γ passa per V₂ e A₂, t₁γ è perpendicolare alla LT. α taglia γ lungo la retta s, da T₁ₛ a T₂ₛ, che incontra lo spigolo VA nel punto 2.
> 4. Il terzo punto, sullo spigolo VB, si trova senza un altro piano. La sezione 1-2-3 (in rosso) sta tutta nel piano α.

### Il punto 1 con un piano proiettante in prima

1. Si costruisce il piano β proiettante in prima che passa per V e per C: la prima traccia t₁β passa per V₁C₁, la seconda t₂β è perpendicolare alla linea di terra.
2. Si cerca l'intersezione tra il piano generico α e il piano proiettante in prima β. La retta di intersezione r ha le tracce dove si incontrano le tracce: T₂ᵣ dove t₂α incontra t₂β, T₁ᵣ dove t₁α incontra t₁β.
3. Si costruisce la retta: r₁ coincide con t₁β, perché tutto ciò che appartiene a un piano proiettante in prima ha la prima proiezione sulla prima traccia; r₂ unisce (T₁ᵣ)₂ con T₂ᵣ.
4. Si guarda dove la retta di intersezione intercetta lo spigolo che si sta considerando, CV. In seconda proiezione r₂ incontra V₂C₂ nel punto 1₂.

Graficamente r₂ sembra incontrare tutti e tre gli spigoli. Ma il punto è solo quello in cui la retta incontra lo spigolo per cui si è fatto passare il piano. Per questo conviene avere messo le lettere: V₂, C₂.

5. Il punto 1₂ si riporta in prima proiezione con la linea di richiamo, sullo spigolo V₁C₁: si trova 1₁.

In prima proiezione il punto non si poteva trovare direttamente, perché r₁ sta sopra lo spigolo.

### Il punto 2 con un piano proiettante in seconda

Per lo spigolo successivo ci sono vari modi. La docente ne mostra uno con un piano proiettante in seconda: non è necessario, ma serve a far vedere che si possono usare anche questi piani.

1. Si costruisce il piano γ proiettante in seconda che passa per lo spigolo VA: t₂γ passa per V₂A₂, t₁γ è perpendicolare alla linea di terra.
2. Si cerca l'intersezione tra il piano generico α e il piano proiettante in seconda γ, sempre allo stesso modo: T₂ₛ dove t₂α incontra t₂γ, T₁ₛ dove t₁α incontra t₁γ.
3. Si costruisce la retta s: s₂ coincide con t₂γ; s₁ unisce T₁ₛ con (T₂ₛ)₁.
4. Dove si trova ora il punto? In seconda non si può trovare, perché lì la retta sta sopra lo spigolo. Si trova in prima: s₁ incontra V₁A₁ nel punto 2₁.
5. Con la linea di richiamo si trova 2₂ su V₂A₂.

La regola si rovescia rispetto al punto 1: con un piano proiettante in prima il punto si legge in seconda proiezione, con un piano proiettante in seconda si legge in prima.

> [!example] Disegno 5 · Il disegno: i punti 1 e 2 con i piani proiettanti per gli spigoli
> ![[15-ripasso-piramide-punti-1-e-2-piani-proiettanti.svg|620]]
>
> 1. La base A₁B₁C₁ ha AC parallelo alla LT; il piano α è generico, con t₁α parallela ad A₁B₁.
> 2. β proiettante in prima per VC: t₁β per V₁C₁ (e r₁ ≡ t₁β), t₂β perpendicolare alla LT.
> 3. T₁ᵣ = t₁α ∩ t₁β, T₂ᵣ = t₂α ∩ t₂β. Da T₁ᵣ si scende sulla LT in (T₁ᵣ)₂ e si traccia r₂ = (T₁ᵣ)₂T₂ᵣ.
> 4. r₂ incontra V₂C₂ in 1₂; con il richiamo si trova 1₁ su V₁C₁.
> 5. γ proiettante in seconda per VA: t₂γ per V₂A₂, t₁γ perpendicolare alla LT. T₂ₛ = t₂α ∩ t₂γ, T₁ₛ = t₁α ∩ t₁γ; s₁ unisce T₁ₛ con (T₂ₛ)₁.
> 6. s₁ incontra V₁A₁ in 2₁; con il richiamo si trova 2₂ su V₂A₂.

### Il punto 3 con l'omologia

A questo punto, in realtà, si è quasi finito.

La sezione è una figura che appartiene al piano secante, e il punto 2 è un punto della sezione, perché appartiene al piano secante. Si considera la faccia A₁V₁B₁.

Il lato di base AB è parallelo alla prima traccia del piano. Se il solido ha un lato parallelo al piano di taglio, tutte le sezioni che si fanno con piani disposti in quel modo danno un elemento parallelo: quindi anche la sezione su questa faccia è parallela ad AB.

Lo stesso risultato si ottiene con il teorema di Desargues, applicando l'omologia:

- l'asse dell'omologia è la prima traccia di α;
- il centro è V₁;
- A₁ e 2₁ sono due punti corrispondenti, perché sono allineati con il centro;
- la retta A₁B₁ è parallela all'asse, quindi la retta omologa che passa per 2₁ è anch'essa parallela all'asse.

Da 2₁ si costruisce la parallela e ci si ferma sull'altro spigolo, V₁B₁: lì c'è 3₁.

Attenzione però: per applicare l'omologia bastava già il punto 1. Se il disegno è fatto bene, prolungando A₁C₁ fino all'asse e unendo quel punto con 1₁ si deve ritrovare il punto 2: cioè l'omologia deve tornare. È un controllo da fare sempre.

### La sezione in seconda proiezione

L'unico problema è il disegno in seconda.

Il punto 1 c'è già, e il punto 2 si trova facilmente con il richiamo. Ma il punto 3 sta sullo spigolo VB, che in questa piramide è una retta di profilo: V₂B₂ e V₁B₁ stanno sulla stessa perpendicolare alla linea di terra, e con il solo richiamo non si sa dove fermarsi.

Si sa invece dove fermarsi se ci si chiede che retta è 2-3. La sezione è una figura che appartiene al piano, quindi 2-3 è una retta del piano α; ed è parallela a t₁α, quindi è un'orizzontale del piano. In seconda proiezione 2₂3₂ è parallela alla linea di terra: 3₂ sta su V₂B₂ alla stessa quota di 2₂.

In alternativa si può prolungare 1-3 fino all'asse, cioè fino alla prima traccia di α: il punto trovato è la traccia della retta 1-3, e unendo la sua seconda proiezione, sulla linea di terra, con 1₂ si trova 3₂ su V₂B₂.

La sezione si ripassa e si campisce in prima e in seconda proiezione.

> [!example] Disegno 6 · Il disegno: il punto 3 con l'omologia e l'orizzontale 2-3
> ![[15-ripasso-piramide-punto-3-omologia.svg|620]]
>
> 1. In prima proiezione c'è un'omologia tra la base A₁B₁C₁ e la sezione 1₁2₁3₁: il centro è V₁, l'asse è t₁α.
> 2. A₁B₁ è parallela all'asse, quindi anche il lato di sezione per 2₁ è parallelo all'asse: da 2₁ la parallela ad A₁B₁ incontra V₁B₁ in 3₁.
> 3. Controllo: si prolunga A₁C₁ fino all'asse, in K; la retta da K a 1₁ deve passare per 2₁.
> 4. In seconda VB è una retta di profilo: il richiamo non basta. Ma 2-3 è un'orizzontale di α, quindi 2₂3₂ è parallela alla LT e 3₂ sta su V₂B₂ alla quota di 2₂.
> 5. La sezione 1-2-3 si ripassa e si campisce nelle due proiezioni.

### Il ribaltamento della sezione

Nella prova può essere chiesto anche il ribaltamento della sezione, per vederla in vera forma.

Bisogna ricordare il procedimento del ribaltamento del punto e del ribaltamento di un poligono, studiati nelle lezioni sul [[07-il-ribaltamento|ribaltamento]] e sul [[09-ribaltamento-del-piano-generico|ribaltamento del piano generico]]. A seconda della posizione della figura le cose possono cambiare leggermente, ma sostanzialmente la questione rimane sempre la stessa.

Il principio è quello della squadretta con un lato sul tavolo, che deve arrivare sul piano: nello spazio il punto si muove lungo un piano perpendicolare all'asse di rotazione, che contiene il raggio di rotazione. Quello che si cerca di costruire è il triangolo rettangolo in cui il raggio è contenuto:

1. si costruisce un piano perpendicolare all'asse, cioè un piano proiettante;
2. lo si ribalta, ribaltando la quota del punto;
3. si ricostruisce il raggio di rotazione.

Se la figura sta in un piano parallelo alla linea di terra la costruzione di questo piano è più facile, ma non cambia niente. Se la figura è in un piano generico bisogna trovare una traccia; ma è una traccia facile, perché sta sempre a terra.

Molti studenti pensano che sia necessario trovare prima la retta di massima pendenza. Non lo è: quello che è importante è ribaltare la quota del punto. Si costruisce la perpendicolare alla traccia e si riporta solo la quota del punto.

Nella sezione della piramide il piano α si ribalta su π₁ intorno alla sua prima traccia:

1. da 1₁ si costruisce la perpendicolare a t₁α, che la incontra nel punto H;
2. in 1₁, parallela all'asse, si riporta la quota di 1, letta in seconda proiezione: il segmento da H all'estremo della quota è il raggio di rotazione, l'ipotenusa del triangolo rettangolo;
3. con il compasso, centro in H, si riporta il raggio sulla perpendicolare: si trova 1\*;
4. per gli altri punti si usa l'affinità che ha per asse t₁α e direzione perpendicolare all'asse: si prolunga 1₁3₁ fino all'asse, e da quel punto si va verso 1\*; dove la retta incontra la perpendicolare all'asse condotta da 3₁ c'è 3\*;
5. 2-3 è parallela all'asse, quindi anche 2\*3\* è parallela all'asse: da 3\* la parallela all'asse incontra la perpendicolare condotta da 2₁ in 2\*.

Il triangolo 1\*2\*3\* è la sezione in vera forma.

> [!example] Disegno 7 · Il disegno: il ribaltamento della sezione su π₁
> ![[15-ripasso-piramide-ribaltamento-sezione.svg|620]]
>
> 1. Si ribalta α su π₁ intorno a t₁α. Non serve la retta di massima pendenza: basta ribaltare la quota di un punto.
> 2. Da 1₁ la perpendicolare a t₁α dà il piede H.
> 3. In 1₁, parallela all'asse, si riporta la quota di 1: da H a quell'estremo c'è il raggio di rotazione.
> 4. Con il compasso, centro H, si porta il raggio sulla perpendicolare e si trova 1\*. Qui il ribaltamento è fatto dalla parte opposta alla piramide, così la sezione ribaltata non si sovrappone alla pianta.
> 5. Con l'affinità: 1₁3₁ prolungata fino all'asse in K, da K verso 1\*, e sulla perpendicolare all'asse da 3₁ si trova 3\*.
> 6. 2\*3\* è parallela all'asse: si trova 2\* sulla perpendicolare da 2₁. Il triangolo 1\*2\*3\* è in vera forma.

### Esercizio 1: la sezione della piramide con un solo punto e l'omologia (dal libro)

> [!example] Esercizio 1 · Applicazione 27 del libro (pp. 136-140)
> Una piramide a base triangolare ABC, con la base su π₁ e il vertice V, è tagliata da un piano generico α, dato con le tracce t₁α e t₂α. Disegnare la sezione nelle due proiezioni, trovando con un piano ausiliario un solo punto e gli altri con il teorema di Desargues.

> [!success]- Soluzione
> Risultato: la sezione è il triangolo 1-2-3, con 1 sullo spigolo VC, 2 su VA e 3 su VB. In pianta 1₁2₁3₁ è il triangolo omologo di C₁A₁B₁ nell'omologia che ha il centro in V₁ e l'asse in t₁α; in seconda proiezione 1₂2₂3₂ si trova con le linee di richiamo.
>
> ![[b15-libro-p139-sezione-piramide-desargues.png|520]]
> *La sezione 1-2-3 in pianta e in prospetto; in pianta U ≡ V₁ è il centro dell'omologia e t₁α ≡ u l'asse (dal libro della prof, allegato, applicazione 27, p. 139).*
>
> Come si arriva:
> 1. Si costruisce il piano β proiettante in prima che contiene lo spigolo VC: t₁β passa per V₁ e C₁, t₂β è perpendicolare alla LT. Si usa un piano verticale per lo spigolo, e non il piano inclinato della faccia, perché è molto più facile da disegnare.
> 2. Si trova la retta m = α ∩ β: T₁ₘ dove t₁α incontra t₁β, T₂ₘ dove t₂α incontra t₂β. m₁ coincide con t₁β; m₂ unisce (T₁ₘ)₂, sulla LT, con T₂ₘ.
> 3. m₂ incontra lo spigolo V₂C₂ nel punto 1₂, perché lo spigolo VC e la retta m stanno tutti e due nel piano β. Con il richiamo si trova 1₁ su V₁C₁.
> 4. Si imposta l'omologia di Desargues: l'asse è t₁α, perché è la retta in cui il piano secante incontra il piano della base; il centro è V₁, perché tutti gli spigoli passano per il vertice; la coppia di punti corrispondenti è C₁ e 1₁, allineati con il centro.
> 5. Punto 2: si prolunga il lato C₁A₁ fino all'asse; da quel punto si traccia la retta che passa per 1₁. È la corrispondente di C₁A₁, perché due rette corrispondenti si incontrano sull'asse. Dove incontra lo spigolo V₁A₁ c'è 2₁.
> 6. Punto 3: lo stesso con il lato C₁B₁, prolungato fino all'asse e unito con 1₁; dove la retta incontra V₁B₁ c'è 3₁.
> 7. Seconda proiezione: con le linee di richiamo si portano 2₁ su V₂A₂ e 3₁ su V₂B₂. Funziona perché in questa piramide nessuno dei due spigoli è di profilo; se lo fosse, come nella piramide della lavagna, si userebbe un'orizzontale del piano o una retta della sezione prolungata fino all'asse.
> 8. Si ripassa la sezione, la si campisce e si completa il disegno del solido risultante, togliendo la parte di piramide che sta sopra il piano.

## IL COMPITO: IL SEGMENTO PERPENDICOLARE A UN PIANO GENERICO

Alla fine della lezione la docente lascia una domanda per la volta successiva.

Si immagini una tavola inclinata, da cui si vuole far uscire un segmento perpendicolare alla tavola: dato un punto che appartiene al piano, come si costruisce un segmento di lunghezza data (nella registrazione si sente 13 cm) perpendicolare al piano generico? Sul piano potrebbe esserci anche una piramide, o qualunque altro solido.

La prima cosa è costruire la perpendicolare, e per la perpendicolare servono l'orizzontale e la frontale del piano. La spiegazione completa è rimandata alla lezione successiva.

È lo stesso problema dell'esercizio 2 della [[10-intersezione-retta-piano-e-segno-di-sezione|lezione del 5 novembre]], lì con una figura piana e una lunghezza di 3 cm, e dell'applicazione 7 del libro (pp. 71-74), il solido alzato perpendicolarmente a un piano generico. La soluzione qui sotto applica quel procedimento a ritroso; i disegni sono nella bozza 10 (Disegni 9 e 10).

> [!example] Esercizio 2 · Il segmento perpendicolare al piano generico (proposto)
> È dato un piano generico α con le sue tracce e un punto P che gli appartiene. Costruire il segmento PQ perpendicolare ad α, lungo 13 cm, che esce dal piano verso l'alto.

> [!success]- Soluzione
> Risultato: P₁Q₁ sta sulla perpendicolare a t₁α condotta da P₁, P₂Q₂ sulla perpendicolare a t₂α condotta da P₂; nelle proiezioni il segmento appare più corto di 13 cm, perché è inclinato rispetto a tutti e due i piani di proiezione, e i 13 cm si misurano solo nel ribaltamento.
>
> Come si arriva:
> 1. Si costruisce la perpendicolare n ad α per P: n₁ perpendicolare a t₁α, n₂ perpendicolare a t₂α. È il teorema di Monge della [[06-piani-ausiliari-e-perpendicolarita|lezione del 20 ottobre]]: le proiezioni di una retta perpendicolare a un piano sono perpendicolari alle tracce del piano, cioè anche all'orizzontale (in prima) e alla frontale (in seconda) del piano.
> 2. Si sceglie un punto qualunque S su n, con S₂ su n₂ e S₁ su n₁ alla stessa linea di richiamo. Serve per avere due punti della retta da ribaltare.
> 3. Si considera il piano γ proiettante in prima che contiene n: la sua prima traccia coincide con n₁. Lo si ribalta su π₁ girandolo intorno a t₁γ: P\* e S\* stanno sulle perpendicolari a n₁ condotte da P₁ e da S₁, a una distanza uguale alle rispettive quote.
> 4. La retta P\*S\* è n ribaltata, in vera grandezza: su di essa, a partire da P\* e verso l'alto, si misurano 13 cm e si trova Q\*. Si misura qui perché nel ribaltamento le misure sono vere.
> 5. A ritroso: da Q\* si torna su n₁ con la perpendicolare a n₁, e si trova Q₁; con la linea di richiamo si trova Q₂ su n₂.
> 6. Controllo: la distanza di Q\* da Q₁ deve essere uguale alla quota di Q, cioè alla distanza di Q₂ dalla linea di terra.

> [!tip] Avvisi della docente per la Prova n. 2 (giovedì 26 novembre)
> - Gli argomenti ripassati sono l'assonometria, i piani delle facce di un solido, le sezioni del prisma e della piramide e il ribaltamento della sezione.
> - Prepararsi un foglio A3 con tutte le assonometrie, svolte correttamente.
> - Nei disegni mettere sempre le lettere: aiuta moltissimo a riconoscere piani e rette.
> - Chiedersi: «so individuare i piani nelle proiezioni ortogonali? E in assonometria?». Prima di fare una sezione bisogna saper costruire i piani delle facce.
> - La sezione è una figura piana che appartiene al piano secante: non dimenticarlo. Si ripassa e si campisce con un tratteggio ordinato.
> - I punti della sezione sono solo quelli in cui la retta di intersezione incontra gli spigoli della faccia, o lo spigolo, che si sta considerando.
> - Nella piramide usare i piani proiettanti per gli spigoli e il teorema di Desargues, e controllare che l'omologia torni.
> - Il ribaltamento della sezione può essere chiesto: non serve la retta di massima pendenza, si ribalta la quota del punto.
> - Esercitarsi anche con le sezioni con un piano orizzontale e con i piani verticali.
> - Ripassare gli esercizi iniziali sulle rette, che sono sul PDF e sul libro: torneranno utili per le ombre.
> - Non saltare le lezioni per preparare la prova: le assenze si vedono.

## Collegamenti

Le sezioni di questa lezione mettono insieme quasi tutto il programma di proiezioni ortogonali. I piani proiettanti, di profilo e orizzontali che contengono le facce sono quelli dei [[04-rette-e-piani-nelle-varie-posizioni|piani nelle varie posizioni]]; la regola per cui le tracce della retta di intersezione stanno dove si incontrano le tracce dei due piani, e il fatto che una retta che appartiene a un piano proiettante ha la proiezione sulla sua traccia, vengono dalle [[05-appartenenza-e-rette-ausiliarie|condizioni di appartenenza]] e dai [[06-piani-ausiliari-e-perpendicolarita|piani ausiliari]]. Il procedimento «una faccia alla volta» è quello della [[11-assonometria-cavaliera-e-sezioni-dei-solidi|lezione del 10 novembre]], che a sua volta applica alle facce dei solidi l'[[10-intersezione-retta-piano-e-segno-di-sezione|intersezione tra retta e piano]]; i solidi stessi, con le loro proiezioni, sono riassunti negli appunti [[PO 7 - Figure piane e solidi]].

Il teorema di Desargues riporta all'inizio del corso: l'omologia, con il suo centro, il suo asse e le coppie di punti corrispondenti, è quella studiata nella [[02-proiezioni-e-omologia-schema|seconda lezione]] e negli appunti di [[teoria-omologia|teoria dell'omologia]], e la regola dell'esercizio «madre» della [[12-errori-della-prova-1-e-quadro-verticale|correzione della Prova n. 1]] (prolungare una retta fino all'asse e da lì passare per il punto corrispondente) è proprio quella che dà i punti 2 e 3 della sezione. L'omotetia della sezione orizzontale è il caso dell'omologia con l'asse all'infinito.

Il ribaltamento della sezione è il ribaltamento del piano generico in forma canonica della [[09-ribaltamento-del-piano-generico|lezione del 29 ottobre]], con la squadretta e il raggio di rotazione, e il resto della figura si trova con l'affinità ortogonale dell'[[02-affinita-ortogonale-passo-passo|esercizio passo passo]]. Il segmento perpendicolare a un piano generico riprende la perpendicolarità di Monge e il procedimento a ritroso della [[10-intersezione-retta-piano-e-segno-di-sezione|bozza 10]].

L'assonometria con la pianta ribaltata è quella della [[12-errori-della-prova-1-e-quadro-verticale|lezione del 12 novembre]], e il confronto con la prospettiva, dove le parallele non restano parallele, rimanda alle lezioni di prospettiva che occupano la prima parte della stessa giornata (sbobine [[13-prospettiva-metodo-della-pianta]] e [[14-prospettiva-altezze-e-punto-di-misura]]). Le sezioni dei solidi, infine, sono la base geometrica delle piante e delle sezioni architettoniche che si disegnano per la casa da studiare ([[studio-villa-tugendhat|Villa Tugendhat]]).

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[566_3.pdf]]: allegato multimediale del libro della docente. Teoria: «Teorema di Desargues» (p. 12, fig. 18, p. 32 del testo a stampa). Esercizi sulle sezioni: applicazione 22, sezioni di solidi con piani verticali, proiettanti, paralleli alla LT, con le regole sulle rette di intersezione e il ribaltamento laterale (pp. 120-121); applicazione 23, sezioni di piramidi e prismi con piani frontali, orizzontali, di profilo e proiettanti (pp. 122-123); applicazioni 24 e 25, prisma tagliato da un piano generico, in proiezioni ortogonali e in cavaliera militare, con il ribaltamento del piano laterale (pp. 124-131); applicazione 26, prisma ruotato in pianta tagliato da un piano generico (pp. 132-135); applicazione 27, sezione della piramide con un piano proiettante in prima e il teorema di Desargues (pp. 136-140, Esercizio 1); applicazioni 3 e 4 delle proiezioni assonometriche, le stesse sezioni in cavaliera militare (pp. 166-173). Per il compito: applicazione 7, solido alzato perpendicolarmente a un piano generico (pp. 71-74)
- [[2agg_Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: data della Prova n. 2 (26 novembre)
