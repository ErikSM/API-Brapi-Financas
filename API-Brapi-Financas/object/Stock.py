from api_data.all_stocks import stocks
from webview import create_window


class Stock:

    def __init__(self, ticker):

        try:
            self.__stock = stocks[ticker]
        except KeyError:
            self.__stock = {'stock': f"{tiker}", "name": "KeyError"}

    def __str__(self):
        return self.__stock['name']

    def __repr__(self):
        return f"Stock({self.__stock['stock']})"

    def __getitem__(self, item):
        return self.__stock[item]

    def __len__(self):
        return len(self.__stock)

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

