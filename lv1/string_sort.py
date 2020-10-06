def solution(strings, n):
    answer = []
    # strings의 n번째 index의 ord를 비교한다.
    # ord가 작은 순서대로 answer에 넣는다
    # ord가 같다면, 사전의 순서대로 오름차순한다.
    # == 완전탐색 문제와 동일!

    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if ord(strings[i][n]) > ord(strings[j][n]):
                temp = strings[i]
                strings[i] = strings[j]
                strings[j] = temp
            elif ord(strings[i][n]) == ord(strings[j][n]):
                tempList = [strings[i], strings[j]]
                tempList.sort()
                strings[i] = tempList[0]
                strings[j] = tempList[1]
        answer.append(strings[i])
    answer.append(strings[-1])

    return answer

print(solution(['abce', 'abcd', 'cdx'], 2))