import numpy as np

class HammingEncoder():
    def __init__(self, generating_matrix):
        self.__generating_matrix = generating_matrix
    
    def encode(self, information_bits):
        """
        Encodes the information_bits by doing the matricial product (modulo 2) 
        with the generating_matrix (G).
        """
        matrix = np.remainder(information_bits @ self.__generating_matrix, 2)
        return np.asarray(matrix).reshape(-1)