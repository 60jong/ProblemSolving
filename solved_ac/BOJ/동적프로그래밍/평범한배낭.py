# idx번째 물건을 사용 / 미사용 중 최고 가치 return
def solution(things, idx, K):
    if K == 0:
        return 0
    if idx == N:
        return 0
    if solutionStore[idx][K] > -1:
        return solutionStore[idx][K]
    # 사용
    used = 0
    if K >= things[idx][0]:
        used = things[idx][1] + solution(things, idx + 1, K - things[idx][0])
    # 미사용
    unused = solution(things, idx + 1, K)

    solutionStore[idx][K] = max(used, unused)
    return max(used, unused)

N, K = map(int, input().split())
things = []
for _ in range(N):
    W, V = map(int, input().split())
    things.append((W, V))

solutionStore = [[-1] * (K + 1) for _ in range(N + 1)]

print(solution(things, 0, K))
