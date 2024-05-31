from math import inf
import numpy as np

def generate_parity_matrix(dv, dc, N):
    M = N*dv/dc
    rows = int(M/dv)
    cols = N
    matrix = np.zeros((rows, cols)).astype(int)
    for j in range(cols):
        matrix[j//dc][j] = 1
    
    permutations = []
    for i in range(dv-1):
        permutation = np.random.permutation(matrix.T).T
        permutations.append(permutation)

    return np.concatenate((matrix, *permutations), axis=0)

class BeliefPropagation:
    def __init__(self, channel_llr, ldpc_matrix):
        self.channel_llr_matrix = np.tile(channel_llr, (ldpc_matrix.shape[0], 1))
        self.ldpc_matrix = ldpc_matrix
        self.nodes_llr = np.zeros_like(ldpc_matrix)
        
    
    
    def transmit_v_nodes_messages(self):
        sum_cols = np.tile(self.nodes_llr.sum(axis=0), (self.nodes_llr.shape[0], 1))
        self.nodes_llr = (sum_cols - self.nodes_llr + self.channel_llr_matrix) * self.ldpc_matrix

    def transmit_c_nodes_messages(self):
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
                
                        
                
                
                
            
        
        


