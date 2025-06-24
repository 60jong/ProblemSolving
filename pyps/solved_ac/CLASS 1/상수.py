numList = list(input())
numList.reverse()
print(max(int(''.join(numList[0:3])), int(''.join(numList[4:]))))