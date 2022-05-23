

import requests
import json

params = {'q': 'name'}

url = 'https://api.github.com'

user = 'olegtereschenko'

responce = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(responce.json(), f)

for i in responce.json():
    print(i['full_name'])

