---
tipo: sbobina
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-06
tags: [geometria-descrittiva, sbobina]
---

# Geometria descrittiva — Lezione del 6 ottobre

> Trascrizione sistemata della registrazione (due parti dello stesso incontro). Il contenuto è fedele alle parole del professore: sono stati corretti gli errori di trascrizione e la terminologia tecnica, e tolte le parti fuori tema. La lezione si divide in una prima parte di ripasso (distanze, parallelismo, postulati, convenzioni) e in una seconda parte vera e propria sulla geometria proiettiva e l'omologia.

> [!info] Note collegate
> Bozza: [[proiezioni-e-omologia]]
>
> Sbobina precedente: [[01-strumenti-e-disegno]] · Successiva: [[06-piani-proiettanti-orizzontali-frontali]]

---

## La distanza di un punto da una retta

Data una retta $r$ e un punto $P$ che non appartiene alla retta, la distanza del punto dalla retta è il segmento che ha per estremi il punto $P$ e il piede della perpendicolare condotta da $P$ alla retta $r$. Il piede della perpendicolare è semplicemente il punto in cui la perpendicolare incontra la retta.

Si parla di distanza minima perché si potrebbero misurare anche altre distanze inclinate — tracciando segmenti che formano con la retta angoli di 30°, 40° e così via — ma quella che interessa è sempre la più breve, cioè quella perpendicolare. La perpendicolarità è una retta condotta rispetto a un'altra in modo da formare un angolo di 90°; graficamente l'angolo retto si indica con un quartino di circonferenza oppure con il segno di perpendicolarità (il piccolo quadrato). Disegnare correttamente le perpendicolari è una delle difficoltà di chi non ha mai disegnato: è bene esercitarsi a non tracciare rette che "quasi" sono perpendicolari.

Questo concetto è fondamentale, perché quando più avanti dovremo misurare la distanza di un punto da un piano, la prima cosa a cui pensare sarà sempre la perpendicolarità.

## Rette parallele, incidenti e sghembe

Due rette si dicono parallele se sono complanari ed equidistanti, cioè se non hanno alcun punto in comune. Se due rette appartengono allo stesso piano — per esempio al vostro foglio — possono trovarsi solo in due situazioni: o sono parallele, oppure sono incidenti, e in questo caso si incontrano in un punto.

Se invece due rette non appartengono allo stesso piano, si dicono sghembe. Due rette sghembe appartengono a due piani diversi e, prese insieme, definiscono una superficie: molte coperture dei nostri centri storici, per esempio, sono vere e proprie superfici sghembe, perché costruite su quattro pali di cui basta che uno non appartenga al piano degli altri tre.

Vale inoltre una proprietà importante: dati una retta $r$ e un punto $P$ che non le appartiene, per quel punto è possibile tracciare una e una sola parallela alla retta data.

Lo stesso ragionamento si estende ai piani: due piani paralleli non hanno alcun punto in comune, mentre due piani incidenti hanno in comune una retta.

## Diedri e triedri

Due piani incidenti, oltre a condividere una retta, delimitano delle porzioni di spazio. Ciascuna di queste porzioni, racchiusa tra i due semipiani, si chiama diedro. Il diedro è dunque ognuna delle porzioni di spazio delimitate da due semipiani che hanno in comune una retta.

> [!note] I piani sono infiniti
> In geometria descrittiva i piani vanno sempre pensati come infiniti, anche se noi siamo costretti a disegnarli delimitati (come dei rettangoli) per poterli rappresentare sul foglio.

Possiamo poi parlare di triedro: è una porzione di spazio delimitata da tre piani. Lavoreremo spesso con il triedro, perché avere un terzo piano di riferimento è molto utile. Tre piani distinti hanno in comune un punto — il vertice del triedro — che diventerà l'origine degli assi.

Anche nello spazio le relazioni si conservano: una retta e un piano hanno in comune un punto, nel quale si incontrano. Una retta esterna a un piano può essere secante (se lo incontra in un punto) oppure parallela al piano. Una retta è parallela a un piano se è parallela a una retta del piano. Una retta è invece perpendicolare a un piano se è perpendicolare a due rette del piano. La distanza di un punto da un piano, infine, è sempre data dal segmento compreso tra il punto e il piede della perpendicolare condotta dal punto al piano.

Come si vede, le definizioni sono tutte concatenate: la geometria, come la matematica, è una sequenza logica di operazioni in cui ogni concetto richiama il precedente. Non bisogna impararle a memoria "a vuoto", ma capire come si legano tra loro.

## I postulati di appartenenza e i loro duali

Conviene fissare i primi tre postulati di appartenenza:

- per due punti distinti passa una e una sola retta;
- tre punti distinti e non allineati individuano un piano;
- un punto e una retta che non lo contiene individuano un piano.

A questi se ne aggiungono altri tre, detti duali, che si ottengono semplicemente sostituendo la parola "piano" alla parola "punto":

- due piani distinti individuano una retta che appartiene a entrambi (comunque siano disposti);
- tre piani distinti, che non passano per una stessa retta, individuano un punto comune a tutti e tre;
- una retta e un piano distinti individuano un punto.

Nel caso dei tre piani è importante la condizione "che non passano per una stessa retta": se tre piani passassero tutti per la medesima retta (come tre pagine di un libro), avrebbero in comune quella retta e non un punto. È invece quando non condividono una retta che individuano un unico punto comune.

## Le convenzioni grafiche

Prima di procedere occorre fissare le convenzioni, cioè il modo in cui si indicano gli elementi:

- le lettere maiuscole dell'alfabeto indicano i punti, e soltanto i punti;
- le lettere minuscole dell'alfabeto latino ($r$, $s$, ...) indicano le rette;
- le lettere minuscole dell'alfabeto greco ($\alpha$, $\beta$, $\gamma$, $\delta$) indicano i piani.

Ci sono poi i simboli: quello di parallelismo e quello di appartenenza (per esempio "il punto $A$ appartiene al piano"). Importante è anche il tratto del segno: i segni di costruzione devono essere sottili ma sempre visibili, perché al professore interessa il procedimento e non solo il risultato; un segno medio va bene per le operazioni; un segno più marcato va riservato al risultato finale.

## La geometria proiettiva: proiezione e sezione

Passiamo ora alla lezione vera e propria, che riguarda la geometria proiettiva. Tutti i metodi di rappresentazione che studieremo hanno in comune la stessa origine: sono espressioni diverse di uno stesso procedimento proiettivo. Conoscendone il principio, in pratica li si conosce tutti.

Questi metodi servono a rappresentare sul piano — il foglio da disegno, che ha due sole dimensioni — ciò che avviene nello spazio. L'obiettivo è trasformare i problemi geometrici dello spazio in problemi di geometria piana, risolvibili sul quaderno.

Quando si proietta una figura su un piano, tra la figura e la sua proiezione non c'è un'uguaglianza perfetta: solo alcune proprietà si conservano, e dipendono anche dalla posizione della figura rispetto al piano. Se proietto un quadrato su uno schermo inclinato, per esempio, gli angoli retti non si mantengono; è l'effetto del cinema, in cui l'immagine proiettata risulta più grande dell'originale. La geometria proiettiva studia proprio le proprietà delle figure che rimangono invariate durante le operazioni di proiezione e sezione: queste proprietà si dicono proprietà proiettive. Fu Girard Desargues, nel Seicento, a fondare questo studio.

Attenzione a distinguere i due termini: la proiezione è ciò che parte dalla fonte (come un fascio di luce da un proiettore), mentre l'immagine che vediamo su una parete o su un tavolo è il frutto di una sezione, cioè di un'intersezione.

## Proiettare un punto, una retta, un piano

L'operazione di proiezione presuppone due elementi: un centro di proiezione e un piano di quadro (indicato con PQ), cioè il piano su cui si proietta.

Proiettare un punto da un centro di proiezione significa costruire il raggio proiettante, cioè la retta che passa per il centro $S$ e per il punto $P$ (per due punti passa una e una sola retta). Questo raggio attraversa il piano di quadro e vi lascia un punto, che è la proiezione: se il punto di partenza si chiama $P$, la sua proiezione si chiama $P'$ (nelle proiezioni ortogonali la chiameremo invece $P_1$, per distinguerla da quella delle proiezioni assonometriche).

La sequenza centro – oggetto – piano di quadro non è rigida: il piano di quadro può anche trovarsi tra il centro e l'oggetto, come avviene nelle macchine fotografiche. L'oggetto, inoltre, può stare al di là o al di qua del piano di quadro, e questo sarà importante soprattutto per la prospettiva: per ottenere immagini più grandi, l'oggetto deve stare davanti al piano di quadro.

Proiettare una retta da un centro significa invece costruire un fascio di rette, cioè tante rette che passano tutte per il centro e per gli infiniti punti della retta da proiettare. La caratteristica del fascio di rette è di appartenere tutto a uno stesso piano.

Proiettare un piano, infine, significa proiettare dal centro tutte le rette che gli appartengono: si ottiene così una stella di rette, che a differenza del fascio non appartengono a un unico piano.

## Le proprietà proiettive

Le proprietà proiettive fondamentali, pur essendo intuitive, servono a risolvere gli esercizi:

- appartenenza: se un punto $P$ appartiene alla retta $r$, la sua immagine $P'$ appartiene alla retta immagine $r'$;
- allineamento: punti allineati restano allineati anche dopo la proiezione;
- incidenza: se due rette sono incidenti in un punto $P$, anche le loro immagini $r'$ e $s'$ sono incidenti nel punto immagine $P'$.

## Gli enti impropri: punti e rette all'infinito

La geometria proiettiva introduce il concetto di ente geometrico improprio, cioè un ente la cui posizione è considerata, per convenzione, all'infinito. Noi non percepiamo l'infinito, ma la geometria proiettiva ne dimostra l'esistenza per induzione geometrica.

Si pensi al modello della retta proiettiva costruito con una circonferenza. Si prende una circonferenza, si pone su di essa il centro di proiezione $S$ e si considera una retta $r$ alla base. Proiettando da $S$ tutti i punti della retta $r$, a ogni punto corrisponde un punto sulla circonferenza. Continuando a proiettare, anche quando il raggio proiettante si dispone parallelo alla retta $r$ esso lascia comunque un'immagine sulla circonferenza, esattamente come gli altri punti. Questo significa che l'intersezione tra le due rette parallele esiste: si trova all'infinito. La circonferenza è quindi il modello grafico della retta proiettiva, cioè di una retta a cui si aggiunge il suo punto all'infinito.

Due rette parallele, dunque, si incontrano in un punto all'infinito (punto improprio), che si rappresenta attraverso la sua direzione, indicata con un piccolo trattino: la direzione ci dice verso dove sta "andando" la retta. Così i postulati di appartenenza si ampliano: per due punti passa una e una sola retta anche quando uno dei due è improprio, perché la retta conterrà il punto proprio e la direzione dell'altro.

## Proiezioni coniche e cilindriche

Il tipo di proiezione dipende dalla posizione del centro di proiezione:

- se il centro di proiezione è proprio (al finito), dal centro parte una stella di rette: si parla di proiezioni coniche;
- se il centro di proiezione è improprio (all'infinito), i raggi proiettanti vanno considerati tutti paralleli tra loro e definiscono un'unica direzione: si parla di proiezioni cilindriche.

Le proiezioni coniche danno origine alla prospettiva; le proiezioni cilindriche comprendono invece le proiezioni ortogonali e le proiezioni assonometriche. Nell'assonometria la proiezione rispetto al piano di quadro non è necessariamente ortogonale: avremo perciò un'assonometria ortogonale, in cui la direzione è perpendicolare al piano di quadro, e un'assonometria obliqua. Da questa distinzione dipenderanno i nomi che useremo quando, tra qualche settimana, affronteremo l'assonometria.

## Prospettività, omografia e omologia

La proiettività più semplice si chiama prospettività: in essa si hanno un centro e un piano, e si stabilisce una corrispondenza biunivoca, nella quale a ogni elemento di un insieme corrisponde uno e un solo elemento dell'altro.

Se da un centro $S$ proiettiamo gli elementi di un piano $\alpha$ su un secondo piano $\alpha'$, a ogni punto di $\alpha$ corrisponde un punto di $\alpha'$: questa corrispondenza si chiama omografia. Due figure si dicono prospettive — cioè legate da una prospettività — quando:

- le rette che congiungono i vertici corrispondenti passano tutte per uno stesso punto, che è il centro di proiezione;
- le rette corrispondenti (i lati prolungati) si incontrano su una retta fissa, chiamata asse della prospettività, che non è altro che la retta di intersezione tra i due piani.

L'omologia nasce da un passo in più. Possiamo considerare due figure sullo stesso piano come il risultato della proiezione di una stessa figura di partenza (posta su un piano $\alpha_0$), ma ottenute da due centri di proiezione diversi, $S$ e $S'$, sullo stesso piano. L'omologia è quindi il prodotto di due prospettività: mentre nell'omografia c'è un solo centro che proietta da un piano a un altro, nell'omologia ci sono due centri che proiettano sul medesimo piano.

Il nostro obiettivo è sempre portare tutto sul foglio da disegno, che va interpretato come il piano $\alpha$ coincidente con $\alpha'$. Sul foglio abbiamo già una coppia di rette corrispondenti $r$ e $r'$, che — come sappiamo — si incontrano sull'asse, cioè sulla retta di intersezione tra i piani. Restano da portare sul piano i due centri di proiezione, che nello spazio stanno uno più in alto e uno più in basso: per farlo si proietta l'uno dall'altro, ottenendo un unico punto sul piano, che è il centro dell'omologia. I punti corrispondenti risultano allineati con questo centro.

Un'omologia è dunque definita da tre dati: il centro, l'asse e una coppia di elementi corrispondenti. Una volta definita, l'omologia vale indipendentemente dalle relazioni nello spazio che l'hanno generata: gli esercizi che faremo sono astratti e non devono preoccuparci della configurazione spaziale di partenza.

> [!abstract] Le due proprietà da ricordare
> 1. I punti corrispondenti sono allineati con il centro.
> 2. Le rette corrispondenti si incontrano sull'asse.
>
> Saperle a memoria non basta: bisogna saperle applicare.

## Gli esercizi di omologia

Il tipo più semplice di esercizio è il seguente. Sono dati il centro, l'asse e una coppia di punti corrispondenti $A$ e $A'$; viene dato un punto $B$ e si chiede di trovare il suo corrispondente $B'$.

Si procede così. Per la prima proprietà, $B'$ è allineato con il centro: si traccia quindi il raggio che parte dal centro e passa per $B$, lungo il quale si troverà $B'$. Per individuarlo esattamente si usa la seconda proprietà: si costruisce la retta $r$ che passa per $A$ e per $B$; questa retta incontra l'asse in un punto unito $U$; la retta corrispondente $r'$ deve passare per lo stesso punto $U$ (perché le rette corrispondenti si incontrano sull'asse) e per $A'$. Il punto $B'$ è allora l'intersezione tra la retta $r'$ e il raggio che parte dal centro e passa per $B$.

Se invece di un punto è dato un segmento, lo si prolunga fino a ottenere la retta che lo contiene e si applica lo stesso ragionamento. Se sono date direttamente due rette corrispondenti, per trovare il corrispondente di un punto conviene prima individuare una coppia di punti corrispondenti sulle rette, in modo da ricondursi all'esercizio più semplice. L'esercizio, in fondo, è sempre una somma di cose che già si conoscono: se si hanno i punti si cercano le rette, se si hanno le rette si cercano i punti.

## Le omologie particolari

A seconda della posizione reciproca dei piani e dei centri di proiezione, l'omologia assume nomi diversi:

- omologia speciale: si ha quando il centro, proiettando un centro dall'altro, viene a cadere proprio sull'asse. Non cambia nulla nella risoluzione: semplicemente il centro appartiene all'asse.
- affinità: si ha quando i due centri sono allineati lungo una retta parallela al piano. In questo caso il centro dell'omologia è all'infinito e va indicato con una direzione. Se la direzione che unisce i due centri è perpendicolare all'asse si parla di affinità ortogonale; se è obliqua, di affinità obliqua. Useremo l'affinità ortogonale nell'assonometria ortogonale e l'affinità obliqua nell'assonometria obliqua.
- omotetia: si ha quando il piano che contiene la figura è parallelo al piano di quadro. In questo caso l'asse è all'infinito (due piani paralleli si incontrano all'infinito) mentre il centro è proprio; le rette corrispondenti risultano parallele tra loro. La figura si ingrandisce in modo omotetico — è ciò che accade nella prospettiva centrale frontale, in cui una pianta parallela al piano si allarga omoteticamente secondo relazioni precise.
- traslazione: è il caso di massima indeterminazione, in cui sia il piano è parallelo (asse all'infinito) sia i due centri sono allineati parallelamente al piano (centro all'infinito). La figura si trasferisce tale e quale, conservando le distanze: viene semplicemente traslata.

In sintesi, l'omologia è sempre il prodotto di due prospettività, ma assume un nome differente a seconda della posizione dei piani e dei centri: omologia speciale, affinità (ortogonale od obliqua), omotetia e traslazione. Queste relazioni ci torneranno utili nel ribaltamento di figure piane, nell'assonometria e nelle sezioni delle piramidi.

> [!tip] Per la prossima volta
> Nella prossima lezione faremo insieme un esercizio di omologia e inizieremo le proiezioni ortogonali. Servirà il materiale per i modellini: cartoncino (meglio se un po' pesante, così sta in piedi), taglierino con la base di plastica da taglio, e bastoncini di legno un po' più lunghi e robusti degli stuzzicadenti.
