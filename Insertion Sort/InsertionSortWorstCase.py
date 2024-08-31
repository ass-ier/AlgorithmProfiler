import time
import matplotlib.pyplot as plt
import random
import copy

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_test_data(size):
        return list(range(size, 0, -1))

def profile_insertion_sort(input_sizes):
    execution_times = []
    for size in input_sizes:
        test_data = generate_test_data(size)
        start_time = time.time()
        insertion_sort(copy.deepcopy(test_data))  # We use a deep copy to avoid modifying the original data
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times

def plot_graph(input_sizes, execution_times):
    plt.plot(input_sizes, execution_times, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Insertion Sort Worst Case Profiler')
    
    # Set y-axis limits
    plt.ylim(0.000, max(execution_times) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)

    plt.show()

def main():
    input_sizes = [100, 200, 300, 400, 500]
    insertion_times = profile_insertion_sort(input_sizes)
    plot_graph(input_sizes, insertion_times)

if __name__ == '__main__':
    main()
