---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-11-17
tags: [geometria-descrittiva, bozza]
---

# La prospettiva: gli elementi, tracce e fughe, il metodo della pianta

> [!info] Note collegate
> Sbobina: [[13-prospettiva-metodo-della-pianta]]
>
> Bozza precedente: [[12-errori-della-prova-1-e-quadro-verticale]] · Bozza successiva: [[14-altezze-e-punto-di-misura-in-prospettiva]] · Poi: [[16-la-prospettiva-a-occhio-di-formica]]
>
> Argomenti collegati: [[02-proiezioni-e-omologia-schema]] · [[03-proiezioni-ortogonali-punto-e-rette]] · [[12-errori-della-prova-1-e-quadro-verticale]] · [[studio-villa-tugendhat]]

La lezione di martedì 17 novembre apre l'ultimo argomento del corso: la prospettiva. È tutta un'esercitazione guidata alla lavagna, registrata solo in parte e con un audio molto disturbato.

La docente salta alcuni passaggi per lasciare tempo agli esercizi di geometria, e avverte che sulla prospettiva tornerà nelle lezioni successive (le bozze [[14-altezze-e-punto-di-misura-in-prospettiva|14]] e [[16-la-prospettiva-a-occhio-di-formica|16]]).

In questa bozza la teoria è messa in ordine, dai prerequisiti in su:

- prima gli elementi della prospettiva (punto di vista, quadro, geometrale, orizzonte, fondamentale, O₀, O*, cerchio di distanza), con i disegni nello spazio;
- poi la regola che regge tutto: la traccia e la fuga di una retta;
- infine il metodo della pianta, cioè come si costruisce la prospettiva di una figura partendo dalla sua pianta, come alla lavagna.

La prospettiva non c'è nel libro della docente (il libro annuncia un secondo volume sulla prospettiva e le ombre): le fonti sono le lezioni. È l'argomento della Prova n. 3, giovedì 17 dicembre.

## GLI ELEMENTI DELLA PROSPETTIVA

### La prospettiva è una proiezione dal centro proprio

All'inizio del corso si è visto che ogni metodo di rappresentazione è una proiezione: da un centro partono i raggi proiettanti, che portano i punti dello spazio su un piano.

- Se il centro è all'infinito, i raggi sono tutti paralleli: sono le proiezioni parallele, cioè le proiezioni ortogonali e l'assonometria.
- Se il centro è proprio, cioè a distanza finita, i raggi partono tutti da un punto: è la proiezione centrale, e da essa nasce la prospettiva.

Nella prospettiva il centro di proiezione è l'occhio di chi guarda. Per questo la prospettiva è il metodo più vicino a come vediamo, e a una fotografia.

C'è però una differenza importante con l'assonometria, che la docente ricorda nel ripasso del 24 novembre:

- in assonometria le rette parallele nella realtà restano parallele nel disegno;
- in prospettiva le rette parallele perdono il parallelismo: nel disegno concorrono in un punto, la loro fuga.

La notazione è quella dell'omologia: la prospettiva di un punto A si scrive con l'apice, A′.

### Il punto di vista, il quadro e il geometrale

Gli elementi nello spazio sono tre.

1. Il punto di vista O: è l'occhio dell'osservatore (alla lavagna, «l'omino»). Sta a una certa altezza h da terra e a una certa distanza d dal quadro.
2. Il quadro (o piano di quadro): è un piano verticale, messo tra l'osservatore e l'oggetto. È il foglio da disegno: tutto quello che disegniamo sta sul quadro.
3. Il geometrale: è il piano orizzontale di terra, su cui stanno l'osservatore e gli oggetti.

La prospettiva di un punto P è il punto P′ in cui il raggio proiettante OP buca il quadro.

> [!example] Disegno 1 · Il disegno nello spazio: gli elementi della prospettiva
> ![[b13-spazio-elementi-della-prospettiva.svg|620]]
>
> 1. Il quadro è verticale, il geometrale orizzontale. Si tagliano lungo una retta, la fondamentale.
> 2. Il punto di vista O sta all'altezza h dal geometrale e alla distanza d dal quadro.
> 3. Il piano orizzontale che passa per l'occhio (piano d'orizzonte) taglia il quadro lungo l'orizzonte.
> 4. Il piede della perpendicolare da O al quadro è O₀: sta sull'orizzonte.
> 5. Il raggio da O a un punto P del geometrale buca il quadro in P′, che sta tra l'orizzonte e la fondamentale.

### L'orizzonte e la fondamentale

Sul quadro ci sono due rette orizzontali, che sono il riferimento di ogni prospettiva. La docente lo dice all'inizio dell'esercitazione: per disegnare sul piano di quadro servono orizzonte e fondamentale.

- La fondamentale è la retta in cui il quadro taglia il geometrale. È la traccia del piano geometrale sul quadro.
- L'orizzonte è la retta in cui il quadro è tagliato dal piano orizzontale che passa per l'occhio. Sta quindi sopra la fondamentale, alla distanza h, l'altezza dell'occhio.

La distanza tra orizzonte e fondamentale dice dunque quanto è alto l'osservatore rispetto all'oggetto. Per deciderla, la docente usa uno schema laterale, in cui si vedono di profilo l'omino, il quadro e l'oggetto: il 17 novembre lo salta e lo riprende il 19 (bozza [[14-altezze-e-punto-di-misura-in-prospettiva|14]]).

Sul foglio la fondamentale conviene metterla almeno un paio di centimetri sotto l'orizzonte, così si vede bene che cosa succede dentro.

### Il punto principale O₀, la distanza e O*

Il punto O₀ («O con zero») è il punto principale. È il piede della perpendicolare condotta da O al quadro, e sta sull'orizzonte, perché la perpendicolare è orizzontale.

La distanza d tra O e O₀ è la distanza del punto di vista dal quadro.

Sul foglio non si può disegnare O, che sta fuori dal quadro. Allora si ribalta: il piano d'orizzonte gira intorno all'orizzonte, come una pagina, fino ad appoggiarsi sul quadro. Il punto O arriva in O* («O asterisco»), sulla verticale di O₀, alla distanza d da O₀.

Con centro in O₀ e raggio uguale alla distanza d si disegna il cerchio di distanza. La docente lo fa disegnare intero. O* sta sul cerchio.

> [!example] Disegno 2 · Il disegno nello spazio: O ribaltato diventa O*, il cerchio di distanza
> ![[b13-spazio-ribaltamento-di-o-e-cerchio-di-distanza.svg|620]]
>
> 1. Il piano d'orizzonte contiene O e taglia il quadro lungo l'orizzonte.
> 2. Il piano d'orizzonte ruota intorno all'orizzonte e si appoggia sul quadro: O descrive un quarto di cerchio e arriva in O*, sotto O₀, alla distanza d.
> 3. Con centro O₀ e raggio d si traccia il cerchio di distanza: passa per O*.
> 4. Le rette da O a 45° rispetto al quadro incontrano l'orizzonte esattamente sul cerchio di distanza, nei due punti di distanza (vedi più avanti).

Il ribaltamento non cambia le figure che stanno nel piano d'orizzonte: per questo, come si vedrà nella bozza [[14-altezze-e-punto-di-misura-in-prospettiva|14]], in O* si leggono gli angoli veri.

### Sul foglio: la pianta e la prospettiva insieme

Nel metodo della pianta si disegnano sullo stesso foglio due cose:

- la pianta, cioè la figura vista dall'alto, con la linea del quadro e il punto di vista O;
- la prospettiva, sul quadro, tra orizzonte e fondamentale.

La docente fa coincidere la linea del quadro in pianta con l'orizzonte: è una linea unica, «lunga lunga lunga». Allora O, visto dall'alto, cade proprio dove sta O*: a partire da O* si conta la distanza, e lì si colloca l'orizzonte. La distanza che si vede in pianta è uguale alla distanza sul quadro.

Il fatto che O e O* coincidano non è una cosa geometrica: è solo una comodità. Si potrebbe disegnare la pianta più in basso, per avere più spazio; l'importante è che il disegno sia chiaro. È una scelta della docente.

Il disegno si imposta così:

1. si traccia l'orizzonte, che è anche la linea del quadro in pianta;
2. si mette la fondamentale sotto, a un paio di centimetri;
3. si segna O₀ e, sotto, a distanza d, O* (che coincide con O della pianta);
4. con centro O₀ e raggio d si disegna il cerchio di distanza;
5. sopra l'orizzonte si disegna la pianta della figura.

## TRACCE E FUGHE

### La traccia e la fuga di una retta

Per disegnare una retta in prospettiva bastano due punti: la sua traccia e la sua fuga.

- La traccia è il punto in cui la retta incontra il piano di quadro. Sta sul quadro, quindi in prospettiva coincide con se stessa. Se la retta sta sul geometrale, la traccia è sulla fondamentale.
- La fuga è il punto in cui arriva sul quadro la parallela alla retta condotta dal punto di vista O. È la prospettiva del punto all'infinito della retta.

La docente fa ripetere la regola in coro: per trovare la fuga di una retta costruisco la parallela alla retta partendo da O. Se la retta appartiene al piano geometrale, la sua fuga sarà sull'orizzonte, perché la parallela per O è orizzontale e sta nel piano d'orizzonte.

La prospettiva r′ della retta r è la retta che congiunge la traccia e la fuga. Ogni punto di r ha la sua prospettiva su r′.

Quindi, per le rette del geometrale:

- le tracce stanno tutte sulla fondamentale;
- le fughe stanno tutte sull'orizzonte.

Rette parallele hanno la stessa parallela per O, quindi hanno lo stesso punto di fuga. È la regola che permette di chiudere le figure.

> [!example] Disegno 3 · Il disegno nello spazio: la traccia e la fuga di una retta
> ![[b13-spazio-traccia-e-fuga-di-una-retta.svg|620]]
>
> 1. La retta r sta sul geometrale e incontra il quadro in Tᵣ, sulla fondamentale: è la traccia.
> 2. Da O si conduce la parallela a r: è orizzontale e incontra il quadro in Fᵣ, sull'orizzonte: è la fuga.
> 3. r′ è la retta TᵣFᵣ. Il raggio da O a un punto A di r buca il quadro in A′, che sta proprio su r′.
> 4. La retta p è perpendicolare al quadro: la parallela a p per O è OO₀, quindi la fuga di p è O₀.

### Le rette perpendicolari al quadro vanno in O₀

Se la retta è perpendicolare al piano di quadro, la parallela per O è proprio la perpendicolare OO₀. Quindi le rette perpendicolari al quadro hanno tutte la fuga in O₀.

È la prospettiva che si faceva alle elementari e alle medie, la prospettiva centrale: i lati della stanza perpendicolari al quadro vanno tutti nel centro, cioè in O₀.

### Le rette parallele al quadro

Se la retta è parallela al quadro, la sua parallela per O non incontra mai il quadro: la fuga è all'infinito.

Allora una retta parallela al quadro si proietta in una retta parallela a se stessa. Se sta sul geometrale, la sua prospettiva è parallela alla fondamentale e all'orizzonte.

### Le rette a 45°: i punti di distanza

Una retta del geometrale che forma 45 gradi con il quadro ha la fuga in un punto preciso.

La sua parallela per O forma 45° con il quadro. Nel triangolo rettangolo O O₀ F, con l'angolo di 45° in O, i due cateti sono uguali: la fuga dista da O₀ esattamente d. Quindi la fuga è sull'orizzonte, nel punto in cui il cerchio di distanza incontra l'orizzonte.

I punti in cui il cerchio di distanza incontra l'orizzonte sono due:

- il punto di distanza a destra, D_d, fuga delle rette a 45° che vanno verso destra;
- il punto di distanza a sinistra, Dₛ, fuga delle rette a 45° che vanno verso sinistra.

Le due rette per O che vanno nei punti di distanza formano tra loro un angolo di 90°, ciascuna a 45° rispetto alla perpendicolare OO₀.

Per disegnare una retta a 45° si fa come per ogni retta:

1. per la fuga si manda la retta per O: arriva sul cerchio di distanza, nel punto di distanza;
2. per la traccia si prolunga la retta in pianta fino al quadro e la si porta sulla fondamentale;
3. si congiungono traccia e fuga.

## IL METODO DELLA PIANTA

### I punti appoggiati al quadro

Nell'esercizio della lezione la figura è appoggiata sul geometrale e due suoi punti, A e B, sono attaccati al piano di quadro.

Un punto che sta sia sul geometrale sia sul quadro sta sulla loro retta comune, la fondamentale. Quindi A′ e B′ si trovano scendendo con una verticale dalla pianta fino alla fondamentale.

Un punto appoggiato al quadro è la traccia di tutte le rette del geometrale che passano per lui.

### Il punto in prospettiva: il raggio e il piano proiettante visti dall'alto

La retta r del lato BC è perpendicolare al quadro. La sua traccia è B, quindi B′ coincide con la traccia Tᵣ′; la sua fuga è O₀. La retta r′ è la retta B′O₀.

Su r si trova il punto C. Per trovare C′ si ragiona nello spazio:

1. Il punto C si proietta da O: il raggio proiettante OC buca il quadro in C′.
2. Per sapere a che altezza il raggio buca il quadro, si costruisce il piano proiettante: il piano verticale che contiene il raggio OC.
3. Il piano proiettante taglia il quadro lungo una retta verticale. C′ sta su questa retta.

Guardato dall'alto, cioè in pianta:

- il raggio proiettante OC si vede come la retta da O a C;
- il piano proiettante si vede come la stessa retta, perché è verticale;
- la retta verticale in cui il piano proiettante taglia il quadro si vede solo come un punto, dove il raggio incontra la linea del quadro.

Quindi da quel punto si scende con una verticale (alla lavagna è rossa) nel disegno sul quadro. Dove la verticale incontra r′ c'è C′. La retta rossa è portata dal disegno in pianta al quadro.

> [!example] Disegno 4 · Il disegno alla lavagna: A, B sul quadro, la retta perpendicolare r e il punto C
> ![[13-prospettiva-metodo-pianta-retta-perpendicolare.svg|620]]
>
> 1. La linea del quadro in pianta coincide con l'orizzonte, quindi O coincide con O*: è solo una comodità.
> 2. A e B stanno sul quadro e sul geometrale: A′ e B′ sono sulla fondamentale, in verticale sotto la pianta.
> 3. La retta r (lato BC) è perpendicolare al quadro: traccia B′ ≡ Tᵣ′, fuga O₀. r′ è la retta B′O₀.
> 4. In pianta si traccia il raggio OC; dove incontra la linea del quadro si scende con la verticale rossa. Dove la verticale incontra r′ c'è C′.

Per la retta n, parallela al quadro, la prospettiva n′ è parallela alla fondamentale e all'orizzonte; il suo punto si trova con lo stesso ragionamento fatto per C.

### Il controllo con la retta a 45°

Se la figura è un quadrato appoggiato al quadro con il lato AB, la diagonale AC forma 45° con il quadro.

La sua fuga è il punto di distanza a destra, la sua traccia è A′. Se il disegno è fatto bene, la retta A′D_d passa per il punto C′ trovato prima con il raggio proiettante. È un controllo utile.

Quando si cerca un punto come intersezione di due rette (per esempio un punto che sta su n′ e su s′), basta disegnare le due rette, ognuna con la sua traccia e la sua fuga: il punto è dove si incontrano.

> [!example] Disegno 5 · Il disegno alla lavagna: la retta a 45° e il punto di distanza
> ![[13-prospettiva-retta-a-45-punto-di-distanza.svg|620]]
>
> 1. La diagonale s forma 45° con il quadro: la parallela per O arriva sull'orizzonte nel punto di distanza a destra D_d.
> 2. La traccia di s è A, quindi Tₛ′ ≡ A′.
> 3. s′ è la retta A′D_d e passa per C′, trovato con il raggio proiettante (s′ e r′ si incontrano in C′).

### Le rette inclinate in un angolo qualsiasi

Nell'esercizio della lezione c'è anche un lato, AE, inclinato rispetto al quadro di un angolo qualsiasi. Per conoscerne la fuga si costruisce la parallela al lato AE passante per O, in pianta, e si guarda dove incontra la linea del quadro: lì, sull'orizzonte, c'è la fuga.

È la regola generale; le rette perpendicolari al quadro (fuga in O₀) e quelle a 45° (fuga nei punti di distanza) sono solo i casi in cui la fuga cade in un punto già noto.

## ESERCIZIO-TIPO RISOLTO

> [!example] Esercizio · La prospettiva della pianta di un rettangolo con il metodo della pianta
> Il rettangolo ABCD sta sul geometrale. Il vertice A è appoggiato al quadro; il lato AB forma 35° con il quadro ed è lungo 7,5 cm, il lato AD è lungo 4,5 cm. Il punto di vista è a 8,5 cm dal quadro, l'occhio a 4,5 cm da terra. Disegna la prospettiva di ABCD con il metodo della pianta.
>
> ![[b13-esercizio-rettangolo-metodo-della-pianta.svg|620]]

> [!success]- Soluzione
> Risultato: la prospettiva è il quadrilatero A′B′C′D′ del disegno. A′ sta sulla fondamentale; i lati A′B′ e D′C′ vanno verso Fᵣ, i lati A′D′ e B′C′ verso Fₙ; Fᵣ e Fₙ stanno sull'orizzonte e, uniti con O, formano un angolo retto.
>
> Come si arriva:
> 1. Si traccia l'orizzonte, che è anche la linea del quadro in pianta, e la fondamentale 4,5 cm sotto. Si segna O₀ e, 8,5 cm sotto, O ≡ O*. Perché: la distanza tra orizzonte e fondamentale è l'altezza dell'occhio; O e O* coincidono per comodità.
> 2. Sopra l'orizzonte si disegna la pianta, con A sulla linea del quadro. Perché: A è appoggiato al quadro.
> 3. Da A si scende in verticale sulla fondamentale: A′. Perché: A sta sul quadro e sul geometrale, quindi sulla fondamentale. A′ è la traccia sia di r (retta di AB) sia di n (retta di AD).
> 4. Da O si conduce la parallela a r: dove incontra l'orizzonte c'è Fᵣ. Da O la parallela a n: Fₙ. Perché: la fuga di una retta è dove arriva la sua parallela per O; le rette del geometrale hanno la fuga sull'orizzonte. Le due parallele formano un angolo retto, come AB e AD.
> 5. Si tracciano r′ = A′Fᵣ e n′ = A′Fₙ. Perché: la prospettiva di una retta congiunge traccia e fuga.
> 6. In pianta si traccia il raggio proiettante OB; dove incontra la linea del quadro si scende in verticale fino a r′: lì c'è B′. Lo stesso con il raggio OD fino a n′: D′. Perché: la verticale è la retta in cui il piano proiettante taglia il quadro.
> 7. Si unisce B′ con Fₙ e D′ con Fᵣ: dove si incontrano c'è C′. Perché: BC è parallelo a AD e DC a AB, e rette parallele hanno la stessa fuga.
> 8. Controllo: il raggio OC, portato giù in verticale, passa per C′.

## ERRORI DA EVITARE

Le avvertenze della docente in questa lezione:

- far coincidere O e O* (cioè la linea del quadro in pianta con l'orizzonte) è solo una comodità, non una regola geometrica: si può anche mettere la pianta più in basso;
- la fondamentale va messa almeno un paio di centimetri sotto l'orizzonte, per vedere che cosa succede dentro;
- le tracce vanno sulla fondamentale e le fughe sull'orizzonte (per le rette del geometrale): non vanno confuse;
- la fuga si trova sempre con la parallela per O, non «a occhio»;
- un punto non si trova con il solo raggio proiettante: serve anche la retta su cui sta (qui r′), e la verticale del piano proiettante dice dove fermarsi;
- le domande si fanno alla lavagna, a voce alta, non al vicino: così la risposta serve a tutti.

## Collegamenti

La prospettiva è la proiezione dal centro proprio introdotta nella [[02-proiezioni-e-omologia-schema|seconda lezione]], dove si è visto che ogni metodo di rappresentazione nasce da un centro e da raggi proiettanti, e che proiettando da un centro una figura su un piano si ottiene una prospettività. La notazione con l'apice, A′, è quella che la docente riserva all'omologia e alla prospettiva, come detto nella bozza sulle [[03-proiezioni-ortogonali-punto-e-rette|proiezioni ortogonali]].

La traccia di una retta sul quadro ha lo stesso significato delle tracce delle rette nel metodo di Monge: il punto in cui la retta buca il piano di proiezione. Il cerchio di distanza e O* nascono da un ribaltamento, quello del piano d'orizzonte intorno all'orizzonte, con la stessa logica dei [[07-il-ribaltamento|ribaltamenti dei piani proiettanti]]. Il confronto con l'[[12-errori-della-prova-1-e-quadro-verticale|assonometria con il quadro verticale]] è istruttivo: là le parallele restano parallele, qui concorrono nella fuga.

Il metodo continua con le altezze e il punto di misura nella bozza [[14-altezze-e-punto-di-misura-in-prospettiva]] e con la [[16-la-prospettiva-a-occhio-di-formica|prospettiva a occhio di formica]]. Nelle tavole d'esame le prospettive della casa partono proprio dalle piante: per Villa Tugendhat vedi il piano di lavoro in [[studio-villa-tugendhat]], che prevede prospettive dal giardino verso la casa.

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale). Nessun file del materiale è dedicato alla prospettiva: la bozza viene dalla lezione.

- [[tavole-anno-scorso-02.jpeg]]: tavola di uno studente dell'anno scorso su Villa Savoye, con prospettive costruite con fughe e cerchio di distanza
- [[tavole-anno-scorso-03.jpeg]]: tavola sul Padiglione di Barcellona, con più prospettive della stessa pianta
- [[566_3.pdf]]: il libro della docente non tratta la prospettiva (annuncia un secondo volume); è utile solo per il ripasso dei ribaltamenti
