from task5_concurrency.sorting import (
    merge_sort,
    parallel_merge_sort,
    threaded_merge_sort
)


data = [38, 27, 43, 3, 9, 82, 10]

sequential_result = merge_sort(data)

executor_result = parallel_merge_sort(
    data,
    max_workers=2
)

thread_result = threaded_merge_sort(
    data,
    thread_count=2
)

print("Original data:", data)
print("Sequential result:", sequential_result)
print("ThreadPoolExecutor result:", executor_result)
print("Thread result:", thread_result)