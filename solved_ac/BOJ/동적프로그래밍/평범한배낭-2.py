N, K = map(int, input().split())

things = []
for _ in range(N):
    things.append(tuple(map(int, input().split())))

dp = [0] * (K + 1)
for w, v in things:
    for k in range(K, w - 1, -1):
        dp[k] = max(dp[k - w] + v, dp[k])

print(dp[-1])