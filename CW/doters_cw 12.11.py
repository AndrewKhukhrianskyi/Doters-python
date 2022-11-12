'''
number = int(input('Число: '))

if number > 0:
    print("Число положительное!")
else:
    print("Число отрицательное или 0!")


ask = input('Куда пойдешь? ')

# ask - строка
if ask == "Лес":
    print("Грибы пошли гулять за тобой!")
    print("Игра окончена!")

else:
    print("Ты стоишь на месте!")
    print("You WIN!")

# Task 1 - Add 2 nums
num = int(input("Число 1: "))
num2 = int(input("Число 2: "))
operation = input('Введи операцию (+ - сложение): ')

# * - умнож
# - минус
# / - обычное деление, // - деление нацело (отбрасывается часть с точкой)
if operation == '+':
    print(num + num2)
elif operation == '-':
    print(num - num2)
elif operation == '*':
    print(num * num2)
elif operation == '/':
    print(num / num2)
else:
    print('ERROR!')
'''

from random import randint

# randint(a, b) - создает случайное число в промежутке от a до b

player_1 = 100
player_2 = 100

player_1_dmg = 20
player_2_dmg = 20

# True\False = 1\0
has_knife = bool(randint(0,1))
agility_chance = 30

# is тоже самое что и ==
if has_knife is True:
    player_1_dmg *= 2 # 40


step = randint(1, 2)

if step == 1:
    print("Бьет игрок 1: ")
    if randint(1, 100) > agility_chance:
        print('Уворот!')
    else:
        print("Удар!")
        player_2 -= player_1_dmg
        print(f"Player 2 HP: {player_2}")  
else:
    print("Бьет игрок 2: ")
    if randint(1, 100) > agility_chance:
        print('Уворот!')
    else:
        print("Удар!")
        player_1 -= player_2_dmg
        print(f"Player 1 HP: {player_1}")  
    
    
    



