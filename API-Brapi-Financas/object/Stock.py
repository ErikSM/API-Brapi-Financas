from api_data.all_stocks import stocks
from webview import create_window

from access.api_request import make_request


class Stock:

    def __init__(self, ticker):

        self.__advanced_data = None

        try:
            self.__stock = stocks[ticker]

        except KeyError:
            self.__stock = {'stock': f"{ticker}", "name": "(Stock) not found"}

            print(f'Error: >>{self.__stock}')
            print("local: Object/Stock")

    def __str__(self):
        return self.__stock['name']

    def __repr__(self):
        return f"Stock({self.__stock['stock']})"

    def __getitem__(self, item):
        return self.__stock[item]

    def _build_advanced(self):
        if self.__advanced_data is None:
            parameter = {'complement': self.__stock['stock']}
            requested = make_request('Specific stock', **parameter)

            try:
                self.__advanced_data = requested['results'][0]
                self.__advanced_data['_this_request'] = {"requestedAt": requested['requestedAt'], "took": requested['took']}
            except KeyError:
                self.__advanced_data = {'Error': 'not found data'}
                print('Error: >> KeyError, Local: Stock._buildAdv" ')
        else:
            pass

    def basic_info(self):
        for i in self.__stock:
            if i != 'logo':
                yield f'{i}: {self.__stock[i]}\n'

    def qualified_data(self):
        self._build_advanced()

        for i in self.__advanced_data:
            yield f'{i}: {self.__advanced_data[i]}\n'

    def show_logo(self):
        try:
            create_window(self.__stock['name'], self.__stock['logo'], width=350, height=200)
        except KeyError:
            create_window(self.__stock['name'], "https://brapi.dev/", width=350, height=200)
        else:
            return webview
