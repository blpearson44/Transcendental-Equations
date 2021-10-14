# Written by Ben Pearson
# V0.0.1

"""
This file contains the functional iteration methods
"""

# import modules
import constants as c


def functional_iteration(func, var):
    """Run functional iteration with a starting value of x on the function func"""
    return func(var)


# Take function and iterate it c.N times
def itor(func, var):
    """Run functional iteration with a starting value of x on the function func c.N times"""
    arr = [var]
    for i in range(c.N):
        var = functional_iteration(func, var)
        arr.append(var)
    return arr
