import sys
from heapq import heappush, heappop

# input
n = int(sys.stdin.readline().strip())
cards = []
for _ in range(n):
    heappush(cards, int(sys.stdin.readline().strip()))

total = 0

while len(cards) > 1:
    # 카드 수가 최소인 두 카드 추출
    a = heappop(cards)
    b = heappop(cards)

    total = total + (a + b)

    # 두 카드 더한 것을 heap에 추가
    heappush(cards, (a + b))

print(total)
