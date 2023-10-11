N, M = map(int, input().split())

start = 1
INF = int(1e9)
dist = [INF] * (N + 1)
dist[start] = 0

edges = []
for m in range(M):
    S, E, T = map(int, input().split())
    edges.append((S, E, T))

for n in range(1, N + 1):
    for s, e, t in edges:
        if dist[s] != INF and dist[e] > dist[s] + t:
            dist[e] = dist[s] + t
            if n == N:
                print('YES')

print(dist)