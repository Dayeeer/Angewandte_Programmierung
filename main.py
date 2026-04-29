from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path

app = FastAPI(
    title="Applied Programming Course HS-Coburg",
    description="Simple note management API",
    version="1.0.0",
)

### Class endpoints ###


@app.get("/")
def root():
    return {"message": "Hello, World"}


@app.get("/status")
def get_status():
    return {"status": "offline", "version": "0.2.0", "day": 1}


@app.get("/about")
def get_about():
    return {
        "project": "My First API",
        "author": "Yeromina Daria",
        "course": "Applied Programming",
    }


@app.get("/name/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}


### Homework endpoints ###


@app.get("/square/{number}")
def calculate_square(number: int):
    result = number * number
    return {
        "number": number,
        "square": result,
        "calculation": f"{number} × {number} = {result}",
    }


@app.get("/student")
def get_student():
    return {
        "name": "Daria Yeromina",
        "semester": 1,
        "course": "Wirtschaftsinformatik",
        "university": "HS Coburg",
    }


@app.get("/double/{number}")
def calculate_double(number: int):
    result = number * 2
    return {
        "number": number,
        "double": result,
        "calculation": f"{number} * 2 = {result}",
    }


@app.get("/even/{number}")
def check_even(number: int):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return {"number": number, "type": result}


############################################
### Note API Endpoints (Day 2)
############################################


class NoteCreate(BaseModel):
    title: str
    content: str


class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: str


NOTES_FILE = Path("data/notes.json")


def load_notes():
    """Load notes from JSON file and return notes list and next ID counter"""
    notes_db = []
    note_id_counter = 1

    if NOTES_FILE.exists():
        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
            notes_db = [Note(**note) for note in data]

            # Set counter to max ID + 1
            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1

    return notes_db, note_id_counter


def save_notes(notes_db):
    """Save notes to JSON file after each change"""
    # Ensure data directory exists
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, "w") as f:
        # Convert Note objects to dicts
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """Create a new note"""

    notes_db, note_id_counter = load_notes()

    new_note = Note(
        id=note_id_counter,
        title=note.title,
        content=note.content,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    notes_db.append(new_note)
    save_notes(notes_db)

    return new_note


@app.get("/notes")
def list_notes() -> list[Note]:
    """Get a list of all notes"""
    notes_db, _ = load_notes()
    return notes_db
