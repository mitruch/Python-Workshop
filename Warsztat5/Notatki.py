#uzywajmy kododwania utf8

#hierarchia wyjatkow
# wszystko dziedziczy po BaseException ale po nim nie dziedziczymy i go nie lapiemy
# pierwszym po ktorym mozemy dziedziczyc i lapac jest Exception, ale jak pokemony xd

#tuplowe list comprehandsdk to generator...

#GENERATORY
#generatory są jednorazowego użytku
#po generatorach mozna iterowac

#generatory tworzymy z funkcji
#yield - zwroci wartosc, to taki return ale nie czysci naszej pamieci
#generator, funkcja ktora zapamietuje swoj stan miedzy wywolaniami
#taka funkcja zwraca generator 

#next(iterator) pobiera nastepna wartosc z czegos co mozna iterowac
#w pythonie wyjatki sa wzglednie tanie wiec mozemy nimy rzucaca swobodniej niz w C++
#iteratory w pythonie to tez konwencja, wystopowanie iteracji rzuca wyjatkiem StopIteration

#Generator za kazdym razem zwraca nam kolejny yield
#W jednym generatorze mozemy miec wiecej niz jeden yield
#Generatory pamietaja swoj stan pomiedzy kolejnymi wykonaniami

#jezeli wezmiemy iterator z iteratora to zwróci siebie w aktualnej pozycji, tylko jezeli z np. z listy to nowy
#iter uruchamia na obiekcie __iter__(self) ktora zwraca iterator
#gdyby nie bylo generatorow musielibysmy pisac wlasne iteratory
#uzywajac generatorow oszczedzmy pamiec bo wartosci sa wyliczane na biezaco a nie trzymane w pamieci
#w python 2.7 range() nie byl generatorem od 3.6 python jest generatorem

################################
#Rozwijanie wiecej niz jednego projektu w tym samym srodowisku - tworzymy srodowiska wirtualne, potrzebujemy osobnych srodowisk dla kazdego projektu

###W sciesce katalogu wpisujemy py -m venv C:\Users\Krzysztof Belewicz\Documents\Kasia\Py4Beginners\Warsztat5\wirtualka
#py pip install requests
#pip freeze #patrzymy co mamy zainstaowane

#requests http for Humans #przeczytac
#GET - tylko pobieranie danych
#POST - wylij
#PUT- podmień
#PATCH -
#DELETE - usuń

#Payload - to co wysylamy, w corpo w xml odchodzi sie do json

#opis standardu  robotstxt.org 
#user-agent: *  # ma pozwolic na dostep, np system operacyjny, wersje przegladarki jakiej uzywamy
#disallow: #ustala gdze nie mamy wchodzic

#api nbp
#r = request...
#request zwraca odpowiedz

url = '...'
r = requests.get(url=url)
print(r)

#wyswietli Response [200] #to dobrze znaczy ze strona istnieje i sie udalo
#tutaj nie mozemy uzyc utf8 albo jednak mozemy ale nie wszedzie tak jest xd

#settery i gettery -> jak napiszmy property to python nam sam stworzy
#content 'b' - to byte #bajty to są bajty to co pozniej bedzie zinterpretowane do utf8
#json zostanie zinterpretowany do pythonowych struktur / typow

#pprint - fajniejszy print

for x in r.json():
    print('type(x)', type(x))
    print(x)
    print(80*'-')

#typ to bedzie dict
#dostaniemy wiele obiektow w roznych dat
#pamietac o obsludze wyjatkow przy obsludze request
#na troszke inny url niz na githubie
