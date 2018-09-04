numbers = [[x] for x in range(100) if x%2 == 0]
result = numbers

assert result[1] == [2]
print(result)