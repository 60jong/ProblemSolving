import sys
from collections import deque

input = sys.stdin.readline


def add_node(nodes, m, p, c, d):
    global t_id

    if p == -1:
        nodes[m] = [t_id, m, -1, c, d, []]
        t_id += 1
        return

    if len(nodes[p][5]) > 0: # Depth doesn't increase
        nodes[p][5].append(m)
        nodes[m] = [nodes[p][0], m, p, c, d, []]
    else: # Depth increases
        # Check addable
        cur_d = 2
        cur_p = p
        while cur_p != -1:
            if nodes[cur_p][4] >= cur_d:
                cur_d += 1
                cur_p = nodes[cur_p][2]
            else:
                break

        if cur_p == -1: # Addable
            nodes[p][5].append(m)
            nodes[m] = [nodes[p][0], m, p, c, d, []]


def update_color(nodes, m, c):
    nodes[m][3] = c
    q = deque(nodes[m][5])

    while q:
        id = q.popleft()
        nodes[id][3] = c
        q.extend(nodes[id][5])


def calculate_score(nodes, m):
    children = nodes[m][5]

    sum = 0
    colors = set()
    colors.add(nodes[m][3])
    for child in children:
        score, color_set = calculate_score(nodes, child)

        sum += score

        colors.update(color_set)

    sum += len(colors) ** 2
    return sum, colors


def get_score(nodes, roots):
    answer = 0

    for root in roots:
        score, color_set = calculate_score(nodes, root)
        answer += score
    return answer


Q = int(input())

t_id = 0

# [t_id, m_id, p_id, color, max_depth, children]
nodes = [[] for _ in range(100_001)]
roots = []

for _ in range(Q):
    cmd = list(map(int, input().strip().split()))

    if cmd[0] == 100:
        m_id, p_id, color, max_depth = cmd[1], cmd[2], cmd[3], cmd[4]
        if p_id == -1:
            roots.append(m_id)

        add_node(nodes, m_id, p_id, color, max_depth)
    elif cmd[0] == 200:
        m_id, color = cmd[1], cmd[2]
        update_color(nodes, m_id, color)
    elif cmd[0] == 300:
        m_id = cmd[1]
        print(nodes[m_id][3])
    else: # cmd[0 == 400
        print(get_score(nodes, roots))
