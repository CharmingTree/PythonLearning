# _, -, . 특수문자 사용가능 단, .은 처음과 끝 사용 불가 
# 1. 모두 소문자
# 알파벳, 숫자, -, _, . 를 제외한 모든 문자 제거
# 마침표 . 가 연속될경우 한개로 치환
# .가 처음이나 맨끝에 존재시 제거
# new_id가 empty then 'a'대입
# new_id가 16자 이상일경우 15까지 허용, 나머지 제거
# 위 필터후 맨앞/맨끝에 . 존재시 제거
# new_id가 2자 이하일경우 마지막 문자를 길이가 3이될때까지 append
import re

def solution(new_id : list):
    answer = ''

    new_id = new_id.lower()

    #print('lower >> ', new_id)

    new_id = re.sub("[^a-z0-9|.|_|-]", "", new_id)

    #print("특수문자 제거 >> ",new_id)
    
    new_id = re.sub("[.]+", ".", new_id)

    #print("마침표 한개로 치환 >> ", new_id)

    new_id = list(new_id)

    if new_id[0] == '.':
        new_id.pop(0)
    
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id.pop(-1)

    #print("맨 앞/뒤에 마침표 존재시 제거 >> ", new_id)

    if len(new_id) == 0:
        #print("빈 문자열일 경우 a 대입 >> ", new_id)
        new_id = list('a')

    if (len(new_id) > 15):
        new_id = new_id[0:15]

    #print('16자 이상일 경우 15이하로 치환 >> ', new_id)

    

    if len(new_id) != 0 and new_id[0] == '.':
        new_id.pop(0)
    
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id.pop(-1)

    #print("맨 앞/뒤에 마침표 존재시 제거 >> ", new_id)

    if len(new_id) <= 2:
        for i in range(3):
            new_id.append(new_id[-1])
            #print(new_id)
            if len(new_id) >= 3:
                break
    
    #print("2자 이하일 경우 3자까지 마지막 문자 append >> ", new_id)

    answer = ''.join(new_id)

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))