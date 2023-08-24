import sys

input = sys.stdin.readline

def solution():
    ### set up
    h, w = map(int, input().split())

    graph = []
    men_queue = []
    dists = [[int(1e9)] * w for _ in range(h)]
    fire_queue = []
    for _y in range(h):
        row = list(input().strip())
        graph.append(row)
        for _x in range(w):
            if row[_x] == 'J':
                men_queue.append((_y, _x, 0))
                dists[_y][_x] = 0
            elif row[_x] == 'F':
                fire_queue.append((_y, _x))
    ###

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while men_queue:
        # fire
        fq_len = len(fire_queue)
        for _ in range(fq_len):
            fy, fx = fire_queue.pop(0)
            for d in dirs:
                nfy, nfx = d[0] + fy, d[1] + fx
                if (0 <= nfy < h and 0 <= nfx < w) and graph[nfy][nfx] == '.':
                    graph[nfy][nfx] = 'F'
                    fire_queue.append((nfy, nfx))

        # men
        mq_len = len(men_queue)
        for _ in range(mq_len):
            y, x, dist = men_queue.pop(0)
            for d in dirs:
                ny, nx, nd = d[0] + y, d[1] + x, dist + 1

                if not 0 <= ny < h or not 0 <= nx < w:

                    # 탈출 성공
                    return nd
                else:
                    if nd < dists[ny][nx] and graph[ny][nx] == '.':
                        dists[ny][nx] = nd
                        men_queue.append((ny, nx, nd))
    return 0

result = solution()
print(result if result > 0 else 'IMPOSSIBLE')