
from joblib import Parallel, delayed
from numpy_pi import numpy_calc_pi


def joblib_calc_pi(n_samples, n_jobs):
    residual = n_samples % n_jobs
    # get number of samples per worker
    n_samples_per_worker = int((n_samples - residual) / n_jobs)
    n_samples_per_process = (n_samples_per_worker, ) * n_jobs
    # apply residual for first worker
    n_samples_per_process = (int(n_samples_per_process[0] + residual), ) + n_samples_per_process[1:]
    # calc pi in parallel
    results = Parallel(n_jobs=n_jobs)(delayed(numpy_calc_pi)(sample) for sample in n_samples_per_process)
    
    count_list = [res * sample for res, sample in zip(results, n_samples_per_process)]
    return sum(count_list) / n_samples
