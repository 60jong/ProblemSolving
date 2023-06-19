import sys

cnt = int(sys.stdin.readline().strip())
minutes = list(map(int, sys.stdin.readline().strip().split()))

minutes.sort()

result = 0
for minute in minutes:
    result = result + (cnt * minute)
    cnt = cnt - 1

print(result)