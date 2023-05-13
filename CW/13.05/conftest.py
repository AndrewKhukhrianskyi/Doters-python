import pytest

from random import randint

@pytest.fixture # метка, которая создает фикстуру
def generate_number(): # Фикстура
    return randint(1, 10)

@pytest.fixture
def generate_number_v2():
    return randint(-1000, 1000)

# yield - return
# Когда return, то после него ничего нельзя писать
# Когда yield - то логика после него не игнорируется
# yield когда работает с фикстурой выступает "заглушкой"
# Шаги перед yield выполняются перед тестом
# Шаги после yield выполняются после теста

@pytest.fixture
def add_one():
    assert True
    yield 1
    #assert False
