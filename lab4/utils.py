import numpy as np

def binary_to_decimal(bits):
    N = len(bits)
    sum = 0
    for i in range(N):
        if bits[N-i-1] == 1:
            sum += (1 << (i))
    return sum