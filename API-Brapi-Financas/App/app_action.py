from access.api_request import make_request
from api_data.data_actions import stocks_names_to_tickers_dict
from object.Index import Index
from object.Stock import Stock


def processing_search(searched):
    searched = searched.upper()
    param = {'search': searched}

    stock_found = None
    possible_tickers = list()

    all_names = stocks_names_to_tickers_dict()
    all_tickers = {all_names[i][0]: (i, all_names[i][1]) for i in all_names}

    if searched in all_names.keys():
        if all_names[searched][1] == 'stock':
            stock_found = Stock(all_names[searched][0]), True
        elif all_names[searched][1] == 'index':
            stock_found = Index(all_names[searched][0]), True

    elif searched in all_tickers.keys():
        if all_tickers[searched][1] == 'stock':
            stock_found = Stock(searched), True
        elif all_tickers[searched][1] == 'index':
            stock_found = Index(searched), True

    else:
        stock_found = 'stock not found', False, 'undefined'

        requested = make_request('All stocks', **param)
        print(requested)

        for i in requested:
            if i == "stocks":
                for j in requested[i]:
                    possible_tickers.append(j['stock'])

        if len(possible_tickers) == 0:
            possible_tickers.append('tickers not found')

    return possible_tickers, stock_found


def processing_menu_opt(opt_str):
    processed_list = list()
    names = stocks_names_to_tickers_dict()

    for i in names:
        stock_or_index = names[i][1]

        if opt_str == 'Indexes tickers':
            if stock_or_index == 'index':
                processed_list.append(names[i][0])

        elif opt_str == 'Indexes names':
            if stock_or_index == 'index':
                processed_list.append(i)

        elif opt_str == 'Stocks names':
            if stock_or_index == 'stock':
                processed_list.append(i)

        elif opt_str == 'Stocks tickers':
            if stock_or_index == 'stock':
                processed_list.append(names[i][0])

    return processed_list


def processing_play(menu_selected, captured):
    processed = None

    if menu_selected == 'Stocks tickers':
        processed = Stock(captured)

    elif menu_selected == 'Indexes tickers':
        processed = Index(captured)

    elif menu_selected == 'Stocks names':
        stock_ticker = stocks_names_to_tickers_dict(captured)
        processed = Stock(stock_ticker)

    elif menu_selected == 'Indexes names':
        index_ticker = stocks_names_to_tickers_dict(captured)
        processed = Index(index_ticker)

    elif menu_selected == 'Search':
        try:
            processed = Stock(captured)
        except Exception as ex:
            print(f'1 - {ex}')
            try:
                processed = Index(captured)
            except Exception as ex_2:
                print(f'2 - {ex_2}')


    return processed
