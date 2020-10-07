def solution(s, n):
    answer = ''
    for c in s:
        if c != ' ':
            if (ord(c) >= ord('a') and ord(c) <= ord('z')) and ord(c) + n > ord('z'):
                answer += chr(ord(c) + n - 26)
            elif (ord(c) >= ord('A') and ord(c) <= ord('Z')) and ord(c) + n > ord('Z'):
                answer += chr(ord(c) + n - 26)
            else:
                answer += chr(ord(c) + n)
        else:
            answer += c
    return answer

print(solution('z b', 1))