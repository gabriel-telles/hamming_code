import numpy as np

class HammingEncoder():
    def __init__(self, generating_matrix):
        self.__generating_matrix = generating_matrix
    
    def encode(self, information_bits):
        matrix = np.remainder(information_bits @ self.__generating_matrix, 2)
        return np.asarray(matrix).reshape(-1)