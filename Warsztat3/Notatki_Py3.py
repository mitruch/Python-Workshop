#definicja klasy też jest obiektem
#mro hardcore nie trzeba ruszac


#nie ma polimorfizmu metod takiego jak w C++ :(

#kompilacja pythona robi sie w locie, load global / load local przed i po inicjalizacji zmiennej

#Python jest kompilowany do byte kodu
#LEGB - Local Enclosing Global Building (szukanie zmiennych)
#dis

class MyClass(): #tworzy obiekt class
    pass

#do atrybutu przez kropke niezaleznie czy funkcja czy pole
#instancjonowanie

pierwszy = MyClass()
print(type(pierwszy))

#w Pythonie jest tylko jeden konstruktor new, ale raczej sie go nie dotyka
#bo mamy init inicjalizator, który inicjalizuje nam obiekt

class Person():
    def __init__(self, name, surname):  #self to nie jest nazwa predefiniowana, ale taka jest konwencja i pierwszy argument to self
        self.name = name
        self.surname = surname

    def formalize(self):
        return "Imie: {} Nazwisko: {} ".format(self.name, self.surname)

    @classmethod #wymagane to jest dekorator, inaczej nie bedzie to metoda klasy
    def from_string(cls, name, surname):
        return cls(name, surname)
    #czyli tak naprawde alternatywny konstruktor


janek = Person("Jan", "Kos")
#self to takie this, na to trafia instancja naszej klasy

#singleton jakby dwie instancje były tymi samymi obiektami, ale gardzimy tym
#None jest singletonem

#instancje mogą współdzielic obszar pamięci, to co zdefiniujemy na klasie zostanie na klasie to co na instancji na inctancji

class Surprise():
    a = 44
    b = []  #atrybuty klasy
    def __init__ (self, name):
        self.name = name #atrybut instancji klasy

sup1 = Surprise("Pierwsza")
sup2 = Surprise("Druga")

def print_surprise():
    print(Surprise, Surprise.a, Surprise.b) 
    print(sup1, sup1.a, sup1.b, sup1.name)
    print(sup2, sup2.a, sup2.b, sup2.name)

sup1.a = 23
print_surprise()

Surprise.a = 55

sup2.b.append("Całkiem blablab") #poleciało do wszystkich i instancji klasy i obiektu

#najpierw szukamy atrybutu w insancji a pozniej w klasie

print_surprise()

#współdzielenie stanu miedzy isntancjami to kiepski pomysl
#kontrole dostepu czyli public, private itp
# w pythonie wszystko jest PUBLIC 
# nie ma opcji zeby zablokowac odstep albo nie moc sie do czegos dostac

# jezeli uzyjemy _nazwazmiennej to wg konwencji programista uwaza ze ten atrybut mial byc prywatny
# Pseudoprywatnosc __ (dwa podkreslniki) sa jakby bardziej prywatne i kompilator dokleja na poczatku nazwe klasy
# Dalej mozna sie do tego dostac, ale programista ostrzega ze nie powinienes

# Na stringu mozemy wywolac .format wstawia w {} podane w funkcji argumenty w stringu

# wszystkie nazwy typu dwa podkreslniki __cos__ sa zarezerwowane dla Pythona, nie uzywac !

# atrybuty klasy są współdzielone a atrybuty instancji nie

# Atrybuty instancji definiujemy w init
# Atrybuty klasy definiujemy w klasie po protstu

#@bleble #to jest dekorator #class method

####Dziedziczenie w Pythonie
## Wszystko dzidziczy po Object

class A():
    pass

class B(A): #klasa B dziedziczy po A
    pass

a = A()
b = B()

print(isinstance(b, B))
issubclass(B, A)
issubclass(A, B)

# MRO # Problem diamentowy #Dziedziczenie wielokrotne jest dostepne

#Metody klasy bazowej mozna nadpisywac

# Wywolywanie metod klasy bazowej

# super() wola nasza baze
# mozna przypisac baza = super() i wywolywac w metodach klasy dziedziczacej

# Metody "Magiczne"
# len(o) wola tak naprawde o.__len_

#Tworzymy klase Vector

# class Vector(list):               #tak nie robimy
#     def __init__(self, *args):
#         super.__init__()
#         self.coords = list(args)



class Vector():
    def __init__(self, *args):
        print(args)
        self.coords = list(args)

    # kolejnosc definicji i w jakiej kolejnosci je pozniej wywolujemy nie ma znaczenia    
    
    def __len__(self): # te metody mają zdefiniowaną liste argumentow nie powinnismy w tym grzebac
        return len(self.coords)

    def __repr__(self): # wypisanie w takiej formie jakbysmy tworzyli obiekt
        temp = '{}({})'
        name = self.__class__.__name__
        args = ', '.join(repr(x) for x in self.coords) 
        # print(name, args)
        return temp.format(name, args)

    # def __add__(self, other):
    #     tmp = []
    #     for i in range(len(self)):
    #         tmp.append(self.coords[i] + other.coords[i])
    #     return Vector(*tmp)     
    
    # def __add__(self, other):
    #     tmp = []
    #     for i in range(len(self)):
    #         tmp.append(self[i] + other[i])
    #     return Vector(*tmp)

    def __add__(self, other):
        tmp = [x + y for x, y in zip(self, other)]
        return Vector(*tmp)        

    # def __iadd__(self, other):
    #     for i in range(len(self)):
    #         self.coords[i] += other.coords[i]   
    #     return self

    # def __iadd__(self, other):
    #     for i in range(len(self)):
    #         self[i] += other[i]   
    #     return self

    # zip() sklada nam listy w takie sekwencje, sklada do najkrotszego, zastosowanie
    # nie trzeba robic petli w petli jesli chcemy iterowac po 

    def __iadd__(self, other):
        for i in range(len(self)):
            self[i] += other[i]   
        return self

    # def __radd__(self, other):
    #     tmp = []
    #     for i in range(len(self)):
    #         tmp.append(other[i] + self[i])   
    #     return Vector(*tmp)
    
    def __radd__(self, other):
        return self + other

    # def __eq__(self, other):
    #     for i in range(len(self)):
    #         if not self.coords[i] == other.coords[i]:
    #             return False
    #     return True # Wielka litera

    def __eq__(self, other):
        for i in range(len(self)):
            if not self[i] == other[i]:
                return False
        return True # Wielka litera

    # def __rmnfkjnd__ mnozenie

    def __getitem__(self, key):
        return self.coords[key]

    def __setitem__(self, key, value):
        self.coords[key] = value

    def list(self):
        return list(self.coord)

    # Zrzucanie do stringa __repr__
    # __str__ str(o) szuka tez czy jest zdef __repr__ zrzuca do stringa tak zeby to bylo czytelne dla czlowieka
    # __repr__ repr(o) powinien zrzucac do stringa tak zebysmy go mogli zrzucic na jakis obiekt
    # jak wywolujemy print(o) to print szuka na obiekcie o __str__ a jezeli nie ma to szuka __repr__
    

Vector(5)
Vector(1, 2, 3)

print(len(Vector(2,3)))
print(repr(Vector(1, 2, 3)))

v1 = Vector(1, 2)
v2 = Vector(2, 3)
v3 = v1 + v2

print(v3)

v1 += v2 #jezeli nie zaimplementujemy to 

print(v1)

v4 = Vector(1, 2, 3, 4, 5)
v5 = Vector(1, 2, 3, 4, 5)

print(v5 == v4)
print(v5 is v4)




# Chcemy mieć możliwość uzyskania wartości konkretnej współrzędnej po indeksie

v = Vector(1, 2, 3, 4)
assert 1 == v[0]
assert 2 == v[1]
assert 3 == v[2]
assert 4 == v[3]

assert 4 == v[-1]

# Chcemy mieć możliwość ustawienia wartości konkretnej współrzędnej

v1 = Vector(3, 4, 8)
v1[2] = 5
assert 'Vector(3, 4, 5)' == str(v1)

# Jeżeli powyższe dwa polecenia zostały wykonane "sprytnie" to powinniśmy
# mieć teraz możliwość iterowania po współrzędnych wektora

v2 = Vector(4, 6, 8, 10, 12)
dumped = [x for x in v2]
print(dumped)
assert [4, 6, 8, 10, 12] == dumped

looks_like_vector = [0, 1, 2, 3]
v3 = Vector(3, 2, 1, 0)
v4 = v3 + looks_like_vector
print(v4)
v5 = looks_like_vector + v3
print(v5)
print(type(v5))
assert v4 == v5
assert isinstance(v4, Vector)
assert isinstance(v5, Vector)
assert 'Vector(3, 3, 3, 3)' == str(v4)

v6 = Vector(0, 1, 2, 3)
print(type(v6))
print(v6)
print(looks_like_vector)
assert v6 == looks_like_vector
assert looks_like_vector == v6