from fibonacci import fibonacci

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