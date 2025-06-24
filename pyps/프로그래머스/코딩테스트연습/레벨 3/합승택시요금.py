from heapq import heappush, heappop

INF = int(1e9)

def get_distance_from(n, s, graph):
    dist_from_s = [INF] * (n + 1)

    dist_from_s[s] = 0
    pq = [(0, s)]

    while pq:
        dist, v = heappop(pq)

        if dist_from_s[v] < dist:
            continue
        for nv, cost in graph[v]:
            if dist_from_s[nv] > dist + cost:
                dist_from_s[nv] = dist + cost
                heappush(pq, (dist_from_s[nv], nv))
    return dist_from_s

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for f, t, c in fares:
        graph[f].append((t, c))
        graph[t].append((f, c))

    # S에서 모든 곳까지 dijstra
    dist_from_s = get_distance_from(n, s, graph)

    # S -> 특정 장소 -> A/B
    answer = INF
    for i, d in enumerate(dist_from_s):
        if d >= INF:
            continue

        dist_from_i = get_distance_from(n, i, graph)

        answer = min(answer, dist_from_s[i] + dist_from_i[a] + dist_from_i[b])
    return answer
