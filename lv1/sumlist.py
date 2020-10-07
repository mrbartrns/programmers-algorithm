def solution(n):
    answer = []
    flag = True
    while flag:
        if n // 10 == 0:
            answer.append(n % 10)
            flag = False
        else:
            r = n % 10
            d = n // 10
            n = d
            answer.append(r)
    return answer

print(solution(12345))