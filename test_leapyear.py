from leap import leapYear

def test_leap_year():
    assert leapYear(2024) == "Leap Year"

def test_leap_year_400():
    assert leapYear(2000) == "Leap Year"

def test_leap_year_100():
    assert leapYear(1900) == "Not a Leap Year"