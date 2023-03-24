# Task 1 - No space
def no_space(x):
    return x.replace(' ', '')

print(no_space('AAA aaa AAA'))

# Task 2 - Is palindrome?

def is_palindrome(numbers):
    result = []
    for number in numbers:
        if str(number) == str(number)[::-1]:
            result.append(1)
        else:
            result.append(0)
    return result

print(is_palindrome([123, 202, 444, 0, 103]))