from tkinter import *

from App.app_action import processing_search, processing_play, processing_menu_opt
from App.app_config import colr, font
from access.data_updates import uploading_and_update_data
from api_data.about_api import about_brapi
from api_data.data_actions import stocks_for_types


class AppMain:

    def __init__(self):
        self.__main_obj = None

        self.last_local = None
        self.local_captured = None

        self.__root = Tk()

        self.buts = list()

        self.entry_search_str = StringVar()
        self.entry_text_str = StringVar()

        self.opt_menu_str = StringVar()
        self.opt_menu_tuple = ('Indexes tickers', 'Indexes names', 'Stocks tickers', 'Stocks names')

        _menu = Menu(self.__root, bd=10)

        menu_types = Menu(_menu, tearoff=0)
        all_types = "stock", "fund", "bdr"
        for i in all_types:
            menu_types.add_command(label=f"{i.title()}'s", command=lambda select=i: self.categories_select(select))

        _menu.add_cascade(label='Categories', menu=menu_types)

        menu_config = Menu(_menu, tearoff=0)
        menu_config.add_command(label='Initial setting', command=self._initial_setting)
        menu_config.add_command(label='Update data', command=self.update_data)
        _menu.add_cascade(label='Config', menu=menu_config)

        self.__root.config(menu=_menu)

        self.img_logo = PhotoImage(file=r'..\assets\logo.png')
        self.img_magnifier = PhotoImage(file=r'..\assets\magnifier.png')

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
        self.opt_menu = OptionMenu(f_list, self.opt_menu_str, *self.opt_menu_tuple,
                                   command=lambda opt_str=self.opt_menu_str: self.active_opt_menu(opt_str))
        self.opt_menu.config(bg=colr['WH'], state=NORMAL, width=28, bd=3, anchor='center')
        self.opt_menu.grid(row=0, column=1)

        self.listbox = Listbox(f_list, font=font['Principal'], bg=colr['BK'], fg=colr['WH'], bd=16)
        self.listbox.grid(row=1, column=1)

        x_scr_list = Scrollbar(f_list, orient=HORIZONTAL, command=self.listbox.xview)
        x_scr_list.grid(row=2, column=1, sticky=W + E)
        self.listbox.config(xscrollcommand=x_scr_list.set)

        y_scr_list = Scrollbar(f_list, orient=VERTICAL, command=self.listbox.yview)
        y_scr_list.grid(row=1, column=0, sticky=N + S)
        self.listbox.config(yscrollcommand=y_scr_list.set)
        f_list.grid(row=1, column=1)

        f_but = Frame(self.__body)
        cont = 0
        while cont < 8:
            self.buts.append(Button(f_but, text='', width=5, height=1))
            cont += 1

        for i in self.buts:
            i.pack()
        f_but.grid(row=1, column=2)

        f_text = Frame(self.__body)
        entry_local = Entry(f_text, font=font['search'], textvariable=self.entry_text_str)
        entry_local.config(width=48, bd=4, bg=colr['WH'], fg=colr['BK'], state=DISABLED)
        entry_local.grid(row=0, column=2)

        self.text = Text(f_text, font=font['Principal'], bg=colr['BK'], fg=colr['WH'], bd=20, height=10, width=50)
        self.text.grid(row=1, column=2)

        x_scr_text = Scrollbar(f_text, orient=HORIZONTAL, command=self.text.xview)
        x_scr_text.grid(row=2, column=2, sticky=W + E)
        self.text.config(xscrollcommand=x_scr_text.set)

        y_scr_text = Scrollbar(f_text, orient=VERTICAL, command=self.text.yview)
        y_scr_text.grid(row=1, column=3, sticky=N + S)
        self.text.config(yscrollcommand=y_scr_text.set)
        f_text.grid(row=1, column=3)

        self.__body.pack()

        self.__foot = Frame(self.__root)

        f_foot = Frame(self.__foot)
        Label(f_foot, text=about_brapi['objetivo brapi'],
              font=font['foot'], bg=colr['BL_L'], bd=3).grid(row=0, column=0)
        f_foot.pack()

        self.__foot.pack()

        self._activate_configuration()

        self.__root.mainloop()

    def _activate_configuration(self):
        self.local_captured = 'initial', None

        self.entry_text_str.set('../>')
        self.opt_menu_str.set('Options Menu')

        self.__root.title('API - Brapi')
        self.__root.geometry('+400+200')
        self.__root.resizable(False, False)
        self.__root.config(bg=colr["BL_L"])

        self.buts[0].config(text=' < ', state=DISABLED, command=self.do_return)
        self.buts[1].config(text=' >> ', state=NORMAL, command=self.do_play)
        self.buts[3].config(text='more', state=DISABLED, command=self.go_to_more)

    def _initial_setting(self):
        self.__main_obj = None

        self.last_local = None
        self.local_captured = 'initial', None

        self.entry_text_str.set('../>')
        self.opt_menu_str.set('Options Menu')

        self.listbox.delete(0, END)
        self.text.delete(1.0, END)

        self.buts[0].config(state=DISABLED)
        self.buts[3].config(state=DISABLED)

    def _write_entry_local_(self, *args):
        all_local = ''

        for i in args:
            all_local += f'>{i}/'
        self.entry_text_str.set(f'../{all_local}')

    def do_search(self):
        searched = self.entry_search_str.get()

        self._write_entry_local_(*['search', searched])
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

        self.last_local = self.local_captured
        self.local_captured = 'search', searched

        self.buts[0].config(state=NORMAL)

    def active_opt_menu(self, opt_str):
        self.listbox.delete(0, END)
        self.text.delete(1.0, END)

        self._write_entry_local_(*[opt_str.title().replace(' ', '')])

        processed = processing_menu_opt(opt_str)
        self.listbox.insert(END, *processed)

        self.last_local = self.local_captured
        self.local_captured = 'menu', opt_str

        self.buts[0].config(state=NORMAL)
        self.buts[1].config(state=NORMAL)

    def do_play(self):
        item_captured = self.listbox.get(ANCHOR)
        menu_selected = self.opt_menu_str.get()

        self._write_entry_local_(*[menu_selected.title().replace(' ', ''), item_captured])

        self.listbox.delete(0, END)
        self.listbox.insert(END, item_captured)

        if self.__main_obj is None or self.__main_obj['stock'] != item_captured:
            self.__main_obj = processing_play(menu_selected, item_captured)

        self.text.delete(1.0, END)
        try:
            for i in self.__main_obj.basic_info():
                self.text.insert(END, i)
        except AttributeError:
            self.text.insert(END, "Item not found or not selected")
            self.listbox.delete(0, END)

            print(f'Error: >> AttributeError')
            print("local: AppMain/do_play")

            self.do_return()
        else:
            self.opt_menu_str.set('')

            self.last_local = self.local_captured
            self.local_captured = 'play', menu_selected, item_captured

            self.buts[1].config(state=DISABLED)
            self.buts[3].config(state=NORMAL)

    def do_return(self):

        match self.last_local:

            case 'initial', None:
                self._initial_setting()

            case 'search', searched:
                self.entry_search_str.set(searched)
                self.do_search()
                self.last_local = 'initial', None
                self.buts[1].config(state=NORMAL)
                self.buts[3].config(state=DISABLED)

            case 'menu', opt_str:
                self.opt_menu_str.set(opt_str)
                self.active_opt_menu(opt_str)
                self.last_local = 'initial', None
                self.buts[1].config(state=NORMAL)
                self.buts[3].config(state=DISABLED)

            case 'categories', type_selected:
                self.categories_select(type_selected)
                self.last_local = 'initial', None
                self.buts[1].config(state=NORMAL)
                self.buts[3].config(state=DISABLED)

            case 'play', menu_selected, item_captured:
                self.opt_menu_str.set(menu_selected)
                self.listbox.delete(0, END)
                self.listbox.insert(0, item_captured)
                self.listbox.selection_anchor(0)
                self.do_play()
                self.buts[3].config(state=NORMAL)
                self.buts[2].config(state=DISABLED)

    def go_to_more(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, *self.__main_obj.basic_info())

        self.text.delete(1.0, END)
        for i in self.__main_obj.qualified_data():
            self.text.insert(END, i)

        local_one = self.last_local
        local_two = self.local_captured

        self.last_local = local_two
        self.local_captured = local_one

        self.buts[3].config(state=DISABLED)

    def update_data(self):
        try:
            uploading_and_update_data()
        except Exception as ex:
            print('Error(Local: update AppMain) >> ', ex)
        else:
            self._initial_setting()
            self.text.insert(END, 'Update OK')

    def categories_select(self, type_selected):
        self._initial_setting()

        self._write_entry_local_(*['categories', type_selected])
        self.opt_menu_str.set('Stocks names')

        self.listbox.insert(END, *stocks_for_types(type_selected))

        self.last_local = self.local_captured
        self.local_captured = 'categories', type_selected

        self.buts[0].config(state=NORMAL)
        self.buts[1].config(state=NORMAL)


AppMain()
