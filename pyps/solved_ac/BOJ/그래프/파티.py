import sys
from heapq import heappop, heappush


def calculateDistances(roads, N, start):
    distance = [1e9 for n in range(N + 1)]
    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while len(q) > 0:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue

        for n in roads[now]:
            cost = dist + roads[now][n]
            if cost < distance[n]:
                distance[n] = cost
                heappush(q, (cost, n))
    return distance


N, M, X = map(int, sys.stdin.readline().strip().split())

roadsFromHome = [dict() for n in range(N + 1)]
roadsFromX = [dict() for n in range(N + 1)]
for m in range(M):
    s, t, d = map(int, sys.stdin.readline().strip().split())
    roadsFromHome[s][t] = d
    roadsFromX[t][s] = d

toX = calculateDistances(roadsFromX, N, X)
toHome = calculateDistances(roadsFromHome, N, X)

maxOfMin = 0
for i in range(1, N + 1):
    total = toX[i] + toHome[i]
    if maxOfMin < total:
        maxOfMin = total

print(maxOfMin)