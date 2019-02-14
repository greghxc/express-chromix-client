import requests
import time
from requests.auth import HTTPBasicAuth

api_url = 'http://localhost:3000/tabs'

def get(id):
    response = requests.get(f'{api_url}/{id}', auth=HTTPBasicAuth(user, password))
    return  response.json()

def get_all():
    response = requests.get(api_url, auth=HTTPBasicAuth(user, password))
    return  response.json()

def create(url):
    response = requests.post(api_url, params = {'url':url}, auth=HTTPBasicAuth(user, password))
    return response.json()['id']

def update(url, id):
    requests.put(f'{api_url}/{id}', params = {'url':url}, auth=HTTPBasicAuth(user, password))

def delete(id):
    requests.delete(f'{api_url}/{id}', auth=HTTPBasicAuth(user, password))

def print_ids(tabs):
    print([tab['id'] for tab in tabs])

user = 'admin'
password = 'supersecret'
cycle_seconds = 5

default_url = 'http://localhost:3000/api-docs'

urls = [line.rstrip('\n') for line in open('urls.txt')]

urls_index = 0

init_tabs = get_all()
created_id = create(default_url)

for tab in init_tabs:
    delete(tab['id'])

try:
    while True:
        urls_index = urls_index % len(urls)
        update(urls[urls_index], created_id)
        urls_index += 1
        time.sleep(cycle_seconds)
except (KeyboardInterrupt, SystemExit):
    print('Exiting...')

update(default_url, created_id)
