import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_survey():
    response = client.post("/surveys", json={"title": "Encuesta Test", "description": "desc"})
    assert response.status_code == 201
    return response.json()

def test_create_survey():
    response = client.post("/surveys", json={"title": "Encuesta Test", "description": "desc"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Encuesta Test"

def test_add_question_to_survey(create_survey):
    survey = create_survey
    response = client.post(f"/surveys/{survey['id']}/questions", json={"text": "Pregunta 1", "question_type": "single_choice"})
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "Pregunta 1"
    assert data["question_type"] == "single_choice"

def test_add_option_to_choice_question(create_survey):
    survey = create_survey
    q_resp = client.post(f"/surveys/{survey['id']}/questions", json={"text": "Pregunta 2", "question_type": "single_choice"})
    question = q_resp.json()
    o_resp = client.post(f"/questions/{question['id']}/options", json={"text": "Opción A"})
    assert o_resp.status_code == 201
    o_data = o_resp.json()
    assert o_data["text"] == "Opción A"
    assert o_data["question_id"] == question["id"]

def test_add_option_to_text_question(create_survey):
    survey = create_survey
    q_resp = client.post(f"/surveys/{survey['id']}/questions", json={"text": "Pregunta texto", "question_type": "text"})
    question = q_resp.json()
    o_resp = client.post(f"/questions/{question['id']}/options", json={"text": "No debería"})
    assert o_resp.status_code == 400
    assert "solo se pueden agregar opciones".lower() in o_resp.text.lower()
