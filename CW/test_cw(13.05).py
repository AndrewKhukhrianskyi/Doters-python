import pytest

def test_gen_num(generate_number):
    number = generate_number
    assert number > 0
