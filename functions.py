# Written by Ben Pearson
# V0.0.1
# This file will hold the primary functions to be used in the program

# Modules
import numpy as np

# Newton's method
# function
def fx(x):
    return ( 3 * (1 - np.exp(-x)) - x )
# derivative
def dfx(x):
    return ( 3 * np.exp(-x) - 1 )
# implement method
def newton(func, dfunc, x):
    return (x - func(x)/dfunc(x))

# Functional Iteration
def gx(x):
    return ( 3 * (1 - np.exp(-x)))
# implement method
def func_itor(func, x):
    return func(x)
