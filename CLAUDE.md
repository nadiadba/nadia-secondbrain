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

Il vault contiene solo cio' che Nadia studia: le lezioni finite e le bozze. Tutto il resto sta fuori dal repository, solo sul computer:

- audio e sbobine in `Documenti/Sbobine/` (vedi "Registrazioni e sbobine");
- slide, PDF del corso, saggi e documenti Word in `Documenti/Materiale/<materia>/` (stessi nomi di cartella del vault: `storia-architettura`, `geometria-descrittiva`, `composizione-architettonica`, `matematica`). Serve solo a Claude come fonte per le bozze.

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
        bozze/                ← riassunti dettagliati sbobina + slide, preparati da Claude
        bozze/img/            ← immagini usate nelle bozze
      geometria-descrittiva/
      composizione-architettonica/
      matematica/
  .claude/scripts/docx2md.py  ← convertitore Word → Markdown
```

Regole sulla struttura:

- Ogni materia sta in `anno-N/semestre-N/<materia>/`. Quando inizia un nuovo semestre, crea la cartella e la sua nota indice `semestre-N.md`, poi aggiorna `home.md`.
- Dentro una materia ci sono solo: la nota indice, i PDF delle lezioni finite (direttamente nella cartella, non in una sottocartella), e `bozze/`. Non creare altre sottocartelle.
- La **nota indice** di una materia ha lo stesso nome della cartella (es. `storia-architettura.md`) e ha due sezioni: **Lezioni finite** e **Bozze**. Ogni volta che aggiungi un file, aggiungilo alla nota indice nella sezione giusta con un wikilink e una riga di descrizione.
- Sul vecchio PC Windows possono esserci ancora cartelle `materiale/` dentro il vault (o sotto il vecchio percorso `docs/<materia>/materiale/`): sono ignorate da git. Il loro contenuto va portato in `Documenti/Materiale/<materia>/`, ma solo copiandolo e dopo averlo chiesto a Nadia.
- Nomi file: minuscoli, senza accenti e senza spazi, parole separate da trattini (`arco-e-volta.md`). Le lezioni finite sono i PDF di Nadia: tengono un numero progressivo e il titolo (`01 - Il tempio e gli ordini.pdf`).
- Un solo `# Titolo` in cima a ogni nota, dopo il blocco delle proprieta'.

### Materie del primo semestre (anno 1)

| Cartella | Corso | Che materiale arriva |
|----------|-------|----------------------|
| `storia-architettura` | Storia dell'architettura 1 | lezioni registrate e trascritte, slide PPT, PDF ufficiali della docente, visite (es. Via Appia), saggi da leggere |
| `geometria-descrittiva` | Geometria descrittiva | lezioni registrate, esercizi grafici (proiezioni, omologia) |
| `composizione-architettonica` | Fondamenti di composizione architettonica (laboratorio) | lezioni introduttive, esercitazioni con plastici |
| `matematica` | Matematica | ancora nulla |

## Il flusso di lavoro

**registrazione → sbobina sistemata (fuori dal vault) → bozza (in `bozze/`) → lezione finita (PDF di Nadia, nella materia)**

1. Nadia mette l'audio in `Documenti/Sbobine/audio/<materia>/`. Claude lo trascrive e sistema la sbobina in `Documenti/Sbobine/sbobine sistemate/<materia>/` (vedi "Registrazioni e sbobine"). Questo passaggio Claude lo fa sempre, appena la trascrizione e' pronta, senza aspettare che Nadia lo chieda.
2. Quando Nadia lo chiede, Claude scrive la **bozza**: il riassunto dettagliato di sbobina + slide. Sicuramente serve per Storia; per le altre materie solo se Nadia la chiede.
3. Nadia studia la bozza, la rielabora fuori da Obsidian e riporta il risultato come PDF: Claude lo mette nella cartella della materia (fuori da `bozze/`) e lo aggiunge alle Lezioni finite della nota indice. La bozza resta dov'e' finche' Nadia non dice di toglierla.

### Sbobina sistemata (fuori dal vault, `Documenti/Sbobine/sbobine sistemate/<materia>/NN-argomento.md`)

- E' la trascrizione **integrale e fedele alle parole del docente**. Non riassumere, non aggiungere contenuti, non cambiare il registro.
- Correggi solo gli errori di trascrizione, soprattutto sui termini tecnici (nomi di architetti e luoghi, parole latine e greche, termini di geometria).
- Togli le parti fuori tema (chiacchiere, problemi tecnici). Gli avvisi organizzativi utili (cosa portare, scadenze) vanno in un callout `> [!tip]` alla fine.
- Se ha senso, dividi il testo in paragrafi con titoli `##` per ritrovare gli argomenti a colpo d'occhio.
- In cima: proprieta' (`tipo: sbobina`, `corso`, `data`), `# Titolo` con materia e data, una citazione (`>`) che dice da quale registrazione viene. Niente link: e' fuori dal vault.

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

Una nota senza link e' un pallino isolato nel grafo di Obsidian. Ogni bozza deve essere collegata:

- **Subito dopo il titolo** metti un callout con le note collegate:

```markdown
> [!info] Note collegate
> Lezione finita: [[01 - Il tempio e gli ordini.pdf|Il tempio e gli ordini (PDF)]]
>
> Argomenti collegati: [[acropoli-partenone]] · [[costruzione-mondo-antico]]
```

- Quando arriva il PDF finito di un argomento, aggiungilo al callout della bozza corrispondente.
- **Quando crei una nota nuova, aggiorna anche le note vecchie** che devono puntare a lei: le bozze sugli argomenti collegati e la nota indice.
- Nella sezione `## Collegamenti`, quando citi un argomento che ha gia' una nota, trasforma la parola in link dentro la frase: `dal [[acropoli-partenone|Partenone]]`. Vale anche tra materie diverse (es. Geometria descrittiva ↔ Composizione).
- Non linkare le sbobine (sono fuori dal vault) e non inventare link a note che non esistono ancora (in Obsidian creerebbero pallini vuoti nel grafo).

## Convenzioni Markdown per Obsidian

Tutto cio' che scrivi deve essere letto in Obsidian. Usa solo la sintassi qui sotto.

### Proprieta' (frontmatter) in cima a ogni nota

```markdown
---
tipo: bozza            # bozza | indice
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

## File in ingresso: docx, PDF, slide, registrazioni

Nadia appoggia slide, PDF e documenti in `Documenti/Materiale/<materia>/` (se la cartella non c'e', creala); gli audio invece vanno in `Documenti/Sbobine/audio/<materia>/`. Da li':

### Documenti Word (.docx)

1. Se `pandoc` e' installato: `pandoc "file.docx" -t gfm --wrap=none --extract-media=. -o "file.md"`.
2. Altrimenti usa lo script del repo, che non ha dipendenze: `python3 -I .claude/scripts/docx2md.py "$HOME/Documents/Materiale/storia-architettura/file.docx" cartella-di-uscita`. Converte titoli, elenchi, grassetto, corsivo, tabelle, immagini (in `img/`) e formule di Word (in LaTeX approssimato: ricontrollale).
3. Poi rileggi il risultato e sistemalo come sbobina o bozza: proprieta', titolo, callout, immagini rinominate, sezione Collegamenti se e' una bozza.
4. Se il documento e' in un'altra lingua (inglese, francese...), traducilo in italiano mantenendo i termini tecnici originali in corsivo tra parentesi la prima volta che compaiono.
5. Il .docx originale resta in `Documenti/Materiale/`: non cancellarlo senza chiedere.

### PDF

- PDF delle lezioni finite (rielaborati da Nadia): mettili direttamente nella cartella della materia, con nome `NN - Titolo.pdf`, e linkali dalla nota indice in Lezioni finite. Restano PDF: non convertirli in testo (Obsidian li apre e permette di evidenziarli).
- PDF del corso, saggi, capitoli: leggili con lo strumento di lettura e usali come fonte per le bozze; il PDF resta in `Documenti/Materiale/<materia>/`.

### Slide (.pptx, .pdf)

- Sono fonte per le bozze: integra i contenuti nel testo, estrai gli schemi utili come immagini PNG in `img/`.

### Registrazioni e sbobine

Gli audio NON stanno nel vault: Nadia li mette nella cartella `Sbobine/` dentro Documenti, fuori dal repository, e Claude li trascrive con Whisper.

```
Documenti/Sbobine/
  audio/<materia>/              ← Nadia mette qui le registrazioni (dall'iPhone: .m4a, .mp3...)
  sbobine grezze/<materia>/     ← uscita di Whisper: <nome>.txt, a paragrafi (niente file con i minuti: a Nadia non servono)
  sbobine sistemate/<materia>/  ← sbobine sistemate da Claude: 01-tempio-e-ordini.md, 02-grecia-antica-partenone.md...
  trascrivi.py                  ← trascrive gli audio di audio/<materia>/ che non hanno ancora un .txt nelle grezze
  .venv/                        ← ambiente Python con Whisper
```

`<materia>` e' sempre una delle quattro cartelle `storia-architettura`, `geometria-descrittiva`, `composizione-architettonica`, `matematica`.

Nomi di audio e sbobine grezze: `materia gg-mm`, con ` (1)`, ` (2)` se ci sono piu' registrazioni nello stesso giorno. Esempi: `storia dell'architettura 30-09.txt`, `geometria descrittiva 06-10 (1).txt`, `composizione architettonica 28-09.txt`, `matematica 15-10.txt`. Nadia vorrebbe la data come gg/mm, ma `/` non e' ammesso nei nomi dei file: si usa il trattino. Se un audio arriva con un altro nome, rinominalo con questo schema (chiedendo la data se non e' chiara); lo script da' alla grezza lo stesso nome dell'audio.

- Su Mac (Apple Silicon): `~/Documents/Sbobine/.venv/bin/python ~/Documents/Sbobine/trascrivi.py`. Usa `mlx-whisper` con il modello `mlx-community/whisper-large-v3-turbo` sul chip grafico: circa mezz'ora per ogni ora di audio. Lancialo in background e avvisa Nadia quando finisce.
- Su Windows lo script e' in `C:\Users\Nadia\Documents\Sbobine\` e usa `faster-whisper` (modello medium, `av==13.1.0` obbligatorio: le versioni piu' nuove di `av` non funzionano). Lancialo con `$env:PYTHONIOENCODING = "utf-8"`. E' molto piu' lento.
- Quando la trascrizione finisce, senza aspettare che Nadia lo chieda, sistemala come sbobina (vedi "Il flusso di lavoro") in `sbobine sistemate/<materia>/`, con il numero progressivo successivo e la `data` nelle proprieta'. Se un audio e' finito fuori dalle cartelle delle materie, riconosci la materia dal nome o dal contenuto e spostalo; se non e' chiaro, chiedi.
- Se Nadia porta una trascrizione gia' fatta (testo o .docx), mettila in `sbobine grezze/<materia>/` con il nome secondo lo schema e parti da li'.
- `Sbobine/` non e' su GitHub: esiste solo sul computer dove e' stata creata. Non cancellare nulla da li' senza chiedere.

## Git e GitHub

- Nadia non conosce Git. **Dopo ogni lavoro concluso nel vault, salva e carica su GitHub in automatico, senza chiedere** (`git add`, `git commit`, `git push`): l'ha chiesto lei il 20/10/2026. Dille in una riga che l'hai fatto ("ho salvato le modifiche anche su GitHub").
- Sul Mac le credenziali di GitHub sono nel Portachiavi (accesso fatto da VS Code): `git push` e `git fetch` vanno lanciati fuori dalla sandbox, altrimenti non le leggono e chiedono il nome utente. Se il push fallisce comunque, spiega a Nadia di cliccare *Sincronizza modifiche* nel pannello *Controllo del codice sorgente* di VS Code.
- Messaggi di commit in italiano, prima riga all'imperativo e specifica: "Aggiungi appunti sulla costruzione nel mondo antico", "Correggi la data della lezione di geometria". Mai "." o "update".
- Prima di committare controlla con `git status` che non ci siano file grandi o finiti per sbaglio nel vault (slide, audio, sbobine). Non committare mai `.obsidian/`.
- Se il lavoro e' su un altro computer, ricorda che le modifiche arrivano con `git pull`: spiegalo se serve.

## Cose da NON fare

- Non creare file fuori dalle cartelle delle materie, tranne la configurazione (`.claude/`, `.gitignore`, `README.md`, questo file) e `Documenti/Sbobine/`
- Non toccare `.obsidian/` (configurazione personale di Obsidian, non e' nel repo). In `.obsidian/app.json` sono esclusi dal vault `modelli/`, `CLAUDE.md` e `README.md`: non annullarlo
- Non reintrodurre MkDocs, siti statici o sintassi che Obsidian non legge
- Non scrivere contenuti in lingue diverse dall'italiano (tranne citazioni e termini tecnici)
- Non eliminare la sezione Collegamenti dalle bozze
- Non riassumere o "migliorare" le sbobine: devono restare fedeli al docente
- Non usare il grassetto nel corpo delle bozze in prosa
- Non cancellare i file di `Documenti/Materiale/` e `Documenti/Sbobine/`: sono solo sul computer di Nadia e git non li protegge
