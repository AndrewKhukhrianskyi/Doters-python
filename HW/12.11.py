# Task 1 - Odd\Even
number = int(input('Number: '))
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# Task 2 - Calculator (Mod)
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
elif operation == '%':
    print(num % num2)
elif operation == '**':
    print(num ** num2)
else:
    print('ERROR!')