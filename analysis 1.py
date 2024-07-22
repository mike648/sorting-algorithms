# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:41:16 2024

@author: HomePC
"""

import random  # Import the random module for generating random numbers
import time  # Import the time module for measuring execution time

# Function to create a random array of a given size
def create_random_array(size):
    # Return a list of random integers between 0 and 100000
    return [random.randint(0, 100000) for _ in range(size)]

# Function to perform Selection Sort and count comparisons
def selection_sort(arr):
    comparisons = 0  # Initialize comparison count
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        min_idx = i  # Assume the current position is the minimum
        for j in range(i+1, n):  # Iterate over the remaining unsorted elements
            comparisons += 1  # Increment comparison count
            if arr[j] < arr[min_idx]:  # Find the minimum element
                min_idx = j  # Update the minimum index
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum element with the current element
    return comparisons  # Return the total number of comparisons

# Function to perform Merge Sort and count comparisons
def merge_sort(arr):
    comparisons = [0]  # Use a list to pass comparison count by reference

    # Helper function to merge two sorted arrays
    def merge(left, right):
        merged = []  # Initialize the merged array
        while left and right:  # While both arrays have elements
            comparisons[0] += 1  # Increment comparison count
            if left[0] <= right[0]:  # Compare the first elements of both arrays
                merged.append(left.pop(0))  # Append the smaller element to the merged array
            else:
                merged.append(right.pop(0))  # Append the smaller element to the merged array
        merged.extend(left or right)  # Extend the merged array with remaining elements
        return merged  # Return the merged array

    # Helper function to recursively sort the array
    def sort(arr):
        if len(arr) <= 1:  # Base case: if array has 1 or no elements, it's already sorted
            return arr
        mid = len(arr) // 2  # Find the middle index
        left = sort(arr[:mid])  # Recursively sort the left half
        right = sort(arr[mid:])  # Recursively sort the right half
        return merge(left, right)  # Merge the sorted halves

    sorted_arr = sort(arr)  # Sort the array
    arr[:] = sorted_arr  # Update the original array with the sorted array
    return comparisons[0]  # Return the total number of comparisons

# Function to perform QuickSort and count comparisons
def quicksort(arr):
    comparisons = [0]  # Use a list to pass comparison count by reference

    # Helper function to recursively sort the array
    def sort(arr):
        if len(arr) <= 1:  # Base case: if array has 1 or no elements, it's already sorted
            return arr
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        comparisons[0] += len(arr) - 1  # Increment comparison count by the number of comparisons in this partition
        return sort(left) + middle + sort(right)  # Recursively sort left and right and concatenate with middle

    sorted_arr = sort(arr)  # Sort the array
    arr[:] = sorted_arr  # Update the original array with the sorted array
    return comparisons[0]  # Return the total number of comparisons

# Function to measure the execution time and comparisons of a sorting function
def measure_sorting_performance(arr, sort_func):
    arr_copy = arr[:]  # Create a copy of the array to sort
    start_time = time.time()  # Record the start time
    comparisons = sort_func(arr_copy)  # Perform the sorting and get the comparison count
    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time in milliseconds
    return execution_time, comparisons  # Return the execution time and comparison count

# Main function to analyze the performance of sorting algorithms
def analyze_sorting_algorithms():
    sizes = [100, 1000, 10000]  # Define the sizes of arrays to test
    results = {size: {} for size in sizes}  # Initialize a dictionary to store results

    for size in sizes:  # Iterate over each array size
        random_array = create_random_array(size)  # Create a random array of the given size
        print(f"Analyzing array size: {size}")  # Print the current array size being analyzed

        # Test each sorting function
        for sort_name, sort_func in [("Selection Sort", selection_sort), 
                                     ("Merge Sort", merge_sort), 
                                     ("QuickSort", quicksort)]:
            exec_time, comparisons = measure_sorting_performance(random_array, sort_func)  # Measure performance
            results[size][sort_name] = (exec_time, comparisons)  # Store the results
            print(f"{sort_name} - Time: {exec_time:.2f} ms, Comparisons: {comparisons}")  # Print the results

    return results  # Return the final results

# Run the analysis and print the final results
results = analyze_sorting_algorithms()  # Run the analysis function
print("\nFinal Results:")  # Print the header for final results
for size, data in results.items():  # Iterate over each array size in the results
    print(f"\nArray Size: {size}")  # Print the array size
    for sort_name, metrics in data.items():  # Iterate over each sorting algorithm and its metrics
        print(f"{sort_name} - Time: {metrics[0]:.2f} ms, Comparisons: {metrics[1]}")  # Print the metrics
