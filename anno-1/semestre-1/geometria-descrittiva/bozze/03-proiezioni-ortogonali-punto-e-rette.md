---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-08
tags: [geometria-descrittiva, bozza]
---

# Dall'omologia alle proiezioni ortogonali: il punto e le rette proiettanti

> [!info] Note collegate
> Sbobina: [[03-proiettiva-e-proiezioni-ortogonali]]
>
> Bozza precedente: [[02-proiezioni-e-omologia-schema]] · Successiva: [[04-rette-e-piani-nelle-varie-posizioni]]

La lezione di giovedì 8 ottobre fa da ponte tra le due parti iniziali del corso. Nella prima parte si riprendono i fondamenti della geometria proiettiva e l'omologia, con l'esercizio guidato sulle omologie da svolgere a casa; nella seconda si entra nel primo metodo di rappresentazione vero e proprio, le proiezioni ortogonali. Si parte dalla posizione del centro di proiezione, si passa per la pianta, i prospetti e le scale, e si arriva a rappresentare il punto con le sue tre proiezioni e le prime due rette particolari, la retta proiettante in prima e la retta proiettante in seconda. Il filo che lega tutto è lo stesso: ogni segno sul foglio è il risultato di un'operazione di proiezione e sezione avvenuta nello spazio.

## DALLA GEOMETRIA PROIETTIVA ALL'OMOLOGIA

### Il processo proiettivo e gli enti impropri

Il processo proiettivo è un insieme di operazioni in cui compaiono sempre tre elementi: un centro di proiezione, un oggetto e un piano di quadro su cui l'oggetto viene proiettato. È così in tutti i metodi di rappresentazione, che sono diversi aspetti dello stesso processo; il caso più semplice è la prospettiva, cioè la fotografia. La geometria proiettiva studia le proprietà delle figure che restano invariate durante le operazioni di proiezione e sezione: alcune cose cambiano tra l'oggetto e la sua immagine, ma l'appartenenza, l'allineamento e l'incidenza si conservano. Sembrano ovvietà, ma sono la struttura di ogni rappresentazione e la chiave per risolvere gli esercizi.

Il punto improprio di una retta non si vede: se ne intuisce l'esistenza. Se si costruiscono i raggi proiettanti per tutti i punti di una retta, anche quando il raggio diventa parallelo alla retta si ottiene un'immagine sul piano di quadro; se esiste un'immagine, esiste il punto che l'ha generata, e quel punto sta all'infinito. Per questo una retta passa per due punti propri, ma anche per un punto proprio e un punto improprio, che le dà la direzione. Lo stesso vale per i piani, e restano validi tutti e sei i postulati, i tre di appartenenza e i loro duali.

### Dalla prospettività all'omologia

La proiettività più semplice è la prospettività: un centro e due piani, con una corrispondenza biunivoca che a ogni punto di un piano associa un solo punto dell'altro (omografia). Di questa corrispondenza l'omologia conserva due fatti. I punti corrispondenti sono allineati con il centro, perché l'immagine $A'$ è prodotta da un raggio che parte da $S$ e passa per $A$. Le rette corrispondenti $r$ e $r'$ si incontrano sull'asse, che è la retta di intersezione tra il piano della figura e il piano su cui la si proietta; il punto in cui si incontrano si chiama punto unito, perché appartiene a tutti e due i piani e proiettandolo resta dov'è.

Per portare queste relazioni sul foglio, secondo Desargues, basta considerare le due figure corrispondenti come le proiezioni di una stessa figura, appartenente a un altro piano (un piano verticale $\alpha_0$), da due centri di proiezione diversi, $S$ ed $S_1$. Proiettando un centro dall'altro si ottiene un unico punto sul piano, il centro $U$. Questa relazione, prodotto di due prospettività, si chiama omologia. Le convenzioni contano: il centro è un punto e si scrive con la maiuscola $U$; l'asse è una retta e si scrive con la minuscola $u$.

> [!abstract] Da ricordare
> - I punti corrispondenti sono allineati con il centro $U$.
> - Le rette corrispondenti si incontrano sull'asse $u$, nel punto unito.
> - L'asse è sempre la retta di intersezione tra i piani che si stanno considerando.
> - Queste due proprietà, più le condizioni di appartenenza, bastano per risolvere tutti gli esercizi: non serve figurarsi lo spazio.

> [!example] Il disegno: trovare il corrispondente di un punto
> ![[03-omologia-punto-corrispondente.svg|620]]
>
> Dati $U$, $u$, le rette corrispondenti $r$ e $r'$ (che si incontrano sull'asse nel punto unito $V$) e un punto $P$, si cerca $P'$.
> 1. Si sceglie un punto $A$ su $r$ e si traccia il raggio da $U$ per $A$: dove incontra $r'$ c'è $A'$.
> 2. Si traccia la retta $s$ per $A$ e $P$ e la si prolunga fino all'asse: lì c'è il suo punto unito $W$.
> 3. La corrispondente $s'$ passa per $W$ e per $A'$.
> 4. Il raggio da $U$ per $P$ incontra $s'$ in $P'$.

### Le omologie particolari

A seconda della posizione dei piani e dei centri, l'omologia prende nomi diversi, che conviene ricordare perché aiutano a distinguere i casi; la soluzione degli esercizi però resta sempre la stessa. L'omologia è speciale quando il centro giace sull'asse. È un'affinità quando la retta che unisce i due centri è parallela al piano: il centro va all'infinito ($U_\infty$) e se ne disegna solo la direzione, con una lineetta che non è casuale; l'affinità è ortogonale se la direzione è perpendicolare all'asse, obliqua se è inclinata. È un'omotetia quando il piano della figura e il piano di proiezione sono paralleli: allora è l'asse a essere improprio ($u_\infty$, segnato con una crocetta), e le rette corrispondenti, incontrandosi all'infinito, sono parallele; la figura risulta ingrandita. Se infine anche i centri sono allineati parallelamente al piano, si ha una traslazione, un'isometria che conserva distanze e angoli ($A'B' = AB$). La bozza [[02-proiezioni-e-omologia-schema]] riprende tutti questi casi in forma di schema.

> [!example] Il disegno: affinità ortogonale e obliqua
> ![[03-affinita-ortogonale-obliqua.svg|620]]
>
> 1. Il centro è improprio: si scrive $U_\infty$ e si disegna solo la sua direzione.
> 2. Le rette che uniscono i punti corrispondenti sono tutte parallele a quella direzione.
> 3. Direzione perpendicolare all'asse $u$: affinità ortogonale; direzione inclinata: affinità obliqua.

### L'esercizio guidato sulle omologie

Il foglio dell'esercizio guidato (`ES.GUIDATA_Omologia_01.pdf`) raccoglie sei esercizi, uno per ogni situazione vista a lezione, da stampare e svolgere a casa; la correzione è avvenuta nella lezione del 13 ottobre. Riconoscere il tipo di omologia dai dati è il primo passo, e i dati si leggono proprio dalle convenzioni: un centro con la lineetta è improprio, un asse con la crocetta è all'infinito.

> [!example] Il disegno: i sei esercizi del foglio, riconosciuti dai dati
> 1. Dati $r$ e $r'$ parallele, $U_\infty$ e $u_\infty$, trovare $A'B'C'$ del triangolo $ABC$: centro e asse impropri, è una traslazione.
> 2. Dati $r$, $r'$, asse $u$ e centro $U$ che sta sull'asse, trovare $M'$: omologia speciale.
> 3. Dati $r$, $r'$ che si incontrano sull'asse, $u$ e $U$ proprio, trovare $M'$: omologia generica.
> 4. Dati $r$ e $r'$ parallele, $U$ proprio e $u_\infty$, trovare la retta $s'$ corrispondente di $s$: omotetia.
> 5. Data la coppia di punti corrispondenti $A$ e $A'$ (allineati con $U$), trovare la figura $A'B'C'D'$ di $ABCD$: si parte dalle rette per $A$ (lati $AB$ e $AD$) e dai loro punti uniti.
> 6. Dati $r$, $r'$, l'asse $u$ e $U_\infty$, trovare la figura corrispondente di $\mathscr{L}$: affinità.
>
> In tutti si applica la stessa regola: se si hanno i punti si cercano le rette, se si hanno le rette si cercano i punti.

## LE PROIEZIONI ORTOGONALI

### Centro proprio e centro improprio

Il centro di proiezione può essere proprio, cioè a distanza finita: da esso parte una stella di rette, i raggi proiettanti che portano la figura sul piano. È il caso del fascio di luce che proietta un rettangolo parallelo alla parete: il rettangolo si ingrandisce, ed è un'omotetia, con asse all'infinito e centro proprio. Se invece il centro è all'infinito si ha soltanto una direzione e tutti i raggi sono paralleli tra loro, come i raggi del sole nella costruzione delle ombre (mentre una lampada, centro proprio, dà ombre diverse). Con il centro proprio si hanno le proiezioni centrali e la prospettiva; con il centro improprio le proiezioni cilindriche, tra cui le proiezioni ortogonali, in cui la figura viene come traslata sul piano di quadro, nelle stesse dimensioni.

> [!example] Il disegno: proiezione centrale e proiezione cilindrica
> ![[03-proiezione-centrale-e-cilindrica.svg|620]]
>
> 1. A sinistra il centro $S$ è proprio: i raggi partono tutti da $S$ e il rettangolo $ABCD$, parallelo al piano di quadro, arriva ingrandito.
> 2. A destra il centro è improprio ($S_\infty$): i raggi sono paralleli e la figura arriva con le stesse dimensioni.
> 3. Se i raggi sono anche perpendicolari al piano di quadro si hanno le proiezioni ortogonali.

Nelle proiezioni ortogonali i centri di proiezione sono tre, tutti all'infinito, ciascuno in direzione perpendicolare a uno dei piani di proiezione: una direzione è perpendicolare al piano verticale, una al piano orizzontale. I piani su cui si proietta l'immagine sono paralleli, quindi è come se si facesse una traslazione: se in partenza c'è un rettangolo, lo si ritrova anche una volta proiettato. Monge lavora principalmente con il triedro, e i suoi esercizi si svolgono soprattutto su due proiezioni.

### Pianta, sezione e prospetti

La pianta è una sezione orizzontale, ottenuta con un piano parallelo al piano orizzontale di proiezione. La quota a cui si taglia l'edificio non è indifferente: deve intercettare le finestre e comprendere tutti gli elementi che compongono l'edificio, altrimenti la pianta mostrerebbe uno spazio completamente chiuso. La sezione verticale passa invece per due punti precisi della pianta, taglia i muri trasversalmente ed è perpendicolare al piano orizzontale; non è mai parallela al piano orizzontale, altrimenti diventerebbe una pianta.

Una pianta da sola non basta a dare l'idea della forma: per stabilire i volumi dell'oggetto si devono disegnare anche i prospetti, cioè le proiezioni ortogonali fatte sui piani di un triedro. Davanti a una pianta bisogna immaginarne il volume, come se ci si camminasse intorno: il prospetto è ciò che si vede guardando l'edificio da fuori, da uno dei suoi lati.

### Da che parte si guarda: il prospetto disegnato al contrario

L'errore più frequente, che si trascina anche fino alla fine del corso, riguarda la posizione della linea di terra. Per disegnare il prospetto del lato che in pianta sta in alto, viene istintivo mettere la linea di terra subito sopra la pianta, tirare su le linee e disegnare il prospetto in piedi. Così però il prospetto viene specchiato: si sta guardando l'edificio da dentro, e una rientranza che chi guarda vede a destra finisce a sinistra. Il prospetto si guarda sempre da fuori; solo la sezione permette di guardare da dentro. Per questo la linea di terra va in alto, e il prospetto si disegna a testa in giù. È come la mano: per vedere il dorso bisogna guardare dalla parte del dorso, non del palmo.

> [!example] Il disegno: il prospetto giusto e quello sbagliato
> ![[03-prospetto-giusto-e-sbagliato.svg|660]]
>
> La forma dell'edificio è uno schema: conta solo la rientranza.
> 1. Dagli spigoli del lato in alto della pianta si tirano le linee di proiezione.
> 2. Giusto: la LT sta in alto, lontana dalla pianta, e il prospetto parte dalla LT e scende verso la pianta, a testa in giù. Girando il foglio, come chi guarda quel lato, la rientranza è a destra.
> 3. Sbagliato: la LT sta subito sopra la pianta e il prospetto è in piedi; la rientranza finisce dalla parte sbagliata.

> [!abstract] Da ricordare
> - Pianta = sezione orizzontale, a una quota che taglia le finestre.
> - Prospetto = proiezione ortogonale di un lato, visto da fuori.
> - La LT si mette dalla parte da cui si guarda il lato da rappresentare: per il lato in alto, LT in alto e prospetto a testa in giù.

### Le scale di rappresentazione

Si lavora sempre in scala. Le scale possono essere di ingrandimento o di riduzione, e in architettura si usano soprattutto quelle di riduzione. La più semplice è la 1:100, in cui 1 metro reale diventa 1 centimetro sul foglio: un muro spesso 50 cm si disegna spesso 5 mm. In 1:200 un metro diventa mezzo centimetro e le misure si dimezzano (lo stesso muro è spesso 2,5 mm); in 1:50 un metro diventa 2 centimetri e le misure raddoppiano (il muro è spesso 1 cm). La tabella delle scale fornita dalla docente (`004b_scale di rappresentazione.jpg`) va dagli ingrandimenti (10:1, 5:1, 2:1) alla scala di riproduzione 1:1, fino alle riduzioni dei disegni di architettura e delle carte del territorio (fino a 1:1.000.000). La scala grafica è fondamentale: è la testimonianza delle dimensioni delle cose e permette di risalire dalle misure del disegno a quelle reali anche dopo vari passaggi.

> [!example] Il disegno: lo stesso muro in tre scale e la scala grafica
> ![[03-scale-di-rappresentazione.svg|620]]
>
> 1. Si disegna lo stesso muro di 50 cm in 1:50, 1:100 e 1:200: lo spessore passa da 1 cm a 5 mm a 2,5 mm.
> 2. Si costruisce la scala grafica: una barra a tratti alterni bianchi e neri, ognuno dei quali vale 1 metro; in 1:100 ogni tratto è lungo 1 cm, in 1:200 è lungo 0,5 cm.

> [!abstract] Da ricordare
> - 1:100 → 1 m = 1 cm · 1:200 → 1 m = 0,5 cm · 1:50 → 1 m = 2 cm
> - Muro di 50 cm: 1 cm in 1:50, 5 mm in 1:100, 2,5 mm in 1:200.
> - La scala grafica va sempre disegnata accanto al disegno.

## IL PUNTO NEL TRIEDRO

### I tre piani di proiezione e i pedici

Per rappresentare un punto nello spazio bisogna prima definire una porzione di spazio, cioè costruire un diedro o un triedro. I piani di proiezione si chiamano con la lettera greca $\pi$, perché i piani si indicano con le minuscole dell'alfabeto greco: $\pi_1$ è il piano orizzontale, $\pi_2$ il piano verticale (quello di uno dei prospetti), $\pi_3$ il terzo piano, verticale anch'esso, di lato. Il punto si rappresenta mediante le sue tre proiezioni, e nelle proiezioni ortogonali si scrivono con il pedice: $P_1$, $P_2$, $P_3$. L'apice resta all'omologia e alla prospettiva ($P'$), e tornerà nell'assonometria accanto al pedice ($P'_1$, $P'_2$, $P'_3$).

> [!abstract] Da ricordare: la notazione
> - $P'$ → omologia e prospettiva.
> - $P_1$, $P_2$, $P_3$ → proiezioni ortogonali (prima, seconda, terza proiezione); lo stesso per le rette: $r_1$, $r_2$, $r_3$.
> - $P'_1$, $P'_2$, ... → assonometria.
> - Tracce della retta: $T_{1r}$, $T_{2r}$, $T_{3r}$ (dove la retta buca $\pi_1$, $\pi_2$, $\pi_3$).
> - Piani: lettere greche minuscole ($\pi_1$, $\pi_2$, $\pi_3$).

### Dallo spazio al foglio: il ribaltamento dei piani

Il modello del triedro che si costruisce in classe è rigido, con i piani in piedi. Per avere tutte le proiezioni su un unico foglio si ruota il terzo piano di proiezione sul secondo, poi si ruota il primo: i due piani verticali si sovrappongono, il piano orizzontale si ribalta, e le tre proiezioni del punto si ritrovano disegnate su un solo piano. Per questo si scrive $\pi_1 \equiv \pi_2 \equiv \pi_3$: dopo le rotazioni i tre piani coincidono. Le proiezioni restano legate da due rette: la linea di terra, che è la retta orizzontale di intersezione tra i piani, e la linea verticale, che rappresenta l'altra intersezione, quella tra i due piani verticali.

> [!example] Disegno proposto (non fatto a lezione): come i tre piani finiscono sul foglio
> ![[b03-ribaltamento-dei-piani.svg|660]]
>
> La docente lo ha mostrato con il modello di cartoncino; lo schema serve a ricordare il movimento.
> 1. $\pi_3$ ruota attorno allo spigolo verticale che ha in comune con $\pi_2$ e si mette accanto a $\pi_2$ (freccia blu).
> 2. $\pi_1$ ruota attorno alla LT e scende sotto $\pi_2$ (freccia verde).
> 3. Sul foglio: $\pi_2$ in alto a sinistra, $\pi_3$ in alto a destra della linea verticale, $\pi_1$ sotto la LT.

### Aggetto, quota e linea di richiamo

Il punto $P$ si proietta perpendicolarmente su ciascun piano. La sua prima proiezione $P_1$ sta sotto la linea di terra, a una distanza che è l'aggetto: la distanza del punto dal piano verticale, come la sporgenza di un balcone, cioè la distanza tra la ringhiera e la facciata. La seconda proiezione $P_2$ sta sopra la linea di terra, a un'altezza che è la quota, la distanza del punto dal piano orizzontale. $P_1$ e $P_2$ non si possono mettere dove si vuole: devono stare sulla stessa linea di richiamo, la linea di costruzione perpendicolare alla LT che le collega. Con aggetto e quota si sa già dove si trova il punto nello spazio.

> [!example] Il disegno: il punto nel triedro
> ![[03-punto-nel-triedro.svg|620]]
>
> 1. Si disegnano i tre piani: $\pi_1$ orizzontale, $\pi_2$ verticale di fronte, $\pi_3$ verticale di lato; la LT è l'intersezione tra $\pi_1$ e $\pi_2$.
> 2. Dal punto $P$ si mandano le perpendicolari ai tre piani: dove li incontrano ci sono $P_1$, $P_2$ e $P_3$.
> 3. Il segmento tra $P$ e $\pi_2$ è l'aggetto (arancione); quello tra $P$ e $\pi_1$ è la quota (verde).

### La terza proiezione

La terza proiezione si ottiene proiettando il punto sul terzo piano, che nello spazio sta di lato, e costruendo sempre la linea di richiamo. Ciò che si trova su $\pi_3$ non è il punto ma la sua immagine; ribaltando il piano, la si riporta sul foglio. In questa operazione la quota non cambia: il punto non può né salire né scendere.

> [!example] Il disegno: le tre proiezioni del punto sul foglio
> ![[03-tre-proiezioni-del-punto.svg|620]]
>
> 1. Si traccia la LT orizzontale e la linea verticale.
> 2. Si segna $P_2$ sopra la LT, a un'altezza pari alla quota, e $P_1$ sotto la LT, a una distanza pari all'aggetto, sulla stessa linea di richiamo.
> 3. Da $P_1$ si va in orizzontale fino alla linea verticale; con il compasso puntato nell'incrocio tra LT e linea verticale si gira l'arco fino alla LT, e da lì si sale in verticale.
> 4. Da $P_2$ si tira l'orizzontale: dove incontra la verticale appena tracciata c'è $P_3$.

> [!abstract] Da ricordare
> - $P_1$ e $P_2$ stanno sulla stessa linea di richiamo, perpendicolare alla LT.
> - Distanza di $P_2$ dalla LT = quota; distanza di $P_1$ dalla LT = aggetto.
> - $P_3$ ha la stessa quota di $P_2$; la sua distanza dalla linea verticale è l'aggetto, riportato con l'arco.

## LE RETTE PROIETTANTI

### Perché si chiamano proiettanti

Le prime rette particolari sono quelle perpendicolari a uno dei primi due piani di proiezione. Si chiamano proiettanti perché hanno la stessa direzione dei raggi proiettanti: il centro di proiezione all'infinito è perpendicolare al piano, e la retta è parallela a quei raggi. Ricordando che i piani sono tre e i centri di proiezione tre, all'infinito e perpendicolari ai tre piani, il nome della retta dipende dalla posizione che assume rispetto ai primi due piani, $\pi_1$ orizzontale e $\pi_2$ verticale. Di ogni retta si cercano le proiezioni e le tracce, cioè i punti in cui la retta buca i piani di proiezione; una retta parallela a un piano non lo incontra mai, e la traccia su quel piano è all'infinito.

### La retta proiettante in prima

La retta $r$ proiettante in prima è perpendicolare a $\pi_1$, cioè verticale. Vista dall'alto si riduce a un punto, in cui coincidono la prima proiezione della retta, la sua prima traccia e la prima proiezione di ogni suo punto: $r_1 \equiv T_{1r} \equiv P_1$. La seconda e la terza proiezione sono verticali; la retta è parallela sia a $\pi_2$ sia a $\pi_3$, quindi la seconda e la terza traccia sono all'infinito.

> [!example] Il disegno: la retta proiettante in prima sul foglio
> ![[03-retta-proiettante-in-prima.svg|620]]
>
> 1. Si segna sotto la LT il punto $r_1 \equiv T_{1r} \equiv P_1$, alla distanza dell'aggetto.
> 2. Dalla linea di richiamo si traccia $r_2$: parte dalla LT ed è perpendicolare alla LT; si scrive $T_{2r}\infty$.
> 3. Da $r_1$ si va in orizzontale alla linea verticale, si gira l'arco e si traccia $r_3$, verticale, a distanza pari all'aggetto; si scrive $T_{3r}\infty$.
> 4. Un punto $P$ della retta ha $P_2$ su $r_2$ e $P_3$ su $r_3$, alla stessa quota.

> [!example] Disegno proposto (non fatto a lezione): la retta proiettante in prima nello spazio
> ![[b03-spazio-retta-proiettante-in-prima.svg|560]]
>
> 1. La retta $r$ sale verticale da $\pi_1$: il punto in cui lo buca è $T_{1r}$, e lì si schiaccia tutta la prima proiezione.
> 2. Proiettata su $\pi_2$ dà $r_2$, verticale; proiettata su $\pi_3$ dà $r_3$, verticale anch'essa.
> 3. Il punto $P$ di $r$ ha le proiezioni $P_2$ e $P_3$ alla stessa quota, e $P_1$ coincide con $T_{1r}$.

### La retta proiettante in seconda

La retta $m$ proiettante in seconda è perpendicolare a $\pi_2$. La sua traccia nota è la seconda, $T_{2m}$, il punto in cui la retta incontra il piano verticale; vista di fronte la retta si riduce a quel punto, quindi la seconda proiezione coincide con la seconda traccia: $m_2 \equiv T_{2m}$. Dalla seconda proiezione si scende con la linea di richiamo e si disegna la prima proiezione $m_1$; la prima traccia è all'infinito. Poi la terza proiezione $m_3$, e anche la terza traccia è all'infinito. Le proiezioni non sono tratteggiate, ma continue: non bisogna farsi confondere, bisogna ragionare.

> [!example] Il disegno: la retta proiettante in seconda nello spazio
> ![[03-spazio-retta-proiettante-in-seconda.svg|560]]
>
> 1. La retta $m$ esce perpendicolare da $\pi_2$: il punto in cui lo buca è $T_{2m}$, e lì sta tutta la seconda proiezione ($m_2 \equiv T_{2m}$).
> 2. Proiettata su $\pi_1$ dà $m_1$, perpendicolare alla LT; proiettata su $\pi_3$ dà $m_3$, orizzontale.
> 3. $m$ è parallela a $\pi_1$ e a $\pi_3$: $T_{1m}$ e $T_{3m}$ sono all'infinito.

> [!example] Il disegno: la retta proiettante in seconda sul foglio
> ![[03-retta-proiettante-in-seconda.svg|620]]
>
> 1. Si segna sopra la LT il punto $m_2 \equiv T_{2m}$, alla sua quota.
> 2. Si scende con la linea di richiamo: $m_1$ parte dalla LT ed è perpendicolare alla LT (si segna l'angolo retto); si scrive $T_{1m}\infty$.
> 3. Da $m_2$ si tira l'orizzontale: dalla linea verticale in poi è $m_3$, alla stessa quota; si scrive $T_{3m}\infty$.
> 4. Tutte le proiezioni della retta si disegnano a tratto continuo.

> [!abstract] Da ricordare: le due rette proiettanti
> - Proiettante in prima ($r \perp \pi_1$): $r_1 \equiv T_{1r} \equiv P_1$ è un punto; $r_2$ e $r_3$ perpendicolari alla LT; $T_{2r}\infty$, $T_{3r}\infty$.
> - Proiettante in seconda ($m \perp \pi_2$): $m_2 \equiv T_{2m}$ è un punto; $m_1$ perpendicolare alla LT; $m_3$ parallela alla LT; $T_{1m}\infty$, $T_{3m}\infty$.
> - La traccia nota è sempre quella sul piano a cui la retta è perpendicolare; le altre due sono all'infinito.

> [!tip] Da fare
> - Stampare il foglio dell'esercizio guidato sulle omologie (`ES.GUIDATA_Omologia_01.pdf`) e svolgere i sei esercizi a casa; la correzione è stata fatta martedì 13 ottobre.
> - Prima della lezione sulla rappresentazione della retta: disegnare e tagliare il modello del triedro (i tre piani di proiezione), tagliando sulla copertina rigida del blocco e non sul tavolo.

## Collegamenti

La prima parte della lezione chiude il discorso sulla geometria proiettiva iniziato nella [[02-proiezioni-e-omologia-schema|lezione sull'omologia]]: le due proprietà dell'omologia e le condizioni di appartenenza resteranno lo strumento per risolvere tutti gli esercizi, e torneranno nell'omologia di ribaltamento, con cui [[07-il-ribaltamento|si ribaltano le figure dei piani proiettanti]]. La seconda parte apre il metodo di Monge: il punto con le sue tre proiezioni e le due rette proiettanti sono il primo passo verso [[04-rette-e-piani-nelle-varie-posizioni|le rette e i piani nelle varie posizioni]], le [[05-appartenenza-e-rette-ausiliarie|condizioni di appartenenza]] e i [[06-piani-ausiliari-e-perpendicolarita|piani ausiliari]]. Le regole del disegno viste nella [[01-strumenti-materiali-e-regole|prima lezione]], come lasciare visibili le linee di richiamo e distinguere il segno delle costruzioni da quello del risultato, trovano qui la prima applicazione. Pianta, prospetti e scale, infine, sono gli stessi strumenti con cui si lavora nel laboratorio di Composizione architettonica.
