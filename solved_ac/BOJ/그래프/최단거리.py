import sys
from collections import deque

V, E = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline().strip())
distances = [dict() for _ in range(V + 1)]

for e in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    if v in distances[u]:
        if distances[u][v] > w:
            distances[u][v] = w
    else:
        distances[u][v] = w

distanceFromStart = [0 for v in range(V + 1)]

visited = [False for v in range(V + 1)]

queue = deque()
queue.append((start, start))
visited[start] = True

while len(queue) > 0:
    f, t = queue.popleft()

    if f == t:
        distanceFromStart[t] = 0
    else:
        if t not in distances[start]:
            distanceFromStart[t] = distanceFromStart[f] + distances[f][t]
        else:
            distanceFromStart[t] = min(distanceFromStart[f] + distances[f][t], distances[start][t])

    for k in distances[t]:
        if not visited[k]:
            visited[k] = True
            queue.append((t, k))

for i in range(1, len(distanceFromStart)):
    if distanceFromStart[i] > 0:
        print(distanceFromStart[i])
    elif i == start:
        print(0)
    else:
        print("INF")