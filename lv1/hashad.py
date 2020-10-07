def solution(x):
    answer = True
    temp = 0
    copy = x
    while copy != 0:
        r = copy % 10
        copy //= 10
        temp += r

    if x % temp != 0:
        answer = False
    return answer

print(solution(13))