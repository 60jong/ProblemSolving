from heapq import heappush, heappop
import sys

def findDist(start, graph):
    distance = [1e9] * len(graph)
    distance[start] = 0

    heap = []
    heappush(heap, (0, start))
    while len(heap) > 0:
        dist, n = heappop(heap)

        if dist > distance[n]:
            continue

        for idx, an in enumerate(graph[n]):
            cost = distance[n] + an
            if distance[idx] > cost:
                distance[idx] = cost
                heappush(heap, (cost, idx))
    return distance


N, E = map(int, sys.stdin.readline().strip().split())

graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for e in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c

d1, d2 = map(int, sys.stdin.readline().strip().split())

distanceFrom1 = findDist(1, graph)
distanceFromD1 = findDist(d1, graph)
distanceFromD2 = findDist(d2, graph)

# N / d1 / d2 / E
calculate1 = distanceFrom1[d1] + distanceFromD1[d2] + distanceFromD2[N]
# N / d2 / d1 / E
calculate2 = distanceFrom1[d2] + distanceFromD2[d1] + distanceFromD1[N]

answer = min(calculate1, calculate2)
if answer >= 1e9:
    print(-1)
else:
    print(answer)