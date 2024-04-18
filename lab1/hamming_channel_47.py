import numpy as np
from matrices import *
from hamming_encoder import HammingEncoder
from bsc_channel import BSCChannel
from hamming_decoder import HammingDecoder

class HammingChannel47():
    def __init__(self, p):
        self.__encoder = HammingEncoder(generating_matrix_47)
        self.__channel = BSCChannel(p)
        self.__decoder = HammingDecoder(parity_matrix_47)
        
    def transmit(self, info):
        encoded = self.__encoder.encode(info)
        received = self.__channel.change_bits(encoded)
        decoded = self.__decoder.decode(received)
        return decoded[0:4]
