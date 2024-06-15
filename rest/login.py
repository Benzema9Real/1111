import requests


login_url = 'http://188.225.26.121:84/api/token/'
login_data = {'username': 'a', 'password': 'a'}

login_response = requests.post(login_url, json=login_data)
token = login_response.json().get('access')

print(token)

