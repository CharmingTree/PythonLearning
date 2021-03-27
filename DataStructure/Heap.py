
def maxHeapify(arr : list, root : int):
    length = len(arr)

    if root >= length:
        return
    
    child1 = root * 2 + 1
    child2 = root * 2 + 2

    maxHeapify(arr, child1)
    maxHeapify(arr, child2)

    if child2 >= length:
        if child1 >= length:
            return
        else:
            if arr[root] < arr[child1]:
                arr[root], arr[child1] = arr[child1], arr[root]
            return
    
    large = child1

    if arr[child1] < arr[child2]:
        large = child2
    
    if arr[root] < arr[large]:
        arr[root], arr[large] = arr[large], arr[root]
        maxHeapSort(arr, large, length)
    
    return
    
def maxHeapSort(arr : list, root : int, length : int):

    child1 = root * 2 + 1
    child2 = root * 2 + 2

    if child2 >= length:
        if child1 >= length:
            return
        else:
            if arr[root] < arr[child1]:
                arr[root], arr[child1] = arr[child1], arr[root]
            return
    

    if arr[child1] > arr[child2]:
        child1 ,child2 = child2, child1
    
    if arr[root] < arr[child2]:
        arr[root], arr[child2] = arr[child2], arr[root]
        maxHeapSort(arr, child2, length)
    return


def heapSort(arr : list, start : int, end : int):
    maxHeapify(arr, 0)
    print(arr)
    for i in reversed(range(len(arr))):
        print(i)
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapSort(arr, 0, i)


a = [10, 1, 3, 5, 2, 11, 123, 0]

heapSort(a, 0, len(a))

print(a)
