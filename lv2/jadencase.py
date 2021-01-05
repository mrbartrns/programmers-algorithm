def solution(s):
    ord_a = 97
    delta = 25
    ord_A = 65
    BETWEEN = 32
    answer = ""
    if ord(s[0]) >= ord_a and ord(s[0]) <= ord_a + delta:
        answer += chr(ord(s[0]) - BETWEEN)
    else:
        answer += s[0]
    for i in range(1, len(s)):
        if s[i - 1] == " " and ord(s[i]) >= ord_a and ord(s[0]) <= ord_a + delta:
            answer += chr(ord(s[i]) - BETWEEN)
        elif s[i - 1] != " " and ord(s[i]) >= ord_A and ord(s[i]) <= ord_A + delta:
            answer += chr(ord(s[i]) + BETWEEN)
        else:
            answer += s[i]
    return answer


print(solution("3people unFollowed me"))
