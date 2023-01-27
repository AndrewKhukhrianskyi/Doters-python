# Task 1 - Recursion function

def recursion_odd_even(number):
    if number % 2 == 0:
        print(f'{number} - четное')
        return recursion_odd_even(number - 1)
    else:
        print(f'{number} - нечетное')
        return number

recursion_odd_even(6)