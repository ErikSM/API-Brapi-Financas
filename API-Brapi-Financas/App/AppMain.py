from tkinter import *

from api_data.all_stocks import all_stocks_tuple
from api_data.all_tickers import all_tickers_tuple


class AppMain:

    def __init__(self):
        self.__root = Tk()

        self.search = StringVar()

        self.img_magnifier = PhotoImage(file=r'..\assets\magnifier.png')

        self.__root.title('API - Brapi')
        self.__root.geometry('+400+300')
        self.__root.resizable(False, False)

        self.__head = Frame(self.__root)

        f_header = Frame(self.__head)

        Label(f_header, text='Search', font=('Consolas', 14, 'bold')).grid(row=0, column=0)

        self.search.set('')
        entry_search = Entry(f_header, font=('Consolas', 14, 'bold'), textvariable=self.search)
        entry_search.grid(row=0, column=1)

        but_search = Button(f_header, image=self.img_magnifier)
        but_search.config(command=self.do_search)
        but_search.grid(row=0, column=2)

        f_header.pack()

        self.__head.pack()

        self.__body = Frame(self.__root)

        f_text = Frame(self.__body)

        self.text = Text(f_text, font=('Consolas', 12,), bg='black', fg='white')
        self.text.grid(row=1, column=1)

        f_text.pack()

        self.__body.pack()

        self.__foot = Frame(self.__root)
        self.__foot.pack()

        self.__root.mainloop()

    def do_search(self):

        cap_type = ''
        captured = self.search.get()

        if captured in all_tickers_tuple[0]:
            cap_type = '  ticker  ', '  (index)  '
        elif captured in all_tickers_tuple[1]:
            cap_type = '  ticker  ', '(stock)'
        else:
            for i in all_tickers_tuple[0]:
                if all_tickers_tuple[0][i]['name'] == captured:
                    cap_type = '  indexes  ', '  (name)  '
            for i in all_tickers_tuple[1]:
                if all_tickers_tuple[1][i]['name'] == captured:
                    cap_type = '  indexes  ', '  (name)  '

        self.text.insert(END, '{},{}: {}'.format(cap_type[0], cap_type[1], captured))


AppMain()
