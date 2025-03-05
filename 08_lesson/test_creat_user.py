import requests


def test_creat_user_worker():

   url = "https://ru.yougile.com/api-v2/projects"

   payload = {
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
   response = requests.request("POST", url, json=payload, headers=headers)

   print(response.text)

def test_creat_user_None():
   url = "https://ru.yougile.com/api-v2/projects"

   payload = {
      "title": "ГосУслуги",
      "users": {
          "None",
         
      }
   }
   headers = {
      "Content-Type": "application/json",
      "Authorization": "123"
   }
   response = requests.request("POST", url, json=payload, headers=headers)

   print(response.text)