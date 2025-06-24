import sys

input = sys.stdin.readline
INF = int(1e9)
TC = int(input())

def solution():

    N, M, W = map(int, input().split())
    table = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        table[S].append([E, T])
        table[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        table[S].append([E, -T])

    distance = [INF] * (N + 1)
    distance[1] = 0
    for n in range(1, N + 1):
        for _n in range(1, N + 1):
            for next, cost in table[_n]:
                if distance[next] > distance[_n] + cost:
                    distance[next] = distance[_n] + cost
                    if n == N:
                        return 'YES'
    return 'NO'

for tc in range(TC):
    print(solution())