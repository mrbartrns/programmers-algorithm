def solution(participant, completion):
    answer = ''
    # sort하면 시간절약이 가능
    participant.sort() # [a, a, b]
    completion.sort() # [a, b]
    print(participant)
    print(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            answer = participant[len(participant) - 1]
    return answer

part = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
comp = ['josipa', 'filipa', 'marina', 'nikola']
print(solution(part, comp))