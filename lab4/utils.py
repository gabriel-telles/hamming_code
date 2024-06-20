import numpy as np
import scipy.stats as stats

def binary_to_decimal(bits):
    N = len(bits)
    sum = 0
    for i in range(N):
        if bits[N-i-1] == 1:
            sum += (1 << (i))
    return sum

def p_to_Ei_N0(p, R):
    Q_inv = stats.norm.ppf(1-p, loc=0, scale=1)
    return (1/(2*R))*Q_inv**2

def Ei_N0_to_p(snr_Ei_N0_db, R):
    snr_Ei_N0 = db_to_linear(snr_Ei_N0_db)
    return 1-stats.norm.cdf(np.sqrt(2*R*snr_Ei_N0))

def linear_to_db(value):
    return 10*np.log10(value)

def db_to_linear(value):
    return 10**(value/10)

def N0_from_db_value(snr_db_value, Eb=1):
    return Eb/db_to_linear(snr_db_value)

def Ei_snr_db_to_Eb_snr_db(Ei_snr_db, R):
    return linear_to_db(db_to_linear(Ei_snr_db)*R)

def Ei_to_Eb(Ei, R):
    return R * Ei