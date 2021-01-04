def solution(n):
    res = [0, 1]
    if n >= 2:
        for i in range(2, n + 1):
            fibo = (res[i - 1] + res[i - 2]) % 1234567
            res.append(fibo)

    return res[n]


print(solution(5))