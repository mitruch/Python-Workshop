def factorial(n):
    if n == 0:
        return 1
    elif n > 0 :
        return n*factorial(n-1) 

# assert factorial(5) == 120
# print(factorial(1))