import numpy as np

class TSEncoder():
    def __init__(self):
        pass
    
    def encode(self, information_bits):
        N = len(information_bits)
        sum = 0
        for i in range(N):
            if information_bits[N-i-1] == 1:
                sum += (1 << (i))
        mod7 = sum % 7
        mod31 = sum % 31

        binary_mod7 = np.array([int(bit) for bit in np.binary_repr(mod7)])
        binary_mod31 = np.array([int(bit) for bit in np.binary_repr(mod31)])

        return np.concatenate((information_bits, binary_mod7, binary_mod31))

