import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
visited = [[False] * M for _ in range(N)]

count = 0
zeros = 0
hasRipen = False
allRipen = True
ripen = []
farm = []
for y in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    farm.append(row)
    for x in range(M):
        if row[x] == 1:
            ripen.append((x, y, count))
            hasRipen = True
            visited[y][x] = True
        else:
            allRipen = False
            if row[x] == 0:
                zeros += 1

if allRipen:
    print(0)
elif not hasRipen:
    print(-1)
else:
    ripen = deque(ripen)

    # for checking a layer's effect
    priorLayer = 0

    while len(ripen) > 0:
        x, y, layer = ripen.popleft()

        if count == layer:
            count += 1

        # 상
        if (y - 1 >= 0) and not visited[y - 1][x] and farm[y - 1][x] == 0:
            visited[y - 1][x] = True
            farm[y - 1][x] = 1
            ripen.append((x, y - 1, count))
            zeros -= 1
        # 하
        if (y + 1 < N) and not visited[y + 1][x] and farm[y + 1][x] == 0:
            visited[y + 1][x] = True
            farm[y + 1][x] = 1
            ripen.append((x, y + 1, count))
            zeros -= 1
        # 좌
        if (x - 1 >= 0) and not visited[y][x - 1] and farm[y][x - 1] == 0:
            visited[y][x - 1] = True
            farm[y][x - 1] = 1
            ripen.append((x - 1, y, count))
            zeros -= 1
        # 우
        if (x + 1 < M) and not visited[y][x + 1] and farm[y][x + 1] == 0:
            visited[y][x + 1] = True
            farm[y][x + 1] = 1
            ripen.append((x + 1, y, count))
            zeros -= 1

    if zeros == 0:
        print(count - 1)
    else:
        print(-1)