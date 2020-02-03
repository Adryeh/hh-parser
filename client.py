from parser import parse_data
from tkinter import *


# SETTINGS
MAIN_BG = 'lightblue'
BUTTON_SUCCESS_BG = '#4CAF50'
BUTTON_ALERT_BG = '#f44336'
SEPARATOR = '=' * 60


root = Tk()
root.resizable(False, False)
root.geometry('870x600+200+100')
button_frame = Frame(root, width=250, bg=MAIN_BG)
button_frame.pack(side="top", fill="both")


def customize_data(data):
    for idx, item in enumerate(data):
        yield f'\nID: {idx+1}\nTitle: {item.title}\nCompany: {item.company}\nMetro: {item.metro}\nLink: ' \
              f'{item.link}\nSalary: {item.salary}\n{SEPARATOR}'


def load_parsed_data():
    q = query.get()
    data = parse_data(query=q)
    text_area.insert(3.0, ''.join([v for v in customize_data(data)]))


def clean_text_area():
    text_area.delete(2.0, END)


# Label
label_for_query = Label(button_frame, text='Введите запрос: ', bg=MAIN_BG)
label_for_query.pack(side=LEFT)
# Entry
query = Entry(button_frame)
query.pack(side=LEFT)
query.insert(0, 'Python junior')
# Buttons
show_button = Button(button_frame, text='Вывести вакансии', command=load_parsed_data,
                     bg=BUTTON_SUCCESS_BG).pack(side=LEFT)
clean_button = Button(button_frame, text='Очистить', command=clean_text_area, bg=BUTTON_ALERT_BG).pack(side=LEFT)
# Text
text_area = Text(bg='gray', fg='white', width=95)
text_area.pack(side=LEFT, fill=BOTH, expand=True)
text_area.insert(1.0, f'!~You can edit this text area for your needs~!\n{SEPARATOR}')
# Other
scroll = Scrollbar(command=text_area.yview, width=25)
scroll.pack(side=RIGHT, fill=BOTH)
text_area.config(yscrollcommand=scroll.set)


root.mainloop()