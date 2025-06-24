import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().strip())

heap = []

row = list(map(int,sys.stdin.readline().strip().split()))