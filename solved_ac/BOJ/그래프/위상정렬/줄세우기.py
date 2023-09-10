# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# def solution():
#     answer = []
#     N, M = map(int, input().strip().split())
#
#     after = [[] for _ in range(N + 1)]
#     before_count = dict()
#
#     for _ in range(M):
#         a, b = map(int, input().strip().split())
#         if a not in before_count:
#             before_count[a] = 0
#
#         if b not in before_count:
#             before_count[b] = 1
#         else:
#             before_count[b] = before_count[b] + 1
#
#         after[a].append(b)
#
#     q = deque()
#     for b in before_count:
#         if before_count[b] == 0:
#             q.append(b)
#             before_count[b] = -1
#
#     # 위상 정렬은 모든 노드를 방문해야한다.
#     for _ in range(len(before_count)):
#         if not q: # 다 방문하기 전에 q가 비면 cycle 존재 의미
#             print("Has Cycle in Graph")
#             return
#         n = q.popleft()
#         answer.append(n)
#         for a in after[n]:
#             before_count[a] = before_count[a] - 1
#             if before_count[a] == 0:
#                 q.append(a)
#                 before_count[a] = -1
#
#     for i in range(1, N + 1):
#         if i not in before_count:
#             answer.append(i)
#
#     return ' '.join(map(str, answer))
#
# print(solution())

print('27,12,245'.replace(',', ''))