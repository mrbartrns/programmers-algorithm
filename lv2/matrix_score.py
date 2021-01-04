def solution(land):
    scores = []
    k = 0
    score = 0
    last = []
    solve(land, last, scores, k, score)
    scores.sort()
    answer = scores[-1]
    return answer


def solve(matrix, stack, scores, k, score):
    if k == len(matrix):
        if score not in scores:
            scores.append(score)
        return
    else:
        for i in range(len(matrix[0])):
            if not stack or stack[-1] != i:
                stack.append(i)
                score += matrix[k][i]
                solve(matrix, stack, scores, k + 1, score)
                stack.pop()
                score -= matrix[k][i]


matrix = [[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]]
print(solution(matrix))