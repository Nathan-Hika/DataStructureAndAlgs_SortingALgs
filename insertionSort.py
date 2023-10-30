import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high, count):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        count[0] += 1  # Increment the count for each comparison operation
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, count):
    if low < high:
        pivot_index = partition(arr, low, high, count)
        quicksort(arr, low, pivot_index - 1, count)
        quicksort(arr, pivot_index + 1, high, count)

def analyze_quicksort(length):
    arr = [random.randint(1, 100) for _ in range(length)]
    count = [0]  # Initialize the count as a mutable object to pass it by reference
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1, count)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return count[0], running_time

def insertion_sort(arr, count):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            count[0] += 1  # Increment the count for each comparison operation
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def analyze_insertion_sort(length):
    arr = [random.randint(1, 100) for _ in range(length)]
    count = [0]  # Initialize the count as a mutable object to pass it by reference
    start_time = time.time()
    insertion_sort(arr, count)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return count[0], running_time

def plot_counts(lengths, counts, algorithm):
    plt.plot(lengths, counts)
    plt.xlabel('Length of List')
    plt.ylabel('Number of Operations')
    plt.title('Number of Operations vs. Length of List - ' + algorithm)
    plt.show()

# Example usage
lengths = [100, 500, 1000, 2000, 5000]  # Define the lengths of the lists
counts_quicksort = []
counts_insertionsort = []

for length in lengths:
    num_comparisons_qs, _ = analyze_quicksort(length)
    counts_quicksort.append(num_comparisons_qs)

    num_comparisons_is, _ = analyze_insertion_sort(length)
    counts_insertionsort.append(num_comparisons_is)

plot_counts(lengths, counts_quicksort, 'QuickSort')
plot_counts(lengths, counts_insertionsort, 'Insertion Sort')