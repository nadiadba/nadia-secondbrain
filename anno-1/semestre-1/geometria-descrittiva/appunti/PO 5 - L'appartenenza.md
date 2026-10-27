---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-13
tags: [geometria-descrittiva, appunti, teoria]
---

# PO 5 - L'appartenenza

> [!info] Note collegate
> Precedente: [[PO 4 - Il piano]] · Successiva: [[PO 6 - La perpendicolarità]]
>
> Esercizi: [[esercitazioni|Esercitazioni]] · Teoria collegata: [[teoria-omologia]]
>
> Bozze delle lezioni: [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]]

Capitolo 5 di 8 della teoria delle proiezioni ortogonali. Lezioni: 13-20 ottobre.

## 5.1 Le tre condizioni di appartenenza (13 e 15 ottobre)

### 5.1.1 Il punto e la retta (13 ottobre)

Un punto appartiene a una retta quando le proiezioni del punto appartengono alle proiezioni della retta: P₁ sta su r₁ e P₂ sta su r₂.

### 5.1.2 La retta e il piano (13 e 15 ottobre)

Una retta appartiene a un piano quando tutti i suoi punti appartengono al piano. In pratica se ne prendono due, che quando è possibile sono le tracce.

Una retta appartiene a un piano quando le tracce della retta appartengono alle rispettive tracce del piano: T₁ᵣ su t₁α, T₂ᵣ su t₂α, T₃ᵣ su t₃α.

Non basta che una sola traccia della retta stia su una traccia del piano: un piano che contiene T₁ᵣ ma non T₂ᵣ non contiene la retta.

Se una traccia della retta è all'infinito, anche quel punto all'infinito deve stare sulla traccia corrispondente del piano. Questo succede solo se la proiezione della retta e la traccia del piano sono parallele.

### 5.1.3 Il punto e il piano (13 e 15 ottobre)

Un punto appartiene a un piano se appartiene a una retta del piano. È una concatenazione: P ∈ r e r ⊂ α, quindi P ∈ α.

Le condizioni vanno rispettate tutte: il punto sulla retta, e la retta sul piano con le sue tracce sulle tracce del piano.

Bisogna anche non confondere le tracce con le proiezioni: le condizioni sulla retta e sul piano parlano di tracce, quella sul punto e sulla retta parla di proiezioni.

## 5.2 Regola e coincidenze (13 e 15 ottobre)

Tranne nei piani particolari, la proiezione di un punto del piano non va a finire sulla traccia: la traccia è soltanto l'intersezione del piano con un piano di proiezione.

Nei piani particolari ci sono però delle coincidenze:

- nei piani verticali (proiettante in prima, frontale, di profilo) la prima proiezione di tutto ciò che sta sul piano coincide con la prima traccia;
- nel piano proiettante in seconda e nel piano orizzontale la seconda proiezione di tutto ciò che sta sul piano coincide con la seconda traccia;
- nel piano parallelo alla linea di terra tutte le terze proiezioni coincidono con la terza traccia.

Queste coincidenze vanno distinte dalla regola. La regola resta una sola: il punto appartiene al piano perché appartiene a una retta del piano.

Nel piano proiettante in prima, per esempio, P₁ cade sulla prima traccia; ma la dimostrazione passa per una retta. La retta verticale r per P ha r₁ ≡ T₁ᵣ ≡ P₁, e T₁ᵣ sta su t₁α: quindi r appartiene ad α, e P, che sta su r, appartiene ad α.

## 5.3 Le rette ausiliarie: l'orizzontale e la frontale (15 e 20 ottobre)

Per dimostrare che un punto sta su un piano si può usare qualunque retta del piano, anche una generica. Le rette che aiutano di più sono però le due ausiliarie, l'orizzontale e la frontale, che vanno disegnate in modo immediato, senza esitazioni, perché servono per qualunque cosa.

L'orizzontale e la frontale sono le rette che servono a risolvere i problemi.

### 5.3.1 Le rette che stanno sul piano generico (15 ottobre)

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

### 5.3.2 L'orizzontale del piano (15 ottobre)

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

### 5.3.3 La frontale del piano (15 ottobre)

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

## 5.4 Disegnare un punto che appartiene a un piano (15 e 20 ottobre)

### 5.4.1 Nel piano generico, con l'orizzontale (15 e 20 ottobre)

Per disegnare un punto del piano generico α si disegna prima una sua orizzontale, come visto sopra. Su questa orizzontale si sceglie un punto qualunque e se ne disegnano le proiezioni.

> [!example] Disegno 30 · Un punto del piano generico con l'orizzontale
> ![[06-punto-piano-generico-orizzontale.svg|620]]
>
> Si traccia o₂ parallela alla LT: dove incontra t₂α c'è T₂ₒ. Da T₂ₒ si scende alla LT, in (T₂ₒ)₁, e si traccia o₁ parallela a t₁α.
> Si sceglie P₂ su o₂ e si scende con il richiamo fino a o₁: lì c'è P₁. P sta su una retta di α, quindi P ∈ α.

### 5.4.2 Nel piano generico, con la frontale (15 ottobre)

Con la frontale si comincia da f₁, parallela alla LT, che incontra t₁α in T₁f. Poi f₂ deve avere la direzione che porta il suo punto all'infinito sulla traccia del piano, quindi si costruisce parallela a t₂α.

Si dimostra così che P appartiene a f e che f appartiene ad α.

> [!example] Disegno 31 · Un punto del piano generico con la frontale
> ![[05-frontale-piano-generico.svg|620]]
>
> f₁ parallela alla LT incontra t₁α in T₁f; da (T₁f)₂ sulla LT si traccia f₂ parallela a t₂α.
> Si sceglie P₂ su f₂ e si scende fino a f₁: lì c'è P₁. P ∈ f ⊂ α.

### 5.4.3 Nei piani proiettanti (20 ottobre)

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

### 5.4.4 Verificare se un punto appartiene a un piano (15 ottobre)

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

## 5.5 I piani ausiliari (15 e 20 ottobre)

I piani ausiliari sono il piano proiettante in prima e il piano proiettante in seconda. Insieme alle rette ausiliarie, sono i pochi strumenti fatti apposta per risolvere quasi tutti i problemi della geometria descrittiva.

Aiutano grazie alla loro coincidenza: tutto ciò che sta sul proiettante in prima ha la prima proiezione sulla prima traccia, tutto ciò che sta sul proiettante in seconda ha la seconda proiezione sulla seconda traccia.

### 5.5.1 La retta generica nei piani proiettanti (15 ottobre)

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

### 5.5.2 La terza traccia della retta generica (15 ottobre)

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

## 5.6 I piani che contengono una retta (15 ottobre)

### 5.6.1 Il metodo (15 ottobre)

Per una retta passano infiniti piani: per una retta verticale, per esempio, passano infiniti piani verticali, ma solo quelli.

Per trovare quali piani possono contenere una retta data:

1. si colloca la retta nel modello e si guardano i piani su cui si appoggia, partendo dall'associazione più immediata tra il nome della retta e il nome del piano (una retta proiettante in seconda sta sicuramente in un piano proiettante in seconda);
2. si disegnano i piani rispettando la condizione di appartenenza: le tracce del piano passano per le tracce della retta.

Per questo, nel disegno delle condizioni, contano le tracce della retta più che le sue proiezioni.

Lo schema del triedro che accompagna questi disegni non è propriamente un'assonometria, ma una trasposizione grafica del modello.

### 5.6.2 La retta proiettante in prima (15 ottobre)

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

### 5.6.3 La retta proiettante in seconda (15 ottobre)

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

### 5.6.4 La retta parallela alla linea di terra (15 ottobre)

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

### 5.6.5 La retta orizzontale (15 ottobre)

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

### 5.6.6 La retta frontale (15 ottobre)

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

### 5.6.7 La retta di profilo (15 ottobre)

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

## 5.7 Il piano dato da una figura (20 ottobre)

### 5.7.1 Forma mongiana e forma tecnica (20 ottobre)

Finora i piani sono stati considerati nella loro estensione, attraverso le tracce. È la forma mongiana, in cui anche la retta è definita dai suoi due punti notevoli, le tracce.

Un piano può però essere rappresentato da qualunque figura piana, per esempio da un triangolo: tre punti individuano un piano, e il triangolo disegnato nelle sue due proiezioni è già il piano.

Questa è la forma tecnica, quella del disegno di architettura, in cui non è sempre necessario avere le tracce. Le due forme non sono due cose diverse: si può lavorare con le tracce o senza, è indifferente.

Se si hanno le tracce si possono disegnare le proiezioni della figura, e se si hanno le proiezioni della figura si possono trovare le tracce.

### 5.7.2 Riconoscere le rette dei lati (20 ottobre)

Per capire in che piano sta una figura si guardano le rette a cui appartengono i lati.

Un lato è un segmento, e il segmento appartiene a una retta: se una proiezione contiene due lettere, l'altra proiezione contiene le stesse lettere.

- Se un lato ha la seconda proiezione parallela alla LT, sta su un'orizzontale.
- Se ha la prima proiezione parallela alla LT, sta su una frontale.
- Se ha tutte e due le proiezioni perpendicolari alla LT, sta su una retta di profilo.
- Se ha tutte e due le proiezioni inclinate rispetto alla LT, sta su una retta generica.

Se tutti e tre i lati di un triangolo stanno su rette generiche, il piano che contiene la figura è un piano generico.

### 5.7.3 Una retta del piano della figura: l'orizzontale (20 ottobre)

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

### 5.7.4 Dalle proiezioni della figura alle tracce del piano (20 ottobre)

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

## Collegamenti

Il capitolo successivo è [[PO 6 - La perpendicolarità]]. Il capitolo precedente è [[PO 4 - Il piano]].
