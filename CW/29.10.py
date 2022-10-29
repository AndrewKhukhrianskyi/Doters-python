# Создание переменной
a = 3
b = 5
c = a + b
print(c)

# Создание переменной с input()
#name = input('Введи свое имя: ')
#surname = input('Введи фамилию, салага! ')

#print("Тебя зовут", name +'!')
#print("Твоя фамилия", surname + '!')

# input по умолчанию работает ТОЛЬКО со строками
num = input('Num 1: ') # '2'
num2 = input('Num 2: ') # '4'
print(num + num2)

# Фильтры: int() - преобразоывает в целое число
#num = int(input('Num 1: '))
#num2 = int(input('Num 2: '))
#print(num + num2)

# +, -, *, /, //
#num = int(input('Num 1: '))
#num2 = int(input('Num 2: '))
#print(num + num2)
#print(num - num2)
#print(num * num2)
#print(num // num2)

kg = int(input('Kilo: '))
print('KILO to POUNDS: ')
print(kg * 2.205)

длина = int(input('Enter line 1: '))
длина_2 = int(input('Enter line 2: '))

print('Square: ', длина * длина_2)
print('Perimeter: ', (длина * 2) + (длина_2 * 2))

# ** - возвести в степень
# % - остаток от деления
print(5 % 2)

number = int(input('Enter number: '))
step = int(input('Enter step: '))
print(number ** step, "- это степень числа", number, "а сама степень равна", step)
