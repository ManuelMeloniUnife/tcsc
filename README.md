# CavedanoSpeedGraph

Questo progetto visualizza una tabella e un grafico delle velocità di una macchinina in base ai metri percorsi.

## Struttura del Progetto

```plaintext
CavedanoSpeedGraph/
├── data/
│   └── velocita.txt            # File di input con le velocità
├── src/
│   ├── __init__.py             # File per rendere src un modulo Python
│   ├── main.py                 # Script principale per eseguire il software
│   ├── grafico.py              # Modulo per la creazione del grafico
│   └── utils.py                # Modulo per funzioni utilitarie (lettura file, ecc.)
├── tests/
│   ├── __init__.py             # File per rendere tests un modulo Python
│   └── test_utils.py           # Test per le funzioni utilitarie
├── .gitignore                  # File per specificare quali file ignorare nel controllo di versione
├── README.md                   # Descrizione del progetto e istruzioni
└── requirements.txt            # Dipendenze del progetto
