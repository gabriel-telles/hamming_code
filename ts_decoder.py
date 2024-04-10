import numpy as np
from utils import *
from copy import deepcopy

class TSDecoder():
    def __init__(self):
        pass
    
    def check_valid(self, message):
        data = binary_to_decimal(message[0:9])
        mod7 = binary_to_decimal(message[9:12])
        mod31 = binary_to_decimal(message[12:])
        return (data % 7 == mod7) and (data % 31 == mod31)

    def flip_bit(self, message, i):
        flipped = deepcopy(message)
        if flipped[i] == 1:
            flipped[i] = 0
        elif flipped[i] == 0:
            flipped[i] = 1
        return flipped

    def decode(self, message):
        if self.check_valid(message):
            return message[0:9]
        
        candidates = [self.flip_bit(message, i) for i in range(len(message))]
        candidates = list(filter(self.check_valid, candidates))
        if len(candidates) == 0:
            return message[0:9]
        return candidates[0][0:9]
