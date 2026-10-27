---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-20
tags: [geometria-descrittiva, appunti, teoria]
---

# PO 8 - Il ribaltamento

> [!info] Note collegate
> Precedente: [[PO 7 - Figure piane e solidi]] · Successiva: —
>
> Esercizi: [[esercitazioni|Esercitazioni]] · Teoria collegata: [[teoria-omologia]]
>
> Bozze delle lezioni: [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]]

Capitolo 8 di 8 della teoria delle proiezioni ortogonali. Lezioni: 20 e 22 ottobre.

## 8.1 Perché si ribalta un piano (22 ottobre)

Quando una figura sta su un piano proiettante, le sue proiezioni non dicono quanto è grande davvero.

Nel piano proiettante in prima, per esempio, un triangolo ABC diventa in prima proiezione tre punti A₁, B₁, C₁ allineati su t₁α: non può essere altrimenti, perché il piano è visto di taglio. Nemmeno la seconda proiezione basta: il triangolo A₂B₂C₂ è più stretto di quello vero, perché il piano che lo contiene è inclinato rispetto a π₂.

Il ribaltamento è l'operazione con cui si fa ruotare il piano che contiene la figura intorno a una delle sue tracce, finché non si appoggia su un piano di proiezione. Il ribaltamento fa conoscere la vera grandezza e forma della figura.

## 8.2 Il piano mobile e la cerniera (20 e 22 ottobre)

Nel modello il ribaltamento si vede con un piano proiettante in prima mobile: un cartoncino grande, piegato o tagliato alla base, che resta in piedi ma può ruotare intorno alla sua prima traccia.

Finché il piano è inclinato rispetto a π₁, la proiezione del triangolo disegnato sul cartoncino non ha la sua vera grandezza: le lunghezze dei lati e gli angoli non sono quelli veri. Ruotando il cartoncino intorno alla prima traccia fino a farlo coincidere con π₁, la figura appare vera.

Le rotazioni avvengono sempre intorno alle tracce. La traccia intorno a cui il piano ruota si chiama cerniera, ed è l'asse di rotazione.

> [!example] Disegno 51 · Il piano mobile
> ![[06-spazio-piano-mobile.svg|600]]
>
> Il piano γ è proiettante in prima e il triangolo ABC ha la prima proiezione su t₁γ.
> Il piano ruota intorno a t₁γ, che fa da cerniera, fino a stendersi su π₁: il triangolo (A)(B)(C) è in vera forma.

## 8.3 La rotazione avviene lungo archi di circonferenza (20 e 22 ottobre)

Durante la rotazione ogni punto del piano descrive un arco di circonferenza, e l'arco sta su un piano perpendicolare all'asse di rotazione, cioè alla traccia. È come la spirale del quaderno che, bloccata, lascia ai fogli un solo movimento possibile.

In gioco ci sono quindi due piani:

- quello che contiene la figura;
- quello che contiene l'arco, perpendicolare alla traccia.

Il centro dell'arco sta sulla traccia, e il raggio è la distanza del punto dalla traccia. Durante la rotazione questa distanza non va perduta, e quando il piano si è abbattuto il punto ribaltato si trova sulla perpendicolare alla traccia condotta dalla sua proiezione.

Il punto ribaltato si indica con l'asterisco: A\* è il ribaltamento di A.

> [!example] Disegno 52 · La rotazione nello spazio
> ![[07-spazio-ribaltamento-su-pi1.svg|620]]
>
> Il piano α, proiettante in prima, ruota intorno a t₁α finché si appoggia su π₁.
> Ogni vertice descrive un quarto di circonferenza (tratteggio rosso) su un piano perpendicolare a t₁α, con il centro sulla traccia; alla fine A\*B\*C\* sta su π₁ con le sue misure vere.

## 8.4 Il ribaltamento del piano proiettante in prima (22 ottobre)

### 8.4.1 Su π₁, intorno alla prima traccia (22 ottobre)

Per ribaltare su π₁ un piano proiettante in prima la seconda traccia non serve: tutto avviene sul primo piano di proiezione, e la cerniera è la prima traccia t₁α.

Il punto A ha la prima proiezione A₁ su t₁α. Quando il piano si abbatte, A arriva su π₁ lungo la perpendicolare a t₁α condotta da A₁.

Si allontana dalla traccia esattamente quanto era alto, perché il raggio di rotazione è la distanza del punto dalla cerniera, cioè la sua quota. La quota si legge sul disegno come distanza di A₂ dalla linea di terra, e si riporta con il compasso sulla perpendicolare a partire da A₁: lì c'è A\*.

> [!example] Disegno 53 · Il proiettante in prima ribaltato su π₁
> ![[07-ribaltamento-proiettante-in-prima-su-pi1.svg|620]]
>
> Da A₁ si traccia la perpendicolare a t₁α e vi si riporta la quota di A, cioè la distanza di A₂ dalla LT: si trova A\*.
> Si fa lo stesso per B e per C, segnando i segmenti uguali con le lineette; A\*B\*C\* è la vera grandezza e forma.

### 8.4.2 Su π₂, intorno alla seconda traccia (22 ottobre)

Lo stesso piano si può ribaltare su π₂. Invece di abbatterlo intorno alla prima traccia, lo si chiude come una porta, facendo cerniera sulla seconda traccia t₂α, che è verticale.

In questa rotazione la quota del punto non cambia. Quando si apre una porta, la maniglia non si abbassa: resta alla stessa altezza, e il suo raggio di rotazione va dalla maniglia alla cerniera.

Il piano si può girare su π₂ in una direzione o nell'altra:

- in una direzione la figura ribaltata si sovrappone alla seconda proiezione già disegnata;
- nell'altra la si vede, per così dire, sul retro.

Il risultato è lo stesso. Questo ribaltamento è il più facile.

> [!example] Disegno 54 · Il proiettante in prima ribaltato su π₂
> ![[07-spazio-ribaltamento-su-pi2.svg|620]]
>
> Nello spazio: ogni punto descrive un arco orizzontale con il centro su t₂α, come la maniglia, e resta alla sua quota.
>
> ![[07-ribaltamento-proiettante-in-prima-su-pi2.svg|620]]
>
> Sul foglio: con il centro in K, dove t₂α incontra la LT, l'arco di raggio KA₁ porta A₁ sulla LT; da lì si sale fino all'altezza di A₂ e si trova A\*.

## 8.5 Il ribaltamento del piano proiettante in seconda (22 ottobre)

Nel piano proiettante in seconda la seconda proiezione della figura si riduce a una linea su t₂α, e la prima proiezione non è in vera grandezza. Valgono le stesse due possibilità: si può ribaltare su π₁ o su π₂.

### 8.5.1 Su π₁, intorno alla prima traccia (22 ottobre)

Per ribaltare su π₁ si fa ruotare il piano intorno alla prima traccia. A₂, B₂, C₂ compiono degli archi di circonferenza con il centro nel punto in cui la traccia incontra la linea di terra, perché l'asse di rotazione è una traccia.

Nel proiettante in prima non cambiava la quota dei punti. Con il piano messo così, invece, non cambia la distanza del punto da π₂, cioè l'aggetto.

1. Si punta il compasso nel punto in cui t₁α incontra la LT.
2. Si costruiscono gli archi che portano A₂, B₂, C₂ sulla linea di terra.
3. Da lì si riporta la stessa distanza dalla linea di terra che hanno A₁, B₁, C₁.

Si trovano così A\*, B\*, C\*.

> [!example] Disegno 55 · Il proiettante in seconda ribaltato su π₁
> ![[b07-spazio-proiettante-in-seconda-su-pi1.svg|620]]
>
> Nello spazio (schema proposto, non disegnato a lezione): gli archi stanno su piani perpendicolari a t₁α, cioè paralleli a π₂, quindi l'aggetto non cambia.
>
> ![[07-ribaltamento-proiettante-in-seconda-su-pi1.svg|620]]
>
> Sul foglio: con il centro in K l'arco di raggio KA₂ porta A₂ sulla LT; da lì si scende fino alla distanza di A₁ dalla LT e si trova A\*.

### 8.5.2 Su π₂, intorno alla seconda traccia (22 ottobre)

Per ribaltare su π₂ si fa ruotare il piano intorno alla seconda traccia. Anche qui la rotazione avviene su piani perpendicolari all'asse: ogni punto ribaltato si trova sulla perpendicolare a t₂α condotta dalla sua seconda proiezione, a una distanza uguale al suo aggetto.

> [!example] Disegno 56 · Il proiettante in seconda ribaltato su π₂
> ![[07-ribaltamento-proiettante-in-seconda-su-pi2.svg|620]]
>
> Da A₂ si traccia la perpendicolare a t₂α e vi si riporta l'aggetto di A, cioè la distanza di A₁ dalla LT: si trova A\*.
> Il triangolo A\*B\*C\* è uguale a quello ribaltato su π₁.

## 8.6 Una sola figura e le lineette di uguaglianza (22 ottobre)

I modi per ribaltare un piano proiettante sono due, intorno alla prima traccia o intorno alla seconda. Riassumendo:

- proiettante in prima su π₁: cerniera t₁α, si riporta la quota sulla perpendicolare a t₁α;
- proiettante in prima su π₂: cerniera t₂α, la quota non cambia;
- proiettante in seconda su π₁: cerniera t₁α, l'aggetto non cambia;
- proiettante in seconda su π₂: cerniera t₂α, si riporta l'aggetto sulla perpendicolare a t₂α.

I due ribaltamenti della stessa figura devono risultare identici. Il ribaltamento non può produrre un'altra figura: la figura è una sola, e quelle che si disegnano sono altre sue proiezioni.

Ogni volta che si riporta una misura, i due segmenti uguali si segnano con lo stesso numero di lineette: una per il primo punto, due per il secondo, tre per il terzo. Va fatto sempre, perché chi disegna deve far capire quello che ha fatto.

## 8.7 L'omologia di ribaltamento (22 ottobre)

### 8.7.1 Ruotare equivale a proiettare (22 ottobre)

Tra la prima proiezione di una figura e il suo ribaltamento si crea una relazione omologica, l'omologia di ribaltamento.

Far compiere a un punto la rotazione equivale a proiettare il punto nella direzione perpendicolare al piano bisettore tra i due piani che si stanno considerando. Il piano bisettore è il piano che sta in mezzo e seca a metà l'angolo formato da α con π₁.

Il centro di proiezione è quindi all'infinito, e si crea un'affinità ortogonale:

- l'asse è la traccia intorno a cui il piano ruota, la cerniera;
- il centro è all'infinito, nella direzione perpendicolare all'asse;
- i punti corrispondenti sono allineati con il centro;
- le rette corrispondenti si incontrano sull'asse.

Nei piani proiettanti c'è una coincidenza: la prima proiezione della figura non è una figura ma una linea, mentre il ribaltamento è una figura. Per questo l'affinità si vedrà meglio nel ribaltamento del piano generico.

> [!example] Disegno 57 · La rotazione in sezione e il piano bisettore
> ![[07-sezione-piano-bisettore.svg|480]]
>
> In sezione, su un piano perpendicolare a t₁α, la traccia è un punto, α una linea verticale e π₁ una linea orizzontale.
> A ruota lungo un quarto di circonferenza fino ad A\*; il segmento AA\* è perpendicolare al piano bisettore, quindi ruotare il punto è come proiettarlo in quella direzione.

### 8.7.2 Il punto unito sulla cerniera (22 ottobre)

La proprietà delle rette corrispondenti si può controllare sul ribaltamento del proiettante in prima.

Una retta del piano, per esempio quella del lato AC, incontra la cerniera nella sua prima traccia, il punto della retta che ha quota zero. Durante la rotazione quel punto non si muove, perché sta sull'asse: è un punto unito.

Per questo la retta ribaltata A\*C\* deve passare per la prima traccia della retta, e i punti corrispondenti stanno sulle perpendicolari alla cerniera, cioè sono allineati con il centro all'infinito.

> [!example] Disegno 58 · Il punto unito sulla cerniera
> ![[b07-punto-unito-sulla-cerniera.svg|620]]
>
> Schema proposto, non disegnato a lezione.
> Si prolunga A₂C₂ fino alla LT e si scende fino a t₁α: lì c'è la prima traccia della retta AC. Il lato ribaltato A\*C\*, prolungato, deve passare per quel punto.
> I segmenti A₁A\* e C₁C\* sono perpendicolari a t₁α: è la direzione del centro all'infinito.

---

## Collegamenti

Il metodo di Monge nasce dalla geometria proiettiva: le proiezioni ortogonali sono il caso con il centro all'infinito, e le regole dell'omologia raccolte in [[teoria-omologia]] tornano nell'omologia di ribaltamento e nella vera grandezza delle figure nel piano frontale.

Il percorso lezione per lezione, con gli esercizi, si trova nelle bozze: il punto e le rette proiettanti in [[03-proiezioni-ortogonali-punto-e-rette]], le rette e i piani particolari in [[04-rette-e-piani-nelle-varie-posizioni]], l'appartenenza in [[05-appartenenza-e-rette-ausiliarie]], i piani ausiliari e la perpendicolarità in [[06-piani-ausiliari-e-perpendicolarita]], il ribaltamento dei piani proiettanti in [[07-il-ribaltamento]].

Il prossimo passo è il ribaltamento del piano generico, che riprende le orizzontali, le frontali e il piano perpendicolare al piano dato. Il triangolo delle tracce tornerà nell'assonometria, le rette con le tracce dall'altra parte nelle ombre, e pianta, prospetti e scale sono gli stessi strumenti del laboratorio di Composizione architettonica.
