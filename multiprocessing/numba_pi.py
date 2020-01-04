
from numba import jit
import numpy as np


@jit(forceobj=True)
def numpy_calc_pi(n_samples):
    rand = np.random.uniform(size=(2, int(n_samples)))
    count = ((rand ** 2).sum(axis=0) <= 1).sum()
    return count * 4 / n_samples
