---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-08
tags: [geometria-descrittiva, appunti, teoria]
---

# PO 3 - La retta

> [!info] Note collegate
> Precedente: [[PO 2 - Il punto]] · Successiva: [[PO 4 - Il piano]]
>
> Esercizi: [[esercitazioni|Esercitazioni]] · Teoria collegata: [[teoria-omologia]]
>
> Bozze delle lezioni: [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]]

Capitolo 3 di 8 della teoria delle proiezioni ortogonali. Lezioni: 8-20 ottobre.

## 3.1 Il nome, le tracce e le proiezioni (8, 13 e 15 ottobre)

### 3.1.1 Il nome della retta (8 e 13 ottobre)

Il nome di una retta si assegna in base alla posizione che assume rispetto ai primi due piani di proiezione, π₁ orizzontale e π₂ verticale.

Una retta perpendicolare a π₃, per esempio, è anche proiettante in terza, ma si chiama parallela alla linea di terra, perché è parallela a π₁ e a π₂.

In pratica, per dare il nome a una retta ci si fanno due domande: com'è rispetto a π₁ (il pavimento)? E com'è rispetto a π₂ (la parete di fronte)? Le risposte possibili sono «perpendicolare», «parallela» o «inclinata», e ogni combinazione ha il suo nome:

- perpendicolare a π₁ (in piedi, come un palo): retta proiettante in prima;<br>![[b04-retta-stanza-1.svg|230]]
- perpendicolare a π₂ (che esce dalla parete verso di te): retta proiettante in seconda;<br>![[b04-retta-stanza-2.svg|230]]
- parallela a π₁ e parallela a π₂ (orizzontale e parallela alla parete): retta parallela alla linea di terra;<br>![[b04-retta-stanza-3.svg|230]]
- parallela a π₂ e inclinata rispetto a π₁ (appoggiata alla parete, come una scala a pioli): retta frontale;<br>![[b04-retta-stanza-4.svg|230]]
- parallela a π₁ e inclinata rispetto a π₂ (orizzontale, ma storta rispetto alla parete): retta orizzontale;<br>![[b04-retta-stanza-5.svg|230]]
- inclinata rispetto a π₁ e a π₂, ma tutta contenuta in un piano perpendicolare alla linea di terra (parallela a π₃, il piano di lato): retta di profilo;<br>![[b04-retta-stanza-6.svg|230]]
- inclinata rispetto a tutti e tre i piani: retta generica.<br>![[b04-retta-stanza-7.svg|230]]

Nei disegnini la stanza è il triedro: π₁ è il pavimento, π₂ la parete di fronte, π₃ la parete di lato. La retta è in rosso; la linea grigia tratteggiata sul pavimento è la sua «ombra» dall'alto, cioè la prima proiezione.

Ognuna di queste rette ha il suo paragrafo più avanti in questa pagina.

### 3.1.2 Le tracce (8 e 13 ottobre)

La traccia di una retta è il punto in cui la retta incontra un piano di proiezione. Essendo un punto si scrive con la T maiuscola, il numero del piano e il nome della retta: T₁ᵣ su π₁, T₂ᵣ su π₂, T₃ᵣ su π₃.

La traccia è un punto della retta reale: è la retta stessa che "buca" il piano, quindi la traccia appartiene alla retta.

Una retta lascia sempre tre tracce. Quando è parallela a un piano di proiezione, la traccia su quel piano esiste, ma è all'infinito, nella direzione della retta.

La traccia all'infinito si scrive (per esempio T₂f∞) e si segna con una lineetta che indica la direzione della retta: non va messa a caso. Anche se non la si vede, va disegnata, perché appartiene alla retta.

Una retta passa infatti per due punti propri, ma anche per un punto proprio e un punto improprio, che le dà la direzione.

### 3.1.3 Le proiezioni passano per le proiezioni delle tracce (8, 13 e 15 ottobre)

Una proiezione non è la retta: è la proiezione di tutti i suoi punti, comprese le tracce. Siccome le tracce sono punti noti della retta, le proiezioni della retta passano per le proiezioni delle tracce.

- La prima proiezione passa per la prima traccia e per la prima proiezione delle altre tracce.
- La seconda proiezione passa per la seconda traccia e per la seconda proiezione delle altre.
- La terza proiezione passa per la terza traccia e per la terza proiezione delle altre.

Le proiezioni delle tracce cadono sempre sulla linea di terra o sulla linea verticale, perché le tracce stanno sui piani di proiezione: tutto ciò che sta su π₁, proiettato su π₂, finisce sulla LT.

Le proiezioni della retta si disegnano a tratto continuo. Si tratteggiano solo le parti che passano dietro un piano di proiezione e non si vedono.

## 3.2 Le rette proiettanti (8 ottobre)

Le rette proiettanti sono quelle perpendicolari a uno dei primi due piani di proiezione. Si chiamano così perché hanno la stessa direzione dei raggi proiettanti: il centro di proiezione all'infinito è perpendicolare al piano, e la retta è parallela a quei raggi.

In una retta proiettante la traccia nota è sempre quella sul piano a cui la retta è perpendicolare; le altre due sono all'infinito.

### 3.2.1 La retta proiettante in prima (8 ottobre)

La retta proiettante in prima è perpendicolare a π₁, cioè verticale.

Vista dall'alto si riduce a un punto, in cui coincidono la prima proiezione della retta, la sua prima traccia e la prima proiezione di ogni suo punto: r₁ ≡ T₁ᵣ ≡ P₁.

La seconda e la terza proiezione sono verticali, cioè perpendicolari alla LT. La retta è parallela sia a π₂ sia a π₃, quindi la seconda e la terza traccia sono all'infinito (T₂ᵣ∞, T₃ᵣ∞).

> [!example] Disegno 8 · La retta proiettante in prima
> ![[03-retta-proiettante-in-prima.svg|620]]
>
> Sul foglio: r₁ ≡ T₁ᵣ ≡ P₁ è un punto sotto la LT; r₂ parte dalla LT ed è perpendicolare alla LT; r₃ è verticale, a una distanza dalla linea verticale pari all'aggetto, riportato con l'arco.
>
> ![[b03-spazio-retta-proiettante-in-prima.svg|560]]
>
> Nello spazio (schema proposto, non disegnato a lezione): la retta sale verticale da π₁ e lo buca in T₁ᵣ, dove si schiaccia tutta la prima proiezione; un suo punto P ha P₂ e P₃ alla stessa quota.

### 3.2.2 La retta proiettante in seconda (8 ottobre)

La retta proiettante in seconda (qui m) è perpendicolare a π₂.

La sua traccia nota è la seconda, T₂ₘ, il punto in cui la retta incontra il piano verticale. Vista di fronte la retta si riduce a quel punto, quindi la seconda proiezione coincide con la seconda traccia: m₂ ≡ T₂ₘ.

Dalla seconda proiezione si scende con la linea di richiamo e si disegna la prima proiezione m₁, perpendicolare alla LT. La terza proiezione m₃ è parallela alla LT, alla stessa quota di m₂.

La retta è parallela a π₁ e a π₃, quindi la prima e la terza traccia sono all'infinito (T₁ₘ∞, T₃ₘ∞).

> [!example] Disegno 9 · La retta proiettante in seconda
> ![[03-retta-proiettante-in-seconda.svg|620]]
>
> Sul foglio: m₂ ≡ T₂ₘ è un punto sopra la LT; m₁ parte dalla LT ed è perpendicolare alla LT; m₃ è orizzontale, alla stessa quota di m₂.
>
> ![[03-spazio-retta-proiettante-in-seconda.svg|560]]
>
> Nello spazio: la retta esce perpendicolare da π₂ e lo buca in T₂ₘ; non incontra mai π₁ e π₃, quindi le altre due tracce sono all'infinito.

## 3.3 Le rette parallele a un piano di proiezione (13 ottobre)

### 3.3.1 La retta parallela alla linea di terra, cioè proiettante in terza (13 ottobre)

La retta parallela alla linea di terra è parallela a π₁ e a π₂ e perpendicolare a π₃: per questo si potrebbe dire anche proiettante in terza.

L'unica traccia propria è T₃ᵣ, il punto in cui la retta buca π₃. La prima e la seconda traccia sono all'infinito, nella direzione delle sue proiezioni.

Proiettando T₃ᵣ su π₁ e su π₂ si trovano due punti sulla linea verticale, (T₃ᵣ)₁ e (T₃ᵣ)₂. Da lì partono le proiezioni r₁ e r₂, parallele alla linea di terra.

In terza proiezione la retta si riduce a un punto, che coincide con la sua traccia: r₃ ≡ T₃ᵣ.

> [!example] Disegno 10 · La retta parallela alla LT
> ![[04-retta-parallela-alla-lt.svg|620]]
>
> Sul foglio: T₃ᵣ sta sul terzo piano, alla quota e all'aggetto della retta; da (T₃ᵣ)₂ e (T₃ᵣ)₁ sulla verticale partono r₂ e r₁, parallele alla LT; T₁ᵣ∞ e T₂ᵣ∞ si segnano con la lineetta.
>
> ![[04-spazio-retta-parallela-alla-lt.svg|560]]
>
> Nello spazio: la retta è fissata su π₃ in T₃ᵣ; le sue proiezioni sul pavimento e sulla parete π₂ sono parallele alla LT.

13-10!!

### 3.3.2 La retta frontale (13 ottobre)

La retta frontale è parallela a π₂, cioè sta di fronte, a distanza costante da π₂, ma ha una sua inclinazione.

Le sue tracce proprie sono la prima, T₁f, e la terza, T₃f, che hanno la stessa distanza da π₂. La seconda traccia T₂f è all'infinito, nella direzione della retta.

Le sue proiezioni:

- la prima proiezione f₁ è parallela alla linea di terra, ed è la caratteristica fondamentale da ricordare;
- la seconda proiezione f₂ è parallela alla retta, cioè ne mostra l'inclinazione; passa per (T₁f)₂ sulla LT e per (T₃f)₂ sulla verticale;
- la terza proiezione f₃ è verticale.

> [!example] Disegno 11 · La retta frontale
> ![[04-retta-frontale.svg|620]]
>
> Sul foglio: f₁ unisce T₁f e (T₃f)₁ ed è parallela alla LT; f₂ unisce (T₁f)₂ e (T₃f)₂ ed è inclinata come la retta; f₃ è verticale e arriva a T₃f; si segna T₂f∞ nella direzione di f₂.
>
> ![[04-spazio-retta-frontale.svg|560]]
>
> Nello spazio: f sta di fronte a π₂, a distanza costante; buca il pavimento in T₁f e π₃ in T₃f.

### 3.3.3 La retta orizzontale (13 ottobre)

La retta orizzontale è parallela a π₁ ma inclinata rispetto ai piani verticali; tutti i suoi punti stanno alla stessa altezza.

Le sue tracce proprie sono la seconda, T₂ₒ, e la terza, T₃ₒ, alla stessa quota. La prima traccia T₁ₒ è all'infinito, nella direzione di o₁.

Le sue proiezioni:

- la seconda proiezione o₂ è parallela alla linea di terra;
- la prima proiezione o₁ passa per (T₂ₒ)₁ sulla LT e per (T₃ₒ)₁ sulla verticale, e mostra l'inclinazione della retta;
- la terza proiezione o₃ sta sulla stessa linea di o₂.

L'orizzontale è molto utile anche in architettura, per esempio per valutare la pendenza di un terreno o di una falda.

> [!example] Disegno 12 · La retta orizzontale
> ![[04-retta-orizzontale.svg|620]]
>
> Sul foglio: o₂ è parallela alla LT e passa per T₂ₒ; o₁ unisce (T₂ₒ)₁ e (T₃ₒ)₁ ed è inclinata; o₃ prosegue o₂ fino a T₃ₒ; si segna T₁ₒ∞ nella direzione di o₁.
>
> ![[04-spazio-retta-orizzontale.svg|560]]
>
> Nello spazio: o resta alla stessa altezza dal pavimento; buca π₂ in T₂ₒ e π₃ in T₃ₒ.

Riassumendo le due rette più importanti:

- la frontale ha la prima proiezione parallela alla LT e la seconda traccia all'infinito;
- l'orizzontale ha la seconda proiezione parallela alla LT e la prima traccia all'infinito.

### 3.3.4 La retta di profilo (13 ottobre)

La retta di profilo è parallela a π₃ e inclinata rispetto agli altri due piani. La prima e la seconda traccia hanno la stessa distanza da π₃, e la terza traccia è all'infinito.

Le sue proiezioni su π₁ e su π₂ stanno sulla stessa linea, perpendicolare alla linea di terra. Per questo la retta si vede davvero soltanto sul terzo piano di proiezione, come una figura parallela a π₃ che si vede di profilo.

Anche un punto della retta di profilo non si individua con le sole prima e seconda proiezione: serve la terza.

> [!example] Disegno 13 · La retta di profilo
> ![[04-retta-di-profilo.svg|620]]
>
> Sul foglio: r₂ e r₁ stanno sulla stessa perpendicolare alla LT; r₃ unisce (T₂ᵣ)₃ e (T₁ᵣ)₃ e solo lì si vede l'inclinazione della retta; si scrive T₃ᵣ∞.
>
> ![[04-spazio-retta-di-profilo.svg|560]]
>
> Nello spazio: la retta scende da π₂ (T₂ᵣ) al pavimento (T₁ᵣ) restando parallela a π₃.

15-10!!!

## 3.4 La retta generica (15 e 20 ottobre)

La retta generica non ha condizioni di particolarità: ha tutte le tracce proprie, cioè buca π₁, π₂ e π₃.

### 3.4.1 Le proiezioni dalle tracce (15 ottobre)

Le proiezioni si costruiscono a partire dai due punti che si conoscono, la prima e la seconda traccia.

- La prima traccia T₁ᵣ, proiettata su π₂, cade sulla LT in (T₁ᵣ)₂. La seconda traccia sta già su π₂. Quindi r₂ passa per T₂ᵣ e per (T₁ᵣ)₂.
- La seconda traccia, proiettata su π₁, cade sulla LT in (T₂ᵣ)₁. Quindi r₁ passa per T₁ᵣ e per (T₂ᵣ)₁.

Le parole vanno usate con attenzione: «la seconda proiezione della prima traccia» non è un gioco di parole, ma un'azione, proiettare quel punto su π₂.

> [!example] Disegno 14 · Le proiezioni della retta generica
> ![[05-retta-generica-proiezioni.svg|560]]
>
> Da T₁ᵣ si sale con il richiamo fino alla LT: (T₁ᵣ)₂; r₂ passa per T₂ᵣ e (T₁ᵣ)₂.
> Da T₂ᵣ si scende fino alla LT: (T₂ᵣ)₁; r₁ passa per T₁ᵣ e (T₂ᵣ)₁.
>
> ![[05-spazio-retta-generica.svg|620]]
>
> Nello spazio: r₁ è come l'ombra della retta sul pavimento, r₂ la sua immagine sulla parete.

### 3.4.2 Le tracce dalle proiezioni: i punti notevoli sulla LT (20 ottobre)

Il procedimento si può fare anche al contrario, quando sono date le proiezioni della retta e se ne cercano le tracce.

Prolungando la seconda proiezione fino alla linea di terra si trova un punto preciso, che ha un nome: la seconda proiezione della prima traccia, (T₁ᵣ)₂. Non è la traccia, perché la retta non incide la linea di terra; ma scendendo con la perpendicolare alla LT fino alla prima proiezione si trova T₁ᵣ.

Allo stesso modo, prolungando la prima proiezione fino alla LT si trova la prima proiezione della seconda traccia, (T₂ᵣ)₁, e salendo fino alla seconda proiezione si trova T₂ᵣ.

Ogni punto va chiamato con il suo nome: non «il punto sulla linea dove va la proiezione», ma prima o seconda proiezione di una traccia.

> [!example] Disegno 15 · I punti notevoli della retta generica
> ![[06-retta-generica-punti-notevoli.svg|620]]
>
> Si prolunga r₂ fino alla LT, si trova (T₁ᵣ)₂ e si scende fino a r₁: lì c'è T₁ᵣ.
> Si prolunga r₁ fino alla LT, si trova (T₂ᵣ)₁ e si sale fino a r₂: lì c'è T₂ᵣ.

### 3.4.3 La posizione delle tracce dipende dalla direzione (20 ottobre)

La retta disegnata finora è quella canonica, ma una retta può avere altre direzioni:

- può non bucare né π₁ né π₂ dalla parte del modello e bucarli sotto la linea di terra;
- può venire da fuori;
- può essere alta e bucare prima π₂, poi π₁, poi π₃.

Si possono quindi trovare tutte e due le tracce sotto la LT o tutte e due sopra. Il procedimento non cambia, perché le proiezioni della retta passano sempre per i due punti notevoli sulla linea di terra.

Questa configurazione servirà per le ombre, in cui la luce deve venire da fuori.

> [!example] Disegno 16 · Una retta con le tracce dall'altra parte
> ![[b06-retta-tracce-sotto-la-lt.svg|600]]
>
> Schema proposto, non disegnato a lezione.
> I punti notevoli (T₁ᵣ)₂ e (T₂ᵣ)₁ si trovano come prima, ma il richiamo da (T₂ᵣ)₁ verso r₂ questa volta va in giù, e T₂ᵣ cade sotto la LT.

### 3.4.4 La terza traccia (15 ottobre)

La retta generica ha anche una terza traccia, il punto in cui buca π₃.

Per disegnare la terza proiezione non serve: bastano le terze proiezioni della prima e della seconda traccia, perché per due punti passa una retta.

Trovarla è più difficile, perché la retta buca π₃ non dentro il primo diedro ma dietro, dove nel modello il piano non c'è; i piani però sono infiniti. Non è uno spazio occulto, ma una posizione dello spazio.

Il primo modo è immediato: la terza proiezione passa per la terza traccia, quindi si prolunga r₃, tratteggiandola perché la retta sta andando dietro. A mano, però, graficamente potrebbe non tornare.

Il secondo modo, più sicuro, usa un piano ausiliario, e si vede più avanti, tra i piani ausiliari.

---

## Collegamenti

Il capitolo successivo è [[PO 4 - Il piano]]. Il capitolo precedente è [[PO 2 - Il punto]].
