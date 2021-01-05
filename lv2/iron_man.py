# greedy 알고리즘


def solution(n):
    ans = solve(n)
    return ans


def solve(n):
    if n == 0:
        return 0
    else:
        ans = 0
        if n % 2 == 1:
            ans = 1
        ans += solve(n // 2)
        return ans


print(solve(5000))