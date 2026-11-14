---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-11-10
tags: [geometria-descrittiva, bozza]
---

# L'assonometria cavaliera militare e le sezioni dei solidi

> [!info] Note collegate
> Sbobina: [[11-assonometria-obliqua-cavaliera-militare]]
>
> Bozza precedente: [[10-intersezione-retta-piano-e-segno-di-sezione]]
>
> Argomenti collegati: [[07-il-ribaltamento]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[02-affinita-ortogonale-passo-passo]] · [[PO 7 - Figure piane e solidi]]

La lezione di martedì 10 novembre, registrata in due parti, ha due argomenti.

Nella prima parte la docente riprende l'assonometria ortogonale e passa all'assonometria obliqua, in particolare a quella che si usa di più, la cavaliera militare:

- come si sceglie l'unità di misura sull'asse z′,
- come si trova la direzione di proiezione ribaltando l'asse z,
- come si riducono graficamente tutte le altezze, con un esercizio in aula su un prisma a pianta rettangolare.

Nella seconda parte comincia le sezioni dei solidi:

- la regola generale, da scrivere sul quaderno,
- un parallelepipedo tagliato da un piano parallelo alla linea di terra, prima in proiezioni ortogonali e poi in cavaliera militare,
- un parallelepipedo tagliato da un piano verticale.

L'assonometria è l'argomento della Prova n. 2, che il calendario aggiornato fissa a giovedì 26 novembre.

## L'ASSONOMETRIA ORTOGONALE: RIPASSO

### Il triangolo delle tracce e l'ortocentro

Nell'assonometria ortogonale il quadro, cioè il piano su cui si proietta, è in posizione generica rispetto alla terna degli assi x, y, z, e la direzione di proiezione è perpendicolare al quadro.

Il quadro taglia i tre assi in tre punti, X, Y e Z: il triangolo che li unisce si chiama triangolo delle tracce.

Proprio perché la proiezione è ortogonale, la proiezione dell'origine degli assi, O′, cade nell'ortocentro del triangolo, cioè nel punto in cui si incontrano le sue altezze.

Per trovarlo si mandano dai vertici del triangolo le perpendicolari ai lati opposti: dove si incontrano c'è O′, e gli assi assonometrici x′, y′, z′ sono le rette che da O′ vanno ai vertici, cioè stanno sulle altezze del triangolo.

È una condizione importante, perché permette di capire quale assonometria si può disegnare.

> [!example] Disegno 1 · Il disegno nello spazio: il quadro taglia i tre assi
> ![[b11-spazio-ortogonale-triangolo-tracce.svg|620]]
>
> 1. Il triedro di riferimento ha gli assi x, y, z, che si incontrano nell'origine O.
> 2. Il quadro (in blu) taglia gli assi in X, Y e Z: il triangolo XYZ è il triangolo delle tracce.
> 3. Da O si manda la proiettante perpendicolare al quadro (tratteggio rosso): lo buca in O′.
> 4. O′ è l'ortocentro del triangolo XYZ. Le rette O′X, O′Y, O′Z sono le proiezioni degli assi, cioè gli assi assonometrici x′, y′, z′.

### Isometria, dimetria, trimetria

Nello spazio le unità di misura su x, y e z sono uguali.

Nell'assonometria ortogonale, invece, le unità di misura subiscono sempre un accorciamento e mai un allungamento, proprio perché la proiezione è ortogonale.

Di quanto si accorciano dipende dalla forma del triangolo delle tracce, che può essere equilatero, isoscele o scaleno:

- triangolo equilatero: l'accorciamento è uguale su tutti e tre gli assi, e l'assonometria è isometrica;
- triangolo isoscele: l'accorciamento è uguale su due assi e diverso sul terzo, e l'assonometria è dimetrica;
- triangolo scaleno: l'accorciamento è diverso su tutti e tre gli assi, e l'assonometria è trimetrica.

La docente dice che disegnerà quasi sempre un triangolo scaleno, oppure un isoscele un po' più largo, con una variazione più piccola sugli assi.

### Come si trovano gli accorciamenti: il ribaltamento dei piani coordinati

Trovato O′, bisogna ancora trovare l'accorciamento delle unità di misura sugli assi.

Il procedimento è quello della scheda Esercizio guidato ASSONOMETRIA_ORTOGONALE, e si basa sul [[07-il-ribaltamento|ribaltamento]].

Ognuna delle tre facce del triedro, per esempio la faccia xOy, è un triangolo rettangolo in O che ha un lato sul quadro: per la faccia xOy è il lato XY.

Si ribalta la faccia sul quadro facendola ruotare intorno a XY, che fa da cerniera:

- il vertice O ribaltato, O\*, sta sulla perpendicolare a XY condotta da O′, perché nel ribaltamento ogni punto si muove su un piano perpendicolare alla cerniera;
- inoltre O\* vede il lato XY sotto un angolo retto, perché l'angolo in O è di 90 gradi: quindi sta sulla semicirconferenza che ha XY come diametro.

O\*X e O\*Y sono gli assi ribaltati x\* e y\*, e su di loro le misure sono vere.

Si prende allora l'unità di misura vera, la si segna su x\* e su y\* (nella scheda u\*x e u\*y) e la si riporta sugli assi assonometrici con le perpendicolari alla cerniera XY: si trovano le unità accorciate su x′ e su y′.

Tra la faccia ribaltata e la sua proiezione c'è infatti un'[[02-affinita-ortogonale-passo-passo|affinità ortogonale]], che ha per asse la cerniera.

Per l'asse z si fa lo stesso con un'altra faccia, per esempio yOz, ribaltata intorno al lato YZ: si trova z\* e da lì l'unità accorciata su z′.

> [!example] Disegno 2 · Il disegno: il triangolo delle tracce e i ribaltamenti (come nella scheda della docente)
> ![[b11-ortogonale-ribaltamento-piani-coordinati.svg|620]]
>
> 1. Si disegna il triangolo delle tracce XYZ e se ne tracciano le altezze: si incontrano in O′. Da O′ partono gli assi x′, y′, z′, che passano per i vertici.
> 2. Faccia xOy: si disegna la semicirconferenza di diametro XY, dalla parte opposta a Z.
> 3. Si prolunga z′ oltre O′ (è la perpendicolare a XY): dove incontra la semicirconferenza c'è O\*.
> 4. Si uniscono O\* con X e con Y: sono x\* e y\*, ad angolo retto.
> 5. Si segna l'unità vera u\*x su x\* e u\*y su y\* e la si riporta su x′ e su y′ con le perpendicolari a XY: si trovano u′x e u′y, più corte.
> 6. Faccia yOz: lo stesso con la semicirconferenza di diametro YZ e la perpendicolare a YZ da O′ (il prolungamento di x′). Si trova un altro O\*, gli assi y\* e z\* e da u\*z l'unità accorciata u′z.
> 7. Le tre unità accorciate sono diverse tra loro: il triangolo è scaleno e l'assonometria è trimetrica.

## L'ASSONOMETRIA OBLIQUA

### Ortogonale e obliqua: la direzione di proiezione

Quando la direzione di proiezione è obliqua rispetto al quadro, si ottiene un'assonometria obliqua.

Gli aggettivi ortogonale e obliqua si riferiscono quindi alla direzione di proiezione rispetto al quadro, non all'angolo tra gli assi.

### L'assonometria obliqua generica

Se il quadro è in posizione generica rispetto alla terna degli assi, l'assonometria si chiama obliqua generica, e non si usa mai.

Il motivo è che, non essendo ortogonale la proiezione, il punto O′ non è più l'ortocentro del triangolo delle tracce. Bisognerebbe quindi fare un'operazione in più:

- trovare un'affinità tra il ribaltamento e il piano di quadro, che paradossalmente non è un'affinità ortogonale ma obliqua, e cercarne la direzione;
- oppure considerare la proiezione ortogonale del centro di proiezione.

Non è un'operazione complicata, ma richiede più passaggi.

### Il quadro coincide con un piano coordinato: la cavaliera militare

Le assonometrie oblique che si usano, e che si usano moltissimo, sono quelle in cui il piano di quadro coincide con uno dei piani coordinati.

Se il quadro coincide con il piano π₁, cioè con il piano della pianta:

- gli assi x e y stanno già sul quadro e non vengono proiettati, quindi coincidono con x′ e y′;
- l'angolo tra x e y, l'angolo a terra, resta quello che è nello spazio, cioè di 90 gradi;
- le unità di misura su x e su y restano vere e uguali.

Quindi la pianta resta in vera forma.

Questa assonometria, in cui il quadro coincide con il piano della pianta, si chiama cavaliera militare.

Sul foglio la pianta si può girare come si preferisce: la docente la disegna ruotata, con x′ e y′ inclinati e ad angolo retto, perché così è facile disegnare.

Di proiettato in modo obliquo resta solo l'asse z, con la sua unità di misura. Tutto si riduce allora a sapere di quanto si riduce, o anche si ingrandisce, l'unità di misura sull'asse z′ disegnato sul quadro.

### La squadretta: un'unità uguale, minore o maggiore

Per capire che cosa succede conviene prendere il modellino degli assi e una squadretta.

La direzione di proiezione obliqua sta nello spazio. Si immagini una squadretta in piedi sul quadro, senza appoggio, con un cateto lungo l'asse z:

- un cateto è l'unità di misura vera sull'asse z;
- l'altro cateto sta sul quadro ed è l'unità di misura proiettata, su z′;
- l'ipotenusa è la direzione di proiezione assonometrica.

Se la direzione di proiezione è inclinata di 45 gradi, i due cateti della squadretta sono uguali: l'unità su z′ è uguale all'unità vera su z.

Se la direzione ha un angolo diverso, le due unità sono diverse:

- con una direzione più ripida l'unità proiettata è più corta di quella vera;
- con una direzione più inclinata l'unità proiettata è più lunga di quella vera.

L'unità su z′ può quindi essere uguale, maggiore o minore di quella vera.

> [!example] Disegno 3 · Il disegno nello spazio: la squadretta e la direzione di proiezione
> ![[b11-spazio-cavaliera-squadretta.svg|620]]
>
> 1. Il quadro è π₁: gli assi x e y ci stanno sopra e coincidono con x′ e y′, ad angolo retto e con le unità vere.
> 2. L'asse z è verticale; la sua unità va da O a Uz.
> 3. La proiettante obliqua che parte da Uz arriva sul quadro in un punto dell'asse z′. O, Uz e quel punto formano un triangolo rettangolo in O, verticale: è la squadretta.
> 4. A 45 gradi (in verde) i due cateti sono uguali: u′z = u.
> 5. Con una direzione più ripida (in arancio) u′z è più corta di u; con una più inclinata (in viola) è più lunga.

### Il ribaltamento dell'asse z e la direzione s

Come si individua la direzione di proiezione assonometrica? Il triangolo della squadretta sta nello spazio, su un piano verticale, e sul foglio non si vede. Per lavorare sul piano di quadro bisogna ribaltarlo.

Lo si ribalta, anche solo mentalmente o con la squadretta sul modellino, facendolo ruotare intorno a z′:

- nel ribaltamento l'asse z si dispone orizzontalmente, a 90 gradi rispetto a z′, e diventa z\*;
- su z\* l'unità di misura è quella vera, uguale a quella su x e su y, perché nello spazio le unità sono uguali su tutti e tre gli assi;
- la si riporta su z\* con il compasso, con un arco che parte dall'unità segnata su x′.

Ora si conoscono i due cateti della squadretta ribaltata: l'unità vera su z\* e l'unità scelta su z′.

Il segmento che li unisce è la direzione di proiezione ribaltata, che si chiama s. Negli schemi è segnata s\*, con l'asterisco degli elementi ribaltati.

Negli esercizi si lavora sempre con questa direzione ribaltata, che sta sul foglio, e non con quella che sta in aria.

Con s tutte le altezze si riducono allo stesso modo:

1. si prende l'altezza vera su z\*;
2. dal punto trovato si conduce la parallela a s;
3. dove la parallela incontra z′ c'è l'altezza ridotta.

È un metodo grafico: le altezze ridotte si ricavano senza fare operazioni con la calcolatrice.

> [!example] Disegno 4 · Il disegno: il ribaltamento dell'asse z
> ![[b11-cavaliera-ribaltamento-asse-z.svg|620]]
>
> 1. Sul foglio, che è il quadro, si disegnano x′ (che coincide con x\*) e y′ (che coincide con y\*) ad angolo retto, e z′ in verticale.
> 2. Si segna l'unità u su x′ e su y′ e si segna l'uguaglianza (una lineetta per ogni segmento uguale).
> 3. Su z′ si sceglie l'unità u′z, qui più piccola di u.
> 4. Si ribalta z: z\* è orizzontale, a 90 gradi da z′. Con il compasso centrato in O′ si riporta l'unità u su z\* (l'arco tratteggiato).
> 5. Il segmento che unisce u su z\* con u′z su z′ è la direzione s\*.
> 6. Un'altezza vera h presa su z\* si porta su z′ con la parallela a s\*: si trova l'altezza ridotta h′.

### La scelta dell'unità di misura su z′

Sul foglio si disegna il cateto che sta sul quadro: la proiezione di z è già avvenuta, e la lavagna, o il foglio, coincide con il piano di quadro.

Sugli assi x′ e y′ si mettono le unità di misura vere, uguali: si può mettere proprio un centimetro, oppure disegnare una scala, e poi si segna l'uguaglianza tra x′ e y′.

Su z′ invece l'unità si può scegliere. Per il teorema di Pohlke la terna degli assi si può disegnare in qualunque modo, con le unità di misura che si vogliono: esisterà sempre una direzione di proiezione che la genera.

Geometricamente quindi si potrebbe disegnare un cubo con un'unità su z′ tripla di quella della pianta, e sarebbe corretto. Il cubo però non sembrerebbe più un cubo, e il disegno non avrebbe senso.

Allo stesso modo, se si disegna la casa di Le Corbusier, che è una scatola schiacciata, e la si alza solo perché la geometria lo consente, si sbaglia dal punto di vista della rappresentazione: non si dà ragione di quell'architettura. Geometricamente è fattibile, ma dal punto di vista della rappresentazione no.

La cosa migliore è mettere su z′ un'unità di misura inferiore a quella vera. La cavaliera con l'unità uguale, per un effetto ottico, fa sembrare le cose sempre più alte di quello che sono, e quindi conviene abbassarle un po'.

Lo scopo di tutto il lavoro sul ribaltamento di z è proprio questo: sapere di quanto si sono ridotte le altezze, e ridurle tutte con un metodo grafico.

## L'ESERCIZIO IN CAVALIERA MILITARE

### Impostare il foglio

In aula la docente fa disegnare un solido in cavaliera militare.

Si disegna il sistema di riferimento della cavaliera militare e si sceglie una pianta, che può essere un quadrato, un rettangolo o una figura un po' più complessa; poi si stabilisce l'altezza. La pianta è la base del solido.

L'esempio della docente è un rettangolo di 4 × 2 cm, disegnato abbastanza grande, così la direzione di proiezione sugli assi viene meglio:

- su x′ e su y′ l'unità è di 2 cm, e si segna sempre l'uguaglianza;
- su z′ l'unità è di 1,5 cm.

La pianta si disegna con un segno leggero, senza calcarla, perché poi sarà coperta dal solido.

### L'altezza ridotta

Si ribalta l'asse z, si trova z\* e su z\* si segna l'unità, che è uguale a quella di x e y perché nello spazio le unità sono uguali su tutti gli assi; anche qui si segna l'uguaglianza.

Unendo l'unità su z\* con quella su z′ si trova la direzione s, che accorcia graficamente le altezze.

Si sceglie l'altezza del solido, per esempio 5 cm, e la si colloca su z\*. Poi la si proietta su z′ nella direzione s: quella che si trova è l'altezza ridotta.

Con le unità dell'esempio, 2 cm su z\* e 1,5 cm su z′, i 5 cm veri diventano 3,75 cm.

### I prospetti assonometrici e il solido

In cavaliera militare ci sono quattro proiezioni assonometriche:

- la proiezione assonometrica vera, che in questo caso è proprio il solido;
- la prima proiezione assonometrica, cioè la pianta;
- la seconda proiezione assonometrica, il prospetto su π₂;
- la terza proiezione assonometrica, il prospetto su π₃.

Per disegnare i due prospetti assonometrici:

1. si proietta la pianta su x′ in direzione parallela all'asse y′, cioè perpendicolarmente a x′;
2. dai punti trovati si alzano delle verticali, tutte parallele a z′;
3. la loro altezza è l'altezza ridotta, che si riporta da z′ parallelamente agli assi;
4. lo stesso si fa su y′, proiettando la pianta parallelamente a x′.

L'altezza sta sempre su z. Può capitare, negli esercizi o nelle tavole, di voler mettere l'asse z in un'altra direzione, a seconda di quello che si vuole mostrare: va benissimo, ma in quel caso anche il solido avrà quella direzione, quella di z′.

Infine il solido: dai vertici della pianta si alzano gli spigoli verticali, paralleli a z′ e lunghi quanto l'altezza ridotta, e si chiude la faccia superiore.

L'esercizio è pensato come la costruzione di un plastico, piccolo oppure un po' più grande.

> [!example] Disegno 5 · Il disegno: il prisma con pianta 4 × 2 cm e altezza 5 cm
> ![[b11-cavaliera-esercizio-prisma.svg|620]]
>
> 1. Si disegnano x′ e y′ ad angolo retto e z′ verticale; l'unità è di 2 cm su x′ e y′ (con il segno di uguaglianza) e di 1,5 cm su z′.
> 2. Si disegna la pianta in vera forma, un rettangolo di 4 × 2 cm con i lati paralleli agli assi, con un segno leggero.
> 3. Si ribalta z: su z\* si riporta col compasso l'unità vera di 2 cm. Unendo i 2 cm su z\* con gli 1,5 cm su z′ si trova s\*.
> 4. L'altezza vera, 5 cm, si prende su z\* e si porta su z′ con la parallela a s\* (tratteggio verde): è h′, 3,75 cm.
> 5. Seconda proiezione assonometrica (in arancio): i vertici della pianta si proiettano su x′ parallelamente a y′; da lì si alzano le verticali fino a h′, riportata da z′ con la parallela a x′.
> 6. Terza proiezione assonometrica (in viola): i vertici della pianta si proiettano su y′ parallelamente a x′, poi si alzano fino a h′.
> 7. Il solido (in blu): dai vertici della pianta si alzano gli spigoli verticali lunghi h′ e si chiude la faccia superiore. Gli spigoli che partono dal vertice più vicino all'origine sono nascosti e si tratteggiano.

### L'angolo a terra di 90 gradi e i due metodi

Sul foglio si scrive il titolo: «Assonometria obliqua cavaliera militare, angolo a terra di 90 gradi».

Anche con un angolo diverso da 90 gradi non succederebbe niente: sarebbe semplicemente un'altra assonometria. La docente però usa l'angolo di 90 gradi perché con le squadre si costruisce sempre più facilmente; con un angolo diverso bisognerebbe spostare le squadre continuamente.

La cavaliera militare ha due metodi di soluzione. Si può scegliere quale usare, ma bisogna mostrare di saperli usare entrambi; nelle tavole che la docente fa vedere si usa il prospetto assonometrico.

## LE SEZIONI DEI SOLIDI

### La regola

La regola da scrivere sul quaderno è questa: le sezioni dei solidi si risolvono costruendo, di volta in volta, le intersezioni tra il piano secante e i piani che contengono le facce del solido.

Il piano secante può essere qualunque: un piano generico, un piano proiettante in prima, un piano parallelo alla linea di terra. «Di volta in volta» significa che si considera una faccia alla volta.

Di quello che succede dentro una faccia non si sa nulla, ma la faccia ha i suoi spigoli, e sono quelli che aiutano.

Il procedimento, per ogni faccia, è questo:

1. si considera il piano che contiene la faccia;
2. si trova la retta di intersezione tra questo piano e il piano secante;
3. si cercano i punti in cui la retta di intersezione incontra gli spigoli della faccia che si sta considerando: quelli sono i punti della sezione.

Unendo i punti trovati faccia per faccia si ottiene l'andamento della sezione.

Gli esercizi sulle sezioni sono sempre accoppiati, in assonometria e in proiezioni ortogonali. La sezione è la stessa nei due disegni, e cambia solo la sequenza delle operazioni; nell'assonometria però la sezione si vede, mentre nelle proiezioni ortogonali non si percepisce. Per questo conviene studiare bene le sezioni in assonometria, che sono più facili, e da lì passare alle proiezioni ortogonali.

### Il parallelepipedo tagliato da un piano parallelo alla linea di terra

Il primo caso è un parallelepipedo a base rettangolare, disposto parallelamente rispetto a π₁ e a π₂, tagliato da un piano α parallelo alla linea di terra, con le tracce t₁α e t₂α.

Il piano α è in una posizione particolare: nelle prime due proiezioni non si vede di taglio, quindi bisogna costruire la terza proiezione, altrimenti non si vede nulla.

La terza proiezione del solido è un rettangolo, e lì α si vede di taglio, come la retta t₃α: si vede subito che il solido è tagliato in due punti, sulla faccia anteriore e sulla faccia posteriore.

La faccia anteriore sta nel piano frontale δ, che ha le tracce t₁δ e t₃δ. Bisogna trovare l'intersezione tra il piano α e il piano frontale δ:

- nelle due proiezioni ordinarie questa intersezione non si vede, ma in terza proiezione sì, perché la terza proiezione di δ è la retta t₃δ;
- la retta di intersezione r ha la terza proiezione r₃ nel punto in cui t₃α incontra t₃δ;
- r è una retta parallela alla linea di terra: la sua prima proiezione r₁ coincide con t₁δ, e la seconda proiezione r₂ si costruisce riportando la quota di r₃.

I punti della sezione sono quelli in cui r incontra gli spigoli della faccia che si sta considerando, la faccia anteriore: sono 1 e 2.

La stessa cosa si fa con il piano frontale posteriore γ: si trova un'altra retta, m, con i punti 3 e 4. La prima proiezione di m coincide con t₁γ.

Si potrebbe fare lo stesso con i piani di profilo delle facce laterali, ma in questo caso non aiuta molto.

Quando il solido è disposto parallelamente ai piani coordinati, le rette di intersezione sulle due facce opposte sono necessariamente parallele tra loro, perché sono parallele le due facce: succede alle due rette orizzontali r ed m, e succede anche alle rette che si trovano sui piani di profilo.

La sezione 1-2-3-4 si ripassa e si campisce con un tratteggio ordinato e fitto. La parte del solido che sta sopra il piano viene eliminata: guardando il solido si vede la faccia anteriore fino alla sezione, poi il piano inclinato della sezione; dall'alto la sezione copre tutta la pianta.

> [!example] Disegno 6 · Il disegno nello spazio: il piano α parallelo alla LT taglia il parallelepipedo
> ![[b11-spazio-sezione-piano-parallelo-lt.svg|620]]
>
> 1. Il piano α (in rosa) è parallelo alla LT: t₁α e t₂α sono parallele alla LT, t₃α sta su π₃ ed è inclinata.
> 2. Il piano della faccia anteriore, δ, è frontale: α lo taglia lungo la retta r, parallela alla LT. r parte dal punto di π₃ in cui t₃α incontra t₃δ.
> 3. r incontra i due spigoli verticali della faccia anteriore nei punti 1 e 2.
> 4. Lo stesso sulla faccia posteriore, nel piano γ: la retta m dà i punti 3 e 4.
> 5. La sezione 1-2-3-4 è inclinata; la parte del solido sopra α (in grigio) si elimina.

> [!example] Disegno 7 · Il disegno: la stessa sezione in proiezioni ortogonali
> ![[b11-sezione-po-piano-parallelo-lt.svg|620]]
>
> 1. Si disegnano le tracce di α, parallele alla LT, e le due proiezioni del parallelepipedo.
> 2. Si costruisce la terza proiezione del solido (un rettangolo) e la terza traccia t₃α, riportando con il compasso l'aggetto di t₁α.
> 3. La faccia anteriore sta nel piano frontale δ (t₁δ parallela alla LT, t₃δ verticale). r₃ è il punto in cui t₃α incontra t₃δ.
> 4. r è parallela alla LT: r₁ coincide con t₁δ, r₂ si trova riportando in orizzontale la quota di r₃. r₂ taglia gli spigoli verticali della faccia anteriore in 1₂ e 2₂.
> 5. Lo stesso con il piano frontale γ della faccia posteriore: m₃ dove t₃α incontra t₃γ, m₁ coincide con t₁γ, m₂ dà 3₂ e 4₂.
> 6. La sezione 1-2-3-4 si ripassa e si campisce: in seconda proiezione è il rettangolo tra r₂ e m₂, in prima copre tutta la pianta, in terza è il segmento r₃m₃. La parte sopra α (in grigio) si elimina.

### La stessa sezione in cavaliera militare

La docente fa poi disegnare la stessa sezione in cavaliera militare. Stavolta senza scala delle unità di misura: si disegna direttamente un parallelepipedo a base rettangolare di 3 × 4 × 5.

La sequenza delle operazioni è questa:

1. si disegna il piano β che contiene la faccia anteriore del solido, cioè le sue tracce t₁′β e t₃′β;
2. si individua la retta di intersezione tra β e il piano secante parallelo alla linea di terra, e la si segna r′: è la proiezione assonometrica vera della retta r;
3. si individuano i punti in cui questa retta incontra gli spigoli della faccia che si sta considerando.

Il terzo passo va fatto con attenzione. Sul disegno la retta r′ potrebbe sovrapporsi anche ad altri spigoli, ma graficamente si sovrappone soltanto: si sta considerando quella faccia, e contano solo i suoi spigoli, quindi i punti 1 e 2. Che cosa succeda in mezzo alla faccia non si sa, ma quello che serve succede tra 1 e 2.

Poi si costruisce il piano γ della faccia posteriore e si ripete lo stesso ragionamento: la retta m′ incontra gli spigoli della faccia in 3 e 4.

Si potrebbero costruire anche i piani di profilo delle facce laterali, che in questo disegno si vedono abbastanza bene, e trovare anche lì le rette di intersezione. Non è necessario, perché sulla faccia di sinistra la retta di intersezione non può che passare dal punto 4 al punto 1: il risultato è la stessa sezione.

> [!example] Disegno 8 · Il disegno: la stessa sezione in cavaliera militare
> ![[b11-sezione-cavaliera-piano-parallelo-lt.svg|620]]
>
> 1. Si disegna il parallelepipedo in cavaliera militare, con le misure riportate direttamente. Il piano secante α è parallelo alla LT, cioè all'asse x: t₁′α e t₂′α sono parallele a x′, t₃′α sta su π₃ e taglia y′ e z′.
> 2. Primo passo: il piano β della faccia anteriore, con le tracce t₁′β (parallela a x′) e t₃′β (parallela a z′).
> 3. Secondo passo: la retta r = α ∩ β parte dal punto in cui t₃′α incontra t₃′β ed è parallela a x′. La sua proiezione assonometrica è r′.
> 4. Terzo passo: r′ incontra i due spigoli verticali della faccia anteriore in 1 e 2.
> 5. Lo stesso con il piano γ della faccia posteriore (t₁′γ, t₃′γ): la retta m′ dà i punti 3 e 4.
> 6. Sul fianco sinistro la sezione va da 4 a 1, sull'altro da 2 a 3. La sezione 1-2-3-4 si ripassa con un segno forte e si campisce; la parte di solido sopra il piano (in grigio) si elimina.

### Il solido tagliato da un piano verticale

Il secondo caso è un solido ruotato in pianta e tagliato da un piano verticale.

Il piano secante, in realtà, non preoccupa: il solido è circondato da piani verticali, e basta trovare l'intersezione del piano verticale secante con i piani verticali delle facce del solido.

Per la faccia anteriore si usa il piano verticale che la contiene, β, proiettante in prima. Non serve nemmeno la sua seconda traccia, perché non interessa.

Due piani verticali si incontrano in una retta verticale. La retta r = α ∩ β ha quindi:

- la prima proiezione r₁ ridotta a un punto, che coincide con la sua prima traccia T₁ᵣ, dove t₁α incontra t₁β;
- la seconda proiezione r₂ perpendicolare alla linea di terra, che si trova con la linea di richiamo; la seconda traccia T₂ᵣ è all'infinito.

Ci si domanda poi dove r incontra gli spigoli della faccia che si sta considerando. Gli spigoli sono quattro, due verticali e due orizzontali: r, che è verticale, incontra quelli orizzontali, e i punti sono 1 e 2. Sulla faccia anteriore la sezione è quindi una linea verticale.

Lo stesso si fa con l'altro piano proiettante in prima, γ, quello della faccia posteriore. Anche qui la seconda traccia non serve. La retta m è verticale: m₁ coincide con T₁ₘ e m₂ ha T₂ₘ all'infinito. m₂ incontra gli spigoli della faccia in 3 e 4.

La sezione 1-2-3-4 è in rosso, come nel primo caso. In pianta la sezione si deve rinforzare, perché sta sulla traccia t₁α, essendo α un piano verticale. Se si facesse lo stesso disegno anche in assonometria, si vedrebbe come è sezionato il solido.

> [!example] Disegno 9 · Il disegno nello spazio: due piani verticali si tagliano in una retta verticale
> ![[b11-spazio-sezione-piano-verticale.svg|620]]
>
> 1. Le facce lunghe del solido stanno su piani verticali, β davanti e γ dietro. Anche il piano secante α (in rosa) è verticale: t₂α è perpendicolare alla LT.
> 2. α taglia β lungo la retta verticale r, che buca π₁ in T₁ᵣ; taglia γ lungo la retta verticale m, con traccia T₁ₘ. T₁ᵣ e T₁ₘ stanno su t₁α.
> 3. r incontra gli spigoli orizzontali della faccia anteriore in 1 (in alto) e 2 (a terra, dove coincide con T₁ᵣ); m incontra quelli della faccia posteriore in 4 e 3.
> 4. La sezione 1-2-3-4 è un rettangolo verticale che sta nel piano α; la parte del solido a sinistra di α (in grigio) si elimina.

> [!example] Disegno 10 · Il disegno: la sezione con il piano verticale in proiezioni ortogonali
> ![[b11-sezione-po-piano-verticale.svg|620]]
>
> 1. Il parallelepipedo è ruotato in pianta: le facce lunghe sono su piani proiettanti in prima, β davanti e γ dietro, di cui basta la prima traccia t₁β e t₁γ.
> 2. Il piano secante α è verticale: t₁α è obliqua, t₂α è perpendicolare alla LT.
> 3. r = α ∩ β è verticale: r₁ ≡ T₁ᵣ dove t₁α incontra t₁β. Con la linea di richiamo si trova (T₁ᵣ)₂ sulla LT e da lì r₂, perpendicolare alla LT.
> 4. r₂ taglia gli spigoli orizzontali della faccia anteriore, quello in alto e quello a terra, in 1₂ e 2₂.
> 5. Lo stesso con γ: m₁ ≡ T₁ₘ dove t₁α incontra t₁γ, m₂ perpendicolare alla LT, punti 3₂ e 4₂.
> 6. In seconda proiezione la sezione è il rettangolo tra m₂ e r₂, che si campisce; in pianta è il segmento T₁ₘT₁ᵣ su t₁α, che si rinforza. Si tiene la parte destra del solido; la sinistra (in grigio) si elimina.

### Come si disegna la sezione

Il disegno deve essere pulito, e si deve capire che cosa sono le cose disegnate, una faccia, un'altra faccia:

- il solido e la sezione si disegnano con un segno nero e forte;
- le costruzioni si fanno con un filo leggero;
- la sezione si ripassa e si campisce con un tratteggio ordinato e fitto.

Le misure vanno tenute proporzionate. Se il piano secante taglia il solido poco sotto la faccia superiore, il solido non va disegnato altissimo nell'assonometria. Al contrario, se lo si fa basso, il piano non lo taglia: conviene vedere prima dove passa il piano e decidere di conseguenza l'altezza del solido.

> [!tip] Avvisi e consegne
> - Tenere a portata di mano il modellino degli assi: serve per vedere la direzione di proiezione e il ribaltamento dell'asse z.
> - In cavaliera militare segnare sempre l'uguaglianza delle unità su x′, y′ e z\*; la pianta si disegna con un segno leggero.
> - Sul foglio scrivere il titolo «Assonometria obliqua cavaliera militare, angolo a terra di 90 gradi».
> - La cavaliera militare ha due metodi di soluzione: bisogna saperli usare entrambi.
> - Per la prossima volta: ripassare l'assonometria e guardare nel PDF le sezioni, cominciando da quelle semplici con i piani verticali; poi si faranno sezioni più complesse.
> - La docente ha comunicato che una scadenza è spostata di almeno una settimana: secondo il calendario aggiornato la Prova n. 2 passa da giovedì 19 a giovedì 26 novembre. La Prova n. 3 resta il 17 dicembre; la consegna di menabò, tavole e taccuino è il 22 dicembre.

## Collegamenti

L'assonometria ortogonale si regge sul [[07-il-ribaltamento|ribaltamento]] e sull'omologia di ribaltamento: le facce del triedro si ribaltano sul quadro intorno ai lati del triangolo delle tracce, e tra la faccia ribaltata e la sua proiezione c'è un'[[02-affinita-ortogonale-passo-passo|affinità ortogonale]], la stessa studiata nelle omologie della [[02-proiezioni-e-omologia|seconda lezione]]. Nell'assonometria obliqua generica l'affinità diventa obliqua, ed è per questo che non si usa.

Anche la cavaliera militare usa un ribaltamento, quello del triangolo della squadretta intorno a z′, e la sua idea di fondo è quella delle [[03-proiezioni-ortogonali-punto-e-rette|proiezioni ortogonali]]: la pianta resta in vera forma, come la prima proiezione nel metodo di Monge, e i prospetti assonometrici sono la seconda e la terza proiezione del solido. Le stesse corrispondenze tra pianta e prospetti erano al centro delle prime esercitazioni, in cui i solidi erano dati in assonometria e bisognava ricavarne piante e prospetti ([[esercitazioni|Esercitazioni]]).

L'esercizio del prisma è pensato come la costruzione di un plastico, come quelli dell'esercitazione di [[esercizio-3-casa-arzachena|Composizione architettonica]]; il richiamo alla casa di Le Corbusier, una scatola schiacciata da non alzare, riguarda invece le architetture dei casi di studio.

Le sezioni dei solidi mettono insieme molte cose già viste: i piani paralleli alla linea di terra e la terza proiezione di [[04-rette-e-piani-nelle-varie-posizioni]], i piani proiettanti e le rette verticali di [[06-piani-ausiliari-e-perpendicolarita]], le figure e i solidi riassunti in [[PO 7 - Figure piane e solidi]]. La lezione del 5 novembre ([[10-intersezione-retta-figura-e-sezioni]]) aveva già mostrato le sezioni con piani verticali e orizzontali nel progetto di architettura, con il segno di sezione nelle piante; qui la stessa operazione diventa una costruzione geometrica, faccia per faccia.

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[Esercizio guidato ASSONOMETRIA_ORTOGONALE_.pdf]]: la scheda della docente con il triangolo delle tracce e i ribaltamenti delle facce del triedro (O\*, x\*, y\*, z\* e le unità u\*)
- [[2agg_Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: calendario aggiornato, con la Prova n. 2 spostata al 26 novembre
