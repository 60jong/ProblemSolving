from heapq import heappush, heappop
import sys

input = sys.stdin.readline

xq = []
nq = []

pl = dict()
N = int(input())
for _ in range(N):
    P, L = map(int, input().strip().split())
    heappush(nq, (L, P))
    heappush(xq, (-L, -P))
    pl[P] = L

M = int(input())
for _ in range(M):
    input_row = input().strip().split()

    if input_row[0] == 'add':
        cmd, P, L = input_row
        P, L = int(P), int(L)
        pl[P] = L
        heappush(nq, (L, P))
        heappush(xq, (-L, -P))
    elif input_row[0] == 'recommend':
        if input_row[1] == '1':
            while True:
                L, P = map(abs, xq[0])
                if pl[P] != L:
                    heappop(xq)
                else:
                    break
            print(-xq[0][1])
        else:
            while True:
                L, P = nq[0]
                if pl[P] != L:
                    heappop(nq)
                else:
                    break
            print(nq[0][1])
    else: # solve
        pl[int(input_row[1])] = -1