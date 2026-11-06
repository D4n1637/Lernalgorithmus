# Lernalgorithmus

## Beschreibung

Ein Chatbot, der gespeicherte Fragen erkennt, passende Antworten ausgibt und durch neue Antworten erweitert werden kann. Das Wissens wird in einer JSON-Datei gespeichert.
Zudem gibt es zusätzliche Funktionen zur Verwaltung und Auswertung der Einträge.

## Funktionen

-Beantwortung gespeicherter Fragen mit zufällig ausgewählten Antworten
-Hinzufügen neuer Fragen und Antworten
-Erweiterung bestehender Antworten
-Erkennung ähnlich formulierter Fragen mithilfe eines Ähnlichkeitsvergleichs
-Löschen einzelner Antworten
-Statistische Übersicht über die Häufigkeit eingegebener Fragen
-Dauerhafte Speicherung des Wissens in einer JSON-Datei 

> [!NOTE]
> Hier steht dein Hinweis zum Projekt.

## Verwendete Technologien

- Python
- difflib (Vergleich von Texten und Zeichenfolgen)
- random (Erzeugung von Zufallszahlen)
- JSON (Datenspeicherung)

## Installation

1. Repository herunterladen oder klonen.
2. Python 3 installieren.
3. Die Python-Datei ausführen.

Es werden keine zusätzlichen Bibliotheken benötigt, da alle verwendeten Module zur Python-Standardbibliothek gehören.

## Verwendung

Nach dem Start des Programms kann zunächst ausgewählt werden, ob neue Antworten hinzugefügt werden können (Ja/Nein).

Anschließend können Fragen direkt über die Konsole eingegeben werden. Der Chatbot sucht nach passenden Einträgen in seiner Wissensdatenbank und gibt eine zufällig ausgewählte Antwort aus.

Falls eine Frage noch nicht bekannt ist, kann eine neue Antwort eingegeben werden. Der Chatbot speichert diese zusammen mit der Frage und kann sie bei zukünftigen Eingaben wiederverwenden.

Bei ähnlich formulierten Fragen schlägt der Chatbot gegebenenfalls einen bereits vorhandenen Eintrag vor.

Über die folgenden Befehle können weitere Funktionen aufgerufen werden:

    /help – Anzeige der verfügbaren Befehle

    /delete – Löschen einzelner Antworten (Passwort erforderlich --> keks)

    /statistics – Anzeige der Häufigkeit eingegebener Fragen

    exit – Beenden des Chatbots und Speichern des Wissens
