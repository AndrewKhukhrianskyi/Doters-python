'''
# Цикл for может работать как переборщик
text = 'Amogus'
for letter in text: # letter - буква из текста
    print(letter)
# range() создает ряд чисел
for number in range(0, 10):
    print(number)

# range() может принять неявно одно выражение и идти по нему
for number in range(10): # -> 0, 10
    print(number)

# step в range позволяет пропускать числа
for number in range(10, -1, -2):
    print('RESULT')
    print(number)

# BAD PRACTICE
message = 'Message'
for elem in range(len(message)):
    print(message[elem])

text = 'Мой дом - моя крепость!'
# break - завершить работу цикла
for letter in text:
    if letter == ' ':
        break
    print(letter)

text = input('Текст: ')
vowels = 'аеоуыиёяюэ'
count = 0
#.count(буква) - подсчитывает выражение в тексте
for letter in vowels:
    count += text.count(letter)
print("Кол-во гласных букв в тексте:", count)
'''


# Список - тип данных, который может хранить другие типы данных
arr = [1, 2, 3, 4, 5]
for elem in arr:
    print('ELEM FROM ARR:', elem)
# Свойства списка
# можно соединить с другим списком
print([1, 2] + [5,9])
# .append() добавляет новое выражение в конец списка
print(arr)
arr.append(6)
print(arr)

numbers = [67,45,21,24,5,0,10,51252]
summa = 0
for number in numbers:
    summa += number
print(summa)

# sum(list) - подсчитывает сумму ЧИСЕЛ. Не работает, если есть что-то кроме чисел
print(sum(numbers))
