import uuid

import requests

TOKEN = "ВСТАВЬТЕ_ВАШ_ТОКЕН"
BASE_URL = "https://yougile.com"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}

def test_create_project():
    title = f"ГосУслуги-{uuid.uuid4().hex[:8]}"
    body = {"title": title}

    resp = requests.post(f"{BASE_URL}/api-v2/projects",
                         json=body, headers=HEADERS)
    assert resp.status_code == 201, f"{resp.status_code}: {resp.text}"

    project_id = resp.json()["id"]

    resp = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}",
                        headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json()["title"] == title


def test_create_project_neg():
    body = {"title": ""}
    resp = requests.post(f"{BASE_URL}/api-v2/projects",
                         json=body, headers=HEADERS)
    assert resp.status_code == 400, f"{resp.status_code}: {resp.text}"

def test_get_project_by_id():
    title = f"Проект для проверки GET-{uuid.uuid4().hex[:8]}"
    resp = requests.post(f"{BASE_URL}/api-v2/projects",
                         json={"title": title}, headers=HEADERS)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    resp = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}",
                        headers=HEADERS)
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body["id"] == project_id
    assert resp_body["title"] == title
    assert "timestamp" in resp_body, "В ответе нет обязательного поля timestamp"
    assert isinstance(resp_body["timestamp"], (int, float)), \
        f"timestamp должен быть числом, получено: {type(resp_body['timestamp'])}"


def test_get_project_by_id_neg():
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = requests.get(f"{BASE_URL}/api-v2/projects/{fake_id}",
                        headers=HEADERS)
    assert resp.status_code in (400, 404), f"{resp.status_code}: {resp.text}"

    if resp.headers.get("Content-Type", "").startswith("application/json"):
        resp_body = resp.json()
        assert "error" in resp_body or "message" in resp_body

def test_update_project():
    old_title = f"Старое название-{uuid.uuid4().hex[:8]}"
    resp = requests.post(f"{BASE_URL}/api-v2/projects",
                         json={"title": old_title}, headers=HEADERS)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    new_title = f"Новое название-{uuid.uuid4().hex[:8]}"
    resp = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}",
                        json={"title": new_title}, headers=HEADERS)
    assert resp.status_code == 200, f"{resp.status_code}: {resp.text}"

    resp = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}",
                        headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json()["title"] == new_title


def test_update_project_neg():
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = requests.put(f"{BASE_URL}/api-v2/projects/{fake_id}",
                        json={"title": "Новое название"}, headers=HEADERS)
    assert resp.status_code in (400, 404), f"{resp.status_code}: {resp.text}"

    if resp.headers.get("Content-Type", "").startswith("application/json"):
        resp_body = resp.json()
        assert "error" in resp_body or "message" in resp_body









