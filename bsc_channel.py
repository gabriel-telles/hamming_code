import numpy as np

class BSCChannel():
    def __init__(self, p):
        self.__p = p
    
    def change_bits(self, bits):
        bit_error_probas = np.array([np.random.uniform(0, 1) for _ in range(len(bits))])
        will_change = np.array([x <= self.__p for x in bit_error_probas])
        return bits ^ will_change