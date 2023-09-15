# SYSC 2100 Winter 2023 Lab 11/Asst 2

# Put import statements here.
import random
from time import perf_counter
from sort import bubble_sort, selection_sort, insertion_sort, heapsort

__author__ = 'Damon Ricci'
__student_number__ = '101229913'


# Helper function to generate a list of random integers
def random_int_list(length: int) -> list:
    return [random.randint(0, 10000) for _ in range(length)]


# Your profiling functions can have as many parameters as you want.
# The return type of each function is up to you.

def profile_bubble_sort():
    results = []
    trials = 10
    lengths = [1000, 1250, 1500, 1750]

    for length in lengths:
        times = []
        for _ in range(trials):
            data = random_int_list(length)
            start = perf_counter()
            bubble_sort(data, len(data))  # Pass the length of the list
            end = perf_counter()
            times.append(end - start)
        average_time = sum(times) / trials
        results.append((length, average_time))

    return results


def profile_selection_sort():
    results = []
    trials = 10
    lengths = [1000, 1250, 1500, 1750]

    for length in lengths:
        times = []
        for _ in range(trials):
            data = random_int_list(length)
            start = perf_counter()
            selection_sort(data, len(data))  # Changed this line
            end = perf_counter()
            times.append(end - start)
        average_time = sum(times) / trials
        results.append((length, average_time))

    return results


def profile_insertion_sort():
    results = []
    trials = 10
    lengths = [1000, 1250, 1500, 1750]

    for length in lengths:
        times = []
        for _ in range(trials):
            data = random_int_list(length)
            start = perf_counter()
            insertion_sort(data, len(data))  # Changed this line
            end = perf_counter()
            times.append(end - start)
        average_time = sum(times) / trials
        results.append((length, average_time))

    return results


def profile_heapsort():
    results = []
    trials = 10
    lengths = [1000, 1250, 1500, 1750]

    for length in lengths:
        times = []
        for _ in range(trials):
            data = random_int_list(length)
            start = perf_counter()
            heapsort(data, len(data))  # Changed this line
            end = perf_counter()
            times.append(end - start)
        average_time = sum(times) / trials
        results.append((length, average_time))

    return results

# You are permitted to change this script.


if __name__ == '__main__':
    bubble_results = profile_bubble_sort()
    selection_results = profile_selection_sort()
    insertion_results = profile_insertion_sort()
    heapsort_results = profile_heapsort()

    print("Bubble Sort Results:", bubble_results)
    print("Selection Sort Results:", selection_results)
    print("Insertion Sort Results:", insertion_results)
    print("Heapsort Results:", heapsort_results)
