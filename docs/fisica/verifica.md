# Verifica — Induzione e onde elettromagnetiche

**1. Un filo metallico è ritorto a U, mostrando la concavità verso il basso. A chiudere il circuito c'è una sbarretta metallica che può scorrere senza attrito in verticale. Spiega cosa succede lasciando cadere la sbarretta nel caso in cui il sistema è immerso in un campo magnetico uniforme perpendicolare al piano del circuito.**

Quando si lascia cadere la sbarretta, l'area racchiusa dal circuito aumenta nel tempo, perché la sbarretta si allontana dalla parte alta della U. Di conseguenza aumenta anche il flusso del campo magnetico concatenato al circuito:

\[
\Phi(\vec{B}) = B \cdot L \cdot x(t)
\]

dove \( L \) è la lunghezza della sbarretta e \( x(t) \) la sua posizione. Per la legge di Faraday-Neumann-Lenz una variazione di flusso genera una forza elettromotrice indotta:

\[
f = -\frac{d\Phi}{dt} = -BLv
\]

In modulo vale \( BLv \), e nel circuito di resistenza \( R \) fa scorrere una corrente \( i = BLv/R \). Il verso di questa corrente, per la legge di Lenz, è tale da opporsi alla causa che l'ha generata, quindi crea dentro la spira un campo magnetico opposto a quello esterno. Su una sbarretta percorsa da corrente immersa in un campo magnetico agisce la forza di Laplace \( \vec{F} = i\vec{L} \times \vec{B} \), che in questo caso risulta diretta verso l'alto e quindi frena la caduta. L'equazione del moto è allora:

\[
m\frac{dv}{dt} = mg - \frac{B^2 L^2}{R} v
\]

La sbarretta accelera ma sempre meno, finché la forza frenante eguaglia il peso e si raggiunge una velocità limite costante:

\[
v_\text{lim} = \frac{mgR}{B^2 L^2}
\]

dopo la quale il moto diventa rettilineo uniforme.

**2. Spiega cosa accade in una spira metallica se vicino ad essa sullo stesso piano ne è presente un'altra percorsa da corrente continua. Spiega cosa accade invece se questa seconda spira è percorsa da una corrente alternata.**

Se la seconda spira è percorsa da una corrente continua \( I \) costante, essa genera attorno a sé un campo magnetico anch'esso costante nel tempo. Il flusso di questo campo attraverso la prima spira è dunque costante e la sua derivata temporale è nulla, quindi per Faraday-Neumann-Lenz non viene indotta alcuna forza elettromotrice e nella prima spira non scorre alcuna corrente. Se invece la seconda spira è percorsa da una corrente alternata:

\[
i(t) = I_0 \sin(\omega t)
\]

il campo magnetico che essa produce varia sinusoidalmente nel tempo, e così varia anche il flusso concatenato alla prima spira, che si può scrivere come \( \Phi(t) = M \cdot i(t) \), dove \( M \) è il coefficiente di mutua induzione tra le due spire e dipende solo dalla loro geometria. Nella prima spira nasce allora una forza elettromotrice indotta:

\[
f = -M \frac{di}{dt} = -M I_0 \omega \cos(\omega t)
\]

che fa scorrere una corrente alternata sfasata di 90° rispetto a quella della seconda spira e diretta in modo da opporsi alla variazione di flusso (legge di Lenz). Questo fenomeno di trasferimento di energia da un circuito a un altro senza contatto elettrico, tramite il solo accoppiamento magnetico, è esattamente il principio su cui si basa il trasformatore.

**3. Spiega la legge di Faraday-Neumann-Henry-Lenz nella sua forma integrale spiegando nel dettaglio i suoi elementi, la sua applicazione, le sue implicazioni.**

La legge si esprime nella forma integrale come:

\[
\oint_\gamma \vec{E} \cdot d\vec{l} = -\frac{d}{dt} \int_S \vec{B} \cdot d\vec{S}
\]

e mette in relazione la circuitazione del campo elettrico lungo una linea chiusa \( \gamma \) con la variazione nel tempo del flusso del campo magnetico attraverso una qualunque superficie \( S \) che abbia \( \gamma \) come bordo. Il primo membro rappresenta la forza elettromotrice indotta lungo il circuito, cioè il lavoro che il campo elettrico compie per spostare una carica unitaria lungo l'intera curva; il secondo membro misura quanto rapidamente cambia il numero di linee di campo magnetico che attraversano la superficie. Il segno meno è il contributo di Lenz, che garantisce la conservazione dell'energia: la corrente indotta si dispone sempre in modo da opporsi alla variazione di flusso che l'ha generata. Il flusso può variare in tre modi, anche combinati: può cambiare l'intensità di \( B \), può cambiare l'area della superficie attraversata (come nella sbarretta che cade), oppure può cambiare l'orientamento reciproco tra \( \vec{B} \) e la normale alla superficie (come nelle spire rotanti degli alternatori). L'implicazione concettuale più importante è che un campo magnetico variabile nel tempo genera un campo elettrico, e questo campo elettrico indotto, a differenza di quello elettrostatico, non è conservativo perché ha circuitazione diversa da zero: non deriva quindi da un potenziale. Questa legge è uno dei pilastri delle equazioni di Maxwell ed è alla base di tutta l'industria elettrica, dagli alternatori ai trasformatori, dai motori elettrici alle dinamo.

**4. Un solenoide è percorso da corrente continua, uno identico da corrente alternata. Spiega la differenza tra i fenomeni osservati nei due casi.**

Quando il solenoide è percorso da corrente continua, al suo interno si genera un campo magnetico uniforme e costante:

\[
B = \mu_0 n I
\]

dove \( n \) è il numero di spire per unità di lunghezza. Una volta raggiunto il regime stazionario, il flusso magnetico non varia più nel tempo, quindi non c'è alcun fenomeno di autoinduzione: il solenoide si comporta semplicemente come un filo resistivo, e l'unico effetto della corrente è dissipare energia per effetto Joule. Quando invece il solenoide è percorso da una corrente alternata \( i(t) = I_0 \sin(\omega t) \), il campo magnetico al suo interno varia continuamente e quindi anche il flusso attraverso le sue stesse spire varia: si manifesta il fenomeno dell'autoinduzione, che fa nascere una forza elettromotrice autoindotta:

\[
f_\text{auto} = -L \frac{di}{dt}
\]

dove \( L \) è il coefficiente di autoinduzione del solenoide e dipende dalla sua geometria. Questa forza elettromotrice si oppone alla variazione della corrente, limitandone l'ampiezza: il solenoide si comporta da induttore e introduce una resistenza apparente al passaggio della corrente alternata detta reattanza induttiva \( X_L = \omega L \), che cresce al crescere della frequenza. La corrente che attraversa l'induttore risulta inoltre sfasata di 90° in ritardo rispetto alla tensione applicata. In sintesi, lo stesso oggetto si comporta come un semplice resistore in corrente continua e come un induttore in corrente alternata: la differenza è tutta nella variabilità nel tempo del flusso magnetico.

**5. In un circuito RL sono posti in serie una pila di FEM pari a f, un resistore di resistenza R e un induttore di induttanza L. Spiega cosa accade alla chiusura del circuito.**

Alla chiusura del circuito si applica la legge di Kirchhoff alla maglia, ottenendo l'equazione:

\[
f = R \cdot i + L \frac{di}{dt}
\]

che è un'equazione differenziale lineare del primo ordine nella corrente \( i(t) \). Imponendo la condizione iniziale \( i(0) = 0 \), perché un istante prima della chiusura il circuito era aperto e quindi non scorreva corrente, si trova la soluzione:

\[
i(t) = \frac{f}{R}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac{L}{R}
\]

dove \( \tau \) è la costante di tempo del circuito. Fisicamente, all'istante della chiusura l'induttore non permette alla corrente di crescere bruscamente, perché qualunque variazione rapida farebbe nascere una forza elettromotrice autoindotta enorme che si oppone al cambiamento; quindi la corrente parte da zero e cresce in modo esponenziale, asintoticamente, verso il valore di regime \( I_\infty = f/R \), che è quello che si avrebbe se l'induttore non ci fosse. La costante di tempo \( \tau \) misura quanto è "pigro" il circuito: dopo un tempo pari a \( 5\tau \) la corrente ha praticamente raggiunto il regime. Durante il transitorio l'induttore accumula energia nel proprio campo magnetico, pari a:

\[
U_L = \frac{1}{2} L I^2
\]

che verrà restituita al circuito all'apertura.

**6. Un sasso viene lasciato cadere dal 10mo piano di un palazzo. Sul sasso agiscono la forza peso e la forza d'attrito dell'aria, il cui modulo può essere scritto come il prodotto tra una costante b e la velocità del sasso v. Dimostra che la velocità può essere descritta da una funzione esponenziale particolare, avendo prima descritto l'equazione differenziale che schematizza il problema fisico.**

Sul sasso agiscono due forze: la forza peso \( mg \) diretta verso il basso, e la forza d'attrito viscoso \( -bv \) diretta verso l'alto e proporzionale alla velocità. Applicando la seconda legge di Newton lungo la verticale si ottiene:

\[
m \frac{dv}{dt} = mg - bv
\]

che è un'equazione differenziale lineare del primo ordine nella velocità. Per risolverla osserviamo che esiste una velocità particolare \( v_\text{lim} = mg/b \) per cui l'accelerazione si annulla, perché le due forze si bilanciano: è la velocità limite. Introducendo la variabile ausiliaria \( u = v - v_\text{lim} \) l'equazione diventa:

\[
\frac{du}{dt} = -\frac{b}{m} u
\]

che è l'equazione del decadimento esponenziale e ha soluzione \( u(t) = u_0 e^{-bt/m} \). Imponendo la condizione iniziale \( v(0) = 0 \), cioè \( u_0 = -v_\text{lim} \), si ricava infine la velocità del sasso nel tempo:

\[
v(t) = \frac{mg}{b}\left(1 - e^{-bt/m}\right)
\]

All'inizio, quando \( t \) è piccolo, lo sviluppo dell'esponenziale dà \( v \approx gt \), cioè la caduta libera ordinaria; man mano che il tempo passa la velocità tende asintoticamente a \( v_\text{lim} \), e la caduta diventa uniforme. L'attrito viscoso ha quindi l'effetto di "ammorbidire" la caduta, impedendo alla velocità di crescere indefinitamente come farebbe nel vuoto.

**7. Spiega cosa hanno in comune il problema del sasso in caduta smorzata con la carica e la scarica del condensatore. Imposta il discorso in maniera matematica, facendo un esame della fisica-matematica sottostante questi due problemi, in particolare le equazioni differenziali che li descrivono.**

I due problemi, pur essendo fisicamente diversissimi (uno meccanico, l'altro elettrico), sono descritti dalla stessa identica struttura matematica: un'equazione differenziale lineare del primo ordine a coefficienti costanti. Per il sasso in caduta smorzata vale:

\[
m\frac{dv}{dt} + bv = mg
\]

mentre per la carica di un condensatore in un circuito RC alimentato da una pila di forza elettromotrice \( f \) si ha:

\[
R \frac{dq}{dt} + \frac{q}{C} = f
\]

Riscrivendole nella forma canonica:

\[
\frac{dy}{dt} + \frac{y}{\tau} = K
\]

risulta evidente che entrambe descrivono una grandezza \( y \) che evolve verso un valore di equilibrio \( y_\infty = K\tau \) con una costante di tempo \( \tau \): per il sasso \( \tau = m/b \) e \( y_\infty = v_\text{lim} = mg/b \); per il condensatore \( \tau = RC \) e \( y_\infty = q_\infty = Cf \). La soluzione con condizione iniziale nulla è in entrambi i casi:

\[
y(t) = y_\infty \left(1 - e^{-t/\tau}\right)
\]

Analogamente, la scarica del condensatore (senza pila) è descritta dall'equazione omogenea \( R\,dq/dt + q/C = 0 \) con soluzione \( q(t) = q_0 e^{-t/RC} \), cioè un decadimento esponenziale puro verso lo zero, perfettamente analogo a quello che si avrebbe per il sasso se eliminassimo la gravità. Il significato profondo di questa analogia è che ogni volta che in un sistema fisico esiste un meccanismo dissipativo proporzionale alla grandezza stessa, e una forzante costante, l'evoluzione segue sempre lo stesso schema esponenziale: la matematica unifica fenomeni che a prima vista sembrano scollegati.

**8. Spiega dettagliatamente il funzionamento dei motori elettrici.**

Un motore elettrico è un dispositivo che trasforma energia elettrica in energia meccanica, sfruttando la forza di Laplace su un conduttore percorso da corrente immerso in un campo magnetico. Il cuore del motore è una spira (o un avvolgimento di molte spire) che può ruotare attorno a un asse e che si trova all'interno di un campo magnetico uniforme \( \vec{B} \) generato da magneti permanenti o elettromagneti, detti collettivamente statore. Quando nella spira scorre una corrente \( i \), su ciascuno dei suoi lati agisce una forza di Laplace; le forze sui due lati opposti hanno verso opposto e formano una coppia di forze, cioè un momento meccanico:

\[
|M| = i\, S\, B \sin\theta
\]

dove \( S \) è l'area della spira e \( \theta \) l'angolo tra la normale alla spira e il campo magnetico. Questo momento tende a portare la spira nella posizione in cui la normale è parallela a \( \vec{B} \), cioè la posizione di equilibrio. Il problema è che, una volta raggiunta questa posizione, il momento si annulla e per inerzia la spira la oltrepassa, ma allora il momento agirebbe in senso opposto, generando una semplice oscillazione invece che una rotazione continua. Per risolvere questo problema si utilizza un commutatore a spazzole, un dispositivo meccanico che ogni mezzo giro inverte il verso della corrente nella spira, in modo che il momento agisca sempre nello stesso senso di rotazione. Nei motori reali si usano molte spire avvolte su un nucleo di ferro dolce (rotore) per aumentare il momento, e diversi avvolgimenti sfasati per garantire una rotazione fluida.

**9. Spiega dettagliatamente il funzionamento degli alternatori.**

L'alternatore è la macchina che trasforma energia meccanica in energia elettrica alternata, ed è il principio su cui si basa la quasi totalità della produzione industriale di elettricità. Il suo funzionamento è essenzialmente l'inverso di quello del motore: una spira di area \( S \), o più realisticamente un avvolgimento di \( N \) spire, viene fatta ruotare con velocità angolare costante \( \omega \) all'interno di un campo magnetico uniforme \( \vec{B} \), tipicamente generato dallo statore. Mentre la spira ruota, l'angolo tra la normale alla spira e il campo magnetico cambia secondo la legge \( \theta(t) = \omega t \), e il flusso concatenato vale:

\[
\Phi(t) = B S \cos(\omega t)
\]

Questa variazione del flusso, per la legge di Faraday-Neumann-Lenz, induce nella spira una forza elettromotrice:

\[
f(t) = -\frac{d\Phi}{dt} = B S \omega \sin(\omega t)
\]

che è quindi una funzione sinusoidale del tempo, cioè una tensione alternata di ampiezza \( f_0 = N B S \omega \) e frequenza \( \nu = \omega/(2\pi) \) (in Europa pari a 50 Hz). Per portare la corrente al circuito esterno senza torcere i fili si usano anelli collettori e spazzole striscianti: a differenza del commutatore del motore, gli anelli collettori non invertono mai la corrente, conservando così la sua natura alternata. L'energia meccanica necessaria a far ruotare la spira proviene da una turbina, che a sua volta è azionata da vapore (centrali termiche o nucleari), acqua (centrali idroelettriche) o vento (eolico).

**10. Spiega dettagliatamente il funzionamento dei trasformatori.**

Il trasformatore è un dispositivo che permette di modificare i valori di tensione e corrente di un circuito in corrente alternata, mantenendo idealmente costante la potenza trasmessa, e si basa interamente sul fenomeno dell'induzione mutua. È costituito da due avvolgimenti distinti, un primario di \( N_1 \) spire collegato alla sorgente e un secondario di \( N_2 \) spire collegato al carico, avvolti attorno a uno stesso nucleo di ferro dolce, che ha il compito di convogliare quasi tutte le linee di campo magnetico da un avvolgimento all'altro. Quando il primario è alimentato da una tensione alternata, vi scorre una corrente alternata che genera nel nucleo un flusso magnetico variabile nel tempo \( \Phi(t) \), uguale per ogni spira di entrambi gli avvolgimenti. Per la legge di Faraday-Neumann-Lenz in ciascun avvolgimento nasce una forza elettromotrice indotta proporzionale al numero di spire:

\[
f_1 = -N_1 \frac{d\Phi}{dt}, \qquad f_2 = -N_2 \frac{d\Phi}{dt}
\]

Dividendo membro a membro si ottiene il rapporto di trasformazione:

\[
\frac{V_2}{V_1} = \frac{N_2}{N_1}
\]

che è la relazione fondamentale del trasformatore: se \( N_2 > N_1 \) la tensione viene elevata, se \( N_2 < N_1 \) viene abbassata. In un trasformatore ideale la potenza si conserva, \( V_1 I_1 = V_2 I_2 \), quindi tensione e corrente variano in senso opposto: a una tensione elevata corrisponde una corrente bassa. Questa proprietà è cruciale per il trasporto dell'energia elettrica sulle lunghe distanze, perché lavorare ad alta tensione e bassa corrente minimizza le perdite per effetto Joule sui cavi, che sono proporzionali a \( I^2 R \). È importante sottolineare che il trasformatore funziona soltanto con corrente alternata, perché serve necessariamente una variazione di flusso per indurre forza elettromotrice; con corrente continua, una volta a regime, non funzionerebbe affatto.

**11. Spiega l'origine delle equazioni di Maxwell (eccetto la corrente di spostamento) dichiarando con particolare enfasi il senso fisico di tali equazioni, usando la loro forma integrale.**

Le equazioni di Maxwell sono quattro leggi che racchiudono tutto l'elettromagnetismo classico, ottenute dalla sintesi e dal completamento di leggi sperimentali scoperte nel corso dell'Ottocento. La prima è la legge di Gauss per il campo elettrico:

\[
\oint_S \vec{E} \cdot d\vec{S} = \frac{Q_\text{int}}{\varepsilon_0}
\]

che afferma che il flusso del campo elettrico attraverso una superficie chiusa dipende soltanto dalla carica racchiusa: il senso fisico è che le cariche elettriche sono le sorgenti del campo elettrico, e le sue linee di forza nascono dalle cariche positive e terminano nelle cariche negative. La seconda è la legge di Gauss per il campo magnetico:

\[
\oint_S \vec{B} \cdot d\vec{S} = 0
\]

che afferma che il flusso del campo magnetico attraverso una qualsiasi superficie chiusa è sempre zero: questo significa che non esistono cariche magnetiche isolate, cioè monopoli magnetici, e le linee del campo magnetico sono sempre chiuse su se stesse. La terza è la legge di Faraday-Neumann-Lenz:

\[
\oint_\gamma \vec{E} \cdot d\vec{l} = -\frac{d \Phi_S(\vec{B})}{dt}
\]

che afferma che un campo magnetico variabile nel tempo genera un campo elettrico indotto non conservativo, cioè con circuitazione diversa da zero: è il principio dell'induzione elettromagnetica. La quarta, nella sua forma originaria precedente al contributo di Maxwell, è la legge di Ampère:

\[
\oint_\gamma \vec{B} \cdot d\vec{l} = \mu_0 I_\text{conc}
\]

che afferma che la circuitazione del campo magnetico lungo una linea chiusa è proporzionale alla corrente elettrica concatenata: il senso fisico è che le correnti elettriche sono le sorgenti del campo magnetico. Queste quattro leggi, prese insieme, mostrano una profonda asimmetria tra il campo elettrico (che ha sorgenti, cioè le cariche) e il campo magnetico (che non ne ha), ma anche una connessione profonda perché le correnti elettriche generano \( B \) e i campi magnetici variabili generano \( E \). Sarà l'aggiunta della corrente di spostamento da parte di Maxwell a rompere l'ultima asimmetria e a far emergere le onde elettromagnetiche.

**12. Spiega la struttura dell'equazione delle onde facendo riferimento in particolare agli operatori di derivata parziale nel caso di propagazione nella direzione dell'asse delle x. Dimostra che la funzione A sin(kx ± ωt), con k = 2π/λ e ω = 2π/T, dove λ è la lunghezza d'onda e T il periodo d'oscillazione dei campi, è una soluzione dell'equazione delle onde.**

L'equazione delle onde, nel caso di propagazione lungo l'asse delle \( x \), si scrive:

\[
\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\,\frac{\partial^2 y}{\partial t^2}
\]

dove \( y(x,t) \) è la grandezza che oscilla (può essere lo spostamento di una corda vibrante, la pressione in un fluido, o una componente del campo elettrico per le onde elettromagnetiche) e \( v \) è la velocità di propagazione. Compaiono due derivate parziali seconde, una rispetto allo spazio e una rispetto al tempo: la derivata parziale \( \partial/\partial x \) significa derivare considerando \( t \) come una costante, mentre \( \partial/\partial t \) significa derivare considerando \( x \) costante. La prima misura la "curvatura spaziale" della funzione, la seconda la sua "accelerazione temporale", e l'equazione afferma che le due sono proporzionali. Per dimostrare che \( y(x,t) = A\sin(kx - \omega t) \) è soluzione, calcoliamo le sue derivate parziali rispetto a \( x \):

\[
\frac{\partial y}{\partial x} = A k \cos(kx - \omega t), \qquad \frac{\partial^2 y}{\partial x^2} = -A k^2 \sin(kx - \omega t) = -k^2 y
\]

e rispetto a \( t \):

\[
\frac{\partial y}{\partial t} = -A \omega \cos(kx - \omega t), \qquad \frac{\partial^2 y}{\partial t^2} = -A \omega^2 \sin(kx - \omega t) = -\omega^2 y
\]

Sostituendo nell'equazione delle onde si ha:

\[
-k^2 y = \frac{1}{v^2}(-\omega^2 y) \quad\Longrightarrow\quad v = \frac{\omega}{k}
\]

che è soddisfatta a patto che la velocità di propagazione sia esattamente \( \omega/k \). Ricordando che \( k = 2\pi/\lambda \) e \( \omega = 2\pi/T \), si ottiene la relazione fondamentale:

\[
v = \frac{\omega}{k} = \frac{\lambda}{T} = \lambda \nu
\]

che lega la velocità di propagazione alla lunghezza d'onda e al periodo (o alla frequenza). Il segno meno tra \( kx \) e \( \omega t \) corrisponde a un'onda progressiva che si muove nel verso positivo dell'asse \( x \); con il segno più si avrebbe un'onda regressiva, che si propaga nel verso opposto.

**13. Spiega le caratteristiche generali delle onde elettromagnetiche, con riferimento anche all'energia e all'impulso trasferiti. Spiega inoltre le caratteristiche dello spettro elettromagnetico.**

Le onde elettromagnetiche sono perturbazioni dei campi elettrico e magnetico che si propagano nello spazio anche in assenza di un mezzo materiale, e nascono come conseguenza diretta delle equazioni di Maxwell completate dalla corrente di spostamento. Si tratta di onde trasversali, in cui \( \vec{E} \) e \( \vec{B} \) oscillano perpendicolarmente alla direzione di propagazione e perpendicolarmente tra loro, formando una terna ortogonale destrorsa con il vettore velocità. Nel vuoto si propagano tutte con la stessa velocità:

\[
c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}} \approx 3 \cdot 10^8 \text{ m/s}
\]

e in ogni punto e istante il modulo del campo elettrico e quello del campo magnetico sono legati dalla relazione \( E = cB \). Le onde elettromagnetiche trasportano energia e impulso: la densità di energia istantanea è equamente divisa tra il contributo elettrico e quello magnetico e vale complessivamente:

\[
u = \varepsilon_0 E^2
\]

mentre l'intensità, cioè la potenza media per unità di area, è:

\[
I = \frac{1}{2} c \varepsilon_0 E_0^2
\]

dove \( E_0 \) è l'ampiezza. Trasportando impulso, le onde elettromagnetiche esercitano sulle superfici che colpiscono una pressione di radiazione, pari a \( I/c \) se la superficie è assorbente e \( 2I/c \) se è perfettamente riflettente: è un effetto piccolo ma reale, sfruttato per esempio nelle vele solari. Le onde elettromagnetiche si differenziano per frequenza, e l'insieme delle frequenze possibili costituisce lo spettro elettromagnetico, che si estende continuamente dalle onde radio (frequenze inferiori a \( 10^9 \) Hz, usate per radio e televisione), alle microonde (forni e wi-fi), all'infrarosso (calore e telecomandi), alla luce visibile (una banda strettissima tra circa 400 e 700 nm), all'ultravioletto, fino ai raggi X delle radiografie e ai raggi gamma emessi dai nuclei atomici e dai fenomeni astrofisici più violenti. Tutte queste radiazioni sono fisicamente lo stesso tipo di onda, e differiscono soltanto per la lunghezza d'onda \( \lambda = c/\nu \).

**14. Spiega il fenomeno della polarizzazione delle onde elettromagnetiche. Spiega cosa sono e come funzionano i filtri polaroid. Enuncia e spiega inoltre il meccanismo della polarizzazione parziale e totale di un'onda elettromagnetica incidente sulla superficie di separazione tra due mezzi trasparenti.**

Un'onda elettromagnetica si dice polarizzata linearmente quando il suo campo elettrico \( \vec{E} \) oscilla sempre nella stessa direzione, detta direzione di polarizzazione, perpendicolare alla direzione di propagazione. La luce emessa da sorgenti naturali come il Sole o una lampadina è invece non polarizzata, perché è la sovrapposizione di moltissime onde con orientazioni di \( \vec{E} \) distribuite casualmente in tutte le direzioni del piano perpendicolare alla propagazione. Un filtro polaroid è una sottile lamina costituita da molecole allineate che si comporta come una "fessura" per il campo elettrico: lascia passare soltanto la componente di \( \vec{E} \) parallela al proprio asse di trasmissione, assorbendo quella perpendicolare. Una luce non polarizzata che attraversa un polaroid esce polarizzata linearmente con intensità dimezzata; se poi questa luce polarizzata incontra un secondo polaroid orientato a un angolo \( \theta \) rispetto al primo, l'intensità trasmessa segue la legge di Malus:

\[
I = I_0 \cos^2 \theta
\]

e in particolare si annulla quando i due polaroid hanno gli assi perpendicolari. Anche la riflessione su una superficie tra due mezzi trasparenti, come ad esempio aria e vetro, produce un'onda riflessa parzialmente polarizzata: la componente di \( \vec{E} \) parallela alla superficie viene riflessa più efficacemente di quella nel piano d'incidenza, perché le due interagiscono in modo diverso con gli elettroni del mezzo. Esiste inoltre un particolare angolo d'incidenza, detto angolo di Brewster, definito dalla legge:

\[
\tan \theta_B = \frac{n_2}{n_1}
\]

per cui la luce riflessa risulta totalmente polarizzata, con \( \vec{E} \) parallelo alla superficie; a questo angolo, il raggio riflesso e quello rifratto risultano esattamente perpendicolari tra loro. Su questo principio si basano gli occhiali da sole polarizzati e i filtri fotografici, che eliminano selettivamente i riflessi orizzontali da specchi d'acqua, asfalto bagnato o vetrine.

## Collegamenti

- **Matematica — Equazioni differenziali**: i circuiti RL e RC e la caduta smorzata si descrivono con equazioni differenziali lineari del primo ordine; l'equazione delle onde è del secondo ordine alle derivate parziali.
- **Matematica — Funzioni esponenziali e trigonometriche**: le soluzioni dei transitori sono esponenziali, quelle delle onde sono sinusoidali.
- **Storia — Seconda rivoluzione industriale**: alternatori, motori e trasformatori sono alla base dell'elettrificazione di fine Ottocento.
- **Filosofia — Positivismo**: la sintesi di Maxwell è un trionfo della razionalità scientifica nell'unificare fenomeni apparentemente distinti come elettricità, magnetismo e luce.
