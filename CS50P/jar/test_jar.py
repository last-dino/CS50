from jar import Jar
import unittest


def test_init():
    jar = Jar()
    assert jar._capacity == 12
    jar1 = Jar(10)
    assert jar1._capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    assert jar._size == 0
    jar.deposit(8)
    assert jar._size == 8
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar(10)
    assert jar._size == 0
    jar.deposit(8)
    assert jar._size == 8
    jar.withdraw(5)
    assert jar._size == 3
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
        jar.withdraw(5)