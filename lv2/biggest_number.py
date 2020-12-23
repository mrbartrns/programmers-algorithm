"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수 찾기
백트래킹으로 문제를 풀 경우 시간초과가 남 > log n의 방법이 필요
"""
# 배열의 순서를 내 맘대로 정할 수 있어야 하는 것이 키 포인트
def solution(numbers):
    tf = [False] * len(numbers)
    string = []
    ans = []
    search(numbers, tf, string, ans)
    ans.sort()
    answer = str(ans[-1])
    return answer


def search(arr, tf, string, ans):
    for i in range(len(arr)):
        if not tf[i]:
            tf[i] = True
            string.append(str(arr[i]))
            search(arr, tf, string, ans)
            tf[i] = False
            if len(string) == len(arr):
                temp = ""
                for c in string:
                    temp += c
                ans.append(int(temp))
            string.pop()


numbers = [40, 403]
print(solution(numbers))