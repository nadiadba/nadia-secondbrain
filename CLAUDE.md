# CLAUDE.md — Istruzioni per il Second Brain di Nadia

## Chi e' Nadia

Nadia e' una studentessa del primo anno di Architettura all'Universita' Roma Tre (anno accademico 2026/27). E' una principiante assoluta con gli strumenti tecnici: non conosce Markdown, Git, il terminale o la programmazione. Legge e consulta gli appunti con **Obsidian**; usa Claude Code per produrli e sistemarli. Ha lavorato sia su Windows sia su Mac: non dare per scontato il sistema operativo, controlla.

Quando la aiuti:

- **Parla in italiano**, sempre
- **Spiega tutto passo passo**, come se fosse la prima volta
- **Non dare nulla per scontato**: se dici "committa", spiega anche cosa significa
- **Non usare gergo tecnico** senza spiegarlo subito dopo
- **Se Nadia chiede di fare qualcosa, falla tu direttamente** — non darle comandi da copiare/incollare a meno che non lo chieda esplicitamente

## Il progetto

Questa cartella e' il **vault di Obsidian** di Nadia (la cartella principale del repository e' il vault). Contiene gli appunti universitari in Markdown, organizzati per anno, semestre e materia. Il repository su GitHub serve solo come copia di sicurezza e per sincronizzare tra computer: **non c'e' nessun sito da pubblicare** (MkDocs e GitHub Pages sono stati rimossi a ottobre 2026).

### Struttura delle cartelle

Tutto sta dentro il vault, materia per materia: sbobine, materiale, bozze e lezioni finite.

```
nadia-secondbrain/            ← vault di Obsidian (su GitHub)
  CLAUDE.md                   ← queste istruzioni
  README.md
  home.md                     ← nota di partenza: elenca anni, semestri e materie
  guida-obsidian.md           ← guida all'uso di Obsidian scritta per Nadia
  tutte-le-note.base          ← tabella automatica delle note (Obsidian Bases)
  modelli/bozza.md            ← modello di bozza (plugin Modelli di Obsidian)
  anno-1/
    semestre-1/
      semestre-1.md           ← indice del semestre
      storia-architettura/
        storia-architettura.md         ← nota indice della materia (stesso nome della cartella)
        01 - Il tempio e gli ordini.pdf ← LEZIONI FINITE: PDF di Nadia, direttamente qui
        sbobine/              ← trascrizioni delle lezioni (01-tempio-e-ordini.md, ...): su git
        materiale/            ← slide, PDF del corso, saggi, Word: NON va su git (.gitignore)
        bozze/                ← riassunti dettagliati sbobina + slide, preparati da Claude
        bozze/img/            ← immagini usate nelle bozze
      geometria-descrittiva/
      composizione-architettonica/
      matematica/
  .claude/scripts/docx2md.py  ← convertitore Word → Markdown
```

Regole sulla struttura:

- Ogni materia sta in `anno-N/semestre-N/<materia>/`. Quando inizia un nuovo semestre, crea la cartella e la sua nota indice `semestre-N.md`, poi aggiorna `home.md`.
- Dentro una materia ci sono solo: la nota indice, i PDF delle lezioni finite (direttamente nella cartella, non in una sottocartella), `sbobine/`, `materiale/` e `bozze/`. Non creare altre sottocartelle.
- La **nota indice** di una materia ha lo stesso nome della cartella (es. `storia-architettura.md`) e ha tre sezioni: **Lezioni finite**, **Sbobine** (con la data) e **Bozze**. Ogni volta che aggiungi un file, aggiungilo alla nota indice nella sezione giusta con un wikilink e una riga di descrizione.
- `materiale/` e' ignorata da git (`.gitignore`): i file restano solo sul computer. Non committarla mai e non spostarne il contenuto.
- Nomi file: minuscoli, senza accenti e senza spazi, parole separate da trattini (`arco-e-volta.md`). Le sbobine hanno un numero progressivo in ordine di data (`06-argomento.md`). Le lezioni finite sono i PDF di Nadia: tengono un numero progressivo e il titolo (`01 - Il tempio e gli ordini.pdf`). I file del materiale tengono il nome originale.
- Un solo `# Titolo` in cima a ogni nota, dopo il blocco delle proprieta'.

### Materie del primo semestre (anno 1)

| Cartella | Corso | Che materiale arriva |
|----------|-------|----------------------|
| `storia-architettura` | Storia dell'architettura 1 | lezioni registrate e trascritte, slide PPT, PDF ufficiali della docente, visite (es. Via Appia), saggi da leggere |
| `geometria-descrittiva` | Geometria descrittiva | lezioni registrate, esercizi grafici (proiezioni, omologia) |
| `composizione-architettonica` | Fondamenti di composizione architettonica (laboratorio) | lezioni introduttive, esercitazioni con plastici |
| `matematica` | Matematica | ancora nulla |

## Il flusso di lavoro

**trascrizione di Memo Vocali (in `sbobine/`) → bozza (in `bozze/`) → lezione finita (PDF di Nadia, nella materia)**

1. Nadia registra la lezione con l'app Memo Vocali dell'iPhone, che produce da sola la trascrizione (sincronizzata sul Mac via iCloud). Nadia mette la trascrizione nella cartella `sbobine/` della materia: puo' essere un `.txt`, un `.md` o testo incollato in chat.
2. Quando arriva una trascrizione nuova, Claude la trasforma in sbobina (vedi sotto) e la aggiunge alla nota indice.
3. Quando Nadia lo chiede, Claude scrive la **bozza** usando direttamente la sbobina e le slide di `materiale/`. Sicuramente serve per Storia; per le altre materie solo se Nadia la chiede.
4. Nadia studia la bozza, la rielabora fuori da Obsidian e riporta il risultato come PDF: Claude lo mette nella cartella della materia (fuori da `bozze/`) e lo aggiunge alle Lezioni finite della nota indice. La bozza resta dov'e' finche' Nadia non dice di toglierla.

### Sbobina (`sbobine/`, `tipo: sbobina`)

- Le trascrizioni di Memo Vocali sono gia' buone: **non riscriverle e non sistemarle** se Nadia non lo chiede. Il testo resta com'e'.
- Claude aggiunge solo la cornice: rinomina il file `NN-argomento.md` (numero successivo in ordine di data; se e' un `.txt`, convertilo in `.md`), mette le proprieta' (`tipo: sbobina`, `corso`, `anno`, `semestre`, `data`, `tags: [<materia>, sbobina]`), il `# Titolo` con materia e data, una citazione (`>`) che dice da dove viene il testo, e il callout Note collegate (bozza, sbobina precedente e successiva).
- Se Nadia non dice la data, cercala nel nome del file o nel testo; se non c'e', chiedila.
- Le sbobine 01-05 di Storia, 01-02 di Geometria e 01 di Composizione vengono dal vecchio sistema (Whisper + sistemazione di Claude): sono trascrizioni fedeli ma ripulite.

### Bozza (`bozze/`, `tipo: bozza`)

- Testo **da manuale universitario**: prosa discorsiva, paragrafi sviluppati, struttura gerarchica con `##` e `###`.
- Integra tutte le fonti disponibili: sbobina, slide, letture assegnate (es. saggi), PDF ufficiali.
- **Niente grassetto nel corpo del testo**, niente elenchi o tabelle al posto della prosa, niente glossari: i termini tecnici si spiegano dentro il discorso, in corsivo se latini o greci.
- Togli i chiarimenti puramente didattici che non sono contenuto d'esame (es. "non confondete la colonna con l'ordine"): la definizione va data in forma affermativa.
- Inserisci gli schemi delle slide dove aiutano a capire (immagini in `bozze/img/`, vedi sotto).
- Chiudi sempre con due sezioni: `## Collegamenti` (prosa: come l'argomento si lega al resto del corso e agli altri corsi) e `## Per approfondire` (bibliografia: manuali del corso, fonti antiche, saggi). **Non eliminare mai la sezione Collegamenti**.
- Il modello e' `anno-1/semestre-1/storia-architettura/bozze/ordini-architettonici.md`.
- Per le lezioni pratiche o organizzative (strumenti da comprare, come funziona il laboratorio) la bozza puo' essere uno schema a elenchi, come `geometria-descrittiva/bozze/strumenti-e-disegno.md`.

## Collegare le note tra loro (fondamentale per il grafo)

Una nota senza link e' un pallino isolato nel grafo di Obsidian. Ogni bozza e ogni sbobina deve essere collegata:

- **Subito dopo il titolo** metti un callout con le note collegate:

```markdown
> [!info] Note collegate
> Sbobina: [[01-tempio-e-ordini]] · Lezione finita: [[01 - Il tempio e gli ordini.pdf|Il tempio e gli ordini (PDF)]]
>
> Argomenti collegati: [[acropoli-partenone]] · [[costruzione-mondo-antico]]
```

- Bozza ↔ sbobina dello stesso argomento si linkano sempre a vicenda; le sbobine linkano anche la precedente e la successiva.
- Quando arriva il PDF finito di un argomento, aggiungilo al callout della bozza corrispondente.
- **Quando crei una nota nuova, aggiorna anche le note vecchie** che devono puntare a lei: la sbobina precedente ("Successiva: ..."), le bozze sugli argomenti collegati e la nota indice.
- Nella sezione `## Collegamenti`, quando citi un argomento che ha gia' una nota, trasforma la parola in link dentro la frase: `dal [[acropoli-partenone|Partenone]]`. Vale anche tra materie diverse (es. Geometria descrittiva ↔ Composizione).
- Nelle sbobine non toccare il testo: i link stanno solo nel callout iniziale.
- Non inventare link a note che non esistono ancora (in Obsidian creerebbero pallini vuoti nel grafo).

## Convenzioni Markdown per Obsidian

Tutto cio' che scrivi deve essere letto in Obsidian. Usa solo la sintassi qui sotto.

### Proprieta' (frontmatter) in cima a ogni nota

```markdown
---
tipo: bozza            # bozza | sbobina | indice
corso: Storia dell'architettura 1
anno: 1
semestre: 1
data: 2026-10-08       # data della lezione, se nota (formato AAAA-MM-GG)
tags: [storia-architettura, bozza]
---
```

Il tag della materia e' il nome della cartella. Queste proprieta' alimentano la tabella `tutte-le-note.base`, quindi scrivile sempre e con gli stessi nomi.

### Link e immagini

- Link a un'altra nota: `[[nome-file]]` oppure `[[nome-file|testo da mostrare]]`. I nomi dei file sono unici nel vault, quindi basta il nome senza percorso.
- Link a un PDF: `[[01 - Il tempio e gli ordini.pdf|Il tempio e gli ordini]]`.
- Immagine semplice: `![[nome-immagine.png|400]]` (il numero e' la larghezza in pixel).
- Immagine a destra con il testo che le scorre attorno (modo gia' verificato da Nadia in Obsidian): metti l'HTML a inizio paragrafo e chiudi il blocco con un `div` di pulizia:

```markdown
<img src="img/parti-tempio.png" alt="descrizione" title="didascalia" style="float: right; width: 300px; margin: 0.3rem 0 1rem 1.5rem; border: 1px solid #ddd;"> Testo del paragrafo...

<div style="clear: both;"></div>
```

- Le immagini vanno in una cartella `img/` accanto alla nota, con nomi descrittivi (`parti-tempio.png`, non `image1.png`).

### Box colorati (callout)

```markdown
> [!note] Titolo del box
> Testo del box. Ogni riga inizia con `> `.
> Una riga vuota dentro il box si scrive con un solo `>`.
```

Tipi utili: `note`, `abstract` (teoremi, cose da ricordare), `tip` (consigli, avvisi), `warning` (attenzione), `example` (esempi svolti), `info`, `quote`, `question`, `danger`.

### Formule

Inline: `$C_nH_{2n+2}$`. Su riga a se':

```markdown
$$
\frac{a}{b} = \sqrt{2}
$$
```

Non usare `\(` `\)` e `\[` `\]`: in Obsidian non funzionano.

### Il resto

- Grassetto `**testo**` (solo negli indici e nelle bozze a schema, non nel corpo delle bozze in prosa), corsivo `*testo*`.
- Elenchi `-` e `1.`, checklist `- [ ]` / `- [x]`, tabelle con `|`, note a pie' di pagina `[^1]`.
- Diagrammi Mermaid in un blocco ```` ```mermaid ```` (Obsidian li disegna).
- Citazioni con `>`.

### Da NON usare (sintassi del vecchio sito, in Obsidian non funziona)

- `!!! note "Titolo"` con testo indentato → usa i callout `> [!note]`
- Schede `=== "Tab"`, attributi `{: .classe }`, `--8<--`
- Link relativi con percorso `[testo](../../materia/file.md)` → usa i wikilink `[[file]]`
- Niente file `index.md`: la nota indice ha il nome della cartella

## File in ingresso: docx, PDF, slide, trascrizioni

Nadia appoggia slide, PDF e documenti in `materiale/` della materia e le trascrizioni in `sbobine/` (se la cartella non c'e', creala). Se trovi file finiti nel posto sbagliato (per esempio in `Download`), riconosci la materia e spostali, dicendolo a Nadia. Da li':

### Documenti Word (.docx)

1. Se `pandoc` e' installato: `pandoc "file.docx" -t gfm --wrap=none --extract-media=. -o "file.md"`.
2. Altrimenti usa lo script del repo, che non ha dipendenze: `python3 -I .claude/scripts/docx2md.py "anno-1/semestre-1/storia-architettura/materiale/file.docx" cartella-di-uscita`. Converte titoli, elenchi, grassetto, corsivo, tabelle, immagini (in `img/`) e formule di Word (in LaTeX approssimato: ricontrollale).
3. Poi rileggi il risultato e sistemalo come sbobina o bozza: proprieta', titolo, callout, immagini rinominate, sezione Collegamenti se e' una bozza.
4. Se il documento e' in un'altra lingua (inglese, francese...), traducilo in italiano mantenendo i termini tecnici originali in corsivo tra parentesi la prima volta che compaiono.
5. Il .docx originale resta in `materiale/`: non cancellarlo senza chiedere.

### PDF

- PDF delle lezioni finite (rielaborati da Nadia): mettili direttamente nella cartella della materia, con nome `NN - Titolo.pdf`, e linkali dalla nota indice in Lezioni finite. Restano PDF: non convertirli in testo (Obsidian li apre e permette di evidenziarli).
- PDF del corso, saggi, capitoli: leggili con lo strumento di lettura e usali come fonte per le bozze; il PDF resta in `materiale/`.

### Slide (.pptx, .pdf)

- Sono fonte per le bozze: integra i contenuti nel testo, estrai gli schemi utili come immagini PNG in `img/`.

### Registrazioni e trascrizioni

- Le trascrizioni le fa Memo Vocali (vedi "Il flusso di lavoro"). Gli audio non servono e non vanno nel vault.
- Se Memo Vocali smette di sincronizzarsi tra iPhone e Mac, la causa trovata il 20/10/2026 era la Modalita' Risparmio energetico (su Mac e iPhone), che fa rinviare a iCloud i caricamenti.
- Se serve trascrivere un audio senza Memo (per esempio una registrazione fatta con il telefono di un'altra persona), sul Mac c'e' ancora Whisper: metti l'audio in `~/Documents/Sbobine/audio/<materia>/` e lancia `~/Documents/Sbobine/.venv/bin/python ~/Documents/Sbobine/trascrivi.py` in background (mlx-whisper, modello `mlx-community/whisper-large-v3-turbo`, circa mezz'ora per ogni ora di audio). La trascrizione esce in `~/Documents/Sbobine/sbobine grezze/<materia>/`: da li' crea la sbobina nel vault.

## Git e GitHub

- Nadia non conosce Git. **Dopo ogni lavoro concluso nel vault, salva e carica su GitHub in automatico, senza chiedere** (`git add`, `git commit`, `git push`): l'ha chiesto lei il 20/10/2026. Dille in una riga che l'hai fatto ("ho salvato le modifiche anche su GitHub").
- Sul Mac le credenziali di GitHub sono nel Portachiavi (accesso fatto da VS Code): `git push` e `git fetch` vanno lanciati fuori dalla sandbox, altrimenti non le leggono e chiedono il nome utente. Se il push fallisce comunque, spiega a Nadia di cliccare *Sincronizza modifiche* nel pannello *Controllo del codice sorgente* di VS Code.
- Messaggi di commit in italiano, prima riga all'imperativo e specifica: "Aggiungi appunti sulla costruzione nel mondo antico", "Correggi la data della lezione di geometria". Mai "." o "update".
- Prima di committare controlla con `git status` che non ci siano file grandi, audio o file di `materiale/`. Non committare mai `.obsidian/`.
- Se il lavoro e' su un altro computer, ricorda che le modifiche arrivano con `git pull`: spiegalo se serve.

## Cose da NON fare

- Non creare file fuori dalle cartelle delle materie, tranne la configurazione (`.claude/`, `.gitignore`, `README.md`, questo file)
- Non toccare `.obsidian/` (configurazione personale di Obsidian, non e' nel repo). In `.obsidian/app.json` sono esclusi dal vault `modelli/`, `CLAUDE.md` e `README.md`: non annullarlo
- Non reintrodurre MkDocs, siti statici o sintassi che Obsidian non legge
- Non scrivere contenuti in lingue diverse dall'italiano (tranne citazioni e termini tecnici)
- Non eliminare la sezione Collegamenti dalle bozze
- Non riassumere, riscrivere o "migliorare" le sbobine: devono restare fedeli al docente
- Non usare il grassetto nel corpo delle bozze in prosa
- Non cancellare i file di `materiale/`: sono solo sul computer di Nadia e git non li protegge
