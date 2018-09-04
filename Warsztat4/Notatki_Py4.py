## PLIKI

f = open('test.txt', 'w') #tworzy tez plik #open zwraca pythonowy obiekt pliku
#w - write
#a - append
#r - read

#at  - t oznacza tryb i domyslnie jest to tryb tekstowy

f.write('hello kasiu\n')
f.write('druga linia')
f.close() #wazne zamykamy pliki na koniec bo moze nam sie nie sflushowac albo przepelni sie nam limit otwartych plikow

#close jest spoko jesli sie nam wczesniej nie wypieprzy, powinnismy obsluzyc wyjatek

##Exceptions

#wszystkie dziedzicza po base exceptions

try: 
    # my_int = int('nie int :d') #ValueError
    # print(my_int)
    a = {'b': 'c'}
    print(a['d'])  #KeyError
except (ValueError): #te nawiasy sa wazne jesli mamy wiecej typow bo to tupla
    print('Dostalem value error')
    raise ValueError('Wiadomosc od wyjatku ') #przekazuje wyzej obiekt wyjatku
except KeyError:
    print("Mam KeyError")
except Exception as exc :
    print("moj wyjatek")
except: 
    print("whatever error") #lapie wszystkie mozliwe typy bledow
    raise #przekazuje wywalenie (error) wyzej
else: #wykona sie tylko wtedy gdy nie bedzie zadnego wyjatku 
    print('Zaden wyjatek nie zostal rzucony')
finally: #wykona sie zawsze czy sie wywali czy nie
    print('Wykona sie zawsze !')

##Zadanie1.py ->>

#context manager #obiekt #metody definiujace co zrobic przed otwarciem pliku i co po
# otwireanie z with samo po sobie sprzata
# To jest jedyny prawilny sposob otwierania robmy tylko tak :D

with open('test.txt', 'w') as f:  #obsluguje otwarcie i zamkniecie pliku #nie uzywamy juz close()
    f.write('Fajniejszy sposob') 
    
with open('test.txt', 'r') as f:  #obsluguje otwarcie i zamkniecie pliku #nie uzywamy juz close()
    file_data = f.read() #wczytuje caly plik na stringa
    file_data_n = f.read(4) #wczyta 4 znaki
    file_line = f.readline() #wczyta jedna linie #wskaznik przeskakuje na kolejna
    file_lines = f.readlines() #wczyta wszystkie linie do LISTY

    #po plikach mozna iterowac #po liniach pliku
    for line in file:
        print(line, end='')
    
#write w trybie tekstowym zwraca liczbe wpisanych znakow #jak uzyjemy polskich liter to nie bo zwraca liczbe bytow :D
