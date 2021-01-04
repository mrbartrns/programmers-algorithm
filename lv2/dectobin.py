def solution(n):
    larger_number = n
    n_count_ones = count_ones(n)
    flag = False
    while not flag:
        larger_number += 1
        if n_count_ones == count_ones(larger_number):
            flag = True
    answer = larger_number
    return answer


def count_ones(n):
    counter = 0
    bin_n = bin(n)
    bin_n = bin_n[2:]
    for i in range(len(bin_n)):
        if bin_n[i] == "1":
            counter += 1
    return counter


print(solution(15))