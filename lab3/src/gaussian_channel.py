import numpy as np

class GaussianChannel:
    def __init__ (self, N0, Eb):
        self.sigma = np.sqrt(N0/2)
        self.Eb = Eb
    
    def transmit_LLR(self, bits):
        symbols = GaussianChannel.bits_to_symbols(bits, self.Eb)
        self.channel_llr =  (2 / self.sigma ** 2) * (symbols + np.random.normal(0, self.sigma, len(symbols)))
        return self.channel_llr
    
    @staticmethod
    def bits_to_symbols(bits, Eb):
        symbols = np.array(bits)
        symbols[symbols == 1] = -np.sqrt(Eb)
        symbols[symbols == 0] = np.sqrt(Eb)
        return symbols