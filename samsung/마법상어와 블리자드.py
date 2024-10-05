N, M, N2 = 0, 0, 0
R, C = 0, 0
grid = []
array = [-1]
dirs = [-1, 7, 3, 1, 5]
exploded = [0, 0, 0, 0]
def flatten_grid():
    r, c = R, C
    hw, vw = 1, 1 # vw 홀-왼 / 짝-오 | hw 홀-아 / 짝-위

    stop = False
    while not stop:
        d = -1 if hw % 2 == 1 else 1
        for _ in range(hw):
            c += d
            if c < 0:
                stop = True
                break
            array.append(grid[r][c])
        if stop:
            break
        hw += 1

        d = 1 if vw % 2 == 1 else -1
        for _ in range(vw):
            r += d
            if r < 0:
                break
            array.append(grid[r][c])
        vw += 1


def move_and_explode(start_idx, end_idx):
    while True:
        if end_idx == N2:
            break

        if array[start_idx] == array[end_idx]:
            end_idx += 1
        elif array[end_idx] != 0:
            start_idx = end_idx
        else:
            # Count zeros
            zeros = 0
            while True:
                if end_idx == N2:
                    break
                if array[end_idx] == 0:
                    zeros += 1
                    end_idx += 1
                    continue

                if array[end_idx] == array[start_idx]:
                    end_idx += 1
                else:
                    break

            biz_count = end_idx - start_idx - zeros
            print(biz_count, array[start_idx])
            if biz_count >= 4:
                exploded[array[start_idx]] += biz_count
                for i in range(start_idx, end_idx):
                    array[i] = 0
                start_idx = start_idx - 1
                while array[start_idx] == 0 or array[start_idx] == array[start_idx - 1]:
                    if start_idx == 1:
                        start_idx = end_idx
                        break
                    start_idx -= 1
                end_idx = start_idx
            else:
                start_idx = end_idx

def blizzard(dir, dist):
    global array

    # Destroy
    d_idx = dirs[dir]
    arr_idx = 0
    for d in range(dist):
        arr_idx = arr_idx + d_idx + 8 * d
        array[arr_idx] = 0
    # Move & Explode
    start_idx = 1
    while start_idx < N2 and array[start_idx] == 0:
        start_idx += 1
    end_idx = start_idx

    # Move and Explode
    move_and_explode(start_idx, end_idx)

    # Grouping
    new_array = [-1]
    start_idx = 1
    while start_idx < N2 and array[start_idx] == 0:
        start_idx += 1
    end_idx = start_idx
    zeros = 0
    while True:
        if end_idx == N2:
            if start_idx < N2:
                biz_count = end_idx - start_idx - zeros
                new_array.append(biz_count)
                new_array.append(array[start_idx])
            break
        if array[end_idx] == 0:
            zeros += 1
            end_idx += 1
        elif array[end_idx] == array[start_idx]:
            end_idx += 1
        else:
            biz_count = end_idx - start_idx - zeros
            new_array.append(biz_count)
            if len(new_array) >= N2:
                break
            new_array.append(array[start_idx])
            if len(new_array) >= N2:
                break

            start_idx = end_idx
            zeros = 0
    while len(new_array) < N2:
        new_array.append(0)

    array = new_array
    return


N, M = map(int, input().strip().split())
N2 = N ** 2
# Shark position
R, C = (N - 1) // 2, (N - 1) // 2

for _ in range(N):
    grid.append(list(map(int, input().strip().split())))

flatten_grid()

for _ in range(M):
    dir, dist = map(int, input().strip().split())
    blizzard(dir, dist)

answer = 1 * exploded[1] + 2 * exploded[2] + 3 * exploded[3]
print(answer)
