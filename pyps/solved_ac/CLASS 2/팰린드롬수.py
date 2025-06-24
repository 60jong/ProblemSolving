

while True:
    num = input()
    if num == '0':
        break
    reversedNum = ''.join(reversed(list(map(str, num))))

    if int(num) == int(reversedNum):
        print('yes')
    else:
        print('no')
