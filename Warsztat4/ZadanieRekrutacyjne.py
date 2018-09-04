import csv #to nam ulatwia zycie, rozdzielanie pol itp #normalnie kazdy by z tego skorzystal

with open('conferences_data.csv') as csv_file:
    d = {} #pusty slownik(
    reader = csv.reader(csv_file, delimiter=';') #mowimy mu w jaki sposob rozdzielane sa pola
    next(reader) #jakis iterator pomijamy pierwsza linijke, naglowki w pliku
    for row in reader:
        print(row)
        for conf, email in enumerate(row): #z enumerate dostajemy index i wartosc #email uczestnika danej konferencji z kolumny 
            if not email:
                continue; #zeby nie tworzyc klucza z pustym mailem bo mamy roznej dlugosci linie
            try:
                conferences = d[email]
            except KeyError:
                conferences = set()
                d[email] = conferences
            conferences.add(conf) #dodajemy konfe do listy konferencji dla danego maila


# print(d)         
# print('' in d)        #stworzyl sie na poczatku pusty email, bo mamy roznej dlugosci linie

## Odpowiedzi na pytania

#Pytanie1

result1 = len([email for email in d if len(d[email]) > 1]) #ludzie ktorzy byli na wiecej niz jednej konferencji
print(result1)

##Pytanie2

def get_company(email):
    login, rest = email.split('@') #split rozdziela nam to co trafi do login i rest
    company, country = rest.split('.')
    return company
    #  _, rest = email.split('@') #split rozdziela nam to co trafi do login i rest
    # company, _ = rest.split('.') #taka konwencja, jesli cos nas nie interere to przypisujemy temu _ (podloge)

result2 = len([
    email for email in d
    if get_company(email) == 'wok'])
print(result2)


#Pytanie3
def get_country(email):
    _, rest = email.split('@') #split rozdziela nam to co trafi do login i rest
    _, country = rest.split('.')
    return country

result3 = len({get_country(email) for email in d})
print(result3)

   