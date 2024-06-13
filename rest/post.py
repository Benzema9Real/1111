import requests
url = 'http://http://127.0.0.1:8000/api/v1/taskpost/'
data = {
{
    "title": "",
    "description": "",

}
response = requests.post(url, data=data)
if response.status_code == 201:
    print("Запрос успешно отправлен.")
else:
    print("Ошибка при отправке запроса:", response.status_code)