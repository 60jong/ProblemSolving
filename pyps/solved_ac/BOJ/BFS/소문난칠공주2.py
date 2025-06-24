from itertools import combinations
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

grid = [input().strip() for _ in range(5)]
count = 0

for combi in combinations(range(25), 7):
    points = []
    for i in combi:
        points.append((i // 5, i % 5))

    # Check count of 'S' is larger than 4
    s_count = 0
    for r, c in points:
        if grid[r][c] == 'S':
            s_count += 1
    if s_count < 4:
        continue

    # Check if they are connected
    points_set = set(points)
    visited = [[False] * 5 for _ in range(5)]

    q = deque()
    q.append(points[0])
    visited[points[0][0]][points[0][1]] = True
    connect_count = 1

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 5 and 0 <= nc < 5:
                if not visited[nr][nc]:
                    if (nr, nc) in points_set:
                        visited[nr][nc] = True
                        connect_count += 1
                        q.append((nr, nc))

    if connect_count == 7:
        count += 1

print(count)




