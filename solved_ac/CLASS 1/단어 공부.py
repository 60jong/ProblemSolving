import collections
string = input().upper()
answer = collections.Counter(string)

maxCnt = max(answer.values())
maxCntList = []
for i in answer:
    if answer[i] == maxCnt:
        maxCntList.append(i)

if len(maxCntList) > 1:
    print('?')
else:
    print(maxCntList[0])

