from itertools import combinations

N, M = map(int, input().split())

def calcChicDist(homeLocations, stores):
    totalChicDist = 0
    for hl in homeLocations:
        minDist = 1e9
        for s in stores:
            dist = abs(hl[0] - s[0]) + abs(hl[1] - s[1])
            minDist = min(minDist, dist)
        totalChicDist += minDist
    return totalChicDist

# M<= 치킨 집 수(CH) <=13
allChicPlaces = []
homeLocations = []
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(N):
        if row[x] == 2:
            allChicPlaces.append((y, x))
        elif row[x] == 1:
            homeLocations.append((y, x))

minChicDist = 1e9
for c in combinations(allChicPlaces, M):
    chicDist = calcChicDist(homeLocations, list(c))
    minChicDist = min(minChicDist, chicDist)

print(minChicDist)