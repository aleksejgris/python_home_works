import requests


def test_delete_user():

   url = "https://ru.yougile.com/api-v2/projects/id"

   payload = {
    "deleted": True,
    "title": "ГосУслуги",
    "users": {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
     }
   }
   headers = {
    "Content-Type": "application/json",
    "Authorization": "123"
   }

   response = requests.request("PUT", url, json=payload, headers=headers)

   print(response.text)

def test_change_user():
    url = "https://ru.yougile.com/api-v2/projects/id"

    payload = {
        "deleted": False,
        "title": "ГосУслуги",
        "users": {
            "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
            "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "123"
    }

    response = requests.request("PUT", url, json=payload, headers=headers)

    print(response.text)