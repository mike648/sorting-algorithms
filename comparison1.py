# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:21:11 2024

@author: HomePC
"""

# Importing necessary libraries
import numpy as np  # Importing numpy for generating random arrays and numerical operations
import time  # Importing time for measuring execution time
import copy  # Importing copy for deep copying arrays
import matplotlib.pyplot as plt  # Importing matplotlib for plotting results

# Generate random arrays of sizes 100, 1000, and 10000
array_sizes = [100, 1000, 10000]  # Defining array sizes to test
arrays = {size: np.random.randint(0, 10000, size) for size in array_sizes}  # Creating random arrays for each size

# Function to perform Selection Sort
def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        min_idx = i  # Assume the current position is the minimum
        for j in range(i+1, n):  # Iterate over the remaining unsorted elements
            if arr[j] < arr[min_idx]:  # Find the minimum element
                min_idx = j  # Update the minimum index
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum element with the current element

# Function to perform Merge Sort
def merge_sort(arr):
    if len(arr) > 1:  # Base case: if array has more than 1 element, proceed with sorting
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Divide the array into left half
        right_half = arr[mid:]  # Divide the array into right half

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for left_half, right_half, and merged array

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):  # While both halves have elements
            if left_half[i] < right_half[j]:  # Compare elements from both halves
                arr[k] = left_half[i]  # Place the smaller element into the merged array
                i += 1  # Move to the next element in left_half
            else:
                arr[k] = right_half[j]  # Place the smaller element into the merged array
                j += 1  # Move to the next element in right_half
            k += 1  # Move to the next position in the merged array

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to perform QuickSort
def quick_sort(arr):
    if len(arr) <= 1:  # Base case: if array has 1 or no elements, it's already sorted
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)  # Recursively sort left and right and concatenate with middle

# Measure execution time for each sorting algorithm on each array size
execution_times = {
    'Selection Sort': [],  # Initialize list for Selection Sort execution times
    'Merge Sort': [],  # Initialize list for Merge Sort execution times
    'QuickSort': []  # Initialize list for QuickSort execution times
}

# Iterate over each array size
for size in array_sizes:
    # Iterate over each sorting function
    for sort_name, sort_func in zip(['Selection Sort', 'Merge Sort', 'QuickSort'], [selection_sort, merge_sort, quick_sort]):
        arr = copy.deepcopy(arrays[size])  # Create a deep copy of the array to sort
        start_time = time.time()  # Record the start time
        if sort_name == 'QuickSort':  # Check if the sorting function is QuickSort
            sort_func(arr)  # Perform QuickSort
        else:
            sort_func(arr)  # Perform the sorting function (for Selection Sort and Merge Sort)
        end_time = time.time()  # Record the end time
        execution_times[sort_name].append(end_time - start_time)  # Calculate and store the execution time

# Plot the results
for sort_name in execution_times:
    plt.plot(array_sizes, execution_times[sort_name], label=sort_name)  # Plot execution time for each sorting function

plt.xlabel('Array Size')  # Set x-axis label
plt.ylabel('Execution Time (seconds)')  # Set y-axis label
plt.title('Sorting Algorithm Performance Comparison')  # Set plot title
plt.legend()  # Show legend
plt.grid(True)  # Show grid
plt.show()  # Display the plot
