# use merge sort
def solution(numbers):
    answer = ""
    arr = merge_sort(numbers)
    for i in arr:
        answer += str(i)
    return answer if answer[0] != "0" else "0"


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        left_string = str(left[i])[0]
        right_string = str(right[j])[0]
        if int(left_string) > int(right_string):
            res.append(left[i])
            i += 1
        elif int(left_string) < int(right_string):
            res.append(right[j])
            j += 1
        else:
            if int(str(left[i]) + str(right[j])) > int(str(right[j]) + str(left[i])):
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


# arr = [40, 403]
# arr = [6, 10, 2]
# arr = [3, 30, 34, 5, 9]
# arr = [1, 11, 111, 1111]
# arr = [0, 5, 10, 15, 20]
# arr = [1000, 0, 5, 99, 100]
arr = [0, 0, 0, 0]
print(solution(arr))