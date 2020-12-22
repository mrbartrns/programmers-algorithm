def solution(n):
    if n != 0:
        if n % 3 == 1:
            string = "1"
        elif n % 3 == 2:
            string = "2"
        elif n % 3 == 0:
            string = "4"
        if n % 3 != 0:
            string = solution(n // 3) + string
        else:
            string = solution((n // 3) - 1) + string
        return string
    return ""


print(solution(500000000))