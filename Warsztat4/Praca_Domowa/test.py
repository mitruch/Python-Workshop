import csv

def check_homework(capitals_csv, questions_csv, answers_csv):
    capitals_dic = {} 
    with open(capitals_csv, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';') 
        next(reader) 
        for row in reader: 
            capitals_dic[row[0]] = row[1]       

    questions_dic = {}
    answ_dic = {}
    with open(questions_csv, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader) 
        for num, row in enumerate(reader):   
            questions_dic[num] = row[0]
            answ_dic[num] = row[1::]

    answer_list = []
    with open(answers_csv, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';') 
        next(reader) 
        for row in reader:   
            answer_list.append(row[0])  

    abc_dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3}        
    result = 0
    for num, answ  in enumerate(answer_list):
        options = answ_dic[num]
        alpha = abc_dic[answ]
        my_answer = options[alpha]
        good_answer = capitals_dic[questions_dic[num]]
        if  my_answer == good_answer :
            result += 1

    return result