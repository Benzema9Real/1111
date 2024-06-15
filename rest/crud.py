import requests
url = 'http://188.225.26.121:84/api/v1/taskput/14'
data = {
    "title": "ff",
    "description": "ffffffffddfff",
    "completed": "false"
}
response = requests.put(url, data=data)
if response.status_code == 200:
    print("Запрос успешно отправлен.")
else:
    print("Ошибка при отправке запроса:",response.status_code)

url = 'http://188.225.26.121:84/api/v1/taskdelete/14'

response = requests.delete(url)
if response.status_code == 200:
    print("Запрос успешно отправлен.")
else:
    print("Ошибка при отправке запроса:",response.status_code)