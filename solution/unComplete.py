
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"


import collections

def solution(participant, completion):
    answer = ''

    participant_map = {}

    

    for i in range(0,len(participant)):
        if participant[i] in participant_map:
            participant_map[participant[i]] += 1
        else:
            participant_map.setdefault(participant[i], 1)

    
    for i in range(len(completion)):
        if not completion[i] in participant_map:
            return completion[i]
        else:
            participant_map[completion[i]] -= 1

    
    for i in participant_map:
        if participant_map[i] > 0:
            return i

    print(participant_map)


def opt_sulution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]
# result =solution(["leo", "kiki", "eden"], ["eden", "kiki"])
result = opt_sulution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

print(result)