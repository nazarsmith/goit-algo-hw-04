from sorters import *
from functools import partial

import random
import numpy as np
import timeit

def make_test_data(num_items = 100):
    test_data = list(np.linspace(0, 10000000, num_items))
    random.shuffle(test_data)
    return test_data

test_data = make_test_data(111)
print(f"\nThe 1st 50 items from the list that is to be sorted: {test_data[:20]}.\n", sep = "\n")

part_merge = partial(merger, arr = test_data)
part_insert = partial(insertion_sort, arr = test_data)
native_sort = partial(sorted, test_data)

merge_sort_time = timeit.timeit(stmt = part_merge, number = 20)
insert_sort_time = timeit.timeit(stmt = part_insert, number = 20)
native_sorted_time = timeit.timeit(stmt = native_sort, number = 20)

print(
    "\nThe time it took to sort the list of 111 random numbers is:",
    f"{merge_sort_time} using sorting via merging;",
    f"{insert_sort_time} using sorting via insertions;",
    f"{native_sorted_time} using sorting via the native python sorted() function.\n",
    sep = "\n"
    )

test_data = make_test_data(1111)

part_merge = partial(merger, arr = test_data)
part_insert = partial(insertion_sort, arr = test_data)
native_sort = partial(sorted, test_data)

merge_sort_time = timeit.timeit(stmt = part_merge, number = 20)
insert_sort_time = timeit.timeit(stmt = part_insert, number = 20)
native_sorted_time = timeit.timeit(stmt = native_sort, number = 20)

print(
    "\nThe time it took to sort the list of 1111 random numbers is:",
    f"{merge_sort_time} using sorting via merging;",
    f"{insert_sort_time} using sorting via insertions;",
    f"{native_sorted_time} using sorting via the native python sorted() function.\n",
    sep = "\n"
    )

test_data = make_test_data(11111)

part_merge = partial(merger, arr = test_data)
part_insert = partial(insertion_sort, arr = test_data)
native_sort = partial(sorted, test_data)

merge_sort_time = timeit.timeit(stmt = part_merge, number = 20)
insert_sort_time = timeit.timeit(stmt = part_insert, number = 20)
native_sorted_time = timeit.timeit(stmt = native_sort, number = 20)

print(
    "\nThe time it took to sort the list of 11111 random numbers is:",
    f"{merge_sort_time} using sorting via merging;",
    f"{insert_sort_time} using sorting via insertions;",
    f"{native_sorted_time} using sorting via the native python sorted() function.\n",
    sep = "\n"
    )