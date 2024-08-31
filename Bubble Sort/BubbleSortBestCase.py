import time
import copy
import matplotlib.pyplot as plt
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    
    
def profile_best_case(input_sizes):
    execution_times = []
    for size in input_sizes:
        test_data = list(range(1, size + 1))
        start_time = time.perf_counter()
        bubble_sort(copy.deepcopy(test_data))
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times
    
    
def plot_best_case(input_sizes, execution_times):
     plt.plot(input_sizes, execution_times, label='Best Case')
     plt.xlabel('Input Size')
     plt.ylabel('Execution Time (seconds)')
     plt.legend()
     plt.title('Bubble Sort Best Case Profiler')

     # Set y-axis limits and ticks
     plt.ylim(0.000, max(execution_times) + 0.002)
     y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times) + 0.002) / 0.002) + 1)]
     plt.yticks(y_ticks)

     plt.show()

def main():
    input_sizes = [100, 200, 300, 400, 500]
    best_case_times = profile_best_case(input_sizes)
    plot_best_case(input_sizes, best_case_times)

if __name__ == '__main__':
    main()
