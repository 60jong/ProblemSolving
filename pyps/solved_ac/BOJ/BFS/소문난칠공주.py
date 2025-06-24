from itertools import combinations
from collections import deque

def check(room, cb):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    s_count = 0
    cb_2d = [(c // 5, c % 5) for c in cb]

    visited = dict(zip(cb_2d, [False] * 7))
    q = deque()
    q.append(cb_2d[0])
    if room[cb_2d[0][0]][cb_2d[0][1]] == 'S':
        s_count += 1
    visited[cb_2d[0]] = True

    while q:
        r, c = q.popleft()
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if (nr, nc) in cb_2d and not visited[(nr, nc)]:
                visited[(nr, nc)] = True
                q.append((nr, nc))
                if room[nr][nc] == 'S':
                    s_count += 1
    if s_count >= 4:
        for v in visited.values():
            if not v:
                return False
        return True
    return False

room = [input() for _ in range(5)]

count = 0
for c in combinations(range(0, 25), 7): # 480,700
    if check(room, c):
        count += 1
print(count)
