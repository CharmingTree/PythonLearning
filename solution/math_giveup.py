def solution(answers):
    answer = []

    a = { 'name' : 1, 'pattern' : [1, 2, 3, 4, 5], 'idx' : 0, 'score' : 0}
    a.setdefault('len', len(a['pattern']))

    b = { 'name' : 2, 'pattern' : [2, 1, 2, 3, 2, 4, 2, 5], 'idx' : 0, 'score' : 0}
    b.setdefault('len', len(b['pattern']))

    c = { 'name' : 3, 'pattern' : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 'idx' : 0, 'score' : 0}
    c.setdefault('len', len(c['pattern']))

    for i in range(len(answers)):
        if a['idx'] == a['len']:
            a['idx'] = 0
        if b['idx'] == b['len']:
            b['idx'] = 0
        if c['idx'] == c['len']:
            c['idx'] = 0

        if answers[i] == a['pattern'][a['idx']]:
            a['score'] += 1
        if answers[i] == b['pattern'][b['idx']]:
            b['score'] += 1
        if answers[i] == c['pattern'][c['idx']]:
            c['score'] += 1
        
        a['idx'] += 1
        b['idx'] += 1
        c['idx'] += 1

    dictList = []
    dictList.append(a)
    dictList.append(b)
    dictList.append(c)

    sortedList = sorted(dictList, key=(lambda x : x['score']), reverse=True)

    answer.append(sortedList[0]['name'])

    for i in range(1,len(sortedList)):
        if sortedList[0]['score'] != sortedList[i]['score']:
            break
        else:
            answer.append(sortedList[i]['name'])
    
    return answer



solution([1,2,3,4,5])
solution([1,3,2,4,2])