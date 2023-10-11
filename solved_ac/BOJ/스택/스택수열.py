N = 8
idx = 1
result = []
s = []
for _ in range(8):
    a = int(input())

    if idx < a:
        while idx < a:
            s.append(idx)
            result.append("+")
            idx += 1
        s.pop()
        result.append("-")
    else:
        while s[-1] < a:
            s.pop()
            result.append("-")



