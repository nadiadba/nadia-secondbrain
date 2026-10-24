---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-29
tags: [geometria-descrittiva, bozza, ripasso]
---

# Ripasso per la Prova n.1 (29 ottobre)

Scheda da ripassare in 30-40 minuti prima della Prova n.1 di giovedì 29 ottobre: tutto il programma dal 1 al 22 ottobre, in ordine di lezione, con le regole da sapere e i passaggi di ogni tipo di esercizio. I disegni svolti sono nelle bozze (link tra parentesi).

> [!info] Note collegate
> Bozze: [[01-strumenti-materiali-e-regole]] · [[02-proiezioni-e-omologia-schema]] · [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]]

> [!question] Che cosa chiederà la prova?
> Il calendario dice solo «Geometria descrittiva prova n.1». Il 13 ottobre la docente ha parlato di una prova sull'omologia (la frase si sente solo a metà); il 20 ottobre ha detto che le posizioni della figura rispetto ai piani di proiezione sono «le cose del compito». Per sicurezza qui c'è tutto.

## 1. Strumenti e regole del segno (1 ottobre)

- **Linee di costruzione**: si lasciano tutte, leggere ma visibili. Conta il procedimento, non solo il risultato ([[01-strumenti-materiali-e-regole#Le linee di costruzione restano|bozza 01]]).
- **Segno**: costruzioni sottili, risultato più marcato; ogni linea con un segno unico, uguale dall'inizio alla fine ([[01-strumenti-materiali-e-regole#LE REGOLE DEL DISEGNO TECNICO|bozza 01]]).
- **Scrittura**: a mano, in stampatello, tra due parallele leggere e vicine; nome, cognome e data in testa al foglio.
- **Mine**: H dure (segno grigio, per le costruzioni), B morbide (segno scuro), HB in mezzo.
- **Formati**: A4 = 21 × 29,7 · A3 = 29,7 × 42 · A2 = 42 × 59,4 · A1 = 59,4 × 84 · il più grande 84 × 118 (cm). Lato maggiore = diagonale del quadrato sul lato minore (rapporto √2).
- **Scale**: 1:100 → 1 m = 1 cm · 1:50 → 1 m = 2 cm · 1:200 → 1 m = 0,5 cm. Sempre la scala grafica.
- **Piante e prospetti**: pianta = oggetto visto dall'alto; prospetto = visto di fronte, sulle stesse verticali della pianta. Campiture: in pianta le superfici orizzontali, nei prospetti quelle verticali; le inclinate restano bianche (in pianta con la freccia che scende).

## 2. Geometria proiettiva e omologia (6 e 8 ottobre)

**Definizioni da sapere**

- Lettere: punti maiuscole (P), rette minuscole latine (r), piani minuscole greche (α).
- Proprietà proiettive: appartenenza (P ∈ r → P′ ∈ r′), allineamento, incidenza.
- Enti impropri: due rette parallele si incontrano in un punto improprio, che si disegna con la lineetta della sua direzione.
- Centro proprio → proiezioni coniche (prospettiva); centro improprio → proiezioni cilindriche (proiezioni ortogonali, assonometria).
- **Omologia** = prodotto di due prospettività: la stessa figura proiettata da due centri sullo stesso piano. È definita da centro U, asse u e una coppia di elementi corrispondenti (due punti o due rette). Il corrispondente di una figura è uno solo.
- Notazione: centro U (punto), asse u (retta), corrispondenti con l'apice (A → A′, r → r′). U∞ con la lineetta della direzione; u∞ con la crocetta.

> [!abstract] Da sapere a memoria: l'omologia
> 1. I punti corrispondenti sono allineati con il centro U.
> 2. Le rette corrispondenti si incontrano sull'asse u (nel punto unito, che corrisponde a se stesso).
>
> | Caso | Centro | Asse | Che cosa cambia nella costruzione |
> |---|---|---|---|
> | omologia classica | U proprio | u proprio | nulla |
> | omologia speciale | U sull'asse | u proprio | nulla: i raggi partono da un punto dell'asse |
> | affinità (ortogonale/obliqua) | U∞ | u proprio | al posto del raggio da U, la parallela alla direzione di U∞ (perpendicolare all'asse: ortogonale; inclinata: obliqua) |
> | omotetia | U proprio | u∞ | rette corrispondenti parallele: al posto del punto unito, la parallela |
> | traslazione | U∞ | u∞ | tutte e due le regole; la figura si sposta uguale |

**Come si risolve** (metodo generale: «se ho i punti cerco le rette, se ho le rette cerco i punti»; [[02-proiezioni-e-omologia-schema#Il metodo|bozza 02]])

*Omologia classica, dati U, u, A e A′: trovare B′* ([[02-proiezioni-e-omologia-schema#COME SI RISOLVONO GLI ESERCIZI DI OMOLOGIA|bozza 02]])
1. Traccia il raggio da U per B: B′ starà lì sopra.
2. Traccia la retta AB e prolungala fino all'asse: punto unito V.
3. Unisci V con A′: è la retta corrispondente A′B′.
4. B′ è dove questa retta incontra il raggio UB.

*Date le rette corrispondenti r e r′: trovare P′* ([[03-proiezioni-ortogonali-punto-e-rette#Dalla prospettività all'omologia|bozza 03]])
1. Prima di tutto una coppia di punti: prendi A su r, raggio da U, dove incontra r′ c'è A′. Se c'è un punto che sta già su due rette (es. intersezione della retta data con r), usa quello: meno linee, meno errori ([[04-rette-e-piani-nelle-varie-posizioni#Trovare la retta corrispondente|bozza 04]]).
2. Retta per A e P fino all'asse: punto unito W.
3. W con A′ dà la retta corrispondente; P′ è dove incontra il raggio UP.

*Data la figura ABC e la coppia A, A′: trovare A′B′C′* ([[07-il-ribaltamento#L'esercitazione guidata sulle omologie|bozza 07, es. 3 e 5]])
1. Prolunga il lato AC fino all'asse; unisci quel punto con A′; C′ è sull'incontro con il raggio per C.
2. Prolunga AB fino all'asse; unisci con A′; B′ sul raggio per B.
3. Verifica: BC e B′C′ si incontrano sull'asse.

*Omologia speciale* (U sull'asse): stessi passaggi ([[02-proiezioni-e-omologia-schema#L'omologia speciale|bozza 02]]).

*Affinità* (U∞, u proprio) ([[02-proiezioni-e-omologia-schema#L'affinità ortogonale e obliqua|bozza 02]]; [[04-rette-e-piani-nelle-varie-posizioni#La figura corrispondente|bozza 04]])
1. La direzione di U∞ è quella di AA′ (o quella data con la lineetta).
2. Lato prolungato fino all'asse → punto unito → unisci con il vertice già trovato.
3. Il nuovo vertice sta sulla parallela alla direzione di U∞ condotta dal vertice di partenza.
4. Se la direzione di U∞ è parallela all'asse (omologia affine speciale) si procede uguale.

*Omotetia* (U proprio, u∞) ([[02-proiezioni-e-omologia-schema#L'omotetia|bozza 02]]; [[07-il-ribaltamento#L'esercitazione guidata sulle omologie|bozza 07, es. 2 e 4]])
1. Trova la coppia A, A′ sul raggio da U (A su r, A′ su r′).
2. Unisci P con A; per A′ traccia la **parallela** a PA.
3. P′ è dove la parallela incontra il raggio UP. Per una retta s: dal punto comune tra s e r trovi P′, poi s′ è la parallela a s per P′.

*Traslazione* (U∞, u∞) ([[02-proiezioni-e-omologia-schema#La traslazione|bozza 02]]; [[07-il-ribaltamento#L'esercitazione guidata sulle omologie|bozza 07, es. 1]])
1. M su r; parallela alla direzione di U∞ fino a r′: M′.
2. Unisci P con M; per M′ la parallela a PM.
3. Da P la parallela alla direzione di U∞: dove incontra la retta del passo 2 c'è P′. PMM′P′ è un parallelogramma.

*Verifica finale di ogni esercizio*: rifallo con un'altra coppia di punti, il risultato deve essere lo stesso.

## 3. Proiezioni ortogonali: il punto e le rette proiettanti (8 ottobre)

- Piani di proiezione: π₁ orizzontale, π₂ verticale di fronte, π₃ verticale di lato. Dopo il ribaltamento dei piani: π₁ ≡ π₂ ≡ π₃.
- LT = intersezione tra π₁ e π₂; linea verticale = intersezione tra π₂ e π₃.
- **Notazione**: proiezioni con i pedici P₁ P₂ P₃, r₁ r₂ r₃. Gli apici (P′) solo per omologia e prospettiva; P₁′ per l'assonometria.
- **Aggetto** = distanza del punto da π₂ (P₁ dalla LT). **Quota** = distanza da π₁ (P₂ dalla LT). P₁ e P₂ sulla stessa linea di richiamo, perpendicolare alla LT ([[03-proiezioni-ortogonali-punto-e-rette#Aggetto, quota e linea di richiamo|bozza 03]]).
- Prospetto: si guarda sempre da fuori. Per il lato in alto della pianta la LT va in alto e il prospetto si disegna a testa in giù ([[03-proiezioni-ortogonali-punto-e-rette#LE PROIEZIONI ORTOGONALI|bozza 03]]).
- **Retta proiettante in prima** (⊥ π₁): r₁ ≡ T₁ᵣ ≡ P₁ (un punto); r₂ e r₃ perpendicolari alla LT; T₂ᵣ∞, T₃ᵣ∞ ([[03-proiezioni-ortogonali-punto-e-rette#La retta proiettante in prima|bozza 03]]).
- **Retta proiettante in seconda** (⊥ π₂): m₂ ≡ T₂ₘ (un punto); m₁ perpendicolare alla LT; m₃ parallela alla LT; T₁ₘ∞, T₃ₘ∞. Proiezioni a tratto continuo ([[03-proiezioni-ortogonali-punto-e-rette#La retta proiettante in seconda|bozza 03]]).

**Come si risolve: trovare la terza proiezione di un punto** ([[03-proiezioni-ortogonali-punto-e-rette#La terza proiezione|bozza 03]])
1. Da P₁ vai in orizzontale fino alla linea verticale.
2. Compasso puntato nell'incrocio tra LT e verticale: giri l'arco fino alla LT (a destra).
3. Da lì sali in verticale.
4. Da P₂ tiri l'orizzontale: dove incontra la verticale c'è P₃ (stessa quota di P₂).

## 4. Rette e piani nelle varie posizioni (13 ottobre)

- Il nome di retta e piano dipende dalla posizione rispetto a π₁ e π₂.
- **Traccia di una retta** = punto in cui buca un piano di proiezione: T₁ᵣ, T₂ᵣ, T₃ᵣ. Una retta ha sempre tre tracce; se è parallela a un piano, quella traccia è all'infinito e si segna con la lineetta nella direzione della retta.
- Le proiezioni della retta passano per le proiezioni delle tracce; le proiezioni delle tracce sulla LT si scrivono tra parentesi: (T₁ᵣ)₂, (T₂ᵣ)₁ ([[04-rette-e-piani-nelle-varie-posizioni#Il nome della retta, le tracce e le proiezioni|bozza 04]]).
- **Traccia di un piano** = retta: t₁α, t₂α, t₃α. Il piano non è una figura: si rappresenta con le tracce.

> [!abstract] Da sapere a memoria: rette e piani particolari
> | Retta | Tracce proprie | All'infinito | Riconoscerla |
> |---|---|---|---|
> | parallela alla LT | T₃ᵣ | T₁ᵣ∞, T₂ᵣ∞ | r₁ e r₂ parallele alla LT |
> | frontale f | T₁f, T₃f | T₂f∞ | **f₁ parallela alla LT**, f₂ inclinata |
> | orizzontale o | T₂ₒ, T₃ₒ | T₁ₒ∞ | **o₂ parallela alla LT**, o₁ inclinata |
> | di profilo | T₁ᵣ, T₂ᵣ | T₃ᵣ∞ | r₁ e r₂ sulla stessa perpendicolare alla LT; si vede solo in r₃ |
>
> | Piano | t₁ | t₂ | t₃ |
> |---|---|---|---|
> | parallelo alla LT | ∥ LT | ∥ LT | inclinata |
> | frontale | ∥ LT | t₂∞ | verticale |
> | orizzontale | t₁∞ | ∥ LT | sulla stessa linea di t₂ |
> | di profilo | ⊥ LT | ⊥ LT (stessa linea) | t₃∞ |
> | proiettante in prima | inclinata | ⊥ LT | verticale |
> | proiettante in seconda | ⊥ LT | inclinata | ∥ LT |
> | generico | inclinata | inclinata | inclinata (triangolo delle tracce) |

> [!abstract] Da sapere a memoria: le condizioni di appartenenza
> - **Punto/retta**: P ∈ r se P₁ ∈ r₁ e P₂ ∈ r₂ (proiezioni).
> - **Retta/piano**: r ⊂ α se le tracce di r stanno sulle tracce omonime di α (T₁ᵣ ∈ t₁α, T₂ᵣ ∈ t₂α, T₃ᵣ ∈ t₃α). Se una traccia di r è all'infinito, la proiezione di r è parallela alla traccia omonima del piano.
> - **Punto/piano**: P ∈ α se P sta su una retta di α.
> - Coincidenze (non sono la regola): piani verticali → prima proiezione di tutto sulla t₁; piano proiettante in seconda e piano orizzontale → seconda proiezione sulla t₂; piano parallelo alla LT → terze proiezioni sulla t₃.

**Come si risolve: figura data in prima e seconda proiezione, trovare la terza e dire che piano è** ([[04-rette-e-piani-nelle-varie-posizioni#La terza proiezione della figura|bozza 04]])
1. Un punto alla volta: da A₁ in orizzontale alla verticale, arco fino alla LT, su fino alla quota di A₂: A₃.
2. Ripeti per gli altri vertici; scrivi le coincidenze (es. A₃ ≡ B₃).
3. Se la terza proiezione è un segmento, la figura sta in un piano parallelo alla LT e quel segmento sta sulla t₃.

## 5. Piano proiettante in seconda, retta e piano generico, appartenenza (15 ottobre)

- **Retta generica**: tutte le tracce proprie. r₁ passa per T₁ᵣ e (T₂ᵣ)₁; r₂ passa per T₂ᵣ e (T₁ᵣ)₂ ([[05-appartenenza-e-rette-ausiliarie#Le proiezioni a partire dalle tracce|bozza 05]]).
- **Piano generico**: le tre tracce formano il triangolo delle tracce; t₁α e t₂α si incontrano sulla LT ([[05-appartenenza-e-rette-ausiliarie#Il triangolo delle tracce|bozza 05]]).
- Nel piano generico: **o₁ ∥ t₁α** (orizzontale), **f₂ ∥ t₂α** (frontale). Non ci sta una retta proiettante in prima ([[05-appartenenza-e-rette-ausiliarie#Le rette che appartengono al piano generico|bozza 05]]).
- Piani ausiliari = proiettante in prima e proiettante in seconda: per una retta generica t₁α ≡ r₁ oppure t₂β ≡ r₂ ([[05-appartenenza-e-rette-ausiliarie#La retta generica nei piani ausiliari|bozza 05]]).
- Piani che contengono una retta ([[05-appartenenza-e-rette-ausiliarie#I PIANI CHE CONTENGONO UNA RETTA|bozza 05]]): proiettante in prima → frontale, di profilo, proiettanti in prima · proiettante in seconda → proiettante in seconda, orizzontale, di profilo · parallela alla LT → parallelo alla LT, frontale, orizzontale · orizzontale → orizzontale, generico (t₁ ∥ o₁), proiettante in prima (t₁ ≡ o₁) · frontale → frontale, generico (t₂ ∥ f₂), proiettante in seconda (t₂ ≡ f₂) · di profilo → di profilo, parallelo alla LT, generico (t₃ ∥ m₃).

**Come si risolve: data la prima proiezione di una figura su un piano proiettante in seconda, trovare la seconda e la terza** ([[05-appartenenza-e-rette-ausiliarie#IL PIANO PROIETTANTE IN SECONDA|bozza 05]])
1. Da ogni vertice sali con la linea di richiamo fino a t₂α: lì ci sono A₂, B₂, C₂ (segna le coincidenze).
2. Calca sulla traccia il tratto della figura.
3. Terza proiezione come per il punto (orizzontale, arco, su; dalla seconda in orizzontale).

**Come si risolve: trovare le tracce di una retta date le proiezioni** ([[06-piani-ausiliari-e-perpendicolarita#I punti notevoli della retta generica sulla linea di terra|bozza 06]])
1. Prolunga r₂ fino alla LT: è (T₁ᵣ)₂. Scendi con il richiamo fino a r₁: lì c'è T₁ᵣ.
2. Prolunga r₁ fino alla LT: è (T₂ᵣ)₁. Sali con il richiamo fino a r₂: lì c'è T₂ᵣ.
3. Le tracce possono cadere anche dall'altra parte della LT: il procedimento è lo stesso.
4. Terza traccia: prolunga r₃ (tratteggiata dietro π₂) oppure, più sicuro, usa il piano ausiliario proiettante in prima con t₁α ≡ r₁ ([[05-appartenenza-e-rette-ausiliarie#La terza traccia|bozza 05]]).

**Come si risolve: la retta r appartiene al piano α?** ([[05-appartenenza-e-rette-ausiliarie#La retta r appartiene al piano?|bozza 05]])
1. Trova T₁ᵣ e T₂ᵣ come sopra.
2. Se T₁ᵣ ∈ t₁α **e** T₂ᵣ ∈ t₂α, sì; se anche una sola non ci sta, no.

**Come si risolve: disegnare un punto P del piano generico α** ([[05-appartenenza-e-rette-ausiliarie#Disegnare un punto del piano con l'orizzontale|bozza 05]])
1. o₂ parallela alla LT: dove incontra t₂α c'è T₂ₒ.
2. Da T₂ₒ scendi alla LT: (T₂ₒ)₁.
3. Da (T₂ₒ)₁ traccia o₁ parallela a t₁α (T₁ₒ∞ sta su t₁α).
4. P₂ su o₂, scendi fino a o₁: P₁. P ∈ o ⊂ α.
- Con la frontale: f₁ ∥ LT fino a t₁α (T₁f), sali alla LT ((T₁f)₂), f₂ ∥ t₂α, P₂ su f₂ e P₁ su f₁ ([[05-appartenenza-e-rette-ausiliarie#Disegnare un punto del piano con la frontale|bozza 05]]).

**Come si risolve: il punto P appartiene ad α?** ([[05-appartenenza-e-rette-ausiliarie#IL PUNTO CHE APPARTIENE A UN PIANO|bozza 05]])
1. Disegna una retta del piano che passi per P₂: r₂ per P₂, T₂ᵣ dove incontra t₂α.
2. r₂ alla LT: (T₁ᵣ)₂; scendi fino a t₁α: T₁ᵣ. Da T₂ᵣ scendi alla LT: (T₂ᵣ)₁. r₁ passa per (T₂ᵣ)₁ e T₁ᵣ.
3. Da P₂ scendi: se P₁ cade su r₁, P ∈ α; se no, P ∉ α.

**Come si risolve: punto in un piano proiettante** ([[06-piani-ausiliari-e-perpendicolarita#Un punto che appartiene ai piani proiettanti|bozza 06]])
1. Proiettante in prima: P₁ su t₁α, P₂ dove vuoi sulla stessa linea di richiamo; dimostralo con la retta verticale (r₁ ≡ T₁ᵣ ≡ P₁ su t₁α) o con l'orizzontale (o₁ ≡ t₁α, T₂ₒ su t₂α).
2. Proiettante in seconda: P₂ su t₂α, P₁ dove vuoi; dimostralo con la frontale (f₁ ∥ LT fino a t₁α, f₂ ≡ t₂α).

**Come si risolve: data la prima proiezione della figura e le tracce di un piano generico, trovare la seconda** ([[05-appartenenza-e-rette-ausiliarie#Dalla prima proiezione e dalle tracce, la seconda proiezione della figura|bozza 05]])
1. Prolunga un lato, es. A₁C₁ = r₁: incontra t₁α in T₁ᵣ e la LT in (T₂ᵣ)₁.
2. Da (T₂ᵣ)₁ sali a t₂α: T₂ᵣ. Da T₁ᵣ sali alla LT: (T₁ᵣ)₂. r₂ passa per T₂ᵣ e (T₁ᵣ)₂.
3. Da A₁ e C₁ sali fino a r₂: A₂ e C₂.
4. Ripeti con un altro lato per B₂ (il vertice comune fa da controllo).
- Variante con le orizzontali (falda del tetto: lato parallelo a t₁α = orizzontale) ([[05-appartenenza-e-rette-ausiliarie#ESERCIZI TIPO DELLE SCHEDE|bozza 05]]).

## 6. Piani ausiliari, figure piane e perpendicolarità (20 ottobre)

- Strumenti per tutto: due piani ausiliari (proiettante in prima e in seconda) e due rette ausiliarie (orizzontale e frontale), da disegnare subito, senza esitare.
- Forma mongiana (con le tracce) e forma tecnica (il piano dato da una figura, senza tracce): è indifferente.
- Lati della figura: se una proiezione contiene due lettere, l'altra contiene le stesse. Due proiezioni inclinate → retta generica.

> [!abstract] Da sapere a memoria: riconoscere il piano di una figura
> - Seconda proiezione ridotta a un segmento ∥ LT → piano orizzontale; inclinato → proiettante in seconda.
> - Prima proiezione ridotta a un segmento ∥ LT → piano frontale; inclinato → proiettante in prima.
> - Tutte e due ridotte a segmenti (perpendicolari alla LT) → piano di profilo.
> - Due proiezioni «piene» → generico **oppure** parallelo alla LT: si decide ragionando sulle rette dei lati.
> - Vera grandezza: piano orizzontale in prima proiezione, frontale in seconda, di profilo in terza.
>
> ([[06-piani-ausiliari-e-perpendicolarita#Il piano non è generico di per sé|bozza 06]])

> [!abstract] Da sapere a memoria: la perpendicolarità
> - **Teorema di Monge**: r ⊥ α se r₁ ⊥ t₁α e r₂ ⊥ t₂α.
> - **Senza tracce**: r ⊥ piano della figura se r₁ ⊥ o₁ e r₂ ⊥ f₂ (orizzontale e frontale della figura).
> - Due piani sono perpendicolari se uno contiene una retta perpendicolare all'altro.
> - Due proiettanti in prima sono perpendicolari se lo sono le prime tracce; due proiettanti in seconda se lo sono le seconde tracce.
> - Piano facile perpendicolare a un generico α: proiettante in prima γ con t₁γ ⊥ t₁α.

**Come si risolve: tracce del piano date le proiezioni di una figura** ([[06-piani-ausiliari-e-perpendicolarita#Dalle proiezioni della figura alle tracce del piano|bozza 06]])
1. Dai un nome alle rette di due lati (r, s) e riconoscile.
2. Per ognuna trova T₁ e T₂ (prolunga fino alla LT, richiamo).
3. t₁α passa per T₁ᵣ e T₁ₛ; t₂α per T₂ᵣ e T₂ₛ. Controllo: si incontrano sulla LT; le tracce del terzo lato ci cadono sopra.
4. Se un lato è orizzontale o frontale, una traccia è all'infinito: t₁α passa per T₁f ed è **parallela a o₁**; t₂α passa per T₂ₒ ed è **parallela a f₂**.

**Come si risolve: un punto nel piano della figura (forma tecnica)** ([[06-piani-ausiliari-e-perpendicolarita#L'orizzontale della figura|bozza 06]])
1. Da A₂ traccia o₂ parallela alla LT: incontra B₂C₂ in H₂.
2. Scendi con il richiamo fino a B₁C₁: H₁.
3. o₁ passa per A₁ e H₁. Ogni punto di o (P₂ su o₂, P₁ su o₁) sta nel piano.

**Come si risolve: retta perpendicolare a un piano** ([[06-piani-ausiliari-e-perpendicolarita#LA PERPENDICOLARITÀ|bozza 06]])
1. Con le tracce: dal punto dato, r₂ ⊥ t₂α e r₁ ⊥ t₁α (segna gli angoli retti).
2. Senza tracce: costruisci l'orizzontale o e la frontale f della figura; r₁ ⊥ o₁ e r₂ ⊥ f₂. Usa colori diversi per o, f, r.

**Come si risolve: piano perpendicolare a un piano generico** ([[06-piani-ausiliari-e-perpendicolarita#Un piano perpendicolare a un piano generico|bozza 06]])
1. Disegna γ proiettante in prima con t₁γ ⊥ t₁α (90° segnati) e t₂γ ⊥ LT.
2. Dimostra con l'orizzontale di α: o₁ ∥ t₁α è ⊥ t₁γ, o₂ ∥ LT è ⊥ t₂γ, quindi o ⊥ γ.

## 7. Il ribaltamento dei piani proiettanti (22 ottobre)

- Si ribalta per vedere la vera grandezza e forma di una figura che sta su un piano proiettante.
- La cerniera (asse di rotazione) è sempre una traccia. Ogni punto ruota su un arco che sta in un piano perpendicolare alla traccia, con il centro sulla traccia.
- Il punto ribaltato si scrive con l'asterisco: A\*.
- **Omologia di ribaltamento**: tra la proiezione e il ribaltamento c'è un'affinità; asse = traccia-cerniera, centro all'infinito nella direzione perpendicolare all'asse. Una retta della figura e la sua ribaltata si incontrano sulla cerniera (es. nella prima traccia della retta) ([[07-il-ribaltamento#L'OMOLOGIA DI RIBALTAMENTO|bozza 07]]).

> [!abstract] Da sapere a memoria: i quattro ribaltamenti
> | Piano | Su | Cerniera | Che cosa si conserva / si riporta |
> |---|---|---|---|
> | proiettante in prima | π₁ | t₁α | sulla perpendicolare a t₁α da A₁ si riporta la **quota** |
> | proiettante in prima | π₂ | t₂α | la **quota** non cambia (la maniglia della porta) |
> | proiettante in seconda | π₁ | t₁α | l'**aggetto** non cambia |
> | proiettante in seconda | π₂ | t₂α | sulla perpendicolare a t₂α da A₂ si riporta l'**aggetto** |
>
> Su π₁ e su π₂ la figura ribaltata deve venire identica.

**Come si risolve: proiettante in prima su π₁** ([[07-il-ribaltamento#Il ribaltamento su π₁ intorno alla prima traccia|bozza 07]])
1. A₁, B₁, C₁ stanno su t₁α. La t₂α non serve.
2. Da A₁ traccia la perpendicolare a t₁α.
3. Con il compasso prendi la quota di A (distanza di A₂ dalla LT) e riportala da A₁: A\*.
4. Ripeti per B e C, con una, due, tre lineette sui segmenti uguali. A\*B\*C\* è la vera grandezza.

**Come si risolve: proiettante in prima su π₂** ([[07-il-ribaltamento#IL PIANO PROIETTANTE IN PRIMA|bozza 07]])
1. K = punto dove t₂α incontra la LT. Compasso in K, raggio KA₁: l'arco porta A₁ sulla LT.
2. Da lì sali fino alla quota di A₂: A\*.

**Come si risolve: proiettante in seconda su π₁** ([[07-il-ribaltamento#IL PIANO PROIETTANTE IN SECONDA|bozza 07]])
1. A₂, B₂, C₂ stanno su t₂α. K = punto dove t₁α incontra la LT.
2. Compasso in K, raggio KA₂: l'arco porta A₂ sulla LT.
3. Da lì scendi alla stessa distanza dalla LT di A₁ (l'aggetto): A\*.

**Come si risolve: proiettante in seconda su π₂** ([[07-il-ribaltamento#Il ribaltamento su π₂ intorno alla seconda traccia|bozza 07]])
1. Da A₂ traccia la perpendicolare a t₂α.
2. Riporta l'aggetto di A (distanza di A₁ dalla LT): A\*.

**Come si risolve: un punto sulla retta di profilo** ([[07-il-ribaltamento#Un punto sulla retta di profilo, con il ribaltamento|bozza 07]]; con la terza proiezione: [[04-rette-e-piani-nelle-varie-posizioni#La retta di profilo|bozza 04]])
1. Ribalta il piano di profilo su π₂: compasso nel piede della verticale, l'arco porta T₁ᵣ sulla LT; r\* unisce quel punto con T₂ᵣ.
2. Scegli P\* su r\*: in orizzontale fino alla verticale trovi P₂ (la quota non cambia).
3. Da P\* scendi alla LT e con il compasso riporta la distanza sotto la LT: P₁.

> [!warning] Errori da evitare (segnalati dalla docente)
> - **Lettere mancanti**: «se non ci sono le lettere viene considerato un errore» (13 ottobre). Usa le stesse lettere della docente; se una proiezione ha due lettere, l'altra ha le stesse.
> - **Lineette di uguaglianza mancanti** sulle misure riportate: «se voi non mettete l'uguaglianza, io metto errore» (22 ottobre).
> - **Linee di costruzione cancellate**: non si arriva all'esame con un disegno senza costruzioni. Devono restare leggere ma visibili, e la retta/figura più marcata.
> - **Prospetto al contrario**: LT messa dalla parte sbagliata, prospetto specchiato, «come guardare l'edificio da dentro». Errore che «si ripete e rimane anche dopo».
> - **Lineetta del punto improprio messa a caso** (U∞, T₂f∞...): la lineetta è la direzione.
> - **Proiezioni tratteggiate**: le proiezioni sono a tratto continuo; si tratteggia solo ciò che è nascosto (la retta dietro un piano).
> - **Vignette separate** dalla linea verticale: le proiezioni partono dalle linee di intersezione dei piani, come sul modello aperto.
> - **Confondere tracce e proiezioni**: le condizioni retta/piano parlano di tracce, quella punto/retta di proiezioni. La proiezione di un punto cade sulla traccia solo nei piani proiettanti (coincidenza, non regola).
> - Far passare il piano per **una sola** traccia della retta: le tracce devono stare tutte sulle tracce omonime.
> - Dire «è generico» solo perché si vedono due proiezioni: può essere parallelo alla LT.
> - Disegnare l'orizzontale con la prima proiezione verticale: l'orizzontale ha la **seconda** proiezione parallela alla LT.
> - Angolo retto non segnato; disegni troppo piccoli.
> - Nell'omologia: tracciare linee inutili («meno se ne tracciano, meno l'errore grafico è in agguato») e cercare di figurarsi lo spazio: gli esercizi si risolvono sul piano con le due proprietà.

> [!tip] Cosa portare
> Dalla lista «Da portare sempre a lezione» (FAGD): portamine 2 mm (mine H, 2H, B) con temperamine; portamine 0,5 mm (mine B, 2B); matite in legno (HB, B, 2B); tre matite colorate che si cancellino bene; **due squadrette piccole**; **un compasso** (serve per la terza proiezione e per i ribaltamenti); gomma buona e gomma pane; alcuni fogli A4 da 80 g e un paio di fogli A4 di cartoncino; il blocco degli appunti 23 × 30. Il modellino dei piani di riferimento va portato sempre a lezione: chiedi alla docente se serve anche alla prova.

## Collegamenti

La prova mette insieme le due anime della prima parte del corso. L'[[02-proiezioni-e-omologia-schema|omologia]] fornisce le regole (punti allineati con il centro, rette che si incontrano sull'asse) che tornano nel [[07-il-ribaltamento|ribaltamento]] come affinità tra proiezione e figura ribaltata. Il metodo di Monge, dal [[03-proiezioni-ortogonali-punto-e-rette|punto e le rette proiettanti]] alle [[04-rette-e-piani-nelle-varie-posizioni|rette e i piani nelle varie posizioni]], si regge sulle [[05-appartenenza-e-rette-ausiliarie|condizioni di appartenenza]] e sulle rette ausiliarie, che a loro volta risolvono la [[06-piani-ausiliari-e-perpendicolarita|perpendicolarità]]. Le [[01-strumenti-materiali-e-regole|regole del segno]] valgono per ogni esercizio: lettere, lineette e costruzioni visibili fanno parte della risposta.
