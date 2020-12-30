def solution(name):
    answer = 0
    a_count = 0
    idx = -1
    not_a_count = 0
    # is_a = False
    # 이것은 갈아 치울 필요 없음
    for c in name:
        if ord(c) - ord("A") <= ord("Z") - ord(c):
            answer += ord(c) - ord("A")
            # print(ord(c) - ord("A"))
        else:
            answer += ord("Z") - ord(c) + 1
    # 여기서부터 수정 필요
    for i in range(1, len(name) + 1):
        pattern = "A" * i
        if name.find(pattern) != -1 and a_count < len(pattern):
            idx = name.find(pattern)
            not_a_count = idx
            a_count = len(pattern)
    not_a_count = idx - 1 if idx > 0 else 0
    if idx == -1:
        answer += len(name) - 1
    else:
        if a_count >= not_a_count:
            if idx == 0:
                if name[
                    len(name) - a_count : len(name)
                ] == "A" * a_count and a_count != len(name):
                    answer += len(name) - 1 - a_count
                else:
                    answer += len(name) - 1 - a_count + not_a_count + 1
            else:
                if (
                    idx + a_count == len(name)
                    and name[:a_count] != name[len(name) - a_count : len(name)]
                ):
                    answer += len(name) - 1 - a_count
                else:
                    answer += len(name) - 1 - a_count + not_a_count
        else:
            if (
                idx + a_count == len(name)
                and name[:a_count] != name[len(name) - a_count : len(name)]
            ):
                answer += len(name) - 1 - a_count
            else:
                answer += len(name) - 1

    return answer


print(solution("BBBBAA"))  # 11 13

# string = "ABABAAAAABA"
# print(string.find("AAAAA"))
"""
def solution(name):
    answer = 0
    a_count = 0
    if len(name) > 2:
        for c in name:
            if ord(c) - ord("A") <= ord("Z") - ord(c):
                answer += ord(c) - ord("A")
                # print(ord(c) - ord("A"))
            else:
                answer += ord("Z") - ord(c) + 1
                # print(ord("Z") - ord(c) + 1)
        if name[1] == "A":
            for i in range(1, len(name)):
                if name[i] == "A":
                    a_count += 1
                else:
                    break

        answer += len(name) - 1 - a_count
        return answer
"""