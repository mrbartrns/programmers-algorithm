def solution(array, commands):
    '''
    array: [], elements: int
    commands: matrix (2 * 2), elements: list, length: 3, (i, j, k)
    '''
    answer = []
    for i in range(len(commands)):
        j = commands[i][0] - 1
        k = commands[i][1]
        l = commands[i][2] - 1
        copy = array[j: k]
        copy.sort()
        number = copy[l]
        answer.append(number)
    return answer
    
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))