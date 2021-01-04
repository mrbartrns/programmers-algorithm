def solution(a, b):
    answer = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        answer += a[i] * b[len(b) - 1 - i]
    return answer


# a = [1, 4, 2]
# b = [5, 4, 4]

a = [1, 2]
b = [3, 4]

print(solution(a, b))