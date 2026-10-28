---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-08
tags: [geometria-descrittiva, appunti, teoria]
---

# PO 3 - La retta

> [!info] Note collegate
> Precedente: [[PO 2 - Il punto]] · Successiva: [[PO 4 - Il piano]]
>
> Esercizi: [[esercitazioni|Esercitazioni]] · Teoria collegata: [[teoria-omologia]]
>
> Bozze delle lezioni: [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]]

Capitolo 3 di 8 della teoria delle proiezioni ortogonali. Lezioni: 8-20 ottobre. Questa pagina è un riassunto diviso per tipo di retta; la versione completa, lezione per lezione, è nelle bozze collegate qui sopra.

## 3.0 Tre regole che valgono per tutte le rette

1. Il nome. Si guarda com'è la retta rispetto a π₁ (il pavimento) e a π₂ (la parete di fronte): perpendicolare, parallela o inclinata. Ogni combinazione ha un nome, e π₃ non conta per il nome.
2. Le tracce. La traccia è il punto in cui la retta buca un piano di proiezione: T₁ᵣ su π₁, T₂ᵣ su π₂, T₃ᵣ su π₃. Se la retta è parallela a un piano, la traccia su quel piano è all'infinito (T∞) e si segna con la lineetta nella direzione della retta.
3. Le proiezioni passano per le proiezioni delle tracce. Le proiezioni delle tracce cadono sempre sulla linea di terra o sulla linea verticale.

In ogni paragrafo il disegnino piccolo mostra la retta nella «stanza»: π₁ è il pavimento, π₂ la parete di fronte, π₃ la parete di lato; la linea grigia tratteggiata è l'ombra della retta sul pavimento.

---

## 3.1 La retta proiettante in prima (8 ottobre)

È perpendicolare a π₁: è verticale, come un palo.

![[b04-retta-stanza-1.svg|220]]

- Traccia propria: solo T₁ᵣ, sul pavimento. T₂ᵣ e T₃ᵣ sono all'infinito.
- Vista dall'alto si riduce a un punto: r₁ ≡ T₁ᵣ.
- r₂ e r₃ sono verticali, perpendicolari alla LT.

> [!example] Disegno 8 · La retta proiettante in prima
> ![[03-retta-proiettante-in-prima.svg|560]]
>
> ![[b03-spazio-retta-proiettante-in-prima.svg|480]]
>
> In 2D: r₁ è un punto sotto la LT, r₂ parte dalla LT perpendicolare. In 3D (schema proposto): la retta sale dal pavimento e lo buca in T₁ᵣ.

## 3.2 La retta proiettante in seconda (8 ottobre)

È perpendicolare a π₂: esce dalla parete verso di te.

![[b04-retta-stanza-2.svg|220]]

- Traccia propria: solo T₂ₘ, sulla parete. T₁ₘ e T₃ₘ sono all'infinito.
- Vista di fronte si riduce a un punto: m₂ ≡ T₂ₘ.
- m₁ è perpendicolare alla LT; m₃ è orizzontale, alla stessa quota di m₂.

> [!example] Disegno 9 · La retta proiettante in seconda
> ![[03-retta-proiettante-in-seconda.svg|560]]
>
> ![[03-spazio-retta-proiettante-in-seconda.svg|480]]
>
> In 2D: m₂ è un punto sopra la LT, m₁ scende perpendicolare alla LT. In 3D: la retta esce dalla parete π₂ in T₂ₘ.

## 3.3 La retta parallela alla linea di terra, cioè proiettante in terza (13 ottobre)

È parallela a π₁ e a π₂: come una mensola attaccata alla parete. È perpendicolare a π₃, ma il nome si dà guardando π₁ e π₂.

![[b04-retta-stanza-3.svg|220]]

- Traccia propria: solo T₃ᵣ, sulla parete di lato. T₁ᵣ e T₂ᵣ sono all'infinito.
- r₁ e r₂ sono parallele alla LT e partono dalla linea verticale, da (T₃ᵣ)₁ e (T₃ᵣ)₂.
- In terza proiezione si riduce a un punto: r₃ ≡ T₃ᵣ.

> [!example] Disegno 10 · La retta parallela alla LT
> ![[04-retta-parallela-alla-lt.svg|560]]
>
> ![[04-spazio-retta-parallela-alla-lt.svg|480]]
>
> In 2D: r₁ e r₂ parallele alla LT, con le lineette di T₁ᵣ∞ e T₂ᵣ∞. In 3D: la retta è fissata su π₃ in T₃ᵣ.

13-10!!

## 3.4 La retta frontale (13 ottobre)

È parallela a π₂ e inclinata rispetto a π₁: come una scala appoggiata alla parete di fronte.

![[b04-retta-stanza-4.svg|220]]

- Tracce proprie: T₁f (pavimento) e T₃f (parete di lato). T₂f è all'infinito.
- La caratteristica da ricordare: f₁ è parallela alla LT.
- f₂ mostra l'inclinazione vera della retta; f₃ è verticale.

> [!example] Disegno 11 · La retta frontale
> ![[04-retta-frontale.svg|560]]
>
> ![[04-spazio-retta-frontale.svg|480]]
>
> In 2D: f₁ parallela alla LT, f₂ inclinata, lineetta di T₂f∞ nella direzione di f₂. In 3D: la retta sta di fronte alla parete, sempre alla stessa distanza.

## 3.5 La retta orizzontale (13 ottobre)

È parallela a π₁ e inclinata rispetto a π₂: tutti i suoi punti hanno la stessa altezza, ma è storta rispetto alla parete.

![[b04-retta-stanza-5.svg|220]]

- Tracce proprie: T₂ₒ (parete di fronte) e T₃ₒ (parete di lato). T₁ₒ è all'infinito.
- La caratteristica da ricordare: o₂ è parallela alla LT.
- o₁ mostra l'inclinazione vera della retta; o₃ prosegue o₂.
- Serve anche in architettura, per esempio per la pendenza di un terreno o di una falda.

> [!example] Disegno 12 · La retta orizzontale
> ![[04-retta-orizzontale.svg|560]]
>
> ![[04-spazio-retta-orizzontale.svg|480]]
>
> In 2D: o₂ parallela alla LT, o₁ inclinata, lineetta di T₁ₒ∞ nella direzione di o₁. In 3D: la retta resta sempre alla stessa altezza dal pavimento.

Frontale e orizzontale sono una lo specchio dell'altra:

- frontale: f₁ parallela alla LT, T₂ all'infinito;
- orizzontale: o₂ parallela alla LT, T₁ all'infinito.

## 3.6 La retta di profilo (13 ottobre)

È inclinata rispetto a π₁ e a π₂, ma sta in un piano di lato, parallelo a π₃: come una scala appoggiata alla parete di lato.

![[b04-retta-stanza-6.svg|220]]

- Tracce proprie: T₁ᵣ e T₂ᵣ, alla stessa distanza da π₃. T₃ᵣ è all'infinito.
- r₁ e r₂ stanno sulla stessa linea, perpendicolare alla LT: da sole non dicono com'è inclinata la retta.
- La retta si vede davvero solo in terza proiezione, r₃. Anche per un suo punto serve la terza proiezione.

> [!example] Disegno 13 · La retta di profilo
> ![[04-retta-di-profilo.svg|560]]
>
> ![[04-spazio-retta-di-profilo.svg|480]]
>
> In 2D: r₁ e r₂ sulla stessa perpendicolare alla LT, l'inclinazione si vede solo in r₃. In 3D: la retta scende dalla parete π₂ al pavimento restando parallela a π₃.

15-10!!!

## 3.7 La retta generica (15 e 20 ottobre)

È inclinata rispetto a tutti e tre i piani: non ha nessuna particolarità.

![[b04-retta-stanza-7.svg|220]]

- Ha tutte e tre le tracce proprie: T₁ᵣ, T₂ᵣ, T₃ᵣ.
- Dalle tracce alle proiezioni: r₂ passa per T₂ᵣ e per (T₁ᵣ)₂, che sta sulla LT; r₁ passa per T₁ᵣ e per (T₂ᵣ)₁, che sta sulla LT.
- Dalle proiezioni alle tracce: si prolunga r₂ fino alla LT e si trova (T₁ᵣ)₂, poi si scende fino a r₁ e lì c'è T₁ᵣ. Allo stesso modo si prolunga r₁ fino alla LT, si trova (T₂ᵣ)₁ e si sale fino a r₂: lì c'è T₂ᵣ.
- I punti sulla LT si chiamano con il loro nome: (T₁ᵣ)₂ è «la seconda proiezione della prima traccia».
- A seconda della direzione, le tracce possono cadere tutte e due sotto la LT o tutte e due sopra: il procedimento non cambia.
- La terza traccia T₃ᵣ cade dietro il modello. Si può trovare prolungando r₃ (tratteggiata), ma il modo più sicuro usa un piano ausiliario (vedi [[PO 5 - L'appartenenza]]).

> [!example] Disegno 14 · La retta generica
> ![[05-retta-generica-proiezioni.svg|520]]
>
> ![[05-spazio-retta-generica.svg|540]]
>
> In 2D: le proiezioni costruite dalle tracce. In 3D: r₁ è come l'ombra della retta sul pavimento, r₂ la sua immagine sulla parete.

> [!example] Disegno 15 · Dalle proiezioni alle tracce: i punti notevoli sulla LT
> ![[06-retta-generica-punti-notevoli.svg|560]]
>
> Si prolunga r₂ fino alla LT, si trova (T₁ᵣ)₂ e si scende fino a r₁: lì c'è T₁ᵣ. Si prolunga r₁ fino alla LT, si trova (T₂ᵣ)₁ e si sale fino a r₂: lì c'è T₂ᵣ.

> [!example] Disegno 16 · Una retta con le tracce dall'altra parte
> ![[b06-retta-tracce-sotto-la-lt.svg|540]]
>
> Schema proposto, non disegnato a lezione: i punti notevoli si trovano come prima, ma T₂ᵣ cade sotto la LT.

---

## Collegamenti

Il capitolo successivo è [[PO 4 - Il piano]]. Il capitolo precedente è [[PO 2 - Il punto]].
