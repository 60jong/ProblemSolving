from collections import deque


def bfs(graph, n):
    vis = [False] * (N + 1)
    q = deque()

    count = 0
    q.append(n)
    vis[n] = True
    while q:

        p = q.popleft()

        for adj in graph[p]:
            if not vis[adj]:
                vis[adj] = True
                count += 1
                q.append(adj)
    return count


N, M = map(int, input().strip().split())

# Set graph
graph_p = [[] for _ in range(N + 1)]
graph_c = [[] for _ in range(N + 1)]

for _ in range(M):
    H, L = map(int, input().strip().split())
    graph_p[L].append(H)
    graph_c[H].append(L)

mid = N // 2 + 1
answer = 0

for n in range(1, N + 1):
    # children
    children = bfs(graph_c, n)

    # parents
    parents = bfs(graph_p, n)


    if children >= mid or parents >= mid:
        answer += 1
print(answer)
