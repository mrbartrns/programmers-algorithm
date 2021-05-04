import sys


def count_parings(taken):
    finished = True
    for i in range(len(taken)):
        if not taken[i]:
            finished = False
            break
    if finished:
        return 1
    ret = 0
    for i in range(len(taken)):
        for j in range(len(taken)):
            if not taken[i] and not taken[j] and friends[i][j]:
                taken[i] = taken[j] = True
                ret += count_parings(taken)
                taken[i] = taken[j] = False
    return ret


# t = int(sys.stdin.readline())
# for _ in range(t):
#     num, pairs = map(int, sys.stdin.readline().split())
#     parings = list(map(int, sys.stdin.readline().split()))
#     friends = [[False for _ in range(num)] for _ in range(num)]
#     taken = [False] * num
#     print(parings)
#     for i in range(0, len(parings), 2):
#         friends[parings[i]][parings[i + 1]] = friends[parings[i + 1]][parings[i]] = True
#     # print(friends)
#     print(count_parings(taken))

friends = [
    [False, True, True, True],
    [True, False, True, True],
    [True, True, False, True],
    [True, True, True, False],
]
taken = [False, False, False, False]
print(count_parings(taken))