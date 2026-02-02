import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    # Get an activity name
    activities = client.get("/activities").json()
    if not activities:
        pytest.skip("No activities available to test signup.")
    activity_name = next(iter(activities.keys()))
    email = "testuser@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup?email={email}"
    response = client.post(signup_url)
    assert response.status_code in (200, 400)  # 400 if already signed up
    data = response.json()
    assert "message" in data or "detail" in data
