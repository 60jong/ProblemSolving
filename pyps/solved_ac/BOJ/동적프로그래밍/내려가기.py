import sys

input = sys.stdin.readline

N = int(input())
INF = int(1000000)

dirs = [(0, 1), (0, 1, 2), (1, 2)]

prior = [[0, 0], [0, 0], [0, 0]]
for n in range(N):
    nums = list(map(int, input().split()))
    temp = [[0, 0], [0, 0], [0, 0]]
    for c in range(3):
        mx, mn = 0, INF
        for x in dirs[c]:
            mx = max(mx, nums[x] + prior[x][0])
            mn = min(mn, nums[x] + prior[x][1])

        temp[c] = [mx, mn]
    prior = temp

mx, mn = 0, INF
for x in dirs[1]:
    mx = max(mx, prior[x][0])
    mn = min(mn, prior[x][1])
print(mx, mn)