n = int(input())
listA = list(map(int,input().split()))
m = int(input())
listM = list(map(int,input().split()))

listA = list(set(listA))
listA.sort()
for i in listM:
    start = 0
    end = len(listA) - 1

    isExist = False
    while (end - start) != 1:
        mid = (start + end) // 2
        if listA[mid] == i:
            isExist = True
            break
        elif listA[mid] > i:
            end = mid
        else:
            start = mid

    if isExist:
        print(1)
    else:
        if i in [listA[start], listA[end]]:
            print(1)
        else:
            print(0)