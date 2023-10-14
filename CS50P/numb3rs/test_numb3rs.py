from numb3rs import validate

def test_nums():
    assert validate("256.0.0.0") == False
    assert validate("1000.0.1000.0") == False
    assert validate("75.456.76.65") == False
    assert validate("0.0.0.0") == True
    assert validate("9.0.107.0") == True

def test_quantity():
    assert validate("234") == False
    assert validate("234.0.0") == False
    assert validate("234.0.0.0") == True

def test_str():
    assert validate("cat") == False