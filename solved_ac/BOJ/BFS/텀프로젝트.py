import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    remain = N
    nums = list(map(int, input().strip().split()))
    visited = [False] * N
    q = deque()
    for i in range(N):
        temp = dict()
        seq = 0

        if not visited[i]:
            visited[i] = True
            q.append(nums[i] - 1)
            temp[i] = seq
            seq += 1

        while q:
            next_i = q.popleft()

            # 사이클 존재
            if next_i in temp:
                cycle_len = len(temp) - temp[next_i]
                remain -= cycle_len
                break

            if not visited[next_i]:
                visited[next_i] = True
                q.append(nums[next_i] - 1)
                temp[next_i] = seq
                seq += 1
    print(remain)
