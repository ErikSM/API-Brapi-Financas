import json
import requests


my_key = 'spxS5DhJhKUmar2nz3TJWj'
test_endpoint = '/quote/list'


all_endpoints = dict()
all_endpoints['All stocks'] = {'endpoint': "/quote/list",
                               'complement': False,
                               'params':
                                   ('search',
                                    'sortBy', 'sortOrder',
                                    'limit', 'page',
                                    'type', 'sector')
                               }

all_endpoints['All tickers'] = {'endpoint': '/available',
                                'complement': False,
                                'params':
                                    ('search', '')
                                }

all_endpoints['Specific stock'] = {'endpoint': '/quote/',
                                   'complement': True,
                                   'params':
                                       ('range', 'interval',
                                        'fundamental', 'dividends',
                                        'modules', )
                                   }


def make_request(endpoint: all_endpoints, **parameters):

    base_url = 'https://brapi.dev/api'

    point_data = all_endpoints[endpoint]
    params = {'token': my_key}

    endpoint_used = ''
    complement_used = ''

    for i in point_data:
        if i == 'endpoint':
            endpoint_used = point_data[i]
        elif i == 'complement':
            if point_data[i]:
                complement_used = parameters[i]

    for i in parameters:
        if i == 'complement':
            pass
        else:
            params[i] = parameters[i]

    print(params)
    print(f'{base_url}{endpoint_used}{complement_used}')

    required = requests.get(f'{base_url}{endpoint_used}{complement_used}', params=params)
    result = json.loads(required.text)

    return result


def testar_request():
    testando = make_request('Specific stock', complement='^AORD')

    print("-" * 70)
    for i in testando:
        try:
            print(i, len(testando[i]), type(testando[i]))
        except Exception as ex:
            print('{}-{}--{}'.format(i, testando[i], ex))
        else:
            print(f'>> {i}:  --')
            if type(testando[i]) is list:
                if i == 'results':
                    for j in testando[i]:
                        for z in j:
                            print('-{}: {}'.format(z, j[z]))
                    print("-" * 70)
                else:
                    for j in testando[i]:
                        print('items:  ', j)
                    print("-" * 70)
            elif type(testando[i]) is dict:
                for j in testando[i]:
                    print('keys:  ', j)
                print("-" * 70)
            else:
                print(testando[i])
                print("-" * 70)


#  testar_request()
