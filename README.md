# Algorithm Profiler for Simple Sorting Algorithms

## Overview

This project involves building an algorithm profiler that analyzes the performance of three simple sorting algorithms: Bubble Sort, Selection Sort, and Insertion Sort. The profiler evaluates the algorithms based on their time complexity in best-case, worst-case, and average-case scenarios. The analysis and insights gained from this profiler can be useful for understanding the efficiency of these basic algorithms.

## Table of Contents

1. [Introduction](#introduction)
   - [Algorithm Analysis](#algorithm-analysis)
   - [Sorting](#sorting)
   - [Algorithm Profiler](#algorithm-profiler)
2. [Bubble Sort](#bubble-sort)
   - [Best Case](#best-case)
   - [Worst Case](#worst-case)
   - [Average Case](#average-case)
3. [Selection Sort](#selection-sort)
   - [Best Case](#best-case-1)
   - [Worst Case](#worst-case-1)
   - [Average Case](#average-case-1)
4. [Insertion Sort](#insertion-sort)
   - [Best Case](#best-case-2)
   - [Worst Case](#worst-case-2)
   - [Average Case](#average-case-2)
5. [Conclusion](#conclusion)
6. [Usage](#usage)
   - [Cloning the Repository](#cloning-the-repository)
   - [Running the Profiler](#running-the-profiler)

## Introduction

### Algorithm Analysis

Algorithm analysis is the process of studying and evaluating the efficiency of algorithms, focusing on time and space complexity as input size increases. The goal is to determine which algorithm is best suited for a specific task by comparing different algorithms.

### Sorting

Sorting involves arranging elements in a particular order, often used in data processing and management. This project focuses on simple sorting algorithms that are easy to understand and implement, making them educational tools for learning about sorting.

### Algorithm Profiler

An algorithm profiler is a tool used to measure and analyze the performance of an algorithm. It helps identify performance bottlenecks and provides insights into optimization opportunities.

## Bubble Sort

Bubble Sort is a simple sorting algorithm that compares and swaps adjacent elements if they are in the wrong order. It is stable and works well for small datasets but is inefficient for large datasets due to its O(n^2) time complexity.

### Best Case

- **Time Complexity**: O(n)  
  Occurs when the list is already sorted, requiring only one pass through the data without any swaps.

### Worst Case

- **Time Complexity**: O(n^2)  
  Occurs when the list is in reverse order, requiring maximum comparisons and swaps.

### Average Case

- **Time Complexity**: O(n^2)  
  Typically occurs when the input list is randomly ordered, leading to an average number of comparisons and swaps.

## Selection Sort

Selection Sort repeatedly selects the smallest element from the unsorted portion of the list and moves it to the sorted portion. It is an in-place sorting algorithm but is not stable.

### Best Case

- **Time Complexity**: O(n^2)  
  Even if the list is already sorted, the algorithm still needs to go through all elements to verify their order.

### Worst Case

- **Time Complexity**: O(n^2)  
  Occurs when the list is in reverse order, requiring maximum comparisons and swaps.

### Average Case

- **Time Complexity**: O(n^2)  
  Similar to the worst-case, as Selection Sort performs a fixed number of comparisons regardless of the initial order.

## Insertion Sort

Insertion Sort builds a sorted list one element at a time by inserting each new element into its correct position within the sorted portion. It is more efficient for small or nearly sorted datasets.

### Best Case

- **Time Complexity**: O(n)  
  Occurs when the list is already sorted, requiring minimal comparisons and no swaps.

### Worst Case

- **Time Complexity**: O(n^2)  
  Occurs when the list is in reverse order, requiring maximum comparisons and swaps.

### Average Case

- **Time Complexity**: O(n^2)  
  Occurs when the list is randomly ordered, leading to an average number of comparisons and swaps.

## Conclusion

This project provided an in-depth analysis of Bubble Sort, Selection Sort, and Insertion Sort. While these algorithms are easy to understand, they are inefficient for large datasets due to their O(n^2) time complexities. However, they serve as valuable educational tools and are useful in specific scenarios, such as when working with small or nearly sorted datasets.

## Usage

### Cloning the Repository

To get started with the project, you can clone the repository using the following command:
  
    ```bash
    git clone https://github.com/yourusername/algorithm-profiler.git


## Running the Profiler

1.	Navigate to the project directory:
     ```bash
     cd algorithm-profiler
2. 	Run the Python script:
    ```bash
    python3 all_in_one_profiler.py
Or You can run the profiler for each algorith separetley in their respective direcotry!
