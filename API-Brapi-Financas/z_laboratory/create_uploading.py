from tkinter import Text, END
from create_brapi_request import *


# all_stocks_tuple = (availableStockTypes, availableSectors, stocks, indexes)
def criar_upload():
    endereco_um = r'..\api_data\all_stocks'
    endereco_dois = r'..\api_data\all_tickers'

    formato = 'py'

    file_um = open(f"{endereco_um}.{formato}", "w+", encoding='cp932', errors='ignore')
    file_dois = open(f"{endereco_dois}.{formato}", "w+", encoding='cp932', errors='ignore')

    texto_um = _escrever_file_um()
    texto_dois = _escrever_file_dois()

    file_um.write(texto_um.get(1.0, END))
    file_dois.write(texto_dois.get(1.0, END))

    file_um.close()
    file_dois.close()


def _escrever_file_um():
    texto_um = Text()

    conteudo_um = create_request(test_endpoint_um)

    for i in conteudo_um:
        texto_um.insert(END, f'\n{i} = [ \n')

        for j in conteudo_um[i]:

            if i == 'stocks':
                texto_um.insert(END, '    { \n')

                for z in j:

                    if type(j[z]) == str:
                        texto_um.insert(END, f'        "{z}": "{j[z]}",\n')
                    else:
                        texto_um.insert(END, f'        "{z}": {j[z]},\n')

                texto_um.insert(END, '    }, \n')

            else:
                if type(j) == str:
                    texto_um.insert(END, f'    "{j}", \n')
                else:
                    texto_um.insert(END, f'    {j}, \n')

        texto_um.insert(END, f'] \n\n')

    texto_um.insert(END, 'all_stocks_tuple = (indexes, stocks, availableSectors, availableStockTypes)')

    return texto_um


def _escrever_file_dois():
    texto_dois = Text()

    conteudo_dois = create_request(test_endpoint_dois)

    for i in conteudo_dois:
        texto_dois.insert(END, f'\n{i} = [ \n    ')

        cont = 0
        for j in conteudo_dois[i]:
            if cont < 10:
                texto_dois.insert(END, f'"{j}", ')
                cont += 1
            elif cont == 10:
                texto_dois.insert(END, f'"{j}", \n    ')
                cont = 0

        texto_dois.insert(END, f'\n] \n\n')

    texto_dois.insert(END, 'all_tickers_tuple = (indexes, stocks)')

    return texto_dois


# criar_upload()
