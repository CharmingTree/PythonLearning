def solution(phone_book):
    answer = True

    s = set(phone_book)

    if len(s) != len(phone_book):
        return False
    phoneMap = {}
    for i in range(len(phone_book)):
        if phone_book[i][0] not in phoneMap:
            phoneMap.setdefault(phone_book[i][0], [phone_book[i]])
        else:
            phoneMap.get(phone_book[i][0]).append(phone_book[i])
    
    for i in phoneMap.keys():
        phoneMap.get(i).sort()
        #print(phoneMap[i])
        for j in range(len(phoneMap[i])-1):
            if phoneMap[i][j+1].startswith(phoneMap[i][j]):
                return False
    return answer



print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["123","456","789","1111","111","11","1"]))




def solution2(phone_book):
    answer = True

    s = set(phone_book)

    if len(s) != len(phone_book):
        return False

    #phone_book = sorted(phone_book)

    phoneMap = {}

    for i in range(len(phone_book)):
        if phone_book[i][0] not in phoneMap:
            phoneMap.setdefault(phone_book[i][0], [phone_book[i]])
        else:
            phoneMap.get(phone_book[i][0]).append(phone_book[i])
    
    for i in phoneMap.keys():
        phoneMap.get(i).sort()
        #print(phoneMap[i])
        for j in range(len(phoneMap[i])):

            for k in range(len(phoneMap[i])):
                if len(phoneMap[i][j]) != len(phoneMap[i][k]) and phoneMap[i][j].startswith(phoneMap[i][k]):
                    return False
                if len(phoneMap[i][j]) != len(phoneMap[i][k]) and phoneMap[i][k].startswith(phoneMap[i][j]):
                    return False
    return answer

