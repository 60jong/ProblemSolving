import sys
from collections import deque

def bfsForNormal(sections):
    global N

    count = 0
    visitCount = 0
    visited = [[False for i in range(N)] for _ in range(N)]
    # init
    cq = deque(list())
    cq.append((0, 0))
    visited[0][0] = True
    visitCount += 1

    while len(cq) > 0:
        while len(cq) > 0:
            y, x = cq.popleft()
            #상
            if y - 1 >= 0 and not visited[y - 1][x] and sections[y - 1][x] == sections[y][x]:
                cq.append((y - 1, x))
                visited[y - 1][x] = True
                visitCount += 1
            #하
            if y + 1 < N and not visited[y + 1][x] and sections[y + 1][x] == sections[y][x]:
                cq.append((y + 1, x))
                visited[y + 1][x] = True
                visitCount += 1
            #좌
            if x - 1 >= 0 and not visited[y][x - 1] and sections[y][x - 1] == sections[y][x]:
                cq.append((y, x - 1))
                visited[y][x - 1] = True
                visitCount += 1
            #우
            if x + 1 < N and not visited[y][x + 1] and sections[y][x + 1] == sections[y][x]:
                cq.append((y, x + 1))
                visited[y][x + 1] = True
                visitCount += 1
        count += 1
        #다음 알파벳 찾기
        found = False
        for y in range(len(sections)):
            if not found:
                for x in range(len(sections[0])):
                    if not visited[y][x]:
                        cq.append((y, x))
                        visited[y][x] = True
                        visitCount += 1
                        found = True
                        break
    return count

def bfsForNotNormal(sections):
    global N
    notNormalColorSet = ('R', 'G')
    count = 0
    visitCount = 0
    visited = [[False for i in range(N)] for _ in range(N)]
    # init
    cq = deque(list())
    cq.append((0, 0))
    visited[0][0] = True
    visitCount += 1
    while len(cq) > 0:
        while len(cq) > 0:
            y, x = cq.popleft()
            #상
            if y - 1 >= 0 and not visited[y - 1][x] and (sections[y][x] == sections[y - 1][x] or (sections[y][x] in notNormalColorSet and sections[y - 1][x] in notNormalColorSet)):
                cq.append((y - 1, x))
                visited[y - 1][x] = True
                visitCount += 1
            #하
            if y + 1 < N and not visited[y + 1][x] and (sections[y][x] == sections[y + 1][x] or (sections[y][x] in notNormalColorSet and sections[y + 1][x] in notNormalColorSet)):
                cq.append((y + 1, x))
                visited[y + 1][x] = True
                visitCount += 1
            #좌
            if x - 1 >= 0 and not visited[y][x - 1] and (sections[y][x] == sections[y][x - 1] or (sections[y][x] in notNormalColorSet and sections[y][x - 1] in notNormalColorSet)):
                cq.append((y, x - 1))
                visited[y][x - 1] = True
                visitCount += 1
            #우
            if x + 1 < N and not visited[y][x + 1] and (sections[y][x] == sections[y][x + 1] or (sections[y][x] in notNormalColorSet and sections[y][x + 1] in notNormalColorSet)):
                cq.append((y, x + 1))
                visited[y][x + 1] = True
                visitCount += 1
        count += 1
        #다음 알파벳 찾기
        found = False
        for y in range(len(sections)):
            if not found:
                for x in range(len(sections[0])):
                    if not visited[y][x]:
                        cq.append((y, x))
                        visited[y][x] = True
                        visitCount += 1
                        found = True
                        break
    return count
N = int(sys.stdin.readline().strip())

sections = []
for i in range(N):
    row = sys.stdin.readline().strip()
    rowElements = [r for r in row]

    sections.append(rowElements)

print(bfsForNormal(sections), bfsForNotNormal(sections), sep=' ')
