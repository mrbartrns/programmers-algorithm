def solution(numbers, hand):
    left = 10
    right = 12
    answer = ''
    for i in range(len(numbers)):
        if numbers[i] % 3 == 1:
            answer += 'L'
            left = numbers[i]
        elif numbers[i] != 0 and numbers[i] % 3 == 0:
            answer += 'R'
            right = numbers[i]
        else:
            lLocation = [left // 3, left % 3]
            if left == 0:
                lLocation = [3, 2]
            mLocation = [numbers[i] // 3, numbers[i] % 3]
            if numbers[i] == 0:
                mLocation = [3, 2]
            if right != 0 and right % 3 == 0:
                rLocation = [right // 3 - 1, right % 3 + 3]
            elif right == 0:
                rLocation = [3, 2]
            else:
                rLocation = [right // 3, right % 3]
            if abs(lLocation[0] - mLocation[0]) + abs(lLocation[1] - mLocation[1]) > abs(rLocation[0] - mLocation[0]) + abs(rLocation[1] - mLocation[1]):
                answer += 'R'
                right = numbers[i]
            elif abs(lLocation[0] - mLocation[0]) + abs(lLocation[1] - mLocation[1]) < abs(rLocation[0] - mLocation[0]) + abs(rLocation[1] - mLocation[1]):
                answer += 'L'
                left = numbers[i]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = numbers[i]
                else:
                    answer += 'L'
                    left = numbers[i]
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))