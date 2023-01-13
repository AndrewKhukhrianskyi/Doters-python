# Task 1 - find circle square
def find_circle(radius):
    print(3.14 * (radius ** 2))

# Task 1 - find figure square
def find_square_fig(radius = None,
                    square_side = None,
                    polygon_sides = None):
    if radius is not None and square_side is None and polygon_sides is None:
        print(3.14 * (radius ** 2))
    elif square_side is not None and radius is None and polygon_sides is None:
        print(square_side * 2)
    elif polygon_sides is not None and square_side is None and radius is None:
        side_1, side_2 = polygon_sides # Распаковали список\кортеж на 2 значения
        print(side_1 * side_2)
    else:
        print('Error')

find_circle(2)
find_square_fig(polygon_sides=(4, 6))

# Task 3 - Vowels
def find_vowels(text):
    dictionary = 'aeuoiy'
    total = 0
    for elem in text.lower():
        if elem in dictionary:
            total += text.count(elem)
    print(f'Amount of vowels: {total}')

find_vowels('doggie')