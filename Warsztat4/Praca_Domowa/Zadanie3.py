import csv
import random

def create_sets_of_question(capitals_csv, number_of_sets, number_of_questions_per_set):

    capitals_dic = {} 
    with open(capitals_csv, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';') 
        next(reader) 
        for row in reader: 
            capitals_dic[row[0]] = row[1] 
    
    if number_of_sets * number_of_questions_per_set > len(capitals_dic.keys()):
        raise ValueError
    
    used_country = set()
    for s in  range(number_of_sets):
        file_name = 'zestaw' + str(s+1) + '.csv'
        with open(file_name, 'w', encoding="utf8", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')   
            csv_file.write('Państwo;A;B;C;D\n') 
            i=0
            while i != number_of_questions_per_set:
                ctr = random.choice(list(capitals_dic.keys()))
                options = []
                if ctr not in used_country:              
                    i+=1
                    used_country.add(ctr)
                    good_answer = capitals_dic[ctr]
                    options.append(good_answer)
                    while len(options) != 4: #mozna tutaj random.sample ([co for skad, if warunek, ile])
                        answ = random.choice(list(capitals_dic.values()))
                        if answ not in options:
                            options.append(answ)
                    random.shuffle(options)
                    options.insert(0, ctr)
                    writer.writerow(options)
               


create_sets_of_question('stolice.csv', 4, 9)


with open('zestaw1.csv') as zestaw1:
    reader = csv.reader(zestaw1, delimiter=';')
    lines_count = 0
    for row in reader:
        print(row)
        assert len(row) == 5  # 5 kolumn - Państwo + propozycje odpowiedzi A, B, C, D
        lines_count += 1
    assert lines_count == 9  # 8 pytan + naglowek

try:
    create_sets_of_question('stolice.csv', 4, 9)
except ValueError:
    print('Błąd wyrzucony tak jak trzeba')
else:
    print('Bez błędu, a trzeba było :(')