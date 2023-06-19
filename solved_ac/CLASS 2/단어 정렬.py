trials = int(input())
vocaList = []
for i in range(trials):
    vocaList.append(input())

vocaList = list(set(vocaList))
vocaList.sort(key=lambda x:(len(x),x))

for i in vocaList:
    print(i)



print(returnList)