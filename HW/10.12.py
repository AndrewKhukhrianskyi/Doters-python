# Task 1 
from random import randint 

random_numbers = [randint(1, 100) for elem in range(5, 100)]

print(random_numbers)
print(f'Amount of numbers: {len(random_numbers)}')

# Сумма чисел
print(f'Sum numbers: {sum(random_numbers)}')
# Максимальное число из ряда
print(f'Maximum value from the list numbers: {max(random_numbers)}')
# Среднее арифметическое число из ряда
print(f'Average arithmetic number from list: {sum(random_numbers) // len(random_numbers)}')

# Task 2 - Word sorter
sentence = input('Enter any sentence: ').lower().split()
ru_word_list = []
en_word_list = []
ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
en_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
for word in sentence:
    ru_letter_count = 0
    en_letter_count = 0
    for letter in word:
        if letter.isalpha() and letter in ru_alphabet:
            ru_letter_count += 1
        elif letter.isalpha() and letter in en_alphabet:
            en_letter_count += 1
    if ru_letter_count == len(word):
        ru_word_list.append(word)
    elif en_letter_count == len(word):
        en_word_list.append(word)
print(f'Russian words: {ru_word_list}')
print(f'English words: {en_word_list}')