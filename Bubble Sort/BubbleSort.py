import time
import matplotlib.pyplot as plt
import random
import copy

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

def generate_test_data(size, scenario):
    if scenario == "best":
        return list(range(1, size - 1))
    elif scenario == "worst":
        return list(range(size, 0, -1))
    else:  # average case, random data
        return [random.randint(1, 1000) for _ in range(size)]

def profile_bubble_sort(input_sizes, scenario):
    execution_times = []
    for size in input_sizes:
        test_data = generate_test_data(size, scenario)
        start_time = time.time()
        bubble_sort(copy.deepcopy(test_data))  # We use a deep copy to avoid modifying the original data
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times

def plot_graph_best(input_sizes, execution_times_best):
    plt.plot(input_sizes, execution_times_best, label='Best Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Bubble Sort Best Case Profiler')
    plt.ylim(0.000, max(execution_times_best) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_best) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.show()

def plot_graph_worst(input_sizes, execution_times_worst):
    plt.plot(input_sizes, execution_times_worst, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Bubble Sort Worst Case Profiler')
    plt.ylim(0.000, max(execution_times_worst) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_worst) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.show()

def plot_graph_avg(input_sizes, execution_times_avg):
    plt.plot(input_sizes, execution_times_avg, label='Average Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Bubble Sort Average Case Profiler')
    plt.ylim(0.000, max(execution_times_avg) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_avg) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.show()

def main():
    input_sizes = [100, 200, 300, 400, 500]
    bubble_times_best = profile_bubble_sort(input_sizes, 'best')
    bubble_times_worst = profile_bubble_sort(input_sizes, 'worst')
    bubble_times_avg = profile_bubble_sort(input_sizes, 'average')
    plot_graph_best(input_sizes, bubble_times_best)
    plot_graph_worst(input_sizes, bubble_times_worst)
    plot_graph_avg(input_sizes, bubble_times_avg)

if __name__ == '__main__':
    main()
