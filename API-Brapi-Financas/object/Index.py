from access.api_request import make_request
from api_data.all_stocks import indexes


class Index:

    def __init__(self, ticker):

        try:
            self.__index = indexes[ticker]
            self.__index['type'] = 'index'

        except KeyError:
            self.__index = {'stock': f"{ticker}", "name": "KeyError"}

        print(self.__index['name'])

    def __str__(self):
        return self.__index['name']

    def __repr__(self):
        return f"Index({self.__index['stock']})"

    def __getitem__(self, item):
        return self.__index[item]

    def information(self):

        for i in self.__index:
            yield f'{i}: {self.__index[i]}\n'

    def qualified_data(self):

        parameter = {'complement': self.__index['stock']}
        requested = make_request('Specific stock', **parameter)

        data = requested['results'][0]
        for i in data:
            yield f'{i}: {data[i]}\n'
