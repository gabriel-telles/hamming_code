import numpy as np
from ts_encoder import TSEncoder
from bsc_channel import BSCChannel
from ts_decoder import TSDecoder

class TSChannel():
    def __init__(self, p):
        self.__encoder = TSEncoder()
        self.__channel = BSCChannel(p)
        self.__decoder = TSDecoder()
        
    def transmit(self, info):
        encoded = self.__encoder.encode(info)
        received = self.__channel.change_bits(encoded)
        decoded = self.__decoder.decode(received)
        return decoded[0:9]
