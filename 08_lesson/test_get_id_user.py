import requests


def test_get_id_user():

   url = "https://ru.yougile.com/api-v2/projects/id"

   headers = {
    "Content-Type": "application/json",
    "Authorization": "123"
   }

   response = requests.request("GET", url, headers=headers)

   print(response.text)

def test_wrong_auth():
    url = "https://ru.yougile.com/api-v2/projects/id"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "321"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)