def solution(seoul):
    kim = seoul.index('Kim' or 'kim')
    answer = f'김서방은 {kim}에 있다'
    return answer

print(solution(['Jane', 'Kim']))