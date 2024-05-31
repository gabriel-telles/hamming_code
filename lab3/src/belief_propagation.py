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
        self.v_nodes_llr = np.zeros_like(ldpc_matrix)
    
    def update_v_nodes(self):
        sum_cols = np.tile(self.v_nodes_llr.sum(axis=0), (self.v_nodes_llr.shape[0], 1))
        self.v_nodes_llr = (sum_cols - self.v_nodes_llr + self.channel_llr_matrix) * self.ldpc_matrix

    def update_c_nodes(self):
        
        


