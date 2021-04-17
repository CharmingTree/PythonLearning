
def merge(arr, west : int, middle : int, east : int):
    print('mm')
    i = west
    j = middle+1
    k = west
    templist = []

    while i <= middle and j <= east:
        if arr[i] > arr[j]:
            templist.append(arr[j])
            j += 1
        else:
            templist.append(arr[i])
            i += 1
        k += 1
    
    if i > middle:
        for t in range(j, east+1):
            templist.append(arr[t])
    else:
        for t in range(i, middle+1):
            templist.append(arr[t])

    for t in range(len(templist)):
        arr[west+t] = templist[t]


def mergesort(arr, start, end):
    print(start, end)
    if start < end:
        middle = (start + end) // 2
        mergesort(arr, start, middle)
        mergesort(arr, middle+1, end)
        merge(arr, start, middle, end)


import random

mylist = [random.randint(1,100) for x in range(100)]

print(f"before List : {mylist}, {len(mylist)}")

mergesort(mylist, 0, len(mylist)-1)

print(f"after List : {mylist}")