numbers = []
for x in range(1,101) :
    n = [z for z in range(1,101)]
    n.append(sum(y for y in n if y<=x))
    numbers.append(n)
result = numbers

assert result[-1][-1] == 5050
print(result)