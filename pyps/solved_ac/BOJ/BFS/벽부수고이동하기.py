import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

dists = [[[int(1e9), int(1e9)] for m in range(M)] for n in range(N)]

queue = deque()
queue.append((0, 0, 1, 0))
dists[0][0] = [1, 1]
reached = False
while queue:
    r, c, dist, used = queue.popleft()

    if r == N - 1 and c == M - 1:
        reached = True

        idx = 0
        if used:
            idx = 1
        dists[r][c][idx] = min(dist, dists[r][c][idx])
        continue

    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < M and dist + 1 < dists[nr][nc][used]:
            if board[nr][nc] == 0:
                queue.append((nr, nc, dist + 1, used))
                dists[nr][nc][used] = dist + 1
            else:
                if not used:
                    queue.append((nr, nc, dist + 1, 1))
                    dists[nr][nc][1] = dist + 1

if reached:
    print(min(dists[N - 1][M - 1][0], dists[N - 1][M - 1][1]))
else:
    print(-1)