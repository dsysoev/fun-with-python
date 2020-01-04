
from numba import njit
import numpy as np


@njit(parallel=True)
def numba_calc_pi(n_samples):
    
    x = np.random.ranf(n_samples)
    y = np.random.ranf(n_samples)
    return 4 * np.sum(x ** 2 + y ** 2 < 1) / n_samples
