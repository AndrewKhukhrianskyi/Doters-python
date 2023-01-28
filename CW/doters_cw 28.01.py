# Task 1 - Reverse text
def reverse_text(text):
    # Task 1 - By index
    print(text[::-1])
    # Task 2 - reversed
    result = ''.join(reversed(text))
    print(result)

#reverse_text('Dog')
# Task 2 - Palindrome
def is_palindrome(text):
    text = text.lower()
    if text == text[::-1]:
        print(True)
    else:
        print(False)

#is_palindrome('Мадам')
#is_palindrome('Кошка')
# Task 3 - Удвоитель
def twicer(element):
    print(element * 2)

twicer('dog')
twicer(4)

'''
HW 28.01
1. Почитать об блок-схемах и алгоритмах:
https://ru.wikipedia.org/wiki/Блок-схема#:~:text=Блок-схема%20—%20распространённый%20тип%20схем,собой%20линиями%2C%20указывающими%20направление%20последовательности.
2. КУРСОВАЯ РАБОТА:
    Никита - Шифратор
    Артем - Виселица
    Рома - Анализатор текста
3. На первой неделе реализовать алгоритм проекта
'''
