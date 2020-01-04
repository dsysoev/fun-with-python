
import numexpr as ne
import numpy as np


def numexpr_pi(n_samples):
    x = np.random.ranf(n_samples)
    y = np.random.ranf(n_samples)
    return 4 * ne.evaluate("sum(where((x ** 2 + y ** 2) < 1, 1, 0))") / n_samples
