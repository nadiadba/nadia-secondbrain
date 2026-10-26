---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-06
tags: [geometria-descrittiva, appunti, teoria]
---

# Teoria: geometria proiettiva e omologia

> [!info] Note collegate
> Bozza con gli esercizi: [[02-proiezioni-e-omologia-schema]] · Sbobine: [[02-proiezioni-e-omologia]] (6 ottobre) · [[03-proiettiva-e-proiezioni-ortogonali]] (8 ottobre)
>
> Teoria successiva: [[teoria-proiezioni-ortogonali]]

Questa pagina raccoglie tutta la teoria della prima parte del corso, dalle lezioni del 6 e dell'8 ottobre: i richiami di geometria euclidea, la geometria proiettiva, la prospettività e l'omologia con i suoi casi particolari, fino alla traslazione.

Gli esercizi non ci sono: si trovano nella bozza [[02-proiezioni-e-omologia-schema]].

---

## 1. RICHIAMI DI GEOMETRIA EUCLIDEA

### 1.1 Le distanze

#### 1.1.1 La distanza di un punto da una retta

La distanza di un punto da una retta è il segmento che ha per estremi il punto e il piede della perpendicolare condotta dal punto alla retta. Data una retta $r$ e un punto $P$ che non le appartiene, il piede della perpendicolare è il punto in cui la perpendicolare da $P$ incontra $r$.

Si parla di distanza minima perché si potrebbero misurare anche altri segmenti inclinati, a 30° o a 40°, ma quello che interessa è sempre il più breve, cioè quello perpendicolare.

La perpendicolare è una retta che forma con l'altra un angolo di 90°. Sul disegno l'angolo retto si segna con un quartino di circonferenza oppure con un piccolo quadrato. Bisogna esercitarsi a tracciare perpendicolari vere, non rette che lo sono "quasi".

> [!example] Disegno 1 · La distanza di un punto da una retta
> ![[b02-distanza-punto-retta.svg|560]]
>
> Da $P$ si conduce la perpendicolare a $r$, che la incontra nel piede $H$; in $H$ è segnato l'angolo retto.
> $PH$ è la distanza: i segmenti inclinati (tratteggiati) sono tutti più lunghi.

#### 1.1.2 La distanza di un punto da un piano

Il concetto ritorna nello spazio. La distanza di un punto da un piano è il segmento compreso tra il punto e il piede della perpendicolare condotta dal punto al piano.

Per questo, ogni volta che si dovrà misurare una distanza, la prima cosa a cui pensare sarà la perpendicolarità.

> [!example] Disegno 2 · La distanza di un punto da un piano
> ![[b02-distanza-punto-piano.svg|560]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. Da $P$ si conduce la perpendicolare al piano $\alpha$, che lo incontra nel piede $H$.
> $PH$ è perpendicolare alle due rette $a$ e $b$ del piano che passano per $H$ (i due angoli retti).
> I segmenti inclinati da $P$ ad altri punti del piano sono tutti più lunghi.

### 1.2 Rette e piani

#### 1.2.1 Due rette: parallele, incidenti, sghembe

Due rette che stanno nello stesso piano, per esempio sul foglio, possono trovarsi solo in due situazioni:

- o sono parallele, cioè complanari ed equidistanti, senza alcun punto in comune,
- oppure sono incidenti, e si incontrano in un punto.

Due rette che non appartengono allo stesso piano si dicono invece sghembe: non si incontrano e non sono parallele. Prese insieme definiscono una superficie, e molte coperture dei centri storici sono vere superfici sghembe, costruite su quattro pali di cui basta che uno non stia nel piano degli altri tre.

Vale poi una proprietà importante: dati una retta e un punto che non le appartiene, per quel punto passa una e una sola parallela alla retta.

> [!example] Disegno 3 · Rette parallele e incidenti
> ![[b02-rette-parallele-incidenti.svg|640]]
>
> A sinistra $r$ e $s$ sono parallele e non si incontrano; al centro sono incidenti nel punto $P$.
> A destra, per il punto $P$ esterno a $r$ passa una sola parallela, la retta $s$.

#### 1.2.2 Due piani

Lo stesso ragionamento vale per i piani:

- due piani paralleli non hanno punti in comune,
- due piani incidenti hanno in comune una retta.

#### 1.2.3 Una retta e un piano

Una retta e un piano si incontrano in un punto. Una retta esterna a un piano può essere:

- secante, se lo incontra in un punto,
- oppure parallela al piano, se non lo incontra.

Una retta è parallela a un piano quando è parallela a una retta del piano.

Una retta è perpendicolare a un piano quando è perpendicolare a due rette del piano.

### 1.3 Diedro e triedro

Il diedro è la porzione di spazio compresa tra due semipiani che hanno in comune una retta. Nasce da due piani incidenti: oltre a condividere una retta, i due piani delimitano delle porzioni di spazio, e ciascuna di queste porzioni è un diedro.

Il triedro è la porzione di spazio delimitata da tre piani. Tre piani distinti hanno in comune un punto, il vertice del triedro, che diventerà l'origine degli assi. Il triedro tornerà spesso, perché avere un terzo piano di riferimento è molto utile.

I piani vanno sempre pensati infiniti, anche se sul foglio siamo costretti a disegnarli come rettangoli.

Gli angoli tra i piani non sono per forza retti: nella definizione i piani possono formare un angolo qualsiasi.

- Un diedro può essere acuto, retto o ottuso: due facce vicine di una piramide formano un diedro non retto, mentre due facce vicine di un parallelepipedo rettangolo formano un diedro retto.
- Anche i tre piani di un triedro, in generale, possono essere inclinati tra loro.

Il triedro delle proiezioni ortogonali è invece un caso particolare: $\pi_1$ (orizzontale), $\pi_2$ (verticale di fronte) e $\pi_3$ (verticale di lato) sono perpendicolari a due a due, quindi tutti i suoi angoli sono retti.

Tutte queste definizioni sono concatenate, ognuna richiama la precedente: non vanno imparate "a vuoto", ma capite nel loro legame.

> [!example] Disegno 4 · Diedro e triedro
> ![[b02-diedro-triedro.svg|640]]
>
> Diedro: i semipiani $\alpha$ e $\beta$ hanno in comune la retta $r$ e racchiudono una porzione di spazio.
> Triedro: i piani $\alpha$, $\beta$ e $\gamma$ hanno in comune il solo vertice $V$, futura origine degli assi.

### 1.4 I postulati di appartenenza e i loro duali

I primi tre postulati di appartenenza sono questi:

- per due punti distinti passa una e una sola retta;
- tre punti distinti e non allineati individuano un piano;
- un punto e una retta che non lo contiene individuano un piano.

Sostituendo la parola "piano" alla parola "punto" si ottengono i tre postulati duali:

- due piani distinti individuano una retta che appartiene a entrambi;
- tre piani distinti, che non passano per una stessa retta, individuano un punto comune a tutti e tre;
- una retta e un piano distinti individuano un punto.

La condizione sui tre piani è importante: se passassero tutti per la stessa retta, come tre pagine di un libro, avrebbero in comune quella retta e non un punto.

### 1.5 Le convenzioni grafiche

Le convenzioni servono a riconoscere subito di che cosa si sta parlando:

- le lettere maiuscole indicano i punti, e soltanto i punti ($P$);
- le minuscole dell'alfabeto latino indicano le rette ($r$, $s$);
- le minuscole dell'alfabeto greco indicano i piani ($\alpha$, $\beta$, $\gamma$, $\delta$).

Si usano poi i simboli di parallelismo e di appartenenza.

Anche il tratto ha un significato:

- i segni di costruzione devono essere sottili ma sempre visibili, perché alla docente interessa il procedimento e non solo il risultato;
- il segno medio va bene per le operazioni;
- il segno più marcato è riservato al risultato finale.

Le lettere sono obbligatorie: nelle esercitazioni un disegno senza lettere viene considerato un errore (avviso del 13 ottobre).

---

## 2. LA GEOMETRIA PROIETTIVA

### 2.1 Che cos'è la geometria proiettiva

#### 2.1.1 Rappresentare lo spazio sul foglio

Tutti i metodi di rappresentazione del corso hanno la stessa origine: sono aspetti diversi di uno stesso processo proiettivo. Il processo proiettivo è un insieme di operazioni in cui compaiono sempre:

- un centro di proiezione,
- un oggetto
- e un piano di quadro su cui l'oggetto viene proiettato.

Conoscendone il principio, in pratica si conoscono tutti i metodi.

Lo scopo è rappresentare sul foglio, che ha due sole dimensioni, ciò che avviene nello spazio, trasformando i problemi geometrici dello spazio in problemi di geometria piana.

#### 2.1.2 Le proprietà invarianti

Tra una figura e la sua proiezione non c'è uguaglianza: alcune cose cambiano, e solo alcune proprietà si conservano. Quali si conservano dipende anche dalla posizione della figura rispetto al piano. Proiettando un quadrato su uno schermo inclinato gli angoli retti non si mantengono, e al cinema l'immagine proiettata è più grande dell'originale.

La geometria proiettiva studia proprio le proprietà delle figure che restano invariate durante le operazioni di proiezione e sezione. Queste proprietà si chiamano proprietà proiettive. La geometria proiettiva è stata fondata da Girard Desargues nel Seicento.

I due termini vanno distinti:

- la proiezione è ciò che parte dalla fonte, come il fascio di luce di un proiettore;
- l'immagine che vediamo su una parete è invece il frutto di una sezione, cioè di un'intersezione.

### 2.2 Proiettare

#### 2.2.1 Il centro di proiezione e il piano di quadro

L'operazione di proiezione richiede due elementi:

- un centro di proiezione $S$,
- e un piano di quadro (PQ), cioè il piano su cui si proietta.

La sequenza centro $S$, oggetto, piano di quadro non è rigida:

- il piano di quadro può stare anche tra il centro $S$ e l'oggetto, come nella macchina fotografica;
- l'oggetto può trovarsi al di qua o al di là del quadro, e questo conterà soprattutto nella prospettiva: per ottenere immagini più grandi, l'oggetto deve stare davanti al piano di quadro.

#### 2.2.2 Punto, retta e piano

Proiettare un punto $P$ significa costruire il raggio proiettante, cioè la retta che passa per $S$ e per $P$ (per due punti passa una e una sola retta). Dove il raggio attraversa il piano di quadro lascia la proiezione $P'$.

Proiettare una retta significa costruire un fascio di rette, cioè tante rette che passano tutte per il centro $S$ e per gli infiniti punti della retta. La caratteristica del fascio è di appartenere tutto a uno stesso piano.

Proiettare un piano significa proiettare dal centro $S$ tutte le sue rette. Si ottiene una stella di rette, che a differenza del fascio non stanno in un unico piano.

In sintesi:

- punto → raggio proiettante;
- retta → fascio di rette (in un piano);
- piano → stella di rette (non in un piano).

> [!example] Disegno 5 · Proiettare un punto e una retta
> ![[b02-proiezione-punto-retta.svg|660]]
>
> Punto: il raggio da $S$ per $P$ incontra il piano di quadro in $P'$.
> Retta: i raggi da $S$ per i punti di $r$ formano un fascio, tutto in un piano (in arancio), che taglia il piano di quadro lungo $r'$, la proiezione di $r$.

> [!example] Disegno 6 · Proiettare un piano
> ![[b02-proiezione-piano.svg|560]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. Da $S$ si proiettano i vertici e alcuni punti interni della porzione di piano $\alpha$ (in blu).
> I raggi vanno in tutte le direzioni e non stanno in un unico piano: è la stella di rette.
> Dove incontrano il piano di quadro si ottiene la proiezione $\alpha'$ (in rosso).

### 2.3 Le proprietà proiettive

Le proprietà proiettive fondamentali sembrano ovvie, ma sono la struttura di ogni rappresentazione e la chiave per risolvere gli esercizi:

- appartenenza: se un punto $P$ appartiene a una retta $r$, la sua immagine $P'$ appartiene alla retta immagine $r'$;
- allineamento: punti allineati restano allineati dopo la proiezione;
- incidenza: se due rette sono incidenti in un punto $P$, le loro immagini $r'$ e $s'$ sono incidenti nel punto immagine $P'$.

### 2.4 Gli enti impropri

#### 2.4.1 Enti propri e impropri

Gli enti impropri sono punti, rette e piani la cui posizione si considera, per convenzione, all'infinito. Si chiamano invece propri gli enti che stanno a distanza finita, cioè quelli che possiamo disegnare sul foglio.

A che cosa servono? Nella geometria euclidea due rette parallele non si incontrano mai. Nella geometria proiettiva, invece, si dice che si incontrano anche loro, ma in un punto che sta all'infinito: il punto improprio.

Oltre al punto improprio ci sono la retta impropria e il piano improprio.

#### 2.4.2 Il modello della circonferenza

L'infinito non si vede: del punto improprio di una retta se ne intuisce l'esistenza. La geometria proiettiva la dimostra per induzione geometrica con il modello della circonferenza, che è una dimostrazione sul piano (Disegno 7); la docente ne ha mostrato anche una nello spazio, con i raggi che vanno al piano di quadro.

1. Si prende una circonferenza, si pone su di essa il centro di proiezione $S$ e si considera una retta $r$ alla base.
2. Proiettando da $S$ i punti di $r$, a ciascuno corrisponde un punto della circonferenza.
3. Continuando, anche il raggio che diventa parallelo a $r$ lascia un'immagine sulla circonferenza, come tutti gli altri.

La circonferenza fa da "schermo". Il centro $S$ sta sulla circonferenza, e ogni raggio che parte da $S$ la taglia in un secondo punto, che è l'immagine del punto di $r$ da cui passa il raggio:

- il raggio da $S$ ad $A$ taglia la circonferenza in $A'$, che è l'immagine di $A$;
- il raggio da $S$ a $B$ la taglia in $B'$, e il raggio da $S$ a $C$ la taglia in $C'$.

Si immagini ora di prendere punti di $r$ sempre più lontani verso destra, oltre $C$. Più il punto è lontano, più il raggio che lo raggiunge si abbassa poco: diventa sempre più "piatto", cioè sempre più vicino a essere parallelo a $r$. Di conseguenza la sua immagine sulla circonferenza sale, da $C'$ verso $P'$.

Alla fine si arriva al raggio parallelo a $r$. Questo raggio non incontra $r$ in nessun punto che si possa disegnare, eppure taglia comunque la circonferenza, nel punto $P'$.

Il ragionamento è questo: se esiste l'immagine, esiste il punto che l'ha generata, e si trova all'infinito. La circonferenza è quindi il modello della retta proiettiva, cioè della retta a cui si aggiunge il suo punto improprio.

> [!example] Disegno 7 · Il modello della circonferenza
> ![[b02-retta-proiettiva.svg|600]]
>
> I raggi da $S$ per $A$, $B$, $C$ incontrano la circonferenza in $A'$, $B'$, $C'$.
> Anche il raggio parallelo a $r$ (rosso tratteggiato) incontra la circonferenza, in $P'$: è l'immagine del punto improprio $P_\infty$ di $r$.

#### 2.4.3 Il punto improprio e la lineetta

Due rette parallele si incontrano dunque in un punto improprio. Il punto improprio non si può disegnare, perché sta all'infinito: si rappresenta con la sua direzione, un piccolo trattino che dice verso dove "va" la retta. Con la retta, quindi, abbiamo anche una direzione.

Tutte le rette parallele tra loro hanno la stessa direzione, quindi hanno lo stesso punto improprio: per questo si dice che si incontrano lì.

#### 2.4.4 I postulati con gli enti impropri

I postulati di appartenenza si ampliano di conseguenza. Una retta passa per due punti propri, ma anche per un punto proprio e un punto improprio: la retta conterrà il punto proprio e avrà la direzione dell'altro.

Per esempio, dati un punto $A$ sul foglio e un punto improprio $P_\infty$, cioè una direzione, la retta che li contiene tutti e due è la retta per $A$ con quella direzione: la parallela per $A$.

Lo stesso vale per i piani, e restano validi tutti e sei i postulati, i tre di appartenenza e i loro duali.

> [!example] Disegno 8 · Il punto improprio di rette parallele
> ![[b02-punto-improprio.svg|600]]
>
> Le parallele $r$ e $s$ si incontrano in $P_\infty$, segnato con il trattino nella loro direzione.
> Per il punto $A$ e per $P_\infty$ passa una sola retta: la $t$, parallela a $r$ e $s$.

### 2.5 Proiezioni coniche e cilindriche

#### 2.5.1 Centro proprio e centro improprio

Il tipo di proiezione dipende dalla posizione del centro di proiezione $S$.

- Se il centro $S$ è proprio, cioè a distanza finita, da esso parte una stella di rette: si hanno le proiezioni coniche (o centrali).
- Se il centro $S$ è improprio, cioè all'infinito, i raggi proiettanti sono tutti paralleli tra loro e definiscono un'unica direzione: si hanno le proiezioni cilindriche.

È la stessa differenza che c'è tra l'ombra di una lampada, che ha un centro proprio, e l'ombra del sole: il sole è molto distante, quindi nella costruzione delle ombre i suoi raggi si assumono paralleli.

Con il centro proprio la figura proiettata cambia dimensione. Per esempio, se un fascio di luce illumina un rettangolo parallelo alla parete, il rettangolo arriva sulla parete ingrandito. Con la proiezione cilindrica, invece, la figura viene praticamente traslata, con le stesse dimensioni.

> [!example] Disegno 9 · Centro proprio e centro improprio
> ![[03-proiezione-centrale-e-cilindrica.svg|640]]
>
> A sinistra il centro $S$ è proprio: i raggi partono tutti da $S$ e il rettangolo, parallelo al piano di quadro, arriva ingrandito (proiezione conica).
> A destra il centro è improprio: i raggi sono paralleli e la figura arriva con le stesse dimensioni (proiezione cilindrica).

#### 2.5.2 I metodi di rappresentazione

Le due posizioni del centro danno luogo a metodi di rappresentazione diversi:

- dalle proiezioni coniche nasce la prospettiva, che è il caso più semplice, la fotografia;
- le proiezioni cilindriche comprendono le proiezioni ortogonali e le assonometrie.

Nell'assonometria la direzione di proiezione non è per forza perpendicolare al piano di quadro:

- se è perpendicolare si ha l'assonometria ortogonale,
- se è inclinata si ha l'assonometria obliqua.

Prospettiva e prospettività sono due cose diverse, anche se le parole si somigliano. La prospettiva è un metodo di rappresentazione, quello che nasce dalle proiezioni coniche. La prospettività è invece l'operazione proiettiva più semplice, la corrispondenza tra due piani descritta nel prossimo blocco.

---

## 3. LA PROSPETTIVITÀ E L'OMOGRAFIA

### 3.1 Le definizioni

La prospettività è la proiettività più semplice. È l'operazione con cui, da un centro $S$ che sta fuori dai due piani, si proiettano i punti di un piano $\alpha$ su un secondo piano $\alpha'$, stabilendo tra i due piani una corrispondenza biunivoca.

Corrispondenza biunivoca vuol dire che la corrispondenza funziona nei due sensi, a coppie:

- a ogni punto del primo piano corrisponde uno e un solo punto del secondo,
- e a ogni punto del secondo piano corrisponde uno e un solo punto del primo.

Per immaginarla si può pensare a una lampadina, il centro $S$, a una lastra di vetro con un triangolo disegnato sopra, il piano $\alpha$, e a un muro, il piano $\alpha'$. La luce che parte dalla lampadina e passa per il triangolo disegna sul muro un altro triangolo: ogni punto del triangolo sul vetro ha il suo punto nel triangolo sul muro, e viceversa.

L'omografia è la corrispondenza biunivoca tra i punti del piano $\alpha$ e i punti del piano $\alpha'$ che si ottiene proiettando da un centro $S$ gli elementi di $\alpha$ su $\alpha'$.

Prospettività e omografia descrivono quindi la stessa situazione da due punti di vista:

- la prospettività è l'operazione, cioè proiettare da un centro $S$ un piano su un altro piano;
- l'omografia è il nome della corrispondenza che si ottiene, cioè il legame tra ogni punto di $\alpha$ e il suo punto su $\alpha'$.

### 3.2 Le due proprietà

Due figure sono prospettive, cioè legate da una prospettività, quando valgono due proprietà.

1. Le rette che congiungono i punti corrispondenti passano tutte per uno stesso punto, il centro di proiezione. È per forza così: l'immagine $A'$ è prodotta da un raggio che parte da $S$ e passa per $A$, quindi $A$, $A'$ ed $S$ stanno su una stessa linea.
2. Le rette corrispondenti, per esempio i lati prolungati di due triangoli, si incontrano su una retta fissa, l'asse della prospettività. L'asse è la retta di intersezione tra il piano che contiene la figura e il piano su cui la si proietta.

Le due proprietà valgono per una retta, per tante rette e per ogni figura, per esempio per i lati $AB$, $BC$, $CA$ di un triangolo.

### 3.3 Il punto unito e l'asse

Il punto unito è il punto in cui una retta incontra l'asse. Sta sulla retta di intersezione, quindi appartiene a tutti e due i piani: proiettandolo non si ottiene un altro punto, si ottiene lo stesso punto. Per questo si chiama unito.

Perché le rette corrispondenti si incontrano proprio sull'asse? Si prenda il lato $AB$, che sta sul piano $\alpha$, e il suo corrispondente $A'B'$, che sta sul piano $\alpha'$.

1. Se si prolunga $AB$, prima o poi esce dal piano $\alpha$ proprio dove $\alpha$ incontra $\alpha'$, cioè sull'asse.
2. In quel punto il raggio che parte da $S$ trova lo stesso punto su tutti e due i piani, perché il punto sta già su $\alpha'$: la sua proiezione è sé stesso.
3. Quindi anche $A'B'$ prolungato passa per quel punto, e i due lati si incontrano lì, sull'asse. Quel punto è il punto unito.

> [!example] Disegno 10 · La prospettività tra due piani
> ![[b02-prospettivita.svg|660]]
>
> Il triangolo $ABC$ sta su $\alpha$; proiettandolo da $S$ su $\alpha'$ si ottiene $A'B'C'$, e ogni raggio da $S$ contiene due vertici corrispondenti.
> I lati corrispondenti prolungati si incontrano a due a due sull'asse, intersezione dei due piani: i cerchietti sono i punti uniti.
> Qui $\alpha'$ sta tra $S$ e il triangolo $ABC$, come nella macchina fotografica.

---

## 4. L'OMOLOGIA

### 4.1 Due prospettività sullo stesso piano

#### 4.1.1 Dallo spazio al foglio

L'omologia nasce da un passo in più: portare sul foglio le relazioni della prospettività. Il foglio va interpretato come il piano $\alpha$ coincidente con $\alpha'$: il piano viene girato, ribaltato, e dopo il ribaltamento le figure corrispondenti si trovano sullo stesso piano.

Come si legano allora due figure che stanno sullo stesso piano? Si possono pensare come il risultato della proiezione di una stessa figura di partenza, che appartiene a un altro piano, un piano verticale $\alpha_0$, da due centri di proiezione diversi, $S$ e $S_1$. Per Desargues, se le relazioni valgono nello spazio, valgono anche sul piano: i corrispondenti restano allineati e le rette corrispondenti si incontrano ancora sull'asse.

L'asse è sempre la retta di intersezione tra i piani considerati, qui $\alpha_0$ e $\alpha$.

Sul foglio bisogna portare anche i centri di proiezione, che nello spazio stanno uno più in alto e uno più in basso: non li si può lasciare "per aria". Per farlo si proietta un centro di proiezione dall'altro, cioè si traccia la retta $SS_1$ fino a dove buca il piano $\alpha$. Si ottiene un solo punto del piano: il centro dell'omologia $U$.

#### 4.1.2 La definizione

L'omologia è la relazione tra due figure generate dalla proiezione della stessa figura da due centri di proiezione diversi. È il prodotto di due prospettività: non si chiama più prospettività, perché i centri sono due.

La differenza con l'omografia è questa:

- nell'omografia c'è un solo centro di proiezione, che proietta da un piano a un altro;
- nell'omologia ci sono due centri di proiezione, che proiettano sul medesimo piano.

Tutti i segni che si trovano sul foglio sono il risultato di cose avvenute nello spazio. Una volta definita, però, l'omologia vale indipendentemente dalla configurazione spaziale che l'ha generata: gli esercizi sono astratti e vanno risolti sul piano, senza figurarsi lo spazio.

> [!example] Disegno 11 · Dai due centri al centro dell'omologia
> ![[b02-omologia-dai-centri-s-s1.svg|660]]
>
> Il segmento $A_0B_0$ sta su $\alpha_0$: da $S$ si proietta su $\alpha$ in $AB$, da $S_1$ in $A'B'$. I tre segmenti prolungati si incontrano sull'asse $u$.
> La retta $SS_1$ incontra il piano in $U$, il centro dell'omologia: sul piano $U$, $A$, $A'$ sono allineati, e così $U$, $B$, $B'$.
> $U$ non sta sull'asse: è dove la retta $SS_1$ incontra la retta $AA'$, e può cadere ovunque sul piano.
>
> Tutorial con un disegno per ogni passaggio: [[02-omologia-dai-due-centri-passo-passo|il Disegno 11 passo passo]].

### 4.2 Centro, asse e coppia di elementi corrispondenti

Un'omologia è definita da tre dati:

- il centro dell'omologia $U$,
- l'asse $u$,
- e una coppia di elementi corrispondenti (due punti, oppure due rette).

Con questi dati la figura corrispondente di qualunque figura è una sola: per una configurazione di dati esiste una e una sola retta corrispondente di una retta data.

La corrispondenza conserva le proprietà proiettive: a rette corrispondono rette, a rette incidenti rette incidenti. Non è invece una corrispondenza di forma, come quella tra due triangoli simili.

### 4.3 Le due proprietà dell'omologia

Le due proprietà dell'omografia restano verificate sul piano:

1. i punti corrispondenti sono allineati con il centro $U$;
2. le rette corrispondenti si incontrano sull'asse $u$.

È il teorema di Desargues sui due triangoli omologici.

Per risolvere gli esercizi non serve altro che queste due proprietà e le condizioni di appartenenza. Saperle a memoria però non basta: bisogna saperle applicare.

### 4.4 Il punto unito V

Il punto unito è il punto in cui una retta incontra l'asse, e si indica con $V$. Corrisponde a sé stesso, quindi sta sia sulla retta sia sulla sua corrispondente: è lì che le due rette corrispondenti si incontrano.

Il Disegno 12 è come guardare dall'alto il piano $\alpha$ del Disegno 11: lo spazio sparisce e sul foglio restano solo il centro $U$, l'asse $u$ e le figure corrispondenti. Nel Disegno 11 le figure erano due segmenti; qui sono due triangoli, ma le regole sono le stesse.

> [!example] Disegno 12 · Due triangoli corrispondenti
> ![[b02-omologia-centro-asse.svg|620]]
>
> Prima proprietà: le rette $AA'$, $BB'$, $CC'$ passano tutte per il centro $U$.
> Seconda proprietà: i lati $AB$ e $A'B'$, $BC$ e $B'C'$, $CA$ e $C'A'$ si incontrano sull'asse $u$, nei punti uniti (cerchietti).

### 4.5 Le convenzioni dell'omologia

Le convenzioni non sono indifferenti alla comprensione del problema: guardando il disegno si distingue subito di che cosa si sta parlando.

- Il centro dell'omologia è un punto e si indica con la maiuscola $U$; il punto si segna anche sul disegno.
- L'asse è una retta e si indica con la minuscola $u$.
- I corrispondenti si indicano con l'apice: $A$ e $A'$, $r$ e $r'$.
- Il centro improprio si scrive $U_\infty$ e si disegna con una lineetta.
- L'asse improprio si scrive $u_\infty$ e si segna con una crocetta.

La lineetta di $U_\infty$ non è casuale: non basta segnare il punto improprio con una lineetta qualunque, perché la lineetta è la direzione, quella in cui stanno tutte le rette che uniscono i punti corrispondenti.

La crocetta dell'asse improprio segna che l'asse è all'infinito: i due piani sono paralleli e si incontrano all'infinito, quindi l'asse non si può disegnare.

Nelle proiezioni ortogonali si useranno invece i pedici ($P_1$, $P_2$, $P_3$): l'apice resta all'omologia.

### 4.6 Centro di proiezione e centro dell'omologia

I due tipi di centro non vanno confusi:

- il centro di proiezione, $S$ (e $S_1$), sta nello spazio: è il punto da cui partono i raggi, e serve solo a capire da dove nasce l'omologia;
- il centro dell'omologia, $U$, sta sul foglio: è il punto per cui passano le rette che uniscono i punti corrispondenti.

Negli esercizi $S$ non compare mai: quando si parla del centro, si intende sempre $U$.

---

## 5. LE OMOLOGIE PARTICOLARI

A seconda della posizione reciproca dei piani e dei centri di proiezione, l'omologia prende nomi diversi. I nomi non sono difficili e aiutano a distinguere le situazioni, ma la soluzione degli esercizi resta sempre la stessa.

In breve, i tipi sono questi:

- omologia classica: $U$ e $u$ propri;
- omologia speciale: $U$ e $u$ propri, ma $U$ sta sull'asse $u$;
- affinità: $U$ improprio ($U_\infty$), $u$ proprio;
	- ortogonale, se la direzione di $U_\infty$ è perpendicolare all'asse;
	- obliqua, se la direzione di $U_\infty$ è inclinata rispetto all'asse;
- omotetia: $U$ proprio, $u$ improprio ($u_\infty$);
- traslazione: $U$ e $u$ impropri ($U_\infty$ e $u_\infty$).

Nello spazio, le due situazioni che mandano qualcosa all'infinito sono queste:

- se i due centri $S$ e $S_1$ sono alla stessa altezza, la retta $SS_1$ è parallela al foglio e non lo buca mai: il centro dell'omologia va all'infinito ($U_\infty$);
- se il piano $\alpha_0$ della figura è parallelo al foglio, i due piani non si tagliano: l'asse va all'infinito ($u_\infty$).

### 5.1 L'omologia classica

L'omologia classica è quella con centro $U$ e asse $u$ propri, e con $U$ fuori dall'asse. È il caso del Disegno 11 e del Disegno 12: la retta $SS_1$ buca il foglio in un punto qualsiasi, lontano dall'asse.

### 5.2 L'omologia speciale

L'omologia è speciale quando, proiettando un centro di proiezione dall'altro, il centro dell'omologia $U$ viene a cadere proprio sull'asse.

Per capire la frase bisogna tornare al Disegno 11.

1. Lì ci sono i due centri di proiezione nello spazio, $S$ e $S_1$.
2. "Proiettare un centro dall'altro" vuol dire tirare la retta che passa per $S$ e per $S_1$ e prolungarla finché buca il piano $\alpha$, cioè il foglio.
3. Il punto in cui la buca è il centro dell'omologia $U$.
4. Di solito questo punto cade in un posto qualsiasi del foglio, lontano dall'asse: è l'omologia classica.
5. Se invece $S$ e $S_1$ sono messi in modo che la retta $SS_1$ buchi il foglio proprio in un punto dell'asse $u$, allora $U$ sta sull'asse: è l'omologia speciale.

Non basta, e non funziona, mettere $S$ e $S_1$ sul piano $\alpha_0$. È vero che allora la retta $SS_1$ starebbe tutta su $\alpha_0$ e toccherebbe $\alpha$ sull'asse, ma anche i raggi che partono da $S$ resterebbero dentro $\alpha_0$: la figura $A_0B_0$ si schiaccerebbe tutta sull'asse e non ci sarebbe più niente da proiettare.

I due centri devono quindi stare fuori dai piani; basta che la retta che li unisce, prolungata, passi per un punto dell'asse. Per costruirla si sceglie un punto dell'asse, si mette $S$ dove si vuole, e si mette $S_1$ sulla retta che va da $S$ a quel punto.

Sul foglio l'omologia speciale si riconosce subito, perché il centro $U$ è disegnato sopra l'asse $u$. Nella risoluzione non cambia nulla: semplicemente il centro appartiene all'asse.

> [!example] Disegno 13 · L'omologia speciale sul foglio
> ![[b02-omologia-speciale-foglio.svg|620]]
>
> $U$ sta sull'asse $u$.
> I corrispondenti restano allineati con $U$ e i lati corrispondenti si incontrano sull'asse, come nell'omologia classica.

> [!example] Disegno 14 · L'omologia speciale nello spazio
> ![[b02-omologia-speciale-spazio-con-u.svg|660]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. È la stessa omologia del Disegno 13, con i piani come nel Disegno 11: da $S$ si ottiene $ABC$ (raggi blu), da $S_1$ si ottiene $A'B'C'$ (raggi verdi).
> $S_1$ sta sulla retta che va da $S$ a un punto dell'asse: per questo la retta $SS_1$ (rossa) buca il foglio proprio sull'asse, in $U$.
> Guardando il foglio $\alpha$ dall'alto si vede esattamente il Disegno 13.

### 5.3 L'affinità

#### 5.3.1 Il centro all'infinito

L'affinità è l'omologia con il centro improprio. Si ha quando i due centri di proiezione $S$ e $S_1$ sono allineati lungo una retta parallela al piano: la retta che li unisce non va a un punto di intersezione sul piano a distanza finita.

Il punto di intersezione non si può vedere, perché le due rette sono parallele; ma si incontrano, all'infinito. A dire dov'è il punto è la direzione della retta $SS_1$: il centro dell'omologia è $U_\infty$ e si indica con questa direzione.

Unendo i punti corrispondenti si ottengono rette tutte parallele a quella direzione, perché "passano" tutte per lo stesso centro all'infinito.

#### 5.3.2 Ortogonale e obliqua

L'affinità può essere ortogonale oppure obliqua, e questo dipende dalla posizione dei due centri rispetto all'asse:

- se la direzione è perpendicolare all'asse, l'affinità è ortogonale;
- se è inclinata, l'affinità è obliqua.

Le due proprietà restano quelle dell'omologia, e la soluzione degli esercizi è sempre la stessa.

L'affinità ortogonale servirà nell'assonometria ortogonale, l'obliqua nell'assonometria obliqua. Un'affinità compare anche nel ribaltamento, dove il centro dell'omologia è all'infinito nella direzione perpendicolare all'asse.

> [!example] Disegno 15 · L'affinità ortogonale sul foglio
> ![[b02-affinita-ortogonale-foglio-2.svg|600]]
>
> $U_\infty$ è disegnato con la lineetta della sua direzione, perpendicolare all'asse.
> Le rette $AA'$, $BB'$, $CC'$ sono tutte parallele a quella direzione; i lati corrispondenti si incontrano sull'asse $u$ (cerchietti).
>
> Tutorial con un disegno per ogni passaggio: [[02-affinita-ortogonale-passo-passo|il Disegno 15 passo passo]].

> [!example] Disegno 16 · L'affinità ortogonale nello spazio
> ![[b02-affinita-ortogonale-spazio-2.svg|660]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. $S$ e $S_1$ sono alla stessa altezza: la retta $SS_1$ (rossa) è parallela al foglio e non lo buca mai, quindi il centro è $U_\infty$.
> $S_1$ sta proprio davanti a $S$, nella direzione perpendicolare all'asse: per questo l'affinità è ortogonale.
> Guardando il foglio dall'alto si vede il Disegno 15.

> [!example] Disegno 17 · L'affinità obliqua sul foglio
> ![[b02-affinita-obliqua-foglio-2.svg|600]]
>
> La lineetta di $U_\infty$ è inclinata rispetto all'asse.
> Le rette $AA'$, $BB'$, $CC'$ sono parallele a quella direzione, inclinate; i lati corrispondenti si incontrano sull'asse $u$.

> [!example] Disegno 18 · L'affinità obliqua nello spazio
> ![[b02-affinita-obliqua-spazio-2.svg|660]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. Come nell'affinità ortogonale, $S$ e $S_1$ sono alla stessa altezza e $U$ va all'infinito.
> Questa volta $S_1$ è spostato anche di lato rispetto a $S$: la direzione di $SS_1$, e quindi di $U_\infty$, è inclinata rispetto all'asse.
> Guardando il foglio dall'alto si vede il Disegno 17.

### 5.4 L'omotetia

L'omotetia è l'omologia con il centro proprio e l'asse improprio. Si ha quando il piano che contiene la figura è parallelo al piano su cui la si proietta.

Due piani paralleli si incontrano all'infinito: la retta di intersezione, cioè l'asse, è impropria. Si indica con $u_\infty$ e con una crocetta. Il centro $U$, invece, resta proprio.

Ne viene una conseguenza importante. Le rette corrispondenti si incontrano sull'asse, ma l'asse è all'infinito: quindi le rette corrispondenti sono necessariamente parallele. È questa la differenza fondamentale dell'omotetia.

L'omotetia ingrandisce la figura. È ciò che succede a un rettangolo parallelo alla parete illuminato da una lampada, o alla pianta che si allarga omoteticamente nella prospettiva centrale frontale.

> [!example] Disegno 19 · L'omotetia sul foglio
> ![[b02-omotetia-foglio-2.svg|600]]
>
> L'asse è all'infinito: $u_\infty$ con la crocetta. $A'$, $B'$, $C'$ stanno sui raggi da $U$.
> I lati corrispondenti sono paralleli: $A'B' \parallel AB$, $B'C' \parallel BC$, $C'A' \parallel CA$.

> [!example] Disegno 20 · L'omotetia nello spazio
> ![[b02-omotetia-spazio-2.svg|660]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. Il piano $\alpha_0$, con il triangolo $A_0B_0C_0$, è parallelo al foglio: i due piani non si tagliano, quindi l'asse è $u_\infty$.
> $S$ e $S_1$ sono ad altezze diverse: la retta $SS_1$ (rossa) buca il foglio nel centro $U$, che è proprio.
> $ABC$ e $A'B'C'$ sono due copie di $A_0B_0C_0$ ingrandite in modo diverso, con i lati paralleli.

### 5.5 La traslazione

La traslazione è l'omologia con centro e asse entrambi impropri. È il caso limite, di massima indeterminazione:

- il piano della figura è parallelo al piano su cui si proietta, quindi l'asse è all'infinito ($u_\infty$);
- e anche i due centri di proiezione $S$ e $S_1$ sono allineati parallelamente al piano, quindi il centro dell'omologia è all'infinito ($U_\infty$).

La traslazione è un'isometria, cioè una trasformazione del piano che conserva sia le distanze sia gli angoli: un quadrato rimane un quadrato e il segmento $A'B'$ è uguale al segmento $AB$. La figura viene semplicemente spostata, tale e quale.

Nello spazio si capisce perché la figura resta uguale. Siccome $\alpha_0$ è parallelo al foglio, ciascuna delle due figure proiettate ha i lati paralleli a quelli della figura di partenza. Siccome $S$ e $S_1$ sono alla stessa altezza, i due centri ingrandiscono la figura della stessa quantità, e la retta $AA'$ è parallela a $SS_1$. Per ridisegnarlo a mano si sceglie quindi un solo punto, $A$, sul raggio da $S$; tutti gli altri si trovano con le parallele.

> [!example] Disegno 21 · La traslazione sul foglio
> ![[b02-traslazione-foglio-2.svg|600]]
>
> Centro e asse impropri: $U_\infty$ con la lineetta, $u_\infty$ con la crocetta.
> Tutti i punti si spostano nella direzione di $U_\infty$ della stessa quantità; i lati corrispondenti sono paralleli e uguali.

> [!example] Disegno 22 · La traslazione nello spazio
> ![[b02-traslazione-spazio-2.svg|660]]
>
> Il disegno è una ricostruzione, non è stato fatto a lezione. Il piano $\alpha_0$ è parallelo al foglio, come nell'omotetia: asse $u_\infty$.
> $S$ e $S_1$ sono alla stessa altezza, come nell'affinità: $SS_1$ è parallela al foglio e il centro è $U_\infty$.
> $ABC$ e $A'B'C'$ sono uguali, uno spostato rispetto all'altro.

---

## Collegamenti

Le due proprietà dell'omologia e le condizioni di appartenenza sono gli strumenti con cui si risolvono tutti gli esercizi della bozza [[02-proiezioni-e-omologia-schema|geometria proiettiva e omologia]], che sono l'argomento della prima prova.

Le stesse relazioni tornano più avanti nel corso: l'affinità ortogonale nel [[07-il-ribaltamento|ribaltamento]] delle figure piane e nell'assonometria ortogonale, l'affinità obliqua nell'assonometria obliqua, l'omologia nelle sezioni delle piramidi, l'omotetia nella prospettiva centrale frontale.

Dalla distinzione tra centro proprio e centro improprio nascono i metodi di rappresentazione: le proiezioni cilindriche portano alle [[teoria-proiezioni-ortogonali|proiezioni ortogonali]], dove al posto degli apici si usano i pedici e dove il triedro dei piani $\pi_1$, $\pi_2$, $\pi_3$ diventa il riferimento di tutte le costruzioni ([[03-proiezioni-ortogonali-punto-e-rette]]).
