import numpy as np

class HammingDecoder():
    def __init__(self, parity_matrix):
        self.__parity_matrix = parity_matrix
        self.__error_pattern_dict = HammingDecoder.error_pattern(self.__parity_matrix)
    
    def decode(self, message):
        matrix = np.remainder(message @ self.__parity_matrix, 2)
        s = np.asarray(matrix).reshape(-1) #syndrome
        e = self.__error_pattern_dict[str(s)]
        return message ^ e
    
    @staticmethod
    def error_pattern(parity_matrix):
        N = parity_matrix.shape[0]
        error_pattern_dict = {}
        error_pattern_dict[str(np.array([0, 0, 0]))] = np.zeros(N).astype(int)
        for i in range(N):
            e = np.zeros(N)
            e[i] = 1
            s = np.asarray(np.remainder((e @ parity_matrix), 2)).reshape(-1).astype(int)
            error_pattern_dict[str(s)] = e.astype(int)
        return error_pattern_dict