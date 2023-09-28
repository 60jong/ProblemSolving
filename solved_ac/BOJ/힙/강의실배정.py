import sys
from heapq import heappush, heappop

input = sys.stdin.readline
def solution():
    N = int(input())
    times = []
    for _ in range(N):
        times.append(tuple(map(int, input().strip().split())))

    times = sorted(times, key=lambda x:x[0])

    pq = []
    for n in range(N):
        s, e = times[n]

        if len(pq) == 0:
            heappush(pq, e)
            continue

        if pq[0] > s:
            heappush(pq, e)
        else:
            heappop(pq)
            heappush(pq, e)

    return len(pq)

print(solution())