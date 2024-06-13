import requests
url = 'http://your-server-url/api/car-brands/'
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