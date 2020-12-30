# def solution(p):
#     answer = ""
#     return answer


def solution(w):
    if w == "":
        return ""
    else:
        left_braket = 0
        right_braket = 0
        idx = -1
        for i in range(len(w)):
            if w[i] == "(":
                left_braket += 1
            elif w[i] == ")":
                right_braket += 1

            if left_braket == right_braket:
                idx = i
                break
        u = w[: idx + 1]
        v = w[idx + 1 :]
        if check(u):
            string = u + solution(v)
            return string
        else:
            string = "("
            string += solution(v)
            string += ")"
            u = u[1:-1]
            new_u = ""
            for i in range(len(u)):
                if u[i] == "(":
                    new_u += ")"
                else:
                    new_u += "("
            string += new_u
            return string


def check(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if s[i] == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        return True
    else:
        return False


print(solution("()))((()"))
