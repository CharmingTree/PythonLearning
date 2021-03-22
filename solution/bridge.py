def solution(bridge_length, weight, truck_weights : list):
    crossOver = []
    complete = []
    cnt = 0
    currentWeight = 0
    while len(truck_weights) > 0 or len(crossOver) > 0:
        cnt += 1
        if len(crossOver) > 0:
            for i in range(len(crossOver)):
                crossOver[i][1] -= 1
            if crossOver[0][1] == 0:
                currentWeight -= crossOver[0][0]
                complete.append(crossOver.pop(0))

        if len(truck_weights) > 0:
            if weight >= currentWeight + truck_weights[0]:
                currentWeight += truck_weights[0]
                crossOver.append([truck_weights.pop(0), bridge_length])

    return cnt


solution(2, 10, [7,4,5,6])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])
solution(1,1,[1])