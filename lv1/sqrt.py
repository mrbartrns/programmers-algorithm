def solution(n):
    temp = n ** (1 / 2)
    if temp - int(temp) == 0:
        return int((temp + 1) ** 2)
    else:
        return -1

print(solution(121))