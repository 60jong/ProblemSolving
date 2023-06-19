num = int(input())
targetList = []
for i in range(num):
    targetList.append(int(input()))

stack = []
printList = []
count = 0
for i in targetList:
    if i > count:
        while (i - count) != 0:
            count += 1
            printList.append('+')
            stack.append(count)
        stack.pop()
        printList.append('-')
    elif stack[-1] == i:
        stack.pop()
        printList.append('-')
    else:
        printList.clear()
        printList.append('NO')
        break

for i in printList:
    print(i)
