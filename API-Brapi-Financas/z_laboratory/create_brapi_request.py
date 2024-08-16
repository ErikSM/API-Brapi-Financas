import json

import requests

my_key = 'spxS5DhJhKUmar2nz3TJWj'


test_endpoint_um = '/quote/list'
test_endpoint_dois = '/available'


def create_request(endpoint, **parameters):

    base_url = 'https://brapi.dev/api'

    params = {'token': my_key}
    for i in parameters:
        params[i] = parameters[i]

    print('endpoint >> ', endpoint)
    print('params >> ', params)

    try:
        required = requests.get(f'{base_url}{endpoint}', params=params)
        result = json.loads(required.text)
    except Exception as ex:
        print(ex)

    return result


def do_create_test():
    testando = create_request(test_endpoint_um)

    print("-" * 70)
    for i in testando:
        try:
            print(i, len(testando[i]), type(testando[i]))
        except Exception as ex:
            print('{}-{}--{}'.format(i, testando[i], ex))
        else:
            print(f'>>{i}')
            for j in testando[i]:
                print(j)
            print("-" * 70)

#do_create_test()
