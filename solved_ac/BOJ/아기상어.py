from collections import deque

def getRealTarget(a, b):
    if a[0] > b[0]:
        return b
    elif a[0] == b[0]:
        # y가 작은 것 먼저
        if a[1] > b[1]:
            return b
        elif a[1] == b[1]:
            if a[2] > b[2]:
                return b
    return a

def findTargetAndDistance(board, sharkLoc, sharkSize):
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append((sharkLoc, 0))
    visited[sharkLoc[0]][sharkLoc[1]] = True

    result = [1e9, N, N]
    while len(queue) > 0:
        (sy, sx), dist = queue.popleft()

        ways = [(sy - 1, sx), (sy, sx -1),  (sy + 1, sx), (sy, sx + 1)]
        for w in ways:
            y, x = w[0], w[1]
            # 방향 index가 유효 and 방문 X and 지나갈 수 있다.

            if (-1 < y < N and -1 < x < N) and (not visited[y][x]) and board[y][x] <= sharkSize:
                # 먹어야 하는 곳이라면
                if 0 < board[y][x] < sharkSize:
                    result = getRealTarget(result, [dist + 1, y, x])
                # 아니면 지나치는 곳
                else:
                    queue.append(((y, x), dist + 1))
                    visited[y][x] = True
    return result if result[0] < 1e9 else None

N = int(input())
board = [[] for i in range(N)]

sharkLoc = (0, 0)
sharkSize = 2
growthBuf = 0
for y in range(N):
    row = input().split()
    for x in range(len(row)):
        num = int(row[x])
        board[y].append(num)
        if num == 9:
            sharkLoc = (y, x)
# 상어 있던 자리는 빈칸으로
board[sharkLoc[0]][sharkLoc[1]] = 0

count = 0
while True:
    result = findTargetAndDistance(board, sharkLoc, sharkSize)
    if result is None:
        break

    dist, ty, tx = result

    # board 수정
    board[ty][tx] = 0
    growthBuf += 1
    if growthBuf == sharkSize:
        sharkSize += 1
        growthBuf = 0

    sharkLoc = (ty, tx)
    count += dist

print(count)