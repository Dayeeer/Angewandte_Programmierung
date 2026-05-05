from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def unique_title(prefix: str = "Validation Test") -> str:
    return f"{prefix} {uuid4().hex[:8]}"


def create_valid_note(client, **overrides):
    payload = {
        "title": unique_title(),
        "content": "Valid content for validation testing.",
        "category": "general",
        "tags": ["valid"],
    }
    payload.update(overrides)

    response = client.post("/notes", json=payload)
    assert response.status_code == 201
    return response.json()


# ---------------------------------------------------------------------------
# Task 1 + Task 2: NoteCreate constraints and validators
# ---------------------------------------------------------------------------


def test_create_note_rejects_short_title(client):
    response = client.post(
        "/notes",
        json={
            "title": "ab",
            "content": "Valid content",
            "category": "general",
            "tags": ["valid"],
        },
    )

    assert response.status_code == 422


def test_create_note_rejects_whitespace_title(client):
    response = client.post(
        "/notes",
        json={
            "title": "   ",
            "content": "Valid content",
            "category": "general",
            "tags": ["valid"],
        },
    )

    assert response.status_code == 422


def test_create_note_rejects_unknown_category(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "banana",
            "tags": ["valid"],
        },
    )

    assert response.status_code == 422


def test_create_note_normalizes_category(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "  SCHOOL  ",
            "tags": ["valid"],
        },
    )

    assert response.status_code == 201
    assert response.json()["category"] == "school"


def test_create_note_normalizes_tags(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "work",
            "tags": [" WORK ", "URGENT", "urgent", "Q2"],
        },
    )

    assert response.status_code == 201
    assert set(response.json()["tags"]) == {"work", "urgent", "q2"}


def test_create_note_rejects_empty_tag(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "general",
            "tags": ["valid", "   "],
        },
    )

    assert response.status_code == 422


def test_create_note_rejects_short_tag(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "general",
            "tags": ["x"],
        },
    )

    assert response.status_code == 422


def test_create_note_rejects_too_many_tags(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "general",
            "tags": [f"tag-{i}" for i in range(11)],
        },
    )

    assert response.status_code == 422


def test_create_note_forbids_extra_fields(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "general",
            "tags": ["valid"],
            "tagz": ["typo"],
        },
    )

    assert response.status_code == 422


# ---------------------------------------------------------------------------
# Task 3: Cross-field validation
# ---------------------------------------------------------------------------


def test_work_note_requires_work_tag(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "work",
            "tags": ["urgent"],
        },
    )

    assert response.status_code == 422


def test_work_note_with_work_tag_succeeds(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "work",
            "tags": ["work", "urgent"],
        },
    )

    assert response.status_code == 201
    assert "work" in response.json()["tags"]


# ---------------------------------------------------------------------------
# Task 4: NoteUpdate / PATCH validation
# ---------------------------------------------------------------------------


def test_patch_with_empty_body_succeeds(client):
    note = create_valid_note(client)

    response = client.patch(f"/notes/{note['id']}", json={})

    assert response.status_code == 200
    assert response.json()["id"] == note["id"]
    assert response.json()["title"] == note["title"]


def test_patch_with_invalid_title_fails(client):
    note = create_valid_note(client)

    response = client.patch(f"/notes/{note['id']}", json={"title": ""})

    assert response.status_code == 422


def test_patch_normalizes_category_and_tags(client):
    note = create_valid_note(client)

    response = client.patch(
        f"/notes/{note['id']}",
        json={
            "category": " IDEAS ",
            "tags": ["  IDEA  ", "idea", "todo"],
        },
    )

    assert response.status_code == 200
    assert response.json()["category"] == "ideas"
    assert set(response.json()["tags"]) == {"idea", "todo"}


# ---------------------------------------------------------------------------
# Task 5: Tag model / tag validation
# ---------------------------------------------------------------------------


def test_tag_name_rejects_uppercase(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "general",
            "tags": ["URGENT!"],
        },
    )

    assert response.status_code == 422


def test_tag_accepts_digits_and_dashes(client):
    response = client.post(
        "/notes",
        json={
            "title": unique_title(),
            "content": "Valid content",
            "category": "general",
            "tags": ["q2-plan", "api-101"],
        },
    )

    assert response.status_code == 201
    assert set(response.json()["tags"]) == {"q2-plan", "api-101"}
