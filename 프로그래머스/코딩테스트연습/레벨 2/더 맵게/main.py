import heapq


def solution(s, K):
    answer = 0

    heapq.heapify(s)
    while s[0] < K:
        if len(s) >= 2:
            heapq.heappush(s, heapq.heappop(s) + 2 * heapq.heappop(s))
            answer += 1
        else:
            answer = -1
            break

    return answer