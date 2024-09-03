import sys
from collections import deque

input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution():
    reached = False
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    cost_grid = [[[int(1e9), int(1e9)] for m in range(M)] for n in range(N)]
    q = deque()
    q.append((0, 0, 1, False))  # (r, c, cost, crashed_before)
    cost_grid[0][0][0] = 1
    cost_grid[0][0][1] = 1

    while q:
        r, c, cost, cb = q.popleft()
        idx = 1 if cb else 0

        if r == (N - 1) and c == (M - 1):
            reached = True
            cost_grid[r][c][idx] = min(cost, cost_grid[r][c][idx])
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] == '0':
                    if cost + 1 < cost_grid[nr][nc][idx]:
                        cost_grid[nr][nc][idx] = cost + 1
                        q.append((nr, nc, cost + 1, cb))
                else:
                    if idx == 0:  # not crashed before
                        if cost + 1 < cost_grid[nr][nc][idx]:
                            cost_grid[nr][nc][idx] = cost + 1
                            q.append((nr, nc, cost + 1, True))

    if reached:
        print(min(cost_grid[N - 1][M - 1]))
    else:
        print(-1)


solution()