
def partition(arr : list, left, right):
    
    pivot = right

    while left < right:
        while arr[pivot] > arr[left] and left < right:
            left += 1
        while arr[pivot] <= arr[right] and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[right], arr[pivot] = arr[pivot], arr[right]

    return right

def quickSort(arr : list, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)
    

a = [350, 15, 45, 50, 80, 300, 110, 120, 125, 200]
S = 247
quickSort(a, 0, len(a)-1)
a = [a[i] for i in range(len(a)) if a[i] < S]
powerSet = []

# 멱집합을 추출하는 방법으로는 사실 위의 정렬의 의미가 없다 ㅋ 
for i in range(1,2**len(a)):
    flag = bin(i)[2:].zfill(len(a))
    temp = [a[j] for j in range(len(a)) if flag[j] == '1']
    # 두 쌍 이고, S보단 작은것만 
    if len(temp) == 2 and sum(temp) < S:
        powerSet.append(temp)

powerSet.sort(key=lambda x : sum(x), reverse=True)
print(powerSet)
# S에 가까운 두 쌍이 여러 개일 경우, 큰 수가 작은 쌍을 출력한다? 무슨 의미인지 모르겠음
result = powerSet[0]