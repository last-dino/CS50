import unittest
from fuel import convert, gauge

def test_convert():
    assert convert("6/7") == 86
    assert convert("4/1") == 400
    with unittest.TestCase.assertRaises(unittest.TestCase, ValueError):
            convert("cat/dog")
    with unittest.TestCase.assertRaises(unittest.TestCase, ZeroDivisionError):
            convert("4/0")

def test_gauge():
    assert gauge(86) == "86%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"