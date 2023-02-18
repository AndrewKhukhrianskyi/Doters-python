from tkinter import *

window = Tk()

window.geometry('500x550')
window.resizable(True,True)

# command работает с функцией БЕЗ параметров
def smth():
    print('Произошло истеричное тыканье!')
    
def get_data():
    text = text_field.get(0.0, END)

def insert_data(): # .insert(...)
    text = input('Text: ')
    text_field.insert(0.0, text)

def delete_data(): # .delete(...)
    text = text_field.delete(0.0, END)

    
# Создание кнопки
button = Button(width = 15,
                height = 2,
                text = 'Достать текст!',
                command = get_data)
button2 = Button(width = 15,
                height = 2,
                text = 'Вставить текст!',
                command = insert_data)
button3 = Button(width = 15,
                height = 2,
                text = 'Удалить текст!',
                command = delete_data)
# Создания текстового поля
text_field = Text(width = 30,
                  height = 20)
# .pack() - прикрепляет виджет СТРОГО по сторонам света
widgets = [text_field, button, button2, button3]

for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()

'''
Homework 18.02
1. Почитать о экране и кнопках
2. Рандом тык. Написать приложение, которое будет выводить случайное сообщение на экран, при нажатии на кнопку
3. Анкета. Создайте приложение-анкету, где будете собирать информацию о пользователе (Имя, Фамилия, Возраст)
Результат вывести в print
'''
