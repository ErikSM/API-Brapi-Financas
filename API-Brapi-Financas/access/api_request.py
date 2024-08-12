import json

import requests

my_key = 'spxS5DhJhKUmar2nz3TJWj'
test_endpoint = '/quote/list'

all_endpoints = dict()
all_endpoints['All stocks'] = '/quote/list'
all_endpoints['All tickers'] = '/api/available'

params = {
    'token': 'eJGEyu8vVHctULdVdHYzQd',
}


def make_request(endpoint):
    base_url = 'https://brapi.dev/api'
    key_use = f'?token={my_key}'

    print(f'{base_url}{endpoint}{key_use}')

    required = requests.get(f'{base_url}{endpoint}', params=params)

    result = json.loads(required.text)

    return result


testando = make_request(test_endpoint)

print("-" * 70)
for i in testando:
    print(i, len(testando[i]), type(testando[i]))
    for j in testando[i]:
        print(j)
    print("-" * 70)
