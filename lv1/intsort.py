def solution(n):
    temp = []
    answer = 0
    flag = True
    while flag:
        if n // 10 == 0:
            temp.append(n % 10)
            flag = False
        else:
            r = n % 10
            d = n // 10
            n = d
            temp.append(r)
    temp.sort()
    for i in range(len(temp)):
        answer += temp[i] * (10 ** i)
    return answer

print(solution(118372))