import random
import sys
import time

import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def main():
    sys.setrecursionlimit(100000)

    sizes = [1000, 5000, 10000, 50000]

    randomized_times = []
    deterministic_times = []

    for size in sizes:
        base_array = [random.randint(0, 100000) for _ in range(size)]
        r_total = 0
        d_total = 0

        for _ in range(5):
            arr_copy = base_array.copy()

            start = time.perf_counter()
            randomized_quick_sort(arr_copy)
            end = time.perf_counter()

            r_total += (end - start)

            arr_copy = base_array.copy()

            start = time.perf_counter()
            deterministic_quick_sort(arr_copy)
            end = time.perf_counter()

            d_total += (end - start)

        r_avg = r_total / 5
        d_avg = d_total / 5

        randomized_times.append(r_avg)
        deterministic_times.append(d_avg)

        print(f"Array size: {size}")
        print(f"   Randomized QuickSort: {r_avg:.4f} seconds")
        print(f"   Deterministic QuickSort: {d_avg:.4f} seconds\n")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, marker='o', label='Randomized QuickSort')
    plt.plot(sizes, deterministic_times, marker='o', label='Deterministic QuickSort')
    plt.xlabel('Array Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Comparison of Randomized and Deterministic QuickSort')
    plt.legend()
    plt.grid(True)
    plt.savefig('quicksort_comparison.png')
    plt.show()


if __name__ == '__main__':
    main()