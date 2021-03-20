def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmp_bi = bin(arr1[i]|arr2[i])[2:].zfill(n)
        tmp_list = []
        print(tmp_bi)
        for j in range(len(tmp_bi)):
            if tmp_bi[j] == '1':
                tmp_list.append('#')
            else:
                tmp_list.append(' ')
        answer.append(''.join(tmp_list))

    return answer




solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])