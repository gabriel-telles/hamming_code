import numpy as np

class HammingDecoder():
    def __init__(self, parity_matrix):
        self.__parity_matrix = parity_matrix
        self.__error_pattern_dict = HammingDecoder.error_pattern(self.__parity_matrix)
    
    def decode(self, message):
        """
        Decodes the message by summing (modulo 2) the message with the error associated with the syndrome.
        The syndrome is obtained by the matricial product (modulo 2) of message (r = v + e) with the parity_matrix (H),
        where v is the code-word and e is the error.
        """
        matrix = np.remainder(message @ self.__parity_matrix, 2)
        s = np.asarray(matrix).reshape(-1) # syndrome
        e = self.__error_pattern_dict[str(s)] # error
        return message ^ e
    
    @staticmethod
    def error_pattern(parity_matrix):
        """
        Determines the error pattern dict, which maps each syndrome (s) 
        to its error (e) with the lowest Hamming weight.
        """
        N = parity_matrix.shape[0]
        error_pattern_dict = {}
        error_pattern_dict[str(np.array([0, 0, 0]))] = np.zeros(N).astype(int)
        for i in range(N):
            e = np.zeros(N)
            e[i] = 1
            s = np.asarray(np.remainder((e @ parity_matrix), 2)).reshape(-1).astype(int)
            error_pattern_dict[str(s)] = e.astype(int)
        return error_pattern_dict