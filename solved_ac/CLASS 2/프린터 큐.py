from collections import deque

trials = int(input())

for _ in range(trials):
    printNum, targetIndex = list(map(int,input().split()))
    priorities = deque(map(int, input().split()))

    printRank = 1

    while len(priorities) > 1:
        i = 1
        while i < len(priorities):
            if priorities[0] < priorities[i]: # 뒤에 더 높은 우선 순위가 존재하는 상황
                priorities.append(priorities.popleft())
                if targetIndex == 0:
                    targetIndex = len(priorities) - 1
                else:
                    targetIndex = targetIndex - 1
                break
            i = i + 1

        if i == len(priorities): # 맨 앞것이 제일 큰 상황
            priorities.popleft()
            targetIndex = targetIndex - 1
            printRank += 1

        if targetIndex < 0:
            print(printRank - 1)
            break
