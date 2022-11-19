# while - цикл, который строится на условиях
# Может работать бесконечно
#while True:
#    print('Hello')
# Для остановки цикла while нужно писать счетчик
'''
count = 0
while count < 5:
    print(count)
    count += 1

command = ''
while command != 'exit':
    command = input('Введите имя и фамилию: ')
    print(command)

# break - сломать
# break завершает работу цикла
while True:
    command = input("Введите имя и фамилию: ")
    if command == 'exit':
        break
    else:
        print(command)
# break работает ТОЛЬКО с цикламми
# continue избегает нежелательного результата в цикле
while True:
    command = input("Введите имя и фамилию: ")
    if command == 'exit':
        break
    elif command.isdigit():
        continue
    else:
        print(command)

while True:
    phone_number = int(input('Номер телефона: '))
    name = input('Имя: ')
    surname = input('Фамилия: ')
    if phone_number <= 0:
        print("Ошибка: Номер телефона не может быть нулем или меньше его!")
        break
    print(phone_number)
    print(name, surname)
'''
# for как переборщик
# for - цикл который работает точное число раз
word = 'Python is my best friend!'
vowels = 'aeouiy'
vowels_count = 0
for letter in word: # letter - буква слова
    if letter in vowels:
        vowels_count += 1

print(vowels_count)
