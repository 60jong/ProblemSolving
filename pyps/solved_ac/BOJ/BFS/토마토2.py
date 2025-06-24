import sys
from collections import deque

X, Y, Z = map(int, sys.stdin.readline().strip().split())

farm = [[list(map(int, sys.stdin.readline().strip().split())) for y in range(Y)] for z in range(Z)]

zeros = 0
visited = [[[False] * X for y in range(Y)] for z in range(Z)]
tomaQ = deque()
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            if farm[z][y][x] == 1:
                visited[z][y][x] = True
                tomaQ.append((z, y, x, 0))
            elif farm[z][y][x] == 0:
                zeros += 1
count = 0
while len(tomaQ) > 0 and zeros > 0:
    z, y, x, layer = tomaQ.popleft()

    if count == layer:
        count += 1

    #앞
    if y + 1 < Y and visited[z][y + 1][x] == False and farm[z][y + 1][x] == 0:
        visited[z][y + 1][x] = True
        farm[z][y + 1][x] = 1
        zeros -= 1
        tomaQ.append((z, y + 1, x, count))
    #뒤
    if y - 1 >= 0 and visited[z][y - 1][x] == False and farm[z][y - 1][x] == 0:
        visited[z][y - 1][x] = True
        farm[z][y - 1][x] = 1
        zeros -= 1
        tomaQ.append((z, y - 1, x, count))
    #좌
    if x - 1 >= 0 and visited[z][y][x - 1] == False and farm[z][y][x - 1] == 0:
        visited[z][y][x - 1] = True
        farm[z][y][x - 1] = 1
        zeros -= 1
        tomaQ.append((z, y, x - 1, count))
    #우
    if x + 1 < X and visited[z][y][x + 1] == False and farm[z][y][x + 1] == 0:
        visited[z][y][x + 1] = True
        farm[z][y][x + 1] = 1
        zeros -= 1
        tomaQ.append((z, y, x + 1, count))
    #상
    if z - 1 >= 0 and visited[z - 1][y][x] == False and farm[z - 1][y][x] == 0:
        visited[z - 1][y][x] = True
        farm[z - 1][y][x] = 1
        zeros -= 1
        tomaQ.append((z - 1, y, x, count))
    #하
    if z + 1 < Z and visited[z + 1][y][x] == False and farm[z + 1][y][x] == 0:
        visited[z + 1][y][x] = True
        farm[z + 1][y][x] = 1
        zeros -= 1
        tomaQ.append((z + 1, y, x, count))

if zeros > 0:
    print(-1)
else:
    print(count)