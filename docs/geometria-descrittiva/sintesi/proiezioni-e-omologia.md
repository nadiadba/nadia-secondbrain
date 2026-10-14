# Geometria descrittiva — proiezioni e omologia (ripasso schematico)

Riassunto rapido della lezione del 6 ottobre: i concetti chiave in forma di schema, per ripassare velocemente.

## Richiami di geometria

- Distanza punto-retta: segmento tra il punto $P$ e il piede della perpendicolare condotta da $P$ alla retta $r$. È sempre la distanza minima (quella perpendicolare).
- Distanza punto-piano: segmento tra il punto e il piede della perpendicolare condotta al piano.
- Due rette complanari: o parallele (nessun punto in comune) o incidenti (un punto in comune).
- Due rette non complanari: sghembe (stanno su piani diversi).
- Per un punto esterno a una retta passa una e una sola parallela alla retta.
- Due piani: o paralleli (nessun punto in comune) o incidenti (una retta in comune).
- Retta parallela a un piano: se è parallela a una retta del piano.
- Retta perpendicolare a un piano: se è perpendicolare a due rette del piano.

## Diedri e triedri

- Diedro: porzione di spazio delimitata da due semipiani che hanno in comune una retta.
- Triedro: porzione di spazio delimitata da tre piani; il loro punto comune è il vertice, che diventerà l'origine degli assi.
- I piani vanno pensati sempre infiniti, anche se si disegnano delimitati.

## Postulati di appartenenza

Primi tre:

- per due punti distinti passa una e una sola retta;
- tre punti non allineati individuano un piano;
- un punto e una retta che non lo contiene individuano un piano.

Tre duali (si sostituisce "piano" a "punto"):

- due piani distinti individuano una retta comune;
- tre piani distinti, che non passano per una stessa retta, individuano un punto comune;
- una retta e un piano distinti individuano un punto.

!!! warning "Attenzione ai tre piani"
    Vale solo se i tre piani non passano per una stessa retta. Se vi passassero (come le pagine di un libro), avrebbero in comune quella retta e non un punto.

## Convenzioni grafiche

- Lettere maiuscole $\to$ punti.
- Lettere minuscole latine ($r$, $s$) $\to$ rette.
- Lettere minuscole greche ($\alpha$, $\beta$, $\gamma$) $\to$ piani.
- Segno sottile per le costruzioni, segno marcato per il risultato: conta il procedimento.

## Geometria proiettiva: proiezione e sezione

- Serve a rappresentare sul piano (il foglio, 2 dimensioni) ciò che sta nello spazio.
- Proiezione: ciò che parte dalla fonte (il fascio che esce dal proiettore).
- Sezione: l'immagine ottenuta dall'intersezione con un piano.
- Proiettando, non tutto si conserva: la geometria proiettiva studia le proprietà che restano invariate (proprietà proiettive). Fondatore: Girard Desargues (Seicento).

## Proiettare punto, retta, piano

Servono due elementi: un centro di proiezione $S$ e un piano di quadro (PQ).

- Punto: si costruisce il raggio proiettante per $S$ e $P$; dove buca il PQ lascia la proiezione $P'$.
- Retta: si ottiene un fascio di rette (tutte per $S$), che appartiene a un unico piano.
- Piano: si ottiene una stella di rette (non appartengono a un unico piano).

## Proprietà proiettive

- Appartenenza: se $P$ appartiene a $r$, allora $P'$ appartiene a $r'$.
- Allineamento: punti allineati restano allineati.
- Incidenza: rette incidenti restano incidenti, nel punto immagine.

## Enti impropri (all'infinito)

- Ente improprio: ente la cui posizione è, per convenzione, all'infinito.
- Due rette parallele si incontrano in un punto improprio (all'infinito), che si indica con la sua direzione (un trattino).
- Modello: la retta proiettiva è una circonferenza (la retta più il suo punto all'infinito).

## Tipi di proiezione

- Centro proprio (al finito) $\to$ proiezioni coniche $\to$ prospettiva.
- Centro improprio (all'infinito, raggi paralleli) $\to$ proiezioni cilindriche $\to$ proiezioni ortogonali e assonometriche.
- Assonometria ortogonale: direzione perpendicolare al PQ. Assonometria obliqua: direzione inclinata.

## Prospettività, omografia, omologia

- Prospettività: la proiettività più semplice (un centro, un piano, corrispondenza biunivoca).
- Omografia: da un centro $S$ si proiettano gli elementi di un piano $\alpha$ su un altro piano $\alpha'$.
- Omologia: prodotto di due prospettività, cioè due centri ($S$ e $S'$) che proiettano sullo stesso piano.
- Un'omologia è definita da tre dati: centro, asse e una coppia di elementi corrispondenti.

!!! abstract "Le due proprietà da ricordare"
    1. I punti corrispondenti sono allineati con il centro.
    2. Le rette corrispondenti si incontrano sull'asse.

## Esercizio tipo di omologia

Dati: centro, asse, una coppia di punti corrispondenti $A$ e $A'$, e un punto $B$. Trovare $B'$.

1. $B'$ sta sul raggio che parte dal centro e passa per $B$ (prima proprietà).
2. Si traccia la retta $r$ per $A$ e $B$; incontra l'asse in un punto unito $U$.
3. La retta corrispondente $r'$ passa per $U$ e per $A'$ (seconda proprietà).
4. $B'$ è l'intersezione tra $r'$ e il raggio dal centro per $B$.

!!! tip "Regola generale"
    Se hai i punti, cerca le rette; se hai le rette, cerca i punti. L'esercizio è sempre una somma di cose che già conosci.

## Omologie particolari

- Omologia speciale: il centro cade sull'asse. Si risolve allo stesso modo.
- Affinità: i due centri sono allineati su una retta parallela al piano $\to$ centro all'infinito (una direzione). Ortogonale se la direzione è perpendicolare all'asse, obliqua se è inclinata.
- Omotetia: il piano della figura è parallelo al PQ $\to$ asse all'infinito, centro proprio; rette corrispondenti parallele, figura ingrandita.
- Traslazione: piano parallelo (asse all'infinito) e centri allineati parallelamente al piano (centro all'infinito); la figura si sposta uguale, conservando le distanze.
