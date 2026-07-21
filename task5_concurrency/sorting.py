from concurrent.futures import ThreadPoolExecutor
from threading import Lock, Thread


def merge(left, right):
    result = []

    left_index = 0
    right_index = 0

    while (
        left_index < len(left)
        and right_index < len(right)
    ):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    middle = len(data) // 2

    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    return merge(left, right)


def merge_sorted_lists(sorted_lists):
    result = []

    for sorted_list in sorted_lists:
        result = merge(result, sorted_list)

    return result


def parallel_merge_sort(data, max_workers=2):
    if len(data) <= 1:
        return data

    worker_count = min(
        max_workers,
        len(data)
    )

    chunk_size = (
        len(data) + worker_count - 1
    ) // worker_count

    chunks = [
        data[index:index + chunk_size]
        for index in range(
            0,
            len(data),
            chunk_size
        )
    ]

    sorted_chunks = []
    lock = Lock()

    def sort_chunk(chunk):
        sorted_chunk = merge_sort(chunk)

        with lock:
            sorted_chunks.append(sorted_chunk)

    with ThreadPoolExecutor(
        max_workers=worker_count
    ) as executor:
        futures = [
            executor.submit(
                sort_chunk,
                chunk
            )
            for chunk in chunks
        ]

        for future in futures:
            future.result()

    return merge_sorted_lists(
        sorted_chunks
    )


def threaded_merge_sort(data, thread_count=2):
    if len(data) <= 1:
        return data

    worker_count = min(
        thread_count,
        len(data)
    )

    chunk_size = (
        len(data) + worker_count - 1
    ) // worker_count

    chunks = [
        data[index:index + chunk_size]
        for index in range(
            0,
            len(data),
            chunk_size
        )
    ]

    sorted_chunks = []
    lock = Lock()
    threads = []

    def sort_chunk(chunk):
        sorted_chunk = merge_sort(chunk)

        with lock:
            sorted_chunks.append(sorted_chunk)

    for chunk in chunks:
        thread = Thread(
            target=sort_chunk,
            args=(chunk,)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return merge_sorted_lists(
        sorted_chunks
    )