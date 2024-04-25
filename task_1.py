from sorters import *
from functools import partial

import random
import numpy as np
import matplotlib.pyplot as plt
import timeit

def make_test_data(num_items = 100):
    test_data = list(np.linspace(0, 10000000, num_items))
    random.shuffle(test_data)
    return test_data

def run_tests(num_items):
    test_data = make_test_data(num_items)
    part_merge = partial(merger, arr = test_data)
    part_insert = partial(insertion_sort, arr = test_data)
    native_sort = partial(sorted, test_data)

    merge_sort_time = timeit.timeit(stmt = part_merge, number = 20)
    insert_sort_time = timeit.timeit(stmt = part_insert, number = 20)
    native_sorted_time = timeit.timeit(stmt = native_sort, number = 20)

    print(
        f"\nThe time it took to sort the list of {len(test_data)} random numbers is:",
        f"{merge_sort_time} using sorting via merging;",
        f"{insert_sort_time} using sorting via insertions;",
        f"{native_sorted_time} using sorting via the native python sorted() function.\n",
        sep = "\n"
        )
    
    return merge_sort_time, insert_sort_time, native_sorted_time


low_data = tuple(run_tests(111))
low_mid_data = tuple(run_tests(555))
mid_data = tuple(run_tests(1111))
mid_large_data = tuple(run_tests(5555))
large_data = tuple(run_tests(11111))
large_very_large_data = tuple(run_tests(55555))
very_large_data = tuple(run_tests(111111))

mr, = plt.plot(
    [
        low_data[0], low_mid_data[0], mid_data[0], mid_large_data[0], large_data[0], large_very_large_data[0], very_large_data[0]
    ],
    color = "b",
    alpha = 0.7,
    label = "Merge"
    )
ins, = plt.plot(
    [
        low_data[1], low_mid_data[1], mid_data[1], mid_large_data[1], large_data[1], large_very_large_data[1], very_large_data[1]
    ],
    color = "r",
    alpha = 0.7,
    label = "Insert"
    )
srt, = plt.plot(
    [
        low_data[2], low_mid_data[2], mid_data[2], mid_large_data[2], large_data[2], large_very_large_data[2], very_large_data[2]
    ],
    color = "g",
    alpha = 0.7,
    label = "sorted()"
    )
plt.xlabel('Num experiments')
plt.ylabel('Seconds')
plt.legend(handles = [mr, ins, srt])
plt.show()