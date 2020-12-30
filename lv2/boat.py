"""
people을 몸무게 순으로 정렬한다.
구명보트의 제한을 넘어섰다면, 더 이상 사람을 추가하지 않고, 구명보트
"""


def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    boat = people[len(people) - 1]
    counter = 1

    while left < right:
        if boat + people[left] <= limit and counter < 2:
            boat += people[left]
            left += 1
            counter += 1
        else:
            answer += 1
            right -= 1
            counter = 1
            boat = people[right]
    answer += 1
    return answer


people = [70, 80, 50]
limit = 100
print(solution(people, limit))
