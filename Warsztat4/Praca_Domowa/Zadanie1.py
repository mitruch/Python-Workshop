class DateError(Exception):
    pass

class InvalidDayError(DateError):
    pass

class InvalidMonthError(DateError):
    pass

class InvalidYearError(DateError):
    pass

class Date:
    day = 1
    month = 1
    year = 2000
    def __init__(self, day, month, year):
        if isinstance(year, int):
            self.year = year
        else:
            raise InvalidYearError
        if isinstance(month, int) and 1 <= month <= 12:
            self.month = month
        else:
            raise InvalidMonthError
        if isinstance(day, int):
            if month == 2 and 1 <= day <= 28:
                self.day = day
            elif month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
                self.day = day
            elif month in [4, 6, 9, 11] and 1 <= day <= 30:
                self.day = day
            else:
                raise InvalidDayError
        else:
            raise InvalidDayError
        
      


date = Date(30, 5, 2020)
assert date.day == 30
assert date.month == 5
assert date.year == 2020

try:
    date2 = Date(31.6, 15.9, 2020.5)
except DateError:
    print('Błąd daty wyrzucony tak jak trzeba')
except InvalidYearError:
    print('Błąd year wyrzucony tak jak trzeba')
except InvalidMonthError:
    print('Błąd month wyrzucony tak jak trzeba')
else:
    print('Bez błędu, a trzeba było :(')