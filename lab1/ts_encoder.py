import numpy as np
from utils import *

class TSEncoder():
    def __init__(self):
        pass
    
    def encode(self, information_bits):
        decimal = binary_to_decimal(information_bits)
        mod7 = decimal % 7
        mod31 = decimal % 31

        binary_mod7 = np.array([int(bit) for bit in np.binary_repr(mod7, width=3)])
        binary_mod31 = np.array([int(bit) for bit in np.binary_repr(mod31, width=5)])

        return np.concatenate((information_bits, binary_mod7, binary_mod31))

