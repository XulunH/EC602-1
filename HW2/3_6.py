import numpy

def construct_float(float_parms, *, float_type=numpy.float64, subnormal=False):
    if subnormal:
        if float_type == numpy.float16:
            if float_params["exponent"] == 0 and 0<=float_params["fraction"]<=511:
                a = float_params["fraction"]
                return a*(2**(-10))
            else:
                print("ValueError")
                return None
        elif float_type == numpy.float32:
            if float_params["exponent"] == 0 and 0<=float_params["fraction"]<=8388607:
                a = float_params["fraction"]
                return a*(2**(-23))
            else:
                print("ValueError")
                return None
        elif float_type == numpy.float64:
            if float_params["exponent"] == 2046 and 0<=float_params["fraction"]<= 4503599627370495:
                a = float_params["fraction"]
                return a*(2**(-52))
            else:
                print("ValueError")
                return None
        else:
                print("ValueError")
                return None
    else:
              
        if float_type == numpy.float16:
            if 0 < float_params["exponent"] <= 30 and 0<=float_params["fraction"]<=511:
                return make_16(float_parms)
            elif float_params["exponent"] == 31:
                print("infinite")
                return None
            else:
                print("ValueError")
                return None
        elif float_type == numpy.float32:
            if 0 < float_params["exponent"] <= 254 and 0<=float_params["fraction"]<= 8388607:
                return make_32(float_parms)
            elif float_params["exponent"] == 255:
                print("infinite")
                return None
            else:
                print("ValueError")
                return None
        elif float_type == numpy.float64:
            if 0 < float_params["exponent"] <= 2046 and 0<=float_params["fraction"]<= 4503599627370495:
                return make_64(float_parms)
            elif float_params["exponent"] == 2047:
                print("infinite")
                return None
            else:
                print("ValueError")
                return None
        else:
                print("ValueError")
                return None

def make_16(i):
    man = i["fraction"]
    exp = i["exponent"]
    unsign_value = 2**(exp-15)*(man*(2**(-10))+1)
    if i["sign"]:
        value = unsign_value * (-1)
    else:
        value = unsign_value
    return value

def make_32(i):
    man = i["fraction"]
    exp = i["exponent"]
    unsign_value = 2**(exp-127)*(man*(2**(-23))+1)
    if i["sign"]:
        value = unsign_value * (-1)
    else:
        value = unsign_value
    return value

def make_64(i):
    man = i["fraction"]
    exp = i["exponent"]
    unsign_value = 2**(exp-1023)*(man*(2**(-52))+1)
    if i["sign"]:
        value = unsign_value * (-1)
    else:
        value = unsign_value
    return value
    

float_params = {"sign": 0, "exponent": 1024, "fraction": 1125899906842624}
my_float = construct_float(float_params, float_type=numpy.float64, subnormal=False)
print(my_float)

