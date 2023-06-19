k,n = map(int,input().split())

lenList = []
for i in range(k):
    lenList.append(int(input()))

start = 1
end = max(lenList) + 1

while (end - start) > 1:
    pipes = 0
    mid = (start + end) // 2
    for i in lenList:
        pipes += i // mid
        if pipes >= n:
            start = mid
            break
    if pipes < n:
        end = mid

pipe = 0
for i in lenList:
    pipe += i // start
if pipe >= n:
    print(start)
else:
    print(end)

