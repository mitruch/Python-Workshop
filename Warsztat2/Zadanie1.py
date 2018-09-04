#Warsztat2

#Zadanie 1
# for i in range(3) :
#     print((3-i-1)*" " + (2*i+1)* "*")


#Zadanie2
# def drawTree() :
#     for i in range(3) :
#         print((3-i-1)*" " + (2*i+1)* "*")

# for i in range(3) :
#     drawTree()

## Zadanie3
# def drawTree(n) :
#     for i in range(n) :
#         print((n-i-1)*" " + (2*i+1)* "*")

# for i in range(3) :
#     drawTree(i+3)

## Zadanie4
# def drawTree(n, x) :
#     for i in range(n) :
#         print((n-i-1)*" " + (2*i+1)* x)

# for i in range(3) :
#     drawTree(i+3, "#")

## Zadanie5
# domyslne argumenty
# def drawTree(n=3, x="*") :
#     for i in range(n) :
#         print((n-i-1)*" " + (2*i+1)* str(x))

# for i in range(3) :
#     drawTree(i+3, "*")

# Zadanie6
# return - zwracanie jednej wartosci
# def drawTree(n=3, x="*") :
#     symbols_count = 0
#     for i in range(n) :
#         symbols_count+=(2*i+1)
#         print((n-i-1)*" " + (2*i+1)* str(x))
#     return symbols_count

# symbols = drawTree(3, "*")
# print("Symbols count = ", symbols)


# # Zadanie7
# # Przyjmowanie dowolnej liczby argumentow do funckji
# # * - zbiera wszystkie argumenty pozycyjne (tupla)

# def sum_numbers(*numbers):
#     result = 0
#     for x in numbers:
#         result += x
#     return result
    
# sum = sum_numbers(1, 2, 3, 4, 5, 6, 7)    
# print(sum)


# Zadanie8
# ** - dowolna ilosc argumentow nazwanych (slownik - dict, klucze to stringi)
# def print_kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print(k)
#         print(v)

# print_kwargs(k=1, w=2, e=3)    

# Zadanie9
# * - zbiera wszystkie argumenty pozycyjne (tupla)
# ** - dowolna ilosc argumentow nazwanych (slownik - dict, klucze to stringi)
# Kolejnosc podawania argumentów pozycyjne, pozniej domyslne, pozniej *, pozniej **

# def sum_numbers(*numbers, **kwargs):
#     result = 0
#     for x in numbers:
#         result += x
#     for k, v in kwargs.items():
#         print(k)
#         print(v)
#     return result

# result = sum_numbers(1, 2, 3, z=1, y=2) 
# print("Suma = ", result)


# Funkcja to obiekt
# Są hashowalne moga byc w slownku //
# def func():
#     """
#     Zajebista Funkcja
#     """
#     print("Funkcja")


# print(func)
# func.y = 1
# print(func.y)
# print(hash(func))

# d = {
#     func: 'ss'
# }

# print(d[func])

# # print(func._doc_) #jak wypisac tego doca? :D


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) #...


 ## IMPORT       


#Modyfikowanie listy
# lista_slow = ['blala', 'jajaj', 'huhu']

# def my_func1(a):
#     a.append("kkkk")
#     for i in a:
#         print(i)

# def my_func2(a):
#     a = ["zzzz", "iiiii"]
#     for i in a:
#         print(i)        

# my_func1(lista_slow)
# my_func2(lista_slow)
# print(lista_slow)

## Tworzac nowa liste w definicji funkcji, przy kazdym wywolaniu bedzie odnosic sie do tej samej listy

# #zle
# def print_words(words=[]): 

# #dobrze
# def print_words(words=None):
#     if words is None
#         words = []

## Return
## domyslna wartosc zwracana przez funkcje to None      


## IMPORT

## import calej zawartosci pliku

# import tree ## importujac wykonuje sie kod z tree
# tree.func()

## import konkretnej funkcji

# from tree import func ## importujac wykonuje sie kod z tree
# func()

# # >>>dir(tree)
#  _ _ name _ _ (podwojne podkreslniki)

# print(__name__)  #wyswietli main

# if _name_ == "main":


## PACKA
## _name_ ? #nie dziala

# from my_pkg.tree import func
# func
