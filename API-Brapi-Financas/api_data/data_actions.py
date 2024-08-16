try:
    from api_data.all_stocks import all_stocks_tuple
except Exception as ex_1:
    print(ex_1)


def names_to_tickers_dict():

    names_to_tickers = dict()

    try:
        indexes = all_stocks_tuple[0]
        stocks = all_stocks_tuple[1]
    except Exception as ex_2:
        print(ex_2)

    else:
        for i in indexes:
            names_to_tickers[indexes[i]['name']] = i
        for i in stocks:
            names_to_tickers[stocks[i]['name']] = i

    return names_to_tickers


teste = names_to_tickers_dict()
print(teste)
