import collections

n,m,b = map(int, input().split())
ground = []
for i in range(n):
    ground.extend(list(map(int,input().split())))

counter = collections.Counter(ground)

minH = min(counter.keys())
maxH = max(counter.keys())

timeList = []
heightList = []
for i in range(minH,maxH+1):
    blocks = b
    time = 0
    for height in counter.keys():
        if height > i:
            unpackBlocks = (height - i) * counter[height]
            time += 2 * unpackBlocks
            blocks += unpackBlocks
        elif height == i:
            continue
        else:
            packBlocks = (i - height) * counter[height]
            time += packBlocks
            blocks -= packBlocks
    if blocks < 0:
        continue
    else:
        timeList.append(time)
        heightList.append(i)
timeList.reverse()
heightList.reverse()
minIdx = 0
for i in range(len(timeList)):
    if timeList[i] < timeList[minIdx]:
        minIdx = i
minTime = timeList[minIdx]
if timeList.count(minTime) > 1:

    print(timeList[minIdx], heightList[minIdx])
else:
    print(timeList[minIdx], heightList[minIdx])



