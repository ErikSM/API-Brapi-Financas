from tkinter import Text, END
from access.api_request import make_request


def uploading_and_update_data():

    type_format = 'py'
    endpoint_stocks = r'..\api_data\all_stocks'
    endpoint_ticker = r'..\api_data\all_tickers'

    file_stocks = open(f"{endpoint_stocks}.{type_format}", "w+", encoding='cp932', errors='ignore')

    stocks_written = _write_stock_file()
    file_stocks.write(stocks_written.get(1.0, END))

    file_stocks.close()

    file_tickers = open(f"{endpoint_ticker}.{type_format}", "w+", encoding='cp932', errors='ignore')

    tickers_written = _write_ticker_file()
    file_tickers.write(tickers_written.get(1.0, END))

    file_tickers.close()


def _write_stock_file():

    text_field = Text()
    data_requested = make_request('All stocks')

    for i in data_requested:

        if i == 'indexes' or i == 'stocks':
            text_field.insert(END, f'\n{i} =')
            text_field.insert(END, ' { \n')
        else:
            text_field.insert(END, f'\n{i} = ( \n')

        for j in data_requested[i]:

            if i == 'stocks':
                text_field.insert(END, f'    "{j['name']}":')
                text_field.insert(END, ' { \n')

                for z in j:
                    if type(j[z]) is str:

                        text_field.insert(END, f'        "{z}": "{j[z]}",\n')
                    else:
                        text_field.insert(END, f'        "{z}": {j[z]},\n')
                text_field.insert(END, '    }, \n\n')

            elif i == 'indexes':
                text_field.insert(END, f'    "{j['name']}": ')

                if type(j) is str:
                    text_field.insert(END, f'"{j}", \n')
                else:
                    text_field.insert(END, f'{j}, \n')

            else:
                if type(j) is str:
                    text_field.insert(END, f'    "{j}", \n')
                else:
                    text_field.insert(END, f'    {j}, \n')

        if i == 'indexes' or i == 'stocks':
            text_field.insert(END, '} \n\n')
        else:
            text_field.insert(END, ') \n\n')

    text_field.insert(END, 'all_stocks_tuple = (indexes, stocks, availableSectors, availableStockTypes)')

    return text_field


def _write_ticker_file():

    text_field = Text()
    data_requested = make_request('All tickers')

    for i in data_requested:
        text_field.insert(END, f'\n{i} = ( \n    ')

        cont = 0
        for j in data_requested[i]:
            if cont < 10:
                text_field.insert(END, f'"{j}", ')
                cont += 1
            elif cont == 10:
                text_field.insert(END, f'"{j}", \n    ')
                cont = 0

        text_field.insert(END, f'\n) \n\n')

    text_field.insert(END, 'all_tickers_tuple = (indexes, stocks)')

    return text_field


uploading_and_update_data()
