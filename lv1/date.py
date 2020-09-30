def solution(a, b):
    answer = ''
    total = 0
    dates = dict([(0, 0), (1, 31), (2, 29), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)])
    days = dict([(0, 'THU'), (1, 'FRI'), (2, 'SAT'), (3, 'SUN'), (4, 'MON'), (5, 'TUE'), (6, 'WED')])
    for i in range(a):
        total += dates[i]
    total += b
    answer = days[total % 7]
    return answer

print(solution(5, 24))