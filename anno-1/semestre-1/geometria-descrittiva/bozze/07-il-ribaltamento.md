---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-22
tags: [geometria-descrittiva, bozza]
---

# Il ribaltamento

> [!info] Note collegate
> Sbobina: [[07-ribaltamento-piani-proiettanti]]
>
> Bozza precedente: [[06-piani-ausiliari-e-perpendicolarita]]

Quando una figura sta su un piano proiettante, le sue proiezioni non dicono quanto è grande davvero:

- in una proiezione la figura si schiaccia su una linea,
- nell'altra appare deformata, con lati e angoli diversi da quelli veri.

Per conoscerne la vera grandezza e forma bisogna far ruotare il piano che la contiene intorno a una delle sue tracce, finché non si appoggia su un piano di proiezione: questa operazione si chiama ribaltamento.

La lezione di giovedì 22 ottobre ha mostrato il ribaltamento dei piani proiettanti in prima e in seconda, su π₁ e su π₂, e ha spiegato perché tra la proiezione di una figura e il suo ribaltamento esiste una relazione omologica, l'omologia di ribaltamento.

Nella stessa giornata si è svolta in aula l'esercitazione guidata sulle omologie, sulla scheda OMOLOGIA_riepilogo che la docente aveva chiesto di stampare.

La registrazione copre solo la seconda parte della lezione: l'esercitazione e la prima parte (il riepilogo sulla perpendicolarità e la ricerca delle tracce di un piano date le proiezioni di una figura) qui sono ricostruite dalle schede della docente e dalle loro soluzioni.

## PERCHÉ SI RIBALTA UN PIANO

### La figura nel piano proiettante

Un piano proiettante in prima è perpendicolare a π₁: per questo tutti gli elementi geometrici che gli appartengono hanno la prima proiezione coincidente con la prima traccia t₁α.

Se sul piano si disegna una figura, per costruirne la prima proiezione non si deve fare altro che portarla sulla prima traccia: un triangolo ABC diventa tre punti A₁, B₁, C₁ allineati su t₁α.

La docente invita a verificarlo sul modello e a rassegnarsi: non può essere altrimenti, perché il piano è visto di taglio.

Nemmeno la seconda proiezione basta. Il triangolo A₂B₂C₂ disegnato su π₂ è più stretto di quello vero, perché il piano che lo contiene è inclinato rispetto a π₂.

Né la prima né la seconda proiezione, quindi, mostrano la vera grandezza e forma della figura: per vederla bisogna portare il piano a coincidere con un piano di proiezione.

### Il modellino con il piano mobile

Già nella lezione del 20 ottobre la docente aveva fatto preparare sul modellino un piano proiettante in prima mobile: un cartoncino grande, piegato (o tagliato) alla base in modo che potesse ruotare intorno alla sua prima traccia, che fa da cerniera.

Sul piano mobile si disegna un triangolo; finché il piano resta inclinato, la sua proiezione non ha le misure vere. Ruotando il cartoncino fino ad appoggiarlo su π₁, il triangolo compare nella sua vera forma.

Le rotazioni avvengono sempre intorno alle tracce, che sono le cerniere del piano.

Il modello va tenuto sempre aperto sul banco, a libretto: è lo strumento con cui si capisce che cosa succede nello spazio prima di disegnarlo sul foglio.

Il modellino della docente ha anche la doppia versione, con il piano che si abbatte su π₁ e quello che si chiude su π₂.

### La rotazione avviene lungo archi di circonferenza

Il principio da cui dipende tutto il ribaltamento è questo: durante la rotazione ogni punto del piano descrive un arco di circonferenza, e l'arco sta su un piano perpendicolare all'asse di rotazione, cioè alla traccia intorno a cui il piano ruota.

In gioco ci sono quindi due piani:

- quello che contiene la figura
- e quello che contiene l'arco, perpendicolare alla traccia.

Il centro dell'arco sta sulla traccia, e il raggio è la distanza del punto dalla traccia: per questo, quando il piano si è abbattuto, il punto ribaltato si trova sulla perpendicolare alla traccia condotta dalla sua proiezione.

Il punto ribaltato si indica con l'asterisco: A\* è il ribaltamento di A. Il ribaltamento fa conoscere la vera grandezza e forma della figura ribaltata sul piano di proiezione.

> [!example] Disegno 1 · Il disegno nello spazio: il piano proiettante in prima si abbatte su π₁
> ![[07-spazio-ribaltamento-su-pi1.svg|620]]
>
> 1. Il piano α è proiettante in prima (verticale). Il triangolo ABC sta su α e le sue prime proiezioni A₁, B₁, C₁ cadono tutte su t₁α.
> 2. Il piano ruota intorno a t₁α, come il cartoncino del modello, finché si appoggia su π₁.
> 3. Ogni vertice descrive un quarto di circonferenza (tratteggio rosso) su un piano perpendicolare a t₁α, con il centro sulla traccia.
> 4. Alla fine il triangolo A\*B\*C\* sta su π₁ con le sue misure vere.

> [!abstract] Da ricordare
> - L'asse di rotazione, la cerniera, è sempre una traccia del piano.
> - Ogni punto ruota lungo un arco di circonferenza che sta su un piano perpendicolare alla traccia, con il centro sulla traccia.
> - Il punto ribaltato si scrive con l'asterisco: A\*, B\*, C\*.
> - Il ribaltamento dà la vera grandezza e forma della figura.

## IL PIANO PROIETTANTE IN PRIMA

### Il ribaltamento su π₁ intorno alla prima traccia

Per ribaltare su π₁ un piano proiettante in prima la seconda traccia non serve: tutto avviene sul primo piano di proiezione.

Il modello, a questo punto, si dimentica: si immagina di avere sul foglio il piano con il suo punto, e ci si chiede dove sia la cerniera. La cerniera è la prima traccia t₁α.

Il punto A ha la prima proiezione A₁ su t₁α; quando il piano si abbatte, A ruota intorno alla traccia e arriva su π₁ lungo la perpendicolare a t₁α condotta da A₁.

Quanto si allontana dalla traccia? Esattamente quanto era alto, perché il raggio di rotazione è la distanza del punto dalla cerniera, cioè la sua quota. La quota si legge sul disegno come distanza della seconda proiezione A₂ dalla linea di terra.

Basta quindi riportare questa misura, con il compasso, sulla perpendicolare a t₁α a partire da A₁: si trova A\*.

Ripetendo per B e per C si ottiene il triangolo A\*B\*C\*, che è la vera grandezza e forma della figura, ribaltata sul primo piano di proiezione.

> [!example] Disegno 2 · Il disegno: il piano proiettante in prima ribaltato su π₁
> ![[07-ribaltamento-proiettante-in-prima-su-pi1.svg|620]]
>
> 1. Si disegnano le tracce di α: t₂α perpendicolare alla LT, t₁α inclinata. La seconda proiezione del triangolo, A₂B₂C₂, non è in vera grandezza; la prima proiezione si riduce a tre punti su t₁α.
> 2. La cerniera è t₁α: la seconda traccia non serve.
> 3. Da A₁ si traccia la perpendicolare a t₁α.
> 4. Si prende con il compasso la quota di A, cioè la distanza di A₂ dalla LT, e la si riporta sulla perpendicolare a partire da A₁: si trova A\*.
> 5. Si fa lo stesso per B e per C, segnando ogni volta i due segmenti uguali con lo stesso numero di lineette (una per A, due per B, tre per C).
> 6. Il triangolo A\*B\*C\* è il ribaltamento: la vera grandezza e forma della figura.

### Le lineette di uguaglianza

Ogni volta che si riporta una misura, i due segmenti uguali vanno segnati con una, due o tre lineette: due lineette sulla quota di un punto e due lineette sul segmento che la riporta, una lineetta per l'altro punto, e così via.

La docente insiste che questa cosa si deve fare sempre: negli esercizi, se l'uguaglianza non è segnata, lo considera un errore, perché non può prendere la squadretta e misurare ogni segmento su tanti esercizi per centoventi persone.

Chi disegna si deve mettere nella condizione di far capire quello che ha fatto.

### Il ribaltamento su π₂: la porta

Lo stesso piano si può ribaltare anche su π₂.

Invece di abbatterlo facendolo ruotare intorno alla prima traccia, lo si chiude come se fosse una porta, facendo cerniera sulla seconda traccia t₂α, che è verticale.

Nella rotazione ogni punto ha il suo raggio di rotazione, che va dal punto alla cerniera, e l'asse di rotazione è la seconda traccia.

In questa rotazione la quota del punto non cambia: quando si apre una porta, la maniglia non si abbassa, resta alla stessa altezza, e il suo raggio di rotazione va dalla maniglia alla cerniera. Allo stesso modo, se si chiude il piano su π₂, ogni punto resta alla sua quota.

Il piano si può girare su π₂ in una direzione o nell'altra:

- in una direzione la figura ribaltata si sovrappone alla seconda proiezione già disegnata;
- nell'altra la si vede, per così dire, sul retro.

Alla lavagna la docente ha portato il ribaltamento dall'altra parte, per non sovrapporlo al disegno della seconda proiezione; sul libro si trova invece il ribaltamento dall'altro lato, con la sovrapposizione, ma il risultato è lo stesso.

Secondo la docente questo ribaltamento è proprio il più facile.

> [!example] Disegno 3 · Il disegno nello spazio: il piano si chiude su π₂ come una porta
> ![[07-spazio-ribaltamento-su-pi2.svg|620]]
>
> 1. La cerniera è la seconda traccia t₂α, verticale.
> 2. Ogni punto del triangolo descrive un arco orizzontale con il centro su t₂α, come la maniglia: resta sempre alla sua quota.
> 3. Il piano è chiuso dalla parte opposta a quella in cui sta la figura, così il ribaltamento non si sovrappone alla seconda proiezione.

> [!example] Disegno 4 · Il disegno: il piano proiettante in prima ribaltato su π₂
> ![[07-ribaltamento-proiettante-in-prima-su-pi2.svg|620]]
>
> 1. Stesso piano α e stesso triangolo. La cerniera è t₂α; K è il punto in cui t₂α incontra la LT.
> 2. Centro del compasso in K, raggio KA₁: l'arco porta A₁ sulla LT, dalla parte opposta rispetto alla figura.
> 3. Da quel punto si sale con una linea di richiamo fino alla quota di A, cioè fino all'altezza di A₂ (la quota non cambia): lì c'è A\*.
> 4. Si fa lo stesso per B e per C.
> 5. Il triangolo A\*B\*C\* è in vera grandezza ed è uguale a quello ribaltato su π₁.

### Due ribaltamenti, una sola figura

I modi per ribaltare un piano proiettante sono quindi due:

- intorno alla prima traccia, su π₁,
- oppure intorno alla seconda traccia, su π₂.

Se si fanno tutti e due con riga e squadra, si deve riscontrare che la figura ribaltata è identica.

Nel modello della docente ci sono i due casi, a e b, con tutti i dati di rotazione: come ruota il piano che contiene la figura in un verso e nell'altro, sul piano π₁ e sul piano π₂.

> [!abstract] Da ricordare: il piano proiettante in prima
> - Su π₁: cerniera t₁α; A\* sta sulla perpendicolare a t₁α per A₁, a una distanza uguale alla quota di A.
> - Su π₂: cerniera t₂α; la quota non cambia (la maniglia della porta); A\* sta alla stessa altezza di A₂.
> - I due ribaltamenti danno la stessa figura.
> - Le misure riportate si segnano sempre con le lineette.

## IL PIANO PROIETTANTE IN SECONDA

### La figura nel piano proiettante in seconda

Il piano proiettante in seconda è perpendicolare a π₂ ed è inclinato rispetto a π₁ e a π₃. La sua caratteristica è che la seconda proiezione di tutti gli elementi che stanno sul piano coincide con la seconda traccia t₂α.

Se sul piano si disegna un triangolo, quella che si vede come figura è la prima proiezione, mentre la seconda si riduce a una linea. Anche qui la prima proiezione non è in vera grandezza, e per conoscere la figura bisogna ribaltare il piano.

Valgono le stesse due possibilità del proiettante in prima: si può ribaltare su π₁ o su π₂.

### Il ribaltamento su π₁ intorno alla prima traccia

Per ribaltare su π₁ si fa ruotare il piano intorno alla prima traccia. Questo significa che A₂, B₂, C₂ compiono tutti degli archi di circonferenza, con il centro nel punto in cui la traccia incontra la linea di terra, perché l'asse di rotazione è una traccia.

Che cosa non cambia, in questo caso? Nel proiettante in prima non cambiava la quota dei punti. Con il piano messo così, invece, quello che non cambia è la distanza del punto dal piano π₂, cioè l'aggetto: si fa un'equivalenza, si mette una cosa uguale a un'altra.

1. Si punta quindi il compasso,
2. si costruiscono gli archi che portano A₂, B₂, C₂ sulla linea di terra,
3. e da lì si riporta la stessa, medesima distanza dalla linea di terra che hanno A₁, B₁, C₁.

Si trovano così A\*, B\*, C\*, il ribaltamento della figura sul primo piano di proiezione.

> [!example] Disegno 5 (proposto, non fatto a lezione): il proiettante in seconda nello spazio
> ![[b07-spazio-proiettante-in-seconda-su-pi1.svg|620]]
>
> 1. Il piano α è perpendicolare a π₂: t₁α è perpendicolare alla LT, t₂α è inclinata. Le seconde proiezioni A₂, B₂, C₂ cadono tutte su t₂α.
> 2. Il piano si abbatte su π₁ ruotando intorno a t₁α.
> 3. Gli archi stanno su piani perpendicolari a t₁α, cioè paralleli a π₂: durante la rotazione la distanza di ogni punto da π₂, l'aggetto, non cambia.
> 4. Il triangolo A\*B\*C\* arriva su π₁ con le sue misure vere.

> [!example] Disegno 6 · Il disegno: il piano proiettante in seconda ribaltato su π₁
> ![[07-ribaltamento-proiettante-in-seconda-su-pi1.svg|620]]
>
> 1. Si disegnano le tracce di α: t₁α perpendicolare alla LT, t₂α inclinata. A₂, B₂, C₂ stanno su t₂α; la prima proiezione A₁B₁C₁ non è in vera grandezza.
> 2. La cerniera è t₁α; K è il punto in cui incontra la LT.
> 3. Centro del compasso in K, raggio KA₂: l'arco porta A₂ sulla LT.
> 4. Da lì si scende con una linea di richiamo fino alla stessa distanza dalla LT di A₁ (l'aggetto non cambia): lì c'è A\*.
> 5. Si fa lo stesso per B e per C. Il triangolo A\*B\*C\* è la vera grandezza e forma; in questo disegno si sovrappone in parte alla prima proiezione.

### Il ribaltamento su π₂ intorno alla seconda traccia

Se invece si vuole ribaltare su π₂, si fa ruotare il piano intorno alla seconda traccia. Anche in questo caso ci sono i piani perpendicolari all'asse, quelli su cui avviene la rotazione, e ogni punto ribaltato si trova sulla perpendicolare a t₂α condotta dalla sua seconda proiezione, a una distanza uguale al suo aggetto. Collocati i tre punti, si ottiene la figura.

I due ribaltamenti devono risultare uguali, perché sono i ribaltamenti della stessa figura.

Il ribaltamento non può produrre un'altra figura: la figura è una sola, e quelle che si disegnano sono altre sue proiezioni.

> [!example] Disegno 7 · Il disegno: il piano proiettante in seconda ribaltato su π₂
> ![[07-ribaltamento-proiettante-in-seconda-su-pi2.svg|620]]
>
> 1. Stesso piano α e stesso triangolo; ora la cerniera è t₂α.
> 2. Da A₂ si traccia la perpendicolare a t₂α.
> 3. Si prende con il compasso l'aggetto di A, cioè la distanza di A₁ dalla LT, e lo si riporta sulla perpendicolare a partire da A₂: si trova A\*.
> 4. Si fa lo stesso per B e per C, segnando i segmenti uguali con le lineette.
> 5. Il triangolo A\*B\*C\* è uguale a quello ribaltato su π₁: la figura è una sola, cambia solo il piano su cui la si ribalta.

> [!abstract] Da ricordare: i quattro ribaltamenti dei piani proiettanti
> - Proiettante in prima su π₁: cerniera t₁α, si riporta la quota sulla perpendicolare a t₁α.
> - Proiettante in prima su π₂: cerniera t₂α, la quota non cambia.
> - Proiettante in seconda su π₁: cerniera t₁α, l'aggetto non cambia.
> - Proiettante in seconda su π₂: cerniera t₂α, si riporta l'aggetto sulla perpendicolare a t₂α.
> - In tutti i casi la figura ribaltata è la stessa, in vera grandezza.

## L'OMOLOGIA DI RIBALTAMENTO

### Ruotare equivale a proiettare

Tra la prima proiezione di una figura e il suo ribaltamento si crea una relazione omologica.

Il motivo è che far compiere a un punto la rotazione equivale a proiettare il punto nella direzione perpendicolare al piano bisettore tra i due piani che si stanno considerando: il piano bisettore è il piano che sta in mezzo e seca a metà l'angolo formato da α con π₁.

Guardando la rotazione in sezione, su un piano perpendicolare alla traccia, si vede che il segmento che unisce A al suo ribaltamento A\* è perpendicolare al piano bisettore: ruotare il punto o proiettarlo in quella direzione porta allo stesso risultato.

Si crea quindi un'affinità, perché il centro di proiezione è all'infinito.

Valgono le proprietà dell'omologia:

- i punti corrispondenti sono allineati con il centro, che è all'infinito nella direzione perpendicolare all'asse;
- le rette corrispondenti si incontrano sull'asse, che è la traccia intorno a cui il piano ruota.

È l'omologia di ribaltamento.

La docente avverte che nei piani proiettanti c'è una coincidenza: la prima proiezione della figura non è una figura ma una linea, mentre il ribaltamento è una figura.

Per questo l'affinità si vedrà meglio nel ribaltamento del piano generico; l'ha introdotta adesso, pur trattandosi di cose della parte sulla geometria proiettiva, per legarla al ribaltamento del piano proiettante.

> [!example] Disegno 8 · Il disegno: la sezione e il piano bisettore
> ![[07-sezione-piano-bisettore.svg|480]]
>
> 1. Si guarda la rotazione in sezione, su un piano perpendicolare a t₁α: la traccia si vede come un punto, α come una linea verticale, π₁ come una linea orizzontale.
> 2. Il punto A ruota intorno alla traccia lungo un quarto di circonferenza e arriva in A\*, su π₁, alla stessa distanza dalla traccia (una lineetta).
> 3. Il piano bisettore divide a metà l'angolo tra α e π₁. Il segmento AA\* è perpendicolare al piano bisettore: ruotare il punto è come proiettarlo in quella direzione.
> 4. Per questo tra la prima proiezione e la figura ribaltata c'è un'affinità: l'asse è la traccia-cerniera e il centro è all'infinito, nella direzione perpendicolare all'asse.

### Rette corrispondenti sull'asse

La proprietà delle rette corrispondenti si può già controllare sul disegno del proiettante in prima.

Una retta r del piano, per esempio quella del lato AC, incontra la cerniera nella sua prima traccia T₁r, il punto della retta che ha quota zero. Durante la rotazione T₁r non si muove, perché sta sull'asse: è un punto unito.

Per questo la retta ribaltata r\* = A\*C\* deve passare per T₁r, e i punti corrispondenti stanno sulle perpendicolari alla cerniera, cioè sono allineati con il centro all'infinito.

> [!example] Disegno 9 (proposto, non fatto a lezione): verifica con il punto unito sulla cerniera
> ![[b07-punto-unito-sulla-cerniera.svg|620]]
>
> 1. Si parte dal ribaltamento su π₁ del piano proiettante in prima, già costruito.
> 2. Si prolunga r₂ = A₂C₂ fino alla LT e si scende con una linea di richiamo fino a t₁α: lì c'è la prima traccia T₁r della retta AC.
> 3. Si prolunga il lato ribaltato A\*C\*: deve passare per T₁r. Se non ci passa, c'è un errore nelle misure riportate.
> 4. I segmenti A₁A\* e C₁C\* sono perpendicolari a t₁α: è la direzione del centro all'infinito dell'affinità.

> [!abstract] Da ricordare: l'omologia di ribaltamento
> - Ruotare un punto equivale a proiettarlo perpendicolarmente al piano bisettore tra il piano e il piano di proiezione.
> - Tra la proiezione e il ribaltamento c'è un'affinità: l'asse è la traccia-cerniera, il centro è all'infinito nella direzione perpendicolare all'asse.
> - Punti corrispondenti allineati con il centro; rette corrispondenti che si incontrano sull'asse.

## ESERCIZI

### L'esercitazione guidata sulle omologie

La scheda OMOLOGIA_riepilogo, da stampare e portare in aula, raccoglie sei esercizi che ripassano tutte le omologie viste nella lezione del 6 ottobre.

La registrazione non copre l'esercitazione: lo svolgimento qui sotto segue la soluzione della docente (OMOLOGIA_riepilogo_soluzione).

Nella scheda il centro si chiama U e l'asse u; quando sono all'infinito si scrivono U∞ (indicato con un trattino nella sua direzione) e u∞ (indicato con una crocetta). Gli esercizi si risolvono sempre con le due proprietà dell'omologia:

- i punti corrispondenti sono allineati con il centro
- e le rette corrispondenti si incontrano sull'asse.

* Quando l'asse è all'infinito, le rette corrispondenti si incontrano all'infinito, cioè sono parallele;
* quando il centro è all'infinito, i punti corrispondenti stanno su rette parallele alla direzione del centro.

Se si hanno i punti, si cercano le rette; se si hanno le rette, si cercano i punti.

> [!example] Disegno 10 · Esercizio 1: dati U∞, u∞, una coppia di rette corrispondenti r e r′ e il punto P, trovare P′
> ![[b07-omologia-es1.svg|520]]
>
> Centro e asse sono entrambi all'infinito: è una traslazione.
> 1. Per P si traccia una retta qualsiasi, che incontra r nel punto M.
> 2. Da M si traccia la parallela alla direzione di U∞: dove incontra r′ c'è M′, il corrispondente di M.
> 3. La retta PM ha come corrispondente la retta per M′ parallela a PM, perché l'asse è all'infinito.
> 4. Da P si traccia la parallela alla direzione di U∞: dove incontra la retta del passo 3 c'è P′.
> 5. PMM′P′ risulta un parallelogramma: la figura si sposta uguale.

> [!example] Disegno 11 · Esercizio 2: dati U, u∞, una coppia di rette corrispondenti r e r′ e la retta n, trovare n′
> ![[b07-omologia-es2.svg|560]]
>
> Il centro è proprio e l'asse è all'infinito: è un'omotetia.
> 1. n incontra r nel punto B. Il corrispondente B′ sta sulla retta UB (punti allineati con il centro) e su r′.
> 2. Serve un secondo punto di n′. Si prende M su n e si traccia UM.
> 3. Si usa una retta ausiliaria t, che unisce M al punto A di r. Il corrispondente A′ sta su UA e su r′.
> 4. La retta t′ corrispondente di t passa per A′ ed è parallela a t, perché l'asse è all'infinito. Dove t′ incontra UM c'è M′.
> 5. n′ è la retta B′M′, e risulta parallela a n. Sulla scheda la docente annota: «Il punto A è stato usato come verifica».

> [!example] Disegno 12 · Esercizio 3: dati U, u, la figura ABC e una coppia di punti corrispondenti A e A′, trovare A′B′C′
> ![[b07-omologia-es3.svg|620]]
>
> Il centro sta sull'asse: è un'omologia speciale, che si risolve allo stesso modo.
> 1. Si prolunga il lato CA (la retta r) fino all'asse: il punto d'incontro è unito, corrisponde a se stesso.
> 2. La retta r′ unisce quel punto ad A′. C′ sta su r′ e sulla retta UC.
> 3. Si prolunga il lato AB fino all'asse; la retta che unisce quel punto ad A′ incontra UB in B′.
> 4. Verifica: il lato CB e il lato C′B′, prolungati, devono incontrarsi sull'asse.

> [!example] Disegno 13 · Esercizio 4: dati U, u∞, una coppia di rette corrispondenti r e r′ e un punto P, trovare P′
> ![[b07-omologia-es4.svg|420]]
>
> Ancora un'omotetia: centro proprio, asse all'infinito.
> 1. Da U si traccia una retta che incontra r in A e r′ in A′: A e A′ sono corrispondenti.
> 2. Si unisce P con A.
> 3. Per A′ si traccia la parallela a PA (l'asse è all'infinito, quindi le rette corrispondenti sono parallele).
> 4. P′ sta su questa parallela e sulla retta UP.

> [!example] Disegno 14 · Esercizio 5: dati U∞, u, la figura ABC e una coppia di punti corrispondenti A e A′, trovare A′B′C′
> ![[b07-omologia-es5.svg|520]]
>
> Il centro è all'infinito e l'asse è proprio: è un'affinità. La direzione del centro è quella di AA′.
> 1. Si prolunga AC fino all'asse u; la retta che unisce quel punto ad A′ è la corrispondente di AC.
> 2. Per C si traccia la parallela ad AA′: dove incontra la retta del passo 1 c'è C′.
> 3. Si prolunga CB fino all'asse; la retta che unisce quel punto a C′ è la corrispondente di CB.
> 4. Per B si traccia la parallela ad AA′: dove incontra la retta del passo 3 c'è B′.
> 5. Il triangolo A′B′C′ è il corrispondente di ABC.

> [!example] Disegno 15 · Esercizio 6: dati U∞, u, una coppia di rette corrispondenti r e r′ e la retta m, trovare m′
> ![[b07-omologia-es6.svg|600]]
>
> Ancora un'affinità: centro all'infinito, asse proprio.
> 1. m incontra l'asse in un punto unito: m′ passa per quel punto.
> 2. Serve un secondo punto. Si prendono A su r e B su m e si traccia la retta ausiliaria n = AB, prolungata fino all'asse.
> 3. A′ sta su r′ e sulla parallela alla direzione di U∞ condotta da A.
> 4. La retta n′ corrispondente di n unisce A′ al punto in cui n incontra l'asse.
> 5. B′ sta su n′ e sulla parallela alla direzione di U∞ condotta da B.
> 6. m′ unisce il punto unito sull'asse con B′.

### Un punto sulla retta di profilo, con il ribaltamento

Il ribaltamento torna utile anche in un esercizio della scheda PO_riepilogo_1: disegnare un punto P che appartenga a una retta r di profilo.

La retta di profilo ha le due proiezioni sovrapposte sulla stessa linea perpendicolare alla LT (r₂ ≡ r₁), che coincide anche con le tracce del piano di profilo che la contiene (t₂α ≡ t₁α): dalla sola seconda proiezione di un punto non si capisce dove stia la prima.

Nella soluzione la docente ribalta il piano di profilo su π₂, facendolo ruotare intorno alla sua seconda traccia: la quota dei punti resta la stessa, mentre l'aggetto diventa la distanza dalla cerniera. Così la retta compare in vera forma come r\*, si sceglie su di essa P\* e si torna indietro alle proiezioni.

Nella bozza [[04-rette-e-piani-nelle-varie-posizioni]] lo stesso problema è risolto con la terza proiezione.

> [!example] Disegno 16 · Il disegno: un punto P sulla retta r di profilo (scheda PO_riepilogo_1, soluzione della docente)
> ![[b07-punto-sulla-retta-di-profilo.svg|520]]
>
> 1. Sono date le tracce T₂r (sopra la LT) e T₁r (sotto la LT) sulla linea verticale r₂ ≡ r₁.
> 2. Si ribalta il piano di profilo su π₂ intorno a t₂α: centro del compasso nel punto in cui la verticale incontra la LT, raggio fino a T₁r; l'arco porta T₁r sulla LT, a sinistra.
> 3. La retta che unisce il punto ribaltato a T₂r è r\*, la retta ribaltata.
> 4. Si sceglie P\* su r\*.
> 5. Da P\* si va in orizzontale fino alla verticale: è P₂, perché la quota non cambia.
> 6. Da P\* si scende fino alla LT e con il compasso si riporta la distanza dalla verticale sotto la LT: è P₁, perché la distanza dalla cerniera era l'aggetto.

> [!tip] Avvisi e consegne
> - Tenere il modello sempre aperto sul banco; il modellino della docente si può vedere da vicino.
> - Negli esercizi segnare sempre i segmenti uguali con una, due o tre lineette: senza, la docente lo considera un errore.
> - Ripassare il disegno delle rette e dei piani: la prossima volta si fa il ribaltamento del piano generico, che è un po' più complesso ma riprende tutto questo.
> - Il calendario delle attività fissa a giovedì 29 ottobre la prova n. 1 di geometria descrittiva.

## Collegamenti

Il ribaltamento mette insieme quasi tutto quello che si è visto finora.

Si fonda sui piani proiettanti e sulle loro tracce, studiati in [[04-rette-e-piani-nelle-varie-posizioni]] e nella sbobina [[04-rette-e-piani-metodo-di-monge]], e sulla lettura di quota e aggetto di un punto, che risale alle [[03-proiettiva-e-proiezioni-ortogonali|proiezioni ortogonali del punto]] e alla bozza [[03-proiezioni-ortogonali-punto-e-rette]].

Il modellino con il piano mobile era stato preparato alla fine della lezione del 20 ottobre ([[06-piani-proiettanti-orizzontali-frontali]]), la stessa in cui la docente aveva raccomandato di riguardare la perpendicolarità tra retta e piano con l'orizzontale e la frontale ([[06-piani-ausiliari-e-perpendicolarita]]), perché servirà nel ribaltamento del piano generico, il prossimo argomento.

L'omologia di ribaltamento riporta invece alla geometria proiettiva della [[02-proiezioni-e-omologia|seconda lezione]] e al suo [[02-proiezioni-e-omologia-schema|schema]]: l'affinità, con il centro all'infinito, è la stessa che si ripassa negli esercizi della scheda OMOLOGIA_riepilogo, e il punto unito sulla cerniera è un caso della regola per cui le rette corrispondenti si incontrano sull'asse.

Infine, il ribaltamento della retta di profilo mostra che la stessa tecnica risolve problemi di appartenenza come quelli di [[05-appartenenza-e-rette-ausiliarie]].

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[ARGOMENTI LEZIONI 26-27.pdf]]: elenco degli argomenti della lezione
- [[OMOLOGIA_riepilogo.pdf]]: la scheda da stampare per l'esercitazione
- [[OMOLOGIA_riepilogo_soluzione.pdf]]: soluzioni della docente
- [[PO_riepilogo_1.pdf]]: esercizio sulla retta di profilo
- [[PO_riepilogo_1_soluzione.pdf]]: soluzione della docente
- [[Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: data della Prova n. 1
