# Copyright 2023 Jinzhi Shen jinzhis9@bu.edu

#### the reason why becoming zero is not happening in the second case is because of the difference
#### between numpy arrays and a numpy scalar: the numpy array when it it ahandling overflow, it will
#### change back to the smallest number while the scalar will sometimes ectends its own bits and creating a rextremly long 
#### number array.
import numpy
import time
def estimate_wrap_around():

    m = numpy.array([1], dtype=numpy.int16)
    start_time = time.perf_counter()
    while m[0] >0:
        m[0] += 1
        ##print(m[0])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time ## unit in second

    elapsed_time_8 = elapsed_time/(2**15 -1) * (2**7 - 1) * (10**9)
    print(f"estimated 8-bit time (nanoseconds): {elapsed_time_8}")

    elapsed_time_16 = (end_time - start_time) * 1e6
    print(f"measured 16-bit time (microseconds): {elapsed_time_16}")

    elapsed_time_32 = elapsed_time/(2**15 -1) * (2**31 - 1) 
    print(f"estimated 32-bit time (seconds): {elapsed_time_32}")

    elapsed_time_64 = elapsed_time/(2**15 -1) * (2**63 - 1) /(3600*24*365)
    print(f"estimated 64-bit time (years): {elapsed_time_64}")

estimate_wrap_around()