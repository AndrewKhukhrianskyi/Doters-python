import pytest

# cd - переход в папку
# cls - отчистка экрана
# ВСЕ ТЕСТЫ НАЧИНАЮТСЯ с конструкции test_
# assert работает так
# Если True - все ок
# Если False - AssertionError
# Запуск: pytest название файла.py
@pytest.mark.metka
def test_concatenation():
    def concatenate(first, second):
        return first + second
    assert concatenate(2, 2) == 5

# метка ставится перед тестом
@pytest.mark.metka
def test_a():
    assert True

def test_b():
    assert True

def test_c():
    assert True
    
'''
1. Указать явно (pytest файл::тест)
2. Метки (@pytest.mark.метка)
pytest файл -m метка
'''

# Task - Odd\even
@pytest.mark.odd
def test_is_odd():
    from random import randint
    def is_odd(first):
        if first % 2 == 1:
            return True
        else:
            return False
        
    assert is_odd(randint(2, 6)) == True

'''
1. Разобрать служебные (parametrize, skipif, skip)
https://docs.pytest.org/en/7.1.x/historical-notes.html#string-conditions

2. Написать тест на ввод имени и фамилии и сделать следующие проверки
- Имя не начинается с большой буквы (Пример: вася)
- Имя содержит внутри большие буквы (Пример: вАся)
- Имя содержит числа или символы

3. Написать тест на проверку пароля:
- Пароль содержит минимум 8 и максимум 16 символов
- Пароль содержит буквы латинского алфавита, числа и символы
- Пароль начинается с большой буквы
- Пароль не содержит символов
'''
