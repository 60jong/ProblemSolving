# def canLay(row, rowIdx, colIdx):
#     for i in range(0, rowIdx):
#         # 열
#         if row[i] == colIdx:
#             return False
#         # 대각선
#         if abs(rowIdx - i) == abs(colIdx - row[i]):
#             return False
#
#     return True
#
#
# def dfs(row, rowIdx, colIdx):
#     tempRow = row[:]
#     tempRow[rowIdx] = colIdx
#
#     global count
#     if rowIdx == N - 1:
#         count += 1
#         return
#
#     for i in range(N):
#         if canLay(tempRow, rowIdx + 1, i):
#             dfs(tempRow, rowIdx + 1, i)
#
#
# N = int(input())
#
# row = [0] * N
# count = 0
# visited = [False] * N
#
# for i in range(N):
#     dfs(row, 0, i)
#
# print(count)
def do(col, x, j):

    return a

N = int(input())

col = [0] * N
for i in range(N):
    returned = do(col, i, j)