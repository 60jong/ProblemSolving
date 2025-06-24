from collections import deque


def solution(board):
    answer = 0
    N = len(board)
    costBoard = [[[1e9 for i in range(N)] for j in range(N)] for k in range(4)]

    for i in range(4): costBoard[i][0][0] = 0
    q = deque()
    q.append((0, 0, -1, 0))

    while len(q) > 0:
        y, x, pd, cost = q.popleft()

        ns = [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]
        for d, (ny, nx) in enumerate(ns):
            # board 내부 and not Wall
            if ((0 <= ny <= N - 1) and (0 <= nx <= N - 1)) and (board[ny][nx] == 0):
                # 움직인 비용이 더 싸면 move
                costAfterMove = cost + calcCost(d, pd)
                if costAfterMove < costBoard[d][ny][nx]:
                    costBoard[d][ny][nx] = costAfterMove
                    q.append((ny, nx, d, costAfterMove))

    return min(costBoard[0][N - 1][N - 1], costBoard[1][N - 1][N - 1], costBoard[2][N - 1][N - 1],
               costBoard[3][N - 1][N - 1])


def calcCost(d, pd):
    if pd == -1: return 100

    a = abs(d - pd)
    if a % 2 == 0:
        return 100
    else:
        return 600