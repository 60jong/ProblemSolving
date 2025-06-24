# 1 큐
from collections import deque


def solution(queue1, queue2):
    N = len(queue1)
    q1 = deque(queue1)
    q2 = deque(queue2)

    # total 합 -> target
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    if total % 2 == 1: return -1

    diff = total // 2 - sum1
    count = 0
    while len(q1) > 0 and len(q2) > 0 and diff != 0:
        if count >= 4 * N:
            return -1
        # q1 기준
        if diff < 0:
            p = q1.popleft()
            q2.append(p)
            diff += p
        else:
            p = q2.popleft()
            q1.append(p)
            diff -= p
        count += 1
    if diff == 0:
        return count
    else:
        return -1
# 2 투 포인터