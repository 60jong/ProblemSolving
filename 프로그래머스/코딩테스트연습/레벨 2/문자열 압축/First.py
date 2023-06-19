s = "aaaabbcc"

s_list = []
minLen = len(s)
print(minLen)
for i in range(len(s)):
    s_list.clear()
    s_list = [s[j:j+(i+1)] for j in range(0,len(s),i+1)]
    print(s_list)

    t = 1
    cnt = 1
    temp = []
    while t < len(s_list):
        cnt = 1

        if s_list[t-1] != s_list[t]:
            temp.append(str(s_list[t-1]))
            if t == len(s_list)-1:
                temp.append(str(s_list[t]))
            t += 1
            continue
        else:
            temp.append(s_list[t-1])
            while s_list[t-1] == s_list[t]:
                cnt += 1
                t += 1
                if(t == len(s_list)):
                    t+=1
                    break
            t+=1
            if cnt > 1:
                temp.append(str(cnt))
    if(minLen >= len("".join(temp))):
        minLen = len("".join(temp))

answer =minLen
print(minLen)