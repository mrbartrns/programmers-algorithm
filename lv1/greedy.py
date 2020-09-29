def solution(n, lost, reserve):
    '''
    n: int, total numbers of student
    lost: list
    reserve: list
    answer: n - len(lost)
    '''
    # 먼저 겹치는 숫자들을 제거 후에 
    lostCopy = lost[:]
    reserveCopy = reserve[:]
    answer = 0
    for i in lost:
        if i in reserve:
            lostCopy.remove(i)
            reserveCopy.remove(i)
    lost = lostCopy[:]
    for i in lost:
        # if i in reserveCopy:
        #     lostCopy.remove(i)
        #     reserveCopy.remove(i)
        if i - 1 in reserveCopy:
            lostCopy.remove(i)
            reserveCopy.remove(i - 1)
        elif i + 1 in reserveCopy:
            lostCopy.remove(i)
            reserveCopy.remove(i + 1)
    answer = n - len(lostCopy)
    return answer

def random_case_generator(n):
    import random
    lost = random.sample(range(1, n), random.randint(0,n-1))
    reserve = random.sample(range(1, n), random.randint(0,n-1))
    arr = [1] * n
    for l in lost:
        arr[l - 1] -= 1
    for r in reserve:
        arr[r - 1] += 1

    for i in range(n - 1):
        if arr[i] == 0 and arr[i + 1] == 2:
            arr[i] = 1
            arr[i + 1] = 1
        if arr[i] == 2 and arr[i + 1] == 0:
            arr[i] = 1
            arr[i + 1] = 1
    answer = n - arr.count(0)
    return n, lost, reserve, answer

# n = 3
# n, lost, reserve, answer = random_case_generator(n)
# while True:
#     *par, answer = random_case_generator(n)
#     if solution(*par) != answer:
#         print(f"incorrect for case:{par}")
#         break

print(solution(3, [1, 2], [1, 2]))
print(solution(5, [2, 4], [1, 3, 5]))