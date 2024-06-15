import requests

url_tasklist = 'http://188.225.26.121:84/api/v1/tasklist/'

get_tasklist = requests.get(url_tasklist)
print(get_tasklist.json())