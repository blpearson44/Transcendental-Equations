# Written by Ben Pearson
# V0.1.1

"""
This file will hold the primary functions to be used in the program
"""

# Modules
import numpy as np
import constants as c


# Newton's method

# Test function
def n_test(x):
    return 3 * (1 - np.exp(-x)) - x


def d_n_test(x):
    return 3 * np.exp(-x) - 1


# Even parity function
def n_even(x):
    return np.sqrt(c.K) * np.abs(np.cos(x)) - x


def d_n_even(x):
    return -np.sqrt(c.K) * np.cos(x) * np.sin(x) / np.abs(np.cos(x)) - 1


# Odd parity funciton
def n_odd(x):
    return np.sqrt(c.K) * np.abs(np.sin(x)) - x


def d_n_odd(x):
    return np.sqrt(c.K) * np.cos(x) * np.sin(x) / np.abs(np.sin(x)) - 1


# Functional Iteration

# Test function
def f_test(x):
    return 3 * (1 - np.exp(-x))


# Even parity function
def f_even(x):
    return np.arccos(x / np.sqrt(c.K))


# Odd parity function
def f_odd(x):
    return np.arctan(-x / np.sqrt(c.K - x ** 2))
