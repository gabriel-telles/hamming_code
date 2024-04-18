import numpy as np
from copy import deepcopy
from bsc_channel import BSCChannel
from generate_matrices import generate_parity_matrix
from ldpc_decoder import LdpcDecoder

class LdpcChannel():
    def __init__(self, p=0.1, dv=3, dc=7, N=98, iterations=100):
        self.__channel = BSCChannel(p)
        self.__decoder = LdpcDecoder(generate_parity_matrix(dv, dc, N))
        self.__N = N
        self.__iterations = iterations
        
    def transmit(self):
        bits = np.array([0]*self.__N).astype(int)
        received = self.__channel.change_bits(bits)
        decoded = self.__decoder.decode(received, self.__iterations)
        return decoded
