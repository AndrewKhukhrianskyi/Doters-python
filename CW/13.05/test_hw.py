from random import randint

import pytest

@pytest.fixture
def generate_numbers():
    return randint(1, 10)

def test_check_number(generate_numbers):
    number = generate_numbers
    if number % 2 == 0:
        assert True
    else:
        assert False