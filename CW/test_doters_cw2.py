import pytest

# Офомрление меток
# @pytest.mark.skip()
# @pytest.mark.skipif()
# @pytest.mark.parametrize

# Опционально, можно указать причину 
@pytest.mark.skip(reason = 'Always return true')
def test_true():
    assert True

# @pytest.mark.skipif(условие, причина)
import sys


@pytest.mark.skipif(sys.version_info < (3, 8), reason='Old version of Python')
def test_true_v2():
    assert True

# @pytest.mark.parametrize((аргумент1, аргумент2, ..., аргументN), [(данные1), (данные2) ...])
@pytest.mark.parametrize(('number', 'number2', 'number3', 'result'), ([4, 2, 5, 11],))
@pytest.mark.add
def test_add_1(number, number2, number3, result):
    assert number + number2 + number3 == result

'''
1. Почитать о служебных (skip, skipif, parametrize) метках:
https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=fixture#id25
2. Почитать о фикстурах:
https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=fixture#pytest-fixture
3. Решить задачу:
https://www.codewars.com/kata/62c93765cef6f10030dfa92b
4. Написать проверочные тесты на задачу 3
'''



    
    

