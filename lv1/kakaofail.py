def solution(n, stages):
    answer = []
    temp = {}
    stages.sort()
    tot = len(stages)
    for i in range(1, n + 1):
        current = stages.count(i)
        if tot == 0:
            failRate = 0
        else:
            failRate = current / tot
        temp[f'{i}'] = failRate
        tot -= current
    temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(temp)):
        answer.append(int(temp[i][0]))
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [3, 3, 3, 3, 3]))