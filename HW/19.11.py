# Task 1 - Counter
count = 10
while count > -1:
    print(count)
    count -= 1

# Task 2 - Filter
number = int(input('Введите число: '))
while number > 0:
    if number % 2 == 0:
        print(number, "это четное!")
    else:
        print(number, "это нечетное!")
    number -= 1

