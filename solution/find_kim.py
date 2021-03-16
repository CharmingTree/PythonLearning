def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return '김서방은 {}에 있다'.format(i)


print(solution(['Kim','Ugn']))

nums = '1234'
if (len(nums) == 4 or len(nums) == 6) and nums.isnumeric:
    True
else:
    False