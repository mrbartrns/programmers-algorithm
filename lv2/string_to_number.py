def solution(s):
    arr = solve(s)
    answer = ""
    answer += str(arr[0])
    answer += " "
    answer += str(arr[-1])
    return answer


def solve(s):
    arr = list(map(lambda x: int(x), s.split(" ")))
    arr.sort()
    return arr


s = "-1 -2 -3 -4"
print(solution(s))