# Task 1 - .title()
text = input('Введите текст: ')
print(text.title())

# Task 2 - Hashtag generator 
text = input('Введите текст: ')
text = text.title()
text = text.replace(' ', '')
print('#' + text)