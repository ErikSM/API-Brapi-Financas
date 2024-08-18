from tkinter import *

from App.app_action import processing_search
from App.app_config import colr, font
from access.api_request import make_request
from api_data.about_api import about_brapi
from api_data.data_actions import stocks_names_to_tickers_dict


class AppMain:

    def __init__(self):
        self.__root = Tk()

        self.search = StringVar()

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
        self.search.set('')
        entry_search = Entry(f_search, font=font['search'], textvariable=self.search, bd=9)
        entry_search.grid(row=0, column=1)

        button_search = Button(f_search, image=self.img_magnifier)
        button_search.config(command=self.do_search)
        button_search.grid(row=0, column=2)
        f_search.pack(side=LEFT)

        self.__head.pack()

        self.__body = Frame(self.__root)

        f_list = Frame(self.__body)
        self.listbox = Listbox(f_list, font=font['Principal'], bg=colr['BK'], fg=colr['WH'], bd=10)
        self.listbox.grid(row=1, column=1)
        f_list.grid(row=1, column=1)

        f_text = Frame(self.__body)
        self.text = Text(f_text, font=font['Principal'], bg=colr['BK'], fg=colr['WH'], bd=20, height=10, width=50)
        self.text.grid(row=1, column=2)
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
        searched = self.search.get()

        processed = processing_search(searched)

        self.listbox.delete(0, END)
        self.listbox.insert(END, *processed[0])

        self.text.delete(1.0, END)
        if processed[1][1]:
            self.text.insert(END, *processed[1][0].basic_info())
        else:
            self.text.insert(END, processed[1][0])



AppMain()
