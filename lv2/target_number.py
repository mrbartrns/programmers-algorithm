"""
numbers	           target	return
[1, 1, 1, 1, 1]	     3	       5
"""


def solution(numbers, target):
    i = 0
    current = 0
    res = [0]
    solve(numbers, target, i, current, res)
    answer = res[0]
    return answer


def solve(numbers, target, i, current, res):
    if current == target and i == len(numbers):
        res[0] += 1
        return
    else:
        if i < len(numbers):
            solve(numbers, target, i + 1, current + numbers[i], res)
            solve(numbers, target, i + 1, current - numbers[i], res)


numbers = [1, 1, 1, 1, 1]
target = 3
i = 0
current = 0
res = [0]
solve(numbers, target, i, current, res)
print(res)