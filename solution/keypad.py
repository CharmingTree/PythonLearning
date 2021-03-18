from typing import Dict
import copy
def solution(numbers, hand):
    
    answer = []
    # 123
    # 456
    # 789
    # *0#
    left = {
    1 : [2,4],
    2 : [1,5],
    4 : [1,5,7],
    5 : [2,4,8],
    7 : [-1,4,8],
    8 : [5,7,0],
    -1 : [7,0],
    0 : [-1,8]   
    }
    right = {
        2 : [3,5],
        3 : [2,6],
        5 : [2,6,8],
        6 : [3,5,9],
        8 : [5,9,0],
        9 : [-2,6,8],
        0 : [-2,8],
        -2 : [0,9]
    }
    left_min = 0
    right_min = 0
    current_left = -1
    current_right = -2
    for i in range(len(numbers)):
        left_dist = []
        right_dist = []

        #print(current_left," : ",left_min,", ", current_right, " : ", right_min) 
        if numbers[i] not in left.keys():
            answer.append("R")
            current_right = numbers[i]
            continue
        if numbers[i] not in right.keys():
            answer.append("L")
            current_left = numbers[i]
            continue

        
        path2(left, [], current_left, numbers[i], 0, left_dist)
        path2(right, [], current_right, numbers[i], 0, right_dist)

        left_min = min(left_dist) #if len(left_dist) != 0 else left_min
        right_min = min(right_dist) #if len(right_dist) != 0 else right_min
        
        if current_left == numbers[i]:
            answer.append('L')
        elif current_right == numbers[i]:
            answer.append('R')
        # if i != 0 and numbers[i-1] == numbers[i]:
        #     if hand == 'left':
        #         answer.append(answer[-1])
        #         current_left = numbers[i]
        #     else:
        #         answer.append(answer[-1])
        #         current_right = numbers[i]
        #     continue
        elif left_min == right_min:
            if hand == 'left':
                answer.append("L")
                current_left = numbers[i]
            else:
                answer.append("R")
                current_right = numbers[i]
        elif left_min < right_min:
            answer.append("L")
            current_left = numbers[i]
        else:
            answer.append("R")
            current_right = numbers[i]
    
    print(current_left, current_right)
    return ''.join(answer)

def path2(graph, p : list, start, end, dist, distance : list):
    p.append(start)
    
    dist += 1
    
    if p[-1] == end:
        dist -= 1
        distance.append(dist)
        return
    if end in graph[p[-1]]:
        p.append(end)
        distance.append(dist)
        return
    else:
        for i in graph[p[-1]]:
            if i not in p:
                path2(graph, copy.copy(p), i, end, dist, distance)