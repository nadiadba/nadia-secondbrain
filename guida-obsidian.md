---
tipo: guida
tags: [guida]
---

# Guida a Obsidian per questo vault

Obsidian e' il programma con cui leggi e consulti gli appunti. Questa cartella (`nadia-secondbrain`) e' il tuo **vault**, cioe' la raccolta di tutte le note. Ogni nota e' un semplice file di testo che puoi aprire anche da altri programmi, ma Obsidian la mostra formattata e collega le note tra loro.

## 1. Orientarsi

- **Barra laterale sinistra**: l'icona delle cartelle mostra tutti i file (anno, semestre, materia). L'icona della lente cerca una parola in tutte le note contemporaneamente.
- **Apertura rapida**: premi Cmd+O (Mac) o Ctrl+O (Windows), scrivi qualche lettera del nome della nota e premi Invio. E' il modo piu' veloce per spostarsi.
- **Nota di partenza**: [[home]] elenca tutte le materie. Da ogni materia si arriva alle lezioni finite (i tuoi PDF) e alle bozze.
- **Indice automatico della nota**: a destra, l'icona con le tre righe ("Struttura") mostra i titoli della nota aperta: cliccane uno per saltare a quel punto.
- **Modifica e lettura**: in alto a destra c'e' un'icona (matita o libro) per passare dalla modalita' modifica alla modalita' lettura. Per studiare tieni la lettura.

## 2. I collegamenti tra le note

I link tra note si scrivono con doppie parentesi quadre, per esempio `[[ordini-architettonici]]`. Cliccandoli si apre la nota collegata. Tenendo premuto Cmd (o Ctrl) mentre passi col mouse si vede un'anteprima senza aprirla.

- **Backlink** (in basso o nella barra destra, "Link entranti"): mostra quali altre note parlano della nota che stai leggendo. Utile per scoprire collegamenti tra argomenti.
- **Vista grafo** (icona a forma di rete): disegna tutte le note come pallini collegati. I pallini piu' grandi sono gli argomenti piu' collegati.

## 3. Le proprieta' (il blocco in cima a ogni nota)

Ogni nota inizia con alcune informazioni: `tipo` (bozza, indice), `corso`, `anno`, `semestre`, `data`, `tags`. Obsidian le mostra come una tabellina in cima alla nota. Servono per filtrare e cercare:

- Clicca su un tag (per esempio `#storia-architettura`) per vedere tutte le note con quel tag.
- La nota [[tutte-le-note.base|Tutte le note]] e' una **Base**: una tabella automatica di tutte le bozze, raggruppate per materia. Puoi ordinarla e filtrarla cliccando sulle intestazioni delle colonne.

## 4. Elementi che trovi negli appunti

- **Box colorati** (callout): riquadri con un'icona, usati per teoremi, avvertenze, consigli. Si possono aprire e chiudere se hanno la freccia.
- **Formule**: scritte in notazione matematica e mostrate formattate.
- **Immagini**: gli schemi presi dalle slide, accanto al testo. Cliccando un'immagine si ingrandisce.
- **PDF**: i PDF ufficiali dei docenti si aprono direttamente dentro Obsidian e si possono evidenziare.
- **Checklist**: le caselle `[ ]` nelle note indice si spuntano cliccandoci sopra.

## 5. Creare una nota nuova

Normalmente le note le prepara Claude a partire dalle registrazioni e dai materiali. Se vuoi crearne una a mano:

1. Fai clic destro sulla cartella giusta (per esempio `bozze` dentro una materia) e scegli *Nuova nota*.
2. Dalle un nome senza accenti e con i trattini al posto degli spazi (esempio: `arco-e-volta`).
3. Premi Cmd+P (o Ctrl+P), scrivi "Modelli: inserisci modello" e scegli `bozza`: la nota si riempie con lo schema giusto.
4. Compila il campo `corso` nelle proprieta' e il titolo.

La prima volta serve dire a Obsidian dove stanno i modelli: Impostazioni, Plugin principali, Modelli, cartella `modelli`.

## 6. Dalla registrazione alla lezione finita

1. Copia la registrazione nella cartella della materia dentro `Documenti/Sbobine/audio` (per esempio `audio/storia-architettura`) e di' a Claude: "ho messo l'audio di storia del 15 ottobre, sbobinalo". Claude la trascrive (la trascrizione grezza va in `sbobine grezze`) e mette la sbobina sistemata in `sbobine sistemate`, sempre nella cartella della materia. Questa cartella resta solo sul computer e non si vede in Obsidian.
2. Le slide e i PDF del corso vanno in `Documenti/Materiale/<materia>`: anche questa cartella resta solo sul computer e non si vede in Obsidian.
3. Quando vuoi studiare un argomento, chiedi a Claude la bozza: un riassunto dettagliato di sbobina e slide, che compare nella cartella `bozze` della materia.
4. Studi la bozza, la sistemi a modo tuo fuori da Obsidian e la riporti come PDF: Claude la mette tra le lezioni finite, direttamente nella cartella della materia.

## 7. Studiare al meglio

- **Studio**: le *bozze* (il riassunto dettagliato di lezione e slide).
- **Ripasso prima dell'esame**: le *lezioni finite*, i tuoi PDF, piu' la ricerca per parola quando non ricordi un termine.
- **Canvas**: con clic destro su una cartella puoi creare un *Canvas*, una lavagna dove trascinare note e immagini per costruire mappe concettuali (utile per collegare argomenti di Storia dell'architettura tra loro).
- **Segnalibri**: clic destro su una nota, *Aggiungi ai segnalibri*, per tenere a portata di mano le note che stai studiando in questo periodo.

## 8. Salvare su GitHub

Obsidian salva le modifiche sul computer da solo. Per mandarle su GitHub (copia di sicurezza e sincronizzazione con altri computer) chiedi a Claude: "salva tutto su GitHub". In alternativa si puo' installare il plugin della community *Obsidian Git*, che lo fa in automatico ogni tot minuti: chiedi a Claude di configurarlo se vuoi.

## 9. Impostazioni consigliate (una volta sola)

- Impostazioni, File e link, *Posizione predefinita per i nuovi allegati*: "Nella sottocartella della nota corrente", nome `img`. Cosi' le immagini incollate finiscono nella cartella giusta.
- Impostazioni, File e link, *Formato link*: "Percorso piu' breve possibile".
- Impostazioni, Aspetto: scegli il tema chiaro o scuro e la dimensione del testo che ti e' comoda.
- Impostazioni, File e link, *File esclusi*: aggiungi `CLAUDE.md` e `README.md`, che sono file tecnici e non appunti.
