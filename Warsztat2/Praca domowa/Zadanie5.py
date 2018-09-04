def function_results_sum(*args, **kwargs):
    s = 0
    for fun in args:
        if (fun.__name__ not in kwargs.keys()):
            s += fun()
        elif type(kwargs[fun.__name__]) == type(()):  #instance(arg, int) sprawdza typ
            s += fun(*kwargs[fun.__name__])
        else :
            s += fun(kwargs[fun.__name__])
    return s

##test

# def no_arg():
#     return 5

# def ident(x):
#     return x

# def mult(x, y):
#     return x * y

# assert function_results_sum(no_arg, ident, mult, ident=2, mult=(3, 4)) == 19  