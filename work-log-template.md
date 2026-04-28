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


## Week 1

### Day 1

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 2

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






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













