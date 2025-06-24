# def mount(p_per_n, summits, gates, intensity):
#     for s in summits:
#         stack = [s]
#         visited = [False] * len(p_per_n)
#         visited[s] = True

#         while stack:
#             node = stack.pop()

#             if node in gates:
#                 return (True, s)

#             for n, w in p_per_n[node]:
#                 if w <= intensity and not visited[n] and not n in summits:
#                     stack.append(n)
#                     visited[n] = True
#     return (False, None)

# def solution(n, paths, gates, summits):
#     hash_summits = dict(zip(sorted(summits), [0]*len(summits)))

#     p_per_n = [[] * (n + 1) for _ in range(n + 1)]
#     w_set = set()
#     for a, b, w in paths:
#         p_per_n[a].append((b, w))
#         p_per_n[b].append((a, w))
#         w_set.add(w)

#     weights = sorted(list(w_set))

#     start = 0
#     end = len(weights) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         success, summit = mount(p_per_n, hash_summits, gates, weights[mid])
#         if success:
#             end = mid - 1
#             answer_summit = summit
#         else:
#             start = mid + 1
#     return [answer_summit, weights[start if start > end else end]]
from heapq import heappush, heappop


def solution(n, paths, gates, summits):
    answer = [summits[0], int(1e9)]
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    summits = set(summits)
    intensities = [int(1e9)] * (n + 1)
    h = []
    for g in gates:
        h.append((0, g))
        intensities[g] = 0

    while h:
        itst, node = heappop(h)

        if itst > intensities[node]: continue
        if node in summits:
            if answer[1] >= itst:
                if answer[1] > itst:
                    answer = [node, itst]
                else:
                    answer = [min(answer[0], node), itst]
            continue

        for nn, cost in graph[node]:
            cur_itst = max(cost, itst)
            if intensities[nn] > cur_itst:
                intensities[nn] = cur_itst
                heappush(h, (cur_itst, nn))
    return answer