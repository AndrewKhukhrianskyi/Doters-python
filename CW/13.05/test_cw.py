import pytest

# Сначала работает фикстура
def test_gen_number(generate_number):
    number = generate_number
    assert number > 0
# Flaky - плавающий
def test_flaky(generate_number_v2):
    number = generate_number_v2
    assert number > 0

@pytest.mark.parametrize('number, result', [(1, 2), (2, 3), (3,4)])
def test_add_one(add_one, number, result):
    one = add_one
    assert number + one == result
    
'''
1. Почитать о фикстурах: https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
2. Почитать о yield (*): https://realpython.com/introduction-to-python-generators/
3. Написать фикстуру, которая генерирует случайное число
4. Написать тест, который проверяет четность сгенерированного числа
Если четное - assert True, else - assert False
'''
