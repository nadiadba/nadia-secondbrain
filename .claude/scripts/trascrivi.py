"""Trascrive le registrazioni delle lezioni con Whisper (versione per Mac Apple Silicon).

Uso:
  "$HOME/Library/Application Support/sbobine-whisper/.venv/bin/python" \
      .claude/scripts/trascrivi.py CARTELLA_USCITA audio1.m4a [audio2.m4a ...]

Per ogni audio scrive CARTELLA_USCITA/<nome audio>.txt, il testo a paragrafi.
L'ambiente Python (.venv con mlx-whisper, faster-whisper e av==13.1.0) sta in
~/Library/Application Support/sbobine-whisper/: vedi CLAUDE.md per reinstallarlo.
"""
import re
import sys
import time
import warnings
from pathlib import Path

import mlx_whisper
import numpy as np
from faster_whisper import decode_audio
from faster_whisper.vad import VadOptions, get_speech_timestamps

# un pezzo di testo ripetuto 4 o piu' volte di fila ("sendsendsend...") diventa uno solo
RIPETIZIONI = re.compile(r"(.{2,40}?)(?:\s*\1){3,}")

# avvisi innocui di numpy sul Mac durante il calcolo dello spettro audio
warnings.filterwarnings("ignore", category=RuntimeWarning)

MODELLO = "mlx-community/whisper-large-v3-turbo"
# Aiuta Whisper a scrivere bene i termini tecnici dei corsi
PROMPT = (
    "Lezione universitaria di architettura, Universita' Roma Tre. "
    "Termini: ordine dorico, ionico, corinzio, trabeazione, fregio, metope, triglifi, "
    "capitello, Partenone, Acropoli, Vitruvio, Foro Romano, opus caementicium, domus, "
    "omologia, affinita', omotetia, proiezioni ortogonali, linea di terra, tracce, "
    "piano proiettante, retta orizzontale, retta frontale, geometria descrittiva."
)


def minuti(secondi):
    h, resto = divmod(int(secondi), 3600)
    m, s = divmod(resto, 60)
    return f"{h}:{m:02d}:{s:02d}"


def trascrivi(file, uscita):
    print(f"\n>> {file.name}", flush=True)
    inizio = time.time()
    audio = decode_audio(str(file), sampling_rate=16000)
    durata = len(audio) / 16000
    # Tiene solo i tratti in cui qualcuno parla: sui silenzi e sul rumore d'aula
    # Whisper si "incanta" e ripete parole a vuoto ("Grazie. Grazie.")
    parlato = get_speech_timestamps(audio, VadOptions(min_silence_duration_ms=1000, speech_pad_ms=300))
    if parlato:
        audio = np.concatenate([audio[p["start"]:p["end"]] for p in parlato])
    print(f"   durata {minuti(durata)}, di cui parlato {minuti(len(audio) / 16000)}", flush=True)
    risultato = mlx_whisper.transcribe(
        audio,
        path_or_hf_repo=MODELLO,
        language="it",
        initial_prompt=PROMPT,
        condition_on_previous_text=False,  # evita che una frase sbagliata si ripeta all'infinito
        verbose=False,
    )
    paragrafi, paragrafo = [], []
    fine_prec = 0.0
    precedente = None
    for seg in risultato["segments"]:
        testo = RIPETIZIONI.sub(r"\1", seg["text"].strip())
        if not testo or testo == precedente:
            continue
        precedente = testo
        # nuova riga dopo una pausa lunga o un paragrafo gia' lungo
        if paragrafo and (seg["start"] - fine_prec > 2.5 or len(paragrafo) >= 8):
            paragrafi.append(" ".join(paragrafo))
            paragrafo = []
        paragrafo.append(testo)
        fine_prec = seg["end"]
    if paragrafo:
        paragrafi.append(" ".join(paragrafo))
    (uscita / f"{file.stem}.txt").write_text("\n\n".join(paragrafi) + "\n", encoding="utf-8")
    print(f"   fatto in {minuti(time.time() - inizio)} (audio di {minuti(durata)})", flush=True)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    uscita = Path(sys.argv[1])
    uscita.mkdir(parents=True, exist_ok=True)
    for nome in sys.argv[2:]:
        try:
            trascrivi(Path(nome), uscita)
        except Exception as e:
            print(f"   ERRORE su {nome}: {e}", flush=True)


if __name__ == "__main__":
    main()
