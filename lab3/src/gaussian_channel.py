import numpy as np

class GaussianChannel:
    def __init__ (self, N0):
        self.sigma = np.sqrt(N0/2)
    
    def transmit_LLR(self, bits):
        symbols = GaussianChannel.bits_to_symbols(bits)
        return (2 / self.sigma ** 2) * (symbols + np.random.normal(0, self.sigma, len(symbols)))
    
    @staticmethod
    def bits_to_symbols(bits):
        symbols = np.array(bits)
        symbols[symbols == 1] = -1
        symbols[symbols == 0] = 1
        return symbols