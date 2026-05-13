"""
- Streamlit Installieren
- Streamlit App "Hello, World!" erstellen und testen
- "Say no" - App als ersten Test erstellen
  - API Documentation: https://github.com/hotheadhacker/no-as-a-service
  - API Endpoint: https://naas.isalman.dev/no
  - Button in Streamlit, der bei Klick eine Anfrage an den API Endpoint sendet und die Antwort anzeigt

- Todos für Nachmittag:
  - Streamlit App mit 2 Funktionen von Notizen API
  - Funktion 1: Alle Notizen anzeigen
    - Liste von Titeln von Notizen anzeigen
    - Möglichkeit zu einem Titel den Inhalt, Tags, Category, etc. anzuzeigen
  - Funktion 2: Neue Notiz erstellen (Formular mit Titel und Inhalt, Button)
    - Erstellen einer neuen Notiz (Titel, Inhalt, Tags, Category)
    - Neu erstellte Notiz soll in Liste auftauchen



import streamlit as st
import requests

URL = "https://naas.isalman.dev/no"


def request_no():
    response = requests.get(URL)
    response_json = response.json()
    return response_json["reason"]


# Initialization
if "text1" not in st.session_state:
    st.session_state["text1"] = request_no()
    print("init Text1")

if "text" not in st.session_state:
    st.session_state["text"] = request_no()
    print("init Text")

name = st.text_input("Name", placeholder="Hier Name eingeben...")
st.write(name)

if st.button("Neuer Text1"):
    st.session_state["text1"] = request_no()

st.write(st.session_state["text1"])


if st.button("Neuer Text"):
    st.session_state["text"] = request_no()

st.write(st.session_state["text"])


with st.expander("session state"):
    st.write(st.session_state)

"""

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Notes Frontend", page_icon="📝", layout="wide")

st.title("📝 Notes Frontend")
st.write("Frontend for FastAPI Notes API")

# =========================
# LOAD NOTES
# =========================


def load_notes():
    response = requests.get(f"{API_URL}/notes")

    if response.status_code == 200:
        return response.json()

    st.error("Could not load notes")
    return []


# =========================
# CREATE NOTE
# =========================


def create_note(title, content, category, tags):
    payload = {"title": title, "content": content, "category": category, "tags": tags}

    response = requests.post(f"{API_URL}/notes", json=payload)

    return response


# =========================
# SIDEBAR
# =========================

st.sidebar.header("Statistics")

try:
    stats_response = requests.get(f"{API_URL}/notes/stats")

    if stats_response.status_code == 200:
        stats = stats_response.json()

        st.sidebar.metric("Total Notes", stats["total_notes"])
        st.sidebar.metric("Unique Tags", stats["unique_tags_count"])

except:
    st.sidebar.write("Statistics unavailable")


# =========================
# CREATE NOTE FORM
# =========================

st.header("Create New Note")

with st.form("create_note_form"):

    title = st.text_input("Title")

    content = st.text_area("Content")

    category = st.selectbox(
        "Category",
        ["general", "work", "personal", "school", "ideas"]
    )

    tags_input = st.text_input("Tags (comma separated)")

    submitted = st.form_submit_button("Create Note")

    if submitted:

        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        response = create_note(title, content, category, tags)

        if response.status_code == 201:
            st.success("Note created successfully!")
            st.rerun()

        else:
            st.error(f"Error: {response.text}")


# =========================
# FILTER
# =========================

st.header("Filter Notes")

selected_category = st.selectbox(
    "Filter by category",
    ["all", "general", "work", "personal", "school", "ideas"]
)

notes = load_notes()

if selected_category != "all":
    notes = [note for note in notes if note["category"] == selected_category]


# =========================
# DISPLAY NOTES
# =========================

st.header("All Notes")

if not notes:
    st.warning("No notes found")

for note in reversed(notes):

    with st.expander(f"{note['title']} ({note['category']})"):

        st.write("### Content")
        st.write(note["content"])

        st.write("### Tags")
        st.write(note["tags"])

        st.write("### Created At")
        st.write(note["created_at"])

        st.divider()
