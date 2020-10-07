def solution(s):
    '''
    s: input, string (small and big alphabet included)
    output: ordered string
    '''
    answer = ''
    temp = []
    for c in s:
        temp.append(c)
    temp.sort()
    for i in range(len(temp)):
        answer += temp[len(temp) - 1 - i]

    return answer

print(solution('Zbcdefg'))