# Work Log

**Student Name: Yeromina Daria** 

This document describes my learning progress and development process during the Applied Programming course at Hochschule Coburg.

The project evolved step by step from simple FastAPI endpoints into a complete Notes API with database integration, automated testing and a Streamlit frontend.

# Table of Contents

- Week 1 – Day 1
- Week 1 – Day 2
- Week 1 – Day 3
- Week 2 – Day 4
- Week 2 – Day 5
- Week 2 – Day 6
- Week 3 – Day 7
- Week 3 – Day 8

# Week 1, Day 1 

## ✅ What did I accomplish?

Am ersten Kurstag habe ich meine Entwicklungsumgebung erfolgreich eingerichtet und meine erste API mit FastAPI erstellt.

Set up:

Ich habe Git, VS Code und den Paketmanager uv installiert bzw. überprüft. Die Installation verlief problemlos, da ein Teil der Tools bereits vorhanden war.

Umsetzung der API:

Ich habe eine FastAPI-Anwendung erstellt und mehrere Endpoints implementiert:

/ → erste Aufruf 
/status → Status und Version der API
/about → Informationen über das Projekt
/square/{number} → Berechnung des Quadrats
/double/{number} → Verdopplung einer Zahl
/student → persönliche Informationen
/name/{name} → Begrüßung + Name

Zusätzlich habe ich einen eigenen Endpoint erstellt:

@app.get("/even/{number}")
def check_even(number: int):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return {
        "number": number,
        "type": result
    }

Dieser überprüft, ob eine Zahl gerade oder ungerade ist.

Ich habe alle Endpoints über /docs getestet und sie funktionieren korrekt.

Außerdem habe ich mein Verständnis darüber erweitert, was eine API ist, wie FastAPI funktioniert und wo APIs in der Praxis eingesetzt werden


## 2. 🚧 What challenges did I face?

Die Einrichtung der Umgebung verlief ohne Probleme.

Während der Umsetzung hatte ich kleinere Schwierigkeiten mit:

- neuer Syntax (z. B. @app.get, Dictionaries, f-strings)
- kleinen Fehlern wie Einrückungen oder Tippfehlern
- Verständnis von Path-Parametern ({number}, {name})

## 3. 💡 How did I overcome them?

Ich habe die Probleme gelöst, indem ich:

- den Code Schritt für Schritt getestet habe
- Fehlermeldungen gelesen und korrigiert habe
- mir die Syntax mit Hilfe von AI erklären lassen habe


# Week 1, day 2 

## 1. ✅ What did I accomplish?

Am zweiten Kurstag habe ich die Grundlagen von Python vertieft und eine Note-Taking API mit FastAPI erweitert.

Ich habe gelernt:

- Variablen und Datentypen (str, int, list, dict)
- Funktionen und deren Aufbau (Parameter, return)
- F-Strings zur Formatierung von Text
- Unterschied zwischen GET und POST
- JSON als Datenformat für APIs

Außerdem habe ich meine API erweitert:

- POST /notes → Notizen erstellen
- GET /notes → alle Notizen anzeigen
- GET /notes/{note_id} → einzelne Notiz abrufen

Zusätzlich habe ich:

- Kategorien zu Notizen hinzugefügt
- Notizen in einer JSON-Datei gespeichert (notes.json)
- Daten persistent gemacht (bleiben nach Neustart erhalten)


## 2. 🚧 What challenges did I face?

 1 
Ein größeres Problem trat nach der Erweiterung mit dem Feld category auf.
Die bereits gespeicherten Notizen enthielten dieses Feld nicht, wodurch ein 500 Internal Server Error entstand.


 2
Ein weiteres Problem trat bei der Definition der Endpoints auf.
Der Endpoint /notes/stats wurde nach /notes/{note_id} definiert, wodurch FastAPI die Anfrage falsch interpretiert hat.

Das führte dazu, dass der String "stats" als note_id behandelt wurde, was einen 422 Fehler (Validation Error) verursachte.


## 3. 💡 How did I overcome them?

 1 

Um das Problem zu lösen, musste ich:

- alle alten Notizen in notes.json löschen
- neue Notizen mit dem Feld category erstellen
Danach funktionierte die API wieder korrekt.

Für die Zukunft habe ich eine Verbesserung umgesetzt:
category: str = "general"

Dadurch wird automatisch eine Standardkategorie gesetzt, falls keine angegeben wird.
So bleiben auch ältere oder unvollständige Daten kompatibel.

 2 
Die Lösung bestand darin, die Reihenfolge der Endpoints zu ändern:
spezifischere Routen (z. B. /notes/stats) müssen vor allgemeinen Routen (/notes/{note_id}) definiert werden
Nach der Anpassung funktionierte der Endpoint korrekt.


# Week 1, day 3

## 1. ✅ What did I accomplish?

Am dritten Tag habe ich meine bestehende Note API gezielt erweitert und an die REST-Prinzipien angepasst.

Zunächst habe ich den Unterschied zwischen Path-Parametern und Query-Parametern praktisch umgesetzt:

- Path-Parameter zur Identifikation einzelner Ressourcen (/notes/{id})
- Query-Parameter zur Filterung von Listen (/notes?category=...)

Darauf aufbauend habe ich den bestehenden GET-Endpoint so erweitert, dass er mehrere Filter gleichzeitig unterstützt:

- Kategorie
- Suchbegriff (Titel und Inhalt)
- Tags
- Datumsbereich

Ein weiterer wichtiger Schritt war die Einführung von Tags als zusätzliches Datenfeld sowie die Implementierung von Resource Relationships:

/tags → Liste aller Tags
/tags/{tag}/notes → alle Notizen mit einem bestimmten Tag

Zusätzlich habe ich neue Endpoints für Kategorien als eigene Ressource ergänzt:

/categories
/categories/{category}/notes

Ich habe außerdem einen Statistik-Endpunkt (/notes/stats) implementiert, der:

- die Gesamtanzahl der Notizen
- die Verteilung nach Kategorien
- die meistgenutzten Tags
- die Anzahl der eindeutigen Tags

berechnet.

Ein weiterer zentraler Bestandteil war die Implementierung von PUT und PATCH:

- PUT für vollständige Updates
- PATCH für partielle Updates einzelner Felder

Der größte Schritt war die Migration von JSON-Dateien zu einer SQLite-Datenbank mit SQLModel.
Dabei habe ich:

- Datenbankmodelle (Note, Tag) definiert
- eine Many-to-Many-Beziehung zwischen Notizen und Tags umgesetzt
- mit Sessions (SessionDep) gearbeitet
- alle bisherigen Endpoints auf Datenbankabfragen umgestellt

Zusätzlich habe ich meinen Code in der Datei `main.py` neu strukturiert, um eine bessere Übersicht und Wartbarkeit zu erreichen.  
Ich habe die einzelnen Komponenten klar getrennt (z. B. Datenbankmodelle, API-Modelle, Endpoints) und die Reihenfolge so angepasst, dass der Aufbau logisch nachvollziehbar ist.  

Diese Struktur erleichtert nicht nur das Verständnis, sondern auch zukünftige Erweiterungen der API.

Dadurch arbeitet die API jetzt mit einer echten Datenbank und ist deutlich realistischer aufgebaut.


## 2. 🚧 What challenges did I face?

Eine der ersten Herausforderungen war, dass der Server nicht gestartet ist aufgrund eines fehlenden Pakets:

ModuleNotFoundError: No module named 'sqlmodel'

Das Problem lag darin, dass die neue Datenbanktechnologie zwar im Code integriert war, aber die entsprechende Bibliothek noch nicht installiert war.

Ein weiteres Problem war das Verständnis der Datenmigration von JSON zur Datenbank.
Zunächst war unklar, warum Änderungen nicht mehr in der JSON-Datei sichtbar waren.
Das hat zu Verwirrung geführt, weil ich zunächst davon ausgegangen bin, dass beide Speicher gleichzeitig verwendet werden.

Zusätzlich hatte ich ein Problem damit, dass ich die Datenbankdatei notes.db zwar im Projekt hatte, aber nicht direkt sehen oder verstehen konnte, wie die Daten strukturiert sind.
Ohne visuelle Darstellung war es schwierig zu überprüfen, ob die Beziehungen zwischen Notizen und Tags korrekt gespeichert wurden.

Auch die Umsetzung der Tag-Beziehungen (Many-to-Many) war anspruchsvoll.
Besonders schwierig war:

doppelte Tags zu vermeiden
Tags konsistent zu speichern (z. B. Groß-/Kleinschreibung)
sicherzustellen, dass Tags korrekt mit mehreren Notizen verknüpft sind

Zusätzlich gab es Schwierigkeiten bei der Implementierung von kombinierten Filtern.
Wenn mehrere Query-Parameter gleichzeitig verwendet wurden, war es nicht sofort klar, wie diese logisch korrekt miteinander kombiniert werden müssen.

Auch der Unterschied zwischen PUT und PATCH war anfangs nicht eindeutig.
Vor allem bei PATCH war es schwierig sicherzustellen, dass nur die übergebenen Felder geändert werden und alle anderen unverändert bleiben.




## 3. 💡 How did I overcome them?

Das Problem mit dem fehlenden Paket habe ich direkt über die Installation gelöst:

pip install sqlmodel

Danach konnte der Server korrekt starten und die Datenbank initialisiert werden.

Um die Migration besser zu verstehen, habe ich gezielt Tests durchgeführt:

- überprüft, ob die Datei notes.db erstellt wird
- den Server neu gestartet und kontrolliert, ob die Daten erhalten bleiben
- getestet, ob neue Änderungen nur in der Datenbank gespeichert werden

So habe ich erkannt, dass die JSON-Datei nur einmal zur Migration verwendet wird und danach die Datenbank die einzige Datenquelle ist.

Das Problem mit der Datenbankdarstellung habe ich gelöst, indem ich ein SQLite-Tool installiert habe.
Damit konnte ich:

- die Tabellenstruktur visualisieren
- die Beziehungen zwischen notes, tags und der Link-Tabelle nachvollziehen
- und überprüfen, ob die Daten korrekt gespeichert werden

Das hat mir geholfen, die Funktionsweise der Datenbank deutlich besser zu verstehen.

Die Probleme mit den Tags habe ich gelöst, indem ich:

- alle Tags vereinheitlicht habe (z. B. in Kleinbuchstaben)
- doppelte Einträge mit Sets verhindert habe
- eine „get-or-create“-Logik verwendet habe, um bestehende Tags wiederzuverwenden

Bei den Filtern bin ich systematisch vorgegangen:

zunächst jeden Filter einzeln getestet
anschließend verschiedene Kombinationen ausprobiert

Dadurch konnte ich Fehler leichter erkennen und die Logik schrittweise korrigieren.

Den Unterschied zwischen PUT und PATCH habe ich durch praktische Tests nachvollzogen:

bei PUT alle Felder bewusst überschrieben
bei PATCH nur einzelne Felder geändert und überprüft, ob die restlichen Daten unverändert bleiben

Durch diesen direkten Vergleich konnte ich das Verhalten klar verstehen und korrekt implementieren.



# Week 2, day 4 

## 1. ✅ What did I accomplish?

Am vierten Tag habe ich mich vollständig auf das Thema Testing von APIs konzentriert und gelernt, wie man bestehende API-Funktionalität systematisch überprüft.

In der Vorlesung habe ich zunächst anhand eines einfachen Beispiels verstanden, wie man mit pytest und der Requests Library API-Endpunkte testet. Dabei wurden grundlegende Tests für einfache Endpoints implementiert, um den Ablauf von automatisierten Tests zu verstehen.

Auf dieser Grundlage habe ich zu Hause meine bereits bestehende Note API (aus den vorherigen Tagen) verwendet und eine vollständige Test-Suite dafür entwickelt. Der Fokus lag darauf, alle vorhandenen Funktionen gezielt zu überprüfen.

Ich habe Tests für folgende Bereiche erstellt:

- CRUD-Operationen (Erstellen, Abrufen,Aktualisieren, Löschen)
- Filterlogik, inklusive Kombination mehrerer Query-Parameter
- Datum-basierte Filterung
- Statistik-Endpunkt (/notes/stats)
- Kategorie- und Tag-Endpoints
- Unterschied zwischen PUT und PATCH
- Fehlerfälle, z. B. nicht existierende Ressourcen oder ungültige Eingaben

Besonders wichtig war dabei, die Tests so zu strukturieren, dass sie unabhängig voneinander funktionieren und realistische Nutzungsszenarien abbilden.

Am Ende konnte ich meine komplette API automatisiert testen und sicherstellen, dass alle Funktionen stabil und korrekt arbeiten.


## 2. 🚧 What challenges did I face?

Eine konkrete Schwierigkeit war, dass meine Tests anfangs fehlschlugen, obwohl die API im Browser korrekt funktionierte.
Das Problem lag daran, dass der Server während des Testlaufs nicht aktiv war, wodurch die Requests keine Verbindung herstellen konnten.

Ein weiteres Problem trat bei der Filterlogik in den Tests auf.
Ich habe zunächst feste Werte verwendet, wodurch Tests teilweise unerwartete Ergebnisse lieferten, da bereits vorhandene Daten in der Datenbank diese Werte beeinflusst haben.

Zusätzlich hatte ich Schwierigkeiten bei der Validierung der Response-Daten.
Einige Tests sind fehlgeschlagen, weil ich versucht habe, exakte Werte zu vergleichen, obwohl sich bestimmte Daten dynamisch ändern (z. B. generierte IDs oder Zeitstempel).

Auch der Umgang mit PATCH-Tests war anfangs nicht eindeutig.
Ich musste sicherstellen, dass wirklich nur die übergebenen Felder geändert werden und alle anderen Daten unverändert bleiben.


## 3. 💡 How did I overcome them?

Das Problem mit dem nicht erreichbaren Server habe ich gelöst, indem ich konsequent mit zwei Terminals gearbeitet habe:

- ein Terminal für den laufenden Server (uvicorn main:app --reload)
- ein zweites Terminal für das Ausführen der Tests (pytest)

Dadurch konnten die Tests korrekt auf die API zugreifen.

Die Probleme mit den Filtern habe ich gelöst, indem ich meine Tests auf dynamische Daten umgestellt habe.
Ich habe eindeutige Werte verwendet, sodass jeder Test unabhängig ist und keine Konflikte mit bestehenden Daten entstehen.

Bei der Validierung der Responses habe ich meine Teststrategie angepasst:

- statt exakter Gleichheit habe ich überprüft, ob bestimmte Felder vorhanden sind
- und ob die Werte logisch korrekt sind (z. B. ob ein Tag enthalten ist oder die Kategorie stimmt)

Den Unterschied zwischen PUT und PATCH habe ich durch gezielte Tests klar herausgearbeitet:

- bei PUT habe ich bewusst alle Felder überschrieben
- bei PATCH habe ich nur einzelne Felder geändert und anschließend überprüft, ob die restlichen unverändert bleiben



# Week 2, day 5

## 1. ✅ What did I accomplish?

Am fünften Tag lag der Fokus auf Datenvalidierung mit Pydantic sowie auf der Vertiefung von automatisierten Tests.

Während der Vorlesung habe ich zunächst den grundlegenden Ansatz zur Validierung von Eingabedaten kennengelernt. Dabei wurde gezeigt, wie man mit Pydantic:

- Eingaben einschränkt (z. B. Mindestlängen)
- Werte normalisiert (z. B. lowercase, trim)
- unerlaubte Felder blockiert
- und logische Regeln zwischen Feldern definiert

Anschließend habe ich meine bestehende Note API (aus den vorherigen Tagen) erweitert und eine strikte Validierung implementiert, unter anderem für:

- title (keine leeren oder zu kurzen Strings)
- category (nur definierte Werte erlaubt)
- tags (Begrenzung der Anzahl, keine Duplikate, Normalisierung)
- zusätzliche logische Regeln (z. B. bestimmte Tags für bestimmte Kategorien)

Darauf aufbauend habe ich eine eigene Test-Suite für die Validierung erstellt (test_validation.py).
Diese überprüft systematisch:

- korrekte Eingaben
- fehlerhafte Eingaben (422)
- Normalisierung von Daten
- Verhalten von PATCH

Alle Tests konnten am Ende erfolgreich ausgeführt werden (16/16 bestanden).

Zusätzlich habe ich im Unterricht mit einem Kommilitonen Tests ausgetauscht und dessen test_day4.py lokal ausgeführt, um die Kompatibilität zu prüfen.



## 2. 🚧 What challenges did I face?

Beim Ausführen der Tests meines Kommilitonen sind nur 2 von 8 Tests erfolgreich durchgelaufen.
Die restlichen Tests sind aus mehreren konkreten Gründen fehlgeschlagen:

- Nicht vorhandene Endpoints
Die Tests erwarteten Endpoints wie:

/greetings/{name}
/is-adult/{age}

Diese existieren in meiner API nicht, da ich eine andere Struktur (Notes API) verwende.
Dadurch kam es zu 404 Not Found Fehlern.

- Falsche erwartete Response-Werte
Ein Test erwartete z. B.:

"Hello ... World!"

während meine API:

"Hello, World"

zurückgibt.
Dadurch sind Assertions fehlgeschlagen, obwohl die Funktion grundsätzlich korrekt war.

- Fehler im Test-Code selbst
In der Funktion test_note_lifecycle_adjusted() wurde eine Variable fake verwendet, die nicht definiert war:

fake.sentence(...)

Stattdessen war nur name_faker = Faker() vorhanden.
Dies führte zu einem NameError.

- Widersprüchliche Testlogik
Einige Tests erwarteten für denselben Fall unterschiedliche Statuscodes (z. B. 200 vs. 400 bei Altersvalidierung), wodurch sie selbst logisch inkonsistent waren.

Diese Kombination hat gezeigt, dass die Tests nicht für meine API geschrieben wurden, sondern für ein anderes Beispielprojekt.



Eine weitere konkrete Schwierigkeit hatte ich bei der Implementierung der Validierung für Kategorien und Tags.

In den ersten Versuchen wurden gültige Eingaben fälschlicherweise als ungültig erkannt.
Zum Beispiel wurde folgende Eingabe:

{
  "title": "Test Note",
  "content": "test",
  "category": "WORK",
  "tags": ["Test", "Work"]
}

abgelehnt, obwohl sie eigentlich gültig sein sollte.

Das Problem lag daran, dass die Validierung case-sensitive war und keine Normalisierung stattgefunden hat.
Dadurch wurden nur exakt passende Werte akzeptiert (z. B. "work"), während "WORK" oder " Work " zu Fehlern führten.


## 3. 💡 How did I overcome them?

Zunächst habe ich die Fehlermeldungen systematisch analysiert und jeden Test einzeln betrachtet, um die Ursache zu verstehen.

- Die fehlenden Endpoints habe ich testweise ergänzt, indem ich:

/greetings/{name} implementiert habe
/is-adult/{age} hinzugefügt habe

Dadurch konnten die entsprechenden 404-Fehler behoben werden.

- Den Fehler mit der undefinierten Variable habe ich direkt im Test-Code korrigiert:

fake = Faker()

Dadurch konnte der NameError behoben werden.

- Die falschen erwarteten Response-Werte habe ich angepasst, sodass die Tests mit den tatsächlichen Rückgaben der API übereinstimmen.

- Zusätzlich habe ich die widersprüchlichen Tests überprüft und die Logik vereinheitlicht, sodass konsistente Statuscodes erwartet werden.

Nach diesen Anpassungen konnte ich die Tests erneut ausführen und sie liefen erfolgreich durch.

Allerdings habe ich bewusst entschieden, diese Änderungen nicht dauerhaft in meinem Projekt zu behalten.
Der Grund ist, dass diese Tests und Endpoints nicht zu meiner aktuellen API-Struktur passen.

Daher habe ich:

meine Änderungen rückgängig gemacht
den ursprünglichen Zustand meiner API wiederhergestellt
und mich weiterhin auf meine eigene, konsistente Struktur mit /notes, /tags und /categories konzentriert



Um das Problem zu lösen, habe ich verschiedene Ansätze ausprobiert:

Zunächst habe ich versucht, die erlaubten Kategorien direkt zu erweitern (z. B. "WORK", "Work" usw.).
Dieser Ansatz war jedoch unübersichtlich und schwer wartbar.

Danach habe ich erkannt, dass das eigentliche Problem nicht die Validierung selbst ist, sondern die fehlende Normalisierung der Eingabedaten.

Ich habe daher die Eingaben vor der Validierung angepasst:

Kategorien werden automatisch in Kleinbuchstaben umgewandelt
führende und trailing Leerzeichen werden entfernt
Tags werden ebenfalls normalisiert und dedupliziert

Beispielsweise wird:

" WORK " → "work"

umgewandelt.

Nach dieser Anpassung wurden gültige Eingaben korrekt akzeptiert und gleichzeitig blieb die Validierung streng für tatsächlich falsche Werte.

Dieser Ansatz hat sich als deutlich stabiler und praxisnäher erwiesen, da er typische Nutzereingaben berücksichtigt und gleichzeitig saubere Daten im System garantiert.


# Week 2, day 6 

## 1. ✅ What did I accomplish?

Am sechsten Tag lag der Fokus auf zwei Themen: Python Decorators und dem Bestehen der vollständigen Referenz-Test-Suite.

Zu Beginn habe ich mich mit Decorators beschäftigt. Dabei habe ich verstanden, dass ein Decorator eine Funktion „umhüllt“ und zusätzliches Verhalten vor oder nach der eigentlichen Funktion ausführen kann. Das hat mir auch geholfen, besser zu verstehen, warum FastAPI mit Schreibweisen wie @app.get(...) arbeitet. Ein Endpoint ist also nicht einfach nur eine normale Funktion, sondern wird durch den Decorator bei FastAPI registriert.

Dafür habe ich eine eigene Datei class_based_decorator.py erstellt und einen einfachen class-based Decorator ausprobiert. Dadurch konnte ich nachvollziehen, wie __call__() verwendet wird und wie eine Funktion erweitert werden kann, ohne ihre eigentliche Logik zu verändern.

Der wichtigste Teil des Tages war anschließend die Arbeit mit der Referenz-Test-Suite des Dozenten. Ich habe die bereitgestellte test_main.py in mein Projekt übernommen, ausgeführt und die Fehlermeldungen analysiert. Am Anfang sind viele Tests fehlgeschlagen, danach habe ich die Ursachen schrittweise behoben.

Am Ende konnte ich die vollständige Test-Suite erfolgreich ausführen, sodass alle Tests bestanden haben. Dadurch habe ich bestätigt, dass meine API nicht nur mit meinen eigenen Tests funktioniert, sondern auch mit den externen Tests des Kurses kompatibel ist.



## 2. 🚧 What challenges did I face?

Die größte Herausforderung war, dass die Referenz-Test-Suite zunächst viele Fehler ausgegeben hat. Auf den ersten Blick sah es so aus, als wären sehr viele unterschiedliche Dinge kaputt. Nach genauerem Lesen der Fehlermeldungen wurde aber klar, dass viele Fehler dieselbe Ursache hatten.

Ein konkretes Problem war meine Cross-Field-Validation aus dem vorherigen Tag. Ich hatte implementiert, dass Notizen mit der Kategorie "work" zwingend den Tag "work" enthalten müssen. Die Referenztests erwarteten jedoch, dass eine Work-Notiz auch mit anderen Tags wie "urgent" oder "meeting" erstellt werden kann. Dadurch gab meine API 422 zurück, obwohl die Tests 201 Created erwarteten.

Ein weiteres Problem betraf die Datumsfilter created_after und created_before. Diese Parameter waren zunächst als normale Strings definiert. Dadurch wurden ungültige Werte wie "not-a-date" oder "2026-13-01" nicht automatisch abgelehnt, sondern einfach als Text verarbeitet. Die Referenztests erwarteten hier aber einen 422 Fehler.

Zusätzlich hatte ich ein Problem mit der Reihenfolge der Fehlerprüfung bei PUT /notes/{id}. Ein Test wollte prüfen, ob ein Update einer nicht existierenden Notiz korrekt 404 zurückgibt. Durch meine zu strenge Validierung wurde der Request aber schon vorher mit 422 abgelehnt. Dadurch konnte der eigentliche 404-Fall gar nicht erreicht werden.

Eine weitere typische Schwierigkeit war, dass die vielen Testfehler zunächst unübersichtlich waren. Einige Fehler waren echte Failures, andere waren Folgefehler aus Fixtures, weil Testdaten gar nicht erst erstellt werden konnten.



## 3. 💡 How did I overcome them?

Zuerst habe ich nicht versucht, jeden einzelnen Test isoliert zu reparieren, sondern die Fehlermeldungen nach wiederkehrenden Mustern durchsucht. Dabei habe ich erkannt, dass ein großer Teil der Fehler durch die gleiche Validierungsregel verursacht wurde.

Die Regel, dass Work-Notizen zwingend den Tag "work" enthalten müssen, habe ich entfernt, weil sie zwar als Übung zur Cross-Field-Validation sinnvoll war, aber nicht zum erwarteten API-Vertrag der Referenztests passte. Danach konnten Work-Notizen auch mit anderen sinnvollen Tags erstellt werden, und viele Tests liefen sofort weiter.

Das Problem mit den Datumsfiltern habe ich gelöst, indem ich die Query-Parameter nicht mehr als str, sondern als datetime typisiert habe. Dadurch übernimmt FastAPI/Pydantic automatisch die Validierung. Ungültige Datumswerte werden jetzt korrekt mit 422 abgelehnt, während gültige ISO-Daten weiterhin funktionieren.

Beim PUT-Problem habe ich verstanden, dass zu strenge Input-Validation manchmal verhindert, dass die eigentliche Endpoint-Logik erreicht wird. Nachdem die überstrenge Work-Tag-Regel entfernt war, konnte der Test für eine nicht existierende ID korrekt bis zur Datenbankprüfung laufen und 404 zurückgeben.

Um die vielen Fehlermeldungen besser zu verstehen, habe ich die Tests mehrfach ausgeführt und nach jeder Änderung erneut geprüft. So konnte ich sehen, welche Fehler echte Hauptursachen waren und welche nur Folgefehler. Am Ende waren alle Tests erfolgreich.


# Week 3, Day 7 

## 1. ✅ What did I accomplish?

Heute habe ich mein erstes Frontend mit Streamlit entwickelt und mit meiner bestehenden FastAPI Notes-API verbunden. Ich konnte Notes aus der SQLite-Datenbank anzeigen und neue Notes direkt über das Frontend erstellen. Zusätzlich habe ich mehrere erweiterte Funktionen eingebaut, darunter:

- Sidebar mit Statistikdaten,
- Filter nach Kategorien,
- Expander für die Anzeige einzelner Notes,
- automatische Aktualisierung nach dem Erstellen einer Note,
- Success- und Error-Messages.

Außerdem habe ich die Verbindung zwischen Frontend, Backend und Datenbank erfolgreich getestet. Zum Arbeiten habe ich KI-Unterstützung, die Streamlit-Dokumentation sowie die Python- und FastAPI-Dokumentation verwendet.


## 2. 🚧 What challenges did I face?

Ein Problem entstand bei den Kategorien im Frontend. Im Streamlit-Frontend hatte ich zusätzliche Kategorien wie study, movies und cars eingebaut, die vom Backend jedoch nicht akzeptiert wurden. Dadurch wurde beim Erstellen einer Note ein HTTP-422-Fehler zurückgegeben.

Zusätzlich ist mir aufgefallen, dass plötzlich sehr viele Notes in der Datenbank vorhanden waren. Ursache dafür waren automatisierte Tests aus den vorherigen Tagen, die beim Ausführen viele Test-Notes erstellt hatten.


## 3. 💡 How did I overcome them?

Zuerst habe ich die Fehlermeldung analysiert und überprüft, ob das Problem im Frontend oder im Backend liegt. Danach habe ich festgestellt, dass die FastAPI-Validation nur bestimmte Kategorien erlaubt. Ich habe die Kategorien im Streamlit-Frontend angepasst und die selectbox mit den erlaubten Backend-Kategorien synchronisiert. Danach funktionierte die Erstellung neuer Notes korrekt.

Bei den vielen Datenbankeinträgen habe ich geprüft, woher die zusätzlichen Notes kommen. Dabei habe ich erkannt, dass die automatisierten Tests neue Datensätze dauerhaft in notes.db gespeichert hatten. Da technisch alles korrekt funktioniert hat und die Datenpersistenz wie erwartet gearbeitet hat, habe ich die Datenbank bewusst nicht zurückgesetzt.



# Week 3, Day 8 

## 1. ✅ What did I accomplish?

Am letzten Projekttag habe ich mein gesamtes Repository final strukturiert und für die Abgabe vorbereitet.

Dabei habe ich:

- die Projektstruktur bereinigt,
- ältere Test- und Experimentdateien in einen separaten exploration-Ordner verschoben,
- eine .gitignore-Datei erstellt,
- die Kompatibilität mit den Referenzbefehlen überprüft,
- das README vollständig dokumentiert,
- sowie die Konsistenz zwischen Backend, Tests und Frontend kontrolliert.

Zusätzlich habe ich das Streamlit-Frontend nochmals verbessert und die Kategorien zwischen Frontend und Backend synchronisiert.

Ein wichtiger Teil war außerdem die finale Überprüfung der gesamten Anwendung:

uv run fastapi dev main.py
uv run pytest test_main.py -v
uv run streamlit run frontend.py

Dadurch konnte ich sicherstellen, dass das gesamte Projekt reproduzierbar und stabil ausführbar ist.


## 2. 🚧 What challenges did I face?

Eine Herausforderung war die Organisation des Repositories.

Im Laufe des Kurses hatten sich viele zusätzliche Dateien angesammelt, darunter:

- ältere Testdateien,
- experimenteller Code,
- Datenbankdateien,
- Cache-Dateien,
- und verschiedene Zwischenversionen.

Dadurch wirkte das Repository zunächst unübersichtlich.

Zusätzlich gab es erneut ein Problem mit den Kategorien im Streamlit-Frontend.
Einige auswählbare Kategorien wurden vom Backend nicht akzeptiert, wodurch weiterhin 422-Fehler entstanden.

Außerdem musste ich sicherstellen, dass alle wichtigen Dateien auf der obersten Ebene des Repositories liegen, da diese direkt bewertet werden.



## 3. 💡 How did I overcome them?

Ich habe das Repository systematisch aufgeräumt und klar strukturiert.

Nicht relevante oder experimentelle Dateien habe ich in einen separaten exploration-Ordner verschoben.
Zusätzlich habe ich eine .gitignore-Datei erstellt, damit lokale Datenbank-, Cache- und Umgebungsdateien nicht versehentlich in Git gespeichert werden.

Die Kategorien im Frontend habe ich mit den erlaubten Kategorien des Backends synchronisiert, sodass die Validierung jetzt konsistent funktioniert.

Zum Abschluss habe ich alle wichtigen Befehle mehrfach getestet und überprüft, ob das Projekt auch in einer sauberen Umgebung korrekt startet und funktioniert.





# 🎉 Congratulations! You did it! 🎓✨













