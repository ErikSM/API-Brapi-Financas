from access.api_request import make_request
from api_data.data_actions import stocks_names_to_tickers_dict
from object.Stock import Stock


def processing_search(searched):

    param = {'search': searched.upper()}

    possible_tickers = list()

    stock_names = stocks_names_to_tickers_dict()
    if searched in stock_names.keys():

        stock_found = Stock(stock_names[searched][0]), True

    else:
        stock_found = 'stock not found', False

        requested = make_request('All stocks', **param)

        for i in requested:
            if i == "stocks":
                for j in requested[i]:
                    possible_tickers.append(j['stock'])

        if len(possible_tickers) == 0:
            possible_tickers.append('tickers not found')

    return possible_tickers, stock_found
