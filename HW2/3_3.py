import numpy as np

def maximum_consecutive_int_value(float_type):
    epsilon = np.finfo(float_type).eps
 ##   print(epsilon)  
    if epsilon == np.finfo(np.float16).eps:
        return 2**11 - 1
    elif epsilon == np.finfo(np.float32).eps:
        return 2**24 -1
    elif epsilon == np.finfo(np.float64).eps:
        return 2**53 -1


##32 1.1920929e-07
##64 2.220446049250313e-16
##128   
float_type_16 = np.float16
result = maximum_consecutive_int_value(float_type_16)
print(f"Maximum consecutive integer for {float_type_16} is {result}")


