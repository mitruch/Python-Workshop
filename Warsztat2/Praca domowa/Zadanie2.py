def copy_reversed(list_a, list_b):
    for x in reversed(list_a):
        list_b.append(x)
    

##test

# x = [1, 2, 3]
# y = [4, 5, 6]

# result = copy_reversed(x, y)

# print(x)
# print(y)

# assert y == [4, 5, 6, 3, 2, 1]
# assert result is None
