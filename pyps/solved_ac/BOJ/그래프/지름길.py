from collections import deque
N, distance = map(int, input().split())

shortcuts = [list(map(int, input().split())) for _ in range(N)]
# shortcuts = sorted(shortcuts, key=lambda x : x[0])

start = 0
myQ = deque()

minDist = distance

for s in shortcuts:
    if s[0] >= start and s[1] <= distance:
        myQ.append((s[1], s[2], s[0] - start + s[2]))

while len(myQ) > 0:
    end, drive, totalDrive = myQ.popleft()
    # 일단 저장
    if end <= distance:
        if minDist > (distance - end + totalDrive):
            minDist = (distance - end + totalDrive)
    for s in shortcuts:
        if s[0] >= end and s[1] <= distance:
            myQ.append((s[1], s[2], s[0] - end + totalDrive + s[2]))

print(minDist)
