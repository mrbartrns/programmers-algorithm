# news clustering
"""
자카드 유사도 J(A, B) # A, B는 집합
두 집합의 교집합의 크기를 두 집합의 합집합의 크기로 나눈 값
자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장 가능

입력으로는 str1과 str2를 받음
입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합을 만듬
영문으로 이루어진 글자 쌍만 유효하고, 기타 공백이나 숫자가 들어있을 경우, 그 글자쌍은 버린다.
대문자와 소문자의 차이는 무시한다.

유사도에 65546을 곱한후 소수점은 버린다.
"""


def solution(str1, str2):
    str1_list = make_list(str1)
    str2_list = make_list(str2)
    str1_used = [False] * len(str1_list)
    str2_used = [False] * len(str2_list)
    same_count = 0
    # 교집합과 합집합 구하기
    # 실제로 구하는 것이 아닌, 겹치는 것의 갯수를 파악한다. 그리고 총 갯수에다가 교집합의 수를 빼 합집합을 구한다.
    # 두 배열이 빈 배열일 경우, 1을 반환한다.
    if str1_list or str2_list:
        for i in range(len(str1_list)):
            for j in range(len(str2_list)):
                if (
                    not str1_used[i]
                    and not str2_used[j]
                    and str1_list[i] == str2_list[j]
                ):
                    same_count += 1
                    str1_used[i], str2_used[j] = True, True
        sum_count = len(str1_list) + len(str2_list) - same_count
        answer = int((same_count / sum_count) * 65536)
    else:
        answer = 1 * 65536
    return answer


def make_list(string):
    ord_a = 97
    ord_A = 65
    delta = 25
    between = 32
    arr = []
    for i in range(len(string) - 1):
        if (
            (ord(string[i]) >= ord_a and ord(string[i]) <= ord_a + delta)
            or (ord(string[i]) >= ord_A and ord(string[i]) <= ord_A + delta)
        ) and (
            (ord(string[i + 1]) >= ord_a and ord(string[i + 1]) <= ord_a + delta)
            or (ord(string[i + 1]) >= ord_A and ord(string[i + 1]) <= ord_A + delta)
        ):
            peice = ""
            peice += (
                string[i]
                if ord(string[i]) >= ord_a and ord(string[i]) <= ord_a + delta
                else chr(ord(string[i]) + between)
            )
            peice += (
                string[i + 1]
                if ord(string[i + 1]) >= ord_a and ord(string[i + 1]) <= ord_a + delta
                else chr(ord(string[i + 1]) + between)
            )
            arr.append(peice)
    arr.sort()
    return arr


str1 = "e=m*c^2"
str2 = "e=m*c^2"
print(solution(str1, str2))
