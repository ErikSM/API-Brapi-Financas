from api_data.all_stocks import all_stocks_tuple
import webview


class Stock:
    stock = all_stocks_tuple[1]

    def __init__(self, ticker):

        try:
            self.__stock = Stock.stock[ticker]
        except KeyError:
            self.__stock = {'stock': "KeyError", "name": "not found"}

    def __str__(self):
        return self.__stock['name']

    def __repr__(self):
        return self.__stock['stock']

    def __getitem__(self, item):
        return self.__stock[item]

    def __len__(self):
        return len(self.__stock)

    def show_logo(self):

        try:
            webview.create_window(self.__stock['name'], self.__stock['logo'], width=350, height=200)
        except KeyError:
            pass
        else:
            return webview

    def basic_info(self):

        for i in self.__stock:
            yield f'{i}: {self.__stock[i]}'


stock = Stock('AMER3')
