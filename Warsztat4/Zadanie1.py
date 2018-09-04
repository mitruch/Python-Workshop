class IncorrectGuessError(Exception):
    def __init__(self, difference):
        super().__init__()
        self.difference = difference
    # pass # czyli nie robie nic

class NumberTooSmallError(IncorrectGuessError):
    pass

class NumberTooBigError(IncorrectGuessError):
    pass

def guess(number):
    number_to_guess = 10
    # if number != number_to_guess:
    #     raise IncorrectGuessError()
    # if number == number_to_guess:
        # print('BRAWO')
    if number > number_to_guess:
        raise NumberTooBigError(
            number - number_to_guess
        )
    elif number < number_to_guess:
        raise NumberTooSmallError(
            number_to_guess - number
        )
    print('BRAWO')


try:
    guess(20)
    # guess(5)
except NumberTooBigError as ntb:
    print('Za duzo o {}'.format(ntb.difference))
except NumberTooSmallError as nts:
    print('Za malo o {}'.format(nts.difference))   
except IncorrectGuessError:
    print('Nie zgadles')


# Tak juz nie robimy ! :D

try:
    f = open('test.txt', 'w') #tworzy tez plik #open zwraca pythonowy obiekt pliku
    f.write('hello kasiu\n')
    f.write('druga linia')
finally:
    f.close() 


#context manager #obiekt #metody definiujace co zrobic przed otwarciem pliku i co po
# otwireanie z with samo po sobie sprzata
# To jest jedyny prawilny sposob otwierania robmy tylko tak :D

with open('test.txt', 'w') as f:  #obsluguje otwarcie i zamkniecie pliku #nie uzywamy juz close()
    f.write('Fajniejszy sposob') 

