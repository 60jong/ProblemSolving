N, K = map(int, input().split())

things = []
for _ in range(N):
    things.append(tuple(map(int, input().split())))

# dp[i][j] = i번째 things까지 사용해서 j 무게를 채워 얻는 최고 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    w, v = things[n - 1]
    for k in range(1, K + 1):
        if w <= k:
            dp[n][k] = max(dp[n - 1][k - w] + v, dp[n - 1][k])
        else:
            dp[n][k] = dp[n - 1][k]

print(dp[N][K])