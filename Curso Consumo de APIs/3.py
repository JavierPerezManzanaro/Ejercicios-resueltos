import requests
import pprint

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {'nombre': 'Izan', 'curso': 'python'}
    response = requests.get(url, params=args)
    print(response.url)
    print(type)
    if response.status_code == 200:
        # content = response.content
        # pprint.pprint(content, depth=1)
        response_json = response.json() # es un diccionario
        origin = response_json['origin']
        print(origin)
        
        url = 'http://httpbin.org/get'
        args = {'nombre': 'Izan', 'curso': 'python'}
        response = requests.get(url, params=args)
        print(response.url)
