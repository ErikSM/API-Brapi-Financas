try:
    from api_data.all_stocks import indexes, stocks
except Exception as ex_1:
    print(ex_1)


def stocks_names_to_tickers_dict():
    name_to_ticker = dict()

    try:
        for i in indexes:
            name_to_ticker[indexes[i]['name']] = i, 'index'
        for i in stocks:
            name_to_ticker[stocks[i]['name']] = i, 'stock'
    except Exception as ex:
        print(ex)
    else:
        return name_to_ticker

