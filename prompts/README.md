# Prompts

## Inhaltsverzeichnis

- [Prompts](#prompts)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Überblick](#überblick)
  - [Struktur](#struktur)
  - [📘 Was ist die Vergleichsbasis (Baseline)?](#-was-ist-die-vergleichsbasis-baseline)
  - [🎯 Warum wird sie genutzt?](#-warum-wird-sie-genutzt)
  - [⚖️ Warum ist sie bewusst nicht spezifisch?](#️-warum-ist-sie-bewusst-nicht-spezifisch)
  - [🏷️ Welche Begriffe gibt es?](#️-welche-begriffe-gibt-es)
  - [▶️ Wie nutze ich sie (essentiell)?](#️-wie-nutze-ich-sie-essentiell)
  - [Usage Example](#usage-example)
  - [Weiteres](#weiteres)

## Überblick

Dieser Ordner enthält alle Ressourcen zur Generierung und Verwaltung von Prompts.

## Struktur

- **title generation/**: Module und Tools zur automatischen Titelerstellung
- **description generation/**: Module und Tools zur Beschreibungserstellung

Jeder Bereich hat einen eigenen `modules`-Unterordner.

## 📘 Was ist die Vergleichsbasis (Baseline)?
Eine Baseline-Prompt ist die einfachste, neutrale Anweisung. So kann man prüfen,
was ohne spezielle Regeln entsteht – und Ursachen einfacher ausschließen.

## 🎯 Warum wird sie genutzt?

- Fairer Vergleich: Änderungen müssen die Referenz sichtbar übertreffen.
- Nachvollziehbarkeit: Fortschritt und Rückschritt werden erkennbar.
- Ursachenfindung: Probleme lassen sich besser zuordnen (Daten, Modell, Regeln).
- Über Zeit und Modelle vergleichbar: Gleichbleibende Basis bei Model-Updates und zwischen Modellen.

## ⚖️ Warum ist sie bewusst nicht spezifisch?

- Keine versteckten Vorteile, die Ergebnisse verfälschen.
- Stabil über Zeit, dadurch verlässliche Vergleiche.
- Klarer Trenner: Was kommt von der Änderung, was von der Basis?

## 🏷️ Welche Begriffe gibt es?

- baseline prompt / vanilla prompt: Kurzbezeichnungen für diese Vergleichsbasis.

## ▶️ Wie nutze ich sie (essentiell)?

- Unverändert lassen und stets parallel mitlaufen lassen.
- Ergebnisse immer gegen diese Referenz betrachten.
 

## Usage Example

## Weiteres

Weitere Hinweise zu Konventionen, Formatierungen oder Links zu Dokumentationen folgen hier.

