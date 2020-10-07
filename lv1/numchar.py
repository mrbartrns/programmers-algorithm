def solution(s):
    answer = True
    print(len(s))
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if ord(c) < 48 or ord(c) > 57:
                answer = False
                break
    else:
        return False
    return answer

print(solution('1234'))