class Vector():
    def __init__(self, *args):
        self.coords = list(args)
    
    def __len__(self):
        return len(self.coords)

    def __repr__(self): 
        temp = '{}({})'
        name = self.__class__.__name__
        args = ', '.join(repr(x) for x in self.coords) 
        return temp.format(name, args)     
    
    def __add__(self, other):
        tmp = []
        for i in range(len(self)):
            tmp.append(self[i] + other[i])
        return Vector(*tmp)    

    def __iadd__(self, other):
        for i in range(len(self)):
            self[i] += other[i]   
        return self

    def __radd__(self, other):
        tmp = []
        for i in range(len(self)):
            tmp.append(other[i] + self[i])   
        return Vector(*tmp)

    def __eq__(self, other):
        for i in range(len(self)):
            if not self[i] == other[i]:
                return False
        return True 

    def __getitem__(self, key):
        return self.coords[key]

    def __setitem__(self, key, value):
        self.coords[key] = value




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
assert [4, 6, 8, 10, 12] == dumped

# Dzięki temu możemy w funkcjach "magicznych" pozbyć się odwołań do implementacji vectora.
# Odwołania do other.coords są już niepotrzebne i większość self.coords też.
# Należy je zastąpić czymś innym - to już wasze zadanie wymyślić i zaprogramować.
# Chcemy zapewnić sobie możliwość "duck typing".

looks_like_vector = [0, 1, 2, 3]
v3 = Vector(3, 2, 1, 0)
v4 = v3 + looks_like_vector
v5 = looks_like_vector + v3
assert v4 == v5
assert isinstance(v4, Vector)
assert isinstance(v5, Vector)
assert 'Vector(3, 3, 3, 3)' == str(v4)

v6 = Vector(0, 1, 2, 3)
assert v6 == looks_like_vector
assert looks_like_vector == v6

    
