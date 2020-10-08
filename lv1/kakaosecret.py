def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        sharp = ''

        for j in range(n):
            divideNumber = 2 ** (n - j - 1)
            n1 = arr1[i] // divideNumber
            r1 = arr1[i] % divideNumber
            arr1[i] = r1

            n2 = arr2[i] // divideNumber
            r2 = arr2[i] % divideNumber
            arr2[i] = r2

            if n1 + n2 != 0:
                sharp += '#'
            else:
                sharp += ' '
        answer.append(sharp)
    
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
