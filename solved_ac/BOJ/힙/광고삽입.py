from heapq import heappush, heappop

def to_num(time):
    a = time.split(":")
    return int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])

def to_str(num):
    hour = num // 3600
    minute = (num - hour * 3600) // 60
    sec = num - hour * 3600 - minute * 60

    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2)


def solution(play_time, adv_time, logs):
    num_adv_time = to_num(adv_time)
    num_play_time = to_num(play_time)

    cv_logs = [(0, 0)]
    for log in logs:
        s, e = log.split("-")
        cv_logs.append((to_num(s), to_num(e)))
    cv_logs = sorted(cv_logs, key=lambda x: (x[0], x[1]))

    accum_time = [[0, i] for i in range(len(cv_logs))]

    q_p, q_c = [], []
    heappush(q_p, (num_adv_time, 0))
    for i in range(1, len(cv_logs)):
        # q_p
        start_time = cv_logs[i][0]
        # 끝난 광고 pop
        while q_p and start_time >= q_p[0][0]:
            heappop(q_p)
        # 진행 중인 광고 누적
        cp_q_p = q_p[:]
        while cp_q_p and start_time < cp_q_p[0][0]:
            adv_end_time, idx = heappop(cp_q_p)
            accum_time[idx][0] = min(num_play_time, accum_time[idx][0] + adv_end_time - start_time)
        heappush(q_p, (min(num_play_time, start_time + num_adv_time), i))
        accum_time[i][0] = min(num_play_time, num_play_time, accum_time[i][0] + num_adv_time)

        # q_c
        cur_adv_end_time = start_time + num_adv_time
        while q_c and start_time >= q_c[0][0]:
            heappop(q_c)
        cp_q_c = q_c[:]
        while cp_q_c and cur_adv_end_time > cp_q_c[0][0]:
            play_end_time, idx = heappop(cp_q_c)
            accum_time[i][0] = min(num_play_time, accum_time[i][0] + cur_adv_end_time - play_end_time)
        heappush(q_c, (min(num_play_time, cv_logs[i][1]), i))

    accum_time = sorted(accum_time, key=lambda x: (-x[0], x[1]))
    return to_str(cv_logs[accum_time[0][1]][0])