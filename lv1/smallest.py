def solution(arr):
    answer = []
    index = 0
    if len(arr) <= 1:
        answer = [-1]
        return answer
    else:
        for i in range(len(arr)):
            if arr[index] > arr[i]:
                index = i
        del arr[index]
        answer = arr
    return answer

print(solution([4, 3, 2, 1]))