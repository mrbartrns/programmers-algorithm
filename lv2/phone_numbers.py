"""
def solution(phone_book):
    answer = True
    sorted_phone_book = merge_sort(phone_book)
    # for 문을 두개 쓰지 않고 해결하는 방법?
    # for i in range(len(sorted_phone_book) - 1):
    #     for j in range(i + 1, len(sorted_phone_book)):
    #         if (
    #             sorted_phone_book[i]
    #             == sorted_phone_book[j][: len(sorted_phone_book[i])]
    #         ):
    #             answer = False
    #             break

    minimum_length = len(sorted_phone_book[0])
    for i in range(len(sorted_phone_book)):
        sorted_phone_book[i] = int(sorted_phone_book[i][:minimum_length])

    int_book = int_sort(sorted_phone_book)

    for i in range(len(int_book)):
        left = int_book[:i]
        right = int_book[i + 1 :]
        left_bool, right_bool = False, False
        if left:
            left_bool = bisection_search(left, int_book[i])
        if right:
            right_bool = bisection_search(right, int_book[i])

        if left_bool or right_bool:
            answer = False
            break

    return answer


def merge_sort(arr):
    if len(arr) <= 1:
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
        if len(left[i]) < len(right[j]):
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


def int_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = int_sort(arr[:mid])
        right = int_sort(arr[mid:])
        return int_merge(left, right)


def int_merge(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


def bisection_search(arr, n):
    mid = len(arr) // 2
    if len(arr) < 2:
        if arr[mid] == n:
            return True
        else:
            return False
    else:
        if arr[mid] == n:
            return True
        else:
            if n < arr[mid]:
                return bisection_search(arr[:mid], n)
            else:
                return bisection_search(arr[mid:], n)


phone_book1 = ["119", "12", "97674223", "1195524421"]
# print(solution(phone_book1))
print(sorted(phone_book1))
phone_book2 = ["123", "456", "789"]
# print(solution(phone_book2))


phone_book3 = ["12", "123", "1235", "567", "88"]
print(solution(phone_book3))
# print(bisection_search(phone_book3, "88"))
"""


    def solution(phone_book):
        answer = True
        phone_book.sort()
        for i in range(len(phone_book) - 1):
            if phone_book[i] == phone_book[i + 1][: len(phone_book[i])]:
                answer = False
                break
        return answer


phone_book1 = ["119", "12", "97674223", "1195524421"]
print(solution(phone_book1))

p