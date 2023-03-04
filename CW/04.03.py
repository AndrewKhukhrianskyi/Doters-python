from tkinter import *
from random import randint

import tkinter.messagebox as mb

'''
def show_messagebox1():
    mb.showinfo(title='Окно',
                message = 'Вы кликнули!')

def show_messagebox2():
    mb.showwarning(title='Окно',
                message = 'Вы кликнули!')

def show_messagebox3():
    mb.showerror(title='Окно',
                message = 'Вы кликнули!')

window = Tk()

window.title('Окно')
window.geometry('200x100')

window.resizable(False, False)

btn1 = Button(width = 8,
             height = 1,
             command = show_messagebox1,
             text = 'Click_1')

btn2 = Button(width = 8,
             height = 1,
             command = show_messagebox2,
             text = 'Click_2')

btn3 = Button(width = 8,
             height = 1,
             command = show_messagebox3,
             text = 'Click_3')

widgets = [btn1, btn2, btn3]

for widget in widgets:
    widget.pack()
'''
def generate_random():
    mb.showinfo(title = 'Результат',
                message = f"Ваше число: {randint(1, 100)}")

window = Tk()

window.title('Окно')
window.geometry('200x100')

window.resizable(False, False)

btn = Button(width = 8,
             height = 1,
             text = 'Click!',
             command = generate_random)
btn.pack()
window.mainloop()

'''
HW
1. Почитать о messagebox (tkinter)
2. Написать приложение "Больше\меньше"
    Игрок вписывает в поле число и нажимает на кнопку "Play"
    Компьютер создает тоже свое случайное число
    Вывести на экран сообщение об полученных числах игрока и компьютера
    Также вывести сообщение (showinfo) о том, кто победи
3. Улучшить калькулятор с классной работы (18.02) прикрутив сообщение об ошибке о том,
что человек делит на 0
'''

