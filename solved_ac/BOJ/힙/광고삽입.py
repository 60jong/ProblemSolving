def to_num(time):
    a = time.split(":")
    return int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])

def to_str(num):
    hour = num // 3600
    minute = (num - hour * 3600) // 60
    sec = num - hour * 3600 - minute * 60

    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2)

def solution(play_time, adv_time, logs):
    pts = play_time.split(':')
    N = int(pts[0]) * 3600 + int(pts[1]) * 60 + int(pts[2]) + 1
    accum = [0] * N
    for log in logs:
        start, end = log.split('-')
        start_num, end_num = to_num(start), to_num(end)
        accum[start_num] = accum[start_num] + 1 
        accum[end_num] = accum[end_num] - 1
    for i in range(N - 1):
        accum[i + 1] = accum[i] + accum[i + 1]

    nat = to_num(adv_time)
    cur_sum = sum(accum[:nat])
    max_sum = cur_sum
    t_idx = 0
    for i in range(1, (N - nat) + 1):
        cur_sum = cur_sum - accum[i - 1] + accum[(i - 1) + nat]
        if cur_sum > max_sum:
            max_sum = cur_sum
            t_idx = i

    return to_str(t_idx)