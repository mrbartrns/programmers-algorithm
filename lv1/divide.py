def solution(arr, divisor):
    arr.sort()
    answer = [i for i in arr if i % divisor == 0]
    if len(answer) == 0:
        answer.append(-1)
    return answer

print(solution([3, 2, 6], 10))
print(solution)