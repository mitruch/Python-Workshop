numbers = [x for x in range (1000)]
for x in numbers :
    if x%3 == 0 and x%5 == 0 :
        numbers[x] = "trzypięć"
    elif x%3 == 0 :
        numbers[x] = "trzy"
    elif x%5 == 0 :
        numbers[x] = "pięć"
result = numbers

assert result[15] == "trzypięć"
print(result)