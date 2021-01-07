# 끝말잇기 규칙
"""
이전 단어의 마지막 문자로 시작하는 단어를 사용해야 함
이전에 이미 사용됬던 단어를 사용해서는 안됨
> 불리언 딕셔너리 사용?
"""


def solution(n, words):
    answer = [0, 0]
    dict_bool = {}
    for i in range(len(words)):
        dict_bool[words[i]] = dict_bool.get(words[i], False)
        if i > 0:
            if words[i - 1][-1] != words[i][0]:
                answer[0] = (i % n) + 1
                answer[1] = (i // n) + 1
                return answer
        if dict_bool[words[i]]:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            return answer
        dict_bool[words[i]] = True
    return answer


# n = 3
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n = 5
words = [
    "hello",
    "observe",
    "effect",
    "take",
    "either",
    "recognize",
    "encourage",
    "ensure",
    "establish",
    "hang",
    "gather",
    "refer",
    "reference",
    "estimate",
    "executive",
]
print(solution(n, words))