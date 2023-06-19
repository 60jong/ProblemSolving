from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

row = len(relation)
col = len(relation[0])

combi = list()

for c in range(1,col+1):
    combi.extend(combinations(range(col),c))

unique = []

for i in combi:
    tmp = []
    tmp = [tuple(item[key] for key in i) for item in relation]
    if len(set(tmp)) == row:
        put = True
        for x in unique:
            if set(x).issubset(i):
                put = False
        if put : unique.append(i)
print(unique)




# def isUniq(relation):
#     if len(relation) == len(set(relation)):
#         return True
#     else:
#         return False
# #
# def rmElement(relation, idx):
#     for r in relation:
#         del r[idx]
#     return relation
#
# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# temp = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
#
# # print(relation)
# #
# # ckList = [0] * len(relation[0])
# # print(len(relation[0]))
# # tempList = list()
# #
# # for i in range(len(relation[0])):
# #     tempList.clear()
# #     for r in relation:
# #         tempList.append(r[i])
# #     if len(tempList) == len(set(tempList)):
# #         ckList[i] = 1
# #
# # print(ckList)
#
#
#
#
#
# def solution(relation):
#     inLen = len(relation[0])
#     outLen = len(relation)
#     testingList = list()
#     temp = relation.copy()
#     for i in reversed(range(inLen)):
#         testingList.clear()
#         for j in range(outLen):
#             testingList.append(relation[j][i])
#         if isUniq(testingList):
#             global cnt
#             cnt += 1
#             rmElement(temp, i)
#
#
# solution(relation)
#






