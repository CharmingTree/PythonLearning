def solution(s : list):

    mapping = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    
    answer = []

    while len(s) > 0:
        if s[0].isnumeric():
            answer.append(s[0])

            
            s = list(s)
            s.pop(0)
        else:
            for i in range(10):
                isMapping = True
                if len(s) >= len(mapping[i]):
                    for j in range(len(mapping[i])):
                        if s[j] != mapping[i][j]:
                            isMapping = False
                            break
                    if isMapping:
                        s = s[len(mapping[i]):]
                        s = list(s)
                        answer.append(str(i))


    
    return int(''.join(answer))


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))