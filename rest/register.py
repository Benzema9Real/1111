import requests
url = 'http://188.225.26.121:84/api/v1/register/'
data = {
    "user": {
        "username": "popopo1",
        "email": "bfggrfdcx@gmail.com",
        "password": "2323@Emir",
        "first_name": "ccc",
        "last_name": "cc"
    },
    "country": "cc",
    "region": "cc"
}
response = requests.post(url, json=data)
if response.status_code == 201:
    print("Запрос успешно отправлен.")
else:
    print("Ошибка при отправке запроса:",response.status_code)