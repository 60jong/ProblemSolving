from heapq import heapify, heappop, heappush
import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N + 1)]

for m in range(M):
    f, t, c = map(int, sys.stdin.readline().strip().split())
    graph[f].append((t, c))

A, B = map(int, sys.stdin.readline().strip().split())

distance = [1e9] * (N + 1)

distance[A] = 0
q = []
heappush(q, (0, A))
while len(q) > 0:
    dist, node = heappop(q)
    if distance[node] < dist:
        continue
    for t, c in graph[node]:
        cost = dist + c
        if cost < distance[t]:
            distance[t] = cost
            heappush(q, (cost, t))

print(distance[B])
