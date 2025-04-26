import requests
import pytest

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def create_user_client():
    url = f"{BASE_URL}/users"
    user_data = {
        "name": "Alice",
        "job": "QA Engineer"
    }
    response = requests.post(url, json=user_data)
    if response.status_code == 201:
        user_id = response.json()["id"]
        print(f"✅ משתמש נוצר בהצלחה! ID: {user_id}")
        return user_id
    else:
        print("❌ שגיאה ביצירת משתמש:", response.text)
        return None

def test_update_user(base_url):
    payload = {
        "name": "Ella Updated",
        "job": "Senior QA Engineer"
    }
    response = requests.put(f"{base_url}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Ella Updated"

def test_delete_user(base_url):
    response = requests.delete(f"{base_url}/users/2")
    assert response.status_code == 204

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
