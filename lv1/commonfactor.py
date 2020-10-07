def solution(n, m):
    answer = []
    copy1 = n
    copy2 = m
    if copy1 > copy2:
        temp = copy1
        copy1 = copy2
        copy2 = temp
    while copy1 != 0:
        r = copy2 % copy1
        copy2 = copy1
        copy1 = r
    answer.append(int(copy2))
    answer.append(int((m * n) / copy2))

    return answer

print(solution(3, 12))