from data_analysis import DATA
from tkinter import *


root = Tk()

root.geometry('670x400+200+100')



def customize_data(data):
    separator = '=' * 60
    for idx, item in enumerate(data):
        yield f'\nID: {idx+1}\nTitle: {item.title}\nCompany: {item.company}\nMetro: {item.metro}\nLink: {item.link}\nSalary: {item.salary}\n{separator}'



def show():
    text_area.insert(1.0, ''.join([v for v in customize_data(DATA)]))


show_button = Button(text='Вывести вакансии', command=show).pack()


text_area = Text(bg='gray', fg='white')
text_area.pack(side=LEFT, fill=BOTH)

scroll = Scrollbar(command=text_area.yview)
scroll.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll.set)


root.mainloop()

