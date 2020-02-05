from tkinter import *
from config import MAIN_BG, BUTTON_SUCCESS_BG, BUTTON_ALERT_BG
from parser import parse_data
from data_analysis import get_all_salaries, get_ruble_salaries, get_avg_from_ruble_salaries
from utils import customize_data


root = Tk()
root.title('HeadHunter Parser')
root.resizable(False, False)
root.geometry('870x600+200+100')
settings_frame = Frame(root, bg=MAIN_BG)
settings_frame.pack(side=BOTTOM, fill=BOTH)
button_frame = Frame(root, bg=MAIN_BG)
button_frame.pack(side="top", fill="both")
data_frame = Frame(root, bg=MAIN_BG)
data_frame.pack(side=TOP, fill=BOTH)


def load_parsed_data():
    q = query.get()
    data = parse_data(query=q)
    return data


# global var
base_user_query = 'Vue junior'


def get_customized_data():
    data = load_parsed_data()
    all_s = get_all_salaries(data)
    rub_s = get_ruble_salaries(all_s)
    avg_s = get_avg_from_ruble_salaries(rub_s)
    salary_value['text'] = f'Средняя зарплата: {avg_s}'
    text_area.insert(3.0, ''.join([v for v in customize_data(data)]))


def clean_text_area():
    text_area.delete(2.0, END)


def set_font():
    size = font_entry.get()
    text_area.configure(font=f'Courier {size} bold')


# Label
label_for_query = Label(button_frame, text='Введите запрос: ', bg=MAIN_BG)
label_for_query.pack(side=TOP)
salary_value = Label(data_frame, bg=MAIN_BG)
salary_value.pack()
# Entry
query = Entry(button_frame, width=50)
query.pack(side=TOP)
query.insert(0, base_user_query)
font_entry = Entry(settings_frame)
font_entry.pack()
# Buttons
show_button = Button(button_frame, text='Вывести вакансии', width=25, command=get_customized_data,
                     bg=BUTTON_SUCCESS_BG).pack(side=TOP)
clean_button = Button(button_frame, text='Очистить', width=25,  command=clean_text_area, bg=BUTTON_ALERT_BG)\
    .pack(side=TOP)
font_set = Button(settings_frame, text='Set font', command=set_font).pack()
# Text
text_area = Text(bg='gray', fg='white', width=95)
text_area.pack(side=LEFT, fill=BOTH, expand=True)
text_area.insert(1.0, f'!~You can edit this text area for your needs~!\n')
# Other
scroll = Scrollbar(command=text_area.yview, width=25)
scroll.pack(side=RIGHT, fill=BOTH)
text_area.config(yscrollcommand=scroll.set)


root.mainloop()
