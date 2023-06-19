def setMatrix(rows, columns):
    mat = [[0] * columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = n
            n += 1
    return mat


def solution(rows, columns, queries):
    answer = []
    matrix = setMatrix(rows, columns)



    for query in queries:
        indexList = []
        matrixTemp = [row[:] for row in matrix]
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1

        min = matrix[x1][y1]
        # > 방향
        for y in range(y1, y2):
            if matrix[x1][y] < min:
                min = matrix[x1][y]
            indexList.append([x1, y])
            # v 방향
        for x in range(x1, x2):
            if matrix[x][y2] < min:
                min = matrix[x][y2]
            indexList.append([x, y2])
        # < 방향
        for y in range(y2, y1, -1):
            if matrix[x2][y] < min:
                min = matrix[x2][y]
            indexList.append([x2, y])
        # ^ 방향
        for x in range(x2, x1, -1):
            if matrix[x][y1] < min:
                min = matrix[x][y1]
            indexList.append([x, y1])
        answer.append(min)
        print(indexList)

        # rotate-clockwise
        rotatedIndexList = indexList.copy()

        rotatedIndexList.insert(0, rotatedIndexList[-1])
        del rotatedIndexList[-1]
        print(rotatedIndexList)

        for i in range(len(indexList)):
            matrix[indexList[i][0]][indexList[i][1]] = matrixTemp[rotatedIndexList[i][0]][rotatedIndexList[i][1]]
        print('matrix : '+str(matrix))
    return answer


print(solution(3,4,[[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]))