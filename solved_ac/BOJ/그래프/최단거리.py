import sys
from heapq import heapify, heappop, heappush

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

distanceFromStart = [1e9 for v in range(V + 1)]

q = []
heappush(q, (0, start))
distanceFromStart[start] = 0

while len(q) > 0:
    distance, targetNode = heappop(q)

    if distance > distanceFromStart[targetNode]:
        continue

    for n in distances[targetNode]:
        cost = distance + distances[targetNode][n]
        if distanceFromStart[n] > cost:
            distanceFromStart[n] = cost
            heappush(q, (cost, n))

for i in range(1, len(distanceFromStart)):
    if distanceFromStart[i] == 1e9:
        print('INF')
    else:
        print(distanceFromStart[i])