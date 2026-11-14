---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-29
tags: [geometria-descrittiva, bozza]
---

# Il ribaltamento del piano generico

> [!info] Note collegate
> Sbobina: [[09-ribaltamento-piano-generico]]
>
> Bozza precedente: [[08-il-ribaltamento-del-punto]] · Successiva: [[10-intersezione-retta-piano-e-segno-di-sezione]]
>
> Argomenti collegati: [[07-il-ribaltamento]] · [[06-piani-ausiliari-e-perpendicolarita]] · [[05-appartenenza-e-rette-ausiliarie]] · [[02-affinita-ortogonale-passo-passo]]

Quando una figura sta su un piano generico, né la prima né la seconda proiezione ne mostrano la vera grandezza e forma: il piano è inclinato rispetto a tutti e due i piani di proiezione, e la figura appare deformata in entrambe.

Per conoscerla bisogna ribaltare il piano, cioè farlo ruotare intorno a una sua retta finché non si appoggia su un piano orizzontale.

La lezione di giovedì 29 ottobre mostra come si fa, in due modi:

- in forma canonica, ribaltando il piano intorno alla sua prima traccia;
- in forma tecnica, ribaltandolo intorno a una qualunque orizzontale del piano, senza cercare le tracce e perfino senza la linea di terra.

Il procedimento è lo stesso del ribaltamento dei piani proiettanti visto il 22 ottobre, con un passaggio in più: siccome la rotazione intorno alla traccia non si vede sul foglio, la si ricostruisce con un piano ausiliario perpendicolare al piano dato.

Alla fine della lezione la docente applica lo stesso ragionamento a una squadretta appoggiata su π₁ con un lato, e introduce lo sviluppo piano della piramide, che servirà per costruirne il modello in cartoncino.

Il ribaltamento del piano generico è tra gli argomenti della Prova n. 2.

La lezione è ricostruita da due registrazioni: la parte centrale, fino al ribaltamento intorno all'orizzontale, è chiara; l'ultima parte (la squadretta e la piramide) è molto frammentaria, e qui è completata con schemi proposti, segnalati come tali.

## IL PRINCIPIO DEL RIBALTAMENTO

### La figura nel piano generico

La figura da disegnare in aula sta su un piano generico, ed è data con le sue due proiezioni.

Non può stare su un piano proiettante in prima, perché il piano proiettante in prima è un piano verticale: tutto quello che c'è sopra (figure, tracce, rette) nella prima proiezione va a finire sulla prima traccia del piano. Se la prima proiezione della figura non si vede come figura, ma si riduce a una linea, il piano è proiettante in prima.

Per dire se un piano è generico, oppure per esempio parallelo alla linea di terra, bisogna fare dei ragionamenti sulle rette della figura.

Nella figura dell'esercizio i lati sono chiaramente rette generiche: non c'è nulla né di orizzontale né di frontale.

### I punti ruotano su piani perpendicolari al piano

Quando si ribalta un piano, i punti che gli appartengono compiono degli archi di circonferenza.

Questo vale qualunque sia la posizione del piano da ribaltare:

- generico,
- proiettante in prima,
- proiettante in seconda,
- frontale,
- parallelo alla linea di terra.

In tutti i casi gli archi si trovano su piani perpendicolari al piano da ribaltare.

Nei piani proiettanti questi piani perpendicolari erano facili da vedere. Nel piano generico bisogna costruirli: è il punto nuovo di questa lezione.

### Il piano perpendicolare al piano generico: il proiettante in prima

Un piano perpendicolare a un piano generico α può essere il piano proiettante in prima, a una condizione: che la sua prima traccia sia perpendicolare alla prima traccia di α.

Questo piano si chiama γ, e la condizione si scrive t₁γ ⊥ t₁α.

Il motivo sta nella regola che mette in relazione di perpendicolarità due piani. Secondo Monge, due piani sono perpendicolari tra loro se per uno dei due si può condurre una retta perpendicolare all'altro.

La condizione t₁γ ⊥ t₁α fa verificare proprio questa regola. Infatti, se si traccia un'orizzontale o che appartiene ad α, la retta o risulta perpendicolare al piano γ:

- o₁ è parallela a t₁α, quindi è perpendicolare a t₁γ;
- o₂ è parallela alla linea di terra, quindi è perpendicolare a t₂γ, che nel proiettante in prima è perpendicolare alla linea di terra.

Una retta è perpendicolare a un piano quando è perpendicolare alle tracce del piano: quindi o è perpendicolare a γ, e α, che contiene o, è perpendicolare a γ.

Era uno degli esercizi assegnati: trovare la prima e la seconda traccia del piano e, per il punto P, costruire la retta perpendicolare.

Lo stesso esercizio si può fare in due forme:

- in forma canonica, con le tracce del piano;
- in forma tecnica, usando l'altra condizione, cioè che una retta è perpendicolare a un piano quando è perpendicolare a due rette del piano.

Allo stesso modo il ribaltamento del piano generico si fa in forma canonica, con le tracce del piano, oppure in forma tecnica, senza.

### La prima traccia è l'orizzontale a quota zero

Prima di ribaltare la docente sottolinea una cosa importante, che aveva già detto la volta precedente: la prima traccia del piano può essere considerata l'orizzontale a quota zero del piano.

Sul piano generico si possono lanciare tante orizzontali, una sotto l'altra. Ognuna, per appartenere ad α, ha la prima proiezione parallela a t₁α.

Via via che si costruiscono orizzontali sempre più basse, la loro prima proiezione si avvicina alla prima traccia: si scende, si scende, finché a un certo punto un'orizzontale coincide con t₁α. È l'orizzontale a quota zero, una retta che sta praticamente sul primo piano di proiezione.

Quindi t₁α, con un altro nome, è l'orizzontale a quota zero del piano.

Questa osservazione per ora si tiene da parte: servirà per la forma tecnica.

> [!example] Disegno 1 · Il disegno: le orizzontali scendono fino alla prima traccia
> ![[09-orizzontali-fino-alla-traccia.svg|620]]
>
> 1. Il piano α è generico: t₁α e t₂α si incontrano sulla LT.
> 2. Un'orizzontale o di α ha o₂ parallela alla LT. Dal punto in cui o₂ incontra t₂α si scende con la linea di richiamo fino alla LT, e da lì si traccia o₁ parallela a t₁α.
> 3. Si disegnano altre orizzontali, a quote sempre più basse: le loro prime proiezioni sono parallele a t₁α e le si avvicinano sempre di più.
> 4. Quando la quota arriva a zero, l'orizzontale sta su π₁ e o₁ coincide con t₁α.

> [!example] Disegno 2 · Il disegno nello spazio: le orizzontali del piano generico
> ![[09-spazio-orizzontali-del-piano.svg|620]]
>
> 1. Le orizzontali sono le rette di α parallele a π₁, ognuna a una quota diversa.
> 2. Le loro prime proiezioni (tratteggiate) sono parallele a t₁α.
> 3. Scendendo verso π₁, l'ultima orizzontale, quella a quota zero, è la prima traccia t₁α.

## LA FORMA CANONICA: IL RIBALTAMENTO INTORNO ALLA PRIMA TRACCIA

### Il triangolo con un vertice su π₁

La figura dell'esercizio è un triangolo ABC su un piano generico, disegnato nella parte superiore del foglio, centrato, abbastanza grande ma non troppo: se è troppo grande, le tracce finiscono fuori dal foglio.

L'unica particolarità è che il punto C è appoggiato sul piano π₁, e pertanto la sua seconda proiezione C₂ sta sulla linea di terra.

Chi ha un dubbio su questo aspetto prende il modello del triedro e ci appoggia una squadretta da 60 con un vertice su π₁: si vede immediatamente che la seconda proiezione di quel vertice va a finire sulla linea di terra.

Che il punto sia appoggiato su π₁ o sollevato è indifferente: si procede sempre allo stesso modo, i procedimenti sono sempre questi.

I plastici vanno bene tutti, anche quelli di piani diversi dal generico, perché il concetto è sempre lo stesso e le regole sono sempre uguali. Come per gli esercizi di omologia, dove le regole erano sempre due.

### Trovare la prima traccia del piano

L'esercizio chiede la vera grandezza e forma del triangolo. Per farlo in forma canonica bisogna trovare la prima traccia del piano, e per trovare la traccia del piano bisogna trovare le tracce delle rette.

I lati del triangolo sono segmenti che appartengono a delle rette, e di queste rette si trovano le tracce:

1. si prolunga la seconda proiezione della retta fino alla linea di terra;
2. quel punto è la seconda proiezione della prima traccia;
3. da lì si scende con la linea di richiamo fino alla prima proiezione della retta: lì c'è la prima traccia.

Le lettere sono importanti, perché altrimenti ci si confonde: la prima traccia della retta m si chiama T₁ₘ, la seconda T₂ₘ. Le tracce sono punti delle rette, e stanno sulle proiezioni delle rette.

In questo esercizio una traccia si trova subito. La retta r che passa per B e per C buca il primo piano di proiezione proprio nel punto C, perché C sta già per terra: C coincide con la prima traccia di r.

Per dimostrarlo si prolunga r₂ fino alla linea di terra, e ci si trova già, in C₂; la proiezione prova che C₁ coincide con T₁ᵣ.

A questo punto l'esercizio è per metà fatto. Per le condizioni di appartenenza, se la figura appartiene al piano, le tracce di tutte le sue rette devono appartenere alle tracce del piano.

Per tracciare una retta bastano due punti, e la retta di cui si parla qui è la prima traccia del piano: si traccia da C₁ ≡ T₁ᵣ e dalla prima traccia di un altro lato.

Non è necessario cercare la seconda traccia del piano: si deve ribaltare su π₁, quindi non interessa.

> [!example] Disegno 3 · Il disegno: la prima traccia del piano dal triangolo
> ![[09-triangolo-prima-traccia.svg|620]]
>
> 1. Il triangolo ABC sta su un piano generico α: si vedono sia la seconda sia la prima proiezione. C sta su π₁, quindi C₂ è sulla LT.
> 2. La retta r = BC buca π₁ proprio in C: prolungando r₂ fino alla LT si arriva già in C₂, e scendendo con la linea di richiamo si trova C₁ ≡ T₁ᵣ.
> 3. Serve la prima traccia di un'altra retta, per esempio s = AB (il nome s è aggiunto qui): si prolunga s₂ fino alla LT, si trova (T₁ₛ)₂, si scende con la linea di richiamo fino a s₁ prolungata: lì c'è T₁ₛ.
> 4. t₁α passa per C₁ ≡ T₁ᵣ e per T₁ₛ. La seconda traccia del piano non serve.

### Quale punto ribaltare

Qualcuno potrebbe chiedere come si trova la retta di massima pendenza. Ma la retta di massima pendenza non è richiesta, e non è necessario ribaltarla.

È vero che la retta di massima pendenza di un piano si trova costruendo un piano perpendicolare al piano dato (la retta di intersezione tra i due è la retta di massima pendenza), e che costruendo il piano perpendicolare se ne costruisce in pratica la prima proiezione. Ma se non serve, non si disegna.

Quello che si deve ribaltare è il punto più lontano dall'asse di rotazione. Come si era visto nella lezione del 27 ottobre, dal punto di vista grafico conviene ribaltare il punto lontano, perché così si è più precisi: con un punto vicino all'asse l'errore aumenta.

In questo esercizio l'asse di rotazione è t₁α, e il punto più lontano è B.

Il procedimento ha quattro passi.

### Passo 1: il piano γ perpendicolare ad α, per B

Si costruisce un piano γ perpendicolare al piano dato, passante per B.

γ è un piano proiettante in prima, con la prima traccia t₁γ perpendicolare a t₁α.

Passante per B significa che B₁ appartiene a t₁γ: si traccia quindi da B₁ la perpendicolare a t₁α, e la si chiama t₁γ.

Il punto in cui t₁γ incontra t₁α qui si chiama H: sarà il centro della rotazione.

La seconda traccia di γ non si disegna: non interessa.

> [!example] Disegno 4 · Il disegno: passo 1
> ![[b09-canonica-passo-1.svg|620]]
>
> 1. Si individua il punto più lontano da t₁α: è B.
> 2. Da B₁ si traccia t₁γ perpendicolare a t₁α (si segna l'angolo retto).
> 3. Si segna H, il punto in cui t₁γ incontra t₁α.

### Passo 2: il ribaltamento laterale di γ e il punto B̄

Il secondo passo è ribaltare lateralmente il piano γ.

Si ribalta γ, e non direttamente α, perché nel ribaltamento intorno alla prima traccia di α la rotazione di B non si può vedere sul foglio: B si muove su γ, che è verticale, e in prima proiezione γ si vede solo come una linea, t₁γ. Per vedere la rotazione bisogna prima stendere γ su π₁.

γ è un piano proiettante in prima, e un piano proiettante in prima si ribalta come si è visto il 22 ottobre:

- si fa ruotare intorno alla sua prima traccia t₁γ;
- si riportano le quote dei punti sulla perpendicolare alla traccia.

Qui interessa un punto solo, B. Si prende quindi la quota di B.

La quota di B è l'altezza del punto rispetto al piano che si sta usando, e può variare a seconda del piano rispetto a cui si ribalta. In questo caso si usa la prima traccia del piano, quindi si considera l'altezza rispetto a π₁: è la distanza di B₂ dalla linea di terra.

Si prende questa quota, la si segna con due lineette e la si riporta da B₁ sulla perpendicolare a t₁γ, segnando anche lì le due lineette.

Il punto che si trova si chiama B soprallineato, B̄.

Non è ancora il punto ribaltato. Il triangolo che ha i vertici in B₁, H e B̄ è il triangolo di rotazione, quello già disegnato la volta precedente:

- un cateto è B₁H, su π₁;
- l'altro cateto è la quota di B, qui stesa su π₁ come B₁B̄;
- l'ipotenusa HB̄ è il raggio di rotazione.

> [!example] Disegno 5 · Il disegno: passo 2
> ![[b09-canonica-passo-2.svg|620]]
>
> 1. Si prende con il compasso la quota di B, cioè la distanza di B₂ dalla LT, e la si segna con due lineette.
> 2. Da B₁ si traccia la perpendicolare a t₁γ.
> 3. Su questa perpendicolare si riporta la quota di B, a partire da B₁, e si segnano di nuovo le due lineette: si trova B̄.
> 4. Si unisce H con B̄: il triangolo B₁HB̄ (verde) è il triangolo di rotazione, e HB̄ è il raggio.

> [!example] Disegno 6 (proposto, non fatto a lezione): il ribaltamento laterale nello spazio
> ![[b09-spazio-ribaltamento-laterale.svg|620]]
>
> 1. Il piano γ (verde) è verticale e passa per B. Su γ c'è il triangolo di rotazione B₁HB: B₁ è sotto B, H è su t₁α, HB è la distanza vera di B dall'asse.
> 2. Si abbatte γ su π₁ facendolo ruotare intorno a t₁γ (arco arancio): B arriva in B̄, a una distanza da B₁ uguale alla sua quota.
> 3. Il triangolo B₁HB̄ (arancio) è il triangolo di rotazione steso su π₁, con le stesse misure: HB̄ = HB.
> 4. Con il compasso (arco grigio) HB̄ si porta su t₁γ: si arriva nello stesso punto B\* in cui arriva B con la rotazione vera intorno a t₁α (arco rosso).

### Passo 3: il raggio di rotazione e il punto B\*

Ora B si ribalta davvero, intorno a t₁α.

Nella rotazione ogni punto compie un arco lungo un piano diverso: B lo compie lungo γ, A lungo un altro piano perpendicolare a t₁α, mentre C non si muove, perché sta per terra.

B ruota intorno a t₁α con centro in H e raggio uguale alla sua distanza da t₁α, che è HB̄. Quando il piano α si è abbattuto, B sta su π₁ e insieme su γ: quindi sta su t₁γ.

Si punta quindi il compasso in H, all'intersezione tra le tracce, con apertura HB̄, e lo si ruota fino a t₁γ: si ottiene il punto B asterisco, B\*.

Il punto si porta dalla parte opposta alla prima proiezione della figura, così il ribaltamento non si sovrappone al disegno già fatto.

> [!example] Disegno 7 · Il disegno: passo 3
> ![[b09-canonica-passo-3.svg|620]]
>
> 1. Si punta il compasso in H, con apertura HB̄.
> 2. Si ruota fino a incontrare t₁γ, dalla parte opposta alla figura: lì c'è B\*.

> [!example] Disegno 8 · Il disegno nello spazio: la rotazione di B intorno a t₁α
> ![[09-spazio-ribaltamento-piano-generico.svg|620]]
>
> 1. Il piano γ (verde) è proiettante in prima e passa per B; t₁γ è perpendicolare a t₁α, quindi γ è perpendicolare ad α.
> 2. Quando α ruota intorno a t₁α per abbattersi su π₁, B si muove lungo un arco (tratteggio rosso) che sta tutto su γ: il centro è H e il raggio è HB.
> 3. A ruota allo stesso modo su un altro piano perpendicolare a t₁α; C sta su π₁ e non si muove.
> 4. Il triangolo A\*B\*C\* sta su π₁ in vera grandezza.

### Passo 4: l'omologia di ribaltamento

Trovato B\*, non serve ripetere tutta la costruzione per gli altri punti: si applica l'omologia.

Tra la prima proiezione della figura e il suo ribaltamento c'è l'omologia di ribaltamento, già vista con i piani proiettanti:

- l'asse dell'omologia è sempre la retta di intersezione tra i piani che si stanno considerando, cioè tra il piano che contiene la figura e il piano su cui si porta la figura: qui α e π₁, quindi l'asse è t₁α;
- è un'affinità ortogonale, e la direzione è perpendicolare all'asse.

Si applicano quindi le due proprietà:

- le rette corrispondenti si incontrano sull'asse;
- i punti corrispondenti stanno sulla direzione dell'affinità, cioè sulle perpendicolari all'asse.

La retta A₁B₁, prolungata, incontra l'asse in un punto U, che non si muove. La sua corrispondente passa per U e per B\*.

A\* sta su questa retta e sulla perpendicolare all'asse condotta da A₁.

C non si è mosso, perché sta sull'asse: C coincide con C\*.

Il triangolo A\*B\*C\* è la vera grandezza e forma della figura.

> [!example] Disegno 9 · Il disegno: passo 4
> ![[b09-canonica-passo-4.svg|620]]
>
> 1. Si prolunga A₁B₁ fino all'asse t₁α: è il punto U.
> 2. Si traccia la retta UB\*: è la corrispondente di A₁B₁.
> 3. Da A₁ si traccia la perpendicolare all'asse: dove incontra la retta UB\* c'è A\*.
> 4. C sta sull'asse: C\* ≡ C₁.
> 5. Si unisce A\*B\*C\*: è la vera grandezza e forma del triangolo.

## LA FORMA TECNICA: IL RIBALTAMENTO INTORNO A UN'ORIZZONTALE

### Qualunque orizzontale del piano può fare da asse

Si torna all'osservazione tenuta da parte: t₁α coincide con l'orizzontale a quota zero del piano.

Questo significa che si può usare qualunque orizzontale del piano. Se si può ribaltare un piano intorno alla sua traccia, che è l'orizzontale a quota zero del piano, si può ribaltare la stessa figura intorno a un'altra orizzontale del piano, senza trovare la traccia.

Come asse si può scegliere un'orizzontale che passa per il punto più basso della figura, in modo che il ribaltamento non si sovrapponga alla prima proiezione. Si può anche prendere un'orizzontale in mezzo alla figura, ma allora tra la prima proiezione e il ribaltamento c'è una sovrapposizione.

Per vederlo si disegna un'altra figura sul piano: un triangolo ABC, in tutte e due le proiezioni, che questa volta non tocca la linea di terra. Il punto C non sta più su π₁.

Con questa figura si potrebbe trovare la traccia del piano, ma non interessa: come asse si usa un'orizzontale che passa per C₂.

### Senza la linea di terra

Nell'esercizio svolto nel PDF del libro manca la linea di terra.

La linea di terra è una convenzione: Monge ha sistemato tre piani, e quindi la linea di terra ce la diamo. Ma nella pratica progettuale la casa non si colloca sempre nel triedro, e non si ha sempre bisogno di questo sistema di riferimento.

Il riferimento serve all'inizio, proprio per poi toglierlo e lavorare anche senza.

Bisogna anche non confondere il piano con la figura piana:

- la figura piana è il triangolo;
- il piano è la cosa estesa, che non si vede, che contiene la figura piana.

Quando si disegna un triangolo sul foglio, la figura è il triangolo, ma il piano che la contiene è il foglio, ed è infinito.

Quindi un'orizzontale del piano non deve stare dentro la figura, né passare in mezzo alla figura: l'importante è che stia nello stesso piano.

### Passo 1: costruire l'orizzontale o

La caratteristica dell'orizzontale è avere la seconda proiezione parallela alla linea di terra. Anche se la linea di terra non c'è, si disegna o₂ orizzontale nel foglio, passante per C₂. Le tracce non si disegnano.

Per disegnare o₁ servono due punti.

Un punto è sicuramente C₁.

Per trovarne un altro si prolunga il segmento A₂B₂, che appartiene alla retta r passante per A e per B: r₂ incontra o₂ in un punto, che si chiama M₂ (il nome non è importante).

M è il punto di intersezione tra la retta r e la retta o, quindi appartiene a tutte e due:

- M₂ appartiene a r₂ e a o₂;
- M₁ apparterrà a r₁ e a o₁.

Sono cose una di seguito all'altra. M₁ e M₂ sono allineati lungo la linea di richiamo: si prolunga r₁, si scende con la linea di richiamo da M₂ e dove questa incontra r₁ c'è M₁.

M₁ deve appartenere a o₁: o₁ è quindi la retta che passa per C₁ e per M₁.

o₁ è l'asse di rotazione. È come se si ribaltasse il piano non rispetto alla sua traccia, ma rispetto a un piano orizzontale un po' più su: o è un'orizzontale del piano generico a una quota un po' più alta, quella di C.

> [!example] Disegno 10 · Il disegno: forma tecnica, passo 1
> ![[b09-tecnica-passo-1.svg|620]]
>
> 1. Il triangolo ABC sta sul piano generico, ma C non sta su π₁. La linea di terra non si disegna.
> 2. Per C₂ si traccia o₂, orizzontale nel foglio: è la seconda proiezione di un'orizzontale o del piano, alla quota di C.
> 3. Si prolunga A₂B₂ (cioè r₂) fino a incontrare o₂ in M₂.
> 4. Da M₂ si scende con la linea di richiamo fino a r₁ prolungata: lì c'è M₁.
> 5. o₁ passa per C₁ e per M₁: è l'asse di rotazione.

### Passo 2 e 3: il ribaltamento intorno a o, cambia una sola misura

Da qui si fa esattamente quello che si è fatto con la traccia. Il procedimento è identico, non cambia nulla: l'asse di rotazione è una retta orizzontale del piano.

Non cambia il fatto che si deve costruire un piano perpendicolare, passante per il punto da ribaltare. Nella forma tecnica però il piano non viene individuato dalla traccia, ma dalla proiezione: lo si può chiamare γ₁, la prima proiezione del piano γ. Anche qui ci sono sempre i 90 gradi tra γ₁ e o₁.

Cambia una cosa sola: una misura.

La misura che cambia è quella che si ribalta per trovare B̄. Prima si riportava la quota di B misurata dal piano π₁, cioè la distanza di B₂ dalla linea di terra. Ora l'asse non sta su π₁ ma alla quota di C, e la quota di B va misurata rispetto al piano orizzontale che contiene l'asse: è la distanza di B₂ da o₂.

È a questo che serve B trattino: a portare sul foglio, insieme a B₁, la vera altezza di B sopra l'asse di rotazione.

Il resto è identico:

1. γ₁ perpendicolare a o₁ per B₁; H è il punto in cui γ₁ incontra o₁;
2. da B₁, sulla perpendicolare a γ₁, si riporta la distanza di B₂ da o₂: si trova B̄;
3. con centro in H e raggio HB̄ si porta il punto su γ₁: si trova B\*;
4. si applica l'affinità di asse o₁.

Nell'affinità c'è una comodità: la retta r₁ incontra l'asse proprio in M₁, perché M sta sull'orizzontale o. M è quindi un punto unito, e la retta corrispondente di r passa per M₁ e per B\*.

Il triangolo ribaltato sta sul piano orizzontale alla quota di C, che è parallelo a π₁: per questo la sua prima proiezione ha le misure vere, e sul foglio lo si disegna direttamente.

> [!example] Disegno 11 · Il disegno: forma tecnica, passo 2
> ![[b09-tecnica-passo-2.svg|620]]
>
> 1. Da B₁ si traccia γ₁ perpendicolare a o₁ (si segna l'angolo retto); H è il punto in cui γ₁ incontra o₁.
> 2. Si prende con il compasso la distanza di B₂ da o₂ (non dalla LT) e la si segna con due lineette.
> 3. La si riporta da B₁ sulla perpendicolare a γ₁: si trova B̄. Il triangolo B₁HB̄ è il triangolo di rotazione.

> [!example] Disegno 12 · Il disegno: forma tecnica, passo 3
> ![[b09-tecnica-passo-3.svg|620]]
>
> 1. Centro del compasso in H, raggio HB̄: l'arco porta il punto su γ₁. Lì c'è B\*.
> 2. La retta r₁ incontra l'asse o₁ in M₁: la retta M₁B\* è la sua corrispondente.
> 3. Da A₁ si traccia la perpendicolare a o₁: dove incontra la retta M₁B\* c'è A\*.
> 4. C sta sull'asse e non si muove: C\* ≡ C₁. A\*B\*C\* è la vera grandezza e forma.

> [!example] Disegno 13 (proposto, non fatto a lezione): il ribaltamento intorno all'orizzontale nello spazio
> ![[b09-spazio-ribaltamento-orizzontale.svg|620]]
>
> 1. L'orizzontale o (arancio) sta su α alla quota di C. Il piano orizzontale che la contiene è colorato in arancio.
> 2. α ruota intorno a o finché si stende su quel piano orizzontale: B descrive l'arco rosso, con centro H.
> 3. La quota di B che conta (tratteggio nero) è quella sopra il piano dell'asse, non quella sopra π₁: sul foglio è la distanza di B₂ da o₂.
> 4. A\*B\*C\* sta su un piano parallelo a π₁, quindi la sua prima proiezione è in vera grandezza.

## LA SQUADRETTA E LO SVILUPPO DELLA PIRAMIDE

### La squadretta appoggiata con un lato su π₁

L'ultimo esercizio è semplice: la figura è un triangolo rettangolo, come la squadra da disegno. È la squadretta da 60, appoggiata su π₁ con un lato: il lato sta per terra, e la squadretta non è verticale, perché è inclinata.

Anche qui la prima domanda è qual è l'asse di rotazione della figura.

In generale la si deve ribaltare intorno alla prima traccia del piano, oppure intorno a un'orizzontale del piano. Ma se il lato sta già per terra, la figura ruota intorno a quel lato: è inutile cercare la traccia, se si vede che i punti stanno già su π₁.

Il lato appoggiato ha le seconde proiezioni dei suoi estremi sulla linea di terra, e la sua prima proiezione sta sulla prima traccia del piano.

Si ribalta quindi solo il terzo vertice, C, con la stessa costruzione:

- la quota di C;
- il piano perpendicolare per C;
- il raggio di rotazione.

Una volta usato il raggio di rotazione, serve solo C ribaltato: gli altri punti non si sono mossi, e la figura è fatta.

La docente ricorda che è la quinta volta che si vede il ribaltamento del piano generico.

> [!example] Disegno 14 · Il disegno: la squadretta con il lato AB su π₁
> ![[b09-squadretta-foglio.svg|620]]
>
> 1. La squadretta è appoggiata su π₁ con il lato AB ed è inclinata: A₂ e B₂ stanno sulla LT, e A₁B₁ sta sulla prima traccia t₁α.
> 2. L'asse di rotazione è il lato stesso: A e B non si muovono (A\* ≡ A₁, B\* ≡ B₁).
> 3. Da C₁ si traccia t₁γ perpendicolare all'asse. Qui incontra l'asse proprio in A₁, perché l'angolo in A è retto: H ≡ A₁.
> 4. Da C₁, sulla perpendicolare a t₁γ, si riporta la quota di C (distanza di C₂ dalla LT, due lineette): si trova C̄.
> 5. Centro in H, raggio HC̄: l'arco porta il punto su t₁γ. Lì c'è C\*.
> 6. A\*B\*C\* è la squadretta in vera forma: angolo retto in A, 30° in B, 60° in C. Le misure sono scelte qui: dall'audio non si ricavano.

> [!example] Disegno 15 (proposto, non fatto a lezione): la squadretta nello spazio
> ![[b09-spazio-squadretta.svg|620]]
>
> 1. Il lato AB sta su π₁ e fa da cerniera: A e B non si muovono.
> 2. C ruota intorno ad AB (arco rosso), su un piano perpendicolare ad AB, e arriva su π₁ in C\*.
> 3. A\*B\*C\* è la squadretta in vera forma.

### Lo sviluppo piano della piramide

Alla fine della lezione la docente introduce lo sviluppo piano della piramide.

Ognuno deve fare un modellino, cioè costruire una piramide con un cartoncino:

1. si sceglie una piramide, nella posizione che si preferisce;
2. sul cartoncino se ne disegna lo sviluppo, per poterlo piegare;
3. si ritaglia e si piega.

Per disegnare lo sviluppo bisogna sapere la vera grandezza e forma di ogni faccia, e per questo serve l'altezza del vertice.

La registrazione di questa parte è quasi incomprensibile. Lo schema qui sotto propone un modo di applicare quello che si è visto nella lezione: se la piramide ha la base appoggiata su π₁, ogni faccia laterale è un triangolo con un lato per terra, proprio come la squadretta.

Ogni faccia si ribalta quindi intorno al suo lato di base, e si ribalta solo il vertice V, usando come quota l'altezza della piramide. Facendo ruotare ogni faccia verso l'esterno della base, le quattro facce ribaltate e la base formano lo sviluppo.

> [!example] Disegno 16 (proposto, non fatto a lezione): una faccia della piramide si abbatte su π₁
> ![[b09-spazio-piramide.svg|620]]
>
> 1. La piramide ha la base quadrata DEFG su π₁ e il vertice V; V₁ è il centro della base.
> 2. La faccia DEV ruota intorno al lato DE, che sta per terra: V descrive un arco su un piano verticale perpendicolare a DE, con centro H.
> 3. Il triangolo HV₁V è il triangolo di rotazione: il cateto V₁V è l'altezza della piramide.
> 4. Quando la faccia arriva su π₁, il triangolo DEV\* è in vera grandezza.

> [!example] Disegno 17 (proposto, non fatto a lezione): lo sviluppo della piramide sul foglio
> ![[b09-sviluppo-piramide.svg|620]]
>
> 1. Si disegnano le due proiezioni della piramide: la base sta sulla LT in seconda proiezione, e l'altezza h si legge come distanza di V₂ dalla LT.
> 2. Per la faccia DE: da V₁ si traccia t₁γ perpendicolare a DE; H è il punto in cui incontra DE.
> 3. Da V₁, sulla perpendicolare a t₁γ (cioè parallela a DE), si riporta l'altezza h (due lineette): si trova V̄.
> 4. Centro in H, raggio HV̄: l'arco porta il punto su t₁γ, dalla parte esterna della base. Lì c'è V\*.
> 5. Si ripete per le altre tre facce, ognuna intorno al suo lato di base: base e quattro facce ribaltate sono lo sviluppo da disegnare sul cartoncino.

> [!tip] Avvisi e consegne
> - Consegna di rette e piani: era per oggi; chi non l'ha portata la porta la prossima volta. La docente fa un controllo incrociato con la consegna precedente (dall'audio si capisce solo che riguarda chi ha sbagliato il piano proiettante in prima).
> - La prossima volta un'ora è dedicata allo studio della casa, anche per gruppi: analizzarla ridisegnandola, collocare le foto sulla pianta, capire come sono fatti infissi e scala, usando il PDF di esempio su come disegnare la scala (su Teams). Serve anche per l'esame di progettazione.
> - Sul foglio: disegno nella parte superiore, centrato, abbastanza grande ma non troppo; lettere grandi e leggibili; niente apici per le proiezioni (A₁, non A′), perché l'apice servirà in assonometria.
> - Il PDF degli esercizi si scarica con il codice del libro; chi non lo ha lo chieda alla docente. Nel PDF l'esercizio è svolto sopra in forma tecnica e sotto in forma canonica, con una fascia laterale che spiega i passaggi; il metodo però è spiegato nel libro, e il PDF da solo non basta.
> - Per la prossima volta: studiare lo sviluppo piano; inventare un esercizio, costruire la piramide in cartoncino con il suo sviluppo, ritagliarlo e portare tutto.
> - Seguire, frequentare e partecipare rispondendo alle domande: la frequenza è obbligatoria perché in aula si capisce meglio, e l'esame è propedeutico a progettazione.
> - La Prova n. 2 di geometria descrittiva è fissata dal calendario aggiornato a giovedì 26 novembre.

## Collegamenti

Il ribaltamento del piano generico completa quello dei piani proiettanti della bozza [[07-il-ribaltamento]]: il piano ausiliario γ è un piano proiettante in prima, e il suo ribaltamento laterale è esattamente il ribaltamento su π₁ visto il 22 ottobre, con la quota riportata sulla perpendicolare alla traccia e segnata con le lineette.

La costruzione di γ si fonda sulla condizione di perpendicolarità tra un piano generico e un proiettante in prima, e sulla perpendicolare costruita con l'orizzontale, che la docente aveva raccomandato di riguardare proprio in vista di questa lezione nella bozza [[06-piani-ausiliari-e-perpendicolarita]].

La ricerca della prima traccia a partire dalle tracce dei lati e la costruzione dell'orizzontale con il punto M sono applicazioni delle condizioni di appartenenza e delle rette ausiliarie di [[05-appartenenza-e-rette-ausiliarie]], a loro volta basate sulle tracce delle rette di [[03-proiezioni-ortogonali-punto-e-rette]] e [[04-rette-e-piani-nelle-varie-posizioni]].

L'idea che la prima traccia sia l'orizzontale a quota zero era stata anticipata nella lezione del 27 ottobre ([[08-tracce-orizzontale-e-ribaltamento-del-punto]]), insieme al consiglio di ribaltare il punto più lontano dall'asse.

L'ultimo passo di ogni ribaltamento è un'[[02-affinita-ortogonale-passo-passo|affinità ortogonale]], l'omologia con il centro all'infinito nella direzione perpendicolare all'asse studiata nella [[02-proiezioni-e-omologia|seconda lezione]]: per questo la docente ricorda che le regole sono sempre due, come negli esercizi di omologia.

Il lavoro senza linea di terra prepara al disegno di progetto, e l'avvertenza di non usare gli apici per le proiezioni guarda già all'assonometria ([[11-assonometria-obliqua-cavaliera-militare]]). Lo sviluppo della piramide, infine, porta il ribaltamento dalle figure piane ai solidi e al modello in cartoncino; la lezione successiva ([[10-intersezione-retta-figura-e-sezioni]]) resta sul piano dato da una figura, con l'intersezione tra una retta e il piano.

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[2agg_Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: calendario aggiornato, con la data della Prova n. 2
- [[il-disegno-della-scala.pdf]]: il PDF di esempio su come disegnare la scala, citato a lezione per lo studio della casa
- [[linee guida per lo studio delle architetture proposte _2026-2027.pdf]]: le indicazioni su come studiare la casa, richiamate all'inizio della lezione
