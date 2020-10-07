def solution(arr):
    tot = 0
    for i in range(len(arr)):
        tot += arr[i]
    ave = int(tot / len(arr)) if tot % len(arr) == 0 else tot / len(arr)
    return ave

print(solution([5, 5]))