def solution(prices):
    answer = []

    cnt = 0
    end = len(prices) - 1
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                answer.append(cnt+1)
                cnt = 0
                break
            if j == end:
                answer.append(cnt)
                cnt = 0

    answer.append(0)        
    print(answer)
    return answer

def solution2(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        print(i , 'i= ',p[i],' < stack[-1]= ', p[stack[-1]], '    ', stack)
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                print(p[i], p[j])
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    print(stack)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans

print(solution2([5, 1,1, 1, 1]))