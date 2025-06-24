import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # set up
    N, K = map(int, input().strip().split())
    cost = list(map(int, input().strip().split()))
    graph = [[] for _ in range(N)]
    prev_count = [[0, 0] for _ in range(N)]
    for k in range(K):
        X, Y = map(int, input().strip().split())
        graph[X - 1].append(Y - 1)
        prev_count[Y - 1][0] = prev_count[Y - 1][0] + 1
    W = int(input()) - 1

    q = deque()
    for n in range(N):
        if prev_count[n][0] == 0:
            q.append((n, 0))

    while q:
        # print(q, prev_count)
        b, before = q.popleft()

        # 타겟 건물
        if b == W:
            print(prev_count[b][1] + cost[b])
            break

        for nb in graph[b]:
            prev_count[nb][0] = prev_count[nb][0] - 1
            prev_count[nb][1] = max(prev_count[nb][1], before + cost[b])
            if prev_count[nb][0] == 0:
                q.append((nb, prev_count[nb][1]))


