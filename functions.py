# Written by Ben Pearson
# V0.1.1
# This file will hold the primary functions to be used in the program

# Modules
import numpy as np
import constants as c


# Newton's method
def fx(x):
    return ( 3 * (1 - np.exp(-x)) - x )

def dfx(x):
    return ( 3 * np.exp(-x) - 1 )

def newton_method(func, dfunc, x):
    return (x - func(x)/dfunc(x))


# Functional Iteration
def gx(x):
    return ( 3 * (1 - np.exp(-x)))
def functional_iteration(func, x):
    return func(x)

# Take function and iterate it c.N times 
def newton_itor(x):
    arr = [x]
    for i in range(c.N):
        x = newton_method(fx, dfx, x)
        arr.append(x)
    return arr

# Take function and iterate it c.N times 
def functional_itor(x):
    arr = [x]
    for i in range(c.N):
        x = functional_iteration(gx, x)
        arr.append(x)
    return arr
