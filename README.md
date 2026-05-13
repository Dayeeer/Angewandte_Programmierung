# Applied Programming Project – Notes API

This repository contains my final project for the Applied Programming course at Hochschule Coburg.

The project is a small note-taking application. It includes a FastAPI backend, a SQLite database, automated tests with pytest, and a simple Streamlit frontend.

---

# Main Files

- `main.py` – FastAPI backend and API endpoints
- `frontend.py` – Streamlit frontend
- `test_main.py` – main test file
- `work-log.md` – learning logbook
- `pyproject.toml` – project dependencies for uv
- `.gitignore` – excludes local files such as database files, cache and virtual environments
- `exploration/` – older experiments and practice files

---

# Features

The application can:

- create notes
- list all notes
- get a single note by ID
- update notes with PUT
- partially update notes with PATCH
- delete notes
- filter notes by category
- search notes by title or content
- filter notes by tag
- show note statistics
- display and create notes in a Streamlit frontend

---

# Note Structure

Each note contains:

```json
{
  "id": 1,
  "title": "Example Note",
  "content": "This is a test note.",
  "category": "school",
  "tags": ["python", "api"],
  "created_at": "2026-05-13T10:00:00"
}
```

---

# Allowed Categories

The API accepts only these categories:

- `general`
- `work`
- `personal`
- `school`
- `ideas`

This validation was added to keep the data clean and consistent.

---

# Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Pytest
- Streamlit
- uv

---

# Installation

Install the project dependencies with:

```bash
uv sync
```

---

# Run the FastAPI Backend

Start the API with:

```bash
uv run fastapi dev main.py
```

The API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

# Run the Streamlit Frontend

First start the FastAPI backend.

Then open a second terminal and run:

```bash
uv run streamlit run frontend.py
```

The frontend will open in the browser and allows creating and viewing notes.

---

# Example API Requests

## Create a Note

Endpoint:

```text
POST /notes
```

Example body:

```json
{
  "title": "Study FastAPI",
  "content": "Repeat endpoints, validation and tests.",
  "category": "school",
  "tags": ["python", "fastapi"]
}
```

---

## Get All Notes

Endpoint:

```text
GET /notes
```

---

## Filter Notes by Category

Endpoint:

```text
GET /notes?category=school
```

---

## Search Notes

Endpoint:

```text
GET /notes?search=fastapi
```

---

## Filter Notes by Tag

Endpoint:

```text
GET /notes?tag=python
```

---

## Get Statistics

Endpoint:

```text
GET /notes/stats
```

Example response:

```json
{
  "total_notes": 10,
  "by_category": {
    "school": 5,
    "work": 3,
    "ideas": 2
  },
  "top_tags": [
    {
      "tag": "python",
      "count": 4
    }
  ],
  "unique_tags_count": 6
}
```

---

# Development Process

During the course I started with simple Python and FastAPI exercises. Step by step, I extended the project into a more complete REST API.

The main learning steps were:

- creating basic API endpoints
- using path parameters and query parameters
- working with request bodies
- adding validation with Pydantic
- saving data in SQLite with SQLModel
- writing automated tests with pytest
- creating a simple frontend with Streamlit
- documenting the process in the work log

Please find more information about it in the `work-log.md` that contains detailed learning process, problems and solutions from the course.