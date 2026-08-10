from app.main import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_user_search():
    client = app.test_client()

    response = client.get("/users?name=Ada")

    assert response.status_code == 200
    assert response.json["users"] == [{"id": 1, "name": "Ada"}]
