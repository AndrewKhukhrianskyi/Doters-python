def add_2(number):
    # return достает параметр из ф-и
    return number + 2

result = add_2(6) # Сохраняем значение
print(result)


def find_circle(radius):
    return 3.14 * (radius ** 2)

result = find_circle(2)
#print(result)
def count_letters(text):
    consonants ='qwrtpsdfghjklzxcvbnm'
    vowels = 'eyuioa'
    consonants_total = 0
    vowels_total = 0
    text = text.lower()
    max_value_consonants = 0
    max_value_vowels = 0
    for elem in consonants:
        if elem in text:
            consonants_total += text.count(elem)
            if max_value_consonants < text.count(elem):
                max_value_consonants = text.count(elem)
                max_letter = elem
    for elem in vowels:
        if elem in text:
            vowels_total += text.count(elem)
            if max_value_vowels < text.count(elem):
                max_value_vowels = text.count(elem)
                max_letter_vowels = elem
    print(f'Часто встречаемая буква (Согласная): {max_letter}')
    print(f'Часто встречаемая буква (Гласная): {max_letter_vowels}')
    return consonants_total, vowels_total

result = count_letters("Hey, i'm a busy man!")
print(result)

"""
Homework:
1. Почитать о return: https://realpython.com/python-return-statement/#:~:text=The%20Python%20return%20statement%20is%20a%20special%20statement%20that%20you,can%20be%20any%20Python%20object.
2. Написать функцию, которая будет подсчитывать кол-во удаленных символов из текста
3. Модифицировать задачу 2 учитывая часто встречаемые символы
4. (*) Сформировать словарь, где будут хранится удаленные символы
"""
