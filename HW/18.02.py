from tkinter import *

from random import choice

def get_random_text():
    list_text = ['Message!', 'Another message!',
                 'And Another Message!']
    random_text = choice(list_text)
    print(random_text)


# Task 1 - Random button

window = Tk()

window.geometry('500x550')
window.resizable(True,True)
'''

# For Task 1

button = Button(width = 8, 
                height = 2,
                text = 'Click!',
                command=get_random_text)
button.pack(anchor='n')
'''

def get_data():
    widgets = name_field, surname_field, age_field
    result = []
    for widget in widgets:
        text = widget.get(0.0, END).strip()
        result.append(text)
    print(result)

name_field = Text(width=20,
                  height=2)
surname_field = Text(width=20,
                    height=2)
age_field = Text(width=20,
                 height=2)
button = Button(width=8,
                height=2,
                text = 'Click!',
                command=get_data)
widgets = [name_field, surname_field, age_field, button]

for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()
