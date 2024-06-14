from belief_propagation import BeliefPropagation
from gaussian_channel import GaussianChannel
import numpy as np
from copy import deepcopy

def generate_ldpc_matrix(dv, dc, N):
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

class LdpcBpskGaussianSystem:
    def __init__(self, N0, Eb=1, dv=3, dc=7, N=98, max_iter=10):
        self.__channel = GaussianChannel(N0, Eb)
        self.__belief_propagation = BeliefPropagation(generate_ldpc_matrix(dv, dc, N))
        self.__N = N
        self.__max_iter = max_iter
        
    def apply_noise_and_decode(self):
        bits = np.zeros(self.__N)
        self.channel_llr = self.__channel.transmit_LLR(bits)
        return self.__belief_propagation.decode(self.channel_llr, self.__max_iter)
    
    def get_uncoded_bits(self):
        Lf = deepcopy(self.channel_llr)
        Lf[Lf > 0] = 0
        Lf[Lf < 0] = 1 
        return Lf # uncoded_bits
    
    