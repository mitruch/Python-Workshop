def power(n, p=2):
    result = 1
    if n>=0 and p>=0:
        for i in range(p):
            result *= n
        return result

# print(power(5))
# assert power(5) == 25
# assert power(5, 3) == 125