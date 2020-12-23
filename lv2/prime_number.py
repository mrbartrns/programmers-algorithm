# 완전탐색을 이용한 소수 찾기
def solution(numbers):
    tf_arr = [False] * len(numbers)
    string = ""
    arr = []
    solve(numbers, string, arr, tf_arr)
    # print(arr)
    answer = check_prime_number(arr)
    return answer


def solve(numbers, string, arr, tf):
    for i in range(len(numbers)):
        if not tf[i]:
            tf[i] = True
            string += numbers[i]
            if int(string) not in arr:
                arr.append(int(string))
            solve(numbers, string, arr, tf)
            string = string[:-1] if len(string) > 1 else ""
            tf[i] = False


def check_prime_number(arr):
    counts = 0
    for i in arr:
        if i == 2 or (i > 2 and i % 2 != 0):
            j = 1
            while j < i:
                if j != 1 and i % j == 0:
                    break
                j += 1
            if j == i:
                counts += 1
    return counts


# number = "011"
# tf_arr = [False] * len(number)
# arr = []
# string = ""
# solve(number, string, arr, tf_arr)
# print(check_prime_number(arr))
print(solution("243"))