def solution(s):
    answer = ''
    index = 0
    for i in range(len(s)):
        if index % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        if s[i] == ' ':
            index = 0
        else:
            index += 1
    return answer

print(solution('name hi'))