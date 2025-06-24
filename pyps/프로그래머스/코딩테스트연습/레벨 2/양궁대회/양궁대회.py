# # 1
# import sys
#
# sys.setrecursionlimit(10000)
#
# occasions = []
#
#
# def do(shots, index, arrows, apeach):
#     # 화살이 없다면 뒤에 전부 0을 추가, 재귀 끝
#     if arrows == 0:
#         temp = shots[:]
#         while len(temp) < len(apeach):
#             temp.append(0)
#         occasions.append(temp)
#
#     # 1번 과녁까지 왔는데 화살이 남았다면, 1번에 다 쏘고 재귀 끝
#     elif index == 10:
#         temp = shots[:]
#         temp.append(arrows)
#         occasions.append(temp)
#
#     # 1번 과녁 아니고 화살 남았다면, 로직 수행 (1개 쏘거나(빈 곳) / 뺏거나 / 패스)
#     else:
#         # 빈 과녁 ->  패스 or 1개 쏨
#         if apeach[index] == 0:
#             # argument 복사
#             tempForPass, tempForShot = shots[:], shots[:]
#             indexForPass, indexForShot = index, index
#             arrowsForPass, arrowsForShot = arrows, arrows
#
#             # 패스하고 재귀
#             tempForPass.append(0)
#             indexForPass += 1
#             do(tempForPass, indexForPass, arrowsForPass,apeach)
#
#             # 패스 재귀 끝나면 1개 쏘고 재귀
#             tempForShot.append(1)
#             arrowsForShot -= 1
#             indexForShot += 1
#             do(tempForShot, indexForShot, arrowsForShot,apeach)
#         # apeach가 쏜 과녁 -> 패스 or 뺏기 (화살개수 가능하면)
#         else:
#             # argument 복사
#             tempForPass, tempForShot = shots[:], shots[:]
#             indexForPass, indexForShot = index, index
#             arrowsForPass, arrowsForShot = arrows, arrows
#
#             # 패스하고 재귀
#             tempForPass.append(0)
#             indexForPass += 1
#             do(tempForPass, indexForPass, arrowsForPass,apeach)
#
#             # 패스 재귀 끝나면 뺏고 재귀
#             # 화살 갯수 가능
#             if arrowsForShot >= apeach[indexForShot] + 1:
#                 tempForShot.append(apeach[indexForShot] + 1)
#                 arrowsForShot -= apeach[indexForShot] + 1
#                 indexForShot += 1
#                 do(tempForShot, indexForShot, arrowsForShot, apeach)
#
#
# def solution(n, info):
#     do([], 0, n, info)
#
#     maxGap = 0
#     result = []
#     for o in occasions:
#         apeachScore = 0
#         lionScore = 0
#         for i in range(len(o) - 1):
#             if info[i] + o[i] == 0:
#                 continue
#             else:
#                 if info[i] < o[i]:
#                     lionScore += 10 - i
#                 else:
#                     apeachScore += 10 - i
#         gap = lionScore - apeachScore
#         if gap > maxGap:
#             maxGap = gap
#         result.append((apeachScore, lionScore, gap))
#
#     if maxGap == 0:
#         return [-1]
#     else:
#         maxCases = []
#         for i in range(len(result)):
#             if result[i][2] == maxGap:
#                 maxCases.append(occasions[i])
#         i = 10
#         while True:
#             temp = []
#             for case in maxCases:
#                 if case[i] != 0:
#                     temp.append(case)
#
#             if len(temp) == 1:
#                 return temp[0]
#                 break
#             elif len(temp) > 1:
#                 maxCases = temp
#                 i -= 1
#             else:
#                 i -= 1
#
#
# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]
# print(solution(n, info))
from itertools import combinations_with_replacement as cwr


def score(a, l):
    a_score = 0
    l_score = 0

    for i in range(11):
        if a[i] >= l[i]:
            if a[i] > 0:
                a_score += i
        else:
            l_score += i

    return l_score - a_score


def solution(n, info):
    info.reverse()
    answer = [-1]

    max_diff = -1
    # 352,715 가지
    for a in cwr(range(11), n):
        comb = [0] * 11
        for _a in a:
            comb[_a] += 1

        # score
        score_diff = score(info, comb)
        if score_diff > 0 and max_diff < score_diff:
            max_diff = score_diff
            answer = comb

    answer.reverse()
    return answer