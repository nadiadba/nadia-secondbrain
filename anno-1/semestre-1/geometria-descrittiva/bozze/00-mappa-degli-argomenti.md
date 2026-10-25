---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-25
tags: [geometria-descrittiva, bozza, mappa]
---

# Mappa degli argomenti di geometria descrittiva

La mappa di tutto quello che si è fatto finora, dalla lezione del 1 ottobre a quella del 22 ottobre, per vedere che cosa sta dentro che cosa. Si legge da sinistra a destra: a sinistra i gruppi grandi, poi i sottogruppi, poi i tipi.

> [!info] Note collegate
> Bozze: [[01-strumenti-materiali-e-regole]] · [[02-proiezioni-e-omologia-schema]] · [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]]
>
> Ripasso: [[00-ripasso-prova-1]]

## IL QUADRO GENERALE

Il corso finora è fatto di quattro gruppi grandi. Le frecce tratteggiate dicono che cosa serve per capire che cosa: per esempio l'omologia serve per il ribaltamento.

```mermaid
flowchart LR
    G["GEOMETRIA DESCRITTIVA<br/>(fin qui)"]
    G --> D["1. IL DISEGNO TECNICO<br/>bozza 01"]
    G --> E["2. GEOMETRIA EUCLIDEA<br/>(i richiami)<br/>bozza 02"]
    G --> P["3. GEOMETRIA PROIETTIVA<br/>bozza 02"]
    G --> M["4. PROIEZIONI ORTOGONALI<br/>(metodo di Monge)<br/>bozze 03-07"]
    E -.-> P
    P -.->|"le proiezioni cilindriche ortogonali"| M
    P -.->|"l'omologia serve per il ribaltamento"| M
    classDef radice fill:#333,color:#fff,stroke:#333
    classDef gruppo fill:#dbe8f6,stroke:#2b5c9e,color:#111
    class G radice
    class D,E,P,M gruppo
```

## 1. IL DISEGNO TECNICO

Le regole e gli strumenti per disegnare bene, dalla prima lezione ([[01-strumenti-materiali-e-regole]]).

```mermaid
flowchart LR
    D["IL DISEGNO TECNICO"]
    D --> S["Gli strumenti"]
    S --> S1["mine e portamine<br/>(H dure, B morbide)"]
    S --> S2["carta e gomma"]
    S --> S3["squadrette e parallelineo"]
    D --> F["I formati dei fogli"]
    F --> F1["serie A: A4, A3...<br/>lati in rapporto √2"]
    F --> F2["tavola 50 × 70"]
    D --> R["Le regole del disegno"]
    R --> R1["linee di costruzione<br/>leggere e lasciate"]
    R --> R2["linee definitive<br/>più marcate"]
    R --> R3["scrittura tra<br/>due parallele"]
    R --> R4["disegnare in scala"]
    D --> X["Gli esercizi:<br/>piante e prospetti di un solido"]
    X --> X1["primo solido<br/>(bozza 01)"]
    X --> X2["secondo solido<br/>(bozza 02, in fondo)"]
    classDef gruppo fill:#dbe8f6,stroke:#2b5c9e,color:#111
    classDef sotto fill:#e6f3e6,stroke:#2e7d32,color:#111
    class D gruppo
    class S,F,R,X sotto
```

## 2. GEOMETRIA EUCLIDEA (I RICHIAMI)

La geometria "di scuola", ripassata all'inizio della lezione del 6 ottobre ([[02-proiezioni-e-omologia-schema#RICHIAMI DI GEOMETRIA EUCLIDEA|bozza 02]]).

```mermaid
flowchart LR
    E["GEOMETRIA EUCLIDEA"]
    E --> DI["Le distanze<br/>(sempre con la perpendicolare)"]
    DI --> DI1["punto - retta"]
    DI --> DI2["punto - piano"]
    E --> RR["Due rette"]
    RR --> RR1["nello stesso piano"]
    RR1 --> RR1a["parallele<br/>(nessun punto in comune)"]
    RR1 --> RR1b["incidenti<br/>(un punto in comune)"]
    RR --> RR2["in piani diversi:<br/>sghembe"]
    E --> PP["Due piani"]
    PP --> PP1["paralleli<br/>(nessun punto in comune)"]
    PP --> PP2["incidenti<br/>(una retta in comune)"]
    E --> RP["Una retta e un piano"]
    RP --> RP1["secante<br/>(un punto in comune)"]
    RP --> RP2["parallela"]
    RP --> RP3["perpendicolare<br/>(⊥ a due rette del piano)"]
    E --> DT["Porzioni di spazio"]
    DT --> DT1["diedro:<br/>due semipiani + una retta"]
    DT --> DT2["triedro:<br/>tre piani + un vertice"]
    E --> PO["I postulati di appartenenza<br/>e i loro duali"]
    E --> CO["Le lettere"]
    CO --> CO1["punti: maiuscole (P)"]
    CO --> CO2["rette: minuscole (r)"]
    CO --> CO3["piani: greche (α)"]
    classDef gruppo fill:#dbe8f6,stroke:#2b5c9e,color:#111
    classDef sotto fill:#e6f3e6,stroke:#2e7d32,color:#111
    class E gruppo
    class DI,RR,PP,RP,DT,PO,CO sotto
```

## 3. GEOMETRIA PROIETTIVA

Che cosa succede quando si proietta, e le proiettività: prospettività e omologia ([[02-proiezioni-e-omologia-schema#I FONDAMENTI DELLA GEOMETRIA PROIETTIVA|bozza 02]]).

Attenzione a due parole che si somigliano: la prospettività è un tipo di proiettività (una corrispondenza tra due piani), mentre la prospettiva è un metodo per disegnare, che nasce dalle proiezioni coniche.

```mermaid
flowchart LR
    P["GEOMETRIA PROIETTIVA"]
    P --> PR["Proiettare<br/>(da un centro S su un piano di quadro)"]
    PR --> PR1["un punto → un raggio"]
    PR --> PR2["una retta → un fascio<br/>(tutto in un piano)"]
    PR --> PR3["un piano → una stella<br/>(in tutte le direzioni)"]
    P --> PP["Le proprietà proiettive<br/>(quello che resta uguale)"]
    P --> EI["Gli enti impropri<br/>(all'infinito)"]
    EI --> EI1["punto improprio:<br/>dove si incontrano le parallele"]
    EI --> EI2["modello della circonferenza"]
    P --> TP["I tipi di proiezione"]
    TP --> TP1["coniche<br/>(centro proprio)"]
    TP1 --> TP1a["prospettiva"]
    TP --> TP2["cilindriche<br/>(centro improprio)"]
    TP2 --> TP2a["proiezioni ortogonali"]
    TP2 --> TP2b["assonometria<br/>ortogonale e obliqua"]
    P --> PV["Le proiettività"]
    PV --> PS["PROSPETTIVITÀ<br/>un centro, due piani"]
    PS --> PS1["omografia:<br/>la corrispondenza che si ottiene"]
    PV --> OM["OMOLOGIA<br/>due prospettività sullo stesso piano"]
    OM --> OM1["gli elementi:<br/>centro U, asse u,<br/>coppia di punti A e A′"]
    OM --> OM2["le due proprietà:<br/>A, A′ allineati con U;<br/>rette corrispondenti sull'asse"]
    OM --> OT["i tipi di omologia"]
    OT --> T1["classica<br/>U e u propri"]
    OT --> T2["speciale<br/>U sull'asse u"]
    OT --> T3["affinità<br/>U improprio (U∞)"]
    T3 --> T3a["ortogonale"]
    T3 --> T3b["obliqua"]
    OT --> T4["omotetia<br/>asse improprio (u∞)"]
    OT --> T5["traslazione<br/>U∞ e u∞"]
    classDef gruppo fill:#dbe8f6,stroke:#2b5c9e,color:#111
    classDef sotto fill:#e6f3e6,stroke:#2e7d32,color:#111
    classDef tipo fill:#fdf0d5,stroke:#b7791f,color:#111
    class P gruppo
    class PR,PP,EI,TP,PV sotto
    class PS,OM,OT tipo
```

## 4. PROIEZIONI ORTOGONALI (METODO DI MONGE)

Come si rappresentano punti, rette, piani e figure con le tre proiezioni, dalla lezione dell'8 ottobre in poi ([[03-proiezioni-ortogonali-punto-e-rette]], [[04-rette-e-piani-nelle-varie-posizioni]], [[05-appartenenza-e-rette-ausiliarie]], [[06-piani-ausiliari-e-perpendicolarita]], [[07-il-ribaltamento]]). Le diramazioni sono tante, quindi lo schema è diviso in due parti.

### Prima parte: il sistema, il punto, le rette e i piani

```mermaid
flowchart LR
    M["PROIEZIONI ORTOGONALI"]
    M --> SI["Il sistema<br/>(bozza 03)"]
    SI --> SI1["triedro: π₁ orizzontale,<br/>π₂ verticale, π₃ di lato"]
    SI --> SI2["linea di terra LT"]
    SI --> SI3["ribaltamento dei piani<br/>sul foglio"]
    SI --> SI4["pianta, prospetti, scale"]
    M --> PU["Il punto<br/>(bozza 03)"]
    PU --> PU1["tre proiezioni:<br/>P₁, P₂, P₃"]
    PU --> PU2["quota, aggetto,<br/>linea di richiamo"]
    M --> RE["Le rette<br/>(bozze 03, 04, 05)"]
    RE --> RE0["tracce: T₁ᵣ, T₂ᵣ, T₃ᵣ"]
    RE --> RE1["proiettante in prima"]
    RE --> RE2["proiettante in seconda"]
    RE --> RE3["parallela alla LT"]
    RE --> RE4["frontale"]
    RE --> RE5["orizzontale"]
    RE --> RE6["di profilo"]
    RE --> RE7["generica"]
    M --> PI["I piani<br/>(bozze 04, 05)"]
    PI --> PI0["tracce: t₁α, t₂α, t₃α"]
    PI --> PI1["proiettante in prima"]
    PI --> PI2["proiettante in seconda"]
    PI --> PI3["parallelo alla LT"]
    PI --> PI4["frontale"]
    PI --> PI5["orizzontale"]
    PI --> PI6["di profilo"]
    PI --> PI7["generico<br/>(triangolo delle tracce)"]
    classDef gruppo fill:#dbe8f6,stroke:#2b5c9e,color:#111
    classDef sotto fill:#e6f3e6,stroke:#2e7d32,color:#111
    class M gruppo
    class SI,PU,RE,PI sotto
```

### Seconda parte: appartenenza, perpendicolarità, figure e ribaltamento

```mermaid
flowchart LR
    M["PROIEZIONI ORTOGONALI"]
    M --> AP["L'appartenenza<br/>(bozze 04, 05, 06)"]
    AP --> AP1["punto - retta"]
    AP --> AP2["retta - piano"]
    AP --> AP3["punto - piano"]
    AP --> AU["gli aiuti"]
    AU --> AU1["rette ausiliarie:<br/>orizzontale e frontale"]
    AU --> AU2["piani ausiliari"]
    AP --> AP4["i piani che contengono<br/>una retta"]
    AP --> AP5["il piano dato da una figura:<br/>forma mongiana e forma tecnica"]
    M --> PE["La perpendicolarità<br/>(bozza 06)"]
    PE --> PE1["retta ⊥ piano:<br/>teorema di Monge"]
    PE --> PE2["retta ⊥ piano con<br/>orizzontale e frontale"]
    PE --> PE3["piano ⊥ piano"]
    M --> FS["Figure e solidi<br/>(bozza 06)"]
    FS --> FS1["la figura nelle<br/>diverse posizioni"]
    FS --> FS2["i solidi:<br/>facce, spigoli, diedri"]
    M --> RI["Il ribaltamento<br/>(bozza 07)"]
    RI --> RI1["piano proiettante in prima"]
    RI1 --> RI1a["su π₁"]
    RI1 --> RI1b["su π₂"]
    RI --> RI2["piano proiettante in seconda"]
    RI2 --> RI2a["su π₁"]
    RI2 --> RI2b["su π₂"]
    RI --> RI3["omologia di ribaltamento<br/>(un'affinità)"]
    classDef gruppo fill:#dbe8f6,stroke:#2b5c9e,color:#111
    classDef sotto fill:#e6f3e6,stroke:#2e7d32,color:#111
    classDef tipo fill:#fdf0d5,stroke:#b7791f,color:#111
    class M gruppo
    class AP,PE,FS,RI sotto
    class AU,RI1,RI2 tipo
```

## Collegamenti

La mappa segue l'ordine delle bozze. Il [[01-strumenti-materiali-e-regole|disegno tecnico]] serve in tutti gli esercizi. La geometria euclidea e la geometria proiettiva della [[02-proiezioni-e-omologia-schema|bozza 02]] sono la base delle proiezioni ortogonali, che partono dalla [[03-proiezioni-ortogonali-punto-e-rette|bozza 03]]. L'omologia torna nel [[07-il-ribaltamento|ribaltamento]] come omologia di ribaltamento. Per ripassare gli esercizi tipo c'è il [[00-ripasso-prova-1|ripasso per la Prova n.1]].
