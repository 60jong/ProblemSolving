# from collections import deque
#
# cardNum = int(input())
#
# list = deque(range(1,cardNum+1))
#
# while len(list) > 1:
#     list.popleft()
#     temp = list.popleft()
#     list.append(temp)
#
# print(list.popleft())

cardNum = int(input())

list = list(range(1, cardNum + 1))

listIndex = 0
initialListLen = len(list)
discarded = 0
while (initialListLen - discarded) != 1:
    # 삭제
    listIndex = listIndex + 1
    discarded = discarded + 1
    # 다음 요소 뒤로
    temp = list[listIndex]
    list.append(temp)
    listIndex = listIndex + 1

print(list[listIndex])