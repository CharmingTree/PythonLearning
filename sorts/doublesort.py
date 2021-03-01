def double_sort(list):
    """
    :param collection: mutable ordered sequence of elements
    :return: the same collection in ascending order
    Examples:
    >>> double_sort([-1, -2, -3, -4, -5, -6, -7])
    [-7, -6, -5, -4, -3, -2, -1]
    >>> double_sort([])
    []
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6])
    [-6, -5, -4, -3, -2, -1]
    >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
    True
    """

    no_of_elements = len(list)
    for i in range(0, int(((no_of_elements -1) / 2) + 1)):
        for j in range(0, no_of_elements -1):
            if (list[j+1] < list[j]):
                temp = list[j + 1]
                list[j+1] = list[j]
                list[j] = temp
            if (list[no_of_elements -1 -j] < list[no_of_elements -2 -j]):
                temp = list[no_of_elements -1 -j]
                list[no_of_elements -1 -j] = list[no_of_elements -2 -j]
                list[no_of_elements -2 -j] = temp
    return list

if __name__ == "__main__":
    print("enter the list to be sorted")
    list = [int(x) for x in input().split(sep=',')]
    sorted_list = double_sort(list)
    print("the sorted list is")
    print(sorted_list)