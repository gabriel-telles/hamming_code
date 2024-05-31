import numpy as np

class GaussianChannel:
    def __init__ (self, sigma):
        self.sigma = sigma
    
    def transmit_LLR(self, symbols):
        return (2 / self.sigma ** 2) * (np.array(symbols) + np.random.normal(0, self.sigma, len(symbols)))