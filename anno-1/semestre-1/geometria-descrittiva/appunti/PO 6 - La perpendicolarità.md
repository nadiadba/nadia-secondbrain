---
tipo: appunti
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-20
tags: [geometria-descrittiva, appunti, teoria]
---

# PO 6 - La perpendicolarità

> [!info] Note collegate
> Precedente: [[PO 5 - L'appartenenza]] · Successiva: [[PO 7 - Figure piane e solidi]]
>
> Esercizi: [[esercitazioni|Esercitazioni]] · Teoria collegata: [[teoria-omologia]]
>
> Bozze delle lezioni: [[06-piani-ausiliari-e-perpendicolarita]]

Capitolo 6 di 8 della teoria delle proiezioni ortogonali. Lezioni: 20 ottobre.

## 6.1 La retta perpendicolare a un piano (20 ottobre)

### 6.1.1 Il teorema di Monge (20 ottobre)

Una retta è perpendicolare a un piano se è perpendicolare a due rette del piano.

Monge traduce questa condizione nelle proiezioni: una retta è perpendicolare a un piano se le proiezioni della retta sono perpendicolari alle rispettive tracce del piano. È il teorema di Monge: r ⊥ α se r₁ ⊥ t₁α e r₂ ⊥ t₂α.

La retta può essere esterna al piano, ma la stessa perpendicolarità vale per rette che appartengono al piano.

> [!example] Disegno 44 · La retta perpendicolare a un piano
> ![[06-retta-perpendicolare-al-piano.svg|600]]
>
> Dal punto P si traccia r₂ perpendicolare a t₂α e r₁ perpendicolare a t₁α, segnando gli angoli retti.
>
> ![[b06-spazio-retta-perpendicolare-al-piano.svg|600]]
>
> Nello spazio (schema proposto, non disegnato a lezione): la retta r per P incontra α nel punto H ad angolo retto, e le sue proiezioni risultano perpendicolari alle tracce del piano.

### 6.1.2 Senza tracce: con l'orizzontale e la frontale (20 ottobre)

Se il piano è dato da una figura e non si hanno le tracce, si torna alla prima definizione: la retta è perpendicolare al piano quando è perpendicolare a due rette del piano. Le rette che vengono in soccorso sono l'orizzontale e la frontale.

La perpendicolare si costruisce imponendo l'angolo retto:

- tra la prima proiezione della retta e la prima proiezione dell'orizzontale (r₁ ⊥ o₁);
- tra la seconda proiezione della retta e la seconda proiezione della frontale (r₂ ⊥ f₂).

Il motivo sta ancora nei piani ausiliari:

- se per la retta r si fa passare un piano proiettante in seconda, r₂ coincide con la sua seconda traccia, che è perpendicolare a f₂;
- se si fa passare un piano proiettante in prima, r₁ coincide con la sua prima traccia, perpendicolare a o₁.

Le condizioni sono più facili di quello che sembrano, perché sono tutte collegate.

> [!example] Disegno 45 · La perpendicolare con l'orizzontale e la frontale
> ![[06-perpendicolare-con-orizzontale-e-frontale.svg|620]]
>
> Nel triangolo ABC l'orizzontale o passa per A e B (A₂B₂ parallelo alla LT), la frontale f per A e C (A₁C₁ parallelo alla LT).
> Dal punto Q si traccia r₁ perpendicolare a o₁ e r₂ perpendicolare a f₂: r è perpendicolare a due rette del piano, quindi al piano.

## 6.2 I piani perpendicolari (20 ottobre)

### 6.2.1 La condizione (20 ottobre)

Due piani sono perpendicolari tra loro se uno dei due contiene una retta perpendicolare all'altro.

### 6.2.2 Due piani proiettanti (20 ottobre)

Per i piani proiettanti la verifica è immediata. Un quaderno aperto e messo in piedi sul banco dà due piani proiettanti in prima, e le loro tracce sul banco sono le prime tracce: quando le due metà sono ortogonali, l'angolo di 90° sta a terra, su π₁.

Due piani proiettanti in prima sono quindi perpendicolari se le loro prime tracce sono perpendicolari. È un fatto, non un'interpretazione, ma vale solo perché si tratta di due piani particolari: con un piano generico non si può fare.

Lo stesso vale per due piani proiettanti in seconda, che sono perpendicolari se lo sono le loro seconde tracce.

Si può comunque verificare la condizione, cercando nel piano δ una retta perpendicolare a γ:

- per essere perpendicolare a γ la retta deve avere r₂ perpendicolare a t₂γ, che è perpendicolare alla LT, quindi r₂ è parallela alla LT: è un'orizzontale;
- per appartenere a δ, che è proiettante in prima, deve avere r₁ sulla prima traccia, quindi r₁ ≡ t₁δ, che è perpendicolare a t₁γ.

δ contiene una retta perpendicolare a γ, e i due piani sono perpendicolari.

> [!example] Disegno 46 · Due piani proiettanti in prima perpendicolari
> ![[06-piani-proiettanti-perpendicolari.svg|560]]
>
> γ e δ hanno le seconde tracce perpendicolari alla LT e l'angolo retto tra le prime tracce t₁γ e t₁δ.
> La retta r di δ, con r₁ ≡ t₁δ e r₂ parallela alla LT, ha r₁ ⊥ t₁γ e r₂ ⊥ t₂γ, quindi r ⊥ γ.
>
> ![[b06-spazio-piani-perpendicolari.svg|600]]
>
> Nello spazio (schema proposto, non disegnato a lezione): le due metà del quaderno sono verticali e l'angolo retto si vede sul banco, tra t₁γ e t₁δ.

> [!example] Disegno 47 · Due piani proiettanti in seconda perpendicolari
> ![[b06-piani-proiettanti-in-seconda-perpendicolari.svg|560]]
>
> Schema proposto, non disegnato a lezione.
> β ed ε hanno le prime tracce perpendicolari alla LT e l'angolo retto tra le seconde tracce.
> La frontale r di ε, con r₂ ≡ t₂ε e r₁ parallela alla LT, è perpendicolare a β.

### 6.2.3 Un piano perpendicolare a un piano generico (20 ottobre)

Si può disegnare un piano generico perpendicolare a un piano generico, ma è abbastanza complicato.

Serve invece un piano facile, perpendicolare a quello dato, che dimostri anche la proprietà, cioè che contenga una retta perpendicolare all'altro piano. È proprio ciò che servirà nei ribaltamenti.

Si usa un piano ausiliario γ proiettante in prima, imponendo la regola: t₁γ perpendicolare a t₁α. Il proiettante in prima non va usato in modo acritico, ma in modo cosciente, con questa condizione.

Per dimostrare che α e γ sono perpendicolari si usa un'orizzontale di α:

- la sua prima proiezione, parallela a t₁α, è perpendicolare a t₁γ;
- la sua seconda proiezione, parallela alla LT, è perpendicolare a t₂γ.

Quell'orizzontale è quindi perpendicolare a γ, e i due piani sono perpendicolari.

> [!example] Disegno 48 · Un piano proiettante in prima perpendicolare a un piano generico
> ![[06-piano-perpendicolare-al-generico.svg|560]]
>
> Il piano γ ha t₁γ ⊥ t₁α (si segnano i 90°) e t₂γ perpendicolare alla LT.
> L'orizzontale di α ha o₁ ⊥ t₁γ e o₂ ⊥ t₂γ. Nello schema c'è anche la verifica inversa: la retta r di γ, con r₁ ≡ t₁γ e r₂ ⊥ t₂α, è perpendicolare ad α.

---

## Collegamenti

Il capitolo successivo è [[PO 7 - Figure piane e solidi]]. Il capitolo precedente è [[PO 5 - L'appartenenza]].
