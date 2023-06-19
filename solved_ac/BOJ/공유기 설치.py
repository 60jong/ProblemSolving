import sys
from bisect import *


def hasNearer(data, head, distance, sections):
    tmp = [head]
    for _ in range(1, sections):
        idx = bisect_left(data, tmp[-1] + distance)
        if idx >= len(data):
            idx = len(data) - 1
        tmp.append(data[idx])
        if distance > tmp[-1] - tmp[-2]:
            return True
    return False


homeCnt, deviceCnt = map(int, sys.stdin.readline().strip().split())
hLocation = [int(sys.stdin.readline().strip()) for _ in range(homeCnt)]

# 정렬
hLocation.sort()

# 최소의 최대 = (최대 - 최소) / (deviceCnt - 1)
maxOfMin = (hLocation[-1] - hLocation[0]) // (deviceCnt - 1)
end = hLocation[-1]
start = hLocation[0]

i = 1
j = maxOfMin

while i + 1 < j:
    mid = (i + j) // 2
    c = "i = {} / j = {} / mid = {}".format(i,j,mid)
    if hasNearer(hLocation, start, mid, deviceCnt):
        j = mid
    else:
        i = mid

if hasNearer(hLocation, start, j, deviceCnt):
    print(i)
else:
    print(j)
