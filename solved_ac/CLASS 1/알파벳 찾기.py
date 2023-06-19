import string

strings = input()
ascii_lower = string.ascii_lowercase

rtnList = []
for a in ascii_lower:
    rtnList.append(str(strings.find(a)))
    rtnList.append(' ')
print(''.join(rtnList))