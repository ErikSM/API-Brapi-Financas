try:
    from api_data.all_stocks import indexes, stocks
except Exception as ex_1:
    print(f'Error: >>{ex_1}')
    print("local: data_actions/stocks_names_to_tickers_dict")


def stocks_names_to_tickers_dict(specific=None):
    name_to_ticker = dict()

    try:
        for i in indexes:
            name_to_ticker[indexes[i]['name']] = i, 'index'
        for i in stocks:
            name_to_ticker[stocks[i]['name']] = i, 'stock'

    except Exception as ex_2:
        print(f'Error: >> {ex_2}')
        print("local: data_actions/stocks_names_to_tickers_dict")

    else:
        if specific is not None:
            try:
                specified = name_to_ticker[specific]
            except KeyError:
                print(f'Error: >> KeyError')
                print("local: data_actions/stocks_names_to_tickers_dict")
            else:
                return specified[0]

        else:
            return name_to_ticker


def stocks_for_types(stock_type):

    type_list = list()

    for i in stocks:
        if stocks[i]['type'] == stock_type:
            type_list.append(stocks[i]['name'])

    return type_list
