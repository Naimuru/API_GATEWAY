import requests
import os
def generalRequest(url, method, body=None, full_response=False):
    headers = {'Content-Type': 'application/json'}
    if os.getenv('SHOW_URLS'):
        print(url)

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=body, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, json=body, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f'Invalid method: {method}')
        return response.json()
    except requests.exceptions.RequestException as err:
        return str(err)