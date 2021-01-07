"""
보드의 행 m
보드의 열 n
배치정보 board

"""


def solution(m, n, board):
    answer = 0
    matrix = []
    # board를 이용하여 matrix 만들기
    for i in range(len(board)):
        temp = []
        for c in board[i]:
            temp.append(c)
        matrix.append(temp)
    print(matrix)
    return answer


# matrix 내부의 요소들을 검사
# def check(matrix):
#     for i in range(len(matrix) - 1):
#         for j in range(len(matrix[0]) - 1):
#             pass


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))
