def solution(board, moves):
    answer = 0
    cnt = 0
    bucket = []

    boardTmp = []
    for l in zip(*board):
        boardTmp.append(list(map(int, l)))

    for n in moves:
        for idx, i in enumerate(boardTmp[n - 1]):
            if i != 0:
                bucket.append(i)
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        cnt += 2
                        bucket = bucket[:-2]
                boardTmp[n - 1][idx] = 0
                break

    return cnt