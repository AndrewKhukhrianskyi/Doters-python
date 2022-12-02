# Task 1 - Zero count
from random import randint
# Создаем случайный набор чисел от 1 до 3
nums = [randint(1, 3) for num in range(randint(5, 10))]
print(nums)
count = 0
check_num = int(input('Числа у нас от 1 до 3. Какое число будем считать? '))
for num in nums:
    if num == check_num:
        count += 1
print(f'Кол-во {check_num} в списке равно {count}')

# Task 2 - Splitter
number = int(input('Enter Number: '))
number = list(str(number))
sum_count = 0
for digit in number:
    sum_count += int(digit)
print(f'SUM: {sum_count}')