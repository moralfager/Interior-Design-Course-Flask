import requests
import json
import base64
import os

def getCourseAddPerson(name, surname, email):
    accountName = os.environ.get('accountName')
    secretKey = os.environ.get('secretKey')

    user = {}
    user['user'] = {}
    user['user']['email'] = email
    user['user']['first_name'] = name
    user['user']['last_name'] = surname
    user['system'] = {}
    user['system']['refresh_if_exists'] = 1

    json_data = json.dumps(user)
    base64_data = base64.b64encode(json_data.encode('utf-8'))

    url = f'https://{accountName}.getcourse.ru/pl/api/users'
    payload = {
        'action': 'add',
        'key': secretKey,
        'params': base64_data.decode('utf-8')
    }

    response = requests.post(url, data=payload).json()
    print('getCourseAddPerson')
    return response["success"]

print(getCourseAddPerson('name','surname','enal@mail.ru'))

