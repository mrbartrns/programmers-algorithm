def solution(progresses: list, speeds: list) -> list:
    answer = []
    while progresses:
        flag = False
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        counts = 0
        temp_idx = 0
        for j in range(len(progresses)):
            if progresses[j] >= 100:
                counts += 1
                temp_idx = j
                flag = True
            else:
                break
        if flag:
            answer.append(counts)
            for _ in range(temp_idx + 1):
                progresses.pop(0)
                speeds.pop(0)
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))