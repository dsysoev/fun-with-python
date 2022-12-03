import os
import sys
import timeit
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def func(x: pd.DataFrame) -> pd.DataFrame:
    # doing some stuff
    return x.copy()


def test() -> pd.DataFrame:
    keys = data.columns.tolist()
    result = (
        data
        .groupby(keys, group_keys=True)
        .apply(func)
    )
    return result


def generate_data(shape: Tuple[int, int]) -> pd.DataFrame:
    """ create pandas dataframe with random data """
    df = pd.DataFrame(np.random.RandomState(47).randint(0, 10, size=shape))
    df = '_' + df.astype(str) + '_'
    df.columns = df.columns.astype(str)
    return df


def main() -> None:
    global data

    # print python and pandas version
    py_version = sys.version.replace('\n', ' ')
    pandas_version = pd.__version__
    print(f"""python version: {py_version}\npandas version: {pandas_version}""")

    # execution time
    current = []
    for j in range(2, 10):
        shape = (10000, j)
        data = generate_data(shape=shape)
        execution_time = timeit.timeit("test()", setup="from __main__ import test", number=10)
        current.append({'shape': str(shape), pandas_version: execution_time})
        print(f"""data shape    : {shape} execution time: {execution_time:.2f} seconds""")
    current = pd.DataFrame(current).round(4)
    current.set_index('shape', inplace=True)

    results_path = 'results.csv'
    if os.path.isfile(results_path):
        results = pd.read_csv(results_path, index_col=0)
        # union with other results
        results[pandas_version] = current[pandas_version].values
    else:
        results = current.copy()

    # save results to file
    results.to_csv(results_path)

    # save chart
    list_of_versions = sorted(results.columns.tolist())
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(results[list_of_versions], label=list_of_versions)
    ax.legend()
    ax.set_yscale('log')
    fig.savefig('results.png')


if '__main__' == __name__:
    main()
