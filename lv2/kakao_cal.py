import operator


def solution(expression):
    # PRIORITY = {"*": 1, "+": 3, "-": 2}
    # OPERATOR = ["(", "+", "-", "*", "/", ")"]

    OPERATOR = []
    arr = []
    temp = []
    res = []
    answer = 0
    for c in expression:
        if c == "*" or c == "+" or c == "-":
            if c not in OPERATOR:
                OPERATOR.append(c)
    n = len(OPERATOR)
    flags = [False] * (n + 1)
    get_arr(n, flags, arr, temp)
    for i in range(len(arr)):
        PRIORITY = {}
        for j in range(len(arr[0])):
            PRIORITY[OPERATOR[j]] = PRIORITY.get(OPERATOR[j], arr[i][j])
        val = calc(postfix(expression, PRIORITY, OPERATOR), OPERATOR)
        res.append(val)
    res.sort()
    answer = res[-1]
    return answer


def postfix(string, PRIORITY, OPERATOR):
    res = []
    stack = []
    temp = ""
    for c in string:
        if c in PRIORITY:
            if temp:
                res.append(temp)
                temp = ""
            while PRIORITY[c] <= (PRIORITY[stack[-1]] if stack != [] else -1):
                op = stack.pop()
                res.append(op)
            stack.append(c)
        else:
            temp += c
    res.append(temp)
    temp = ""
    while stack:
        op = stack.pop()
        res.append(op)
    return res


def get_eval(op, num1, num2):
    return get_operator(op)(num1, num2)


def calc(arr: list, OPERATOR) -> int or float:
    stack = []
    for c in arr:
        if c not in OPERATOR:
            stack.append(int(c))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            val = get_eval(c, num1, num2)
            stack.append(val)
    res = stack.pop()
    return abs(int(res)) if int(res) == float(res) else abs(float(res))


def get_operator(op: str):
    return {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }[op]


def get_arr(n, flags, arr, temp):
    if len(temp) == n:
        arr.append(temp[:])
    else:
        for i in range(1, n + 1):
            if not flags[i]:
                flags[i] = True
                temp.append(i)
                get_arr(n, flags, arr, temp)
                temp.pop()
                flags[i] = False


print(solution("100-200*300-500+20"))