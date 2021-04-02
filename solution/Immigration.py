
# k = 심사대 개수
# lst = 대기자 
# n = 대기자 수 
def solution99(k, lst : list, n):
    answer = 0
    # 각 대기자의 누적 시간(분)을 초기화 
    for i in range(len(lst)):
        if i == 0:
            lst[i].append(0)
        else:
            lst[i].append(lst[i-1][2]+lst[i][0])
    # t = 처음부터 심사가 끝나는 시간을 카운트
    t = 0

    # 심사대의 개수 만큼 리스트를 초기화 
    bucket = [0 for i in range(k)]

    while len(lst) != 0:
        for i in range(len(bucket)):
            # 현재 심사대가 비어있지 않으면 마이너스 카운트
            if bucket[i] != 0:
                bucket[i] -= 1
            # 도착한 대기자가 존재할 경우
            if len(lst) != 0 and lst[0][2] <= t:
                # 심사대가 비어 있는 경우
                if bucket[i] == 0:
                    answer += t-lst[0][2]
                    print(t-lst[0][2])
                    bucket[i] += lst.pop(0)[1]
        t += 1
    
    answer = round(answer / n, 1)
    return answer
        
def solution2(k, lst : list, n):
    curWait = 0
    answer = 0
    if k == 1:
        for i in range(len(lst)):
            if i == 0:
                curWait = lst[i][1]
            else:
                if (curWait - lst[i][0]) > 0:
                    curWait -= lst[i][0]
                    answer += curWait
                    curWait += lst[i][1]
                else:
                    curWait = lst[i][1]
        answer = round(answer / n, 1)
        print(answer)
    else:   
        for i in range(len(lst)):
            if i == 0:
                lst[i].append(0)
            else:
                lst[i].append(lst[i-1][2]+lst[i][0])
        t = 0
        bucket = [0,0]
        while len(lst) != 0:
            if bucket[0] != 0:
                bucket[0] -= 1
            if bucket[1] != 0:
                bucket[1] -= 1
            if lst[0][2] <= t:
                if bucket[0] == 0:
                    answer += t-lst[0][2]
                    #print(t-lst[0][2])
                    bucket[0] += lst.pop(0)[1]
            if len(lst) != 0 and lst[0][2] <= t:
                if bucket[1] == 0:
                    answer += t-lst[0][2]
                    #print(t-lst[0][2])
                    bucket[1] += lst.pop(0)[1]
            t += 1
        
        answer = round(answer / n, 1)
        print(answer)
                

#solution(2,[[0 ,4],[2 ,7],[1 ,6],[2, 5],[1, 3]],5)
#solution(2,[[0 ,3],[2 ,4],[3 ,3]],3)
#solution(2,[[0 ,100],[2 ,4],[3 ,3],[3,10],[5,40]],5)
#solution(2,[[0 ,1],[2 ,1],[2 ,1]],3)
#solution2(2,[[0 ,4],[2 ,7],[1 ,6],[2, 5],[1, 3]],5)
#solution2(2,[[0 ,3],[2 ,4],[3 ,3]],3)
#solution2(2,[[0 ,100],[2 ,4],[3 ,3],[3,10],[5,40]],5)
#solution2(2,[[0 ,1],[2 ,1],[2 ,1]],3)




solution99(2,[[0, 3],[3, 2],[3, 2],[3, 2],
[3, 2],
[3, 3],
[3, 3],
[3, 3],
[3, 3],
[3, 3]],10)



solution99(1,[[0, 15],
[1, 1],
[1 ,1],
[1, 1],
[1, 1],
[1, 1],
[1, 1],
[1, 1],
[1 ,1],
[1, 1]],10)



# 퀵 정렬
def quick_sort(lst, left, right):
   if left < right:
      pivot = partitionrand(lst, left, right)
      quick_sort(lst, left, pivot - 1)
      quick_sort(lst, pivot + 1, right)

# pivot 뽑기
def partitionrand(lst, left, right):
   import random
   rand_pivot = random.randrange(left, right) # pivot 랜덤으로 뽑기
   lst[left], lst[rand_pivot] = lst[rand_pivot], lst[left]
   return partition(lst, left, right)

def partition(lst, left, right):
   pivot = left
   i = left + 1
   
   for j in range(left + 1, right + 1):
      if lst[j] <= lst[pivot]:
         lst[i], lst[j] = lst[j], lst[i]
         i = i + 1
   lst[pivot], lst[i - 1] = lst[i - 1], lst[pivot]
   pivot = i - 1
   return pivot

def closest_sum(lst, n, S):
    result_l, result_r = 0, 0
    quick_sort(lst, 0, len(lst)-1)
    # 리스트 내에 이미 S보다 큰수는 제외 한다.
    lst = [lst[i] for i in range(len(lst)) if lst[i] < S]
    left, right= 0, len(lst)-1
    st = {}
    left = right-1
    while right != 0:
        pair = lst[left] + lst[right]
        if (S >= pair):
            # if right-left <= 3:
            #     break
            if pair not in st:
                st[pair] = []
                st[pair].append([left, right])
            else:
                st[pair].append([left, right])
            right -= 1
            left = right - 1
        else:
            left -= 1
    temp = list(st.keys())
    quick_sort(temp, 0, len(temp)-1)
    result_l = st[temp[-1]][0][0]
    result_r = st[temp[-1]][0][1]
    return lst[result_l], lst[result_r]


lst = [ 13426, 264100,
13426, 26478, 17122, 23488, 13863, 988, 24625, 9799, 121, 29555, 16641, 9041,
8228,
28752, 22030, 25473, 31447, 17081, 6805 ,14568, 3813 ,20991 ,
29103, 28436 ,23357, 15529, 28125, 17481, 924, 15310 ,14052, 2062, 1281,
 21955 ,475 ,747 ,3682, 9207, 20354 ,2930 ,20893,
  12314, 25813 ,27772, 24753, 11397, 12769, 181, 27438, 3030, 6871, 10075, 28650,
   15322, 22367 ,30274 ,14070 ,1969 ,23598, 19740, 10192 ,25900 ,731, 11767, 20442,
    12666, 25582, 32519, 11531, 8452 ,5947 ,6566, 4325, 26261 ,20078 ,
    19097, 12199, 21950, 32230, 10133, 12227, 1145, 1991, 24065, 19858, 12300, 7498, 24318,
     26439, 26928, 19032, 3237, 1314, 19315, 24408, 19599, 12774, 17371, 11589, 9115 ]
import time
start = time.time()  # 시작 시간 저장
x, y = closest_sum(lst, 100, 51281)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
print(x, y)
print(x+y)


lst = [200, 190, 18,
20,
200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
start = time.time()  # 시작 시간 저장
x, y = closest_sum(lst, 20, 214)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
print(x, y)
print(x+y)

