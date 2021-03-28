def solution(genres, plays):
    answer = []

    map = {}

    index = 0
    for i, j in zip(genres, plays):
        if i not in map:
            map[i] = []
            map[i].append([index, j])
        else:
            map[i].append([index, j])
        index += 1
    
    map = dict(sorted(map.items(), key= lambda x : sum(x[1][1]), reverse=True))

    for i in map.keys():
        map[i].sort(key=lambda x : x[1], reverse=True)

    for i,j in map.items():
        print(len(j))
        if len(j) == 1:
            answer.append(j[0][0])
        else:
            for k in range(2):
                answer.append(j[k][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))