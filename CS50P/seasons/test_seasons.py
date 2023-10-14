from seasons import convert
import pytest
import datetime

def test_seasons():
    with pytest.raises(SystemExit) as e:
        convert("2000-02-30")
    assert e.type == SystemExit
    assert e.value.code == "Invalid date"
    assert convert(str(datetime.date.today() - datetime.timedelta(days = 365))) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(str(datetime.date.today() - datetime.timedelta(days = 730))) == "One million, fifty-one thousand, two hundred minutes"


def test_exit():
    with pytest.raises(SystemExit) as e:
        convert("1990-05-32")
    assert e.type == SystemExit
    assert e.value.code == "Invalid date"