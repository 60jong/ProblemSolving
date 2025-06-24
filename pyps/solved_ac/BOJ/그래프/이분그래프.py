from collections import deque
import sys

input = sys.stdin.readline


def solution():
    # given
    V, E = map(int , input().strip().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int , input().strip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (V + 1)
    cache = [0] * (V + 1)
    a = [] # 1
    b = [] # -1

    # BFS
    for v in range(1, V + 1):
        if visited[v]:
            continue

        q = deque()
        q.append((v, 1))
        cache[v] = 1
        visited[v] = True
        a.append(v)

        while q:
            n, group = q.popleft()

            next_group = -1 * group
            target_group = a if next_group == 1 else b

            for nv in graph[n]:
                if not visited[nv]:
                    visited[nv] = True
                    cache[nv] = next_group

                    q.append((nv,  next_group))
                    target_group.append(nv)
                else:
                    if next_group != cache[nv]:
                        print("NO")
                        return
    print("YES")


K = int(input())
for _ in range(K):
    solution()