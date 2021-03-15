def solution(s : str):
    answer = ''
    slen = len(s)
    if slen <= 2:
        return s
    elif slen % 2 == 0:
        mid = slen//2-1
        answer = s[mid]+s[mid+1]
    else:
        answer = s[slen//2]

    return answer


print(solution("qwer"))