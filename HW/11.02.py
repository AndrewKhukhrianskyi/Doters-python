from tkinter import *
from random import choice

# Task 1 - Random title
def generate_random_title():
    title_list = ["Окно", "Окошко", "Окошкевич"]
    return choice(title_list)

root = Tk()
root.geometry('500x200')
root.title(generate_random_title())

root.mainloop()