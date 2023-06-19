import collections

A = int(input())
B = int(input())
C = int(input())

numCntList = collections.Counter(str(A*B*C))

i = 0
while i < 10:
    print(numCntList[str(i)])
    i += 1