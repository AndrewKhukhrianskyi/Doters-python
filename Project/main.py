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
    if len(regex) == 0:
        mb.showerror(title='Error',
                     message='Please, enter regular expression!')
        mb.showerror(title='Сообщение',
                     message = 'Это сообщение для сообщения с ошибкой!')
    else:
        text = text_field.get(0.0, END).strip()
        result_regex = re.findall(rf'{regex}', text) # [1, 2, 3, 4]
        result_field.insert(0.0, str(result_regex))
        mb.showinfo(title='Message',
                    message = 'Данные были записаны в поле результата!')
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

def analyze_text(language_status='en'):
    text = text_field.get(0.0, END).strip().lower()
    result = []
    result_text = ''
    if language_status == 'en':
        # Кол-во гласных букв реализовывается тут
        vowels = 'aeouiy'
        consonants = 'qwrtpsdfghjklzxcvbnm'
        vowels_count = 0
        for vowel in vowels:
            vowels_count += text.count(vowel)
        result.append(vowels_count)
        # Кол-во согласных букв реализовывается тут
        consonants_count = 0
        for consonant in consonants:
            consonants_count += text.count(consonant)
        result.append(consonants_count)
        # Кол-во символов реализовывается тут
        result.append(len(text))
        # Часто встречаемая буква реализовывается тут
        dictionary_letters = {} # {'a':..., 'b' : ...
        for letter in LANGUAGE_EN:
            dictionary_letters[letter] = text.count(letter)
        maximum_value = max(dictionary_letters.values())

        dictionary_letters = dict(zip(dictionary_letters.values(),
                                      dictionary_letters.keys()))
        result.append(f'{dictionary_letters[maximum_value]}({maximum_value})')
        for elem in range(len(ANALYZE_TEXT_LIST)): # range(0, 8)
            try:
                result_text += f'{ANALYZE_TEXT_LIST[elem]} {result[elem]}\n'
            except IndexError:
                result_text += f'{ANALYZE_TEXT_LIST[elem]} Нема ничего, дядя!\n'
        result_field.insert(0.0, result_text)
        

        
        
        

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
regex_button = Button(width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      text = 'Find!',
                      command = find_data)
analyze_button = Button(width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      text = 'Analyze!',
                      command = analyze_text)

widgets = [regex_label, regex_text,
           text_label, text_field,
           result_label, result_field, clear_button,
           regex_button, analyze_button]

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
