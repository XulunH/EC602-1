import numpy as np
import struct

def construct_float(float_parms, *, float_type=np.float64, subnormal=False):
    """
    Construct a floating-point number from a dictionary of sign, exponent, and fraction.

    Args:
        float_parms (dict): Dictionary containing 'sign', 'exponent', and 'fraction' as integers.
        float_type (type, optional): The desired floating-point type (default is np.float64).
        subnormal (bool, optional): If True, create a subnormal float (default is False).

    Returns:
        The constructed floating-point number of the specified type.

    Raises:
        ValueError: If it's not possible to create a valid floating-point number.
    """
    # Define the bit-width for the chosen float_type
    if float_type == np.float16:
        total_bits = 16
        exponent_bits = 5
        fraction_bits = 10
    elif float_type == np.float32:
        total_bits = 32
        exponent_bits = 8
        fraction_bits = 23
    elif float_type == np.float64:
        total_bits = 64
        exponent_bits = 11
        fraction_bits = 52
    elif float_type == np.float128:
        total_bits = 128
        exponent_bits = 15
        fraction_bits = 112
    else:
        raise ValueError("Unsupported float_type. Choose from np.float16, np.float32, np.float64, or np.float128.")

    # Check if the provided float parameters are within the valid range
    if not (0 <= float_parms['sign'] <= 1 and 0 <= float_parms['exponent'] < 2**exponent_bits and 0 <= float_parms['fraction'] < 2**fraction_bits):
        raise ValueError("Invalid float parameters.")

    # Construct the binary representation
    sign_bit = float_parms['sign'] << (total_bits - 1)
    exponent_bit = float_parms['exponent'] << fraction_bits
    fraction_bit = float_parms['fraction']

    # Combine the bit parts
    binary_representation = sign_bit | exponent_bit | fraction_bit

    # Check if subnormal numbers are allowed
    if subnormal:
        binary_representation &= (2**total_bits - 1)

    # Pack the binary representation into bytes and unpack as a float
    byte_format = f"{total_bits//8}s"
    float_bytes = struct.pack(byte_format, int(binary_representation).to_bytes(total_bits//8, byteorder='big'))
    constructed_float = struct.unpack(float_type.__format__, float_bytes)[0]

    return constructed_float

# Example usage:
float_parms = {'sign': 0, 'exponent': 1023, 'fraction': 0}
result = construct_float(float_parms, float_type=np.float64)
print(result)
