import numpy as np

def linear_to_db(value):
    return 10*np.log10(value)

def db_to_linear(value):
    return 10**(value/10)

def N0_from_db_value(snr_db_value, Eb=1):
    return Eb/db_to_linear(snr_db_value)