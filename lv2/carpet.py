def solution(brown, yellow):
    answer = []
    area = brown + yellow
    divisors = get_divisor(area)
    for i in range(len(divisors)):
        if (divisors[i][0] - 2) * 2 + divisors[i][1] * 2 == brown:
            answer = divisors[i]

    return answer


def get_divisor(n):
    divisors = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0 and (i != 1 and i != 2):
            arr = []
            arr.append(n // i)
            arr.append(i)
            divisors.append(arr)

    return divisors


print(solution(24, 24))