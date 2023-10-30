import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high, count):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        count[0] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, count):
    if low < high:
        pi = partition(arr, low, high, count)
        quicksort(arr, low, pi - 1, count)
        quicksort(arr, pi + 1, high, count)

def analyze_quicksort(length):
    arr = [random.randint(1, 100) for _ in range(length)]
    count = [0]
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1, count)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000
    return count[0], running_time

def merge(arr, left, mid, right, count):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        count[0] += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def mergesort(arr, left, right, count):
    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid, count)
        mergesort(arr, mid+1, right, count)
        merge(arr, left, mid, right, count)

def analyze_mergesort(length):
    arr = [random.randint(1, 100) for _ in range(length)]
    count = [0]
    start_time = time.time()
    mergesort(arr, 0, len(arr) - 1, count)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000
    return count[0], running_time

def insertion_sort(arr, count):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            count[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def analyze_insertion_sort(length):
    arr = [random.randint(1, 100) for _ in range(length)]
    count = [0]
    start_time = time.time()
    insertion_sort(arr, count)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000
    return count[0], running_time

def plot_counts(lengths, counts, algorithms):
    for algorithm, count in zip(algorithms, counts):
        plt.plot(lengths, count, label=algorithm)

    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.title('Number of Operations vs. Length of List')
    plt.legend()
    plt.show()

# Example usage
lengths = [100, 500, 1000, 5000, 10000]  # Define the lengths of the lists

# Define the algorithms to be analyzed
algorithms = ['QuickSort', 'Insertion Sort', 'Merge Sort']

# Lists to store the counts for each algorithm and length
counts_quicksort = []
counts_insertionsort = []
counts_mergesort = []

# Analyze each algorithm for each length
for length in lengths:
    num_comparisons_qs, _ = analyze_quicksort(length)
    counts_quicksort.append(num_comparisons_qs)

    num_comparisons_is, _ = analyze_insertion_sort(length)
    counts_insertionsort.append(num_comparisons_is)


    num_comparisons_ms, _ = analyze_mergesort(length)
    counts_mergesort.append(num_comparisons_ms)

# Plot the number of comparisons for each algorithm
plot_counts(lengths, [counts_quicksort, counts_insertionsort, counts_mergesort], algorithms)