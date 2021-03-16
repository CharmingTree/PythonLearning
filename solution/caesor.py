def solution(s, n):
    answer = ''
    ss = []
    for i in range(len(s)):
        if s[i] == ' ':
                ss.append(' ')
        elif 97 <= ord(s[i]) and 122 >= ord(s[i]):
            if ord(s[i])+n > 122:
                tmp = ord(s[i])+n - 122 + 96
                ss.append(chr(tmp))
            else:
                ss.append(chr(ord(s[i])+n))
        else:
            if ord(s[i])+n > 90:
                tmp = ord(s[i])+n - 90 + 64
                ss.append(chr(tmp))
            else:
                ss.append(chr(ord(s[i])+n))
    
    return ''.join(ss)


solution('ad zZ', 1)

