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

def hamming_rate_matrices():
    N_values = [98, 203, 497, 1001]
    matrices = []
    dv = 3
    dc = 7
    for N in N_values:
        matrices.append(generate_parity_matrix(dv, dc, N))
        
    return matrices