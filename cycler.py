import requests
import time
from requests.auth import HTTPBasicAuth

user = 'admin'
password = 'supersecret'
post_url = 'http://localhost:3000/tabs'

time.sleep(3)
print('Posting')
response = requests.post(post_url, params = {'url':'http://google.com'}, auth=HTTPBasicAuth(user, password))
print(response.text)
created_tab_id = response.json()['id']

time.sleep(3)
print('Putting')
requests.put(f'{post_url}/{created_tab_id}', params = {'url':'http://bing.com', 'id':created_tab_id}, auth=HTTPBasicAuth(user, password))
print(response.text)

time.sleep(3)
print('Deleting')
requests.delete(f'{post_url}/{created_tab_id}', params = {'id':created_tab_id}, auth=HTTPBasicAuth(user, password))
print(response.text)
