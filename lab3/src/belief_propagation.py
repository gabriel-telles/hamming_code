from math import inf
import numpy as np

class BeliefPropagation:
    def __init__(self, ldpc_matrix):
        self.ldpc_matrix = ldpc_matrix
        
    def decode(self, channel_llr, max_iter=10):
        self.nodes_llr = np.zeros_like(self.ldpc_matrix)
        self.channel_llr_matrix = np.tile(channel_llr, (self.ldpc_matrix.shape[0], 1))
        iterations_counter = 1
        while True:            
            self.__transmit_v_nodes_messages()
            if iterations_counter == max_iter or self.__check_parity():
                return self.__decide_bits()
            self.__transmit_c_nodes_messages()
            iterations_counter += 1
        
    def __transmit_v_nodes_messages(self):
        sum_cols = np.tile(self.nodes_llr.sum(axis=0), (self.nodes_llr.shape[0], 1))
        self.nodes_llr = (sum_cols - self.nodes_llr + self.channel_llr_matrix) * self.ldpc_matrix

    def __transmit_c_nodes_messages(self):
        nodes_llr_aux = np.zeros_like(self.nodes_llr)
        for i in range(self.nodes_llr.shape[0]):
            row = self.nodes_llr[i]
            for j in range(len(row)):
                if self.ldpc_matrix[i][j] != 0:
                    row_except_j = np.delete(row, j)
                    row_except_j_and_zero = row_except_j[row_except_j != 0]
                    min_module = np.min(np.abs(row_except_j_and_zero))
                    sign_product = np.prod(np.sign(row_except_j_and_zero))
                    nodes_llr_aux[i][j] = min_module * sign_product
        self.nodes_llr = nodes_llr_aux
                
    def __check_parity(self):
        for i in range(self.nodes_llr.shape[0]):
            row = self.nodes_llr[i]
            index_mask = (self.ldpc_matrix[i] != 0)
            row_except_zero = row[index_mask]
            sign_product = np.prod(np.sign(row_except_zero))
            if sign_product < 0:
                return False    
        return True
                
    def __decide_bits(self):
        sum_cols = self.nodes_llr.sum(axis=0)
        Lf = sum_cols + self.channel_llr_matrix[0]
        Lf[Lf > 0] = 0
        Lf[Lf < 0] = 1 
        return Lf # bits
                
                
            
        
        


