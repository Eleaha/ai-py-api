from fastapi.testclient import TestClient
import json

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")

    endpoint_data = open("endpoints.json")
    endpoints = json.load(endpoint_data)
    endpoint_data.close()
    assert response.status_code == 200
    assert response.json() == endpoints

def test_read_generated_letter():
    response = client.get("/letter?to_name=Justin&from_name=Ellie&subject=the+bins+were+not+collected&emotion=dissapointed&location=my+street&timescale=since+last+week")
    assert response.status_code == 200
    assert "letter" in response.json()

def test_read_generated_letter_missing_queries():
    response = client.get("/letter")
    assert response.status_code == 400
    assert response.json() == {"detail": "Please provide the mandatory queries for from_name, subject and emotion"}