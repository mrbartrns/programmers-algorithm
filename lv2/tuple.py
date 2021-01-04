"""
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	[111, 20]
"{{123}}"	[123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]
"""


def solution(s):
    answer = []
    s = s[1:-1]
    raw_arr = make_arr(s)
    arr = merge_sort(raw_arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in answer:
                answer.append(arr[i][j])
    return answer


def make_arr(s):
    arr = []
    temp = []
    number = ""
    for i in range(len(s)):
        if s[i] == "{":
            temp = []
        elif s[i] in "0123456789":
            number += s[i]
        elif s[i] == "," and s[i - 1] != "}":
            temp.append(int(number))
            number = ""
        elif s[i] == "}":
            if number:
                temp.append(int(number))
                number = ""
            arr.append(temp)
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if len((left[i])) < len(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


a = "{{20,111},{111}}"
print(solution(a))