from config import *

from tkinter import *

import re

import tkinter.messagebox as mb

'''
Main - это файл, который отвечает за запуск
приложения
'''

# Functions (Функции)
def find_data():
    regex = regex_text.get(0.0, END).strip()
    text = text_field.get(0.0, END).strip()
    '''
    TODO:
    1. Дописать логику find_data
    '''
    #re.findall(rf'{regex}', ...)
def clear_data():
    fields = [regex_text,
              text_field,
              result_field]
    ask = mb.askyesno(title='Message',
                      message = 'Clear data?')
    if ask: # ask == True
        for field in fields:
            field.delete(0.0, END)
            
        mb.showinfo(title='Message',
                    message = 'Data cleared!')

# UI (Графическая часть)
window = Tk()

window.title(TITLE)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(WINDOW_STATUS_RESIZABLE[0],
                 WINDOW_STATUS_RESIZABLE[1])

regex_label = Label(text = 'Enter regular expression below:',
                    width = LABEL_WIDTH)

regex_text = Text(width = REGEX_WIDTH,
                  height = REGEX_HEIGHT)

text_label = Label(text = 'Enter text below:',
                   width = LABEL_WIDTH)

text_field = Text(width = TEXT_WIDTH,
                  height = TEXT_HEIGHT)

result_label = Label(text = 'Result:',
                     width = LABEL_WIDTH)

result_field = Text(width = TEXT_WIDTH,
                    height = TEXT_HEIGHT)

clear_button = Button(width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      text = 'Clear!',
                      command = clear_data)
# TODO - прописать кнопку, которая вызывает find_data
widgets = [regex_label, regex_text,
           text_label, text_field,
           result_label, result_field, clear_button]

for widget in widgets:
    widget.pack(anchor='n')
    
window.mainloop()

'''
TODO:
1. Найти баги и отредактировать код
2. Реализовать функцию подсчета символов по отдельности (гласные, согласные и прочие символы)
3. Структурировать результат
Результат:
Согласные - ...
Гласные - ...
Прочие символы - ...
...
'''
