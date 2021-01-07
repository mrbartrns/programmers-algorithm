"""
n: 진법
t: 미리 구할 숫자의 갯수
m: 게임에 참가하는 인원,
p: 튜브의 순서
"""


def solution(n, t, m, p):
    answer = ""
    string = "0"
    i = 0
    while len(string) <= t * m:
        string += solve(i, n)
        i += 1
    # print(string)
    for j in range(len(string)):
        if j % m == p - 1:
            answer += string[j]
        if len(answer) == t:
            break

    return answer


def solve(i, n):
    if i == 0:
        string = ""
    else:
        string = ""
        string += solve(i // n, n)
        if i % n > 9:
            string += chr(ord("A") - 10 + (i % n))
        else:
            string += str(i % n)
    return string


ans = solution(16, 16, 2, 2)
print(ans == "13579BDF01234567")