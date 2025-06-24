def addPath(board, x, y):
    tempBoard = [board[i][:] for i in range(N)]
    tempBoard[x][y] += (999 - 3)

    for i in range(N - x):
        # 열
        tempBoard[x + i][y] += 1
        # 우하향 대각
        if y + i < N:
            tempBoard[x + i][y + i] += 1
        # 우상향 대각
        if y - i >= 0:
            tempBoard[x + i][y - i] += 1

    return tempBoard


def getLayable(row):
    layable = []
    for i in range(len(row)):
        if row[i] == 0:
            layable.append(i)
    return layable


def dfs(board, x, y):
    global count

    if x == (N - 1):
        count += 1
        print(count)
        return

    returned = addPath(board, x, y)
    layable = getLayable(returned[x + 1])
    if len(layable) == 0:
        return
    else:
        for c in layable:
            dfs(returned, x + 1, c)


N = int(input())

board = [[0 for i in range(N)] for j in range(N)]
count = 0

for i in range(N):
    dfs(board, 0, i)

print(count)