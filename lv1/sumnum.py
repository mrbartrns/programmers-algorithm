def solution(n):
    answer = 0
    flag = True
    while flag:
        if n // 10 == 0:
            answer += n % 10
            flag = False
        else:
            r = n % 10
            d = n // 10
            n = d
            answer += r
    return answer

print(solution(123))