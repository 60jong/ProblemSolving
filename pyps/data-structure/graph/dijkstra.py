from heapq import heappush, heappop


def get_smallest_v1():
    idx = 0
    for i, d in enumerate(distance):
        if i == 0:
            continue

        if not visited[i] and distance[i] < distance[idx]:
            idx = i
    return idx


# Set up
data = [
    "1 2 2",
    "1 3 3",
    "1 4 1",
    "2 3 3",
    "2 4 4",
    "3 2 3",
    "3 6 5",
    "4 3 3",
    "4 5 1",
    "5 3 1",
    "5 6 2",
]

graph = [[] for _ in range(7)]

for d in data:
    v1, v2, w = map(int, d.split())
    graph[int(v1)].append((v2, w))

# Find distance
INF = int(1e9)
distance = [INF] * 7
visited = [False] * 7

start = 1
distance[start] = 0

pq = []
heappush(pq, (distance[start], start))

for _ in range(6):
    dist, v = heappop(pq)
    visited[v] = True

    for nv, nw in graph[v]:
        new_dist = dist + nw

        if distance[nv] > new_dist:
            distance[nv] = new_dist
            if not visited[nv]:
                heappush(pq, (new_dist, nv))


print(distance)