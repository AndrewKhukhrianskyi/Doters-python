# Добавление библиотеки
from tkinter import *

text_title = input('Введите название окна: ')

window = Tk()
window.title(text_title)
# geometry устанаваливает размер окна
window.geometry('800x600')
# resizable блокирует изменение размера окна
window.resizable(False, False)
# mainloop позволяет переиспользовать приложение
window.mainloop()

"""
1. Почитать о Tkinter:
https://ru.wikipedia.org/wiki/Tkinter
2. Почитать о параметрах окна Tkinter:
https://younglinux.info/tkinter/window
3. Написать программу, которая будет создавать
случайное название окна
"""
