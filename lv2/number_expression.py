def solution(n):
    i = 1
    sum_val = 0
    counter = 0
    while i <= n:
        for j in range(i, n + 1):
            sum_val += j
            if sum_val > n:
                i += 1
                sum_val = 0
                break
            elif sum_val == n:
                counter += 1
                sum_val = 0
                i += 1
                break

    return counter


print(solution(15))