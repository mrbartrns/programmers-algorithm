# least common multiple

"""
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
"""
from functools import reduce


def solution(arr):
    lcms = solve(arr)
    answer = reduce(lambda acc, cur: acc * cur, lcms, 1)
    return answer


def solve(arr):
    arr.sort()
    flag = True
    is_lcm = False
    lcms = []
    i = 2
    while flag:
        while i <= arr[-1]:
            val = i
            for j in range(len(arr)):
                if arr[j] % i == 0:
                    is_lcm = True
                    val = i
                    arr[j] = arr[j] // i
            if is_lcm:
                lcms.append(val)

            one_count = 0
            for k in range(len(arr)):
                if arr[k] == 1:
                    one_count += 1
                else:
                    break
                if one_count == len(arr):
                    flag = False
                    break
            if is_lcm:
                i = 2
                is_lcm = False
            else:
                i += 1
            arr.sort()

    return lcms


arr = [3, 4, 9, 16]
# arr = [2, 6, 8, 14]
print(solution(arr))