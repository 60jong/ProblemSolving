from heapq import heappop, heappush


def solution(jobs):
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    answer, start, i, now, = 0, -1, 0, 0,
    N = len(jobs)
    heap = []

    while i < N:
        for j in jobs:
            if start < j[0] <= now:
                heappush(heap, (j[1], j[0]))
        if len(heap) > 0:
            b, a = heappop(heap)
            start = now
            now += b
            answer += now - a
            i += 1
        else:
            now += 1

    return answer // N