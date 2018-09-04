from collections import Counter #pomaga zliczac wystepowania w slowniku i n wystepujcych

with open('pan_tadeusz.txt') as file:
    counter = Counter()
    for line in file:
        words = line.split() #domyslnie splituje po bialych znakach
        counter.update(words)

print(counter.most_common(10)) #powyzej? 
