from typing import NoReturn


def maxHeapify(unsorted, root):
    length = len(unsorted)
    if (root >= length):
        return

    child1 = root * 2 + 1
    child2 = root * 2 + 2

    maxHeapify(unsorted, child1)
    maxHeapify(unsorted, child2)

    if ( child2 >= length):
        if (child1 >= length):
            return
        else:
            if unsorted[root] < unsorted[child1]:
                unsorted[root], unsorted[child1] = unsorted[child1], unsorted[root]
            return
    
    large = child1

    if unsorted[child1] < unsorted[child2]:
        large = child2
    
    if unsorted[root] < unsorted[large]:
        unsorted[root], unsorted[large] = unsorted[large], unsorted[root]
        heapsort(unsorted, large, length)
        return


def heapsort(unsorted, root, length):
    child1 = root * 2 + 1
    child2 = root * 2 + 2

    if (child2 >= length):
        if (child1 >= length):
            return
        else:
            if (unsorted[root] < unsorted[child1]):
                unsorted[root], unsorted[child1] = unsorted[child1], unsorted[root]
            return
    
    if (unsorted[child1] < unsorted[child2]):
        child1, child2 = child2, child1

    if (unsorted[root] < unsorted[child2]):
        unsorted[root], unsorted[child2] = unsorted[child2], unsorted[root]
        heapsort(unsorted, child2, length)

def maxHeapSort(unsorted):
    start = 0
    end = len(unsorted)
    maxHeapify(unsorted, 0)
    for i in range(end-1, start-1, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapsort(unsorted, 0, i)



if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma : \n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(maxHeapSort(unsorted))