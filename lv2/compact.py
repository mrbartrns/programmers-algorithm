def solution(arr):
    answer = [0, 0]
    res = solve(arr)
    for i in range(len(res)):
        if res[i][0] == 0:
            answer[0] += 1
        elif res[i][0] == 1:
            answer[1] += 1
    return answer


def solve(arr):
    if len(arr) == 1:
        return arr
    else:
        flag = check(arr)
        if flag != -1:
            arr = [[flag]]
            return arr
        else:
            splited_arr = split_arr(arr)
            p1 = splited_arr[0]
            p2 = splited_arr[1]
            p3 = splited_arr[2]
            p4 = splited_arr[3]
            arr = solve(p1) + solve(p2) + solve(p3) + solve(p4)
            return arr


def check(arr):
    num = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != num:
                return -1
    return num


def split_arr(arr):
    p1, p2, p3, p4 = [], [], [], []
    for i in range(len(arr) // 2):
        temp = []
        for j in range(len(arr) // 2):
            temp.append(arr[i][j])
        p1.append(temp)
        temp = []
        for j in range(len(arr) // 2, len(arr)):
            temp.append(arr[i][j])
        p2.append(temp)

    for i in range(len(arr) // 2, len(arr)):
        temp = []
        for j in range(len(arr) // 2):
            temp.append(arr[i][j])
        p3.append(temp)
        temp = []
        for j in range(len(arr) // 2, len(arr)):
            temp.append(arr[i][j])
        p4.append(temp)
    return [p1, p2, p3, p4]


arr1 = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
arr2 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
]


print(solution(arr2))