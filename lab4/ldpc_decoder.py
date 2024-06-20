import numpy as np

class LdpcDecoder():
    def __init__(self, parity_matrix):
        self.__parity_matrix = parity_matrix
        self.__Ht = parity_matrix.T
    
    def decode(self, bits, iterations=100): 
        for it in range(iterations):
            e = np.remainder(bits @ self.__Ht, 2)
            error_counter = np.array([0]*len(bits)).astype(int)
            for i in range(len(e)):
                if e[i] == 1:
                    error_counter += self.__parity_matrix[i]
            greater_error_index = np.argmax(error_counter)
            if error_counter[greater_error_index] == 0:
                break
            bits[greater_error_index] = (bits[greater_error_index] + 1) % 2
        return bits