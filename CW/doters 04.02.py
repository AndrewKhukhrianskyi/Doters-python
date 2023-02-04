# Task - Palindrome
def is_palindrome(text):
    text = text.lower()
    if text == text[::-1]:
        print(True)
    else:
        print(False)

# Task - Cipher
def text_to_number(text):
    text = text.lower()
    cipher = []
    alphabet = {'a':'00', 'b' : '01', 'c' : '02'}
    for letter in text:
        try:
            text = text.replace(letter, alphabet[letter] + ',')
        except KeyError:
            pass
    return text

text = 'I am a beautiful guy'

#print(text_to_number(text))

    
    
'''
HW 04.02

1. Доработать алгоритмы по вашим проектам
(Для Вики: Текстовая приключенческая новелла)
2. Повторить функции
3. Реализовать (хотя бы частично) свой проект
'''
