def solution(array : list, commands : list):
    answer = []

    for c in range(len(commands)):
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]

        splits = array[i-1:j]
        splits = sorted(splits)
        answer.append(splits[k-1])

    print(answer)
    return answer


solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])