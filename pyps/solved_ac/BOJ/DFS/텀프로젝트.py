import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().strip().split()))
    visited = [False] * N

