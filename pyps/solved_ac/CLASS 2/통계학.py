import collections
count = int(input())
numList = []
for i in range(count):
    numList.append(int(input()))

numList.sort()

print(round(sum(numList)/count))
print(numList[count//2])

counter = collections.Counter(numList).most_common()

mostCount = counter[0][1]
if len(counter) == 1:
    print(counter[0][0])
else:
    if counter[1][1] == mostCount:
        print(counter[1][0])
    else:
        print(counter[0][0])

print(numList[-1] - numList[0])

