from doctest import testmod
from typing import List

def bucket_sort(my_list: list) -> list:
    """
    >>> data = [-1, 2, -5, 0]
    >>> bucket_sort(data) == sorted(data)
    True
    """
    if len(my_list) == 0:
        return []
    min_value, max_value = min(my_list), max(my_list)
    bucket_count = int(max_value - min_value) + 1
    buckets: List[list] = [[] for _ in range(bucket_count)]

    for i in range(len(my_list)):
        buckets[(int(my_list[i] - min_value) // bucket_count)].append(my_list[i])

    return [v for bucket in buckets for v in sorted(bucket)]


    if __name__ == "__main__":
        from doctest import testmod

        testmod()
        assert bucket_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]