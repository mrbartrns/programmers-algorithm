"""
후보키 구하기
후보키는 다음과 같은 규칙을 만족
유일성, 최소성
"""


def solution(relation):
    answer = 0
    keys = make_keys(len(relation[0]))
    print(keys)
    unique = [False] * len(relation[0])
    for i in range(len(keys)):
        temp = []
        for k in range(len(keys[i])):
            category = keys[i][k]
            if unique[category]:
                break
            else:
                for j in range(len(relation)):
                    temp.append(relation[j][category])
                    print(relation[j][category], end=" ")  # 이 표현 잘 익혀두기
                print()
        print()

    return answer


def make_keys(n):
    arr = [i for i in range(n)]
    result = []
    for i in range(1 << len(arr)):
        temp = []
        for j in range(len(arr)):
            if i & (1 << j):
                temp.append(arr[j])
        if temp:
            result.append(temp)
    result.sort(key=lambda x: len(x))
    return result


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]

solution(relation)