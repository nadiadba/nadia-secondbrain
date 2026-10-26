---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-08
tags: [geometria-descrittiva, appunti, teoria]
---

# Teoria: le proiezioni ortogonali

> [!info] Note collegate
> Bozze delle lezioni: [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]]
>
> Teoria collegata: [[teoria-omologia]]

Questa pagina raccoglie in ordine logico tutta la teoria delle proiezioni ortogonali (il metodo di Monge) spiegata nelle lezioni dall'8 al 22 ottobre.

Si parte dal metodo e dai piani di proiezione, si passa al punto, alla retta e al piano, poi alle relazioni tra questi elementi (appartenenza e perpendicolarità), e si arriva alle figure piane e al ribaltamento, che permette di vederle in vera grandezza.

Gli esercizi e le esercitazioni sono nella pagina [[esercitazioni|Esercitazioni]].

---

## 1. IL METODO DI MONGE

### 1.1 Proiezioni centrali e proiezioni cilindriche (8 ottobre)

Ogni metodo di rappresentazione è un processo proiettivo, in cui compaiono sempre tre elementi:

- un centro di proiezione,
- un oggetto,
- un piano di quadro su cui l'oggetto viene proiettato.

Il centro di proiezione può essere proprio, cioè a distanza finita. Da esso parte una stella di rette, i raggi proiettanti, e la figura arriva sul piano deformata o ingrandita, come il rettangolo illuminato da un fascio di luce. Con il centro proprio si hanno le proiezioni centrali e la prospettiva.

Il centro può essere invece improprio, cioè all'infinito. Allora si ha soltanto una direzione, e tutti i raggi sono paralleli tra loro, come i raggi del sole nella costruzione delle ombre. Con il centro improprio si hanno le proiezioni cilindriche.

Le proiezioni ortogonali sono proiezioni cilindriche in cui i raggi sono perpendicolari al piano su cui si proietta. Una figura parallela a quel piano vi arriva come traslata, nelle stesse dimensioni: se in partenza c'è un rettangolo, lo si ritrova anche una volta proiettato.

> [!example] Disegno 1 · Proiezione centrale e proiezione cilindrica
> ![[03-proiezione-centrale-e-cilindrica.svg|620]]
>
> A sinistra il centro S è proprio: i raggi partono tutti da S e il rettangolo ABCD arriva ingrandito.
> A destra il centro è all'infinito: i raggi sono paralleli e la figura arriva con le stesse dimensioni.
> Se i raggi sono anche perpendicolari al piano di quadro si hanno le proiezioni ortogonali.

### 1.2 I tre piani di proiezione e il triedro (8 e 13 ottobre)

Per rappresentare un punto nello spazio bisogna prima definire una porzione di spazio, cioè costruire un diedro o un triedro. Monge lavora principalmente con il triedro, e i suoi problemi si risolvono soprattutto su due proiezioni.

I piani di proiezione si chiamano con la lettera greca π, perché i piani si indicano con le minuscole dell'alfabeto greco:

- π₁ è il piano orizzontale;
- π₂ è il piano verticale di fronte, quello di uno dei prospetti;
- π₃ è il terzo piano, verticale anch'esso, di lato.

Nelle proiezioni ortogonali i centri di proiezione sono tre, tutti all'infinito, ciascuno nella direzione perpendicolare a uno dei tre piani.

Alla lavagna il triedro si disegna con un'assonometria particolare, in cui il piano su cui si proietta coincide con π₁. Così la pianta mantiene la sua forma (non la dimensione, che dipende dalla scala) e gli angoli di 90° restano di 90°. Per comodità lo schema si disegna ruotato, con l'angolo retto alla base: π₁ in basso, π₂ e π₃ in verticale.

> [!example] Disegno 2 · Il triedro come si disegna alla lavagna
> ![[04-triedro-come-alla-lavagna.svg|560]]
>
> Lo spigolo tra π₂ e π₃ è verticale.
> Dal suo piede partono la LT e lo spigolo tra π₁ e π₃, ad angolo retto, perché π₁ è in vera forma.
> π₂ sta a sinistra, π₃ a destra, π₁ in basso.

#### 1.2.1 La linea di terra (13 ottobre)

La linea di terra (LT) è la retta di intersezione tra π₁ e π₂. Quando si ribaltano i piani gli uni sugli altri, divide la pianta dal prospetto.

Non divide però lo spazio in modo rigido: le prime proiezioni non stanno per forza sotto la LT e le seconde sopra, perché dipende dal quadrante in cui si trovano i punti. In architettura, naturalmente, le cose stanno tutte nel primo diedro.

### 1.3 Dallo spazio al foglio (8 e 13 ottobre)

Il triedro è un modello rigido, con i piani in piedi. Per avere tutte le proiezioni su un unico foglio i piani si ruotano:

1. si ruota il terzo piano di proiezione sul secondo;
2. poi si ruota il primo, che si ribalta sotto la LT.

Dopo le rotazioni i tre piani coincidono, e per questo si scrive π₁ ≡ π₂ ≡ π₃.

Sul foglio le proiezioni restano legate da due rette:

- la linea di terra, orizzontale, intersezione tra π₁ e π₂;
- la linea verticale, che rappresenta l'intersezione tra i due piani verticali π₂ e π₃.

Le proiezioni non sono vignette separate dalla linea verticale. Partono dalle linee di intersezione dei piani, e il disegno deve essere quello che si vede sul modello aperto.

> [!example] Disegno 3 · Come i tre piani finiscono sul foglio
> ![[b03-ribaltamento-dei-piani.svg|660]]
>
> Schema proposto per ricordare il movimento, non disegnato a lezione (la docente lo ha mostrato con il modello).
> π₃ ruota attorno allo spigolo che ha in comune con π₂ e si mette accanto a π₂; π₁ ruota attorno alla LT e scende sotto π₂.
> Sul foglio: π₂ in alto a sinistra, π₃ in alto a destra della linea verticale, π₁ sotto la LT.

### 1.4 La notazione (8, 13, 15 e 22 ottobre)

Nelle proiezioni ortogonali le proiezioni si scrivono con il pedice. L'apice resta all'omologia e alla prospettiva, e tornerà nell'assonometria accanto al pedice.

- P₁, P₂, P₃ sono la prima, la seconda e la terza proiezione del punto P; allo stesso modo r₁, r₂, r₃ sono le proiezioni della retta r.
- T₁ᵣ, T₂ᵣ, T₃ᵣ sono le tracce della retta r, cioè i punti in cui buca π₁, π₂ e π₃.
- (T₁ᵣ)₂, (T₂ᵣ)₁, (T₃ᵣ)₁ sono le proiezioni delle tracce: la seconda proiezione della prima traccia, la prima proiezione della seconda traccia, e così via.
- t₁α, t₂α, t₃α sono le tracce del piano α.
- P′ si usa per l'omologia e la prospettiva; P₁′, P₂′, P₃′ per l'assonometria.
- A\* è il punto A ribaltato.

I punti si scrivono con le lettere maiuscole, le rette con le minuscole, i piani con le minuscole greche.

Per le rette particolari si usano spesso o per l'orizzontale e f per la frontale, ma è solo una convenzione. Per i piani non c'è nessuna convenzione sulla lettera.

Il nome della posizione invece (proiettante in prima, frontale, di profilo...) è importante, perché serve a capirsi.

### 1.5 Pianta, sezione e prospetti (8 ottobre)

La pianta è una sezione orizzontale, fatta con un piano parallelo a π₁. La quota a cui si taglia l'edificio deve intercettare le finestre e comprendere tutti gli elementi che compongono l'edificio, altrimenti la pianta mostrerebbe uno spazio completamente chiuso.

La sezione verticale passa per due punti precisi della pianta, taglia i muri trasversalmente ed è perpendicolare al piano orizzontale. Non è mai parallela al piano orizzontale, altrimenti diventerebbe una pianta.

La pianta da sola non basta a dare l'idea della forma. Per stabilire i volumi dell'oggetto si disegnano anche i prospetti, cioè le proiezioni ortogonali fatte sui piani verticali del triedro.

Il prospetto è ciò che si vede guardando l'edificio da fuori, da uno dei suoi lati, come se ci si camminasse intorno.

#### 1.5.1 Da che parte si guarda (8 ottobre)

Il prospetto si guarda sempre da fuori; solo la sezione permette di guardare da dentro.

Per questo la linea di terra va messa dalla parte da cui si guarda il lato da rappresentare. Per il lato che in pianta sta in alto, la LT va in alto, lontana dalla pianta, e il prospetto si disegna a testa in giù.

Se invece si mette la LT subito sopra la pianta e si disegna il prospetto in piedi, il prospetto viene specchiato: si sta guardando l'edificio da dentro, e una rientranza che chi guarda vede a destra finisce a sinistra.

È come la mano: per vedere il dorso bisogna guardare dalla parte del dorso, non del palmo.

> [!example] Disegno 4 · Il prospetto giusto e quello sbagliato
> ![[03-prospetto-giusto-e-sbagliato.svg|660]]
>
> La forma dell'edificio è uno schema: conta solo la rientranza.
> Giusto: la LT sta in alto e il prospetto scende dalla LT verso la pianta, a testa in giù; girando il foglio la rientranza è a destra.
> Sbagliato: la LT sta subito sopra la pianta e il prospetto è in piedi; la rientranza finisce dalla parte sbagliata.

### 1.6 Le scale di rappresentazione (8 ottobre)

Si lavora sempre in scala. Le scale possono essere di ingrandimento (10:1, 5:1, 2:1), di riproduzione (1:1) o di riduzione, e in architettura si usano soprattutto quelle di riduzione, fino a quelle delle carte del territorio.

- In 1:100 un metro reale diventa 1 centimetro sul foglio: un muro spesso 50 cm si disegna spesso 5 mm.
- In 1:200 un metro diventa mezzo centimetro e le misure si dimezzano: lo stesso muro è spesso 2,5 mm.
- In 1:50 un metro diventa 2 centimetri e le misure raddoppiano: il muro è spesso 1 cm.

La scala grafica è fondamentale. È la testimonianza delle dimensioni delle cose e permette di risalire dalle misure del disegno a quelle reali anche dopo vari passaggi.

> [!example] Disegno 5 · Lo stesso muro in tre scale e la scala grafica
> ![[03-scale-di-rappresentazione.svg|620]]
>
> Lo stesso muro di 50 cm è spesso 1 cm in 1:50, 5 mm in 1:100, 2,5 mm in 1:200.
> La scala grafica è una barra a tratti alterni, ognuno dei quali vale 1 metro: in 1:100 ogni tratto è lungo 1 cm, in 1:200 è lungo 0,5 cm.

---

## 2. IL PUNTO (8 ottobre)

### 2.1 Le proiezioni, l'aggetto e la quota (8 ottobre)

Il punto si rappresenta mediante le sue tre proiezioni. Il punto P si proietta perpendicolarmente su ciascun piano, e dove la perpendicolare incontra il piano c'è la proiezione.

La prima proiezione P₁ sta sotto la linea di terra, a una distanza che è l'aggetto. L'aggetto è la distanza del punto dal piano verticale π₂, come la sporgenza di un balcone, cioè la distanza tra la ringhiera e la facciata.

La seconda proiezione P₂ sta sopra la linea di terra, a un'altezza che è la quota. La quota è la distanza del punto dal piano orizzontale π₁.

P₁ e P₂ non si possono mettere dove si vuole: stanno sulla stessa linea di richiamo, la linea di costruzione perpendicolare alla LT che le collega.

Con aggetto e quota si sa già dove si trova il punto nello spazio.

> [!example] Disegno 6 · Il punto nel triedro
> ![[03-punto-nel-triedro.svg|620]]
>
> Dal punto P si mandano le perpendicolari ai tre piani: dove li incontrano ci sono P₁, P₂ e P₃.
> Il segmento tra P e π₂ è l'aggetto (arancione); quello tra P e π₁ è la quota (verde).

### 2.2 La terza proiezione (8 ottobre)

La terza proiezione P₃ si ottiene proiettando il punto sul terzo piano, che nello spazio sta di lato, e costruendo sempre la linea di richiamo.

Ciò che si trova su π₃ non è il punto, ma la sua immagine. Ribaltando π₃ la si riporta sul foglio, e in questa operazione la quota non cambia: il punto non può né salire né scendere.

Sul foglio, quindi:

- P₃ ha la stessa quota di P₂;
- la distanza di P₃ dalla linea verticale è l'aggetto, riportato con un arco di circonferenza.

> [!example] Disegno 7 · Le tre proiezioni del punto sul foglio
> ![[03-tre-proiezioni-del-punto.svg|620]]
>
> Da P₁ si va in orizzontale fino alla linea verticale; con il compasso puntato nell'incrocio tra LT e linea verticale si gira l'arco fino alla LT, e da lì si sale.
> Da P₂ si tira l'orizzontale: dove incontra la verticale appena tracciata c'è P₃.

---

## 3. LA RETTA (8-20 ottobre)

### 3.1 Il nome, le tracce e le proiezioni (8, 13 e 15 ottobre)

#### 3.1.1 Il nome della retta (8 e 13 ottobre)

Il nome di una retta si assegna in base alla posizione che assume rispetto ai primi due piani di proiezione, π₁ orizzontale e π₂ verticale.

Una retta perpendicolare a π₃, per esempio, è anche proiettante in terza, ma si chiama parallela alla linea di terra, perché è parallela a π₁ e a π₂.

#### 3.1.2 Le tracce (8 e 13 ottobre)

La traccia di una retta è il punto in cui la retta incontra un piano di proiezione. Essendo un punto si scrive con la T maiuscola, il numero del piano e il nome della retta: T₁ᵣ su π₁, T₂ᵣ su π₂, T₃ᵣ su π₃.

La traccia è un punto della retta reale: è la retta stessa che "buca" il piano, quindi la traccia appartiene alla retta.

Una retta lascia sempre tre tracce. Quando è parallela a un piano di proiezione, la traccia su quel piano esiste, ma è all'infinito, nella direzione della retta.

La traccia all'infinito si scrive (per esempio T₂f∞) e si segna con una lineetta che indica la direzione della retta: non va messa a caso. Anche se non la si vede, va disegnata, perché appartiene alla retta.

Una retta passa infatti per due punti propri, ma anche per un punto proprio e un punto improprio, che le dà la direzione.

#### 3.1.3 Le proiezioni passano per le proiezioni delle tracce (8, 13 e 15 ottobre)

Una proiezione non è la retta: è la proiezione di tutti i suoi punti, comprese le tracce. Siccome le tracce sono punti noti della retta, le proiezioni della retta passano per le proiezioni delle tracce.

- La prima proiezione passa per la prima traccia e per la prima proiezione delle altre tracce.
- La seconda proiezione passa per la seconda traccia e per la seconda proiezione delle altre.
- La terza proiezione passa per la terza traccia e per la terza proiezione delle altre.

Le proiezioni delle tracce cadono sempre sulla linea di terra o sulla linea verticale, perché le tracce stanno sui piani di proiezione: tutto ciò che sta su π₁, proiettato su π₂, finisce sulla LT.

Le proiezioni della retta si disegnano a tratto continuo. Si tratteggiano solo le parti che passano dietro un piano di proiezione e non si vedono.

### 3.2 Le rette proiettanti (8 ottobre)

Le rette proiettanti sono quelle perpendicolari a uno dei primi due piani di proiezione. Si chiamano così perché hanno la stessa direzione dei raggi proiettanti: il centro di proiezione all'infinito è perpendicolare al piano, e la retta è parallela a quei raggi.

In una retta proiettante la traccia nota è sempre quella sul piano a cui la retta è perpendicolare; le altre due sono all'infinito.

#### 3.2.1 La retta proiettante in prima (8 ottobre)

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

#### 3.2.2 La retta proiettante in seconda (8 ottobre)

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

### 3.3 Le rette parallele a un piano di proiezione (13 ottobre)

#### 3.3.1 La retta parallela alla linea di terra, cioè proiettante in terza (13 ottobre)

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

#### 3.3.2 La retta frontale (13 ottobre)

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

#### 3.3.3 La retta orizzontale (13 ottobre)

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

#### 3.3.4 La retta di profilo (13 ottobre)

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

### 3.4 La retta generica (15 e 20 ottobre)

La retta generica non ha condizioni di particolarità: ha tutte le tracce proprie, cioè buca π₁, π₂ e π₃.

#### 3.4.1 Le proiezioni dalle tracce (15 ottobre)

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

#### 3.4.2 Le tracce dalle proiezioni: i punti notevoli sulla LT (20 ottobre)

Il procedimento si può fare anche al contrario, quando sono date le proiezioni della retta e se ne cercano le tracce.

Prolungando la seconda proiezione fino alla linea di terra si trova un punto preciso, che ha un nome: la seconda proiezione della prima traccia, (T₁ᵣ)₂. Non è la traccia, perché la retta non incide la linea di terra; ma scendendo con la perpendicolare alla LT fino alla prima proiezione si trova T₁ᵣ.

Allo stesso modo, prolungando la prima proiezione fino alla LT si trova la prima proiezione della seconda traccia, (T₂ᵣ)₁, e salendo fino alla seconda proiezione si trova T₂ᵣ.

Ogni punto va chiamato con il suo nome: non «il punto sulla linea dove va la proiezione», ma prima o seconda proiezione di una traccia.

> [!example] Disegno 15 · I punti notevoli della retta generica
> ![[06-retta-generica-punti-notevoli.svg|620]]
>
> Si prolunga r₂ fino alla LT, si trova (T₁ᵣ)₂ e si scende fino a r₁: lì c'è T₁ᵣ.
> Si prolunga r₁ fino alla LT, si trova (T₂ᵣ)₁ e si sale fino a r₂: lì c'è T₂ᵣ.

#### 3.4.3 La posizione delle tracce dipende dalla direzione (20 ottobre)

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

#### 3.4.4 La terza traccia (15 ottobre)

La retta generica ha anche una terza traccia, il punto in cui buca π₃.

Per disegnare la terza proiezione non serve: bastano le terze proiezioni della prima e della seconda traccia, perché per due punti passa una retta.

Trovarla è più difficile, perché la retta buca π₃ non dentro il primo diedro ma dietro, dove nel modello il piano non c'è; i piani però sono infiniti. Non è uno spazio occulto, ma una posizione dello spazio.

Il primo modo è immediato: la terza proiezione passa per la terza traccia, quindi si prolunga r₃, tratteggiandola perché la retta sta andando dietro. A mano, però, graficamente potrebbe non tornare.

Il secondo modo, più sicuro, usa un piano ausiliario, e si vede più avanti, tra i piani ausiliari.

---

## 4. IL PIANO (13-20 ottobre)

### 4.1 Il piano non è una figura (13 ottobre)

Il piano si considera esteso all'infinito: non è una figura, ma un ente geometrico esteso nelle due dimensioni. Quando nel modello lo si vede come un rettangolo è solo per comodità, e i tratteggi oltre i bordi dicono che prosegue.

Per questo il piano non si rappresenta con le proiezioni, ma con le tracce.

La traccia del piano è la retta di intersezione che il piano lascia su un piano di proiezione. La traccia è il segno lasciato dal contatto di una cosa sull'altra:

- la traccia della retta è un punto;
- la traccia del piano è una retta.

Si scrive con la t minuscola (perché è una retta), il numero del piano e la lettera greca del piano: t₁α, t₂α, t₃α.

Conviene scrivere il nome vicino alla traccia, così si riconosce subito il piano. Se il piano è parallelo a un piano di proiezione, la traccia corrispondente è all'infinito, e si scrive anche quella (per esempio t₂β∞).

Come le rette, anche i piani prendono il nome dalla posizione che assumono rispetto ai piani di proiezione.

> [!example] Disegno 17 · Il piano non è una figura
> ![[04-spazio-piano-non-e-una-figura.svg|560]]
>
> Il piano frontale β è disegnato come un rettangolo, ma i tratteggi dicono che prosegue.
> Le uniche cose che restano sul foglio sono le tracce: t₁β sul pavimento e t₃β su π₃; t₂β è all'infinito.

Nei disegni che seguono ogni piano è costruito in modo da contenere la retta dello stesso nome: perché la retta stia sul piano, le sue tracce stanno sulle tracce del piano. È la condizione di appartenenza, spiegata nel capitolo successivo.

### 4.2 I piani proiettanti (13 e 15 ottobre)

#### 4.2.1 Il piano proiettante in prima (13 ottobre)

Il piano proiettante in prima è perpendicolare a π₁ e forma un angolo con π₂. È un piano verticale, da distinguere dal frontale, e insieme al proiettante in seconda è tra i piani più usati.

Le sue tracce:

- la prima traccia t₁α è inclinata;
- la seconda t₂α parte dallo stesso punto della LT ed è perpendicolare alla LT;
- la terza t₃α è verticale.

La caratteristica dei piani verticali è che la prima proiezione di tutto ciò che giace sul piano coincide con la prima traccia. Una retta, un triangolo, un cerchio su un piano verticale, visti dall'alto, si riducono a una linea.

La coincidenza c'è solo sulla prima traccia: la quota del punto non cambia tra la seconda e la terza proiezione, e la terza proiezione di un punto non sta su t₃α.

> [!example] Disegno 18 · Il piano proiettante in prima
> ![[04-piano-proiettante-in-prima.svg|620]]
>
> Sul foglio: t₁α inclinata, t₂α perpendicolare alla LT; t₃α sale verticale dal punto in cui t₁α, portata con l'arco, arriva sulla LT.
> Il punto P ha P₁ su t₁α; la retta verticale r per P ha r₁ ≡ T₁ᵣ ≡ P₁ su t₁α.
>
> ![[04-spazio-piano-proiettante-in-prima.svg|560]]
>
> Nello spazio: il piano è un cartoncino in piedi, girato rispetto a π₂; visto dall'alto si riduce alla linea t₁α.

#### 4.2.2 Il piano proiettante in seconda (15 ottobre)

Il piano proiettante in seconda è perpendicolare a π₂ e inclinato rispetto a π₁ e a π₃.

Le sue tracce:

- la prima traccia t₁α è perpendicolare alla linea di terra;
- la seconda traccia t₂α è inclinata quanto è inclinato il piano;
- la terza traccia t₃α è parallela alla linea di terra e incontra t₂α sulla linea verticale.

Se si guarda di taglio, come lo vedrebbe π₂, un triangolo disegnato sul piano, non si vede più un triangolo ma una linea. Nel piano proiettante in seconda, infatti, la seconda proiezione di tutti gli elementi che stanno sul piano coincide con la seconda traccia.

> [!example] Disegno 19 · Il piano proiettante in seconda
> ![[05-piano-proiettante-in-seconda-tre-tracce.svg|620]]
>
> Sul foglio: t₁α perpendicolare alla LT, t₂α inclinata dallo stesso punto della LT, t₃α parallela alla LT dal punto in cui t₂α incontra la linea verticale.
>
> ![[05-spazio-piano-proiettante-in-seconda.svg|620]]
>
> Nello spazio: ogni punto del triangolo, proiettato su π₂, cade su t₂α; per questo A₂ coincide con B₂, perché AB è perpendicolare a π₂.

### 4.3 I piani paralleli alla linea di terra o a un piano di proiezione (13 ottobre)

#### 4.3.1 Il piano parallelo alla linea di terra (13 ottobre)

Il piano parallelo alla linea di terra è inclinato rispetto a π₁ e a π₂ e taglia tutti e tre i piani di proiezione, quindi ha tre tracce:

- la prima traccia t₁α e la seconda t₂α sono parallele alla linea di terra;
- la terza traccia t₃α è variamente inclinata.

Sul piano ci possono essere tante rette parallele alla linea di terra, figure e punti. Nel piano parallelo alla linea di terra tutte le terze proiezioni coincidono con la terza traccia, come nel piano verticale tutte le prime proiezioni coincidono con la prima traccia.

> [!example] Disegno 20 · Il piano parallelo alla LT
> ![[04-piano-parallelo-alla-lt.svg|620]]
>
> Sul foglio: t₃α passa per T₃ᵣ della retta r parallela alla LT ed è inclinata; dal punto in cui incontra la verticale parte t₂α, parallela alla LT; dal punto in cui incontra la LT si torna con l'arco sulla verticale, sotto la LT, e parte t₁α, parallela alla LT.
>
> ![[04-spazio-piano-parallelo-alla-lt.svg|560]]
>
> Nello spazio: il piano è un cartoncino inclinato tra il pavimento e la parete π₂; r sta sul cartoncino e buca π₃ sulla traccia t₃α.

#### 4.3.2 Il piano frontale (13 ottobre)

Il piano frontale è parallelo a π₂ e perpendicolare a π₁ e a π₃. È uno dei piani più usati in architettura: i piani frontali sono infiniti, come le sezioni di un edificio, e dove farli passare dipende da che cosa si vuole far vedere.

Le sue tracce:

- la prima traccia t₁β è parallela alla linea di terra, e la sua distanza dalla LT è l'aggetto del piano;
- la terza traccia t₃β è verticale;
- la seconda traccia è all'infinito, perché il piano è parallelo a π₂, e si scrive t₂β∞ vicino alle altre.

Essendo un piano verticale, tutto ciò che vi sta ha la prima proiezione sulla prima traccia.

> [!example] Disegno 21 · Il piano frontale
> ![[04-piano-frontale.svg|620]]
>
> Sul foglio: t₁β è parallela alla LT e coincide con f₁ della frontale che il piano contiene; con l'arco si porta l'aggetto sul terzo piano e si alza t₃β, verticale; si scrive t₂β∞.
>
> ![[04-spazio-piano-frontale.svg|560]]
>
> Nello spazio: il piano è una parete parallela a π₂; T₁f sta su t₁β e T₃f su t₃β.

#### 4.3.3 Il piano orizzontale (13 ottobre)

Il piano orizzontale è parallelo a π₁. Tutte le sezioni orizzontali, tutte le piante, sono fatte con piani orizzontali.

Le sue tracce:

- la prima traccia è all'infinito (t₁γ∞);
- la seconda e la terza sono orizzontali e stanno sulla stessa linea, all'altezza del piano.

Tutto ciò che sta sul piano orizzontale ha la seconda proiezione sulla seconda traccia.

> [!example] Disegno 22 · Il piano orizzontale
> ![[04-piano-orizzontale.svg|620]]
>
> Sul foglio: t₂γ è parallela alla LT e coincide con o₂ dell'orizzontale che il piano contiene (t₂γ ≡ o₂); t₃γ prosegue alla stessa altezza dall'altra parte della verticale; si scrive t₁γ∞.
>
> ![[04-spazio-piano-orizzontale.svg|560]]
>
> Nello spazio: il piano è un pavimento sollevato, come il piano di sezione di una pianta.

#### 4.3.4 Il piano di profilo (13 ottobre)

Il piano di profilo è parallelo a π₃.

Le sue tracce:

- la terza traccia è all'infinito (t₃δ∞);
- la prima t₁δ e la seconda t₂δ stanno sulla stessa linea perpendicolare alla linea di terra.

Il piano di profilo è verticale, quindi le prime proiezioni dei suoi elementi stanno sulla prima traccia; ma anche le seconde proiezioni cadono sulla seconda traccia, e per vedere a cosa corrisponde una figura serve la terza proiezione.

> [!example] Disegno 23 · Il piano di profilo
> ![[04-piano-di-profilo.svg|620]]
>
> Sul foglio: t₂δ e t₁δ partono dallo stesso punto della LT e sono perpendicolari alla LT (si segnano gli angoli retti); la retta di profilo contenuta nel piano ha t₂δ ≡ r₂ e t₁δ ≡ r₁, e si vede com'è solo in r₃.
>
> ![[04-spazio-piano-di-profilo.svg|560]]
>
> Nello spazio: il piano è una parete parallela a π₃; taglia il pavimento e la parete π₂ lungo due tracce perpendicolari alla LT.

### 4.4 Il piano generico (15 ottobre)

Il piano generico è in posizione generica rispetto a tutti e tre i piani di proiezione: forma un angolo con ciascuno, e li taglia lungo un triangolo.

Sul foglio le tre tracce si incontrano a due a due sulle rette di intersezione dei piani di proiezione:

- t₂α e t₁α partono dallo stesso punto della LT;
- t₃α unisce il punto in cui t₂α incontra la linea verticale con il punto in cui t₁α, portata con l'arco, arriva sulla LT dalla parte di π₃.

Questo triangolo è molto importante, perché in assonometria il piano generico diventerà il piano di quadro e il triangolo si chiamerà triangolo delle tracce.

> [!example] Disegno 24 · Il piano generico nello spazio
> ![[05-spazio-piano-generico.svg|620]]
>
> Il piano taglia π₁, π₂ e π₃ lungo t₁α, t₂α e t₃α, che formano un triangolo.
> Un'orizzontale o del piano è parallela al pavimento: o₁ è parallela a t₁α.

### 4.5 Riconoscere il piano dalle proiezioni di una figura (13, 15 e 20 ottobre)

Un piano non è generico di per sé: lo è in relazione alla posizione che assume rispetto ai piani di proiezione. Lo stesso triangolo, spostato nel modello, può stare in un piano orizzontale, frontale, proiettante in prima, proiettante in seconda o generico.

Il piano si riconosce dalla forma delle proiezioni della figura:

- se la seconda proiezione si riduce a una linea parallela alla LT, il piano è orizzontale;
- se la seconda proiezione si riduce a una linea inclinata, il piano è proiettante in seconda;
- se la prima proiezione si riduce a una linea parallela alla LT, il piano è frontale;
- se la prima proiezione si riduce a una linea inclinata, il piano è proiettante in prima;
- se tutte e due le proiezioni si riducono a linee, il piano è di profilo.

Quando si vedono due proiezioni "piene", il piano può essere generico oppure parallelo alla linea di terra. Per decidere si ragiona sulle rette dei lati, oppure si costruisce la terza proiezione: nel piano parallelo alla LT la figura in terza proiezione si riduce a un segmento sulla terza traccia.

Per ogni piano riconosciuto si scrivono tutte e due le tracce, anche quella all'infinito (per esempio t₂γ e subito sotto t₁γ∞), perché mettendole vicine si riconosce subito il piano.

> [!example] Disegno 25 · Lo stesso triangolo in quattro piani diversi
> ![[06-triangolo-quattro-posizioni.svg|700]]
>
> Piano orizzontale: la seconda proiezione è un segmento su t₂γ, parallelo alla LT.
> Piano proiettante in seconda: la seconda proiezione è un segmento su t₂β inclinata.
> Piano proiettante in prima: la prima proiezione è un segmento su t₁δ inclinata. Piano frontale: la prima proiezione è un segmento su t₁ε, parallelo alla LT.

> [!example] Disegno 26 · Un quadrato in un piano parallelo alla LT
> ![[05-quadrato-piano-parallelo-alla-lt.svg|620]]
>
> Prima e seconda proiezione sono due rettangoli, con i lati AB e CD paralleli alla LT.
> In terza proiezione A₃ ≡ B₃ e C₃ ≡ D₃: il quadrato diventa un segmento che sta sulla terza traccia t₃α, inclinata; t₁α e t₂α sono parallele alla LT.

---

## 5. L'APPARTENENZA (13-20 ottobre)

### 5.1 Le tre condizioni di appartenenza (13 e 15 ottobre)

#### 5.1.1 Il punto e la retta (13 ottobre)

Un punto appartiene a una retta quando le proiezioni del punto appartengono alle proiezioni della retta: P₁ sta su r₁ e P₂ sta su r₂.

#### 5.1.2 La retta e il piano (13 e 15 ottobre)

Una retta appartiene a un piano quando tutti i suoi punti appartengono al piano. In pratica se ne prendono due, che quando è possibile sono le tracce.

Una retta appartiene a un piano quando le tracce della retta appartengono alle rispettive tracce del piano: T₁ᵣ su t₁α, T₂ᵣ su t₂α, T₃ᵣ su t₃α.

Non basta che una sola traccia della retta stia su una traccia del piano: un piano che contiene T₁ᵣ ma non T₂ᵣ non contiene la retta.

Se una traccia della retta è all'infinito, anche quel punto all'infinito deve stare sulla traccia corrispondente del piano. Questo succede solo se la proiezione della retta e la traccia del piano sono parallele.

#### 5.1.3 Il punto e il piano (13 e 15 ottobre)

Un punto appartiene a un piano se appartiene a una retta del piano. È una concatenazione: P ∈ r e r ⊂ α, quindi P ∈ α.

Le condizioni vanno rispettate tutte: il punto sulla retta, e la retta sul piano con le sue tracce sulle tracce del piano.

Bisogna anche non confondere le tracce con le proiezioni: le condizioni sulla retta e sul piano parlano di tracce, quella sul punto e sulla retta parla di proiezioni.

### 5.2 Regola e coincidenze (13 e 15 ottobre)

Tranne nei piani particolari, la proiezione di un punto del piano non va a finire sulla traccia: la traccia è soltanto l'intersezione del piano con un piano di proiezione.

Nei piani particolari ci sono però delle coincidenze:

- nei piani verticali (proiettante in prima, frontale, di profilo) la prima proiezione di tutto ciò che sta sul piano coincide con la prima traccia;
- nel piano proiettante in seconda e nel piano orizzontale la seconda proiezione di tutto ciò che sta sul piano coincide con la seconda traccia;
- nel piano parallelo alla linea di terra tutte le terze proiezioni coincidono con la terza traccia.

Queste coincidenze vanno distinte dalla regola. La regola resta una sola: il punto appartiene al piano perché appartiene a una retta del piano.

Nel piano proiettante in prima, per esempio, P₁ cade sulla prima traccia; ma la dimostrazione passa per una retta. La retta verticale r per P ha r₁ ≡ T₁ᵣ ≡ P₁, e T₁ᵣ sta su t₁α: quindi r appartiene ad α, e P, che sta su r, appartiene ad α.

### 5.3 Le rette ausiliarie: l'orizzontale e la frontale (15 e 20 ottobre)

Per dimostrare che un punto sta su un piano si può usare qualunque retta del piano, anche una generica. Le rette che aiutano di più sono però le due ausiliarie, l'orizzontale e la frontale, che vanno disegnate in modo immediato, senza esitazioni, perché servono per qualunque cosa.

L'orizzontale e la frontale sono le rette che servono a risolvere i problemi.

#### 5.3.1 Le rette che stanno sul piano generico (15 ottobre)

Sul piano generico possono stare:

- la retta generica, con T₁ᵣ su t₁α e T₂ᵣ su t₂α;
- l'orizzontale;
- la frontale;
- la retta di profilo.

Non può starci invece una retta proiettante in prima: è verticale, esce dal piano e lo buca in un solo punto.

> [!example] Disegno 27 · Le rette del piano generico nello spazio
> ![[05-spazio-piano-generico-rette.svg|620]]
>
> La retta generica r ha T₁ᵣ su t₁α e T₂ᵣ su t₂α; l'orizzontale o è parallela a t₁α; la frontale f è parallela a t₂α.
> La proiettante in prima v non sta sul piano: lo buca in un punto.

#### 5.3.2 L'orizzontale del piano (15 ottobre)

L'orizzontale del piano non è la parallela alla linea di terra (anche quella è orizzontale), ma la retta con la seconda proiezione parallela alla LT e la prima variamente inclinata.

Essendo parallela a π₁, ha la prima traccia all'infinito. Per appartenere al piano anche quel punto all'infinito deve stare su t₁α, e questo succede solo se la retta ha la direzione di t₁α.

Quindi l'orizzontale di un piano ha:

- la seconda proiezione o₂ parallela alla LT;
- la seconda traccia T₂ₒ su t₂α (e la terza T₃ₒ su t₃α);
- la prima proiezione o₁ parallela a t₁α.

> [!example] Disegno 28 · L'orizzontale del piano generico
> ![[05-piano-generico-orizzontale.svg|620]]
>
> o₂ parallela alla LT incontra t₂α in T₂ₒ; scendendo sulla LT si trova (T₂ₒ)₁, e da lì o₁ si traccia parallela a t₁α.
> o₁ incontra la verticale in (T₃ₒ)₁; con l'arco e salendo all'altezza di o₂ si trova T₃ₒ, che cade su t₃α.

#### 5.3.3 La frontale del piano (15 ottobre)

Allo stesso modo la frontale, che ha la prima proiezione parallela alla LT, è parallela a π₂ e ha la seconda traccia all'infinito. Per rispettare la condizione di appartenenza deve essere parallela alla seconda traccia del piano.

Quindi la frontale di un piano ha:

- la prima proiezione f₁ parallela alla LT;
- la prima traccia T₁f su t₁α (e la terza T₃f su t₃α);
- la seconda proiezione f₂ parallela a t₂α.

> [!example] Disegno 29 · La frontale del piano generico
> ![[05-piano-generico-frontale.svg|620]]
>
> f₁ parallela alla LT incontra t₁α in T₁f; salendo sulla LT si trova (T₁f)₂, e da lì f₂ si traccia parallela a t₂α.
> f₃ è verticale; f₂ incontra la verticale in (T₃f)₂, e portando quel punto in orizzontale su f₃ si trova T₃f, che cade su t₃α.

### 5.4 Disegnare un punto che appartiene a un piano (15 e 20 ottobre)

#### 5.4.1 Nel piano generico, con l'orizzontale (15 e 20 ottobre)

Per disegnare un punto del piano generico α si disegna prima una sua orizzontale, come visto sopra. Su questa orizzontale si sceglie un punto qualunque e se ne disegnano le proiezioni.

> [!example] Disegno 30 · Un punto del piano generico con l'orizzontale
> ![[06-punto-piano-generico-orizzontale.svg|620]]
>
> Si traccia o₂ parallela alla LT: dove incontra t₂α c'è T₂ₒ. Da T₂ₒ si scende alla LT, in (T₂ₒ)₁, e si traccia o₁ parallela a t₁α.
> Si sceglie P₂ su o₂ e si scende con il richiamo fino a o₁: lì c'è P₁. P sta su una retta di α, quindi P ∈ α.

#### 5.4.2 Nel piano generico, con la frontale (15 ottobre)

Con la frontale si comincia da f₁, parallela alla LT, che incontra t₁α in T₁f. Poi f₂ deve avere la direzione che porta il suo punto all'infinito sulla traccia del piano, quindi si costruisce parallela a t₂α.

Si dimostra così che P appartiene a f e che f appartiene ad α.

> [!example] Disegno 31 · Un punto del piano generico con la frontale
> ![[05-frontale-piano-generico.svg|620]]
>
> f₁ parallela alla LT incontra t₁α in T₁f; da (T₁f)₂ sulla LT si traccia f₂ parallela a t₂α.
> Si sceglie P₂ su f₂ e si scende fino a f₁: lì c'è P₁. P ∈ f ⊂ α.

#### 5.4.3 Nei piani proiettanti (20 ottobre)

Nei piani proiettanti vale la stessa regola, con una scorciatoia data dalla coincidenza.

Nel piano proiettante in prima si mette P₁ sulla prima traccia e P₂ sulla stessa linea di richiamo, all'altezza che si vuole.

Nel piano proiettante in seconda si mette P₂ sulla seconda traccia e P₁ a qualunque distanza sulla stessa linea di richiamo.

Per verificare che il punto del proiettante in seconda appartiene davvero al piano si usa una frontale:

- ha la prima proiezione parallela alla linea di terra;
- la sua prima traccia sta sulla prima traccia del piano;
- la seconda traccia è all'infinito;
- la seconda proiezione coincide con la seconda traccia del piano.

Il punto sta sulla frontale, e quindi sul piano.

> [!example] Disegno 32 · Un punto del piano proiettante in seconda
> ![[06-piano-proiettante-in-seconda-frontale.svg|620]]
>
> Il piano β ha t₁β perpendicolare alla LT e t₂β inclinata; P₂ sta su t₂β e P₁ sulla stessa linea di richiamo.
> La frontale f per P ha f₁ parallela alla LT, che incontra t₁β in T₁f, e f₂ ≡ t₂β, con T₂f∞: P sta su f, f sta su β.

#### 5.4.4 Verificare se un punto appartiene a un piano (15 ottobre)

Il problema si può porre anche al contrario: date le tracce di α e le due proiezioni P₂ e P₁, il punto P appartiene ad α?

Si disegna una retta che passa per il punto e appartiene al piano. Si è liberi di sceglierla, ma una volta scelta una proiezione l'altra non è più libera.

1. Si disegna r₂ per P₂ e si segna T₂ᵣ dove incontra t₂α.
2. Dove r₂ incontra la LT c'è (T₁ᵣ)₂; scendendo si trova T₁ᵣ su t₁α.
3. La prima proiezione r₁ passa per T₁ᵣ e per (T₂ᵣ)₁.
4. Se P₁ cade su r₁ il punto appartiene al piano; altrimenti no.

Così si fanno due cose insieme: si verifica la condizione di appartenenza e si disegna una retta che appartiene al piano.

> [!example] Disegno 33 · Il punto appartiene al piano?
> ![[05-verifica-punto-con-retta-generica.svg|620]]
>
> La retta r per P₂ ha T₂ᵣ su t₂α e T₁ᵣ su t₁α, quindi r ⊂ α.
> Da P₂ si scende con il richiamo: P₁ non cade su r₁, quindi in questo caso P ∉ α.

### 5.5 I piani ausiliari (15 e 20 ottobre)

I piani ausiliari sono il piano proiettante in prima e il piano proiettante in seconda. Insieme alle rette ausiliarie, sono i pochi strumenti fatti apposta per risolvere quasi tutti i problemi della geometria descrittiva.

Aiutano grazie alla loro coincidenza: tutto ciò che sta sul proiettante in prima ha la prima proiezione sulla prima traccia, tutto ciò che sta sul proiettante in seconda ha la seconda proiezione sulla seconda traccia.

#### 5.5.1 La retta generica nei piani proiettanti (15 ottobre)

Una retta generica appartiene sempre a un piano proiettante: se si appoggia una retta sul cartoncino, ci sta.

- Per farla stare in un piano proiettante in prima α si fa coincidere r₁ con t₁α; t₂α, perpendicolare alla LT, parte da (T₂ᵣ)₁ e conterrà T₂ᵣ.
- Per farla stare in un piano proiettante in seconda β si fa coincidere r₂ con t₂β; t₁β, perpendicolare alla LT, parte da (T₁ᵣ)₂ e passa per T₁ᵣ.

In tutti e due i casi le tracce della retta stanno sulle tracce del piano.

> [!example] Disegno 34 · La retta generica nei due piani ausiliari
> ![[05-retta-generica-piani-proiettanti.svg|620]]
>
> Piano α proiettante in prima: t₁α ≡ r₁, e t₂α perpendicolare alla LT per T₂ᵣ.
> Piano β proiettante in seconda: t₂β ≡ r₂, e t₁β perpendicolare alla LT per T₁ᵣ.
>
> ![[05-spazio-retta-generica-piani-ausiliari.svg|620]]
>
> Nello spazio: il piano verticale α (blu) ha come prima traccia r₁; il piano β (verde), perpendicolare a π₂, ha come seconda traccia r₂.

#### 5.5.2 La terza traccia della retta generica (15 ottobre)

Il piano ausiliario dà il modo più sicuro per trovare la terza traccia della retta generica.

Se per r si fa passare un piano proiettante in prima, con r₁ ≡ t₁α, per le condizioni di appartenenza la terza traccia della retta deve stare sulla terza traccia del piano, anche se sta dietro.

1. Si prolunga t₁α fino alla retta di intersezione tra π₁ e π₃, la linea verticale: lì c'è (T₃ᵣ)₁, sopra la LT perché è dietro π₂.
2. Quel punto si ruota con l'arco fino alla LT.
3. Da lì si sale in verticale: quella verticale è la terza traccia del piano, e T₃ᵣ sta su di essa.

Per controllo, r₂ prolungata incontra la verticale in (T₃ᵣ)₂; portando quel punto in orizzontale su t₃α si ritrova T₃ᵣ.

> [!example] Disegno 35 · La terza traccia con il piano ausiliario
> ![[05-retta-generica-terza-traccia.svg|620]]
>
> r₃ passa per (T₁ᵣ)₃ e (T₂ᵣ)₃; oltre T₂ᵣ la retta va dietro π₂ e si tratteggia.
> Con il piano ausiliario α (t₁α ≡ r₁) si trova (T₃ᵣ)₁, lo si gira con l'arco e si sale: è t₃α, e T₃ᵣ sta lì sopra.
>
> ![[05-spazio-retta-generica-terza-traccia.svg|620]]
>
> Nello spazio: oltre T₂ᵣ la retta passa dietro π₂ (tratteggio) e buca π₃ prolungato in T₃ᵣ, proprio sulla traccia t₃α del piano verticale che la contiene.

### 5.6 I piani che contengono una retta (15 ottobre)

#### 5.6.1 Il metodo (15 ottobre)

Per una retta passano infiniti piani: per una retta verticale, per esempio, passano infiniti piani verticali, ma solo quelli.

Per trovare quali piani possono contenere una retta data:

1. si colloca la retta nel modello e si guardano i piani su cui si appoggia, partendo dall'associazione più immediata tra il nome della retta e il nome del piano (una retta proiettante in seconda sta sicuramente in un piano proiettante in seconda);
2. si disegnano i piani rispettando la condizione di appartenenza: le tracce del piano passano per le tracce della retta.

Per questo, nel disegno delle condizioni, contano le tracce della retta più che le sue proiezioni.

Lo schema del triedro che accompagna questi disegni non è propriamente un'assonometria, ma una trasposizione grafica del modello.

#### 5.6.2 La retta proiettante in prima (15 ottobre)

La retta verticale buca π₁ in T₁ᵣ. Un piano orizzontale non può contenerla, perché la retta lo buca in un solo punto.

La contengono i piani verticali, e in tutti la prima traccia passa per T₁ᵣ:

- il piano di profilo;
- il piano frontale;
- i piani proiettanti in prima, che ruotano attorno alla retta.

> [!example] Disegno 36 · I piani che contengono una retta proiettante in prima
> ![[05-piani-per-retta-proiettante-in-prima.svg|620]]
>
> Piano di profilo γ (viola): t₁γ e t₂γ sulla stessa perpendicolare alla LT. Piano frontale α (verde): t₁α per T₁ᵣ, parallela alla LT.
> Piano proiettante in prima β (blu): t₁β per T₁ᵣ, con l'inclinazione che si vuole, e t₂β perpendicolare alla LT.
>
> ![[05-spazio-piani-retta-proiettante-in-prima.svg|620]]

#### 5.6.3 La retta proiettante in seconda (15 ottobre)

La retta perpendicolare a π₂ lo buca in T₂ᵣ: r₂ è un punto e la prima traccia è all'infinito.

La contengono, e in tutti la seconda traccia passa per T₂ᵣ:

- il piano proiettante in seconda;
- il piano orizzontale;
- il piano di profilo.

> [!example] Disegno 37 · I piani che contengono una retta proiettante in seconda
> ![[05-piani-per-retta-proiettante-in-seconda.svg|620]]
>
> Proiettante in seconda β: t₂β per T₂ᵣ, inclinata, e t₁β perpendicolare alla LT. Orizzontale γ: t₂γ per T₂ᵣ, parallela alla LT.
> Di profilo δ: t₂δ per T₂ᵣ e t₁δ ≡ r₁, tutte e due perpendicolari alla LT.
>
> ![[05-spazio-piani-retta-proiettante-in-seconda.svg|620]]

#### 5.6.4 La retta parallela alla linea di terra (15 ottobre)

La retta parallela alla linea di terra non buca né π₁ né π₂, e l'unica traccia propria è la terza, T₃ᵣ, che coincide con r₃.

La contengono:

- il piano parallelo alla linea di terra, che la contiene per forza, con t₃α per T₃ᵣ;
- il piano frontale, con t₁φ ≡ r₁ e t₃φ verticale per T₃ᵣ;
- il piano orizzontale, con t₂ ≡ r₂.

> [!example] Disegno 38 · I piani che contengono una retta parallela alla LT
> ![[05-piani-per-retta-parallela-alla-lt.svg|620]]
>
> T₃ᵣ ≡ r₃ si trova portando r₁ sul terzo piano con l'arco e salendo all'altezza di r₂. Piano α parallelo alla LT: t₃α per T₃ᵣ. Piano frontale φ: t₁φ ≡ r₁.
>
> ![[05-retta-parallela-alla-lt-piano-orizzontale.svg|620]]
>
> Il piano orizzontale (dal taccuino di Marta): t₂α ≡ r₂, parallela alla LT, e la prima traccia all'infinito.
>
> ![[05-spazio-piani-retta-parallela-alla-lt.svg|620]]

#### 5.6.5 La retta orizzontale (15 ottobre)

L'orizzontale ha la prima traccia all'infinito e la seconda T₂ₒ.

La contengono:

- il piano orizzontale, con t₂ ≡ o₂;
- un piano generico: si parte da una seconda traccia per T₂ₒ, e la prima traccia del piano, dal punto in cui la seconda incontra la LT, si disegna parallela a o₁;
- il piano proiettante in prima, con t₁ ≡ o₁.

Nel piano generico si è liberi di scegliere, ma una volta fissati gli elementi di partenza il piano è determinato.

> [!example] Disegno 39 · I piani che contengono una retta orizzontale
> ![[05-piani-per-retta-orizzontale.svg|620]]
>
> Orizzontale α: t₂α ≡ o₂, t₁α all'infinito. Generico β: t₂β per T₂ₒ e t₁β parallela a o₁.
> Proiettante in prima γ: t₁γ ≡ o₁ e t₂γ perpendicolare alla LT per T₂ₒ.
>
> ![[05-spazio-piani-retta-orizzontale.svg|620]]

#### 5.6.6 La retta frontale (15 ottobre)

La frontale ha la seconda traccia all'infinito e la prima T₁f. Conviene disegnare comunque f₁, per essere certi del parallelismo.

La contengono:

- il piano frontale, che è verticale, con t₁ ≡ f₁;
- un piano generico, con la prima traccia per T₁f e la seconda traccia parallela a f₂;
- il piano proiettante in seconda, con t₂ ≡ f₂.

> [!example] Disegno 40 · I piani che contengono una retta frontale
> ![[05-piani-per-retta-frontale.svg|620]]
>
> Frontale β: t₁β ≡ f₁, t₂β all'infinito. Generico α: t₁α per T₁f e t₂α parallela a f₂.
> Proiettante in seconda γ: t₂γ ≡ f₂ e t₁γ perpendicolare alla LT per T₁f.
>
> ![[05-spazio-piani-retta-frontale.svg|620]]

#### 5.6.7 La retta di profilo (15 ottobre)

La retta di profilo m ha la terza traccia all'infinito.

La contengono:

- il piano di profilo, a cui appartiene per definizione, con t₂δ ≡ m₂ e t₁δ ≡ m₁;
- un piano parallelo alla linea di terra, con t₂ per T₂ₘ, t₁ per T₁ₘ e t₃ ≡ m₃;
- un piano generico, con le tracce per T₂ₘ e T₁ₘ e la terza traccia necessariamente parallela a m₃.

> [!example] Disegno 41 · I piani che contengono una retta di profilo
> ![[05-piani-per-retta-di-profilo.svg|620]]
>
> Di profilo δ: t₂δ ≡ m₂, t₁δ ≡ m₁. Parallelo alla LT ε: t₂ε e t₁ε parallele alla LT per T₂ₘ e T₁ₘ, t₃ε ≡ m₃.
> Generico α: t₂α e t₁α per T₂ₘ e T₁ₘ si incontrano sulla LT, e t₃α risulta parallela a m₃.
>
> ![[05-spazio-piani-retta-di-profilo.svg|620]]

### 5.7 Il piano dato da una figura (20 ottobre)

#### 5.7.1 Forma mongiana e forma tecnica (20 ottobre)

Finora i piani sono stati considerati nella loro estensione, attraverso le tracce. È la forma mongiana, in cui anche la retta è definita dai suoi due punti notevoli, le tracce.

Un piano può però essere rappresentato da qualunque figura piana, per esempio da un triangolo: tre punti individuano un piano, e il triangolo disegnato nelle sue due proiezioni è già il piano.

Questa è la forma tecnica, quella del disegno di architettura, in cui non è sempre necessario avere le tracce. Le due forme non sono due cose diverse: si può lavorare con le tracce o senza, è indifferente.

Se si hanno le tracce si possono disegnare le proiezioni della figura, e se si hanno le proiezioni della figura si possono trovare le tracce.

#### 5.7.2 Riconoscere le rette dei lati (20 ottobre)

Per capire in che piano sta una figura si guardano le rette a cui appartengono i lati.

Un lato è un segmento, e il segmento appartiene a una retta: se una proiezione contiene due lettere, l'altra proiezione contiene le stesse lettere.

- Se un lato ha la seconda proiezione parallela alla LT, sta su un'orizzontale.
- Se ha la prima proiezione parallela alla LT, sta su una frontale.
- Se ha tutte e due le proiezioni perpendicolari alla LT, sta su una retta di profilo.
- Se ha tutte e due le proiezioni inclinate rispetto alla LT, sta su una retta generica.

Se tutti e tre i lati di un triangolo stanno su rette generiche, il piano che contiene la figura è un piano generico.

#### 5.7.3 Una retta del piano della figura: l'orizzontale (20 ottobre)

Per disegnare una retta che appartiene al piano del triangolo, senza tracce, si sceglie un'orizzontale, costruita sfruttando il fatto che la retta passa per punti della figura.

1. Si parte da A₂ e si traccia o₂ parallela alla linea di terra: dentro la figura incontra il lato B₂C₂ in un punto H₂.
2. Con il richiamo si trova H₁ su B₁C₁.
3. La prima proiezione o₁ è la retta che passa per A₁ e H₁.

Qualunque punto preso sull'orizzontale appartiene al piano. Allo stesso modo si può costruire una frontale.

Le orizzontali sono importanti anche in architettura: per sapere in che direzione mettere le tegole di una falda bisogna trovare le orizzontali del piano, perché le tegole sono perpendicolari alla gronda, che di solito è orizzontale.

> [!example] Disegno 42 · L'orizzontale nel piano di un triangolo
> ![[06-orizzontale-nel-triangolo.svg|560]]
>
> Da A₂ si traccia o₂ parallela alla LT, che incontra B₂C₂ in H₂; scendendo con il richiamo si trova H₁ su B₁C₁, e o₁ passa per A₁ e H₁.
> Un punto P preso su o appartiene al piano del triangolo.

#### 5.7.4 Dalle proiezioni della figura alle tracce del piano (20 ottobre)

Le tracce di un piano contengono le tracce delle rette che compongono la figura, cioè dei lati che la limitano. La prima traccia del piano contiene le prime tracce delle rette dei lati, la seconda traccia ne contiene le seconde tracce.

Per ogni lato si fa quello che si è visto per la retta generica:

1. si prolunga la seconda proiezione fino alla LT e si trova la seconda proiezione della prima traccia;
2. si prolunga la prima proiezione e si trova la prima proiezione della seconda traccia;
3. con i richiami si arriva alle tracce vere.

Bastano due lati, perché la traccia di un piano è una retta e per una retta bastano due punti. La terza retta, se si trova, serve solo da controllo.

Un punto all'infinito è una direzione, e una retta si costruisce anche con un punto proprio e un punto improprio. Se un lato sta su un'orizzontale, la sua prima traccia è all'infinito: la prima traccia del piano passa per la prima traccia dell'altro lato ed è parallela a o₁. Se un lato sta su una frontale, la seconda traccia del piano è parallela a f₂.

Le tracce non sono però sempre utili, perché spesso finiscono lontano.

> [!example] Disegno 43 · Le tracce del piano dalle proiezioni del triangolo
> ![[06-tracce-dal-triangolo-generico.svg|660]]
>
> Per la retta r del lato AB e la retta s del lato BC si trovano le tracce con i punti notevoli sulla LT.
> t₁α passa per T₁ᵣ e T₁ₛ, t₂α per T₂ᵣ e T₂ₛ, e le due tracce si incontrano sulla LT; le tracce della retta m del lato AC servono da controllo.

---

## 6. LA PERPENDICOLARITÀ (20 ottobre)

### 6.1 La retta perpendicolare a un piano (20 ottobre)

#### 6.1.1 Il teorema di Monge (20 ottobre)

Una retta è perpendicolare a un piano se è perpendicolare a due rette del piano.

Monge traduce questa condizione nelle proiezioni: una retta è perpendicolare a un piano se le proiezioni della retta sono perpendicolari alle rispettive tracce del piano. È il teorema di Monge: r ⊥ α se r₁ ⊥ t₁α e r₂ ⊥ t₂α.

La retta può essere esterna al piano, ma la stessa perpendicolarità vale per rette che appartengono al piano.

> [!example] Disegno 44 · La retta perpendicolare a un piano
> ![[06-retta-perpendicolare-al-piano.svg|600]]
>
> Dal punto P si traccia r₂ perpendicolare a t₂α e r₁ perpendicolare a t₁α, segnando gli angoli retti.
>
> ![[b06-spazio-retta-perpendicolare-al-piano.svg|600]]
>
> Nello spazio (schema proposto, non disegnato a lezione): la retta r per P incontra α nel punto H ad angolo retto, e le sue proiezioni risultano perpendicolari alle tracce del piano.

#### 6.1.2 Senza tracce: con l'orizzontale e la frontale (20 ottobre)

Se il piano è dato da una figura e non si hanno le tracce, si torna alla prima definizione: la retta è perpendicolare al piano quando è perpendicolare a due rette del piano. Le rette che vengono in soccorso sono l'orizzontale e la frontale.

La perpendicolare si costruisce imponendo l'angolo retto:

- tra la prima proiezione della retta e la prima proiezione dell'orizzontale (r₁ ⊥ o₁);
- tra la seconda proiezione della retta e la seconda proiezione della frontale (r₂ ⊥ f₂).

Il motivo sta ancora nei piani ausiliari:

- se per la retta r si fa passare un piano proiettante in seconda, r₂ coincide con la sua seconda traccia, che è perpendicolare a f₂;
- se si fa passare un piano proiettante in prima, r₁ coincide con la sua prima traccia, perpendicolare a o₁.

Le condizioni sono più facili di quello che sembrano, perché sono tutte collegate.

> [!example] Disegno 45 · La perpendicolare con l'orizzontale e la frontale
> ![[06-perpendicolare-con-orizzontale-e-frontale.svg|620]]
>
> Nel triangolo ABC l'orizzontale o passa per A e B (A₂B₂ parallelo alla LT), la frontale f per A e C (A₁C₁ parallelo alla LT).
> Dal punto Q si traccia r₁ perpendicolare a o₁ e r₂ perpendicolare a f₂: r è perpendicolare a due rette del piano, quindi al piano.

### 6.2 I piani perpendicolari (20 ottobre)

#### 6.2.1 La condizione (20 ottobre)

Due piani sono perpendicolari tra loro se uno dei due contiene una retta perpendicolare all'altro.

#### 6.2.2 Due piani proiettanti (20 ottobre)

Per i piani proiettanti la verifica è immediata. Un quaderno aperto e messo in piedi sul banco dà due piani proiettanti in prima, e le loro tracce sul banco sono le prime tracce: quando le due metà sono ortogonali, l'angolo di 90° sta a terra, su π₁.

Due piani proiettanti in prima sono quindi perpendicolari se le loro prime tracce sono perpendicolari. È un fatto, non un'interpretazione, ma vale solo perché si tratta di due piani particolari: con un piano generico non si può fare.

Lo stesso vale per due piani proiettanti in seconda, che sono perpendicolari se lo sono le loro seconde tracce.

Si può comunque verificare la condizione, cercando nel piano δ una retta perpendicolare a γ:

- per essere perpendicolare a γ la retta deve avere r₂ perpendicolare a t₂γ, che è perpendicolare alla LT, quindi r₂ è parallela alla LT: è un'orizzontale;
- per appartenere a δ, che è proiettante in prima, deve avere r₁ sulla prima traccia, quindi r₁ ≡ t₁δ, che è perpendicolare a t₁γ.

δ contiene una retta perpendicolare a γ, e i due piani sono perpendicolari.

> [!example] Disegno 46 · Due piani proiettanti in prima perpendicolari
> ![[06-piani-proiettanti-perpendicolari.svg|560]]
>
> γ e δ hanno le seconde tracce perpendicolari alla LT e l'angolo retto tra le prime tracce t₁γ e t₁δ.
> La retta r di δ, con r₁ ≡ t₁δ e r₂ parallela alla LT, ha r₁ ⊥ t₁γ e r₂ ⊥ t₂γ, quindi r ⊥ γ.
>
> ![[b06-spazio-piani-perpendicolari.svg|600]]
>
> Nello spazio (schema proposto, non disegnato a lezione): le due metà del quaderno sono verticali e l'angolo retto si vede sul banco, tra t₁γ e t₁δ.

> [!example] Disegno 47 · Due piani proiettanti in seconda perpendicolari
> ![[b06-piani-proiettanti-in-seconda-perpendicolari.svg|560]]
>
> Schema proposto, non disegnato a lezione.
> β ed ε hanno le prime tracce perpendicolari alla LT e l'angolo retto tra le seconde tracce.
> La frontale r di ε, con r₂ ≡ t₂ε e r₁ parallela alla LT, è perpendicolare a β.

#### 6.2.3 Un piano perpendicolare a un piano generico (20 ottobre)

Si può disegnare un piano generico perpendicolare a un piano generico, ma è abbastanza complicato.

Serve invece un piano facile, perpendicolare a quello dato, che dimostri anche la proprietà, cioè che contenga una retta perpendicolare all'altro piano. È proprio ciò che servirà nei ribaltamenti.

Si usa un piano ausiliario γ proiettante in prima, imponendo la regola: t₁γ perpendicolare a t₁α. Il proiettante in prima non va usato in modo acritico, ma in modo cosciente, con questa condizione.

Per dimostrare che α e γ sono perpendicolari si usa un'orizzontale di α:

- la sua prima proiezione, parallela a t₁α, è perpendicolare a t₁γ;
- la sua seconda proiezione, parallela alla LT, è perpendicolare a t₂γ.

Quell'orizzontale è quindi perpendicolare a γ, e i due piani sono perpendicolari.

> [!example] Disegno 48 · Un piano proiettante in prima perpendicolare a un piano generico
> ![[06-piano-perpendicolare-al-generico.svg|560]]
>
> Il piano γ ha t₁γ ⊥ t₁α (si segnano i 90°) e t₂γ perpendicolare alla LT.
> L'orizzontale di α ha o₁ ⊥ t₁γ e o₂ ⊥ t₂γ. Nello schema c'è anche la verifica inversa: la retta r di γ, con r₁ ≡ t₁γ e r₂ ⊥ t₂α, è perpendicolare ad α.

---

## 7. FIGURE PIANE E SOLIDI (13 e 20 ottobre)

### 7.1 La figura e il suo piano (20 ottobre)

Una figura non è di per sé un piano generico: è una figura messa in una certa posizione, che appartiene a un piano. A seconda di come la si colloca nel modello, lo stesso triangolo può stare in un piano verticale, frontale, orizzontale, proiettante o generico, e le condizioni di appartenenza restano sempre rispettate.

Come si riconosce il piano dalle proiezioni della figura si è visto nel capitolo sul piano; come si passa dalla figura alle tracce, nel capitolo sull'appartenenza.

### 7.2 La vera grandezza (13 e 20 ottobre)

Solo in alcune posizioni il disegno corrisponde alle misure vere della figura.

- Nel piano frontale la seconda proiezione è in vera grandezza. Il piano che contiene la figura e il piano su cui si proietta sono paralleli, il centro di proiezione è all'infinito e l'asse dell'omologia è all'infinito: la figura si riproduce esattamente, come in una traslazione intesa come rapporto omologico tra due figure.
- Nel piano orizzontale, come nella pianta, è in vera grandezza la prima proiezione.
- Nel piano di profilo è in vera grandezza la terza proiezione.

Sono le configurazioni usate di più in architettura.

Ma non tutto ciò che si disegna è ad angolo retto. Una figura su un piano proiettante è il risultato di una proiezione tra piani non paralleli tra loro: in una proiezione si riduce a una linea, nelle altre appare accorciata, e la sua vera grandezza non è nessuna di esse. Per recuperarla si usa il ribaltamento.

> [!example] Disegno 49 · Il quadrato nel piano proiettante in prima
> ![[04-quadrato-piano-proiettante-in-prima.svg|620]]
>
> In prima proiezione il quadrato è un segmento su t₁α (A₁ ≡ D₁, B₁ ≡ C₁).
> In seconda proiezione l'altezza è vera ma la larghezza è ridotta; in terza è ancora più stretto. Nessuna delle tre proiezioni è in vera grandezza.

### 7.3 I solidi (20 ottobre)

I solidi sono delimitati da una serie di facce, che sono figure piane.

- Lo spigolo è il lato comune a due facce.
- Il diedro è la porzione di spazio delimitata da due semipiani: due facce vicine che si intersecano formano un diedro.

In una piramide triangolare ci sono tre facce laterali, che si incontrano nel vertice.

Il solido più usato è il parallelepipedo, le cui facce sono parallelogrammi. Nella consuetudine si chiama parallelepipedo il parallelepipedo rettangolo, ma bisognerebbe specificarlo.

Il prisma è un solido in cui la base inferiore e la base superiore sono due figure piane congruenti e parallele, unite tra loro dalle facce laterali. Congruenti significa che, sovrapposte, coincidono perfettamente.

Il parallelepipedo rettangolo è quindi un prisma, ma si può avere anche, per esempio, un prisma a base triangolare.

Per capire in che piano sta una faccia di un solido si ragiona come per qualunque figura piana, sulle rette dei suoi lati.

> [!example] Disegno 50 · Piramide, parallelepipedo e prisma
> ![[06-solidi-piramide-prisma-parallelepipedo.svg|700]]
>
> Nella piramide a base triangolare le tre facce laterali si incontrano nel vertice.
> Nel parallelepipedo rettangolo ogni spigolo è il lato comune di due facce, che formano un diedro.
> Nel prisma a base triangolare le due basi sono congruenti e parallele.

---

## 8. IL RIBALTAMENTO (20 e 22 ottobre)

### 8.1 Perché si ribalta un piano (22 ottobre)

Quando una figura sta su un piano proiettante, le sue proiezioni non dicono quanto è grande davvero.

Nel piano proiettante in prima, per esempio, un triangolo ABC diventa in prima proiezione tre punti A₁, B₁, C₁ allineati su t₁α: non può essere altrimenti, perché il piano è visto di taglio. Nemmeno la seconda proiezione basta: il triangolo A₂B₂C₂ è più stretto di quello vero, perché il piano che lo contiene è inclinato rispetto a π₂.

Il ribaltamento è l'operazione con cui si fa ruotare il piano che contiene la figura intorno a una delle sue tracce, finché non si appoggia su un piano di proiezione. Il ribaltamento fa conoscere la vera grandezza e forma della figura.

### 8.2 Il piano mobile e la cerniera (20 e 22 ottobre)

Nel modello il ribaltamento si vede con un piano proiettante in prima mobile: un cartoncino grande, piegato o tagliato alla base, che resta in piedi ma può ruotare intorno alla sua prima traccia.

Finché il piano è inclinato rispetto a π₁, la proiezione del triangolo disegnato sul cartoncino non ha la sua vera grandezza: le lunghezze dei lati e gli angoli non sono quelli veri. Ruotando il cartoncino intorno alla prima traccia fino a farlo coincidere con π₁, la figura appare vera.

Le rotazioni avvengono sempre intorno alle tracce. La traccia intorno a cui il piano ruota si chiama cerniera, ed è l'asse di rotazione.

> [!example] Disegno 51 · Il piano mobile
> ![[06-spazio-piano-mobile.svg|600]]
>
> Il piano γ è proiettante in prima e il triangolo ABC ha la prima proiezione su t₁γ.
> Il piano ruota intorno a t₁γ, che fa da cerniera, fino a stendersi su π₁: il triangolo (A)(B)(C) è in vera forma.

### 8.3 La rotazione avviene lungo archi di circonferenza (20 e 22 ottobre)

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

### 8.4 Il ribaltamento del piano proiettante in prima (22 ottobre)

#### 8.4.1 Su π₁, intorno alla prima traccia (22 ottobre)

Per ribaltare su π₁ un piano proiettante in prima la seconda traccia non serve: tutto avviene sul primo piano di proiezione, e la cerniera è la prima traccia t₁α.

Il punto A ha la prima proiezione A₁ su t₁α. Quando il piano si abbatte, A arriva su π₁ lungo la perpendicolare a t₁α condotta da A₁.

Si allontana dalla traccia esattamente quanto era alto, perché il raggio di rotazione è la distanza del punto dalla cerniera, cioè la sua quota. La quota si legge sul disegno come distanza di A₂ dalla linea di terra, e si riporta con il compasso sulla perpendicolare a partire da A₁: lì c'è A\*.

> [!example] Disegno 53 · Il proiettante in prima ribaltato su π₁
> ![[07-ribaltamento-proiettante-in-prima-su-pi1.svg|620]]
>
> Da A₁ si traccia la perpendicolare a t₁α e vi si riporta la quota di A, cioè la distanza di A₂ dalla LT: si trova A\*.
> Si fa lo stesso per B e per C, segnando i segmenti uguali con le lineette; A\*B\*C\* è la vera grandezza e forma.

#### 8.4.2 Su π₂, intorno alla seconda traccia (22 ottobre)

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

### 8.5 Il ribaltamento del piano proiettante in seconda (22 ottobre)

Nel piano proiettante in seconda la seconda proiezione della figura si riduce a una linea su t₂α, e la prima proiezione non è in vera grandezza. Valgono le stesse due possibilità: si può ribaltare su π₁ o su π₂.

#### 8.5.1 Su π₁, intorno alla prima traccia (22 ottobre)

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

#### 8.5.2 Su π₂, intorno alla seconda traccia (22 ottobre)

Per ribaltare su π₂ si fa ruotare il piano intorno alla seconda traccia. Anche qui la rotazione avviene su piani perpendicolari all'asse: ogni punto ribaltato si trova sulla perpendicolare a t₂α condotta dalla sua seconda proiezione, a una distanza uguale al suo aggetto.

> [!example] Disegno 56 · Il proiettante in seconda ribaltato su π₂
> ![[07-ribaltamento-proiettante-in-seconda-su-pi2.svg|620]]
>
> Da A₂ si traccia la perpendicolare a t₂α e vi si riporta l'aggetto di A, cioè la distanza di A₁ dalla LT: si trova A\*.
> Il triangolo A\*B\*C\* è uguale a quello ribaltato su π₁.

### 8.6 Una sola figura e le lineette di uguaglianza (22 ottobre)

I modi per ribaltare un piano proiettante sono due, intorno alla prima traccia o intorno alla seconda. Riassumendo:

- proiettante in prima su π₁: cerniera t₁α, si riporta la quota sulla perpendicolare a t₁α;
- proiettante in prima su π₂: cerniera t₂α, la quota non cambia;
- proiettante in seconda su π₁: cerniera t₁α, l'aggetto non cambia;
- proiettante in seconda su π₂: cerniera t₂α, si riporta l'aggetto sulla perpendicolare a t₂α.

I due ribaltamenti della stessa figura devono risultare identici. Il ribaltamento non può produrre un'altra figura: la figura è una sola, e quelle che si disegnano sono altre sue proiezioni.

Ogni volta che si riporta una misura, i due segmenti uguali si segnano con lo stesso numero di lineette: una per il primo punto, due per il secondo, tre per il terzo. Va fatto sempre, perché chi disegna deve far capire quello che ha fatto.

### 8.7 L'omologia di ribaltamento (22 ottobre)

#### 8.7.1 Ruotare equivale a proiettare (22 ottobre)

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

#### 8.7.2 Il punto unito sulla cerniera (22 ottobre)

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
