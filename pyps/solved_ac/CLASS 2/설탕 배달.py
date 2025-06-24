total = int(input())

div, mod = divmod(total,5)
if mod == 0:
    print(div)
elif mod == 1:
    div += 1
    print(div)
elif mod == 2:
    if div == 1:
        print(-1)
    else:
        div += 2
        print(div)
elif mod == 3:
    div += 1
    print(div)
else:
    if div == 0:
        print(-1)
    else:
        div+=2
        print(div)
