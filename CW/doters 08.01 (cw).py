# Переменная 
a = 4
print(a)

# Функция
def a():
    print(6)
    print(5)
    print(4)
# Для работы с функцией нужно обратиться к ней по имени
# a()
# Иногда для работы функции нужно передавать АРГУМЕНТЫ
# Аргумент - параметр, который нужен для работы ф-и
# (ЖЕЛАТЕЛЬНО) функции принято называть глаголом
def add_2(number): # передаем аргумент
    print(f'До добавления двойки: {number}')
    print(f'После добавления двойки: {number + 2}')

add_2(4)

def find_distance(speed, time):
    # расстояние = скорость * время
    print(speed * time)
# Кол-во переданных аргументов для него ВАЖНО и равно кол-ву требуемых
find_distance(12,2)

# Пример задания аргумента по умолчанию
def add_4(number = 1):
    print('Добавили четверку!')
    print(number + 4)

# Передача аргументов очень чувствительна
def add_nums(num = 1, num2 = 1, num3 = 1):
    print(num + num2 + num3)
#add_nums(num2 = 6,
#         num3 = 3)

def find_value(distance = None,
               speed = None,
               time = None):
        # неизвестно расстояние
    if speed is not None and time is not None:
        print(speed * time)
        # неизвестно время
    elif speed is not None and distance is not None:
        print(distance / speed)
        # неизвестна скорость
    elif distance is not None and time is not None:
        print(distance / time)
    else:
        print('Error!')

find_value(distance = 60,
           speed = 20)

'''
Homework:
1. Почитать о функциях: https://www.youtube.com/watch?v=DJAlfolEv9A
2. Написать функцию, которая будет искать площадь круга
3. Модифицировать функцию из задачи 2, которая будет искать площадь квадрата, прямоугольника
4. Написать функцию, которая будет искать только гласные буквы в тексте
'''




