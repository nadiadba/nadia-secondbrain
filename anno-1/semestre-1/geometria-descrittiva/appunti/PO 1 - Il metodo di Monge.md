---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-08
tags: [geometria-descrittiva, appunti, teoria]
---

# PO 1 - Il metodo di Monge

> [!info] Note collegate
> Precedente: — · Successiva: [[PO 2 - Il punto]]
>
> Esercizi: [[esercitazioni|Esercitazioni]] · Teoria collegata: [[teoria-omologia]]
>
> Bozze delle lezioni: [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]]

Capitolo 1 di 8 della teoria delle proiezioni ortogonali. Lezioni: 8, 13, 15 e 22 ottobre.

Le otto pagine raccolgono in ordine logico tutta la teoria delle proiezioni ortogonali (il metodo di Monge) spiegata nelle lezioni dall'8 al 22 ottobre. Si parte dal metodo e dai piani di proiezione, si passa al punto, alla retta e al piano, poi alle relazioni tra questi elementi (appartenenza e perpendicolarità), e si arriva alle figure piane e al ribaltamento, che permette di vederle in vera grandezza.

## 1.1 Proiezioni centrali e proiezioni cilindriche (8 ottobre)

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

## 1.2 I tre piani di proiezione e il triedro (8 e 13 ottobre)

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

### 1.2.1 La linea di terra (13 ottobre)

La linea di terra (LT) è la retta di intersezione tra π₁ e π₂. Quando si ribaltano i piani gli uni sugli altri, divide la pianta dal prospetto.

Non divide però lo spazio in modo rigido: le prime proiezioni non stanno per forza sotto la LT e le seconde sopra, perché dipende dal quadrante in cui si trovano i punti. In architettura, naturalmente, le cose stanno tutte nel primo diedro.

## 1.3 Dallo spazio al foglio (8 e 13 ottobre)

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

## 1.4 La notazione (8, 13, 15 e 22 ottobre)

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

## 1.5 Pianta, sezione e prospetti (8 ottobre)

La pianta è una sezione orizzontale, fatta con un piano parallelo a π₁. La quota a cui si taglia l'edificio deve intercettare le finestre e comprendere tutti gli elementi che compongono l'edificio, altrimenti la pianta mostrerebbe uno spazio completamente chiuso.

La sezione verticale passa per due punti precisi della pianta, taglia i muri trasversalmente ed è perpendicolare al piano orizzontale. Non è mai parallela al piano orizzontale, altrimenti diventerebbe una pianta.

La pianta da sola non basta a dare l'idea della forma. Per stabilire i volumi dell'oggetto si disegnano anche i prospetti, cioè le proiezioni ortogonali fatte sui piani verticali del triedro.

Il prospetto è ciò che si vede guardando l'edificio da fuori, da uno dei suoi lati, come se ci si camminasse intorno.

### 1.5.1 Da che parte si guarda (8 ottobre)

Il prospetto si guarda sempre da fuori; solo la sezione permette di guardare da dentro.

Per questo la linea di terra va messa dalla parte da cui si guarda il lato da rappresentare. Per il lato che in pianta sta in alto, la LT va in alto, lontana dalla pianta, e il prospetto si disegna a testa in giù.

Se invece si mette la LT subito sopra la pianta e si disegna il prospetto in piedi, il prospetto viene specchiato: si sta guardando l'edificio da dentro, e una rientranza che chi guarda vede a destra finisce a sinistra.

È come la mano: per vedere il dorso bisogna guardare dalla parte del dorso, non del palmo.

Un modo semplice per non sbagliare è immaginare di camminare intorno all'edificio disegnato in pianta.

1. Per disegnare un prospetto ti metti fuori dall'edificio, davanti al lato che vuoi rappresentare, con le spalle verso l'esterno del foglio.
2. La linea di terra va tra te e l'edificio: dalla tua parte, cioè dalla parte di quel lato.
3. Il prospetto si disegna oltre la linea di terra, ancora più lontano dalla pianta, "in piedi" rispetto a te che guardi da lì.
4. Per il lato in basso nel foglio sei tu che guardi normalmente, quindi il prospetto viene dritto. Per il lato in alto stai guardando dalla parte opposta del foglio, quindi il prospetto, visto da te seduta al tavolo, è a testa in giù. Per leggerlo basta girare il foglio, o girarci intorno.

> [!example] Disegno 4 · Il prospetto giusto e quello sbagliato
> ![[03-prospetto-giusto-e-sbagliato.svg|660]]
>
> La forma dell'edificio è uno schema: conta solo la rientranza.
> Giusto: la LT sta in alto e il prospetto scende dalla LT verso la pianta, a testa in giù; girando il foglio la rientranza è a destra.
> Sbagliato: la LT sta subito sopra la pianta e il prospetto è in piedi; la rientranza finisce dalla parte sbagliata.

## 1.6 Le scale di rappresentazione (8 ottobre)

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

## Collegamenti

Il capitolo successivo è [[PO 2 - Il punto]].
