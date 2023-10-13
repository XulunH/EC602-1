import numpy as np

def largest_double():
    ## this number is 0|111...11110|1111...
    ##so the number is:
    
    largest_finite_double = 2**1023 * (2-2**(-52))

    return largest_finite_double


largest_double_precision = largest_double()
print(f"Largest double-precision number (not infinity): {largest_double_precision}")

def smallest_double():
    ## since subnormal is always smaller, they smallest will happen in them
    ##so the number is:
    ## minimum normal exponent is -1022  as when 0000...1
    ## The smallest positive subnormal number has a 1 in its lowest bit and zeros in all other bits
    smallest_finite_double = 2**(-1022) * 2**(-52)

    return smallest_finite_double


smallest_double_precision = smallest_double()
print(f"the smallest double-precision number greater than zero: {smallest_double_precision}")

def largest_single():
    ## this number is 0|11111110|1111...(23 of them) we dont' want infinite
    ##so the number is:
    result = (2 - 2**(-23)) * 2**127

    return result

largest_single_precision = largest_single()
print(f"Largest double-precision number (not infinity): {largest_single_precision}")



def smallest_single():
    ## since subnormal is always smaller, they smallest will happen in them
    ##so the number is:
    ## minimum normal exponent is -126  as when 0000...1
    ## The smallest positive subnormal number has a 1 in its lowest bit and zeros in all other bits
    smallest_finite_single = 2**(-126) * 2**(-23)

    return smallest_finite_single


smallest_single_precision = smallest_single()
print(f"the smallest single-precision number greater than zero: {smallest_single_precision}")