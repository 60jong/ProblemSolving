from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = []

for _ in range(M):
    f, t = map(int, sys.stdin.readline().strip().split())
    graph[f].append(t)

# BFS
q = deque()
q.append((X, 0))
visited[X] = True
while len(q) > 0:
    n, d = q.popleft()

    if d == K:
        result.append(n)

    for node in graph[n]:
        if not visited[node]:
            visited[node] = True
            q.append((node, d + 1))

result.sort()
if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r)