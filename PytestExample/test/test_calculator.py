from src.calculator import addition, subtraction, multiplication, division


def test_addition():
    res = addition(20,10)
    assert res == 30

def test_subtraction():
    res = subtraction(10,5)
    assert res == 5

def test_multiplication():
    res = multiplication(20,5)
    assert res == 100

def test_division():
    res = division(10,5)
    assert res == 2