from collections import deque

N, K = map(int, input().split())

if K <= N:
    print(N - K)
else:
    cost = [1e9] * 2 * K
    q = deque()
    q.append((N, 0))
    cost[N] = 0

    if N == 0:
        q.append((N + 1, 1))
        cost[N + 1] = 1

    while len(q) > 0:
        n, c = q.popleft()

        if n > K and c + 1 < cost[n - 1]:
            cost[n - 1] = c + 1
            q.append((n - 1, c + 1))

        if 0 < n < K:
            move = [n - 1, n + 1]
            for m in move:
                if c + 1 < cost[m]:
                    cost[m] = c + 1
                    q.append((m, c + 1))
            if c < cost[2 * n]:
                cost[2 * n] = c
                q.append((2 * n, c))

    print(cost[K])