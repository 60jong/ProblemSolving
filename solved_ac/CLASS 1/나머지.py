numList = []
for i in range(10):
    numList.append(int(input()))

modList = []

for n in numList:
    modList.append(n % 42)

print(len(set(modList)))