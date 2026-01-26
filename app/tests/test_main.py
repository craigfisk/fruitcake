from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert "id" in response.json()

def test_login_for_access_token():
    # First, create a user
    client.post("/users/", json={"email": "test@example.com", "password": "password"})
    
    response = client.post("/token", data={"username": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_logout():
    # First, create a user and login
    client.post("/users/", json={"email": "test@example.com", "password": "password"})
    login_response = client.post("/token", data={"username": "test@example.com", "password": "password"})
    token = login_response.json()["access_token"]
    
    response = client.post("/logout", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully logged out"}

def test_read_users_me():
    # First, create a user and login
    client.post("/users/", json={"email": "test@example.com", "password": "password"})
    login_response = client.post("/token", data={"username": "test@example.com", "password": "password"})
    token = login_response.json()["access_token"]
    
    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert "subscription_status" in response.json()
