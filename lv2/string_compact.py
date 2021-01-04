def solution(s):
    answer = 0
    arr = solve(s)
    arr.sort(key=lambda x: len(x))
    answer = len(arr[0])
    return answer


def solve(s):
    arr = []
    for i in range(1, len(s) + 1):
        stack = []
        string = ""
        counter = 1
        for j in range(0, len(s), i):
            if not stack:
                stack.append(s[j : j + i])
            else:
                if stack[-1] == s[j : j + i]:
                    counter += 1
                else:
                    string += str(counter) + stack[-1] if counter != 1 else stack[-1]
                    stack.append(s[j : j + i])
                    counter = 1
        string += str(counter) + stack[-1] if counter != 1 else stack[-1]
        if string not in arr:
            arr.append(string)
    return arr


# print(solve("ababcdcdababcdcd"))
print(solution("xababcdcdababcdcd"))
