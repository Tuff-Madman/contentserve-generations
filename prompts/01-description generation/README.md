# description generation

In diesem Ordner findest du Prompts zur automatischen Beschreibungserstellung.

## Struktur

- **Hauptprompt**: Der zentrale Prompt für die Beschreibungserstellung.
- **Baseline Prompt**: Ein einfacher Vergleichsprompt.
- **Promptmodule**: Zusätzliche Module, nummeriert mit 01, 02 usw., die in den Hauptprompt integriert werden können.

## Beispiel

### Baseline Prompt
```
Schreibe eine einfache Beschreibung für das Thema.
```

### Haupt-Prompt (zusammengesetzt)
```
Nutze die Module 01 und 02, um eine ausführliche Beschreibung zu generieren:
[Modul 01]
[Modul 02]
```
