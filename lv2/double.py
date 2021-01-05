def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return 1 if not stack else 0


print(solution("cdcd"))
