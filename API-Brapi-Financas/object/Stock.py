from api_data.all_stocks import stocks
from webview import create_window

from access.api_request import make_request


class Stock:

    def __init__(self, ticker):

        try:
            self.__stock = stocks[ticker]
        except KeyError:
            self.__stock = {'stock': f"{ticker}", "name": "KeyError"}

    def __str__(self):
        return self.__stock['name']

    def __repr__(self):
        return f"Stock({self.__stock['stock']})"

    def __getitem__(self, item):
        return self.__stock[item]

    def show_logo(self):
        try:
            create_window(self.__stock['name'], self.__stock['logo'], width=350, height=200)
        except KeyError:
            create_window(self.__stock['name'], "https://brapi.dev/", width=350, height=200)
        else:
            return webview

    def basic_info(self):

        advanced = 'logo', 'change', 'volume', 'close'

        for i in self.__stock:
            if i not in advanced:
                yield f'{i}: {self.__stock[i]}\n'

    def qualified_data(self):

        parameter = {'complement': self.__stock['stock']}
        requested = make_request('Specific stock', **parameter)

        data = requested['results'][0]
        for i in data:
            yield f'{i}: {data[i]}\n'
