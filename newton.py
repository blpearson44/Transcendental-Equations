# Written by Ben Pearson
# V0.0.1

"""
This module contains newton's methods
"""
# import modules
import constants as c


def newton_method(func, d_func, var):
    """Run newton's method on the function func with a starting value of var"""
    return var - func(var) / d_func(var)


def itor(func, d_func, var):
    """Run newton's method on the function func with a starting value of x c.N times"""
    arr = [var]
    for i in range(c.N):
        var = newton_method(func, d_func, var)
        arr.append(var)
    return arr
