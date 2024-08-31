from cProfile import label
import time
import matplotlib.pyplot as plt
import random
import copy

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def generate_test_data(size):
      return list(range(1, size - 1))
  

def profile_selection_sort(input_sizes):
    execution_times = []
    for size in input_sizes:
        test_data = generate_test_data(size)
        start_time = time.time()
        selection_sort(copy.deepcopy(test_data))  # We use a deep copy to avoid modifying the original data
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times

def plot_graph(input_sizes, execution_times):
    plt.plot(input_sizes, execution_times, label = 'Best Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Selection Sort Best Case Profiler')
    plt.ylim(0.000, max(execution_times) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.show()

def main():
    input_sizes = [100, 200, 300, 400, 500]
    selection_times = profile_selection_sort(input_sizes)
    plot_graph(input_sizes, selection_times)

if __name__ == '__main__':
    main()
