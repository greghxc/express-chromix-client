import requests
from requests.auth import HTTPBasicAuth

user = 'admin'
password = 'supersecret'
post_url = 'http://localhost:3000/tabs'

response = requests.post(post_url, params = {'url':'http://google.com'}, auth=HTTPBasicAuth(user, password))
print(response.text)