from random import randint
# Работа с неключевыми аргументами (*)
def sum_numbers(*numbers):
    print(numbers)
    print(sum(numbers))
sum_numbers(1,2,3)
sum_numbers(1,5,6,7,8,1,2,4,5,7,44,20)
sum_numbers(4,5,6,2)

def odd_numbers(*numbers):
    print(numbers)
    for numbers in numbers:
        if numbers % 2 == 0:
            print(True)
        else:
            print(False)


odd_numbers(1,5,2,4,6,7,8,9,10,2,4,5)

# Работа с ключевыми аргументами (**)
def print_smth(**data):
    print(data)


print_smth(name = 'Andy' ,
           surname = 'Anderson',
           year = '10.01.1991')

# Task - Triangle perimeters
def find_perimeter(**figures):
    results = []
    for triangle_name, sides in figures.items():
        results.append(sum(sides))
    print(results)

find_perimeter(ABC = (10, 20, 30),
               CQX = (5, 12, 13),
               MNP = (4, 25, 10))

# Рекурсия (Рекурсивный подход)
def recursion():
    print('Рекурсия!')
    return recursion() # Работает до RecursionError

# Подход контроля рекурсии идет
def correct_recursion(n):
    print(n)
    if n == 0:
        return None
    else:
        return correct_recursion(n - 1)
correct_recursion(10)
'''
Homework
1. Почитать о ключевых и не ключевых аргументах
2. Почитать о рекурсии
3. Написать рекурсивную функцию, которая будет
проверять четность\нечетность числа
'''
