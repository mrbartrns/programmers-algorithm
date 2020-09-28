def solution(answers):
    '''
    input answers: []
    return answer: []
    '''
    # 가장 많이 맞춘 사람만 , 그러나 동점일때에는 오름차순으로
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    counts = [0, 0, 0]
    for i in range(len(answers)):
        if p1[i % len(p1)] == answers[i]:
            counts[0] += 1
        if p2[i % len(p2)] == answers[i]:
            counts[1] += 1
        if p3[i % len(p3)] == answers[i]:
            counts[2] += 1
    maxVal = max(counts)
    for i in range(len(counts)):
        if counts[i] == maxVal:
            answer.append(i + 1)
    return answer

a =[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5] # 4, 3, 4
print(solution(a))