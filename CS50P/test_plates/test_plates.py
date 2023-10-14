from plates import is_valid

def test_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("A666") == False

def test_length():
    assert is_valid("I") == False
    assert is_valid("AAA2222") == False
    assert is_valid("CS") == True
    assert is_valid("AAAAAA") == True

def test_numbers():
    assert is_valid("AAA22") == True
    assert is_valid("AAA02") == False
    assert is_valid("AA22A") == False

def test_symbols():
    assert is_valid("CS.50!") == False
    assert is_valid("CS 50") == False