"""
[1, 2, 3, 2, 3]
1보다 낮은 값이 있는지, 있으면 인덱스를 추가, 없으면 배열의 길이 - 1 - 자신의 인덱스
2보다 낮은 값이 있는지, 있으면 인덱스를 추가, 없으면 배열의 길이 -1 자신의 인덱스
"""


def solution(prices: list) -> list:
    answer = []
    for i in range(len(prices)):
        temp_idx = i
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                temp_idx = j
                break
        if temp_idx != i:
            answer.append(temp_idx - i)
        else:
            answer.append(len(prices) - i - 1)
    return answer


print(solution([1, 2, 3, 2, 3]))