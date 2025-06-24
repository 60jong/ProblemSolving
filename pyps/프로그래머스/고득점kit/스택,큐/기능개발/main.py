progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
durations = []
answer = []
for i in range(len(progresses)):
    if (100 - progresses[i]) % speeds[i] > 0:
        durations.append(
            (100 - progresses[i]) // speeds[i] + 1)
    else:
        durations.append(
            (100 - progresses[i]) // speeds[i]
        )

maxDur = durations[0]
cnt = 0
while True:
    if len(durations) == 0:
        answer.append(cnt)
        break
    popVal = durations.pop(0)

    if popVal > maxDur:
        answer.append(cnt)
        maxDur = popVal
        cnt = 1
    else:
        cnt += 1

print(answer)
