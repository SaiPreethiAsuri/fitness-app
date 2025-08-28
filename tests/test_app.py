import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Home page should load with status 200"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEestFitness and Gym" in response.data

def test_add_workout_success(client):
    """Adding a valid workout should redirect to home"""
    response = client.post("/add", data={"workout": "Pushups", "duration": "30"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Pushups" in response.data

def test_add_workout_invalid_duration(client):
    """Adding a workout with non-numeric duration should show error"""
    response = client.post("/add", data={"workout": "Running", "duration": "abc"})
    assert b"Duration must be a number" in response.data

def test_add_workout_missing_fields(client):
    """Missing fields should show error"""
    response = client.post("/add", data={"workout": "", "duration": ""})
    assert b"Please enter both workout and duration" in response.data

def test_home_page_contains_form(client):
    response = client.get("/")
    assert b"<form" in response.data
    assert b"name=\"workout\"" in response.data
    assert b"name=\"duration\"" in response.data

def test_invalid_workout_with_numbers(client):
    response = client.post("/add", data={"workout": "12345", "duration": "30"})
    assert b"Workout must contain only letters" in response.data

def test_negative_duration(client):
    response = client.post("/add", data={"workout": "Running", "duration": "-10"})
    assert b"Duration must be greater than 0" in response.data