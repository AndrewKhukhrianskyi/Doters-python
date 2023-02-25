from tkinter import *

from random import choice

window = Tk()

window.geometry('400x300')
'''
def get_data():
    widgets = name_field, surname_field, age_field
    result = []
    for widget in widgets:
        text = widget.get(0.0, END).strip()
        result.append(text)
    print(result)

label_name = Label(width = 20,
                   height = 1,
                   text = 'Введите ваше имя ниже')

name_field = Text(width=20,
                  height=1)

label_surname = Label(width = 30,
                   height = 1,
                   text = 'Введите вашу фамилию ниже')

surname_field = Text(width=20,
                    height=1)

label_age = Label(width = 20,
                  height = 1,
                  text = 'Введите ваш возраст')

age_field = Text(width=20,
                 height=1)
button = Button(width=8,
                height=2,
                text = 'Click!',
                command=get_data)
widgets = [label_name, name_field,
           label_surname, surname_field,
           label_age, age_field, button]
'''
def add():
    n1 = int(f1.get(0.0, END).strip())
    n2 = int(f2.get(0.0, END).strip())
    oper = f3.get(0.0, END).strip()
    if oper == '+': # *, \, -, %
        print(f'Result {n1} + {n2} = {n1 + n2}')
    elif oper == '*':
        print(f'Result {n1} x {n2} = {n1 * n2}')
    elif oper == '/':
        print(f'Result {n1} : {n2} = {n1 / n2}')
    elif oper == '-':
        print(f'Result {n1} - {n2} = {n1 - n2}')
    elif oper == '%':
        print(f'Result {n1} mod {n2} = {n1 % n2}')
    else:
        print('ERROR!')
l1 = Label(width = 20,
           height = 1,
           text = 'Enter Number 1 below: ')
f1 = Text(width = 5,
          height = 1)
l2 = Label(width = 20,
           height = 1,
           text = 'Enter Number 2 below: ')
f2 = Text(width = 5,
          height = 1)
l3 = Label(width = 20,
           height = 1,
           text = 'Enter math operation: ')
f3 = Text(width = 5,
          height = 1)
button = Button(width = 8,
                height = 2,
                text = 'Click',
                command = add)
widgets = [l1, f1, l2, f2,
           l3, f3, button]
for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()

