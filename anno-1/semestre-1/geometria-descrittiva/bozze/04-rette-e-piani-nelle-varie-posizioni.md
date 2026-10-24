---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-13
tags: [geometria-descrittiva, bozza]
---

# Rette e piani nelle varie posizioni (metodo di Monge)

> [!info] Note collegate
> Sbobina: [[04-rette-e-piani-metodo-di-monge]]
>
> Bozza precedente: [[03-proiezioni-ortogonali-punto-e-rette]] · Successiva: [[05-appartenenza-e-rette-ausiliarie]]

Dopo il punto e le rette proiettanti, la lezione del 13 ottobre completa la rappresentazione delle rette particolari nel metodo di Monge:

- la retta parallela alla linea di terra,
- la frontale,
- l'orizzontale
- e la retta di profilo.

E introduce i piani, che non si rappresentano come figure ma attraverso le loro tracce:

- il piano parallelo alla linea di terra,
- il frontale,
- l'orizzontale,
- quello di profilo
- e il proiettante in prima.

Ogni retta viene costruita su un piano che la contiene, e da questo accostamento nascono le condizioni di appartenenza tra punto, retta e piano.

Il metodo di lavoro è sempre lo stesso:

1. si colloca l'elemento nel modello del triedro (uno stecchino per la retta, un cartoncino per il piano),
2. si fanno le proiezioni sul modello,
3. si apre il modello e si ricava il disegno sul foglio.

La lezione si chiude con un esercizio sulla figura nel piano parallelo alla linea di terra e con la correzione dell'esercizio guidato di omologia.

## IL TRIEDRO E IL NOME DELLE RETTE

### Lo schema del triedro

Per richiamare il modello, alla lavagna il triedro si disegna con un'assonometria particolare, in cui il piano su cui si proietta coincide con π₁: la pianta mantiene così la sua forma (non la dimensione, che dipende dalla scala), e gli angoli di 90° restano di 90°.

Per comodità lo schema si disegna ruotato, con l'angolo retto alla base:

- π₁ in basso,
- π₂ e π₃ in verticale.

La linea di intersezione tra π₁ e π₂ è la linea di terra (LT), che, quando si ribaltano i piani gli uni sugli altri, divide la pianta dal prospetto.

Non divide però lo spazio in modo rigido: le prime proiezioni non stanno per forza sotto e le seconde sopra, perché dipende dal quadrante in cui si trovano i punti.

In architettura, naturalmente, le cose stanno tutte nel primo diedro.

> [!example] Disegno 1 · Il disegno: il triedro come alla lavagna
> ![[04-triedro-come-alla-lavagna.svg|560]]
>
> 1. Si disegna lo spigolo π₂/π₃ in verticale.
> 2. Dal suo piede partono la LT, verso il basso a sinistra, e lo spigolo π₁/π₃, verso il basso a destra: tra le due c'è un angolo retto, perché π₁ è in vera forma.
> 3. Si chiudono i tre piani: π₂ a sinistra, π₃ a destra, π₁ in basso. Lo schema deve essere grande, come le proiezioni.

### Il nome della retta, le tracce e le proiezioni

Il nome di una retta viene assegnato in base alla posizione che assume rispetto ai primi due piani di proiezione, π₁ (orizzontale) e π₂ (verticale); il nome è importante perché serve a condividere la conoscenza sulle cose.

Una retta perpendicolare a π₃, per esempio, è anche proiettante in terza, ma si chiama parallela alla linea di terra, perché è parallela a π₁ e a π₂.

Il punto in cui una retta incontra un piano di proiezione si chiama traccia della retta.

Essendo un punto si scrive con la T maiuscola, con il numero del piano e il nome della retta:

- T₁ᵣ su π₁,
- T₂ᵣ su π₂,
- T₃ᵣ su π₃.

La traccia è un punto della retta reale: è la retta stessa che "buca" il piano, quindi la traccia appartiene alla retta.

Una retta lascia sempre tre tracce; quando è parallela a un piano di proiezione, la traccia su quel piano esiste ma è all'infinito, nella direzione della retta, e si segna con una lineetta che indica quella direzione (per esempio T₂f∞): non va messa a caso.

Le proiezioni ortogonali presuppongono che la retta sia proiettata da un centro all'infinito, con raggi paralleli, sul primo, sul secondo e sul terzo piano.

Si potrebbero proiettare gli infiniti punti della retta, ma due o tre punti sono sicuramente noti, le tracce: per questo le proiezioni della retta passano per le proiezioni delle tracce.

Una proiezione non è la retta, è la proiezione di tutti i suoi punti, comprese le tracce; le proiezioni delle tracce sulla linea di terra o sulla verticale si scrivono tra parentesi, come (T₃ᵣ)₁ o (T₁ᵣ)₂.

Le proiezioni non sono vignette separate dalla linea verticale: partono dalla linea di intersezione dei piani, perché si lavora con le tracce, e il disegno deve essere quello che si vede sul modello aperto.

> [!abstract] Da ricordare
> - Il nome della retta dipende dalla sua posizione rispetto a π₁ e π₂.
> - La traccia è un punto della retta: T maiuscola, con il numero del piano (T₁ᵣ, T₂ᵣ, T₃ᵣ).
> - Una retta lascia sempre tre tracce; se è parallela a un piano, la traccia su quel piano è all'infinito e si segna con la lineetta nella direzione della retta.
> - Le proiezioni della retta passano per le proiezioni delle tracce.
> - La prima proiezione passa per la prima traccia e per la prima proiezione delle altre tracce (e così per la seconda e la terza).

## LE RETTE NELLE VARIE POSIZIONI

### La retta parallela alla linea di terra

Uno stecchino fissato su π₃ e perpendicolare a π₃, a una certa quota (altezza) e a una certa distanza da π₂ (l'aggetto), è parallelo a π₁ e a π₂: è la retta parallela alla linea di terra, anche se è giusto dire che è proiettante in terza.

Le sue tracce:

- l'unica traccia propria è T₃ᵣ, il punto in cui la retta è fissata su π₃;
- la prima e la seconda traccia sono all'infinito, perché la retta incontra π₁ e π₂ all'infinito, nella direzione delle sue proiezioni.

Proiettando T₃ᵣ su π₁ e su π₂ si trovano due punti sulla linea di intersezione dei piani, e da lì partono le proiezioni r₁ e r₂, parallele alla linea di terra.

In terza proiezione la retta si riduce a un punto, che coincide con la sua traccia.

> [!example] Disegno 2 · Il disegno: la retta parallela alla LT
> ![[04-retta-parallela-alla-lt.svg|620]]
>
> 1. Si segna T₃ᵣ (r₃ ≡ T₃ᵣ) sul terzo piano, alla quota della retta e all'aggetto della retta (portato con l'arco).
> 2. Si proietta T₃ᵣ su π₂: cade sulla verticale in (T₃ᵣ)₂. Da lì parte r₂, parallela alla LT.
> 3. Si proietta T₃ᵣ su π₁: cade sulla verticale, sotto la LT, in (T₃ᵣ)₁. Da lì parte r₁, parallela alla LT.
> 4. Si segnano T₁ᵣ∞ e T₂ᵣ∞ con la lineetta nella direzione di r₁ e r₂.
> 5. La retta in grassetto, le costruzioni più leggere.
>
> ![[04-spazio-retta-parallela-alla-lt.svg|560]]
>
> Nello spazio: lo stecchino è fissato su π₃ in T₃ᵣ; le sue proiezioni r₁ (sul pavimento) e r₂ (sulla parete π₂) sono parallele alla LT.

### La retta frontale

La frontale è una delle due rette fondamentali per la soluzione degli esercizi.

Si trova su un piano parallelo a π₂ (di fronte, come nella prospettiva frontale), ma ha una sua inclinazione. Per collocarla nel modello le due tracce devono avere la stessa distanza da π₂, altrimenti la retta non è parallela: in pratica si costruisce già il piano che la contiene.

Le tracce:

- le tracce proprie sono la prima, T₁f, e la terza, T₃f;
- la seconda, T₂f, è all'infinito nella direzione della retta, ed è proprio il punto all'infinito visto nella prima lezione. Anche se non la si vede, va disegnata, perché appartiene alla retta.

Guardando il modello:

- la seconda proiezione f₂ è parallela alla retta, cioè ne mostra l'inclinazione;
- la prima proiezione f₁ risulta parallela alla linea di terra, ed è la caratteristica fondamentale da ricordare;
- la terza proiezione f₃ è verticale.

Per costruire f₂ si proiettano su π₂ la prima e la terza traccia: f₂ passa per le loro proiezioni e per la seconda traccia, all'infinito.

> [!example] Disegno 3 · Il disegno: la retta frontale
> ![[04-retta-frontale.svg|620]]
>
> 1. Si fissano T₁f (sotto la LT, all'aggetto della retta) e T₃f (sul terzo piano, alla stessa distanza da π₂).
> 2. Prima proiezione: T₃f proiettato su π₁ cade in (T₃f)₁ sulla verticale; f₁ unisce T₁f e (T₃f)₁ ed è parallela alla LT.
> 3. Seconda proiezione: T₁f proiettato su π₂ cade sulla LT in (T₁f)₂, T₃f cade sulla verticale in (T₃f)₂; f₂ unisce i due punti ed è inclinata come la retta.
> 4. Terza proiezione: T₁f si porta con l'arco sulla LT in (T₁f)₃; f₃ è verticale e arriva a T₃f.
> 5. Si segna T₂f∞ con la lineetta nella direzione di f₂.
>
> ![[04-spazio-retta-frontale.svg|560]]
>
> Nello spazio: f sta di fronte a π₂, a distanza costante; buca il pavimento in T₁f e π₃ in T₃f.

### La retta orizzontale

Uno stecchino parallelo a π₁ ma inclinato rispetto ai piani verticali è una retta orizzontale, che si indica con la o minuscola; anche lei è molto utile negli esercizi, per esempio per valutare la pendenza di un terreno quando si vuole segnare la freccia di pendenza.

Le tracce:

- le tracce proprie sono la seconda, T₂ₒ, e la terza, T₃ₒ, alla stessa quota, perché la retta è orizzontale;
- la prima traccia T₁ₒ esiste, ma è all'infinito nella direzione di o₁.

Le proiezioni:

- la seconda proiezione o₂ passa per la seconda traccia, che sta già su π₂, e per la seconda proiezione della terza traccia (e della prima, all'infinito): è parallela alla linea di terra;
- la prima proiezione o₁ passa per la prima proiezione di T₂ₒ e di T₃ₒ, e per la prima traccia all'infinito: mostra l'inclinazione della retta;
- aprendo il modello, o₂ e o₃ stanno sulla stessa linea.

Le frasi che sembrano difficili si capiscono leggendole guardando il modello: la geometria descrittiva si studia così.

> [!example] Disegno 4 · Il disegno: la retta orizzontale
> ![[04-retta-orizzontale.svg|620]]
>
> 1. Si fissano T₂ₒ (sopra la LT, alla quota della retta) e T₃ₒ (sul terzo piano, alla stessa quota).
> 2. Seconda proiezione: T₃ₒ proiettato su π₂ cade sulla verticale, sulla stessa orizzontale di T₂ₒ; o₂ è parallela alla LT.
> 3. Prima proiezione: T₂ₒ proiettato su π₁ cade sulla LT in (T₂ₒ)₁, T₃ₒ cade sulla verticale in (T₃ₒ)₁; o₁ unisce i due punti ed è inclinata.
> 4. Terza proiezione: o₃ è sulla stessa linea di o₂ e arriva a T₃ₒ, portato con l'arco da (T₃ₒ)₁.
> 5. Si segna T₁ₒ∞ con la lineetta nella direzione di o₁.
>
> ![[04-spazio-retta-orizzontale.svg|560]]
>
> Nello spazio: o è uno stecchino tenuto alla stessa altezza dal pavimento; buca π₂ in T₂ₒ e π₃ in T₃ₒ.

### La retta di profilo

La retta parallela a π₃ ha la prima e la seconda traccia alla stessa distanza da π₃, ed è inclinata rispetto agli altri due piani.

Le sue proiezioni su π₁ e su π₂ stanno sulla stessa linea, perpendicolare alla linea di terra: potremmo dire coincidenti.

Per capire come si chiama basta immaginare, al posto della retta, una figura parallela a π₃: la si vede di profilo. È quindi una retta di profilo, perché tutte le rette e i segmenti paralleli a π₃ hanno la prima e la seconda proiezione sulla stessa linea, e la retta si vede davvero soltanto sul terzo piano di proiezione.

La terza traccia è all'infinito.

> [!example] Disegno 5 · Il disegno: la retta di profilo
> ![[04-retta-di-profilo.svg|620]]
>
> 1. T₂ᵣ e T₁ᵣ stanno sulla stessa perpendicolare alla LT: r₂ va da T₂ᵣ alla LT, r₁ dalla LT a T₁ᵣ. Sulla LT, (T₁ᵣ)₂ ≡ (T₂ᵣ)₁.
> 2. Terza proiezione: T₂ᵣ si porta in orizzontale sulla verticale, in (T₂ᵣ)₃; T₁ᵣ si porta sulla verticale e con l'arco sulla LT, in (T₁ᵣ)₃.
> 3. r₃ unisce (T₂ᵣ)₃ e (T₁ᵣ)₃: solo qui si vede l'inclinazione della retta. Si scrive T₃ᵣ∞.
>
> ![[04-spazio-retta-di-profilo.svg|560]]
>
> Nello spazio: la retta scende da π₂ (T₂ᵣ) al pavimento (T₁ᵣ) restando parallela a π₃.

Proprio perché r₁ e r₂ stanno sulla stessa linea, anche un punto della retta di profilo non si individua con le sole due proiezioni: come dirà la docente a proposito del piano di profilo, per vedere a cosa corrisponde una figura serve la terza proiezione.

> [!example] Disegno 6 (proposto, non fatto a lezione): un punto P sulla retta di profilo
> ![[b04-punto-sulla-retta-di-profilo.svg|620]]
>
> 1. Si disegna la retta di profilo con le sue tracce e la terza proiezione r₃, come sopra.
> 2. Si sceglie P₂ su r₂: si porta la sua quota in orizzontale fino a r₃, e lì c'è P₃.
> 3. Da P₃ si scende sulla LT, si torna con l'arco sulla verticale (sotto la LT) e si va in orizzontale fino a r₁: lì c'è P₁.
> 4. È il primo esercizio a sinistra in seconda fila del foglio PO_riepilogo_1 ("Disegnare un punto P appartenente alla retta r"); nella soluzione della docente la terza proiezione è costruita a sinistra della retta, ruotando T₁ᵣ sulla LT, con lo stesso principio.

> [!abstract] Da ricordare: le rette nelle varie posizioni
> | Retta | Posizione | Tracce proprie | Traccia all'infinito | Proiezioni |
> |---|---|---|---|---|
> | parallela alla LT (r) | parallela a π₁ e π₂, perpendicolare a π₃ | T₃ᵣ | T₁ᵣ∞, T₂ᵣ∞ | r₁ e r₂ parallele alla LT; r₃ è un punto (≡ T₃ᵣ) |
> | frontale (f) | parallela a π₂ | T₁f, T₃f | T₂f∞ | f₁ parallela alla LT; f₂ inclinata come la retta; f₃ verticale |
> | orizzontale (o) | parallela a π₁ | T₂ₒ, T₃ₒ (stessa quota) | T₁ₒ∞ | o₂ parallela alla LT; o₁ inclinata come la retta; o₂ e o₃ sulla stessa linea |
> | di profilo (r) | parallela a π₃ | T₁ᵣ, T₂ᵣ | T₃ᵣ∞ | r₁ e r₂ sulla stessa perpendicolare alla LT; si vede solo r₃ |
>
> Frontale: prima proiezione parallela alla LT. Orizzontale: seconda proiezione parallela alla LT.

## I PIANI E LE LORO TRACCE

### Il piano non è una figura

Il piano si considera esteso all'infinito: non è una figura, ma un ente geometrico esteso nelle due dimensioni.

Quando nel modello o negli esercizi lo si vede come un rettangolo, è solo per comodità; i tratteggi oltre i bordi dicono che il piano prosegue. Per questo il piano non si rappresenta con le proiezioni (se fosse un rettangolo, nel prospetto se ne vedrebbero tutti i lati), ma con le tracce, cioè le rette di intersezione che lascia sui piani di proiezione.

La traccia è il segno lasciato dal contatto di una cosa sull'altra:

- la traccia della retta è un punto,
- la traccia del piano è una retta.

Si scrive con la t minuscola (perché è una retta), il numero del piano e la lettera greca del piano: t₁α, t₂α, t₃α.

Conviene scrivere il nome vicino alla traccia, così si riconosce subito il piano; se il piano è parallelo a un piano di proiezione, la traccia corrispondente è all'infinito e si scrive anche quella (per esempio t₂β∞).

Come le rette, anche i piani prendono il nome dalla posizione rispetto ai piani di proiezione.

> [!example] Disegno 7 · Il disegno: il piano frontale non è una figura
> ![[04-spazio-piano-non-e-una-figura.svg|560]]
>
> 1. Il cartoncino del piano frontale β è disegnato come un rettangolo, ma i tratteggi dicono che prosegue.
> 2. Le uniche cose che restano sono le tracce: t₁β sul pavimento e t₃β su π₃; t₂β è all'infinito.
> 3. Sul foglio si disegnano solo t₁β, che dà l'aggetto del piano rispetto a π₂, e t₃β, portata con la rotazione di π₃ (vedi il piano frontale più avanti).

### Il piano parallelo alla linea di terra

Il primo piano è costruito per contenere la retta parallela alla linea di terra: è anch'esso parallelo alla linea di terra, ma inclinato rispetto a π₁ e a π₂.

Taglia tutti e tre i piani di proiezione, quindi ha tre tracce: aprendo il modello,

- la prima traccia t₁α e la seconda t₂α risultano parallele alla linea di terra,
- mentre la terza t₃α è variamente inclinata.

Il piano è stato fatto passare apposta per la retta r, costruendo la terza traccia del piano t₃α passante per la terza traccia della retta T₃ᵣ: è da qui che nascono le condizioni di appartenenza.

Sul piano non c'è solo r: ci possono essere tante rette parallele alla linea di terra, figure e punti, ognuno con le sue proiezioni.

> [!example] Disegno 8 · Il disegno: il piano parallelo alla LT che contiene la retta r
> ![[04-piano-parallelo-alla-lt.svg|620]]
>
> 1. Si disegna la retta r parallela alla LT (r₂, r₁ e T₃ᵣ), come prima.
> 2. Si traccia t₃α passante per T₃ᵣ, inclinata: incontra la verticale in alto e la LT a destra.
> 3. Dal punto in alto sulla verticale parte t₂α, parallela alla LT.
> 4. Dal punto sulla LT a destra si torna con l'arco sulla verticale, sotto la LT: da lì parte t₁α, parallela alla LT.
> 5. r appartiene ad α perché T₃ᵣ sta su t₃α (le altre tracce di r sono all'infinito, come le direzioni di t₁α e t₂α).
>
> ![[04-spazio-piano-parallelo-alla-lt.svg|560]]
>
> Nello spazio: α è un cartoncino inclinato tra il pavimento e la parete π₂, parallelo alla LT; r sta sul cartoncino e buca π₃ sulla traccia t₃α.

### Il piano frontale

Il piano frontale è parallelo a π₂ e perpendicolare a π₁ e a π₃; è uno dei piani più usati in architettura.

Facendolo passare per la retta frontale, ha:

- la prima traccia t₁β sul pavimento
- e la terza t₃β verticale,
- mentre la seconda non c'è, perché il piano è parallelo a π₂: la retta di intersezione esiste, ma all'infinito, e si scrive t₂β∞ vicino alle altre tracce.

Perché la frontale appartenga al piano, la prima traccia del piano deve passare per la prima traccia della retta: si sta verificando una condizione di appartenenza.

I piani frontali sono infiniti, come le sezioni di un edificio: dove farli passare dipende da che cosa si vuole far vedere.

> [!example] Disegno 9 · Il disegno: il piano frontale che contiene la retta frontale f
> ![[04-piano-frontale.svg|620]]
>
> 1. Si traccia t₁β parallela alla LT, passante per T₁f: coincide con f₁. La distanza dalla LT è l'aggetto del piano.
> 2. Con l'arco si porta l'aggetto sul terzo piano e si alza t₃β, verticale: contiene f₃ e T₃f.
> 3. Si scrive t₂β∞.
>
> ![[04-spazio-piano-frontale.svg|560]]
>
> Nello spazio: β è una parete parallela a π₂; T₁f sta su t₁β e T₃f su t₃β.

### Il piano orizzontale

Tutte le sezioni orizzontali, tutte le piante, sono fatte con piani orizzontali.

Il piano orizzontale è parallelo a π₁, quindi:

- la prima traccia è all'infinito (t₁γ∞),
- mentre la seconda e la terza ci sono e, aprendo il modello, risultano orizzontali, sulla stessa linea.

Sempre per le condizioni di appartenenza, il piano si fa passare per la retta orizzontale, facendo incidere la traccia della retta con la traccia del piano; si possono scrivere anche le coincidenze.

> [!example] Disegno 10 · Il disegno: il piano orizzontale che contiene la retta orizzontale o
> ![[04-piano-orizzontale.svg|620]]
>
> 1. Si traccia t₂γ parallela alla LT, all'altezza del piano, passante per T₂ₒ: coincide con o₂ (t₂γ ≡ o₂).
> 2. t₃γ prosegue alla stessa altezza dall'altra parte della verticale e passa per T₃ₒ.
> 3. Si scrive t₁γ∞.
>
> ![[04-spazio-piano-orizzontale.svg|560]]
>
> Nello spazio: γ è un pavimento sollevato, come il piano di sezione di una pianta; contiene la retta o.

### Il piano di profilo

Per la retta di profilo si può costruire un piano di profilo, parallelo a π₃ (anche qui i piani possibili sono infiniti).

Le tracce:

- la terza traccia è all'infinito;
- la prima, t₁δ, e la seconda, t₂δ, ci sono e, aprendo il modello, stanno sulla stessa linea perpendicolare alla linea di terra, dove si possono scrivere direttamente le coincidenze con le proiezioni della retta.

Sono piani semplici e intuitivi.

> [!example] Disegno 11 · Il disegno: il piano di profilo che contiene la retta di profilo
> ![[04-piano-di-profilo.svg|620]]
>
> 1. t₂δ e t₁δ partono dallo stesso punto della LT e sono perpendicolari alla LT (segnare gli angoli retti).
> 2. La retta di profilo appartiene a δ: T₂ᵣ sta su t₂δ, T₁ᵣ su t₁δ, e t₂δ ≡ r₂, t₁δ ≡ r₁.
> 3. Si scrive t₃δ∞. La retta si vede com'è solo in r₃.
>
> ![[04-spazio-piano-di-profilo.svg|560]]
>
> Nello spazio: δ è una parete parallela a π₃; taglia il pavimento e la parete π₂ lungo due tracce perpendicolari alla LT.

### Il piano proiettante in prima

Anche il frontale è un piano verticale, ma il piano proiettante in prima va distinto da quello: è perpendicolare a π₁ e forma un angolo con π₂. Questi piani sono molto utili e sono quelli che si usano di più in architettura.

Ha tre tracce:

- la prima è inclinata,
- la seconda e la terza, aprendo il modello, sono verticali.

Se si segna un punto P sul cartoncino prima di collocarlo e se ne fa la prima proiezione, P₁ cade proprio sulla prima traccia del piano. Non è la regola, ma una coincidenza dei piani verticali: la regola dice che un punto appartiene al piano se appartiene a una retta del piano.

Facendo passare per P una retta verticale r:

1. la sua prima proiezione è un punto che coincide con T₁ᵣ,
2. e T₁ᵣ sta sulla traccia del piano:
3. quindi r appartiene ad α,
4. e P, che sta su r, appartiene ad α.

La caratteristica dei piani verticali è che la prima proiezione di tutto ciò che giace sul piano coincide con la prima traccia: una retta, un triangolo, un cerchio su un piano verticale, visti dall'alto, si riducono a una linea.

La coincidenza c'è solo sulla prima traccia; la quota del punto non cambia tra la seconda e la terza proiezione.

> [!example] Disegno 12 · Il disegno: il piano proiettante in prima e il punto P
> ![[04-piano-proiettante-in-prima.svg|620]]
>
> 1. t₁α è inclinata, t₂α parte dallo stesso punto della LT ed è perpendicolare alla LT (angolo retto).
> 2. Dove t₁α incontra la verticale si porta l'aggetto con l'arco sulla LT: da lì sale t₃α, verticale.
> 3. P₁ sta su t₁α. Per P passa la retta verticale r: r₁ ≡ T₁ᵣ ≡ P₁ sta su t₁α, quindi r appartiene ad α e P appartiene ad α.
> 4. P₂ e P₃ hanno la stessa quota; P₃ non sta su t₃α.
>
> ![[04-spazio-piano-proiettante-in-prima.svg|560]]
>
> Nello spazio: α è un cartoncino in piedi, girato rispetto a π₂; visto dall'alto si riduce alla linea t₁α.

### Una figura nel piano proiettante in prima

Un quadrato disposto con il suo piano verticale, in pianta, è una linea: appartiene a un piano proiettante in prima, e la sua prima proiezione coincide con t₁α.

Proiettandolo sul secondo piano, la figura non corrisponde a quella reale, perché è il risultato di una proiezione tra piani non paralleli tra loro: appare più stretta, più piccola. In terza proiezione è ancora più scorciata. La sua vera grandezza non è nessuna delle due.

Le figure, a seconda di come sono disposte, appartengono a piani diversi.

> [!example] Disegno 13 · Il disegno: il quadrato nel piano proiettante in prima
> ![[04-quadrato-piano-proiettante-in-prima.svg|620]]
>
> 1. In prima proiezione il quadrato è un segmento su t₁α (A₁ ≡ D₁, B₁ ≡ C₁).
> 2. In seconda proiezione si sale da A₁ e B₁ con le linee di richiamo: l'altezza è vera, la larghezza è ridotta.
> 3. In terza proiezione si portano gli aggetti con gli archi e si riportano le quote: il rettangolo è ancora più stretto.

> [!abstract] Da ricordare: i piani nelle varie posizioni
> | Piano | Posizione | t₁ | t₂ | t₃ |
> |---|---|---|---|---|
> | parallelo alla LT (α) | parallelo alla LT, inclinato su π₁ e π₂ | parallela alla LT | parallela alla LT | inclinata |
> | frontale (β) | parallelo a π₂ | parallela alla LT (dà l'aggetto) | all'infinito (t₂β∞) | verticale |
> | orizzontale (γ) | parallelo a π₁ | all'infinito (t₁γ∞) | parallela alla LT | sulla stessa orizzontale di t₂ |
> | di profilo (δ) | parallelo a π₃ | perpendicolare alla LT | perpendicolare alla LT (stessa linea di t₁) | all'infinito (t₃δ∞) |
> | proiettante in prima (α) | perpendicolare a π₁, inclinato su π₂ | inclinata | perpendicolare alla LT | verticale |
>
> - La traccia del piano è una retta: t minuscola, numero del piano, lettera greca (t₁α).
> - Piani verticali: la prima proiezione di tutto ciò che sta sul piano coincide con la prima traccia.

## LE CONDIZIONI DI APPARTENENZA

### Punto, retta e piano

Le condizioni di appartenenza si mettono in fila.

1. Un punto appartiene a una retta quando le proiezioni del punto appartengono alle proiezioni della retta: P₁ deve stare su r₁ e P₂ su r₂ (era già stato detto la volta precedente).
2. Una retta appartiene a un piano quando le tracce della retta appartengono alle rispettive tracce del piano: è quello che si è fatto costruendo ogni piano per la sua retta:
    - T₃ᵣ su t₃α nel piano parallelo alla linea di terra,
    - T₁f su t₁β nel frontale,
    - T₂ₒ su t₂γ nell'orizzontale.
3. Un punto appartiene a un piano se appartiene a una retta del piano.

Bisogna fare attenzione a non confondere la proiezione con la traccia: le condizioni sulla retta e sul piano parlano di tracce, quella sul punto e sulla retta parla di proiezioni.

### Regola e coincidenza

Nei piani particolari ci sono delle coincidenze, cose abbastanza normali, che vanno distinte dalla regola:

- nei piani verticali la prima proiezione di un punto del piano cade sempre sulla prima traccia;
- nel piano di profilo le proiezioni di un punto della retta cadono sulle proiezioni della retta ma anche sulle tracce del piano, e per vedere una figura serve la terza proiezione;
- nel piano parallelo alla linea di terra, come si vedrà nell'esercizio, tutte le terze proiezioni coincidono con la terza traccia.

La regola resta però una sola: il punto appartiene al piano perché appartiene a una retta del piano.

> [!abstract] Da ricordare: le tre condizioni di appartenenza
> - Punto/retta: P ∈ r se P₁ ∈ r₁ e P₂ ∈ r₂.
> - Retta/piano: r ∈ α se le tracce di r stanno sulle rispettive tracce di α (T₁ᵣ ∈ t₁α, T₂ᵣ ∈ t₂α, T₃ᵣ ∈ t₃α).
> - Punto/piano: P ∈ α se P appartiene a una retta di α.
> - Le coincidenze (P₁ su t₁α nei piani verticali, terze proiezioni su t₃α nel piano parallelo alla LT) non sono la regola.

Per esercitarsi, nel foglio PO_riepilogo_1 della docente ci sono due esercizi su questi casi:

- "Dato il piano α, indicare un punto che appartiene al piano" (un piano proiettante in prima: nella soluzione si usa un'orizzontale o con T₂ₒ su t₂α, o₂ parallela alla LT, o₁ ≡ t₁α e T₁ₒ∞)
- e "Date le proiezioni della retta, individuarne le tracce. Indicare un punto P che appartiene alla retta" (una retta proiettante in prima: r₁ ≡ T₁ᵣ ≡ P₁ e T₂ᵣ∞).

Gli altri esercizi dei fogli PO_condizioni di appartenenza 1 e 2 riguardano soprattutto il piano generico, che si fa nelle lezioni successive.

## ESERCIZIO: LA FIGURA NEL PIANO PARALLELO ALLA LINEA DI TERRA

### La terza proiezione della figura

L'esercizio si fa direttamente sul foglio: è data una figura ABCD, in prima e seconda proiezione, leggermente sollevata rispetto alla linea di terra; bisogna trovarne la terza proiezione e dire a che tipo di piano appartiene.

Si segue un punto alla volta:

1. si proietta A fino alla linea di intersezione (la verticale),
2. si fa l'arco di circonferenza,
3. si sale alla quota di A
4. e si scrive A₃.

B ha lo stesso aggetto e la stessa quota di A, quindi B₃ coincide con A₃; allo stesso modo C₃ coincide con D₃.

La terza proiezione è un segmento: la figura appartiene a un piano parallelo alla linea di terra.

La risposta alla domanda sta nel disegno, che deve avere tutte le lettere e non va tratteggiato.

Trovare la terza traccia di questo piano è molto facile: la terza proiezione della figura sta già tutta sulla terza traccia, perché nel piano parallelo alla linea di terra tutte le terze proiezioni coincidono con la terza traccia, come nel piano verticale tutte le prime proiezioni coincidono con la prima traccia.

La figura potrebbe essere la falda di un tetto.

> [!example] Disegno 14 · Il disegno: la terza proiezione della figura ABCD
> ![[04-esercizio-figura-piano-parallelo-alla-lt.svg|620]]
>
> 1. Si ricopiano le proiezioni date: A₁B₁D₁C₁ sotto la LT, A₂B₂D₂C₂ sopra, con AB e CD paralleli alla LT.
> 2. Da A₁ in orizzontale fino alla verticale, arco fino alla LT a destra, si sale alla quota di A₂: A₃. B₃ ≡ A₃.
> 3. Lo stesso per C e D: C₃ ≡ D₃.
> 4. Il segmento A₃C₃ sta sulla terza traccia: prolungandolo si trova t₃α.

### Il compito per casa: le tracce del piano

A casa, sul taccuino, bisogna individuare le rette che compongono la figura: i lati sono segmenti, ma stanno su rette, e sono di due tipi già visti:

- AB e CD sono rette parallele alla linea di terra,
- AC e BD sono rette di profilo.

Con le condizioni di appartenenza se ne trovano le tracce, e quindi le tracce del piano. Il concetto è passare dalla figura ai piani, per poterli poi ribaltare.

> [!example] Disegno 15 (proposto, non fatto a lezione): le tracce del piano della figura ABCD
> ![[b04-tracce-del-piano-della-figura.svg|620]]
>
> 1. AB e CD sono parallele alla LT: la loro unica traccia propria è la terza, A₃ ≡ B₃ e C₃ ≡ D₃, che stanno su t₃α.
> 2. AC è la retta di profilo r: prolungando la sua terza proiezione (che sta su t₃α) si trova (T₂ᵣ)₃ sulla verticale e (T₁ᵣ)₃ sulla LT.
> 3. Da (T₂ᵣ)₃ si va in orizzontale fino al prolungamento di A₂C₂: lì c'è T₂ᵣ. Da (T₁ᵣ)₃ si torna con l'arco sulla verticale e si va in orizzontale fino al prolungamento di A₁C₁: lì c'è T₁ᵣ.
> 4. Lo stesso per BD (retta s): T₂ₛ e T₁ₛ.
> 5. t₂α passa per T₂ᵣ e T₂ₛ, t₁α per T₁ᵣ e T₁ₛ: tutte e due parallele alla LT, come deve essere nel piano parallelo alla linea di terra.

Un esercizio simile è il terzo del foglio PO_condizioni di appartenenza_2 ("Data la figura in prima proiezione e le tracce del piano, disegnare la seconda proiezione della figura"): il piano è parallelo alla linea di terra, A₁ e C₁ stanno su t₁α, quindi A₂ e C₂ cadono sulla linea di terra.

## LA CORREZIONE DELL'ESERCIZIO DI OMOLOGIA

### Trovare la retta corrispondente

Nell'esercizio guidato di omologia bisognava trovare la retta s′ corrispondente di s, con il centro U, l'asse all'infinito e le rette corrispondenti r e r′ parallele (si incontrano sull'asse, che è all'infinito).

Basta la regola fondamentale:

- i punti corrispondenti sono allineati con il centro,
- le rette corrispondenti si incontrano sull'asse.

Prima di tutto serve una coppia di punti corrispondenti. Prendere un punto qualsiasi su r non è sbagliato, ma è più rapido usare il punto P comune a s e r: il suo corrispondente P′ sta sul raggio da U per P e appartiene sia a r′ sia a s′ (sono solo le condizioni di appartenenza).

Poi basta costruire per P′ la parallela a s.

Meno linee si tracciano, meno l'errore grafico è in agguato; per verificare si può usare un'altra coppia di punti, ma la retta s′ è una e una sola.

> [!example] Disegno 16 · Il disegno: trovare s′
> ![[04-omologia-retta-corrispondente.svg|620]]
>
> 1. Si prolunga r fino a s: il punto comune è P.
> 2. Il raggio da U per P incontra r′ (prolungata) in P′.
> 3. L'asse è all'infinito: s′ è la parallela a s per P′.
> 4. Verifica (in blu): con un altro punto M di s e una retta per M e A si trova M′, che cade su s′.

### La figura corrispondente

Nell'ultimo esercizio sono dati la direzione del centro, l'asse e la coppia di rette, e la figura ha un vertice proprio sulla retta r:

1. il suo corrispondente si trova su r′, andando nella direzione del centro.
2. Poi si prolunga un lato fino all'asse e si trova il lato corrispondente, che passa per il punto sull'asse e per il vertice già trovato;
3. il vertice successivo sta su quel lato, nella direzione del centro.

È la costruzione per punti, che viene con l'esperienza. Per le regole dell'omologia si veda la bozza [[02-proiezioni-e-omologia-schema]].

> [!example] Disegno 17 · Il disegno: la figura corrispondente
> ![[04-omologia-figura-corrispondente.svg|620]]
>
> 1. A sta su r: A′ sta su r′, nella direzione di U∞.
> 2. Si prolunga AB fino all'asse u; il lato A′B′ passa per quel punto e per A′. B′ sta nella direzione di U∞ da B.
> 3. Allo stesso modo si trovano D′ (con il lato AD) e C′ (con il lato DC).
> 4. Controllo: i lati corrispondenti si incontrano tutti sull'asse.

## COME LAVORARE SUL TACCUINO

La docente ha insistito molto sul modo di disegnare.

- Le proiezioni si fanno prima sul modello e poi sul foglio degli appunti, aprendo il modello e ricopiando quello che si vede, senza vignette separate.
- I disegni devono essere grandi, sia le proiezioni sia lo schema tridimensionale: non più di quattro disegni per pagina, accurati, con tracce, proiezioni e scritte grandi.
- La retta va distinta dalle costruzioni, che devono essere più leggere.
- Le lettere sono obbligatorie: nelle esercitazioni, un disegno senza lettere viene considerato un errore.

Il taccuino verrà controllato.

> [!tip] Avvisi e consegne
> - Portare sempre fogli di cartoncino: servono per costruire i piani nel modello.
> - Per casa (13 ottobre): nella figura dell'esercizio, individuare le rette dei lati (due parallele alla LT, due di profilo) e trovare le tracce del piano con le condizioni di appartenenza.
> - Prova sull'omologia: giovedì 29 ottobre (Prova n. 1 nel calendario; nella registrazione la frase si sente solo a metà).
> - Compito su rette e piani (assegnato il 16 ottobre, foglio "assegno su rette e piani e modello", sette fogli in tutto): per ogni elemento un foglio con tre riquadri, la fotografia del modello con l'elemento geometrico e le proiezioni, la fotografia del modello aperto con le proiezioni, e il disegno con l'elemento nella stessa posizione del modello; nel modello si usa un'asta di legno per le rette. Nell'esempio della docente: retta proiettante in prima (r₁ ≡ T₁ᵣ, r₂ e r₃ con T₂ᵣ∞ e T₃ᵣ∞) e piano proiettante in prima (t₁α, t₂α, t₃α). In alto nome e cognome e anno accademico (se di altri anni accademici).

## Collegamenti

Questa lezione prosegue direttamente quella sul punto e sulle rette proiettanti ([[03-proiezioni-ortogonali-punto-e-rette]]), da cui riprende la condizione di appartenenza del punto alla retta, il metodo delle tracce e l'uso degli archi per portare l'aggetto sul terzo piano.

Le rette frontale e orizzontale, presentate qui come rette notevoli, diventano gli strumenti principali nella lezione successiva ([[05-appartenenza-e-rette-ausiliarie]]), dove servono come rette ausiliarie per verificare l'appartenenza di un punto a un piano generico; da lì si passa ai piani ausiliari e alla perpendicolarità ([[06-piani-ausiliari-e-perpendicolarita]]).

Il passaggio "dalla figura ai piani", con cui la docente chiude l'esercizio sulla figura nel piano parallelo alla linea di terra, prepara il ribaltamento dei piani proiettanti ([[07-il-ribaltamento]]), che serve a vedere le figure in vera grandezza; il quadrato nel piano proiettante in prima, che non appare mai in vera grandezza nelle tre proiezioni, ne è la motivazione.

La correzione dell'esercizio guidato rimanda all'omologia ([[02-proiezioni-e-omologia-schema]]), che tornerà proprio come omologia di ribaltamento. Le regole sul disegno (strumenti, segno, lettere) sono quelle della prima lezione ([[01-strumenti-materiali-e-regole]]).

Il testo completo della lezione è nella sbobina [[04-rette-e-piani-metodo-di-monge]]; il seguito è nella sbobina [[05-piani-rette-e-appartenenza]].

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[ARGOMENTI LEZIONI 26-27.pdf]]: elenco degli argomenti della lezione
- [[PO_riepilogo_1.pdf]]: esercizi su punto, rette e piani
- [[PO_riepilogo_1_soluzione.pdf]]: soluzioni della docente
- [[PO_condizioni di appartenenza_1.pdf]]: esercizi sulle condizioni di appartenenza
- [[PO_condizioni di appartenenza_1_soluzione.pdf]]: soluzioni della docente
- [[PO_condizioni di appartenenza_2.pdf]]: altri esercizi di appartenenza
- [[PO_condizioni di appartenenza_2_soluzione.pdf]]: soluzioni della docente
- [[assegno su rette e piani e modello.pdf]]: il compito con il modello (sette fogli)
- [[taccuino-marta-07-rette-orizzontale-frontale-di-profilo.jpg]]: foto del taccuino di Marta
- [[Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: data della Prova n. 1
