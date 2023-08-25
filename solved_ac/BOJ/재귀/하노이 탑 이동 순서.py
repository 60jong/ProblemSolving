N = int(input())
def moveBelow(f, t, num):
    global count

    if num == 1:
        print(f, t, sep=' ')
        return
    moveBelow(f, 6 - f - t, num - 1)
    print(f, t, sep=' ')
    moveBelow(6 - f - t, t, num - 1)

print(2 ** N - 1)
moveBelow(1, 3, N)
