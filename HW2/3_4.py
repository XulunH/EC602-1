import numpy as np

def largest_double():
    return np.finfo(np.float64).max

largest_double_precision = largest_double()

print(f"Largest double-precision number (not infinity): {largest_double_precision}")


def smallest_double():
    return np.finfo(np.float64).tiny


smallest_double_precision = smallest_double()

print(f"Smallest double-precision number greater than zero: {smallest_double_precision}")



def largest_single():
    return np.finfo(np.float32).max


largest_single_precision = largest_single()

print(f"Largest possible single-precision number (not infinity): {largest_single_precision}")



import numpy as np

def smallest_single():
    return np.finfo(np.float32).tiny

smallest_single_precision = smallest_single()

print(f"Smallest single-precision number greater than zero: {smallest_single_precision}")