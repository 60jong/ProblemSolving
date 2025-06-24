from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

walls = []
graph = []

for n in range(N):
    row = input().strip()
    graph.append(list(map(int, row)))
    for m in range(M):
        if graph[n][m] == 1:
            walls.append((n, m))

visited = [[False] * M for _ in range(N)]
connected = [[0] * M for _ in range(N)]
parent = [[(n, m) for m in range(M)] for n in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
for n in range(N):
    for m in range(M):
        if graph[n][m] == 0 and not visited[n][m]:

            count = 0

            q.append((n, m))
            visited[n][m] = True
            while q:
                r, c = q.popleft()
                parent[r][c] = parent[n][m]
                count += 1

                for d in range(4):
                    nr, nc = r + dx[d], c + dy[d]
                    if (0 <= nr < N and 0 <= nc < M) and graph[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            connected[n][m] = count

# sum [connected] nearby a wall
for wr, wc in walls:
    parents = set()
    for d in range(4):
        nr, nc = wr + dx[d], wc + dy[d]
        if 0 <= nr < N and 0 <= nc < M:
            parents.add(parent[nr][nc])
    for pr, pc in parents:
        graph[wr][wc] = (graph[wr][wc] + connected[pr][pc]) % 10

for g in graph:
    print(''.join(map(str, g)))
