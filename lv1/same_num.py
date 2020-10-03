def solution(arr):
    answer = []
    temp = arr[0]
    for i in range(len(arr)):
        if temp != arr[i] or len(answer) == 0:
            temp = arr[i]
            answer.append(temp)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([1, 1, 1, 0, 1]))