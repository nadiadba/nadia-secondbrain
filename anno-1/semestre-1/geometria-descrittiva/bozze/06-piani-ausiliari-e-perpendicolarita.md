---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-20
tags: [geometria-descrittiva, bozza]
---

# Piani ausiliari, figure piane e perpendicolarità

> [!info] Note collegate
> Sbobina: [[06-piani-proiettanti-orizzontali-frontali]]
>
> Bozza precedente: [[05-appartenenza-e-rette-ausiliarie]] · Successiva: [[07-il-ribaltamento]]

La lezione di martedì 20 ottobre riprende le condizioni di appartenenza e le mette al lavoro. Il punto di partenza è che per risolvere quasi tutti i problemi della geometria descrittiva ci si appoggia a pochi strumenti fatti apposta per aiutarci: due piani ausiliari, il proiettante in prima e il proiettante in seconda, e due rette ausiliarie, l'orizzontale e la frontale. Con questi strumenti si disegna un punto che appartiene a un piano, si riconosce in che piano sta una figura piana disegnata nelle sue due proiezioni, si ricavano le tracce del piano a partire dalla figura e si costruiscono rette e piani perpendicolari a un piano dato. La lezione si chiude con il modellino del piano mobile, che prepara il ribaltamento della lezione successiva, e con la presentazione delle due case da studiare durante il corso, Villa Tugendhat e Villa Le Lac, insieme alle indicazioni per il raccoglitore.

## I PIANI AUSILIARI E LE RETTE AUSILIARIE

### Quali sono e perché servono

I piani ausiliari sono il piano proiettante in prima e il piano proiettante in seconda; le rette che si usano allo stesso scopo sono le orizzontali e le frontali. La docente insiste su un punto: queste rette vanno disegnate in modo immediato, senza esitazioni, perché servono per qualunque cosa. L'orizzontale ha la seconda proiezione parallela alla linea di terra e la prima traccia all'infinito; la frontale ha la prima proiezione parallela alla linea di terra e la seconda traccia all'infinito.

Della retta bisogna conoscere le tracce: fatto questo si risolve qualunque questione. Nella forma mongiana, infatti, la retta è definita dai suoi due punti notevoli, che sono appunto le tracce, e la condizione di appartenenza dice che una retta appartiene a un piano se le sue tracce appartengono alle rispettive tracce del piano.

### Un punto che appartiene a un piano generico

Per disegnare un punto che appartiene a un piano generico α, dato con le sue tracce t₁α e t₂α, si parte dalla regola: un punto appartiene al piano se appartiene a una retta del piano. Si disegna quindi una retta del piano, e la più comoda è l'orizzontale. La sua seconda traccia sta su t₂α; la prima traccia è all'infinito, e per stare su t₁α deve averne la direzione: per questo la prima proiezione dell'orizzontale è parallela a t₁α. Su questa orizzontale si sceglie un punto e se ne disegnano le proiezioni.

> [!example] Il disegno
> ![[06-punto-piano-generico-orizzontale.svg|620]]
>
> 1. Disegna le tracce del piano generico α, che partono dallo stesso punto della LT: t₂α sopra, t₁α sotto.
> 2. Traccia o₂ parallela alla LT, all'altezza che vuoi. Dove incontra t₂α c'è T₂ₒ, la seconda traccia dell'orizzontale.
> 3. Da T₂ₒ scendi con il richiamo fino alla LT: trovi (T₂ₒ)₁.
> 4. Da (T₂ₒ)₁ traccia o₁ parallela a t₁α (la prima traccia T₁ₒ è all'infinito).
> 5. Scegli P₂ su o₂ e scendi con il richiamo fino a o₁: lì c'è P₁. P appartiene ad α perché sta su una retta di α.

### Un punto che appartiene ai piani proiettanti

La stessa regola vale per i piani proiettanti, con una scorciatoia. Il piano proiettante in prima è verticale e c'è una coincidenza da non dimenticare: la prima proiezione di tutti gli elementi che gli appartengono coincide con la prima traccia. Il piano proiettante in seconda ha la prima traccia perpendicolare alla linea di terra e la seconda inclinata a piacere; tutto ciò che gli appartiene ha la seconda proiezione sulla seconda traccia. Per disegnarvi un punto basta quindi mettere P₂ sulla seconda traccia e P₁ a qualunque distanza sulla stessa linea di richiamo.

Per verificare che il punto appartiene davvero al piano si usa una frontale: ha la prima proiezione parallela alla linea di terra, la sua prima traccia si fa coincidere con un punto della prima traccia del piano, la seconda traccia è all'infinito e la seconda proiezione coincide con la seconda traccia del piano. Il punto sta sulla frontale, e quindi sul piano.

> [!example] Il disegno
> ![[06-piano-proiettante-in-seconda-frontale.svg|620]]
>
> 1. Disegna il piano β proiettante in seconda: t₁β perpendicolare alla LT, t₂β inclinata.
> 2. Metti P₂ su t₂β e P₁ in un punto qualunque della stessa linea di richiamo.
> 3. Verifica con la frontale f: f₁ parallela alla LT per P₁, che incontra t₁β in T₁f.
> 4. f₂ coincide con t₂β e la seconda traccia è all'infinito (T₂f∞): P sta su f, f sta su β.

> [!abstract] Da ricordare
> - Un punto appartiene a un piano se appartiene a una retta del piano.
> - Una retta appartiene a un piano se le sue tracce appartengono alle tracce omonime del piano.
> - Orizzontale di un piano: seconda proiezione parallela alla LT, prima proiezione parallela a t₁ del piano.
> - Frontale di un piano: prima proiezione parallela alla LT, seconda proiezione parallela a t₂ del piano.
> - Piano proiettante in prima: tutto ciò che vi appartiene ha la prima proiezione sulla prima traccia.
> - Piano proiettante in seconda: tutto ciò che vi appartiene ha la seconda proiezione sulla seconda traccia.

## IL PIANO DATO DA UNA FIGURA: LA FORMA TECNICA

### Forma mongiana e forma tecnica

Finora i piani sono stati considerati nella loro estensione, attraverso le tracce, cioè le loro intersezioni con i piani di proiezione. Ma un piano può essere rappresentato da qualunque figura piana, per esempio da un triangolo: tre punti individuano un piano, e il triangolo disegnato nelle sue due proiezioni è già il piano. Questa è la forma tecnica, quella del disegno di architettura, in cui una retta non si rappresenta con le sue tracce: quando si disegna una casa non si usano tutti i piani (servono, per esempio, quando si progettano le terrazze), e non è sempre necessario avere le tracce. Le due forme non sono due cose diverse: si può lavorare con le tracce o senza, è indifferente.

Per disegnare un punto che appartiene alla figura si ragiona come prima, senza inventare procedimenti propri: serve una retta che stia sul piano, e le rette che aiutano sono l'orizzontale e la frontale.

### Riconoscere le rette dei lati

Prima di tutto bisogna capire in che piano sta la figura, e per farlo si guardano le rette a cui appartengono i lati. Un lato è un segmento, e il segmento appartiene a una retta: se una proiezione contiene due lettere, l'altra proiezione contiene le stesse lettere. Se di un lato si vedono entrambe le proiezioni inclinate rispetto alla linea di terra, la retta è generica; se tutti e tre i lati stanno su rette generiche, il piano che contiene la figura è un piano generico.

### I punti notevoli della retta generica sulla linea di terra

La retta, a differenza del segmento, è estesa: per lavorare con una retta generica bisogna prolungarne le proiezioni. Prolungando la seconda proiezione fino alla linea di terra si trova un punto preciso, che ha un nome: la seconda proiezione della prima traccia, (T₁)₂. Non è la traccia, perché la retta non incide la linea di terra; ma sapendo che cos'è, basta scendere con la perpendicolare alla linea di terra fino alla prima proiezione per trovare T₁, il punto in cui la retta buca π₁. Allo stesso modo, prolungando la prima proiezione fino alla linea di terra si trova la prima proiezione della seconda traccia, (T₂)₁, e salendo fino alla seconda proiezione si trova T₂.

Il motivo è sempre lo stesso: le tracce sono i punti in cui la retta buca i piani di proiezione, e le proiezioni delle tracce finiscono sempre sulla linea di terra (o sulla retta di proiezione della terza). Ogni punto va chiamato con il suo nome: non si dice "il punto sulla linea dove va la proiezione", ma prima o seconda proiezione di una traccia.

> [!example] Il disegno
> ![[06-retta-generica-punti-notevoli.svg|620]]
>
> 1. La retta generica r ha tutte e due le proiezioni inclinate rispetto alla LT.
> 2. Prolunga r₂ fino alla LT: trovi (T₁ᵣ)₂, la seconda proiezione della prima traccia.
> 3. Da (T₁ᵣ)₂ scendi con il richiamo fino a r₁: lì c'è T₁ᵣ.
> 4. Prolunga r₁ fino alla LT: trovi (T₂ᵣ)₁, la prima proiezione della seconda traccia.
> 5. Da (T₂ᵣ)₁ sali con il richiamo fino a r₂: lì c'è T₂ᵣ.

La retta disegnata così è quella canonica, ma la retta può avere altre direzioni, e allora le tracce non stanno per forza come prima. Una retta può non bucare né π₁ né π₂ dalla parte del modello e bucarli sotto la linea di terra; può venire da fuori; oppure può essere alta e bucare prima π₂, poi π₁, poi π₃. La posizione delle tracce dipende dalla direzione della retta: si possono trovare tutte e due le tracce sotto o tutte e due sopra. Il procedimento però non cambia, perché le proiezioni della retta passano sempre per quei due punti notevoli sulla linea di terra. Questa configurazione servirà per le ombre, in cui la luce deve venire da fuori; conviene esercitarsi con un disegno a squadra e con il modello.

> [!example] Disegno proposto (non fatto a lezione): una retta con le tracce dall'altra parte
> ![[b06-retta-tracce-sotto-la-lt.svg|600]]
>
> 1. Prolunga r₂ fino alla LT: trovi (T₁ᵣ)₂; scendi con il richiamo fino a r₁ e trovi T₁ᵣ.
> 2. Prolunga r₁ fino alla LT: trovi (T₂ᵣ)₁; il richiamo verso r₂ questa volta va in giù, e T₂ᵣ cade sotto la LT.
> 3. Le due tracce sono entrambe sotto la LT, ma i punti notevoli e il procedimento sono gli stessi.

> [!abstract] Da ricordare
> - (T₁)₂ = seconda proiezione della prima traccia: si trova prolungando la seconda proiezione della retta fino alla LT.
> - (T₂)₁ = prima proiezione della seconda traccia: si trova prolungando la prima proiezione fino alla LT.
> - Dal punto notevole, con il richiamo, si arriva sull'altra proiezione e si trova la traccia vera.

### L'orizzontale della figura

Per disegnare rapidamente una retta che appartiene al piano del triangolo si sceglie un'orizzontale, costruita in forma tecnica sfruttando il fatto che la retta passa per punti della figura. Si parte da A₂ e si traccia la seconda proiezione parallela alla linea di terra: dentro la figura incontra il lato B₂C₂ in un punto che si chiama H₂. Con il richiamo si trova H₁ su B₁C₁, e la prima proiezione dell'orizzontale, o₁, è la retta che passa per A₁ e H₁. Qualunque punto preso sull'orizzontale appartiene al piano. Allo stesso modo si può costruire una frontale.

Le orizzontali sono importanti anche in architettura. Per sapere qual è la pendenza di un piano, per esempio in che direzione mettere le tegole di una falda, bisogna trovare le orizzontali: le tegole sono perpendicolari alla gronda, che di solito è orizzontale, e la parte più bassa del piano dipende dalla sua inclinazione. Si trova quindi un'orizzontale del piano e poi la perpendicolare, argomento ripreso nella lezione successiva.

> [!example] Il disegno
> ![[06-orizzontale-nel-triangolo.svg|560]]
>
> 1. Il triangolo ABC ha i tre lati su rette generiche: il piano è generico ed è dato in forma tecnica, senza tracce.
> 2. Da A₂ traccia o₂ parallela alla LT: incontra B₂C₂ in H₂.
> 3. Scendi con il richiamo da H₂ fino a B₁C₁: lì c'è H₁.
> 4. Traccia o₁ per A₁ e H₁.
> 5. Prendi un punto P su o (P₂ su o₂, P₁ su o₁ con il richiamo): P appartiene al piano del triangolo.

### Dalle proiezioni della figura alle tracce del piano

Se si hanno le tracce si possono disegnare le proiezioni della figura, e se si hanno le proiezioni si possono trovare le tracce. La regola da scrivere è questa: le tracce di un piano generico contengono le tracce delle rette che compongono la figura, cioè dei lati che la limitano. I lati sono segmenti, i segmenti appartengono a rette, quindi la prima traccia del piano contiene le prime tracce delle rette dei lati e la seconda traccia del piano ne contiene le seconde tracce.

Per ogni lato si fa quello che si è visto per la retta generica: si prolunga la seconda proiezione fino alla linea di terra e si trova la seconda proiezione della prima traccia, si prolunga la prima proiezione e si trova la prima proiezione della seconda traccia, e con i richiami si arriva alle tracce vere. Bastano due lati, perché la traccia di un piano è una retta e per una retta bastano due punti; la terza retta, se si trova, serve solo da controllo, e le cose tornano. Le tracce non sono però sempre utili, perché spesso finiscono lontano.

> [!example] Il disegno
> ![[06-tracce-dal-triangolo-generico.svg|660]]
>
> 1. Chiama r, s e m le rette dei lati AB, BC e AC: sono tutte generiche.
> 2. Retta r: prolunga A₂B₂ fino alla LT e trovi (T₁ᵣ)₂; scendi fino ad A₁B₁ prolungata e trovi T₁ᵣ. Prolunga A₁B₁ fino alla LT e trovi (T₂ᵣ)₁; sali fino ad A₂B₂ prolungata e trovi T₂ᵣ.
> 3. Ripeti con la retta s del lato BC: trovi T₁ₛ e T₂ₛ.
> 4. Traccia t₁α per T₁ᵣ e T₁ₛ, e t₂α per T₂ᵣ e T₂ₛ: le due tracce si incontrano sulla LT.
> 5. Controllo: anche le tracce di m (lato AC) cadono su t₁α e t₂α.

> [!abstract] Da ricordare
> - Le tracce di un piano contengono le tracce delle rette dei lati della figura.
> - Per la prima traccia del piano servono le prime tracce di due rette; per la seconda, le seconde tracce di due rette.
> - Un punto all'infinito è una direzione: una retta si costruisce anche con un punto proprio e un punto improprio.

### L'esercizio: un triangolo con un lato orizzontale e uno frontale

L'esercizio svolto in aula, a mano libera nella metà superiore del foglio, usa un triangolo più semplice. Una figura non è di per sé un piano generico: è un triangolo messo in una posizione qualunque, che appartiene a un piano. Il triangolo dato ha un lato orizzontale, AB, con A₂B₂ parallelo alla linea di terra, e un lato frontale, AC, con A₁C₁ parallelo alla linea di terra. La richiesta è doppia: trovare le tracce del piano generico che contiene la figura e poi ridisegnare la stessa figura come se appartenesse a un piano proiettante in prima.

Lavorando su un lato bisogna immaginare che esista solo quel segmento: l'orizzontale contiene A e B, quindi o₂ passa per A₂ e B₂ e o₁ per A₁ e B₁; la frontale contiene A e C, quindi f₁ passa per A₁ e C₁ e f₂ per A₂ e C₂. Prolungando o₂ si trova la seconda traccia dell'orizzontale, e va segnato anche il suo punto all'infinito, che è fondamentale perché dice da dove far passare la prima traccia. Prolungando f₂ fino alla linea di terra e scendendo su f₁ si trova la prima traccia della frontale, con la seconda all'infinito. Il terzo lato, BC, sta su una retta di cui non si possono trovare le tracce se non costruendo la terza proiezione, ma non serve: per le tracce del piano bastano due punti.

La prima traccia del piano deve passare per la prima traccia della frontale e contenere il punto all'infinito dell'orizzontale, quindi è parallela a o₁; la seconda traccia deve passare per la seconda traccia dell'orizzontale e contenere il punto all'infinito della frontale, quindi è parallela a f₂. Si ottiene così il piano generico che contiene la figura, che si può colorare per farla risaltare. La vera forma del triangolo, invece, richiede operazioni che si vedono più avanti.

> [!example] Il disegno
> ![[b06-triangolo-lato-di-profilo.svg|600]]
>
> 1. Riconosci i lati: AB orizzontale (A₂B₂ ∥ LT), AC frontale (A₁C₁ ∥ LT), BC di profilo (B₂C₂ e B₁C₁ perpendicolari alla LT).
> 2. Orizzontale o: prolunga o₂ e trova T₂ₒ (con (T₂ₒ)₁ dove o₁ taglia la LT); segna T₁ₒ∞ nella direzione di o₁.
> 3. Frontale f: prolunga f₂ fino alla LT, trova (T₁f)₂ e scendi su f₁: lì c'è T₁f; segna T₂f∞ nella direzione di f₂.
> 4. t₂γ passa per T₂ₒ ed è parallela a f₂.
> 5. t₁γ passa per T₁f ed è parallela a o₁.
> 6. Controllo: t₁γ e t₂γ si incontrano sulla LT.

### La stessa figura nel piano proiettante in prima

Se invece la stessa figura appartiene a un piano proiettante in prima, si sa che tutto ciò che sta sul piano ha la prima proiezione coincidente con la prima traccia: la seconda proiezione si può disegnare come prima, ma la prima proiezione si schiaccia sulla traccia. Il confronto mostra che non è la figura in sé a essere generica: a seconda di come la si colloca nel modello, lo stesso triangolo può stare in un piano verticale, frontale, orizzontale, proiettante in prima o generico. Il lato BC, che nel piano generico era una retta di profilo, nel piano proiettante in prima non lo è più. Le condizioni di appartenenza restano naturalmente rispettate.

> [!example] Il disegno
> ![[06-triangolo-piano-proiettante-in-prima.svg|560]]
>
> 1. Disegna il piano δ proiettante in prima: t₂δ perpendicolare alla LT, t₁δ inclinata a piacere.
> 2. Riporta la seconda proiezione del triangolo come nell'esercizio precedente.
> 3. Con i richiami porta A, B e C su t₁δ: A₁ e B₁ cadono sulla traccia, e C₁ coincide con B₁.
> 4. BC diventa una retta proiettante in prima; AB resta orizzontale.

## LA FIGURA NELLE DIVERSE POSIZIONI E I SOLIDI

### Il piano non è generico di per sé

Un piano non è generico di per sé: lo è in relazione alla posizione che assume rispetto ai piani di proiezione. Lo stesso triangolo, spostato nel modello, cambia aspetto. Se la sua seconda proiezione si riduce a una linea parallela alla linea di terra (A₂ coincide con B₂ e con C₂ sulla stessa retta), il triangolo appartiene a un piano orizzontale: si segna t₂γ e subito sotto t₁γ all'infinito. Se la seconda proiezione si riduce a una linea che non è parallela alla linea di terra, il piano non è orizzontale e nemmeno frontale (nel frontale è la prima proiezione a essere una linea): è un piano proiettante in seconda, con la prima traccia perpendicolare alla linea di terra. Se è la prima proiezione a ridursi a una linea inclinata, il piano è verticale, cioè proiettante in prima; se la prima proiezione è una linea parallela alla linea di terra, il piano è frontale.

Solo in alcune di queste posizioni il disegno corrisponde alle misure vere della figura. Nel piano frontale la seconda proiezione è in vera grandezza: il piano che contiene la figura e il piano su cui si proietta sono paralleli, il centro di proiezione è all'infinito, l'asse dell'omologia è all'infinito, e la figura si riproduce esattamente, come in una traslazione intesa come rapporto omologico tra due figure. Per il frontale si segna t₁γ e subito t₂γ all'infinito: vanno sempre scritte tutte e due le tracce, anche se si sovrappongono, perché mettendole vicine si riconosce subito il piano. Le altre configurazioni in vera grandezza sono il piano orizzontale, come nella pianta, con la prima proiezione, e il piano di profilo, con la terza: sono quelle usate di più in architettura. Ma non tutto ciò che si disegna è ad angolo retto, e nei piani proiettanti la figura appare accorciata; come si recuperi la vera forma si vede nella lezione successiva.

> [!example] Il disegno
> ![[06-triangolo-quattro-posizioni.svg|700]]
>
> 1. Piano orizzontale: la seconda proiezione è un segmento su t₂γ, parallelo alla LT; la prima proiezione è in vera forma.
> 2. Piano proiettante in seconda: A₂, B₂ e C₂ stanno su t₂β inclinata; t₁β è perpendicolare alla LT; nessuna proiezione è in vera forma.
> 3. Piano proiettante in prima: A₁, B₁ e C₁ stanno su t₁δ inclinata; t₂δ è perpendicolare alla LT.
> 4. Piano frontale: la prima proiezione è un segmento su t₁ε, parallelo alla LT; la seconda proiezione è in vera forma.

> [!abstract] Da ricordare
> - Seconda proiezione ridotta a una linea parallela alla LT: piano orizzontale. Inclinata: proiettante in seconda.
> - Prima proiezione ridotta a una linea parallela alla LT: piano frontale. Inclinata: proiettante in prima.
> - Entrambe le proiezioni ridotte a linee: piano di profilo.
> - Due proiezioni "piene": piano generico oppure piano parallelo alla LT, e per deciderlo si ragiona sulle rette.
> - Vera grandezza: piano orizzontale in prima proiezione, frontale in seconda, di profilo in terza.

### I solidi: facce, spigoli, diedri

I solidi sono delimitati da una serie di facce, che sono figure piane. In una piramide triangolare ci sono tre facce laterali, e il lato comune a due facce è lo spigolo; due facce vicine che si intersecano formano un diedro, cioè una porzione di spazio delimitata da due semipiani. Il solido più usato è il parallelepipedo, le cui facce sono parallelogrammi; nella consuetudine si chiama parallelepipedo il parallelepipedo rettangolo, ma bisognerebbe specificarlo. Il prisma è più vario: è un solido in cui la base inferiore e la base superiore sono due figure piane congruenti e parallele, unite tra loro dalle facce laterali. Congruenti significa che, sovrapposte, coincidono perfettamente. Il parallelepipedo rettangolo è quindi un prisma, ma si può avere anche, per esempio, un prisma a base triangolare.

> [!example] Il disegno
> ![[06-solidi-piramide-prisma-parallelepipedo.svg|700]]
>
> 1. Piramide a base triangolare: tre facce laterali che si incontrano nel vertice.
> 2. Parallelepipedo rettangolo: sei facce rettangolari; ogni spigolo è il lato comune di due facce, che formano un diedro.
> 3. Prisma a base triangolare: base inferiore e base superiore congruenti e parallele, unite dalle facce laterali.

### Esercizio: in che piano sta la base del solido

Il solido disegnato in aula ha una base inferiore, una base superiore parallela e le facce laterali; bisogna usare le stesse lettere della docente, così che "ragioniamo sul segmento AC" sia chiaro a tutti. La base è un piano: in che posizione sta? Prima di rispondere "è generico" perché si vedono due proiezioni, bisogna fare attenzione. Nel frontale e nel proiettante in prima la prima proiezione è una linea, nel proiettante in seconda è la seconda proiezione a essere una linea, nel piano di profilo lo sono tutte e due; ma due proiezioni si vedono sia nel piano generico sia nel piano parallelo alla linea di terra. Per decidere si ragiona ancora una volta sulle rette.

Il segmento AB ha entrambe le proiezioni perpendicolari alla linea di terra: sta su una retta di profilo, di cui è difficile trovare le tracce senza la terza proiezione. Il segmento AC ha entrambe le proiezioni inclinate: sta su una retta generica, e prolungandone le proiezioni fino alla linea di terra si trovano i punti notevoli e quindi le tracce. Per disegnare la prima traccia del piano servono le prime tracce di due rette: una è T₁ di AC, l'altra è un punto all'infinito, che esiste anche se è all'infinito e dà una direzione. La prima traccia passa quindi per T₁ di AC ed è parallela a quella direzione; allo stesso modo si può trovare la seconda traccia. Il disegno va rifatto a casa per esercitare la mano: la geometria descrittiva non è un accidente che capita, e la mano che disegna è governata da ciò che si sa.

> [!example] Il disegno
> ![[06-solido-base-nel-piano-generico.svg|640]]
>
> 1. Il solido è un prisma: base ABC, base superiore DEF parallela e congruente.
> 2. AB: A₂B₂ e A₁B₁ perpendicolari alla LT, quindi retta di profilo.
> 3. AC: proiezioni inclinate, quindi retta generica. Prolunga A₂C₂ fino alla LT, trova (T₁)₂ e scendi su A₁C₁ prolungata: lì c'è T₁ di AC.
> 4. BC: B₂C₂ parallelo alla LT, quindi orizzontale, con T₁∞ nella direzione di B₁C₁ e T₂ propria.
> 5. t₁α passa per T₁ di AC ed è parallela a B₁C₁; t₂α passa per T₂ di BC e per il punto in cui t₁α incontra la LT.

## LA PERPENDICOLARITÀ

### Retta perpendicolare a un piano: il teorema di Monge

Nei richiami di geometria si è detto che una retta è perpendicolare a un piano se è perpendicolare a due rette del piano. Monge traduce questa condizione nelle proiezioni: una retta è perpendicolare a un piano se le proiezioni della retta sono perpendicolari alle rispettive tracce del piano. Per disegnare una retta r perpendicolare al piano α basta quindi costruire r₂ perpendicolare a t₂α e r₁ perpendicolare a t₁α. La retta può essere esterna al piano, come in questo caso, ma la stessa perpendicolarità vale per rette che appartengono al piano.

> [!example] Il disegno
> ![[06-retta-perpendicolare-al-piano.svg|600]]
>
> 1. Parti da un punto P, con le proiezioni P₂ e P₁.
> 2. Da P₂ traccia r₂ perpendicolare a t₂α (segna l'angolo retto).
> 3. Da P₁ traccia r₁ perpendicolare a t₁α (segna l'angolo retto).
> 4. Per il teorema di Monge la retta r è perpendicolare ad α.

> [!example] Disegno proposto (non fatto a lezione): la stessa situazione nello spazio
> ![[b06-spazio-retta-perpendicolare-al-piano.svg|600]]
>
> 1. Il piano α taglia i tre piani di proiezione lungo le tracce t₁α, t₂α e t₃α.
> 2. La retta r per P incontra α nel punto H e forma un angolo retto con il piano.
> 3. Le proiezioni r₁ (su π₁) e r₂ (su π₂) risultano perpendicolari alle tracce t₁α e t₂α.

### Due piani perpendicolari

Due piani sono perpendicolari tra loro se uno dei due contiene una retta perpendicolare all'altro. Con i piani ausiliari la verifica è immediata. Si prenda il quaderno, lo si apra e lo si metta in piedi sul banco: le due metà sono due piani proiettanti in prima, e le loro tracce sul banco sono le prime tracce. Quando le due metà sono ortogonali, l'angolo di 90° sta a terra, sul π₁. Per i piani proiettanti in prima, quindi, non c'è nulla da dimostrare: sono perpendicolari se le prime tracce sono perpendicolari. È un fatto, non un'interpretazione, ma vale solo perché si tratta di due piani particolari; con un piano generico non si può fare. Lo stesso vale per i piani proiettanti in seconda, mettendo il quaderno in modo che siano le seconde tracce a formare l'angolo retto.

Si può comunque verificare che è vero, cercando nel piano δ una retta perpendicolare a γ. Per essere perpendicolare a γ la retta deve avere la seconda proiezione perpendicolare a t₂γ, che è perpendicolare alla linea di terra, quindi r₂ è parallela alla linea di terra: è un'orizzontale. Per appartenere a δ, che è proiettante in prima, deve avere la prima proiezione sulla prima traccia, quindi r₁ coincide con t₁δ, ed è perpendicolare a t₁γ. Il ragionamento è una concatenazione di condizioni già note: δ contiene una retta perpendicolare a γ, e i due piani sono perpendicolari.

> [!example] Il disegno
> ![[06-piani-proiettanti-perpendicolari.svg|560]]
>
> 1. Disegna due piani proiettanti in prima γ e δ, con le seconde tracce perpendicolari alla LT.
> 2. Imponi l'angolo retto tra le prime tracce t₁γ e t₁δ (quelle sul banco, non quelle sopra).
> 3. Verifica: in δ prendi la retta r con r₁ ≡ t₁δ e r₂ parallela alla LT (un'orizzontale).
> 4. r₁ ⊥ t₁γ e r₂ ⊥ t₂γ, quindi r ⊥ γ: δ contiene una retta perpendicolare a γ.

> [!example] Disegno proposto (non fatto a lezione): il quaderno aperto nello spazio
> ![[b06-spazio-piani-perpendicolari.svg|600]]
>
> 1. Le due metà del quaderno sono i piani γ e δ, entrambi verticali.
> 2. L'angolo retto si vede sul banco, tra le prime tracce t₁γ e t₁δ.
> 3. La retta orizzontale r di δ è perpendicolare a γ.

> [!example] Disegno proposto (non fatto a lezione): due piani proiettanti in seconda perpendicolari
> ![[b06-piani-proiettanti-in-seconda-perpendicolari.svg|560]]
>
> 1. Disegna β ed ε proiettanti in seconda: prime tracce perpendicolari alla LT.
> 2. Imponi l'angolo retto tra le seconde tracce t₂β e t₂ε.
> 3. Verifica: in ε prendi la frontale r, con r₂ ≡ t₂ε e r₁ parallela alla LT. r₂ ⊥ t₂β e r₁ ⊥ t₁β, quindi r ⊥ β.

### Un piano perpendicolare a un piano generico

Si può disegnare un piano generico perpendicolare a un piano generico, ma è abbastanza complicato. Serve invece un piano facile, perpendicolare a quello dato, che dimostri anche la proprietà, cioè che contenga una retta perpendicolare all'altro piano; ed è proprio ciò che servirà nei ribaltamenti. Si usa un piano ausiliario γ proiettante in prima, imponendo la regola: t₁γ perpendicolare a t₁α. Il proiettante in prima non va usato in modo acritico, ma in modo cosciente, con questa condizione.

Per dimostrare che α e γ sono perpendicolari vengono in aiuto le rette ausiliarie. Si prende un'orizzontale di α: per appartenere ad α la sua prima proiezione è parallela a t₁α, quindi è perpendicolare a t₁γ, e la sua seconda proiezione, parallela alla linea di terra, è perpendicolare a t₂γ. Disegnando l'orizzontale si vede che quella retta è effettivamente perpendicolare a γ, e quindi i due piani sono perpendicolari.

> [!example] Il disegno
> ![[06-piano-perpendicolare-al-generico.svg|560]]
>
> 1. Dato il piano generico α, disegna il piano ausiliario γ proiettante in prima con t₁γ ⊥ t₁α (segna i 90°); t₂γ è perpendicolare alla LT.
> 2. Verifica con l'orizzontale di α: o₁ ∥ t₁α è perpendicolare a t₁γ, o₂ ∥ LT è perpendicolare a t₂γ, quindi α contiene una retta perpendicolare a γ.
> 3. Nello schema compare anche la verifica inversa: la retta r di γ, con r₁ ≡ t₁γ e r₂ ⊥ t₂α, è perpendicolare ad α.

### Senza tracce: la perpendicolare con l'orizzontale e la frontale

Se il piano è dato da una figura e non si hanno le tracce, bisogna comunque poter costruire una retta perpendicolare al piano. Si torna alla prima definizione: una retta è perpendicolare a un piano quando è perpendicolare a due rette del piano, e le rette che vengono in soccorso sono l'orizzontale e la frontale. La perpendicolare si costruisce imponendo l'angolo retto tra la prima proiezione della retta e la prima proiezione dell'orizzontale, e tra la seconda proiezione della retta e la seconda proiezione della frontale.

Il motivo sta ancora nei piani ausiliari. Se per la retta r si fa passare un piano β proiettante in seconda, la seconda proiezione di r coincide con la seconda traccia di β, che è perpendicolare a f₂; se si fa passare un piano δ proiettante in prima, r₁ coincide con la prima traccia di δ, perpendicolare a o₁. Le proiezioni della retta risultano così perpendicolari alle proiezioni "vere" delle rette del piano. Il disegno va fatto a colori e riguardato, perché sarà ripreso per il ribaltamento: le condizioni sono più facili di quello che sembrano, perché sono tutte collegate.

> [!example] Il disegno
> ![[06-perpendicolare-con-orizzontale-e-frontale.svg|620]]
>
> 1. Nel triangolo ABC individua l'orizzontale o (per A e B, A₂B₂ ∥ LT) e la frontale f (per A e C, A₁C₁ ∥ LT).
> 2. Dal punto Q traccia r₁ perpendicolare a o₁.
> 3. Traccia r₂ perpendicolare a f₂.
> 4. r è perpendicolare a due rette del piano, quindi al piano. Usa colori diversi per o, f e r.

> [!abstract] Da ricordare
> - Teorema di Monge: r ⊥ α se r₁ ⊥ t₁α e r₂ ⊥ t₂α.
> - Due piani sono perpendicolari se uno contiene una retta perpendicolare all'altro.
> - Due piani proiettanti in prima sono perpendicolari se lo sono le prime tracce; due proiettanti in seconda se lo sono le seconde tracce.
> - Piano facile perpendicolare a un generico α: un proiettante in prima γ con t₁γ ⊥ t₁α.
> - Senza tracce: r ⊥ piano se r₁ ⊥ o₁ e r₂ ⊥ f₂.

## IL MODELLINO: IL PIANO MOBILE E LA VERA GRANDEZZA

### Costruire il piano mobile

Nel modello si fissa un piano proiettante in prima che si possa muovere. Si usa un cartoncino grande e si fa una piega alla base, oppure un taglio, in modo che una parte vada piegata sotto e il piano resti in piedi ma possa ruotare. La prima traccia del piano arriva fino al bordo del cartoncino. Sul piano mobile si disegna un triangolo e se ne segna la prima proiezione, che va a finire a terra, sulla prima traccia.

### La rotazione intorno alla traccia

Finché il piano è inclinato rispetto a π₁, la proiezione del triangolo non ha la sua vera grandezza: le lunghezze dei lati e gli angoli non sono quelli veri. Per conoscere le dimensioni vere bisogna fare una rotazione del piano, e le rotazioni avvengono intorno alle tracce. Ruotando il cartoncino intorno alla prima traccia fino a farlo coincidere con π₁, la figura appare vera. Durante la rotazione l'altezza dei punti non va perduta: ogni punto descrive un arco di circonferenza che sta su un piano perpendicolare all'asse di rotazione, cioè alla traccia, come la spirale del quaderno che, bloccata, lascia ai fogli un solo movimento possibile. È il principio del ribaltamento, ripreso nella lezione successiva.

> [!example] Il disegno
> ![[06-spazio-piano-mobile.svg|600]]
>
> 1. Il piano γ è proiettante in prima: verticale, con t₂γ perpendicolare alla LT e t₁γ inclinata su π₁.
> 2. Il triangolo ABC sta su γ; la sua prima proiezione è un segmento su t₁γ.
> 3. Il piano ruota intorno a t₁γ, che fa da cerniera, fino a stendersi su π₁.
> 4. Ogni punto descrive un arco in un piano perpendicolare a t₁γ; a rotazione finita il triangolo (A)(B)(C) è in vera forma su π₁.

## LE CASE DA STUDIARE E IL RACCOGLITORE

### Le due architetture proposte

Durante la lezione sono stati presentati i due casi di studio, tra i quali ciascuno sceglie la casa su cui lavorare. Il primo è Villa Tugendhat di Ludwig Mies van der Rohe, a Brno, nella Repubblica Ceca (1928-1930): una villa costruita su un terreno in pendenza, come mostrano i prospetti, con grandi vetrate al piano del soggiorno. Il dossier fornito contiene l'assonometria, le piante del piano rialzato e del piano terra, i prospetti nord, sud, est e ovest e le sezioni AA' e BB' in scala 1:100, e fotografie degli esterni e degli interni. Il secondo è Villa Le Lac di Le Corbusier, a Corseaux, in Svizzera (1923-1924): una piccola casa dalla pianta lunga e stretta, affacciata sul lago. Il dossier contiene gli schizzi di Le Corbusier, i disegni originali (tra cui la pianta del piano terra del 1924, fornita anche come immagine separata, e una sezione), e fotografie degli esterni, del giardino e degli interni.

### Che cosa analizzare

Prima del ridisegno si fa una ricerca sul caso scelto (articoli di rivista, estratti di libri e monografie sull'autore, altro materiale in cui si parli dell'opera), a integrazione dei materiali messi su Teams. Poi si studia la casa seguendo l'elenco di analisi delle linee guida, con disegni di studio su fogli A4 a mano libera o a riga e squadra, accompagnati se serve da brevi commenti. I disegni devono mostrare i ragionamenti fatti, anche attraverso appunti sulle foto o sulle piante stampate.

Gli aspetti da studiare sono l'impianto strutturale (pilastri o setti in cemento armato); il rapporto con il suolo, cioè l'attacco a terra, da analizzare con la sezione secondo l'inclinata del terreno e con l'assonometria, disegnando come il terreno scende lungo tutti i lati della costruzione; la distribuzione interna (zona giorno, zona notte, aree porticate), guardando sempre la pianta insieme ai prospetti e alle sezioni; la copertura, valutando da foto e disegni il sistema di smaltimento delle acque meteoriche; i dettagli, cioè le aperture (finestre a doppia anta, vetrate scorrevoli, balconi) con un dettaglio in scala 1:100 in pianta, prospetto e assonometria, le scale esterne e interne in pianta, sezione, assonometria e prospettiva, il corrimano delle scale o la balaustra dei balconi (forma, numero e dimensione degli elementi) e ogni altro dettaglio utile; infine il rapporto volumetrico tra le parti, con assonometrie o esplosi assonometrici. Si possono aggiungere l'analisi dei pieni e dei vuoti sui prospetti, la collocazione delle aperture rispetto al contesto (le visuali, attraverso le foto), l'orientamento degli ambienti, i materiali e i colori.

### Il ridisegno e il raccoglitore

I disegni di analisi servono a capire tutti gli aspetti della casa, così da poterla ridisegnare a riga e squadra in proiezioni ortogonali (piante, prospetti, sezioni) e poi in prospettive, assonometrie, esplosi, spaccati assonometrici e sezioni prospettiche: sono i disegni delle tavole 50x70 previste per l'esame. Per questo è indispensabile elaborare in scala 1:100, a riga e squadra, parti della casa come gli infissi (partendo dai disegni e dalle foto fornite e dal file di suggerimenti su Teams), le scale (con il PDF nella cartella "materiali del corso"), la copertura. Gli arredi interni non si disegnano, a meno che non siano fissi (per esempio una mensola sotto una finestra): niente sanitari, arredi della cucina o del salotto.

Il raccoglitore ha buste trasparenti. In copertina va la copertina fornita dai docenti, stampata, con nome, cognome e anno accademico scritti in alto a destra, nello spazio bianco sotto il nome della casa e del progettista. Nelle prime buste va un breve testo descrittivo della casa, poi i disegni di analisi a mano libera e a riga e squadra delle parti significative e dei dettagli, che serviranno per le tre tavole 50x70 dell'esame. Le foto della casa, stampate, vanno nelle ultime pagine.

> [!tip] Consegne e cose da fare
> - Casa e raccoglitore: si lavora alle analisi da martedì 20 ottobre. La data di consegna del raccoglitore sarà comunicata solo con una settimana di anticipo. I disegni vanno portati sempre a lezione, per ricevere indicazioni man mano.
> - Esame: i menabò delle tre tavole 50x70 si consegnano a dicembre (nel calendario delle attività, date orientative: martedì 22 dicembre, consegna menabò tavole e taccuino).
> - Rifare a casa, prima a mano libera e poi con precisione, il triangolo con un lato orizzontale e uno frontale: tracce del piano generico e stessa figura nel proiettante in prima. Oggi la docente non ritira nulla, ma vuole vederlo la volta successiva.
> - Rifare il disegno del solido e la ricerca delle tracce della sua base.
> - Esercitarsi a squadra e con il modello sulle tracce di rette con direzioni diverse (servirà per le ombre).
> - Fare a colori il disegno della perpendicolare con orizzontale e frontale e riguardarlo: serve per il ribaltamento.
> - Preparare il piano mobile nel modello, con un cartoncino grande e una piega.
> - Esercizi caricati su Teams il 20 ottobre, con le soluzioni per controllarsi: "PO_condizioni di appartenenza_1" (seconda proiezione della figura date la prima e le tracce, tracce del piano dalla figura, prima proiezione dalla seconda, verifica che P appartenga ad α), "PO_condizioni di appartenenza_2" (la retta r appartiene al piano?, seconda proiezione della figura in un piano parallelo alla LT), "PO_proiezioni-solidi_1" (dalle piante di tre solidi: prospetti frontali e laterali, un piano e una retta per ciascun solido verificando l'appartenenza, schema assonometrico a mano libera) e "OMOLOGIA_2_affinità" (omologia affine speciale applicata a un quadrato e omotetia applicata a un quadrilatero).
> - Le posizioni della figura rispetto ai piani di proiezione sono "le cose del compito": nel calendario la prova n. 1 di geometria descrittiva è giovedì 29 ottobre.
> - Dalla lezione successiva la docente cambia aula, per poter disegnare alla lavagna.

## Collegamenti

Questa lezione mette al lavoro tutto ciò che si è costruito nelle lezioni precedenti. Le tracce e i punti notevoli della retta generica vengono dalle [[03-proiezioni-ortogonali-punto-e-rette|proiezioni ortogonali del punto e delle rette]]; i piani nelle varie posizioni, che qui si riconoscono dalla forma delle proiezioni di una figura, sono quelli della bozza sulle [[04-rette-e-piani-nelle-varie-posizioni|rette e i piani nelle varie posizioni]]; le orizzontali, le frontali e le condizioni di appartenenza sono quelle della bozza su [[05-appartenenza-e-rette-ausiliarie|appartenenza e rette ausiliarie]]. Il discorso sulla vera grandezza nel piano frontale si appoggia all'omologia e alla traslazione, con asse e centro all'infinito, viste nello [[02-proiezioni-e-omologia-schema|schema su proiezioni e omologia]], mentre la definizione di diedro e di retta perpendicolare a un piano risale ai richiami di geometria della lezione del 6 ottobre. Il piano ausiliario perpendicolare al piano dato e il piano mobile del modellino preparano direttamente [[07-il-ribaltamento|il ribaltamento]], dove la rotazione intorno alla traccia diventa una costruzione sul foglio. Le orizzontali e le perpendicolari servono anche per le ombre e per le falde dei tetti, e il ridisegno di Villa Tugendhat o di Villa Le Lac applica in scala 1:100 le stesse proiezioni ortogonali, che il corso porterà fino alle tavole d'esame. Per il testo completo della docente si veda la sbobina [[06-piani-proiettanti-orizzontali-frontali]], e per la lezione successiva [[07-ribaltamento-piani-proiettanti]].

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[ARGOMENTI LEZIONI 26-27.pdf]]: elenco degli argomenti della lezione
- [[PO_condizioni di appartenenza_1.pdf]]: esercizi caricati il 20 ottobre
- [[PO_condizioni di appartenenza_1_soluzione.pdf]]: soluzioni della docente
- [[PO_condizioni di appartenenza_2.pdf]]: esercizi caricati il 20 ottobre
- [[PO_condizioni di appartenenza_2_soluzione.pdf]]: soluzioni della docente
- [[PO_proiezioni-solidi_1.pdf]]: esercizio sulle proiezioni dei solidi
- [[PO_proiezioni-solidi_1_soluzione.pdf]]: soluzione della docente
- [[linee guida per lo studio delle architetture proposte _2026-2027.pdf]]: come si studia la casa scelta
- [[2_Villa Tugendhat_Mies van der Rohe.pdf]]: la prima delle due case proposte
- [[3_Villa Le Lac_Le Corbusier.pdf]]: la seconda casa proposta
- [[3_Pianta casa a Le Lac.jpg]]: pianta di Villa Le Lac
- [[Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: date delle prove e delle consegne
