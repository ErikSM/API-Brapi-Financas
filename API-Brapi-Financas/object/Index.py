from access.api_request import make_request
from api_data.all_stocks import indexes


class Index:

    def __init__(self, ticker):

        self.__advanced_data = None

        try:
            self.__index = indexes[ticker]
            self.__index['type'] = 'index'

        except KeyError:
            self.__index = {'stock': f"{ticker}", "name": "(Stock) not found"}

            print(f'Error: >>{self.__index}')
            print("local: Object/Index")

    def __str__(self):
        return self.__index['name']

    def __repr__(self):
        return f"Index({self.__index['stock']})"

    def __getitem__(self, item):
        return self.__index[item]

    def _build_advanced(self):
        if self.__advanced_data is None:
            parameter = {'complement': self.__index['stock']}
            requested = make_request('Specific stock', **parameter)

            self.__advanced_data = requested['results'][0]
            self.__advanced_data['_this_request'] = {"requestedAt": requested['requestedAt'], "took": requested['took']}
        else:
            pass

    def basic_info(self):
        for i in self.__index:
            yield f'{i}: {self.__index[i]}\n'

    def qualified_data(self):
        self._build_advanced()

        for i in self.__advanced_data:
            yield f'{i}: {self.__advanced_data[i]}\n'
