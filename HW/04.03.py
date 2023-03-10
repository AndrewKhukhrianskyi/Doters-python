from tkinter import *
from random import randint

import tkinter.messagebox as mb

# Task 1 - more or less
'''
def more_or_less():
    def generate_number():
        player_number = int(text_field.get(0.0, END).strip())
        pc_number = randint(1, 100)
        if player_number > pc_number:
            mb.showinfo(title = 'Результат!',
                        message = f'Игрок: {player_number}, PC: {pc_number}. Игрок победил!')
        elif player_number == pc_number:
            mb.showinfo(title = 'Результат!',
                        message = f'Игрок: {player_number}, PC: {pc_number}. Ничья!')
        else:
            mb.showinfo(title = 'Результат!',
                        message = f'Игрок: {player_number}, PC: {pc_number}. PC победил!')
    more_window = Toplevel()
    more_window.geometry('300x150')
    more_window.resizable(False, False)
    more_window.title('Больше\меньше')

    label = Label(more_window,
                  width=20,
                  text = 'Введите число ниже')
    text_field = Text(more_window,
                      width = 10,
                      height = 1)
    button = Button(more_window,
                    width=5,
                    height=2,
                    text = 'Click!',
                    command=generate_number)
    widgets = [label, text_field, button]
    for widget in widgets:
        widget.pack(anchor='n')

window = Tk()
window.geometry('300x150')
window.resizable(False, False)
window.title('Главное окно')

btn1 = Button(text='Больше\меньше',
              width = 15,
              height = 1,
              command=more_or_less)

widgets = [btn1]
for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()
'''

window = Tk()

window.geometry('400x300')

# Task 2 - Calculator

def add():
    n1 = int(f1.get(0.0, END).strip())
    n2 = int(f2.get(0.0, END).strip())
    oper = f3.get(0.0, END).strip()
    if oper == '+': # *, \, -, %
        print(f'Result {n1} + {n2} = {n1 + n2}')
    elif oper == '*':
        print(f'Result {n1} x {n2} = {n1 * n2}')
    elif oper == '/':
        try:
            print(f'Result {n1} : {n2} = {n1 / n2}')
        except ZeroDivisionError:
            print('Ошибка! Делим на 0!')
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