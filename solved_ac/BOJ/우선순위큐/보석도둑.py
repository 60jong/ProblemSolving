from heapq import heappush,heappop
import sys

input = sys.stdin.readline

def solution():
    count = 0

    N, K = map(int, input().strip().split())
    jewels = []
    bags = []
    # jewels
    for n in range(N):
        M, V = map(int, input().strip().split())
        jewels.append((M, V))
    for m in range(K):
        C = int(input())
        bags.append(C)
    jewels.sort()
    bags.sort()

    pq = []
    j_idx = 0
    for b in bags:
        while j_idx < len(jewels) and jewels[j_idx][0] <= b:
            heappush(pq, -jewels[j_idx][1])
            j_idx += 1

        if len(pq) > 0:
            negative_v = heappop(pq)
            count += negative_v * -1
        else: # 가방보다 보석이 무거움 or 더이상 보석이 없음
            if j_idx == len(jewels):
                break
            continue

    return count

print(solution())