from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().strip().split())

board = [list(input().strip()) for _ in range(R)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
queue = set()
queue.add((0, 0, 1, board[0][0]))

max_dist = 1
while queue:
    y, x, cnt, passed = queue.pop()
    for d in dirs:
        ny, nx = y + d[0], x + d[1]

        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in passed:
            queue.add((ny, nx, cnt + 1, board[ny][nx] + passed))
            max_dist = max(max_dist, cnt + 1)
print(max_dist)