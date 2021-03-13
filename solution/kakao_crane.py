def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for b in board:
            print(stack)
            if b[m-1] == 0:
                continue
            else:
                if len(stack) > 0:
                    print('last ', stack[-1], 'b[m-1] ', b[m-1])
                    if stack[-1] == b[m-1]:
                        print("pop ", stack[-1])
                        answer += 2
                        stack.pop()
                        b[m-1] = 0
                        break
                    else:
                        stack.append(b[m-1])
                        b[m-1] = 0
                        break
                else:
                    stack.append(b[m-1])
                    b[m-1] = 0
                    break
    
    #print(stack)


    return answer


l = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]	

re = solution(l, m)

print(re)