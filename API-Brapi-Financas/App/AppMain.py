from tkinter import *

from App.app_action import processing_search, processing_play
from App.app_config import colr, font
from api_data.about_api import about_brapi
from api_data.data_actions import stocks_names_to_tickers_dict


class AppMain:

    def __init__(self):

        self.__main_obj = None

        self.__root = Tk()

        self.entry_search_str = StringVar()

        self.entry_text_str = StringVar()
        self.entry_text_str.set('../>')

        self.opt_menu_str = StringVar()
        self.opt_menu_str.set('Options Menu')
        self.opt_menu_list = 'Indexes tickers', 'Stocks tickers', 'Stocks names'

        self.buts = list()

        self.img_logo = PhotoImage(file=r'..\assets\logo.png')
        self.img_magnifier = PhotoImage(file=r'..\assets\magnifier.png')

        self.__root.title('API - Brapi')
        self.__root.geometry('+400+200')
        self.__root.resizable(False, False)
        self.__root.config(bg=colr["BL_L"])

        self.__head = Frame(self.__root)

        f_title = Frame(self.__head)
        Label(f_title, image=self.img_logo).grid(row=0, column=0)
        Label(f_title, text=about_brapi['title'], font=font['title']).grid(row=0, column=1)
        f_title.pack(side=LEFT)

        f_search = Frame(self.__head)
        self.entry_search_str.set('')
        entry_search = Entry(f_search, font=font['search'], textvariable=self.entry_search_str, bd=9)
        entry_search.grid(row=0, column=1)

        button_search = Button(f_search, image=self.img_magnifier)
        button_search.config(command=self.do_search)
        button_search.grid(row=0, column=2)
        f_search.pack(side=LEFT)

        self.__head.pack()

        self.__body = Frame(self.__root)
        f_list = Frame(self.__body)
        self.opt_menu = OptionMenu(f_list, self.opt_menu_str, *self.opt_menu_list,
                                   command=lambda opt_str=self.opt_menu_str: self.active_opt_menu(opt_str))
        self.opt_menu.config(bg=colr['WH'], state=NORMAL, width=28, bd=3, anchor='center')
        self.opt_menu.grid(row=0, column=1)

        self.listbox = Listbox(f_list, font=font['Principal'], bg=colr['BK'], fg=colr['WH'], bd=16)
        self.listbox.grid(row=1, column=1)

        x_list = Scrollbar(f_list, orient=HORIZONTAL, command=self.listbox.xview)
        x_list.grid(row=2, column=1, sticky=W + E)
        self.listbox.config(xscrollcommand=x_list.set)

        y_list = Scrollbar(f_list, orient=VERTICAL, command=self.listbox.yview)
        y_list.grid(row=1, column=0, sticky=N + S)
        self.listbox.config(yscrollcommand=y_list.set)
        f_list.grid(row=1, column=1)

        f_but = Frame(self.__body)
        cont = 0
        while cont < 8:
            self.buts.append(Button(f_but, text='', width=5, height=1))
            cont += 1

        self.buts[1].config(text=' >> ', command=self.do_play)

        for i in self.buts:
            i.pack()
        f_but.grid(row=1, column=2)

        f_text = Frame(self.__body)
        entry_local = Entry(f_text, font=font['search'], textvariable=self.entry_text_str)
        entry_local.config(width=48, bd=4, bg=colr['WH'], fg=colr['BK'], state=DISABLED)
        entry_local.grid(row=0, column=2)

        self.text = Text(f_text, font=font['Principal'], bg=colr['BK'], fg=colr['WH'], bd=20, height=10, width=50)
        self.text.grid(row=1, column=2)

        x_text = Scrollbar(f_text, orient=HORIZONTAL, command=self.text.xview)
        x_text.grid(row=2, column=2, sticky=W + E)
        self.text.config(xscrollcommand=x_text.set)

        y_text = Scrollbar(f_text, orient=VERTICAL, command=self.text.yview)
        y_text.grid(row=1, column=3, sticky=N + S)
        self.text.config(yscrollcommand=y_text.set)
        f_text.grid(row=1, column=3)

        self.__body.pack()

        self.__foot = Frame(self.__root)

        f_foot = Frame(self.__foot)
        Label(f_foot, text=about_brapi['objetivo brapi'],
              font=font['foot'], bg=colr['BL_L'], bd=3).grid(row=0, column=0)
        f_foot.pack()

        self.__foot.pack()

        self.__root.mainloop()

    def do_search(self):
        searched = self.entry_search_str.get()

        self._update_local(*['search', searched])
        processed = processing_search(searched)

        self.listbox.delete(0, END)
        self.listbox.insert(END, *processed[0])

        self.text.delete(1.0, END)

        if processed[1][1]:

            for i in processed[1][0].basic_info():
                self.text.insert(END, i)

            self.listbox.insert(END, processed[1][0]['stock'])
        else:
            self.text.insert(END, processed[1][0])

        self.opt_menu_str.set('Search')

    def active_opt_menu(self, opt_str):
        self.listbox.delete(0, END)
        self.text.delete(1.0, END)

        self._update_local(*[opt_str.title().replace(' ', '')])

        names = stocks_names_to_tickers_dict()

        for i in names:
            stock_or_index = names[i][1]

            if opt_str == 'Indexes tickers':
                if stock_or_index == 'index':
                    self.listbox.insert(END, names[i][0])

            elif opt_str == 'Stocks names':
                if stock_or_index == 'stock':
                    self.listbox.insert(END, i)

            elif opt_str == 'Stocks tickers':
                if stock_or_index == 'stock':
                    self.listbox.insert(END, names[i][0])

    def do_play(self):
        item_captured = self.listbox.get(ANCHOR)
        menu_selected = self.opt_menu_str.get()

        self._update_local(*[menu_selected.title().replace(' ', ''), item_captured])

        self.listbox.delete(0, END)
        self.text.delete(1.0, END)

        self.listbox.insert(END, item_captured)

        self.__main_obj = processing_play(menu_selected, item_captured)

        try:
            for i in self.__main_obj.basic_info():
                self.text.insert(END, i)
        except AttributeError:
            self.text.insert(END, "Item not found or not selected")
            self.listbox.delete(0, END)
            print(f'Error: >> AttributeError')
            print("local: AppMain/do_play")

        self.opt_menu_str.set('')

    def _update_local(self, *args):
        all_local = ''

        for i in args:
            all_local += f'>{i}/'
        self.entry_text_str.set(f'../{all_local}')


AppMain()
