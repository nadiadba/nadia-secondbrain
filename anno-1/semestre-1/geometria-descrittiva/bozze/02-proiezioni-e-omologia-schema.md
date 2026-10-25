---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-06
tags: [geometria-descrittiva, bozza]
---

# Geometria proiettiva e omologia

> [!info] Note collegate
> Sbobina: [[02-proiezioni-e-omologia]] · Riepilogo dell'8 ottobre: [[03-proiettiva-e-proiezioni-ortogonali]] · Correzione dell'esercizio: [[04-rette-e-piani-metodo-di-monge]]
>
> Bozza precedente: [[01-strumenti-materiali-e-regole]] · Successiva: [[03-proiezioni-ortogonali-punto-e-rette]]

La lezione del 6 ottobre si divide in due parti.

La prima è un ripasso della geometria euclidea che serve da base a tutto il corso:

- la distanza di un punto da una retta,
- il parallelismo e l'incidenza,
- i diedri e i triedri,
- i postulati di appartenenza
- e le convenzioni grafiche.

La seconda introduce la geometria proiettiva, cioè lo studio delle proprietà che restano invariate quando una figura viene proiettata e sezionata, e arriva fino all'omologia e ai suoi casi particolari:

- omologia speciale,
- affinità ortogonale e obliqua,
- omotetia
- e traslazione.

L'omologia è l'argomento della Prova n. 1 di giovedì 29 ottobre, per questo l'ultima parte della bozza raccoglie, passo passo, tutti i tipi di esercizio che la docente ha proposto e corretto.

## RICHIAMI DI GEOMETRIA EUCLIDEA

### La distanza di un punto da una retta e da un piano

Data una retta $r$ e un punto $P$ che non le appartiene, la distanza del punto dalla retta è il segmento che ha per estremi $P$ e il piede della perpendicolare condotta da $P$ alla retta, cioè il punto in cui la perpendicolare incontra $r$.

Si parla di distanza minima perché si potrebbero misurare anche altri segmenti inclinati, a 30° o a 40°, ma quello che interessa è sempre il più breve, quello perpendicolare.

La perpendicolare è una retta che forma con l'altra un angolo di 90°, e sul disegno l'angolo retto si segna con un quartino di circonferenza oppure con un piccolo quadrato. Bisogna esercitarsi a tracciare perpendicolari vere, non rette che lo sono "quasi".

Il concetto è fondamentale perché ritorna nello spazio: la distanza di un punto da un piano è il segmento compreso tra il punto e il piede della perpendicolare condotta dal punto al piano.

Ogni volta che si dovrà misurare una distanza, la prima cosa a cui pensare sarà la perpendicolarità.

> [!example] Disegno 1 · Il disegno: la distanza di un punto da una retta
> ![[b02-distanza-punto-retta.svg|560]]
>
> 1. Si disegnano la retta $r$ e il punto $P$ esterno.
> 2. Da $P$ si conduce la perpendicolare a $r$; il punto in cui la incontra è il piede $H$.
> 3. Si segna l'angolo retto in $H$.
> 4. $PH$ è la distanza: i segmenti inclinati (tratteggiati) sono tutti più lunghi.

> [!example] Disegno 2 (proposto, non fatto a lezione): la distanza di un punto da un piano
> ![[b02-distanza-punto-piano.svg|560]]
>
> 1. Si disegnano il piano $\alpha$ (in prospettiva, come un parallelogramma) e il punto $P$ esterno, sopra il piano.
> 2. Da $P$ si conduce la perpendicolare al piano; il punto in cui lo incontra è il piede $H$.
> 3. Per verificare che $PH$ sia perpendicolare al piano, si prendono due rette del piano che passano per $H$, $a$ e $b$: $PH$ è perpendicolare a tutte e due, e si segnano i due angoli retti.
> 4. $PH$ è la distanza del punto dal piano: i segmenti inclinati (tratteggiati) che vanno da $P$ ad altri punti del piano sono tutti più lunghi.

### Rette e piani: paralleli, incidenti, sghembi

Due rette che stanno nello stesso piano, per esempio sul foglio, possono trovarsi solo in due situazioni:

- o sono parallele, cioè complanari ed equidistanti, senza alcun punto in comune,
- oppure sono incidenti e si incontrano in un punto.

Due rette che non appartengono allo stesso piano si dicono invece sghembe: non si incontrano e non sono parallele. Prese insieme definiscono una superficie, e molte coperture dei centri storici sono vere superfici sghembe, costruite su quattro pali di cui basta che uno non stia nel piano degli altri tre.

Vale poi una proprietà importante: dati una retta e un punto che non le appartiene, per quel punto passa una e una sola parallela alla retta.

Lo stesso ragionamento vale per i piani:

- due piani paralleli non hanno punti in comune,
- due piani incidenti hanno in comune una retta.

Una retta e un piano si incontrano in un punto; una retta esterna a un piano può essere:

- secante, se lo incontra in un punto,
- oppure parallela al piano, se non lo incontra, e lo è quando è parallela a una retta del piano.

Una retta è perpendicolare a un piano quando è perpendicolare a due rette del piano.

> [!example] Disegno 3 · Il disegno: rette parallele e incidenti
> ![[b02-rette-parallele-incidenti.svg|640]]
>
> 1. A sinistra le rette $r$ e $s$ sono parallele: non si incontrano.
> 2. Al centro sono incidenti: si incontrano nel punto $P$.
> 3. A destra, per il punto $P$ esterno a $r$ si traccia l'unica parallela $s$.

### Diedri e triedri

Il diedro è la porzione di spazio compresa tra due semipiani che hanno in comune una retta, e nasce da due piani incidenti. Due piani incidenti, oltre a condividere una retta, delimitano delle porzioni di spazio: ciascuna di queste porzioni, racchiusa tra due semipiani che hanno in comune una retta, si chiama diedro.

Il triedro è invece la porzione di spazio delimitata da tre piani; tre piani distinti hanno in comune un punto, il vertice del triedro, che diventerà l'origine degli assi.

Il triedro tornerà spesso, perché avere un terzo piano di riferimento è molto utile: anche i tre piani di proiezione $\pi_1$, $\pi_2$, $\pi_3$ formano un triedro.

I piani vanno sempre pensati infiniti, anche se sul foglio siamo costretti a disegnarli come rettangoli.

Gli angoli tra i piani non sono per forza retti: nella definizione i piani possono formare un angolo qualsiasi.

- Un diedro può essere acuto, retto o ottuso: per esempio due facce vicine di una piramide formano un diedro non retto, mentre due facce vicine di un parallelepipedo rettangolo formano un diedro retto.
- Anche i tre piani di un triedro, in generale, possono essere inclinati tra loro.

Il triedro che usiamo nelle proiezioni ortogonali è invece un caso particolare: $\pi_1$ (orizzontale), $\pi_2$ (verticale di fronte) e $\pi_3$ (verticale di lato) sono perpendicolari a due a due, quindi tutti i suoi angoli sono retti.

Tutte queste definizioni sono concatenate, ognuna richiama la precedente: non vanno imparate "a vuoto", ma capite nel loro legame.

> [!example] Disegno 4 · Il disegno: diedro e triedro
> ![[b02-diedro-triedro.svg|640]]
>
> 1. Diedro: i semipiani $\alpha$ e $\beta$ hanno in comune la retta $r$ e racchiudono una porzione di spazio.
> 2. Triedro: i piani $\alpha$, $\beta$ e $\gamma$ hanno in comune il solo vertice $V$, futura origine degli assi.

### I postulati di appartenenza e i loro duali

I primi tre postulati di appartenenza dicono:

- che per due punti distinti passa una e una sola retta,
- che tre punti distinti e non allineati individuano un piano
- e che un punto e una retta che non lo contiene individuano un piano.

Sostituendo la parola "piano" alla parola "punto" si ottengono i tre postulati duali:

- due piani distinti individuano una retta che appartiene a entrambi;
- tre piani distinti, che non passano per una stessa retta, individuano un punto comune a tutti e tre;
- una retta e un piano distinti individuano un punto.

La condizione sui tre piani è importante: se passassero tutti per la stessa retta, come tre pagine di un libro, avrebbero in comune quella retta e non un punto.

> [!abstract] Da ricordare: i sei postulati
> - Due punti distinti → una retta. Tre punti non allineati → un piano. Un punto e una retta che non lo contiene → un piano.
> - Duali: due piani distinti → una retta. Tre piani che non passano per una stessa retta → un punto. Una retta e un piano → un punto.
> - Valgono anche con gli enti impropri: una retta passa per due punti propri, ma anche per un punto proprio e uno improprio.

### Le convenzioni grafiche

Le convenzioni servono a riconoscere subito di che cosa si sta parlando.

- Le lettere maiuscole indicano i punti, e soltanto i punti;
- le minuscole dell'alfabeto latino ($r$, $s$) indicano le rette;
- le minuscole dell'alfabeto greco ($\alpha$, $\beta$, $\gamma$, $\delta$) indicano i piani.

Si usano poi i simboli di parallelismo e di appartenenza.

Anche il tratto ha un significato:

- i segni di costruzione devono essere sottili ma sempre visibili, perché alla docente interessa il procedimento e non solo il risultato;
- il segno medio va bene per le operazioni,
- quello più marcato è riservato al risultato finale.

> [!abstract] Da ricordare: lettere e segni
> - Punti: maiuscole ($P$). Rette: minuscole latine ($r$). Piani: minuscole greche ($\alpha$).
> - Costruzioni sottili ma visibili, risultato marcato.
> - Le lettere sono obbligatorie: nelle esercitazioni un disegno senza lettere viene considerato un errore (avviso del 13 ottobre).

## I FONDAMENTI DELLA GEOMETRIA PROIETTIVA

### Rappresentare lo spazio sul foglio

Tutti i metodi di rappresentazione che si studiano nel corso hanno la stessa origine: sono espressioni diverse di uno stesso procedimento proiettivo, in cui ci sono:

- un centro di proiezione,
- un oggetto
- e un piano di quadro su cui l'oggetto viene proiettato.

Conoscendone il principio, in pratica li si conosce tutti.

Lo scopo è rappresentare sul foglio, che ha due sole dimensioni, ciò che avviene nello spazio, trasformando i problemi geometrici dello spazio in problemi di geometria piana.

Tra una figura e la sua proiezione non c'è uguaglianza: solo alcune proprietà si conservano, e dipendono anche dalla posizione della figura rispetto al piano. Proiettando un quadrato su uno schermo inclinato gli angoli retti non si mantengono, e al cinema l'immagine proiettata è più grande dell'originale.

La geometria proiettiva, fondata da Girard Desargues nel Seicento, studia proprio le proprietà delle figure che restano invariate durante le operazioni di proiezione e sezione, dette proprietà proiettive.

I due termini vanno distinti:

- la proiezione è ciò che parte dalla fonte, come il fascio di luce di un proiettore;
- l'immagine che vediamo su una parete è invece il frutto di una sezione, cioè di un'intersezione.

### Proiettare un punto, una retta, un piano

L'operazione di proiezione richiede due elementi:

- un centro di proiezione $S$
- e un piano di quadro (PQ), il piano su cui si proietta.

Proiettare un punto $P$ significa costruire il raggio proiettante, la retta che passa per $S$ e per $P$: dove il raggio attraversa il piano di quadro lascia la proiezione $P'$.

La sequenza centro, oggetto, piano di quadro non è rigida:

- il piano può stare anche tra il centro e l'oggetto, come nella macchina fotografica,
- e l'oggetto può trovarsi al di qua o al di là del quadro, cosa che conterà soprattutto nella prospettiva.

Proiettare una retta significa costruire un fascio di rette, cioè tante rette che passano tutte per il centro e per gli infiniti punti della retta: il fascio appartiene tutto a uno stesso piano.

Proiettare un piano significa invece proiettare dal centro tutte le sue rette, e si ottiene una stella di rette, che non stanno in un unico piano.

> [!example] Disegno 5 · Il disegno: proiettare un punto e una retta
> ![[b02-proiezione-punto-retta.svg|660]]
>
> 1. Punto: il raggio da $S$ per $P$ incontra il piano di quadro in $P'$.
> 2. Retta: i raggi da $S$ per i punti di $r$ formano un fascio, tutto in un piano (in arancio).
> 3. Quel piano taglia il piano di quadro lungo $r'$, la proiezione di $r$.

> [!example] Disegno 6 (proposto, non fatto a lezione): proiettare un piano
> ![[b02-proiezione-piano.svg|560]]
>
> 1. Si disegnano il centro $S$, una porzione del piano $\alpha$ (in blu) e il piano di quadro.
> 2. Da $S$ si proiettano i punti di $\alpha$: i quattro vertici e alcuni punti interni.
> 3. I raggi vanno in tutte le direzioni, in alto, in basso, a destra e a sinistra: non stanno in un unico piano, come invece il fascio della retta. Questa è la stella di rette.
> 4. Dove i raggi incontrano il piano di quadro si ottiene la proiezione $\alpha'$ (in rosso).

### Le proprietà proiettive

Le proprietà proiettive fondamentali sembrano ovvie, ma sono la struttura di ogni rappresentazione e la chiave per risolvere gli esercizi.

- Per l'appartenenza, se un punto $P$ appartiene a una retta $r$, la sua immagine $P'$ appartiene alla retta immagine $r'$.
- Per l'allineamento, punti allineati restano allineati dopo la proiezione.
- Per l'incidenza, se due rette sono incidenti in un punto $P$, le loro immagini $r'$ e $s'$ sono incidenti nel punto immagine $P'$.

> [!abstract] Da ricordare: le tre proprietà proiettive
> - Appartenenza: $P \in r$ → $P' \in r'$.
> - Allineamento: punti allineati restano allineati.
> - Incidenza: $r$ e $s$ incidenti in $P$ → $r'$ e $s'$ incidenti in $P'$.

### Gli enti impropri

La geometria proiettiva introduce gli enti impropri: punti, rette e piani la cui posizione si considera, per convenzione, all'infinito.

In altre parole, si chiamano propri gli enti che stanno a una distanza finita, cioè quelli che possiamo disegnare sul foglio, e impropri quelli che stanno all'infinito. A che cosa serve? Nella geometria euclidea due rette parallele non si incontrano mai; nella geometria proiettiva, invece, si dice che si incontrano anche loro, ma in un punto che sta all'infinito: il punto improprio.

L'infinito non si vede, ma se ne dimostra l'esistenza per induzione geometrica con il modello della circonferenza (Disegno 7).

1. Si prende una circonferenza, si pone su di essa il centro di proiezione $S$ e si considera una retta $r$ alla base.
2. Proiettando da $S$ i punti di $r$, a ciascuno corrisponde un punto della circonferenza;
3. continuando, anche il raggio che diventa parallelo a $r$ lascia un'immagine sulla circonferenza, come tutti gli altri.

Per capire il modello conviene guardare il Disegno 7 seguendo i punti da sinistra a destra.

La circonferenza fa da "schermo": il centro $S$ sta sulla circonferenza, e ogni raggio che parte da $S$ la taglia in un secondo punto, che è l'immagine del punto di $r$ da cui passa il raggio.

- Il raggio che va da $S$ ad $A$ taglia la circonferenza in $A'$: $A'$ è l'immagine di $A$.
- Il raggio che va da $S$ a $B$ la taglia in $B'$, e il raggio che va da $S$ a $C$ la taglia in $C'$.

Ora si immagini di prendere punti di $r$ sempre più lontani, verso destra, oltre $C$. Più il punto è lontano, più il raggio che parte da $S$ per raggiungerlo si abbassa poco: diventa sempre più "piatto", cioè sempre più vicino a essere parallelo a $r$. Di conseguenza la sua immagine sulla circonferenza sale, da $C'$ verso $P'$.

Alla fine si arriva al raggio parallelo a $r$ (la linea rossa tratteggiata). Questo raggio non incontra $r$ in nessun punto che si possa disegnare, ma taglia comunque la circonferenza, nel punto $P'$.

Il ragionamento è questo. Ogni raggio che parte da $S$ e incontra $r$ in un punto lascia la sua immagine sulla circonferenza. Il raggio parallelo a $r$ non incontra $r$ in nessun punto che possiamo disegnare, eppure lascia anche lui la sua immagine sulla circonferenza.

Se esiste l'immagine, esiste il punto che l'ha generata, e si trova all'infinito: la circonferenza è il modello della retta proiettiva, cioè della retta a cui si aggiunge il suo punto improprio.

Due rette parallele, dunque, si incontrano in un punto improprio (Disegno 8), che si rappresenta con la sua direzione, un piccolo trattino che dice verso dove "va" la retta. Infatti il punto improprio non si può disegnare, perché sta all'infinito.

Tutte le rette parallele tra loro hanno la stessa direzione, quindi hanno lo stesso punto improprio: per questo si dice che si incontrano lì.

I postulati di appartenenza si ampliano di conseguenza: per due punti passa una e una sola retta anche quando uno dei due è improprio, perché la retta conterrà il punto proprio e avrà la direzione dell'altro.

Per esempio, dati un punto $A$ sul foglio e un punto improprio $P_\infty$ (cioè una direzione), la retta che li contiene tutti e due è la retta che passa per $A$ e ha quella direzione: è la parallela per $A$.

> [!example] Disegno 7 · Il disegno: il modello della circonferenza
> ![[b02-retta-proiettiva.svg|600]]
>
> 1. Si disegnano la circonferenza, il centro $S$ su di essa e la retta $r$.
> 2. I raggi da $S$ per $A$, $B$, $C$ incontrano la circonferenza in $A'$, $B'$, $C'$.
> 3. Anche il raggio parallelo a $r$ incontra la circonferenza, in $P'$: è l'immagine del punto improprio $P_\infty$ di $r$.

> [!example] Disegno 8 · Il disegno: il punto improprio di rette parallele
> ![[b02-punto-improprio.svg|600]]
>
> 1. Le parallele $r$ e $s$ si incontrano in $P_\infty$, segnato con il trattino nella loro direzione.
> 2. Per il punto $A$ e per $P_\infty$ passa una sola retta: la $t$, parallela a $r$ e $s$.

### Proiezioni coniche e cilindriche

Il tipo di proiezione dipende dalla posizione del centro.

- Se il centro è proprio, cioè a distanza finita, da esso parte una stella di rette e si hanno le proiezioni coniche, da cui nasce la prospettiva.
- Se il centro è improprio, all'infinito, i raggi proiettanti sono tutti paralleli e definiscono un'unica direzione: si hanno le proiezioni cilindriche, che comprendono le proiezioni ortogonali e le assonometrie.

È la stessa differenza che c'è tra l'ombra di una lampada, che ha un centro proprio, e l'ombra del sole, i cui raggi si assumono paralleli perché il sole è molto distante.

Nell'assonometria la direzione di proiezione può essere:

- perpendicolare al piano di quadro (assonometria ortogonale)
- oppure inclinata (assonometria obliqua).

> [!example] Disegno 9 · Il disegno: centro proprio e centro improprio
> ![[03-proiezione-centrale-e-cilindrica.svg|640]]
>
> 1. Centro $S$ proprio: i raggi partono tutti da $S$ e la figura proiettata cambia dimensione (proiezione conica).
> 2. Centro improprio: i raggi sono paralleli e la figura viene trasferita con le stesse dimensioni (proiezione cilindrica).

## DALLA PROSPETTIVITÀ ALL'OMOLOGIA

### La prospettività e l'omografia

La proiettività più semplice è la prospettività: ci sono un centro e due piani, e si stabilisce una corrispondenza biunivoca, in cui a ogni punto di un piano corrisponde uno e un solo punto dell'altro.

Corrispondenza biunivoca vuol dire che la corrispondenza funziona nei due sensi, a coppie:

- a ogni punto del primo piano corrisponde un solo punto del secondo,
- e a ogni punto del secondo piano corrisponde un solo punto del primo.

Per immaginarla si può pensare a una lampadina, il centro $S$, a una lastra di vetro con un triangolo disegnato sopra, il piano $\alpha$, e a un muro, il piano $\alpha'$: la luce che parte dalla lampadina e passa per il triangolo disegna sul muro un altro triangolo. Ogni punto del triangolo sul vetro ha il suo punto nel triangolo sul muro, e viceversa.

Se da un centro $S$ si proiettano gli elementi di un piano $\alpha$ su un secondo piano $\alpha'$, la corrispondenza tra i punti dei due piani si chiama omografia.

Prospettività e omografia descrivono quindi la stessa situazione da due punti di vista:

- la prospettività è l'operazione, cioè proiettare da un centro $S$ un piano su un altro piano;
- l'omografia è il nome della corrispondenza che si ottiene, cioè il legame tra ogni punto di $\alpha$ e il suo punto su $\alpha'$.

Due figure sono prospettive:

- quando le rette che congiungono i vertici corrispondenti passano tutte per uno stesso punto, il centro di proiezione,
- e quando le rette corrispondenti, cioè i lati prolungati, si incontrano su una retta fissa, l'asse della prospettività, che è la retta di intersezione tra i due piani.

Il punto in cui una retta incontra l'asse si chiama punto unito: sta sulla retta di intersezione, quindi appartiene a tutti e due i piani, e proiettandolo si ottiene lo stesso punto.

Perché le rette corrispondenti si incontrano proprio sull'asse? Si prenda il lato $AB$, che sta sul piano $\alpha$, e il suo corrispondente $A'B'$, che sta sul piano $\alpha'$.

1. Se si prolunga $AB$, prima o poi esce dal piano $\alpha$ proprio dove $\alpha$ incontra $\alpha'$, cioè sull'asse.
2. In quel punto il raggio che parte da $S$ trova lo stesso punto su tutti e due i piani, perché il punto sta già su $\alpha'$: la sua proiezione è sé stesso.
3. Quindi anche $A'B'$ prolungato passa per quel punto, e i due lati si incontrano lì, sull'asse. Quel punto è il punto unito.

Le due proprietà, allineamento con il centro e incontro sull'asse, valgono per una retta, per tante rette e per ogni figura, per esempio per i lati $AB$, $BC$, $CA$ di un triangolo.

> [!example] Disegno 10 · Il disegno: la prospettività tra due piani
> ![[b02-prospettivita.svg|660]]
>
> 1. Il triangolo $ABC$ sta su $\alpha$; proiettandolo da $S$ su $\alpha'$ si ottiene $A'B'C'$.
> 2. Ogni raggio da $S$ contiene due vertici corrispondenti.
> 3. I lati corrispondenti prolungati si incontrano a due a due sull'asse, intersezione dei due piani: i cerchietti sono i punti uniti.
> 4. Il centro $S$ sta fuori da tutti e due i piani: è in alto, sopra $\alpha$, e davanti ad $\alpha'$, dalla parte di chi guarda. Qui il piano $\alpha'$ sta tra $S$ e il triangolo $ABC$, come nella macchina fotografica: i raggi partono da $S$, attraversano $\alpha'$ (dove lasciano $A'$, $B'$, $C'$) e arrivano ai vertici di $ABC$.

### L'omologia: due prospettività sullo stesso piano

L'omologia nasce da un passo in più. Due figure che stanno sullo stesso piano si possono pensare come il risultato della proiezione di una stessa figura di partenza, posta su un altro piano $\alpha_0$, da due centri diversi, $S$ e $S_1$. Se le relazioni valgono nello spazio, per Desargues valgono anche sul piano.

Per portare tutto sul foglio, che va interpretato come il piano $\alpha$ coincidente con $\alpha'$, bisogna portarci anche i centri, che nello spazio stanno uno più in alto e uno più in basso: si proietta un centro dall'altro e si ottiene un solo punto del piano, il centro dell'omologia $U$.

L'asse è sempre la retta di intersezione tra i piani considerati.

L'omologia è dunque la relazione tra due figure generate dalla proiezione della stessa figura da due centri diversi: è il prodotto di due prospettività.

- Nell'omografia c'è un solo centro che proietta da un piano a un altro;
- nell'omologia ci sono due centri che proiettano sul medesimo piano.

Una volta definita, l'omologia vale indipendentemente dalla configurazione spaziale che l'ha generata: gli esercizi sono astratti e vanno risolti sul piano, senza figurarsi lo spazio.

> [!example] Disegno 11 · Il disegno: dai due centri al centro dell'omologia
> ![[b02-omologia-due-centri.svg|660]]
>
> 1. Il segmento $A_0B_0$ sta su $\alpha_0$; proiettandolo su $\alpha$ da $S$ si ottiene $AB$, da $S_1$ si ottiene $A'B'$.
> 2. $AB$, $A'B'$ e $A_0B_0$ si incontrano sull'asse $u$, intersezione di $\alpha_0$ e $\alpha$.
> 3. La retta $SS_1$ incontra il piano in $U$: è il centro dell'omologia.
> 4. Sul piano $U$, $A$, $A'$ sono allineati, e così $U$, $B$, $B'$.

### Centro, asse e coppia di elementi corrispondenti

Un'omologia è definita da tre dati:

- il centro,
- l'asse
- e una coppia di elementi corrispondenti (due punti, oppure due rette).

Con questi dati la figura corrispondente di qualunque figura è una sola: per una configurazione di dati esiste una e una sola retta corrispondente di una retta data.

La corrispondenza conserva le proprietà proiettive: a rette corrispondono rette, a rette incidenti rette incidenti. Non è invece una corrispondenza di forma, come quella tra due triangoli simili.

Per risolvere gli esercizi non serve altro che le due proprietà dell'omologia e le condizioni di appartenenza. Saperle a memoria non basta: bisogna saperle applicare.

> [!example] Disegno 12 · Il disegno: due triangoli corrispondenti
> ![[b02-omologia-centro-asse.svg|620]]
>
> 1. Le rette $AA'$, $BB'$, $CC'$ passano tutte per il centro $U$.
> 2. I lati $AB$ e $A'B'$, $BC$ e $B'C'$, $CA$ e $C'A'$ si incontrano sull'asse $u$ (cerchietti).

> [!abstract] Da ricordare: le due proprietà dell'omologia
> 1. I punti corrispondenti sono allineati con il centro.
> 2. Le rette corrispondenti si incontrano sull'asse.
>
> Il punto in cui una retta incontra l'asse è un punto unito: corrisponde a sé stesso, quindi sta sia sulla retta sia sulla sua corrispondente.

### Le convenzioni dell'omologia

Le convenzioni non sono indifferenti alla comprensione del problema: guardando il disegno si distingue subito di che cosa si sta parlando.

- Il centro è un punto e si indica con la maiuscola $U$;
- l'asse è una retta e si indica con la minuscola $u$.
- I corrispondenti si indicano con l'apice: $A$ e $A'$, $r$ e $r'$.

Nelle proiezioni ortogonali si useranno invece i pedici ($P_1$, $P_2$, $P_3$), perché l'apice resta all'omologia e all'assonometria.

> [!abstract] Da ricordare: come si scrive
> - Centro $U$ (punto, segnato), asse $u$ (retta). Corrispondenti con l'apice: $A$ → $A'$, $r$ → $r'$.
> - Centro improprio: $U_\infty$ con una lineetta. La lineetta non è casuale: è la direzione in cui stanno tutti i punti corrispondenti.
> - Asse improprio: $u_\infty$ con una crocetta.

## LE OMOLOGIE PARTICOLARI

A seconda della posizione reciproca dei piani e dei centri di proiezione, l'omologia prende nomi diversi. I nomi aiutano a distinguere le situazioni, ma la soluzione degli esercizi resta sempre la stessa.

Quella con centro e asse propri è l'omologia classica.

### L'omologia speciale

L'omologia è speciale quando, proiettando un centro dall'altro, il centro viene a cadere proprio sull'asse. Nella risoluzione non cambia nulla: semplicemente il centro appartiene all'asse.

> [!example] Disegno 13 · Il disegno: l'omologia speciale
> ![[b02-omologia-speciale.svg|620]]
>
> 1. $U$ sta sull'asse $u$.
> 2. I corrispondenti restano allineati con $U$ e i lati corrispondenti si incontrano sull'asse.

### L'affinità ortogonale e obliqua

Si ha un'affinità quando i due centri sono allineati lungo una retta parallela al piano: la retta che li unisce non incontra il piano a distanza finita, ma all'infinito. Il centro dell'omologia è allora improprio e si indica con una direzione.

Unendo i punti corrispondenti si ottengono rette tutte parallele a quella direzione:

- se la direzione è perpendicolare all'asse l'affinità è ortogonale,
- se è inclinata è obliqua.

L'affinità ortogonale servirà nell'assonometria ortogonale, l'obliqua nell'assonometria obliqua; un'affinità compare anche nel ribaltamento, dove il centro è all'infinito nella direzione perpendicolare all'asse.

> [!example] Disegno 14 · Il disegno: affinità ortogonale e obliqua
> ![[b02-affinita.svg|640]]
>
> 1. $U_\infty$ si disegna con la lineetta della sua direzione.
> 2. Le rette $AA'$, $BB'$, $CC'$ sono tutte parallele a quella direzione.
> 3. I lati corrispondenti si incontrano sull'asse $u$, come nell'omologia classica.
> 4. Direzione perpendicolare a $u$: affinità ortogonale; direzione inclinata: affinità obliqua.

### L'omotetia

L'omotetia si ha quando il piano che contiene la figura è parallelo al piano su cui la si proietta. La retta di intersezione tra i due piani, cioè l'asse, è allora impropria, mentre il centro è proprio.

Poiché le rette corrispondenti si incontrano sull'asse, che è all'infinito, le rette corrispondenti sono necessariamente parallele: è la differenza fondamentale dell'omotetia.

La figura si ingrandisce, come un rettangolo parallelo alla parete illuminato da una lampada, o come la pianta che si allarga nella prospettiva centrale frontale.

> [!example] Disegno 15 · Il disegno: l'omotetia
> ![[b02-omotetia.svg|620]]
>
> 1. Asse all'infinito: $u_\infty$ con la crocetta.
> 2. $A'$, $B'$, $C'$ stanno sui raggi da $U$.
> 3. I lati corrispondenti sono paralleli: $A'B' \parallel AB$, $B'C' \parallel BC$, $C'A' \parallel CA$.

### La traslazione

La traslazione è il caso limite, di massima indeterminazione:

- il piano della figura è parallelo al piano su cui si proietta (asse all'infinito)
- e anche i due centri sono allineati parallelamente al piano (centro all'infinito).

È un'isometria, una trasformazione del piano che conserva distanze e angoli: un quadrato rimane un quadrato e il segmento $A'B'$ è uguale ad $AB$.

La figura viene semplicemente spostata.

> [!example] Disegno 16 · Il disegno: la traslazione
> ![[b02-traslazione.svg|620]]
>
> 1. Centro e asse impropri: $U_\infty$ con la lineetta, $u_\infty$ con la crocetta.
> 2. Tutti i punti si spostano nella direzione di $U_\infty$ della stessa quantità.
> 3. I lati corrispondenti sono paralleli e uguali.

> [!abstract] Da ricordare: i casi dell'omologia
> - Omologia classica: centro $U$ proprio, asse $u$ proprio.
> - Omologia speciale: $U$ proprio che sta sull'asse $u$.
> - Affinità: centro improprio $U_\infty$, asse proprio. Ortogonale se la direzione è perpendicolare all'asse, obliqua se è inclinata.
> - Omotetia: centro proprio $U$, asse improprio $u_\infty$; rette corrispondenti parallele.
> - Traslazione: $U_\infty$ e $u_\infty$; la figura si sposta uguale.

## COME SI RISOLVONO GLI ESERCIZI DI OMOLOGIA

### Il metodo

Ogni esercizio è una somma di cose già note: se si hanno i punti si cercano le rette, se si hanno le rette si cercano i punti.

La prima cosa da fare è sempre individuare una coppia di punti corrispondenti, perché serve sempre.

Se il testo dà due rette corrispondenti $r$ e $r'$, la coppia si trova prendendo un punto su $r$ e mandando il raggio dal centro fino a $r'$; ma conviene guardare se c'è un punto che appartiene già a due rette (per esempio l'intersezione tra la retta data e $r$), perché il suo corrispondente sta su entrambe le rette corrispondenti: è solo una condizione di appartenenza, ed è più rapido.

Si traccia una linea in meno, e meno linee si tracciano, meno l'errore grafico è in agguato.

Questo modo di procedere, un punto dopo l'altro, si chiama costruire per punti.

- Quando il centro è improprio, "mandare il raggio dal centro" significa tracciare dal punto la parallela alla direzione di $U_\infty$.
- Quando l'asse è improprio, "le rette corrispondenti si incontrano sull'asse" significa che sono parallele: la retta corrispondente si traccia come parallela per un punto già trovato.

Alla fine conviene sempre verificare con un'altra coppia di punti: la figura corrispondente è una sola, quindi qualunque coppia si usi il risultato deve essere lo stesso.

> [!abstract] Da ricordare: i passaggi di ogni esercizio
> 1. Trova una coppia di punti corrispondenti ($A$ e $A'$), se non è già data.
> 2. Per trovare $X'$: traccia la retta $AX$ e prolungala fino all'asse (punto unito); unisci il punto unito con $A'$.
> 3. $X'$ sta dove questa retta incontra il raggio da $U$ per $X$.
> 4. Con $U_\infty$: al posto del raggio, la parallela alla direzione del centro. Con $u_\infty$: al posto del punto unito, la parallela ad $AX$ per $A'$.
> 5. Verifica: i lati corrispondenti si incontrano sull'asse (o sono paralleli, se l'asse è improprio).

### Omologia classica: dati A e A′, trovare B′

È l'esercizio più semplice, quello spiegato a lezione il 6 ottobre: sono dati il centro, l'asse, una coppia di punti corrispondenti $A$ e $A'$ e un punto $B$, e si chiede il corrispondente $B'$.

Se invece di un punto è dato un segmento, lo si prolunga fino a ottenere la retta che lo contiene e si ragiona allo stesso modo.

> [!example] Disegno 17 · Il disegno: dati U, u, A e A′, trovare B′
> ![[b02-es-punto-coppia.svg|620]]
>
> 1. $B'$ è allineato con $U$: si traccia il raggio da $U$ per $B$.
> 2. Si traccia la retta $r$ per $A$ e $B$ e la si prolunga fino all'asse: lì c'è il punto unito $V$.
> 3. La retta corrispondente $r'$ passa per $V$ e per $A'$.
> 4. $B'$ è l'intersezione tra $r'$ e il raggio da $U$ per $B$.

### Omologia classica: date le rette corrispondenti r e r′

Quando sono date due rette corrispondenti, si cerca prima la coppia di punti e ci si riconduce all'esercizio precedente.

È l'esercizio fatto insieme l'8 ottobre ed è lo stesso tipo del terzo esercizio del foglio «ES.GUIDATA Omologia 01» (dati $U$, $u$, $r$ e $r'$ che si incontrano sull'asse, trovare $M'$).

> [!example] Disegno 18 · Il disegno: dati U, u, r e r′, trovare P′ (lezione dell'8 ottobre)
> ![[03-omologia-punto-corrispondente.svg|620]]
>
> 1. Si sceglie un punto $A$ su $r$ e si manda il raggio da $U$: dove incontra $r'$ c'è $A'$.
> 2. Si traccia $s$ per $A$ e $P$ fino all'asse: punto unito $W$.
> 3. $s'$ passa per $W$ e per $A'$.
> 4. $P'$ sta su $s'$ e sul raggio da $U$ per $P$.

> [!example] Disegno 19 (proposto, non fatto a lezione): esercizio 3 di «ES.GUIDATA Omologia 01»
> ![[b02-es-classica-punto-m.svg|620]]
>
> Sono dati il centro $U$, l'asse $u$ e le rette corrispondenti $r$ e $r'$, che si incontrano in un punto unito dell'asse; si chiede il corrispondente $M'$ del punto $M$, che sta tra $U$ e l'asse.
>
> 1. Si sceglie un punto $A$ su $r$ e si traccia il raggio da $U$ per $A$. Il raggio non incontra il tratto di $r'$ disegnato sotto l'asse: si prolunga $r'$ oltre l'asse, e dove il raggio la incontra c'è $A'$.
> 2. Si traccia la retta $s$ per $A$ e $M$ fino all'asse: lì c'è il punto unito $W$.
> 3. La retta corrispondente $s'$ passa per $W$ e per $A'$.
> 4. Si traccia il raggio da $U$ per $M$ e lo si prolunga oltre $U$: $M'$ è il punto in cui incontra $s'$.
> 5. In questo esercizio $M'$ cade dall'altra parte del centro rispetto a $M$, sopra $U$. Verifica: $U$, $M$ e $M'$ sono allineati e $s$ e $s'$ si incontrano sull'asse in $W$.

### Omologia speciale

Il metodo non cambia: l'unica particolarità è che il centro sta sull'asse, quindi i raggi partono da un punto dell'asse.

Il foglio «OMOLOGIA riepilogo» contiene un esercizio di questo tipo con la soluzione della docente; il secondo esercizio del foglio «ES.GUIDATA Omologia 01» è dello stesso tipo, ma senza soluzione.

> [!example] Disegno 20 · Il disegno: dati U sull'asse, ABC e A′, trovare A′B′C′ (soluzione della docente, «OMOLOGIA riepilogo»)
> ![[b02-es-speciale-figura.svg|620]]
>
> 1. Si prolunga il lato $AC$ (la retta $r$) fino all'asse: punto unito 1.
> 2. $r'$ passa per 1 e per $A'$; $C'$ sta su $r'$ e sul raggio da $U$ per $C$.
> 3. Si prolunga $AB$ fino all'asse: punto unito 2. La retta per 2 e $A'$ incontra il raggio da $U$ per $B$ in $B'$.
> 4. Verifica: $BC$ e $B'C'$ si incontrano sull'asse (punto 3).

> [!example] Disegno 21 (proposto, non fatto a lezione): dati U sull'asse, r e r′, trovare M′ («ES.GUIDATA Omologia 01», esercizio 2)
> ![[b02-es-speciale-punto.svg|580]]
>
> 1. Si sceglie un punto $A$ su $r$ e si manda il raggio da $U$: dove incontra $r'$ c'è $A'$.
> 2. Si traccia la retta $s$ per $A$ e $M$ fino all'asse: punto unito $W$.
> 3. $s'$ passa per $W$ e per $A'$.
> 4. $M'$ sta su $s'$ e sul raggio da $U$ per $M$.

### Omotetia: asse improprio

Con l'asse all'infinito le rette corrispondenti sono parallele: non si cerca il punto unito, si traccia la parallela.

Il foglio «OMOLOGIA riepilogo» ha due esercizi di questo tipo con la soluzione della docente (trovare $P'$ e trovare la retta $n'$); l'esercizio sulla retta $s'$ del foglio «ES.GUIDATA» è stato corretto in aula il 13 ottobre.

> [!example] Disegno 22 · Il disegno: dati U, u∞, r e r′ e il punto P, trovare P′ (soluzione della docente, «OMOLOGIA riepilogo»)
> ![[b02-es-omotetia-punto.svg|560]]
>
> 1. Si sceglie un punto $A$ su $r$ e si manda il raggio da $U$: dove incontra $r'$ c'è $A'$.
> 2. Si unisce $P$ con $A$.
> 3. Per $A'$ si traccia la parallela a $PA$ (l'asse è all'infinito).
> 4. $P'$ sta su questa parallela e sul raggio da $U$ per $P$.

> [!example] Disegno 23 · Il disegno: dati U, u∞, r e r′, trovare s′ (correzione del 13 ottobre)
> ![[04-omologia-retta-corrispondente.svg|620]]
>
> 1. Si prolunga $r$ fino a $s$: il punto comune $P$ sta su entrambe le rette.
> 2. Il raggio da $U$ per $P$ incontra $r'$ in $P'$, che sta su $r'$ e su $s'$.
> 3. $s'$ è la parallela a $s$ per $P'$.
> 4. Verifica (in blu): con un altro punto $M$ di $s$ si trova $M'$, che cade su $s'$.

> [!example] Disegno 24 (proposto, non fatto a lezione): dati U, u∞, A e A′, trovare A′B′C′D′ («ES.GUIDATA Omologia 01», esercizio 5)
> ![[b02-es-omotetia-figura.svg|580]]
>
> 1. Si mandano i raggi da $U$ per tutti i vertici.
> 2. Per $A'$ si traccia la parallela ad $AB$: dove incontra il raggio da $U$ per $B$ c'è $B'$.
> 3. Per $B'$ la parallela a $BC$ dà $C'$; per $C'$ la parallela a $CD$ dà $D'$.
> 4. Verifica: $D'A'$ deve risultare parallela a $DA$.

### Affinità: centro improprio

Con il centro all'infinito i corrispondenti stanno su rette parallele alla direzione di $U_\infty$, mentre l'asse resta proprio e i lati corrispondenti si incontrano su di esso.

Il foglio «OMOLOGIA riepilogo» ha due esercizi di questo tipo con la soluzione della docente; l'esercizio della figura ℒ del foglio «ES.GUIDATA» è stato corretto in aula il 13 ottobre.

Il foglio «OMOLOGIA 2 affinità», tratto dal libro di Docci, Gaiani e Maestri, propone anche un'omologia affine speciale, in cui la direzione di $U_\infty$ è parallela all'asse.

> [!example] Disegno 25 · Il disegno: dati U∞, u, ABC e A′, trovare A′B′C′ (soluzione della docente, «OMOLOGIA riepilogo»)
> ![[b02-es-affinita-figura.svg|580]]
>
> 1. La direzione di $U_\infty$ è quella della retta $AA'$: da ogni vertice si tracciano le parallele a questa direzione.
> 2. Si prolunga $AC$ fino all'asse: punto unito 1. La retta per 1 e $A'$ incontra la parallela per $C$ in $C'$.
> 3. Si prolunga $BC$ fino all'asse: punto unito 2. La retta per 2 e $C'$ incontra la parallela per $B$ in $B'$.
> 4. Si uniscono $A'$, $B'$, $C'$.

> [!example] Disegno 26 · Il disegno: dati U∞, u, r e r′ e la retta m, trovare m′ (soluzione della docente, «OMOLOGIA riepilogo»)
> ![[b02-es-affinita-retta.svg|600]]
>
> 1. Si sceglie $A$ su $r$; la parallela alla direzione di $U_\infty$ incontra $r'$ in $A'$.
> 2. Si sceglie $B$ su $m$ e si traccia la retta $n$ per $A$ e $B$ fino all'asse: punto unito $N$.
> 3. $n'$ passa per $N$ e per $A'$; la parallela per $B$ alla direzione di $U_\infty$ la incontra in $B'$.
> 4. $m$ incontra l'asse nel punto unito $Q$: $m'$ passa per $Q$ e per $B'$.

> [!example] Disegno 27 · Il disegno: dati U∞, u, r e r′, trovare la figura corrispondente di ℒ (correzione del 13 ottobre)
> ![[04-omologia-figura-corrispondente.svg|620]]
>
> 1. Il vertice $A$ sta su $r$: andando nella direzione di $U_\infty$ fino a $r'$ si trova $A'$.
> 2. Il lato $AB$ prolungato incontra l'asse in un punto unito; $A'B'$ passa per quel punto e per $A'$; $B'$ sta sulla parallela per $B$ alla direzione del centro.
> 3. Allo stesso modo, con $AD$ si trova $D'$ e con $DC$ si trova $C'$.
> 4. Verifica: i lati corrispondenti si incontrano tutti sull'asse.

> [!example] Disegno 28 · Il disegno: omologia affine speciale, dati il quadrato ABCD e B′ (soluzione della docente, «OMOLOGIA 2 affinità»)
> ![[b02-es-affinita-speciale.svg|640]]
>
> 1. La direzione di $U_\infty$ è parallela all'asse: da ogni vertice si tracciano le parallele all'asse.
> 2. Si prolunga $AB$ fino all'asse (punto 1): la retta per 1 e $B'$ incontra la parallela per $A$ in $A'$.
> 3. Si prolunga $CB$ fino all'asse (punto 2): la retta per 2 e $B'$ incontra la parallela per $C$ in $C'$.
> 4. $CD$ incontra l'asse nel punto 3: la retta per 3 e $C'$ incontra la parallela per $D$ in $D'$.

### Traslazione: centro e asse impropri

Con centro e asse all'infinito valgono insieme le due regole:

- i corrispondenti stanno sulle parallele alla direzione di $U_\infty$
- e le rette corrispondenti sono parallele.

Il foglio «OMOLOGIA riepilogo» ha un esercizio con la soluzione della docente; il primo esercizio del foglio «ES.GUIDATA» è dello stesso tipo, con un triangolo.

> [!example] Disegno 29 · Il disegno: dati U∞, u∞, r e r′ e il punto P, trovare P′ (soluzione della docente, «OMOLOGIA riepilogo»)
> ![[b02-es-traslazione-punto.svg|560]]
>
> 1. Si sceglie $M$ su $r$; la parallela alla direzione di $U_\infty$ incontra $r'$ in $M'$.
> 2. Si unisce $P$ con $M$; per $M'$ si traccia la parallela a $PM$.
> 3. La parallela per $P$ alla direzione di $U_\infty$ la incontra in $P'$.
> 4. $PP'$ e $MM'$ risultano uguali e paralleli: è una traslazione.

> [!example] Disegno 30 (proposto, non fatto a lezione): dati U∞, u∞, r e r′ e il triangolo ABC, trovare A′B′C′ («ES.GUIDATA Omologia 01», esercizio 1)
> ![[b02-es-traslazione-figura.svg|580]]
>
> 1. Si sceglie $M$ su $r$ e si trova $M'$ su $r'$ nella direzione di $U_\infty$.
> 2. Per $M'$ la parallela ad $AM$ incontra la parallela per $A$ alla direzione di $U_\infty$ in $A'$.
> 3. Con la coppia $A$, $A'$ si trovano allo stesso modo $B'$ e $C'$.
> 4. $A'B'C'$ è uguale ad $ABC$, soltanto spostato.

## L'ESERCITAZIONE IN AULA: IL SECONDO SOLIDO

Alla fine della lezione la docente fa svolgere in aula un secondo esercizio di piante e prospetti, sullo stesso modello di quello della [[01-strumenti-materiali-e-regole|prima lezione]].

Il solido è dato in assonometria nella scheda esrcit_02 ed è più articolato del primo: è misurato con due moduli diversi, b per le dimensioni in pianta e a per le altezze (quattro moduli a), a partire dall'origine O, e ha anche linee nascoste tratteggiate e superfici inclinate.

Si risolve con lo stesso procedimento:

1. impaginare il foglio con il reticolo dei moduli,
2. disegnare le piante ruotando l'oggetto,
3. ricavare i prospetti,
4. campire.

Questa parte della lezione non è registrata, perché in aula si lavorava in silenzio.

> [!example] Disegno 31 · Il disegno: il secondo solido in assonometria (scheda della docente)
> ![[b01-esercizio-2-solido-assonometria.png|520]]
>
> 1. Si parte dall'origine O, in basso: da lì partono i due spigoli di base (misurati con il modulo b) e lo spigolo verticale (misurato con il modulo a, quattro volte).
> 2. Si ricopia prima il reticolo con linee leggere: le tacche dei moduli b sui lati in alto e dei moduli a sul lato verticale a destra.
> 3. Poi si ripassano con il tratto marcato gli spigoli visibili del solido; le linee nascoste restano tratteggiate.
> 4. Per l'esercizio si procede come nel primo: reticolo dei moduli sul foglio, piante ruotate, prospetti, campiture.

> [!tip] Consegne e avvisi
> - Prova n. 1 sull'omologia: giovedì 29 ottobre (calendario della docente; accennata a lezione il 13 ottobre).
> - 8 ottobre: stampare gli esercizi di omologia indicati dalla docente e farli a casa (probabilmente i fogli «ES.GUIDATA Omologia 01» e «OMOLOGIA riepilogo»). La correzione è stata fatta il 13 ottobre; il calendario prevede anche la correzione dell'esercitazione sulle omologie il 15 ottobre e un'esercitazione guidata sulle omologie il 22 ottobre.
> - Per la lezione dell'8 ottobre: materiale per i modellini (cartoncino un po' pesante, taglierino con base da taglio, bastoncini di legno più lunghi e robusti degli stuzzicadenti).
> - Disegni grandi e lettere sempre scritte; linee di costruzione più leggere del risultato.

## Collegamenti

L'omologia è lo strumento che tiene insieme tutto il corso.

Le proprietà proiettive e le condizioni di appartenenza viste qui tornano subito nelle proiezioni ortogonali, introdotte nella lezione dell'8 ottobre ([[03-proiettiva-e-proiezioni-ortogonali]] e [[03-proiezioni-ortogonali-punto-e-rette]]), dove i punti si indicano con i pedici invece che con l'apice, e nel metodo di Monge per rette e piani ([[04-rette-e-piani-metodo-di-monge]], [[04-rette-e-piani-nelle-varie-posizioni]], [[05-appartenenza-e-rette-ausiliarie]]).

L'affinità ortogonale ricompare nel ribaltamento ([[07-ribaltamento-piani-proiettanti]] e [[07-il-ribaltamento]]), dove tra la prima proiezione di una figura e il suo ribaltamento c'è un'omologia con l'asse sulla traccia-cerniera e il centro all'infinito nella direzione perpendicolare all'asse.

Più avanti l'affinità servirà nell'assonometria, ortogonale e obliqua, e l'omologia nella sezione delle piramidi e nella ricerca della vera forma di una sezione; l'omotetia è alla base della prospettiva centrale frontale.

Le regole sul tratto e sulle lettere riprendono quelle della prima lezione ([[01-strumenti-materiali-e-regole]]).

## Materiale usato

I file della cartella `materiale` da cui viene questa bozza (si aprono solo sul computer dove c'è il materiale).

- [[ARGOMENTI LEZIONI 26-27.pdf]]: elenco degli argomenti della lezione
- [[PROGRAMMA_26-27.pdf]]: bibliografia e modalità d'esame
- [[ES.GUIDATA_Omologia_01.pdf]]: i sei esercizi guidati sull'omologia
- [[OMOLOGIA_riepilogo.pdf]]: sei esercizi di riepilogo
- [[OMOLOGIA_riepilogo_soluzione.pdf]]: soluzioni della docente, ridisegnate nella bozza
- [[OMOLOGIA_2_affinità.pdf]]: esercizio sull'affinità
- [[OMOLOGIA_2_affinità_soluzione.pdf]]: soluzione della docente
- [[esrcit_02.pdf]]: il secondo solido in assonometria, esercitazione in aula
- [[Calendario_attivita_AA_2026-2027_ottobre-dicembre.pdf]]: data della Prova n. 1
