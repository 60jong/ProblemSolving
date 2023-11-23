# # 1
# def dfs(idx, sheep, wolf, possible):
#     global g_info, answer, graph
#     if g_info[idx] == 0:
#         sheep += 1
#         answer = max(answer, sheep)
#     else:
#         wolf += 1
#
#     if wolf >= sheep:
#         return
#
#     possible.extend(graph[idx])
#     for p in possible:
#         dfs(p, sheep, wolf, [i for i in possible if i != p])
#
#
# def solution(info, edges):
#     global answer, g_info, visited, graph
#     answer = 0
#     g_info = info
#     n = len(info)
#     graph = [[] for _ in range(n)]
#
#     for a, b in edges:
#         graph[a].append(b)
#
#     dfs(0, 0, 0, [])
#     return answer
# 2

info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

answer = 1
def dfs(tree, visited, s, w):
    global answer

    answer = max(answer, s)
    # w가 s보다 크거나 같은 경우
    if w >= s:
        return

    for v in visited:
        for e, a in tree[v]:
            if e not in visited:
                # count
                if a == 0:
                    s += 1
                else:
                    w += 1
                # visited
                visited.add(e)

                dfs(tree, visited, s, w)

                # count 복구
                if a == 0:
                    s -= 1
                else:
                    w -= 1
                # visited 복구
                visited.remove(e)

def solution(info, edges):
    global answer
    tree = [[] for _ in range(len(info))]
    for f, t in edges:
        tree[f].append((t, info[t]))

    dfs(tree, {0}, 1, 0)

    return answer

print(solution(info, edges))
