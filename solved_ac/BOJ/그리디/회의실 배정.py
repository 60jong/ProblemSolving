import sys

count = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(count)]

data = sorted(data, key=lambda x: (x[1], x[0]))

schedule = [data[0]]

for i in range(1,len(data)):
    # 회의 시작 시간 >= 마지막 회의의 끝나는 시간
    if data[i][0] >= schedule[-1][1]:
        schedule.append(data[i])

print(len(schedule))
