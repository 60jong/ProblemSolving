N = int(input())
M = int(input())
if M > 0:
    broken = list(map(int, input().split()))
else:
    broken = list()

def canMake(made, canTouch):
    if made < 0:
        return False
    elif made == 0:
        return made in canTouch

    while made > 0:
        m = made % 10
        if m not in canTouch:
            return False
        made = made // 10
    return True

def getNearestTouched(target, canTouch):
    offset = 0
    while True:
        if canMake(target - offset, canTouch):
            touches = len(str(target - offset))
            if offset + touches > abs(target - 100):
                return (100, 0)
            else:
                return (target - offset, touches)
        elif canMake(target + offset, canTouch):
            touches = len(str(target + offset))
            # 누르고 하나씩 이동 > 그냥 이동, 굳이 누르지 말기
            if offset + touches > abs(target - 100):
                return (100, 0)
            else:
                return (target + offset, touches)
        else:
            offset += 1

canTouch = []
for i in range(10):
    if i not in broken:
        canTouch.append(i)

nearest, touches = getNearestTouched(N, canTouch)
print(touches + abs(N - nearest))