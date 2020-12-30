def solution(s):
    answer = 0
    length = 1

    while length <= len(s):
        compacted = ""
        prev = ""
        temp = 0
        pattern = ""
        for i in range(0, len(s), length):
            pattern = s[i : i + length]
            if len(pattern) == length:

                if prev != "" and prev != pattern:
                    compacted += str(temp) + prev if temp > 1 else prev
                    temp = 0
                else:
                    temp += 1

                prev = pattern
            else:
                compacted += pattern
        length += 1
        if length == 2:
            break
    return answer


print(solution("string"))
"""
def solution(s):
    answer = 0
    # 맨 앞부터 1씩 늘려나가면서 패턴의 길이 수를 늘린다.
    length = 1
    while length <= len(s):
        patterns = []
        compacted = ""
        for i in range(0, len(s), length):
            pattern = s[i : i + length]
            if pattern not in patterns:
                patterns.append(pattern)
                kmp_value = kmp(s, pattern)
                compacted += str(kmp_value) + pattern if kmp_value != 1 else pattern
        print(compacted)
        if answer == 0 or answer > len(compacted):
            answer = len(compacted)

        length += 1

    return answer


def kmp(t, p):
    n = len(t)
    m = len(p)
    begin = 0
    matched = 0
    res = 0
    f = failure_function(p)
    while begin <= n - m:
        if matched < m and t[begin + matched] == p[matched]:
            matched += 1
            if matched == m:
                res += 1

        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched + f[matched - 1]
                matched = f[matched - 1]
                if res != 0:
                    return res
    return res


def failure_function(p):
    m = len(p)
    begin = 0
    matched = 0
    f = [0 for _ in range(m)]
    while begin + matched < m:
        if p[begin + matched] == p[matched]:
            matched += 1
        else:
            if begin == 0:
                begin += 1
            else:
                begin += begin + f[matched - 1]
                matched = f[matched - 1]
    return f


print(kmp("aabbaccc", "a"))
"""