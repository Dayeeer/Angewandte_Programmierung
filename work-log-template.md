# Work Log

**Student Name: Yeromina Daria** 

### Week 1, Day 1 ###

## ✅ What did I accomplish?

Am ersten Kurstag habe ich meine Entwicklungsumgebung erfolgreich eingerichtet und meine erste API mit FastAPI erstellt.

## Set up

Ich habe Git, VS Code und den Paketmanager uv installiert bzw. überprüft. Die Installation verlief problemlos, da ein Teil der Tools bereits vorhanden war.

## Umsetzung der API

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


### Week 1, day 2 ###

### 1. ✅ What did I accomplish?

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


#### 2. 🚧 What challenges did I face?

# 1 
Ein größeres Problem trat nach der Erweiterung mit dem Feld category auf.
Die bereits gespeicherten Notizen enthielten dieses Feld nicht, wodurch ein 500 Internal Server Error entstand.


# 2
Ein weiteres Problem trat bei der Definition der Endpoints auf.
Der Endpoint /notes/stats wurde nach /notes/{note_id} definiert, wodurch FastAPI die Anfrage falsch interpretiert hat.

Das führte dazu, dass der String "stats" als note_id behandelt wurde, was einen 422 Fehler (Validation Error) verursachte.


#### 3. 💡 How did I overcome them?

# 1 

Um das Problem zu lösen, musste ich:

- alle alten Notizen in notes.json löschen
- neue Notizen mit dem Feld category erstellen
Danach funktionierte die API wieder korrekt.

Für die Zukunft habe ich eine Verbesserung umgesetzt:
category: str = "general"

Dadurch wird automatisch eine Standardkategorie gesetzt, falls keine angegeben wird.
So bleiben auch ältere oder unvollständige Daten kompatibel.

# 2 
Die Lösung bestand darin, die Reihenfolge der Endpoints zu ändern:
spezifischere Routen (z. B. /notes/stats) müssen vor allgemeinen Routen (/notes/{note_id}) definiert werden
Nach der Anpassung funktionierte der Endpoint korrekt.


### Week 1, day 3###

#### 1. ✅ What did I accomplish?

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


#### 2. 🚧 What challenges did I face?

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




#### 3. 💡 How did I overcome them?

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




---

### Day 3

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 5

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 6

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 8

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 9

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---


# 🎉 Congratulations! You did it! 🎓✨













