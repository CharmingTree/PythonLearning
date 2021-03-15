def solution(s):
    answer = True
    
    p_cnt = 0
    y_cnt = 0

    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P' : p_cnt += 1
        if s[i] == 'y' or s[i] == 'Y' : y_cnt += 1


    return False if p_cnt != y_cnt else True


print(solution('a'))

print("".join(sorted("Zbcdefg", reverse=True)))

