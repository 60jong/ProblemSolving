zeros = 0

def fill_up(board, i, j):
    while i > 0 and board[i - 1][j] != 6:
        i -= 1
        board[i][j] = '#'
    return board

def fill_down(board, i, j):
    while i < len(board) - 1 and board[i + 1][j] != 6:
        i += 1
        board[i][j] = '#'
    return board

def fill_left(board, i, j):
    while j > 0 and board[i][j - 1] != 6:
        j -= 1
        board[i][j] = '#'
    return board

def fill_right(board, i, j):
    while j < len(board[0]) - 1 and board[i][j + 1] != 6:
        j += 1
        board[i][j] = '#'
    return board

def func(board, cctv, k, N):
    global zeros

    # base condition
    if k == len(cctv):
        count_zero = 0
        for b in board:
            for _b in b:
                if _b == 0:
                    count_zero += 1
        zeros = min(zeros, count_zero)
        return

    i, j, num = cctv[k]
    if num == 1: # 4방향
        # 상
        func(fill_up([b[:] for b in board], i, j), cctv, k + 1, N)

        # 우
        func(fill_right([b[:] for b in board], i, j), cctv, k + 1, N)

        # 하
        func(fill_down([b[:] for b in board], i, j), cctv, k + 1, N)

        # 좌
        func(fill_left([b[:] for b in board], i, j), cctv, k + 1, N)

    elif num == 2:
        # 상하
        up_filled_board = fill_up([b[:] for b in board], i, j)
        func(fill_down(up_filled_board, i, j), cctv, k + 1, N)

        # 좌우
        left_filled_board = fill_left([b[:] for b in board], i, j)
        func(fill_right(left_filled_board, i, j), cctv, k + 1, N)

    elif num == 3:
        # 상우
        up_filled_board = fill_up([b[:] for b in board], i, j)
        func(fill_right(up_filled_board, i, j), cctv, k + 1, N)

        # 우하
        right_filled_board = fill_right([b[:] for b in board], i, j)
        func(fill_down(right_filled_board, i, j), cctv, k + 1, N)

        # 하좌
        down_filled_board = fill_down([b[:] for b in board], i, j)
        func(fill_left(down_filled_board, i, j), cctv, k + 1, N)

        # 좌상
        left_filled_board = fill_left([b[:] for b in board], i, j)
        func(fill_up(left_filled_board, i, j), cctv, k + 1, N)

    elif num == 4:
        # 상 제외
        right_filled_board = fill_right([b[:] for b in board], i, j)
        down_filled_board = fill_down(right_filled_board, i, j)
        func(fill_left(down_filled_board, i, j), cctv, k + 1, N)

        # 우 제외
        down_filled_board = fill_down([b[:] for b in board], i, j)
        left_filled_board = fill_left(down_filled_board, i, j)
        func(fill_up(left_filled_board, i, j), cctv, k + 1, N)

        # 하 제외
        left_filled_board = fill_left([b[:] for b in board], i, j)
        up_filled_board = fill_up(left_filled_board, i, j)
        func(fill_right(up_filled_board, i, j), cctv, k + 1, N)

        # 좌 제외
        up_filled_board = fill_up([b[:] for b in board], i, j)
        right_filled_board = fill_right(up_filled_board, i, j)
        func(fill_down(right_filled_board, i, j), cctv, k + 1, N)
    else:
        up_filled_board = fill_up([b[:] for b in board], i, j)
        right_filled_board = fill_right(up_filled_board, i, j)
        down_filled_board = fill_down(right_filled_board, i, j)
        func(fill_left(down_filled_board, i, j), cctv, k + 1, N)

def solution():
    global zeros

    N, M = map(int, input().strip().split())

    board = []
    cctv = []
    for n in range(N):
        row = list(map(int, input().strip().split()))
        board.append(row)
        for idx, r in enumerate(row):
            if r == 0:
                zeros += 1
            elif 1 <= r <= 5:
                cctv.append((n, idx, r))

    if cctv:
        func(board, cctv, 0, N)
    return zeros

print(solution())