s = "a"

resultList = []
resultLenList = []
for i in range(1,(len(s) // 2) +1):
    result = ""
    temp = s[0:i]
    cnt = 1
    for j in range(i,len(s),i):
        if s[j:j+i] == temp:
            cnt += 1
        else:
            if cnt > 1:
                result += "".join([str(cnt), temp])
            else:
                result += "".join([temp])
            temp = s[j:j+i]
            cnt=1
    if cnt > 1:
        result += "".join([str(cnt), temp])
    else:
        result += "".join([temp])
    resultList.append(result)
    resultLenList.append(len(result))

print(resultList)
print(min(resultLenList))

