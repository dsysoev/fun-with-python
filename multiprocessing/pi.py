

from random import uniform

def estimate_total_in_circle(n_samples):
    total_in_circle = 0
    for step in range(int(n_samples)):
        x = uniform(0, 1)
        y = uniform(0, 1)
        is_in_unit_circle = x * x + y * y <= 1.0
        total_in_circle += is_in_unit_circle
        
    return total_in_circle

def calc_pi(list_total_in_circle, n_samples):
    return sum(list_total_in_circle) * 4 / n_samples


from multiprocessing import Pool


def parallel_calc_pi(n_jobs, n_samples):
    # get residual
    residual = n_samples % n_jobs
    # get number of samples per worker
    n_samples_per_worker = (n_samples - residual) / n_jobs
    n_samples_per_process = (n_samples_per_worker, ) * n_jobs
    # apply residual for first worker
    n_samples_per_process = (n_samples_per_process[0] + residual, ) + n_samples_per_process[1:]
    
    # create pool of executors and calc it
    with Pool(processes=n_jobs) as p:
        list_total_in_circle = p.map(estimate_total_in_circle, n_samples_per_process)
        
    value = calc_pi(list_total_in_circle, n_samples)
    return value
