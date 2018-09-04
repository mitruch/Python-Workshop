A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
result = set()
for i in range(2**len(A)):
    subset = frozenset([x for j,x in enumerate(A) if (i >> j) & 1])
    result.add(subset)

assert frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) in result
print(result)