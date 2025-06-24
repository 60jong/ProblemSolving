keyboard = ["a", "b", "c", "d", "e", ], ["f", "g", "h", "i", "j", ], ["k", "l", "m", "n", "o", ]

word = "dj"

char_list = list()
char_loc = [[] for _ in range(len(word))]
distRes = []

for i in range(len(word)):
    char_list.append(word[i])
    for j in range(len(keyboard)):
        for k in range(len(keyboard[j])):
            if (keyboard[j][k] == word[i]):
                char_loc[i].extend(tuple([j, k]))
    if (len(char_loc[i])) == 0:
        char_loc[i].extend("X")

if len(set(char_list)) == 1:
    answer = list([0, 1])
    print(answer)
print(char_loc)
t = 0
while (True):
    if t == len(char_loc) - 1:
        break
    if len(char_loc[t]) == 1:
        distRes.append(20)
        t += 1
    else:
        if len(char_loc[t + 1]) == 1:
            distRes.append(20)
            t += 1
        else:
            dist = []
            if (len(char_loc[t + 1]) == 2):
                res = abs(char_loc[t][0] - char_loc[t + 1][0]) + abs(char_loc[t][1] - char_loc[t + 1][1])
                distRes.append(res)

print(distRes)

