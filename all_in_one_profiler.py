import time
import matplotlib.pyplot as plt
import random
import copy

# Selection Sort implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort implementation
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Bubble Sort implementation
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

# generates data for each cases of the 3 sorting algorithms
def generate_test_data(size, scenario):
    if scenario == "best":
        return list(range(1, size - 1))
    elif scenario == "worst":
        return list(range(size, 0, -1))
    else:  # average case, random data
        return [random.randint(1, 1000) for _ in range(size)]


# Profiler for each cases of the 3 sorting algorithms
def algorithm_profiler(input_sizes, scenario):

    execution_times = []     # Stores execution time of each case for each sorting algorithms
    for size in input_sizes:
        test_data = generate_test_data(size, scenario)
        start_time = time.time()
        bubble_sort(copy.deepcopy(test_data))  # Used a copy so that so the original data won't be affected
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times

# Graph plotter for best case scenario of Bubble Sort's best case scenario
def bubble_sort_best_case_graph(input_sizes, execution_times_best):
    plt.plot(input_sizes, execution_times_best, label='Best Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Bubble Sort Best Case Profiler')
    plt.ylim(0.000, max(execution_times_best) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_best) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Bubble Sort's worst case scenario
def bubble_sort_worst_case_graph(input_sizes, execution_times_worst):
    plt.plot(input_sizes, execution_times_worst, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Bubble Sort Worst Case Profiler')
    plt.ylim(0.000, max(execution_times_worst) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_worst) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Bubble Sort's average case scenario
def bubble_sort_avg_case_graph(input_sizes, execution_times_avg):
    plt.plot(input_sizes, execution_times_avg, label='Average Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Bubble Sort Average Case Profiler')
    plt.ylim(0.000, max(execution_times_avg) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_avg) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Inserion Sort's best case scenario
def insertion_sort_best_case_graph(input_sizes, execution_times_best):
    plt.plot(input_sizes, execution_times_best, label='Best Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Insertion Sort Best Case Profiler')
    plt.ylim(0.000, max(execution_times_best) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_best) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Inserion Sort's worst case scenario
def insertion_sort_worst_case_graph(input_sizes, execution_times_worst):
    plt.plot(input_sizes, execution_times_worst, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Insertion Sort Worst Case Profiler')
    plt.ylim(0.000, max(execution_times_worst) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_worst) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Inserion Sort's average case scenario
def insertion_sort_avg_case_graph(input_sizes, execution_times_avg):
    plt.plot(input_sizes, execution_times_avg, label='Average Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Insertion Sort Average Case Profiler')
    plt.ylim(0.000, max(execution_times_avg) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_avg) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Slection Sort's best case scenario
def selection_sort_best_case_graph(input_sizes, execution_times_best):
    plt.plot(input_sizes, execution_times_best, label='Best Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Selection Sort Best Case Profiler')
    plt.ylim(0.000, max(execution_times_best) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_best) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Selection Sort's worst case scenario
def selection_sort_worst_case_graph(input_sizes, execution_times_worst):
    plt.plot(input_sizes, execution_times_worst, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Selection Sort Worst Case Profiler')
    plt.ylim(0.000, max(execution_times_worst) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_worst) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

# Graph plotter for best case scenario of Selection Sort's average case scenario
def selection_sort_avg_case_graph(input_sizes, execution_times_avg):
    plt.plot(input_sizes, execution_times_avg, label='Average Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.title('Selection Sort Average Case Profiler')
    plt.ylim(0.000, max(execution_times_avg) + 0.002)
    y_ticks = [0.000 + 0.002 * i for i in range(int((max(execution_times_avg) + 0.002) / 0.002) + 1)]
    plt.yticks(y_ticks)
    plt.grid(True)
    plt.show()

def main():

    # Initalizes test data size for each algorithms
    input_sizes = [100, 200, 300, 400, 500]

    
    bubble_times_best = algorithm_profiler(input_sizes, 'best')
    bubble_times_worst = algorithm_profiler(input_sizes, 'worst')
    bubble_times_avg = algorithm_profiler(input_sizes, 'average')
    bubble_sort_best_case_graph(input_sizes, bubble_times_best)
    bubble_sort_worst_case_graph(input_sizes, bubble_times_worst)
    bubble_sort_avg_case_graph(input_sizes, bubble_times_avg)


    insertion_times_best = algorithm_profiler(input_sizes, 'best')
    insertion_times_worst = algorithm_profiler(input_sizes, 'worst')
    insertion_times_avg = algorithm_profiler(input_sizes, 'average')
    insertion_sort_best_case_graph(input_sizes, insertion_times_best)
    insertion_sort_worst_case_graph(input_sizes, insertion_times_worst)
    insertion_sort_avg_case_graph(input_sizes, insertion_times_avg)


    selection_times_best = algorithm_profiler(input_sizes, 'best')
    selection_times_worst = algorithm_profiler(input_sizes, 'worst')
    selection_times_avg = algorithm_profiler(input_sizes, 'average')
    selection_sort_best_case_graph(input_sizes, selection_times_best)
    selection_sort_worst_case_graph(input_sizes, selection_times_worst)
    selection_sort_avg_case_graph(input_sizes, selection_times_avg)


if __name__ == '__main__':
    main()
