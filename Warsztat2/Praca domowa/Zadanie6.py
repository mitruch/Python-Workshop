def ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia):
    result = []
    result.append(0)
    time = tempo_schodzenia
    list_end = len(lista_osob)-1
    start = list_end
    while lista_osob[start] == 0: #empty upstairs
        start -= 1
        result.append(0)                     
    for i in range(start, 0, -1):
        x = lista_osob[i]
        while x > 0:
            x -= (liczba_klatek_schodowych * liczba_osob_w_rzedzie)
            time += 1 
        result.insert(0, time)
        time += tempo_schodzenia
    # print(result)
    return result

##test

# lista_osob = [5, 10, 0]
# liczba_klatek_schodowych = 2
# liczba_osob_w_rzedzie = 1
# tempo_schodzenia = 30

# assert [73, 38, 0] == ewakuacja(
#     lista_osob=lista_osob,
#     liczba_klatek_schodowych=liczba_klatek_schodowych,
#     liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
#     tempo_schodzenia=tempo_schodzenia
# )