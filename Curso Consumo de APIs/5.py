import requests
import json
import pprint


if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Izan', 'curso': 'python'}
    response = requests.post(url, json=payload)
    print(response.url)

    if response.status_code == 200:
        content = response.content
