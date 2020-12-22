"""
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 
그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 
이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 
이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.
1. 인쇄 대기목록의 가장 앞에 있는 문서 J를 대기목록에서 꺼낸다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한개라도 존재한다면, J를 대기목록의 가장 마지막에 넣는다.
3. 그렇지 않으면 J를 인쇄한다. 
"""


def solution(priorities: list, location: int) -> int:
    ans = 0
    while priorities != []:
        if location == 0:
            if is_biggest(priorities, priorities[0]):
                ans += 1
                return ans
            to_print = priorities.pop(0)
            priorities.append(to_print)
            location = len(priorities) - 1
        else:
            if is_biggest(priorities, priorities[0]):
                ans += 1
                priorities.pop(0)
                location -= 1
            else:
                to_print = priorities.pop(0)
                priorities.append(to_print)
                location -= 1
    return -1


def is_biggest(arr, num):
    for i in arr:
        if num < i:
            return False
    return True


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))