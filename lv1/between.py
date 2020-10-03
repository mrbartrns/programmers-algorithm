def solution(a, b):
    answer = 0
    arr = [a, b]
    arr.sort()
    for i in range(arr[0], arr[1] + 1):
        answer += i

    return answer

print(solution(3, 3))