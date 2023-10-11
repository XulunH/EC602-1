import numpy

def breakdown_float(f):
    # Constants for bit manipulation
    SIGN_MASK = 0x8000000000000000
    EXPONENT_MASK = 0x7FF0000000000000
    FRACTION_MASK = 0x000FFFFFFFFFFFFF

    # Extract the raw bits of the floating-point number
    raw_bits = f.tobytes()

    # Convert the raw bits to an integer
    raw_int = int.from_bytes(raw_bits, byteorder='big', signed=False)

    # Extract the sign bit, exponent, and fraction
    sign = 0 if (raw_int & SIGN_MASK) == 0 else 1
    exponent = (raw_int & EXPONENT_MASK) >> 52
    fraction = raw_int & FRACTION_MASK

    # Check if the number is in subnormal state
    subnormal = exponent == 0 and fraction != 0

    # Create a dictionary with the extracted values
    result = {
        'sign': sign,
        'exponent': exponent,
        'fraction': fraction,
        'subnormal': subnormal
    }

    return result

# Example usage
m = numpy.float64(2.5)
d = breakdown_float(m)
print(d)
