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

```
nadia-secondbrain/            ← vault di Obsidian
  CLAUDE.md                   ← queste istruzioni
  README.md
  home.md                     ← nota di partenza: elenca anni, semestri e materie
  guida-obsidian.md           ← guida all'uso di Obsidian scritta per Nadia
  tutte-le-note.base          ← tabella automatica di tutte le note (Obsidian Bases)
  modelli/                    ← modelli per i tre tipi di nota (plugin Modelli di Obsidian)
    lezione.md  appunti.md  sintesi.md
  anno-1/
    semestre-1/
      semestre-1.md           ← indice del semestre
      storia-architettura/
        storia-architettura.md   ← nota indice della materia (stesso nome della cartella)
        lezioni/              ← trascrizioni sistemate delle lezioni, numerate 01-, 02-...
        appunti/              ← rielaborazione in prosa, stile manuale
        appunti/img/          ← immagini usate negli appunti
        sintesi/              ← schemi di ripasso
        materiale/            ← sorgenti (registrazioni, sbobine .docx, slide, PDF): NON va su git
      geometria-descrittiva/
      composizione-architettonica/
      matematica/
  .claude/scripts/docx2md.py  ← convertitore Word → Markdown
```

Regole sulla struttura:

- Ogni materia sta in `anno-N/semestre-N/<materia>/`. Quando inizia un nuovo semestre, crea la cartella e la sua nota indice `semestre-N.md`, poi aggiorna `home.md`.
- La **nota indice** di una materia ha lo stesso nome della cartella (es. `storia-architettura.md`): fa da sommario e sostituisce il vecchio menu del sito. **Ogni volta che aggiungi una nota, aggiungila alla nota indice** nella sezione giusta (Lezioni, Appunti o Sintesi) con un wikilink e una riga di descrizione.
- La cartella `materiale/` e' ignorata da git (`.gitignore`): e' il posto dove Nadia appoggia i file di partenza. Non committarla mai e non spostarne il contenuto.
- Nomi file: minuscoli, senza accenti e senza spazi, parole separate da trattini (`arco-e-volta.md`). Le lezioni hanno un numero progressivo a due cifre (`06-argomento.md`). I PDF ufficiali dei docenti possono tenere il nome originale.
- Un solo `# Titolo` in cima a ogni nota, dopo il blocco delle proprieta'.

### Materie del primo semestre (anno 1)

| Cartella | Corso | Che materiale arriva |
|----------|-------|----------------------|
| `storia-architettura` | Storia dell'architettura 1 | lezioni registrate e trascritte, slide PPT, PDF ufficiali della docente, visite (es. Via Appia), saggi da leggere |
| `geometria-descrittiva` | Geometria descrittiva | lezioni registrate, esercizi grafici (proiezioni, omologia) |
| `composizione-architettonica` | Fondamenti di composizione architettonica (laboratorio) | lezioni introduttive, esercitazioni con plastici |
| `matematica` | Matematica | ancora nulla |

## I tre tipi di nota e il flusso di lavoro

Il flusso tipico di Nadia e': **registrazione della lezione → trascrizione grezza (la "sbobina", spesso un .docx o .txt in `materiale/`) → lezione sistemata → appunti → sintesi**. Ogni passaggio e' una nota diversa, con un `tipo` diverso nelle proprieta'.

### 1. Lezione sistemata (`lezioni/`, `tipo: lezione`)

- E' la trascrizione **integrale e fedele alle parole del docente**. Non riassumere, non aggiungere contenuti, non cambiare il registro.
- Correggi solo gli errori di trascrizione, soprattutto sui termini tecnici (nomi di architetti e luoghi, parole latine e greche, termini di geometria).
- Togli le parti fuori tema (chiacchiere, problemi tecnici). Gli avvisi organizzativi utili (cosa portare, scadenze) vanno in un callout `> [!tip]` alla fine.
- Aggiungi titoli `##` per ritrovare gli argomenti a colpo d'occhio e, subito dopo il titolo, una citazione (`>`) che spiega cos'e' la nota (vedi `modelli/lezione.md`).
- Se il docente fornisce la versione ufficiale (PDF), quella va in `lezioni/` al posto della trascrizione e viene linkata dalla nota indice con `[[nome del file.pdf|Titolo]]`.

### 2. Appunti (`appunti/`, `tipo: appunti`)

- Testo **da manuale universitario**: prosa discorsiva, paragrafi sviluppati, struttura gerarchica con `##` e `###`.
- Integra tutte le fonti disponibili: lezione, slide, letture assegnate (es. saggi), PDF ufficiali.
- **Niente grassetto nel corpo del testo**, niente elenchi o tabelle al posto della prosa, niente glossari: i termini tecnici si spiegano dentro il discorso, in corsivo se latini o greci.
- Togli i chiarimenti puramente didattici che non sono contenuto d'esame (es. "non confondete la colonna con l'ordine"): la definizione va data in forma affermativa.
- Inserisci gli schemi delle slide dove aiutano a capire (immagini in `appunti/img/`, vedi sotto).
- Chiudi sempre con due sezioni: `## Collegamenti` (prosa: come l'argomento si lega al resto del corso e agli altri corsi) e `## Per approfondire` (bibliografia: manuali del corso, fonti antiche, saggi). **Non eliminare mai la sezione Collegamenti**.
- Il modello e' `anno-1/semestre-1/storia-architettura/appunti/ordini-architettonici.md`.

### 3. Sintesi (`sintesi/`, `tipo: sintesi`)

- Schema di ripasso rapido: elenchi puntati, frasi brevi, formule, callout `> [!abstract]` per le cose da sapere a memoria.
- Una o due pagine al massimo. Si legge in dieci minuti prima dell'esame.
- Per le lezioni pratiche o organizzative (strumenti da comprare, come funziona il laboratorio) basta la sintesi, senza lezione sistemata.

## Collegare le note tra loro (fondamentale per il grafo)

Una nota senza link e' un pallino isolato nel grafo di Obsidian. Ogni nota di contenuto deve essere collegata:

- **Subito dopo il titolo** (dopo la citazione introduttiva nelle lezioni, dopo la riga descrittiva nelle sintesi) metti un callout con le note collegate:

```markdown
> [!info] Note collegate
> Appunti: [[acropoli-partenone]]
>
> Lezione precedente: [[02-grecia-antica-partenone]] · Successiva: [[04-costruzione-mondo-antico]]
```

- Lezione ↔ appunti ↔ sintesi dello stesso argomento si linkano sempre a vicenda. Le lezioni linkano anche la precedente e la successiva.
- **Quando crei una nota nuova, aggiorna anche le note vecchie** che devono puntare a lei: il callout della lezione corrispondente, la lezione precedente ("Successiva: ..."), la nota indice.
- Nella sezione `## Collegamenti` degli appunti, quando citi un argomento che ha gia' una nota, trasforma la parola in link dentro la frase: `dal [[acropoli-partenone|Partenone]]`. Vale anche tra materie diverse (es. Geometria descrittiva ↔ Composizione).
- Nelle lezioni sistemate non toccare il testo del docente: i link stanno solo nel callout iniziale.
- Non inventare link a note che non esistono ancora (in Obsidian creerebbero pallini vuoti nel grafo).

## Convenzioni Markdown per Obsidian

Tutto cio' che scrivi deve essere letto in Obsidian. Usa solo la sintassi qui sotto.

### Proprieta' (frontmatter) in cima a ogni nota

```markdown
---
tipo: lezione          # lezione | appunti | sintesi | indice
corso: Storia dell'architettura 1
anno: 1
semestre: 1
data: 2026-10-08       # data della lezione, se nota (formato AAAA-MM-GG)
tags: [storia-architettura, lezione]
---
```

Il tag della materia e' il nome della cartella. Queste proprieta' alimentano la tabella `tutte-le-note.base`, quindi scrivile sempre e con gli stessi nomi.

### Link e immagini

- Link a un'altra nota: `[[nome-file]]` oppure `[[nome-file|testo da mostrare]]`. I nomi dei file sono unici nel vault, quindi basta il nome senza percorso.
- Link a un PDF: `[[01 - Il tempio e gli ordini (versione ufficiale).pdf|Il tempio e gli ordini]]`.
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

- Grassetto `**testo**` (solo nelle sintesi e negli indici, non nel corpo degli appunti), corsivo `*testo*`.
- Elenchi `-` e `1.`, checklist `- [ ]` / `- [x]`, tabelle con `|`, note a pie' di pagina `[^1]`.
- Diagrammi Mermaid in un blocco ```` ```mermaid ```` (Obsidian li disegna).
- Citazioni con `>`.

### Da NON usare (sintassi del vecchio sito, in Obsidian non funziona)

- `!!! note "Titolo"` con testo indentato → usa i callout `> [!note]`
- Schede `=== "Tab"`, attributi `{: .classe }`, `--8<--`
- Link relativi con percorso `[testo](../../materia/file.md)` → usa i wikilink `[[file]]`
- Niente file `index.md`: la nota indice ha il nome della cartella

## File in ingresso: docx, PDF, slide, registrazioni

Nadia appoggia i file in `materiale/` della materia (se la cartella non c'e', creala). Da li':

### Documenti Word (.docx)

1. Se `pandoc` e' installato: `pandoc "file.docx" -t gfm --wrap=none --extract-media=. -o "file.md"`.
2. Altrimenti usa lo script del repo, che non ha dipendenze: `python3 -I .claude/scripts/docx2md.py "materiale/file.docx" cartella-di-uscita`. Converte titoli, elenchi, grassetto, corsivo, tabelle, immagini (in `img/`) e formule di Word (in LaTeX approssimato: ricontrollale).
3. Poi rileggi il risultato e sistemalo come nota del tipo giusto: proprieta', titolo, callout, immagini rinominate, sezione Collegamenti se sono appunti.
4. Se il documento e' in un'altra lingua (inglese, francese...), traducilo in italiano mantenendo i termini tecnici originali in corsivo tra parentesi la prima volta che compaiono.
5. Il .docx originale resta in `materiale/`: non cancellarlo senza chiedere.

### PDF

- PDF ufficiali del docente: lasciali come PDF in `lezioni/` (Obsidian li apre e permette di evidenziarli) e linkali dalla nota indice. Convertirli in testo fa perdere l'impaginazione: Nadia ha gia' provato e ha preferito il PDF.
- PDF da studiare (saggi, capitoli): leggili con lo strumento di lettura e usali come fonte per gli appunti; il PDF resta in `materiale/`.

### Slide (.pptx, .pdf)

- Sono fonte per gli appunti: integra i contenuti nel testo, estrai gli schemi utili come immagini PNG in `img/`.

### Registrazioni e trascrizioni

- Claude non trascrive audio. Nadia produce la trascrizione con un altro strumento e la mette in `materiale/` (testo o .docx); da li' nasce la lezione sistemata.

## Git e GitHub

- Nadia non conosce Git. Dopo un lavoro concluso, **proponi** di salvare su GitHub e, se dice si', esegui tu: `git add`, `git commit`, `git push`. Spiega in una riga cosa stai facendo ("salvo una copia delle modifiche e la carico su GitHub").
- Messaggi di commit in italiano, prima riga all'imperativo e specifica: "Aggiungi appunti sulla costruzione nel mondo antico", "Correggi la data della lezione di geometria". Mai "." o "update".
- Prima di committare controlla con `git status` che non ci siano file di `materiale/` o file grandi. Non committare mai `.obsidian/`.
- Se il lavoro e' su un altro computer, ricorda che le modifiche arrivano con `git pull`: spiegalo se serve.

## Cose da NON fare

- Non creare file fuori dalle cartelle degli appunti, tranne la configurazione (`.claude/`, `.gitignore`, `README.md`, questo file)
- Non toccare `.obsidian/` (configurazione personale di Obsidian, non e' nel repo). In `.obsidian/app.json` sono esclusi dal vault `modelli/`, `CLAUDE.md` e `README.md`: non annullarlo
- Non reintrodurre MkDocs, siti statici o sintassi che Obsidian non legge
- Non scrivere contenuti in lingue diverse dall'italiano (tranne citazioni e termini tecnici)
- Non eliminare la sezione Collegamenti dagli appunti
- Non riassumere o "migliorare" le lezioni sistemate: devono restare fedeli al docente
- Non usare il grassetto nel corpo degli appunti
- Non cancellare i file di `materiale/` e non spostare le cartelle `materiale/`: sono solo sul computer di Nadia e git non le protegge
