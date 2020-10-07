def solution(n):
    m = n + 1
    sieve = [True] * m
    for i in range(2, int(n ** (1 / 2) + 1)):
        if sieve[i] == True:
            for j in range(i + i, m, i):
                sieve[j] = False
    prime = [i for i in range(2, m) if sieve[i] == True]
    answer = len(prime)
    return answer

print(solution(10))