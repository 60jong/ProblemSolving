import sys
from collections import deque

input=sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    remain = N
    nums = list(map(int,input().strip().split()))
    visited = [False] * N
    q = deque()
    for i in range(N):
        team_made = False
        if not visited[i]:
            q.append(nums[i]-1)
            visited[i] = True
        temp = []
        while q:
            next_i = q.popleft()

            # 사이클 존재
            if next_i == i:
                team_made = True
                remain -= len(temp) + 1
                for t in temp:
                    visited[t] = True
                break

            if not visited[next_i]:
                q.append(nums[next_i]-1)
                visited[next_i] = True
                temp.append(next_i)
        if not team_made:
            for t in temp:
                visited[t] = False

    print(remain)