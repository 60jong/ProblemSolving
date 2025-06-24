s = "-1 -2 -3 -4"

s_list = s.split(" ")

for i in range(len(s_list)):
    s_list[i] = int(s_list[i])

s_list.sort()
answer = str(s_list[0]) + " " + str(s_list[-1])
print(answer)