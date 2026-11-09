---
tipo: bozza
corso: Matematica
anno: 1
semestre: 1
tags: [matematica, bozza]
---

# Geometria del piano: la retta e la circonferenza

La geometria analitica traduce le figure in numeri e in equazioni. Un punto diventa una coppia di numeri, una retta diventa un'equazione di primo grado, una circonferenza un'equazione di secondo grado. Il vantaggio è che domande geometriche ("queste due rette si incontrano?", "questa retta tocca il cerchio?") si risolvono con i conti, cioè con le equazioni e i sistemi studiati nella pagina precedente. Lo strumento che regge tutto è uno solo: la distanza tra due punti, ricavata dal teorema di Pitagora.

> [!info] Note collegate
> Teoria: [[01-insiemi-e-intervalli]] · [[02-equazioni-e-disequazioni]] · [[04-le-matrici]] · [[05-i-vettori]] · [[06-le-funzioni]] · Ripasso: [[00-ripasso-esonero-1]]

## IL PIANO CARTESIANO E LA DISTANZA

### Coordinate e quadranti

Il piano cartesiano si costruisce con due rette perpendicolari, gli assi.

- L'asse orizzontale è l'asse $x$ (asse delle *ascisse*).
- L'asse verticale è l'asse $y$ (asse delle *ordinate*).
- Il punto in cui si incrociano è l'*origine* $O$.

Su ciascun asse si fissa la stessa unità di misura. A destra dell'origine le $x$ sono positive, a sinistra negative; in alto le $y$ sono positive, in basso negative.

Ogni punto $P$ del piano si individua con due numeri, le sue *coordinate* $P(x, y)$. Per trovarle si proietta il punto sui due assi con due segmenti perpendicolari: il primo numero è dove cade la proiezione sull'asse $x$, il secondo dove cade quella sull'asse $y$. L'ordine conta: $(3, 2)$ e $(2, 3)$ sono due punti diversi.

![[03-piano-cartesiano.svg|500]]

Gli assi dividono il piano in quattro *quadranti*, numerati in senso antiorario a partire da quello in alto a destra. Il segno delle coordinate dice subito in quale quadrante sta un punto:

1. I quadrante: $x > 0$, $y > 0$.
2. II quadrante: $x < 0$, $y > 0$.
3. III quadrante: $x < 0$, $y < 0$.
4. IV quadrante: $x > 0$, $y < 0$.

I punti sugli assi non stanno in nessun quadrante: sull'asse $x$ hanno $y = 0$, sull'asse $y$ hanno $x = 0$.

### Il valore assoluto come distanza

Prima di misurare distanze nel piano conviene guardare la retta dei numeri, che è un asse solo.

> [!abstract] Valore assoluto
> Il *valore assoluto* di un numero $a$ è il numero stesso senza il segno:
> $$
> |a| = \begin{cases} a & \text{se } a \geq 0 \\ -a & \text{se } a < 0 \end{cases}
> $$
> Geometricamente, $|a|$ è la distanza di $a$ da $0$ sulla retta dei numeri, e $|a - b|$ è la distanza tra i numeri $a$ e $b$.

Per esempio $|-4| = 4$, perché $-4$ dista 4 passi da zero. E $|5 - 2| = |2 - 5| = 3$: la distanza tra 2 e 5 non dipende dall'ordine in cui li si prende.

Il "meno" della definizione spaventa, ma serve proprio a togliere il segno: se $a = -4$, allora $-a = -(-4) = 4$.

![[03-valore-assoluto-distanza.svg|600]]

Leggere il valore assoluto come distanza rende facili le disequazioni. $|x| < 3$ chiede "quali numeri distano da 0 meno di 3?", e la risposta si vede sulla retta: quelli tra $-3$ e $3$.

> [!example] Esempio: $|x - 2| < 3$
> La domanda è: quali numeri distano da 2 meno di 3?
> 1. Da 2 si va 3 passi a sinistra: si arriva a $-1$.
> 2. Da 2 si va 3 passi a destra: si arriva a $5$.
> 3. I numeri cercati sono quelli in mezzo: $-1 < x < 5$.
>
> Con l'algebra si arriva allo stesso punto: $|x - 2| < 3$ equivale a $-3 < x - 2 < 3$, e aggiungendo 2 a tutti i membri si ottiene $-1 < x < 5$.

### La distanza tra due punti

Per due punti sullo stesso asse basta il valore assoluto. Per due punti qualsiasi del piano, $A(x_A, y_A)$ e $B(x_B, y_B)$, si usa un triangolo rettangolo.

Il trucco è questo: da $A$ si va in orizzontale fino a sotto $B$, poi si sale in verticale fino a $B$. Si è disegnato un triangolo rettangolo in cui:

- il cateto orizzontale misura $|x_B - x_A|$ (quanto cambia la $x$);
- il cateto verticale misura $|y_B - y_A|$ (quanto cambia la $y$);
- l'ipotenusa è proprio il segmento $AB$.

Per il teorema di Pitagora l'ipotenusa al quadrato è la somma dei quadrati dei cateti. Quando si eleva al quadrato il segno sparisce, quindi i valori assoluti non servono più.

![[03-distanza-pitagora.svg|480]]

> [!abstract] Distanza tra due punti
> $$
> d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}
> $$
> È il teorema di Pitagora applicato al triangolo che ha per cateti le differenze delle coordinate.

Le differenze si scrivono spesso con la lettera greca $\Delta$ ("delta"), che si legge "variazione di": $\Delta x = x_B - x_A$ e $\Delta y = y_B - y_A$. Con questa notazione $d = \sqrt{\Delta x^2 + \Delta y^2}$.

> [!example] Esempio (esercizio 14 del foglio sui vettori): distanza tra $A(1, -1)$ e $B(5, 1)$
> 1. $\Delta x = 5 - 1 = 4$.
> 2. $\Delta y = 1 - (-1) = 2$.
> 3. $d(A, B) = \sqrt{4^2 + 2^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5} \approx 4{,}47$.
>
> Per semplificare la radice: $20 = 4 \cdot 5$, quindi $\sqrt{20} = \sqrt{4}\cdot\sqrt{5} = 2\sqrt{5}$.

> [!warning] Attenzione ai segni
> L'errore più frequente è sbagliare la sottrazione con i numeri negativi: $1 - (-1) = 1 + 1 = 2$, non $0$. Mettere sempre le parentesi intorno alle coordinate negative.

### Il punto medio di un segmento

Il *punto medio* $M$ di un segmento $AB$ è il punto che sta esattamente a metà. Le sue coordinate sono la media delle coordinate degli estremi: la $x$ di $M$ è a metà strada tra $x_A$ e $x_B$, e lo stesso per la $y$.

> [!abstract] Punto medio
> $$
> M = \left( \frac{x_A + x_B}{2}, \; \frac{y_A + y_B}{2} \right)
> $$

![[03-punto-medio.svg|480]]

> [!example] Esempio: punto medio di $A(1, -1)$ e $B(5, 1)$
> $$
> M = \left( \frac{1 + 5}{2}, \frac{-1 + 1}{2} \right) = (3, 0)
> $$
> Verifica: $d(A, M) = \sqrt{2^2 + 1^2} = \sqrt{5}$ e $d(M, B) = \sqrt{2^2 + 1^2} = \sqrt{5}$. Le due metà sono uguali, e ciascuna è metà di $2\sqrt{5}$.

### Coordinate e distanza nello spazio

Il programma del corso chiede anche le coordinate nello spazio. L'idea è la stessa, con un asse in più.

Nello spazio si usano tre assi perpendicolari tra loro: $x$, $y$ e $z$ (l'asse $z$ è la quota, verso l'alto). Ogni punto ha tre coordinate, $P(x, y, z)$. I tre assi a due a due individuano tre *piani coordinati*: il piano $xy$ (dove $z = 0$, il "pavimento"), il piano $xz$ (dove $y = 0$) e il piano $yz$ (dove $x = 0$).

Per la distanza si usa Pitagora due volte. Si guardi la figura: dall'origine $O$ al punto $P$.

1. Prima si cammina sul pavimento da $O$ fino a $H(x, y, 0)$, il punto proprio sotto $P$. Sul pavimento vale la formula del piano: $OH = \sqrt{x^2 + y^2}$.
2. Poi si sale in verticale da $H$ a $P$, per un tratto lungo $z$.
3. Il triangolo $OHP$ è rettangolo in $H$, quindi $OP^2 = OH^2 + z^2 = x^2 + y^2 + z^2$.

![[03-coordinate-spazio.svg|520]]

> [!abstract] Distanza nello spazio
> $$
> d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}
> $$
> Rispetto al piano si aggiunge solo il quadrato della differenza delle quote.

> [!example] Esempio: distanza tra $A(1, 2, -1)$ e $B(3, 0, 0)$
> $$
> d = \sqrt{(3-1)^2 + (0-2)^2 + (0-(-1))^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3
> $$

Chi ha studiato il metodo di Monge in Geometria descrittiva riconoscerà la situazione: il punto $H$ è la proiezione di $P$ sul piano orizzontale, e $z$ è la sua quota.

## LA RETTA

### La pendenza (coefficiente angolare)

Una retta non verticale ha una sua inclinazione costante: ovunque la si guardi, sale (o scende) sempre allo stesso modo. Questa inclinazione si misura con un numero, la *pendenza* o *coefficiente angolare*, che si indica con $m$.

Si prendono due punti qualsiasi della retta, $A$ e $B$, e si guarda di quanto si sale ($\Delta y$) mentre ci si sposta in orizzontale ($\Delta x$).

> [!abstract] Pendenza di una retta
> Se $A(x_A, y_A)$ e $B(x_B, y_B)$ sono due punti della retta, con $x_A \neq x_B$:
> $$
> m = \frac{\Delta y}{\Delta x} = \frac{y_B - y_A}{x_B - x_A}
> $$
> La pendenza dice di quanto sale la retta per ogni passo di 1 verso destra.

Perché il risultato non dipende da quali due punti si scelgono? Perché i triangoli rettangoli costruiti su punti diversi della stessa retta sono tutti simili (hanno gli stessi angoli), quindi il rapporto tra cateto verticale e cateto orizzontale è sempre lo stesso.

![[03-pendenza.svg|500]]

C'è anche una lettura con gli angoli. Sia $\alpha$ l'angolo che la retta forma con il verso positivo dell'asse $x$. Nel triangolo rettangolo della figura, il cateto opposto ad $\alpha$ è $\Delta y$ e il cateto adiacente è $\Delta x$. Il loro rapporto è, per definizione, la tangente dell'angolo.

> [!abstract] Pendenza e angolo
> $$
> m = \operatorname{tg} \alpha
> $$
> dove $\alpha$ è l'angolo tra la retta e il verso positivo dell'asse $x$, misurato in senso antiorario.

> [!example] Esempio: pendenza della retta per $A(1, 1)$ e $B(6, 4)$
> 1. $\Delta y = 4 - 1 = 3$.
> 2. $\Delta x = 6 - 1 = 5$.
> 3. $m = \dfrac{3}{5} = 0{,}6$.
>
> La retta sale di 3 ogni 5 passi verso destra, cioè di $0{,}6$ per ogni passo. L'angolo con l'asse $x$ è $\alpha = \operatorname{arctg}(0{,}6) \approx 31°$.

Il segno e la grandezza di $m$ si leggono direttamente nel disegno:

- $m > 0$: la retta sale andando verso destra;
- $m < 0$: la retta scende andando verso destra;
- $m = 0$: la retta è orizzontale;
- più $|m|$ è grande, più la retta è ripida.

![[03-pendenze-confronto.svg|480]]

### Un esempio di architettura: la pendenza di una rampa

In architettura la pendenza si usa tutti i giorni, ma di solito si scrive in percentuale. Una pendenza dell'8% vuol dire $m = 0{,}08$: si sale di 8 cm ogni metro (100 cm) percorso in pianta.

![[03-rampa.svg|620]]

Le norme sull'accessibilità per le persone in carrozzina fissano di solito per le rampe una pendenza massima dell'8%. La formula della pendenza permette di calcolare quanto deve essere lunga la rampa.

> [!example] Esempio: quanto è lunga una rampa all'8%?
> Bisogna superare un dislivello di 60 cm con una pendenza dell'8%.
> 1. Si scrive la pendenza: $m = \dfrac{\Delta y}{\Delta x}$, cioè $0{,}08 = \dfrac{0{,}60}{\Delta x}$.
> 2. Si ricava $\Delta x$: $\Delta x = \dfrac{0{,}60}{0{,}08} = 7{,}5$ m.
>
> Servono 7,5 m in pianta. L'angolo è piccolo: $\alpha = \operatorname{arctg}(0{,}08) \approx 4{,}6°$. La rampa del disegno, che sale di 1 m in 12 m, ha pendenza $1/12 \approx 8{,}3\%$: di poco troppo ripida.

### L'equazione della retta: forma esplicita e forma implicita

Una retta è un insieme di infiniti punti. La sua *equazione* è una condizione su $x$ e $y$ che è vera per i punti della retta e falsa per tutti gli altri. Un punto sta sulla retta se, sostituendo le sue coordinate nell'equazione, si ottiene un'uguaglianza vera.

> [!abstract] Forma esplicita
> Ogni retta non verticale ha un'equazione del tipo
> $$
> y = mx + q
> $$
> - $m$ è la pendenza;
> - $q$ è l'*ordinata all'origine*: il valore di $y$ quando $x = 0$, cioè il punto $(0, q)$ in cui la retta taglia l'asse $y$.

Perché proprio questa forma? Si parte dal punto $(0, q)$ sull'asse $y$. Spostandosi di $x$ verso destra, la retta sale di $m$ per ogni passo, quindi di $m \cdot x$ in tutto. L'altezza raggiunta è $q + mx$.

Rette con la stessa $m$ e $q$ diversa sono parallele: hanno la stessa inclinazione e sono solo spostate in alto o in basso.

![[03-ruolo-di-q.svg|480]]

> [!abstract] Forma implicita
> Ogni retta del piano, comprese quelle verticali, ha un'equazione del tipo
> $$
> ax + by + c = 0
> $$
> con $a$ e $b$ non entrambi nulli. Se $b \neq 0$ si può passare alla forma esplicita ricavando $y$:
> $$
> y = -\frac{a}{b}\,x - \frac{c}{b} \qquad \text{quindi} \qquad m = -\frac{a}{b}, \quad q = -\frac{c}{b}
> $$

> [!example] Esempio: da implicita a esplicita
> Retta $2x + 3y - 6 = 0$.
> 1. Si porta tutto tranne $3y$ a destra: $3y = -2x + 6$.
> 2. Si divide per 3: $y = -\dfrac{2}{3}x + 2$.
> 3. Quindi $m = -\dfrac{2}{3}$ (la retta scende) e $q = 2$ (taglia l'asse $y$ in $(0, 2)$).
>
> Il punto $(3, 0)$ sta sulla retta? $2 \cdot 3 + 3 \cdot 0 - 6 = 0$: sì. Il punto $(1, 1)$? $2 + 3 - 6 = -1 \neq 0$: no.

### Rette orizzontali e verticali

Due casi particolari vanno riconosciuti al volo.

- Una retta orizzontale ha tutti i punti alla stessa altezza $k$: la sua equazione è $y = k$. La pendenza è $m = 0$, perché $\Delta y = 0$. L'asse $x$ stesso è la retta $y = 0$.
- Una retta verticale ha tutti i punti con la stessa ascissa $h$: la sua equazione è $x = h$. Qui $\Delta x = 0$ e la frazione $\Delta y / \Delta x$ non si può calcolare (non si divide per zero): la pendenza non è definita. L'asse $y$ è la retta $x = 0$.

![[03-orizzontali-verticali.svg|480]]

> [!warning] La retta verticale non ha forma esplicita
> $x = -3$ non si può scrivere come $y = mx + q$, perché nell'equazione la $y$ non compare. Per questo la forma implicita è più generale: $x = -3$ diventa $1 \cdot x + 0 \cdot y + 3 = 0$.

### La retta per un punto con pendenza data

Spesso si conosce un punto $P_0(x_0, y_0)$ della retta e la sua pendenza $m$. Per ogni altro punto $(x, y)$ della retta, la pendenza calcolata tra $P_0$ e $(x, y)$ deve valere $m$:
$$
\frac{y - y_0}{x - x_0} = m
$$
Moltiplicando per $x - x_0$ si ottiene la formula.

> [!abstract] Retta per un punto con pendenza $m$
> $$
> y - y_0 = m\,(x - x_0)
> $$

> [!example] Esempio: retta per $P_0(2, 3)$ con pendenza $m = -\frac{1}{2}$
> 1. Si sostituisce: $y - 3 = -\dfrac{1}{2}(x - 2)$.
> 2. Si svolge: $y - 3 = -\dfrac{1}{2}x + 1$.
> 3. Si ricava $y$: $y = -\dfrac{1}{2}x + 4$.
>
> Verifica: per $x = 2$ si ha $y = -1 + 4 = 3$. Il punto $P_0$ sta sulla retta.

### La retta per due punti

Per due punti distinti passa una e una sola retta. Per trovarne l'equazione si combinano le due formule precedenti: prima si calcola la pendenza con i due punti, poi si usa uno dei due punti.

> [!abstract] Retta per due punti $A(x_A, y_A)$ e $B(x_B, y_B)$
> Procedimento in due passi:
> 1. $m = \dfrac{y_B - y_A}{x_B - x_A}$;
> 2. $y - y_A = m\,(x - x_A)$.
>
> Mettendo insieme i due passi si ottiene la formula in un colpo solo (valida se $x_A \neq x_B$ e $y_A \neq y_B$):
> $$
> \frac{y - y_A}{y_B - y_A} = \frac{x - x_A}{x_B - x_A}
> $$
> Se $x_A = x_B$ la retta è verticale, $x = x_A$; se $y_A = y_B$ è orizzontale, $y = y_A$.

> [!example] Esempio: retta per $A(1, -1)$ e $B(5, 1)$
> 1. Pendenza: $m = \dfrac{1 - (-1)}{5 - 1} = \dfrac{2}{4} = \dfrac{1}{2}$.
> 2. Retta per $A$: $y - (-1) = \dfrac{1}{2}(x - 1)$, cioè $y + 1 = \dfrac{1}{2}x - \dfrac{1}{2}$.
> 3. Si ricava $y$: $y = \dfrac{1}{2}x - \dfrac{3}{2}$.
> 4. Verifica con $B$: $\dfrac{1}{2}\cdot 5 - \dfrac{3}{2} = \dfrac{5 - 3}{2} = 1$. Giusto.
>
> In forma implicita (si moltiplica tutto per 2 e si porta a sinistra): $x - 2y - 3 = 0$.

![[03-retta-due-punti.svg|500]]

La verifica finale con il secondo punto è un'abitudine da prendere: costa pochi secondi e scopre quasi tutti gli errori di segno.

### Rette parallele e rette perpendicolari

Due rette parallele hanno la stessa inclinazione, quindi la stessa pendenza. Per le perpendicolari la regola è meno ovvia: il prodotto delle pendenze vale $-1$.

> [!abstract] Parallelismo e perpendicolarità
> Siano $r: y = m_1 x + q_1$ e $s: y = m_2 x + q_2$.
> - $r$ e $s$ sono parallele se e solo se $m_1 = m_2$.
> - $r$ e $s$ sono perpendicolari se e solo se $m_1 \cdot m_2 = -1$, cioè $m_2 = -\dfrac{1}{m_1}$.
>
> La pendenza della perpendicolare è l'opposto del reciproco: si capovolge la frazione e si cambia il segno. Per esempio la perpendicolare a una retta di pendenza $2$ ha pendenza $-\frac{1}{2}$.

![[03-parallele-perpendicolari.svg|480]]

Perché $-1$? Si prende la retta di pendenza $m$ passante per l'origine e il triangolo che ha per cateti 1 (in orizzontale) e $m$ (in verticale): arriva al punto $(1, m)$. Si ruota tutto il triangolo di 90° in senso antiorario. Il cateto orizzontale lungo 1 diventa verticale, quello verticale lungo $m$ diventa orizzontale e punta a sinistra: il punto $(1, m)$ va in $(-m, 1)$. La retta ruotata è perpendicolare alla prima e la sua pendenza è
$$
\frac{\Delta y}{\Delta x} = \frac{1}{-m} = -\frac{1}{m}.
$$
Moltiplicando le due pendenze: $m \cdot \left(-\frac{1}{m}\right) = -1$.

![[03-perpendicolari-perche.svg|480]]

> [!example] Esempio: parallela e perpendicolare per un punto
> Data $r: y = 2x + 1$ e il punto $P(1, 2)$, trovare la parallela e la perpendicolare a $r$ passanti per $P$.
> 1. Parallela: stessa pendenza $m = 2$. $y - 2 = 2(x - 1)$, cioè $y = 2x$.
> 2. Perpendicolare: pendenza $m = -\dfrac{1}{2}$. $y - 2 = -\dfrac{1}{2}(x - 1)$, cioè $y = -\dfrac{1}{2}x + \dfrac{5}{2}$.
>
> Controllo: $2 \cdot \left(-\dfrac{1}{2}\right) = -1$.

> [!warning] Casi da tenere a parte
> La regola $m_1 m_2 = -1$ non vale se una delle due rette è verticale (non ha pendenza). Una retta orizzontale $y = k$ e una verticale $x = h$ sono comunque perpendicolari.
>
> Con le rette in forma implicita $a_1x + b_1y + c_1 = 0$ e $a_2x + b_2y + c_2 = 0$ la condizione di perpendicolarità si scrive $a_1a_2 + b_1b_2 = 0$, e vale in tutti i casi. È un prodotto scalare: si ritrova nella pagina [[05-i-vettori]].

### L'intersezione di due rette

Il punto in cui due rette si incontrano deve stare su entrambe, quindi le sue coordinate devono soddisfare tutte e due le equazioni nello stesso momento. Trovarlo vuol dire risolvere il sistema delle due equazioni.

> [!abstract] Intersezione di due rette
> Il punto di intersezione di $r$ e $s$ è la soluzione del sistema
> $$
> \begin{cases} a_1x + b_1y + c_1 = 0 \\ a_2x + b_2y + c_2 = 0 \end{cases}
> $$
> Ci sono tre casi possibili:
> 1. una sola soluzione: le rette sono *incidenti* e si incontrano in un punto;
> 2. nessuna soluzione (il sistema è impossibile): le rette sono parallele e distinte;
> 3. infinite soluzioni: le due equazioni descrivono la stessa retta (rette *coincidenti*).

> [!example] Esempio: intersezione di $x + y = 5$ e $2x - y = 1$
> 1. Si sommano le due equazioni membro a membro: la $y$ si cancella e resta $3x = 6$, quindi $x = 2$.
> 2. Si sostituisce nella prima: $2 + y = 5$, quindi $y = 3$.
> 3. Il punto di intersezione è $P(2, 3)$.
>
> Verifica nella seconda: $2 \cdot 2 - 3 = 1$. Giusto.

![[03-intersezione.svg|460]]

### La distanza di un punto da una retta

La distanza di un punto $P$ da una retta $r$ è la lunghezza del segmento più corto che li unisce. Il segmento più corto è quello perpendicolare alla retta: il suo estremo $H$ sulla retta si chiama *piede della perpendicolare*.

Per calcolarla ci sono due strade.

1. La strada lunga, geometrica: si scrive la perpendicolare a $r$ passante per $P$, la si interseca con $r$ per trovare $H$, poi si calcola la distanza $PH$ con la formula di Pitagora.
2. La strada breve: una formula che fa tutti questi passaggi in una volta.

> [!abstract] Distanza punto-retta
> La distanza del punto $P(x_0, y_0)$ dalla retta $ax + by + c = 0$ è
> $$
> d(P, r) = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}
> $$
> La retta va scritta in forma implicita. Al numeratore si sostituiscono le coordinate di $P$ nell'equazione della retta, e si prende il valore assoluto perché una distanza non è mai negativa.

Il numeratore vale zero esattamente quando $P$ sta sulla retta: in quel caso la distanza è zero, come deve essere.

> [!example] Esempio (esercizio 22 del foglio sui vettori): distanza di $P(4, 1)$ dalla retta per $A(1, 0)$ con direzione $(1, 2)$
> La retta va da $A(1, 0)$ nella direzione $(1, 2)$: a ogni passo a destra sale di 2, quindi $m = 2$. Equazione: $y = 2(x - 1)$, cioè $2x - y - 2 = 0$.
>
> Con la formula ($a = 2$, $b = -1$, $c = -2$):
> $$
> d = \frac{|2 \cdot 4 - 1 - 2|}{\sqrt{4 + 1}} = \frac{5}{\sqrt{5}} = \sqrt{5}
> $$
>
> Con la strada geometrica:
> 1. Perpendicolare per $P$: pendenza $-\frac{1}{2}$, quindi $y - 1 = -\frac{1}{2}(x - 4)$, cioè $y = -\frac{1}{2}x + 3$.
> 2. Intersezione con $y = 2x - 2$: $2x - 2 = -\frac{1}{2}x + 3$, cioè $\frac{5}{2}x = 5$, $x = 2$, $y = 2$. Il piede è $H(2, 2)$.
> 3. $d(P, H) = \sqrt{(4-2)^2 + (1-2)^2} = \sqrt{4 + 1} = \sqrt{5}$.
>
> Le due strade danno lo stesso risultato. Nell'esercizio il professore chiede di trovare $H$ con i vettori: si ritrova lo stesso punto nella pagina [[05-i-vettori]].

![[03-distanza-punto-retta.svg|460]]

## LA CIRCONFERENZA

### Definizione ed equazione

> [!abstract] Circonferenza
> La *circonferenza* di centro $C$ e raggio $r > 0$ è l'insieme di tutti i punti del piano che hanno distanza $r$ da $C$.

Un insieme di punti definito da una proprietà si chiama *luogo geometrico*: la circonferenza è il luogo dei punti equidistanti dal centro. Questa definizione si traduce subito in equazione con la formula della distanza.

Sia $C(x_0, y_0)$ il centro e $P(x, y)$ un punto qualsiasi. $P$ sta sulla circonferenza se e solo se $d(P, C) = r$, cioè
$$
\sqrt{(x - x_0)^2 + (y - y_0)^2} = r.
$$
Entrambi i membri sono positivi, quindi si può elevare al quadrato senza perdere né aggiungere soluzioni.

![[03-circonferenza-definizione.svg|460]]

> [!abstract] Equazione della circonferenza di centro $C(x_0, y_0)$ e raggio $r$
> $$
> (x - x_0)^2 + (y - y_0)^2 = r^2
> $$
> Se il centro è l'origine diventa $x^2 + y^2 = r^2$.
>
> Molti libri chiamano il centro $(a, b)$ e scrivono $(x - a)^2 + (y - b)^2 = r^2$: è la stessa formula con altre lettere.

Nella figura si vede che l'equazione è di nuovo il teorema di Pitagora: i cateti sono $x - x_0$ e $y - y_0$, l'ipotenusa è il raggio.

> [!warning] Il segno dentro le parentesi
> Nell'equazione compare un "meno": $(x - x_0)$. Se il centro ha una coordinata negativa il segno si inverte. Il centro $(2, -1)$ dà $(x - 2)^2 + (y + 1)^2$, perché $y - (-1) = y + 1$. Al contrario, leggendo $(x + 3)^2$ il centro ha $x_0 = -3$.

### La forma sviluppata e come risalire al centro e al raggio

Se si svolgono i quadrati nell'equazione della circonferenza si ottiene un'equazione con $x^2$, $y^2$, termini di primo grado e un numero.

> [!example] Esempio: sviluppare la circonferenza di centro $C(2, -1)$ e raggio $3$
> 1. Equazione: $(x - 2)^2 + (y + 1)^2 = 9$.
> 2. Si svolgono i quadrati: $x^2 - 4x + 4 + y^2 + 2y + 1 = 9$.
> 3. Si porta tutto a sinistra e si ordina: $x^2 + y^2 - 4x + 2y - 4 = 0$.

![[03-circonferenza-esempio.svg|440]]

> [!abstract] Forma sviluppata
> Ogni circonferenza ha un'equazione del tipo
> $$
> x^2 + y^2 + ax + by + c = 0
> $$
> dove $x^2$ e $y^2$ hanno coefficiente 1 e non c'è il termine $xy$. Centro e raggio si leggono così:
> $$
> C = \left( -\frac{a}{2}, \; -\frac{b}{2} \right), \qquad r = \sqrt{\frac{a^2}{4} + \frac{b^2}{4} - c}
> $$
> L'equazione rappresenta una circonferenza solo se il numero sotto la radice è positivo: $\dfrac{a^2}{4} + \dfrac{b^2}{4} - c > 0$.

Le formule non vanno imparate a memoria a tutti i costi: si ricavano con il *completamento dei quadrati*. L'idea è riconoscere in $x^2 + ax$ l'inizio del quadrato di un binomio. Siccome $(x + k)^2 = x^2 + 2kx + k^2$, per avere $x^2 + ax$ serve $2k = a$, cioè $k = a/2$; manca solo il termine $k^2$, che si aggiunge e si toglie.

> [!example] Esempio: centro e raggio di $x^2 + y^2 + 6x - 8y + 9 = 0$
> Metodo del completamento dei quadrati:
> 1. Si raggruppano i termini in $x$ e quelli in $y$: $(x^2 + 6x) + (y^2 - 8y) = -9$.
> 2. Per $x^2 + 6x$: la metà di 6 è 3, e $3^2 = 9$. Si aggiunge 9 a entrambi i membri.
> 3. Per $y^2 - 8y$: la metà di $-8$ è $-4$, e $(-4)^2 = 16$. Si aggiunge 16 a entrambi i membri.
> 4. $(x^2 + 6x + 9) + (y^2 - 8y + 16) = -9 + 9 + 16$, cioè $(x + 3)^2 + (y - 4)^2 = 16$.
> 5. Centro $C(-3, 4)$, raggio $r = \sqrt{16} = 4$.
>
> Con le formule ($a = 6$, $b = -8$, $c = 9$): $C = (-3, 4)$ e $r = \sqrt{9 + 16 - 9} = 4$. Stesso risultato.

> [!warning] Non tutte le equazioni di questo tipo sono circonferenze
> Prendiamo $x^2 + y^2 - 2x + 4y + 10 = 0$. Completando i quadrati: $(x - 1)^2 + (y + 2)^2 = -10 + 1 + 4 = -5$.
>
> Una somma di quadrati non può essere negativa, quindi nessun punto soddisfa l'equazione: non è una circonferenza. Se a destra viene $0$, l'unico punto è il centro (circonferenza "degenere" di raggio zero). Per questo bisogna sempre controllare la condizione sul raggio.
>
> Altro controllo: se $x^2$ e $y^2$ hanno coefficienti diversi (per esempio $2x^2 + y^2 = 4$) l'equazione non è una circonferenza. Se hanno lo stesso coefficiente diverso da 1 ($2x^2 + 2y^2 - 8 = 0$), prima si divide tutto per quel numero.

### Posizione di una retta rispetto a una circonferenza

Una retta e una circonferenza possono trovarsi in tre posizioni:

1. *secante*: la retta taglia la circonferenza in due punti;
2. *tangente*: la retta la tocca in un solo punto;
3. *esterna*: la retta non la tocca.

![[03-retta-circonferenza.svg|620]]

Ci sono due modi per capire in quale caso ci si trova.

Il primo modo è con la distanza dal centro. Si calcola la distanza $d$ del centro dalla retta (con la formula punto-retta) e la si confronta con il raggio:

- $d < r$: secante;
- $d = r$: tangente;
- $d > r$: esterna.

Il secondo modo è con il sistema. I punti comuni sono le soluzioni del sistema tra l'equazione della retta e quella della circonferenza. Si ricava $y$ (o $x$) dalla retta, la si sostituisce nella circonferenza e si ottiene un'equazione di secondo grado. Il numero delle soluzioni dipende dal discriminante $\Delta = b^2 - 4ac$ di quell'equazione (vedi [[02-equazioni-e-disequazioni]]):

- $\Delta > 0$: due soluzioni, retta secante;
- $\Delta = 0$: una soluzione, retta tangente;
- $\Delta < 0$: nessuna soluzione, retta esterna.

Il metodo della distanza è più veloce se serve solo sapere la posizione; il sistema serve quando si vogliono anche le coordinate dei punti di intersezione.

> [!example] Esempio: circonferenza $x^2 + y^2 = 25$ e retta $y = x + 1$
> Con la distanza: il centro è $O(0, 0)$, il raggio è 5, la retta in forma implicita è $x - y + 1 = 0$.
> $$
> d = \frac{|0 - 0 + 1|}{\sqrt{1 + 1}} = \frac{1}{\sqrt{2}} \approx 0{,}71 < 5
> $$
> quindi la retta è secante.
>
> Con il sistema:
> 1. Si sostituisce $y = x + 1$: $x^2 + (x + 1)^2 = 25$.
> 2. Si svolge: $x^2 + x^2 + 2x + 1 = 25$, cioè $2x^2 + 2x - 24 = 0$, e dividendo per 2: $x^2 + x - 12 = 0$.
> 3. Discriminante: $\Delta = 1 + 48 = 49 > 0$: due punti, conferma che è secante.
> 4. Soluzioni: $x = \dfrac{-1 \pm 7}{2}$, cioè $x = 3$ oppure $x = -4$.
> 5. Con $y = x + 1$: i punti sono $(3, 4)$ e $(-4, -3)$.
>
> Verifica: $9 + 16 = 25$ e $16 + 9 = 25$. Entrambi i punti stanno sulla circonferenza.

![[03-esempio-secante.svg|440]]

> [!example] Esempio: una retta tangente
> Circonferenza $x^2 + y^2 = 25$ e retta $3x + 4y - 25 = 0$.
>
> Distanza del centro: $d = \dfrac{|0 + 0 - 25|}{\sqrt{9 + 16}} = \dfrac{25}{5} = 5 = r$. La retta è tangente.
>
> Per trovare il punto di contatto: dalla retta $y = \dfrac{25 - 3x}{4}$; sostituendo e moltiplicando per 16 si ottiene $25x^2 - 150x + 225 = 0$, cioè $x^2 - 6x + 9 = 0$, cioè $(x - 3)^2 = 0$. Il discriminante è zero, l'unica soluzione è $x = 3$ e quindi $y = 4$. Il punto di tangenza è $(3, 4)$.

Una proprietà utile: la retta tangente è perpendicolare al raggio nel punto di contatto. Nell'esempio, il raggio da $O$ a $(3, 4)$ ha pendenza $\frac{4}{3}$, la tangente ha pendenza $-\frac{3}{4}$, e il prodotto è $-1$.

### La sfera nello spazio

Il programma chiede anche l'equazione della sfera, che è la sorella tridimensionale della circonferenza. La definizione è la stessa: la *sfera* (più precisamente la superficie sferica) di centro $C$ e raggio $r$ è l'insieme dei punti dello spazio che distano $r$ da $C$.

Si usa la formula della distanza nello spazio al posto di quella nel piano, e si eleva al quadrato.

![[03-sfera.svg|460]]

> [!abstract] Equazione della sfera di centro $C(x_0, y_0, z_0)$ e raggio $r$
> $$
> (x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = r^2
> $$
> Se il centro è l'origine: $x^2 + y^2 + z^2 = r^2$.

> [!example] Esempio: sfera di centro $C(1, -2, 3)$ e raggio 2
> $$
> (x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 4
> $$
> Il punto $(1, -2, 5)$ sta sulla sfera? $0 + 0 + 2^2 = 4$: sì, è il punto più alto, 2 unità sopra il centro.

Anche per la sfera, se l'equazione è data in forma sviluppata ($x^2 + y^2 + z^2 + \dots = 0$), centro e raggio si trovano completando i quadrati, come per la circonferenza: un esempio svolto è nel capitolo di Stewart (esempio 5 del paragrafo 2.1).

## ESERCIZI

Questa sezione serve per allenarsi in vista dell'esonero. Conviene provare ogni esercizio da sola, su carta e con un piccolo disegno sul piano cartesiano, e solo dopo aprire la soluzione cliccando sul riquadro verde: se il risultato è diverso, si confrontano i passaggi uno per uno per trovare dove ci si è fermati.

### Gli esercizi del professore

Il professore non ha dato un foglio dedicato alla retta e alla circonferenza. Alcuni esercizi del foglio sui vettori ([[Esercizi_vettori.pdf]]) toccano però gli argomenti di questa pagina:

- Esercizio 14 (punti $A(1, -1)$, $B(5, 1)$, $C(2, 4)$): la distanza $AB$ e il punto medio di $AB$ sono svolti in questa pagina, nelle sezioni sulla distanza e sul punto medio. Le parti b e c (il quarto vertice $D$ del parallelogramma e il punto medio delle diagonali) sono svolte nella pagina [[05-i-vettori]], ma sono un buon allenamento sul punto medio: provarle da sola prima di guardare.
- Esercizio 22 (distanza di $P(4, 1)$ dalla retta per $A(1, 0)$ con direzione $(1, 2)$): svolto in questa pagina con la formula della distanza punto-retta e con la strada geometrica (perpendicolare e piede $H$), e svolto con i vettori nella pagina [[05-i-vettori]].
- Esercizio 10 (triangolo $A(1, 1)$, $B(5, 2)$, $C(3, 6)$): è svolto con il prodotto scalare nella pagina [[05-i-vettori]]. La parte b si può controllare anche con le distanze di questa pagina: $AB^2 = 17$, $AC^2 = 29$, $BC^2 = 20$; il lato più lungo al quadrato è minore della somma dei quadrati degli altri due ($29 < 37$), quindi il triangolo è acutangolo.
- Esercizio 11 (Pitagora in forma vettoriale): è il teorema di Pitagora su cui si regge la formula della distanza; è svolto nella pagina [[05-i-vettori]].

Per l'equazione della retta, il parallelismo e la perpendicolarità con le pendenze, l'intersezione di due rette, la circonferenza, la posizione retta-circonferenza e la sfera non ci sono esercizi del professore: per questi argomenti servono gli esercizi qui sotto. Negli appunti presi in classe c'è solo l'esercizio 14 (distanze $AB = \sqrt{20}$ e $AC = \sqrt{26}$, quarto vertice $D = (6, 6)$); attenzione che il punto medio di $AB$ è $(3, 0)$, non $(2, 1)$.

### Esercizi per allenarti

#### Distanza e punto medio

> [!question] Esercizio 1
> Dati $A(-2, 3)$ e $B(4, -5)$, calcolare la distanza $AB$ e il punto medio $M$ del segmento $AB$.

> [!success]- Soluzione
> Risultato: $AB = 10$ e $M = (1, -1)$.
>
> Come si arriva:
> 1. Si calcolano le differenze delle coordinate, che servono nella formula della distanza: $\Delta x = 4 - (-2) = 6$ e $\Delta y = -5 - 3 = -8$.
> 2. Distanza: è la radice della somma dei quadrati delle differenze (teorema di Pitagora), $AB = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.
> 3. Punto medio: ogni coordinata è la media delle coordinate di $A$ e $B$, $M = \left( \dfrac{-2 + 4}{2}, \dfrac{3 + (-5)}{2} \right) = (1, -1)$.
> 4. Controllo: $AM = \sqrt{3^2 + 4^2} = 5$, cioè metà di $AB$.

> [!question] Esercizio 2
> Il punto $M(2, 1)$ è il punto medio del segmento $AB$, con $A(-1, 4)$. Trovare le coordinate di $B$ e la lunghezza di $AB$.

> [!success]- Soluzione
> Risultato: $B = (5, -2)$ e $AB = \sqrt{72} = 6\sqrt{2}$.
>
> Come si arriva:
> 1. Ascissa di $B$: nella formula del punto medio l'incognita è $x_B$, quindi $\dfrac{-1 + x_B}{2} = 2$, cioè $-1 + x_B = 4$ e $x_B = 5$.
> 2. Ordinata di $B$: allo stesso modo $\dfrac{4 + y_B}{2} = 1$, cioè $4 + y_B = 2$ e $y_B = -2$.
> 3. Quindi $B(5, -2)$. Scorciatoia: $B = 2M - A = (4 - (-1),\ 2 - 4) = (5, -2)$.
> 4. Lunghezza: si usa la formula della distanza tra $A$ e $B$, $AB = \sqrt{(5 - (-1))^2 + (-2 - 4)^2} = \sqrt{36 + 36} = \sqrt{72} = 6\sqrt{2}$.

> [!question] Esercizio 3
> Dati $A(1, 2)$, $B(4, 6)$ e $C(5, -1)$, calcolare i lati del triangolo $ABC$. Che tipo di triangolo è? Calcolarne perimetro e area.

> [!success]- Soluzione
> Risultato: $AB = 5$, $AC = 5$, $BC = 5\sqrt{2}$; il triangolo è rettangolo isoscele (angolo retto in $A$); perimetro $10 + 5\sqrt{2}$, area $\dfrac{25}{2}$.
>
> Come si arriva:
> 1. Lato $AB$ con la formula della distanza: $AB = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.
> 2. Lato $AC$: $AC = \sqrt{4^2 + (-3)^2} = \sqrt{25} = 5$.
> 3. Lato $BC$: $BC = \sqrt{1^2 + (-7)^2} = \sqrt{50} = 5\sqrt{2}$.
> 4. Tipo: due lati sono uguali, quindi è isoscele. Inoltre $AB^2 + AC^2 = 25 + 25 = 50 = BC^2$: per il teorema di Pitagora (al contrario) è rettangolo in $A$.
> 5. Perimetro: è la somma dei tre lati, $5 + 5 + 5\sqrt{2} = 10 + 5\sqrt{2}$.
> 6. Area: in un triangolo rettangolo i cateti fanno da base e altezza; i cateti sono $AB$ e $AC$, quindi $\dfrac{5 \cdot 5}{2} = \dfrac{25}{2}$.

#### Pendenza ed equazione della retta

> [!question] Esercizio 4
> Scrivere l'equazione della retta passante per $A(-1, 2)$ e $B(3, -6)$, in forma esplicita e in forma implicita. Passa per l'origine?

> [!success]- Soluzione
> Risultato: forma esplicita $y = -2x$, forma implicita $2x + y = 0$; sì, passa per l'origine.
>
> Come si arriva:
> 1. Pendenza: è il rapporto tra la differenza delle $y$ e la differenza delle $x$, $m = \dfrac{-6 - 2}{3 - (-1)} = \dfrac{-8}{4} = -2$.
> 2. Retta per $A$ con pendenza $-2$: $y - 2 = -2(x + 1)$, cioè $y = -2x - 2 + 2 = -2x$.
> 3. Forma implicita: si porta tutto a sinistra, $2x + y = 0$.
> 4. Origine: il termine noto è $q = 0$, quindi sì, la retta passa per l'origine.
> 5. Controllo con $B$: $-2 \cdot 3 = -6$.

> [!question] Esercizio 5
> Una rampa deve superare un dislivello di 60 cm. Quanto deve essere lunga in pianta se la pendenza è del 5%? E se è dell'8%?

> [!success]- Soluzione
> Risultato: con il 5% la rampa è lunga 12 m in pianta; con l'8% è lunga 7,5 m.
>
> Come si arriva:
> 1. La pendenza è il rapporto tra dislivello e lunghezza in pianta: $m = \dfrac{\Delta y}{\Delta x}$, quindi la lunghezza è $\Delta x = \dfrac{\Delta y}{m}$ (con il dislivello in metri, $0{,}60$ m).
> 2. Con il 5%: $\Delta x = \dfrac{0{,}60}{0{,}05} = 12$ m.
> 3. Con l'8%: $\Delta x = \dfrac{0{,}60}{0{,}08} = 7{,}5$ m.
> 4. Più la pendenza è bassa, più la rampa è lunga.

#### Parallele, perpendicolari e intersezioni

> [!question] Esercizio 6
> Data la retta $r: 2x - 3y + 1 = 0$ e il punto $P(3, -1)$, scrivere la parallela e la perpendicolare a $r$ passanti per $P$.

> [!success]- Soluzione
> Risultato: parallela $y = \dfrac{2}{3}x - 3$ (cioè $2x - 3y - 9 = 0$); perpendicolare $y = -\dfrac{3}{2}x + \dfrac{7}{2}$ (cioè $3x + 2y - 7 = 0$).
>
> Come si arriva:
> 1. Per leggere la pendenza si porta $r$ in forma esplicita: $3y = 2x + 1$, cioè $y = \dfrac{2}{3}x + \dfrac{1}{3}$. La pendenza è $m = \dfrac{2}{3}$.
> 2. Parallela: ha la stessa pendenza, $y + 1 = \dfrac{2}{3}(x - 3)$, cioè $y = \dfrac{2}{3}x - 3$, in forma implicita $2x - 3y - 9 = 0$.
> 3. Perpendicolare: la pendenza è l'opposto del reciproco, $-\dfrac{3}{2}$, quindi $y + 1 = -\dfrac{3}{2}(x - 3)$, cioè $y = -\dfrac{3}{2}x + \dfrac{7}{2}$, in forma implicita $3x + 2y - 7 = 0$.
> 4. Controllo: $P$ sta su entrambe ($6 + 3 - 9 = 0$ e $9 - 2 - 7 = 0$) e $\dfrac{2}{3} \cdot \left(-\dfrac{3}{2}\right) = -1$.

> [!question] Esercizio 7
> Per quale valore di $k$ le rette $y = (k - 1)x + 2$ e $y = 3x - 5$ sono parallele? Per quale valore sono perpendicolari?

> [!success]- Soluzione
> Risultato: parallele per $k = 4$; perpendicolari per $k = \dfrac{2}{3}$.
>
> Come si arriva:
> 1. Parallele: le pendenze devono essere uguali, $k - 1 = 3$, quindi $k = 4$.
> 2. Perpendicolari: il prodotto delle pendenze deve essere $-1$, cioè $3(k - 1) = -1$, quindi $k - 1 = -\dfrac{1}{3}$ e $k = \dfrac{2}{3}$.
> 3. Controllo: con $k = \dfrac{2}{3}$ la prima pendenza è $-\dfrac{1}{3}$, e $-\dfrac{1}{3} \cdot 3 = -1$.

> [!question] Esercizio 8
> Trovare il punto di intersezione delle rette $r: 3x + 2y = 7$ e $s: x - 4y = 7$.

> [!success]- Soluzione
> Risultato: il punto di intersezione è $(3, -1)$.
>
> Come si arriva:
> 1. Il punto comune deve soddisfare tutte e due le equazioni: si risolve il sistema per sostituzione, ricavando $x$ da $s$: $x = 7 + 4y$.
> 2. Si sostituisce in $r$: $3(7 + 4y) + 2y = 7$, cioè $21 + 14y = 7$, quindi $14y = -14$ e $y = -1$.
> 3. Si torna a $x$: $x = 7 + 4 \cdot (-1) = 3$.
> 4. Controllo: $3 \cdot 3 + 2 \cdot (-1) = 7$ e $3 - 4 \cdot (-1) = 7$.

> [!question] Esercizio 9
> Dati $A(1, 2)$ e $B(5, 6)$, scrivere l'equazione dell'*asse* del segmento $AB$, cioè la retta perpendicolare ad $AB$ passante per il suo punto medio.

> [!success]- Soluzione
> Risultato: l'asse è $y = -x + 7$, in forma implicita $x + y - 7 = 0$.
>
> Come si arriva:
> 1. L'asse passa per il punto medio: $M = \left( \dfrac{1 + 5}{2}, \dfrac{2 + 6}{2} \right) = (3, 4)$.
> 2. Pendenza di $AB$: $m = \dfrac{6 - 2}{5 - 1} = 1$.
> 3. L'asse è perpendicolare ad $AB$, quindi la sua pendenza è l'opposto del reciproco: $-\dfrac{1}{1} = -1$.
> 4. Retta per $M$ con pendenza $-1$: $y - 4 = -1(x - 3)$, cioè $y = -x + 7$, in forma implicita $x + y - 7 = 0$.
> 5. Controllo: ogni punto dell'asse è alla stessa distanza da $A$ e da $B$. Con $(0, 7)$: la distanza da $A$ è $\sqrt{1 + 25} = \sqrt{26}$, la distanza da $B$ è $\sqrt{25 + 1} = \sqrt{26}$.

#### Distanza di un punto da una retta

> [!question] Esercizio 10
> Calcolare la distanza del punto $P(2, -1)$ dalla retta $r: 3x + 4y + 8 = 0$.

> [!success]- Soluzione
> Risultato: $d = 2$.
>
> Come si arriva:
> 1. Si leggono i coefficienti della retta in forma implicita: $a = 3$, $b = 4$, $c = 8$.
> 2. Si mettono nella formula della distanza punto-retta, con le coordinate di $P$ al posto di $x$ e $y$:
> $$
> d = \frac{|3 \cdot 2 + 4 \cdot (-1) + 8|}{\sqrt{3^2 + 4^2}} = \frac{|6 - 4 + 8|}{\sqrt{25}} = \frac{10}{5} = 2
> $$

> [!question] Esercizio 11
> Dati $A(1, 0)$, $B(4, 4)$ e $C(5, -2)$, calcolare la lunghezza di $AB$, l'altezza del triangolo $ABC$ relativa al lato $AB$ e l'area del triangolo.

> [!success]- Soluzione
> Risultato: $AB = 5$, altezza $h = \dfrac{22}{5}$, area $11$.
>
> Come si arriva:
> 1. Base: con la formula della distanza, $AB = \sqrt{3^2 + 4^2} = 5$.
> 2. Per l'altezza serve l'equazione della retta $AB$: pendenza $\dfrac{4 - 0}{4 - 1} = \dfrac{4}{3}$, quindi $y = \dfrac{4}{3}(x - 1)$. Moltiplicando per 3: $3y = 4x - 4$, in forma implicita $4x - 3y - 4 = 0$.
> 3. L'altezza relativa ad $AB$ è la distanza di $C$ dalla retta $AB$:
> $$
> h = \frac{|4 \cdot 5 - 3 \cdot (-2) - 4|}{\sqrt{16 + 9}} = \frac{|20 + 6 - 4|}{5} = \frac{22}{5}
> $$
> 4. Area: base per altezza diviso 2, $\dfrac{AB \cdot h}{2} = \dfrac{5 \cdot \frac{22}{5}}{2} = \dfrac{22}{2} = 11$.

#### La circonferenza

> [!question] Esercizio 12
> Scrivere l'equazione della circonferenza di centro $C(-1, 2)$ passante per il punto $P(2, 6)$, prima nella forma con il centro e poi nella forma sviluppata.

> [!success]- Soluzione
> Risultato: forma con il centro $(x + 1)^2 + (y - 2)^2 = 25$; forma sviluppata $x^2 + y^2 + 2x - 4y - 20 = 0$.
>
> Come si arriva:
> 1. Il raggio è la distanza tra centro e punto: $r = \sqrt{(2 + 1)^2 + (6 - 2)^2} = \sqrt{9 + 16} = 5$.
> 2. Equazione con centro $(-1, 2)$ e $r^2 = 25$: $(x + 1)^2 + (y - 2)^2 = 25$.
> 3. Per la forma sviluppata si svolgono i quadrati: $x^2 + 2x + 1 + y^2 - 4y + 4 = 25$.
> 4. Si porta tutto a sinistra: $x^2 + y^2 + 2x - 4y - 20 = 0$.

> [!question] Esercizio 13
> L'equazione $2x^2 + 2y^2 - 8x + 4y - 10 = 0$ rappresenta una circonferenza? Se sì, trovare centro e raggio.

> [!success]- Soluzione
> Risultato: sì, è una circonferenza di centro $C(2, -1)$ e raggio $r = \sqrt{10}$.
>
> Come si arriva:
> 1. $x^2$ e $y^2$ hanno lo stesso coefficiente e non c'è il termine $xy$, quindi può essere una circonferenza: si divide tutto per 2, $x^2 + y^2 - 4x + 2y - 5 = 0$.
> 2. Si raggruppano i termini in $x$ e quelli in $y$: $(x^2 - 4x) + (y^2 + 2y) = 5$.
> 3. Si completano i quadrati: metà di $-4$ è $-2$, e $(-2)^2 = 4$; metà di $2$ è $1$, e $1^2 = 1$. Si aggiunge $4 + 1$ a entrambi i membri.
> 4. Si ottiene $(x - 2)^2 + (y + 1)^2 = 5 + 4 + 1 = 10$.
> 5. Il numero a destra è positivo, quindi è una circonferenza: centro $C(2, -1)$, raggio $r = \sqrt{10}$.
> 6. Controllo con le formule ($a = -4$, $b = 2$, $c = -5$): $C = (2, -1)$ e $r = \sqrt{4 + 1 + 5} = \sqrt{10}$.

> [!question] Esercizio 14
> Trovare i punti di intersezione della circonferenza $x^2 + y^2 = 10$ con la retta $x - y + 2 = 0$ e la lunghezza della corda che li unisce.

> [!success]- Soluzione
> Risultato: i punti sono $(1, 3)$ e $(-3, -1)$; la corda è lunga $\sqrt{32} = 4\sqrt{2}$.
>
> Come si arriva:
> 1. Si ricava $y$ dalla retta: $y = x + 2$.
> 2. Si sostituisce nella circonferenza: $x^2 + (x + 2)^2 = 10$, cioè $x^2 + x^2 + 4x + 4 = 10$, cioè $2x^2 + 4x - 6 = 0$, e dividendo per 2: $x^2 + 2x - 3 = 0$.
> 3. Si risolve l'equazione di secondo grado: $\Delta = 4 + 12 = 16 > 0$, quindi la retta è secante. $x = \dfrac{-2 \pm 4}{2}$, cioè $x = 1$ oppure $x = -3$.
> 4. Con $y = x + 2$ si trovano le ordinate: i punti sono $(1, 3)$ e $(-3, -1)$.
> 5. La corda è la distanza tra i due punti: $\sqrt{(1 + 3)^2 + (3 + 1)^2} = \sqrt{16 + 16} = \sqrt{32} = 4\sqrt{2}$.
> 6. Controllo: $1 + 9 = 10$ e $9 + 1 = 10$.

> [!question] Esercizio 15
> Data la circonferenza $x^2 + y^2 - 2x - 4y - 20 = 0$, stabilire la posizione rispetto a essa delle rette $a: 3x + 4y + 14 = 0$, $b: x = 4$, $c: y = 8$. Per la retta tangente trovare il punto di contatto.

> [!success]- Soluzione
> Risultato: $a$ è tangente, con punto di contatto $(-2, -2)$; $b$ è secante; $c$ è esterna.
>
> Come si arriva:
> 1. Per confrontare le distanze con il raggio si trovano centro e raggio: $(x - 1)^2 + (y - 2)^2 = 20 + 1 + 4 = 25$, quindi $C(1, 2)$ e $r = 5$.
> 2. Retta $a$: distanza di $C$ con la formula punto-retta, $d = \dfrac{|3 + 8 + 14|}{\sqrt{9 + 16}} = \dfrac{25}{5} = 5 = r$: tangente.
> 3. Retta $b$ (verticale): la distanza di $C$ è la differenza delle ascisse, $|4 - 1| = 3 < 5$: secante.
> 4. Retta $c$ (orizzontale): la distanza di $C$ è la differenza delle ordinate, $|8 - 2| = 6 > 5$: esterna.
> 5. Punto di contatto di $a$: si mette a sistema la retta con la circonferenza. Da $a$, $y = \dfrac{-14 - 3x}{4}$, quindi $y - 2 = \dfrac{-22 - 3x}{4}$. Si sostituisce in $(x - 1)^2 + (y - 2)^2 = 25$ e si moltiplica per 16:
> $$
> 16(x - 1)^2 + (3x + 22)^2 = 400 \quad\Rightarrow\quad 25x^2 + 100x + 100 = 0 \quad\Rightarrow\quad x^2 + 4x + 4 = 0 \quad\Rightarrow\quad (x + 2)^2 = 0
> $$
> 6. L'unica soluzione è $x = -2$ (è tangente, quindi un solo punto), e $y = \dfrac{-14 + 6}{4} = -2$: il punto di contatto è $(-2, -2)$.
> 7. Controllo: il raggio da $C(1, 2)$ a $(-2, -2)$ ha pendenza $\dfrac{4}{3}$, la retta $a$ ha pendenza $-\dfrac{3}{4}$: sono perpendicolari, come deve essere.

#### La sfera

> [!question] Esercizio 16
> Trovare centro e raggio della sfera $x^2 + y^2 + z^2 + 4x - 2y - 8z + 12 = 0$. Il punto $P(0, 2, 2)$ sta sulla sfera? L'origine è dentro o fuori?

> [!success]- Soluzione
> Risultato: centro $C(-2, 1, 4)$ e raggio $r = 3$; $P$ sta sulla sfera; l'origine è fuori.
>
> Come si arriva:
> 1. Si raggruppano i termini di ogni variabile: $(x^2 + 4x) + (y^2 - 2y) + (z^2 - 8z) = -12$.
> 2. Si completano i quadrati aggiungendo $4$, $1$ e $16$ a entrambi i membri: $(x + 2)^2 + (y - 1)^2 + (z - 4)^2 = -12 + 4 + 1 + 16 = 9$.
> 3. Si leggono centro e raggio: $C(-2, 1, 4)$, $r = \sqrt{9} = 3$.
> 4. $P$: si sostituiscono le sue coordinate, $(0 + 2)^2 + (2 - 1)^2 + (2 - 4)^2 = 4 + 1 + 4 = 9$, che è proprio $r^2$: sì, sta sulla sfera.
> 5. Origine: la distanza dal centro è $\sqrt{4 + 1 + 16} = \sqrt{21} \approx 4{,}58 > 3$, maggiore del raggio: è fuori.

## Collegamenti

Questa pagina usa continuamente gli strumenti di [[02-equazioni-e-disequazioni|equazioni e disequazioni]]: l'intersezione di due rette è un sistema lineare, la posizione tra retta e circonferenza si decide con il discriminante di un'equazione di secondo grado, e le disequazioni con il valore assoluto diventano facili se lette come distanze sulla retta dei numeri.

La pagina sui [[05-i-vettori|vettori]] riprende quasi tutto in un linguaggio diverso. La distanza tra due punti è la norma del vettore che li unisce, il punto medio è una media di vettori, la direzione $(1, m)$ di una retta è un vettore, e la condizione di perpendicolarità $m_1 m_2 = -1$ diventa "prodotto scalare uguale a zero". L'esercizio 22 del foglio sui vettori, risolto qui con la formula della distanza punto-retta, si risolve lì trovando il piede $H$ con il prodotto scalare.

La retta $y = mx + q$ è anche il primo esempio di funzione: nella pagina sulle [[06-le-funzioni|funzioni]] diventa la funzione lineare $f(x) = mx + q$, il cui grafico è proprio questa retta, e la pendenza $m$ dice se la funzione cresce o decresce. Nelle [[06-le-funzioni#LE FUNZIONI ELEMENTARI: RETTE, POTENZE, RADICI E VALORE ASSOLUTO|funzioni elementari]] ritornano la tangente dell'angolo e il valore assoluto come funzioni vere e proprie. Più avanti nel corso la pendenza diventerà la derivata: la pendenza della retta tangente al grafico di una funzione.

Fuori dalla matematica, le coordinate nello spazio sono le stesse della Geometria descrittiva: il punto $(x, y, z)$ ha una quota e un aggetto, e la sua proiezione sul piano orizzontale corrisponde al punto $H(x, y, 0)$ della figura sulla distanza nello spazio. La pendenza, infine, è un numero che in architettura si usa davvero: per le rampe, le scale, le coperture e lo scolo delle acque si scrive in percentuale, ed è sempre il rapporto tra dislivello e lunghezza in pianta.

## Per approfondire

- Programma del corso (`Programma del corso_Istituzioni_di_matematiche_1_canale_1.pdf`, pagina 1): coordinate nel piano e nello spazio, distanza, valore assoluto, equazione della circonferenza e della sfera, pendenza di un segmento, condizioni di parallelismo e ortogonalità.
- Stewart, capitolo sui vettori (`Capitolo_Vettori.pdf`), paragrafo 2.1 "Sistemi tridimensionali di coordinate", pagine 58-63 del libro (pagine 1-6 del PDF): piani coordinati, formula della distanza in tre dimensioni con la dimostrazione con Pitagora, equazione della sfera ed esempio del completamento dei quadrati.
- Paxia, *Lezioni di geometria* (`paxia_libro.pdf`), capitolo 2 "Geometria lineare nel piano", pagine 31-50 del libro: equazioni della retta (2.2), mutua posizione e intersezione di due rette (2.3 e 2.4), coefficiente angolare (2.5), distanze (2.7) ed esempi (2.8). Il paragrafo 4.8 "Circonferenze" (pagina 88) e il 4.9 "Tangenti" (pagina 90) trattano la circonferenza. Il testo è più formale di quanto serve per l'esonero: usarlo per gli esempi.
- Esercizi del professore (`Esercizi_vettori.pdf`): esercizio 14 (punti, distanza e punto medio) ed esercizio 22 (distanza di un punto da una retta), svolti in questa pagina.
- Esercizi per allenarsi, con le soluzioni: sezione [[#ESERCIZI]] di questa pagina.
- Per il ripasso veloce delle formule: [[00-ripasso-esonero-1]].
