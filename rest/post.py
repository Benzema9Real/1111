import requests
url = 'http://188.225.26.121:84/api/v1/taskpost/'
data = {
    "title": "ff",
    "description": "fffffffffff",
    "completed": "false"
}
response = requests.post(url, data=data)
if response.status_code == 201:
    print("Запрос успешно отправлен.")
else:
    print("Ошибка при отправке запроса:",response.status_code)