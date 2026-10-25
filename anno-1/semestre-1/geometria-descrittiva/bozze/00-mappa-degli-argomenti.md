---
tipo: bozza
corso: Geometria descrittiva
anno: 1
semestre: 1
data: 2026-10-25
tags: [geometria-descrittiva, bozza, mappa]
---

# Mappa degli argomenti di geometria descrittiva

Lo schema di che cosa sta dentro che cosa, solo con gli argomenti di geometria fatti finora (dal 6 al 22 ottobre). Più una voce è spostata a destra, più è un argomento piccolo, che sta dentro quello sopra di lei. Le voci segnate «non ancora fatto» la docente le ha solo nominate: si faranno più avanti.

> [!info] Note collegate
> Bozze: [[02-proiezioni-e-omologia-schema]] · [[03-proiezioni-ortogonali-punto-e-rette]] · [[04-rette-e-piani-nelle-varie-posizioni]] · [[05-appartenenza-e-rette-ausiliarie]] · [[06-piani-ausiliari-e-perpendicolarita]] · [[07-il-ribaltamento]]
>
> Ripasso: [[00-ripasso-prova-1]]

## 1. LE BASI: I RICHIAMI DI GEOMETRIA EUCLIDEA

[[02-proiezioni-e-omologia-schema#RICHIAMI DI GEOMETRIA EUCLIDEA|Bozza 02]]

- **Distanza** (sempre con la perpendicolare)
	- punto - retta
	- punto - piano
- **Rette e piani**
	- due rette: parallele, incidenti, sghembe
	- due piani: paralleli, incidenti
	- retta e piano: secante, parallela, perpendicolare
- **Diedro e triedro**

## 2. PROIETTARE

[[02-proiezioni-e-omologia-schema#I FONDAMENTI DELLA GEOMETRIA PROIETTIVA|Bozza 02]]

- **Che cosa serve**: un centro di proiezione S e un piano di quadro
- **Che cosa si ottiene**
	- da un punto → un raggio
	- da una retta → un fascio di rette
	- da un piano → una stella di rette
- **Gli enti impropri** (all'infinito)
	- punto improprio: dove si incontrano le rette parallele
	- centro improprio: i raggi diventano tutti paralleli

## 3. I DUE TIPI DI PROIEZIONE E I METODI CHE NE NASCONO

Tutto dipende da dove sta il centro di proiezione: al finito o all'infinito.

- **Proiezioni coniche**: il centro è proprio, i raggi partono tutti da un punto
	- la prospettiva (non ancora fatta)
- **Proiezioni cilindriche**: il centro è improprio, i raggi sono tutti paralleli
	- **le proiezioni ortogonali** (metodo di Monge): è quello che si sta facendo ora, vedi il gruppo 5
	- l'assonometria (non ancora fatta)
		- ortogonale
		- obliqua

## 4. LE PROIETTIVITÀ: LE CORRISPONDENZE TRA FIGURE PROIETTATE

[[02-proiezioni-e-omologia-schema#LA PROSPETTIVITÀ|Bozza 02]]

- **La prospettività**: un centro, due piani
	- omografia: la corrispondenza tra i punti dei due piani
- **L'omologia**: due prospettività sullo stesso piano (il foglio)
	- gli elementi: centro U, asse u, una coppia di punti A e A′
	- le due proprietà
		- i punti corrispondenti sono allineati con il centro
		- le rette corrispondenti si incontrano sull'asse
	- i tipi di omologia, divisi come le proiezioni, cioè a seconda del centro
		- **con il centro proprio** (come nelle proiezioni coniche)
			- omologia classica: centro e asse propri
			- omologia speciale: il centro sta sull'asse
			- omotetia: l'asse è improprio
		- **con il centro improprio** (come nelle proiezioni cilindriche)
			- affinità: solo il centro è improprio
				- ortogonale
				- obliqua
			- traslazione: centro e asse impropri

## 5. LE PROIEZIONI ORTOGONALI (METODO DI MONGE)

Bozze [[03-proiezioni-ortogonali-punto-e-rette|03]], [[04-rette-e-piani-nelle-varie-posizioni|04]], [[05-appartenenza-e-rette-ausiliarie|05]], [[06-piani-ausiliari-e-perpendicolarita|06]], [[07-il-ribaltamento|07]]

- **Il sistema**: tre piani di proiezione (π₁, π₂, π₃) e la linea di terra
- **Il punto**: tre proiezioni (P₁, P₂, P₃)
- **Le rette** e le loro tracce (T₁ᵣ, T₂ᵣ, T₃ᵣ)
	- proiettante in prima, proiettante in seconda
	- parallela alla linea di terra
	- frontale, orizzontale
	- di profilo
	- generica
- **I piani** e le loro tracce (t₁α, t₂α, t₃α)
	- proiettante in prima, proiettante in seconda
	- parallelo alla linea di terra
	- frontale, orizzontale
	- di profilo
	- generico
- **L'appartenenza**
	- punto - retta, retta - piano, punto - piano
	- gli aiuti: rette ausiliarie (orizzontale e frontale) e piani ausiliari
- **La perpendicolarità**
	- retta perpendicolare a un piano
	- piano perpendicolare a un piano
- **Il ribaltamento**: per vedere una figura in vera grandezza
	- dei piani proiettanti in prima e in seconda, su π₁ o su π₂
	- l'omologia di ribaltamento: è un'affinità ortogonale (gruppo 4)

## Collegamenti

I gruppi si tengono l'uno con l'altro. Dal [[02-proiezioni-e-omologia-schema|proiettare]] nascono i due tipi di proiezione, e le proiezioni ortogonali sono il caso cilindrico che si studia dalla [[03-proiezioni-ortogonali-punto-e-rette|bozza 03]] in poi. L'omologia, a sua volta, torna proprio dentro le proiezioni ortogonali, nel [[07-il-ribaltamento|ribaltamento]]. Per ripassare gli esercizi tipo c'è il [[00-ripasso-prova-1|ripasso per la Prova n.1]].
