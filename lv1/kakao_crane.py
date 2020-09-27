def solution(board, moves):
    # board: matrix, 
    '''
    board: n * n matrix 0: empty, else: full
    return: answer 
    '''
    new = []
    answer = 0
    # 보드의 길이에서 보드[x][1]이 0이 아니라면 0으로 바꾸고 숫자를 새로운 리스트에 집어넣는다.
    for i in moves:
        x = i - 1
        for j in range(len(board)):
            if board[j][x] != 0:
                num = board[j][x] # num을 저장하고 num이 new에 저장하는 숫자와 같다면 숫자를 제거한다.
                new.append(num)
                if len(new) > 1 and new[-1] == new[-2]:
                    answer += 2
                    new.pop(-1)
                    new.pop(-1)
                board[j][x] = 0
                break
    return answer

board  = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]

moves = [1,5,3,5,1,2,1,4]

solution(board, moves)