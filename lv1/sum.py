def solution(n):
    answer = 0
    max = n
    if n == 1:
        answer = 1
    else:
        for i in range(1, n):
            if n % i == 0:
                if i >= max:
                    break
                else:
                    max = n // i
                    answer += i
                    if max != i:
                        answer += max

    return answer

def solution1(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

# print(solution(4), solution1(4))

def compare(n):
    flag = True
    for i in range(n):
        if solution(i) != solution1(i):
            flag = False
            print(i)
            break
    return flag

print(compare(3000))

# print(solution(4))