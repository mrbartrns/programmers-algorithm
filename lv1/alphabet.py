def solution(s):
    numofP = 0
    numofY = 0
    for c in s:
        if c == 'p' or c == 'P':
            numofP += 1
        elif c == 'y' or c == 'Y':
            numofY += 1

    return numofP == numofY

print(solution('pPoooyY'))