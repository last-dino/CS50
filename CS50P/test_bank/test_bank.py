from bank import value

def test_hello():
    assert value("Hello") == "0"

def test_h():
    assert value("Hey") == "20"

def test_other():
    assert value("What's up?") == "100"
    assert value("$100") == "100"

def test_space():
    assert value("   hello  ") == "0"
    assert value("  hey  ") == "20"
    assert value("   what's up?   ") == "100"

def test_upper():
    assert value("HELLO") == "0"
    assert value("HEY") == "20"
    assert value("WHAT'S UP?") == "100"

def test_lower():
    assert value("hello") == "0"
    assert value("hey") == "20"
    assert value("what's up?") == "100"
