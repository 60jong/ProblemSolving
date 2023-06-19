n, m = map(int,input().split())
treeLenList = list(map(int,input().split()))

start = 0
end = max(treeLenList)

while (end - start) != 1:
    canTake = 0
    mid = (start + end) // 2
    for tree in treeLenList:
        canTake += tree - mid if tree >= mid else 0

    if canTake < m:
        end = mid
    elif canTake > m:
        start = mid
    else:
        start = mid
print(start)