from fibonacci import fibonacci
import pytest

def test_fibonacci_of_1():
    assert fibonacci(1) == 0

def test_fibonacci_of_2():
    assert fibonacci(2) == 1

def test_fibonacci_of_3():
    assert fibonacci(3) == 1
    
def test_fibonacci_of_4():
    assert fibonacci(4) == 2
    
def test_fibonacci_of_5():  
    assert fibonacci(5) == 3
    
def test_fibonacci_large():
    assert fibonacci(50) == 7778742049
    
def test_fibonacci_of_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)