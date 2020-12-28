"""
H-Index는 과학자의 생산ㅅ겅과 영향력을 나타내는 지표이다.
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고,
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index이다.
어떤 과학자 발표한 논문의 인용 횟수를 담은 배열 citations
ex) citation = [3, 0, 6, 1, 5] => H-Index: 3
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었다.
그리고 나머지 2편의 논문의 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3이다.
"""


def solution(citations):
    answer = 0
    citations.sort()
    max_value = citations[-1]
    counts = [0] * (max_value + 1)

    # make counts array
    for i in citations:
        counts[i] += 1

    return answer


citations = [3, 0, 6, 1, 5]  # [1, 1, 1, 1, 1] expected answer: 0 but it is 1
print(solution(citations))
"""
    for j in range(len(counts)):
        # 더했을 때 합이 j를 초과하면 h-index의 기준을 만족한다.
        min_sum = 0
        max_sum = 0
        if j > 0:
            for k in range(j):
                min_sum += counts[k]
            for k in range(j, len(counts)):
                max_sum += counts[k]
        if min_sum != 0 and max_sum != 0 and min_sum <= max_sum:
            answer = j
"""