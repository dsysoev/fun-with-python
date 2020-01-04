
import numexpr as ne
import numpy as np


def numexpr_pi(n_samples):
    rand = np.random.uniform(size=(2, int(n_samples)))
    s = ne.evaluate("sum(rand ** 2, axis=0)")
    return ne.evaluate("sum(where(s <= 1, 1, 0))") * 4 / n_samples
