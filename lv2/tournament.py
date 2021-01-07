# 조금 까다로웠던 문제 > 다시 복습해보기 , 재귀로 표현할 수 있는지 확인하기!


def solution(n, a, b):
    counts = 0
    trigger = True
    start = 0
    end = n
    if a > b:
        a, b = b, a

    while trigger:
        mid = (start + end) // 2
        if a > start and a <= mid and b > mid and b <= end:
            counts = solve(n)
            trigger = False
        else:
            n //= 2
            if a <= mid:
                end = mid
                mid = (start + mid) // 2
            else:
                start = mid
                mid = (mid + end) // 2
    return counts


# 거듭제곱 구하는 함수. n은 2의 거듭제곱 꼴로 나타낸다.
def solve(n):
    if n == 1:
        a = 0
    else:
        a = 1 + solve(n // 2)
    return a


print(solution(8, 2, 3))