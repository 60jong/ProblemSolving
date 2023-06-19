keyboard = ["배","달","의","민","족"],["카","카","오","토","스"],["네","이","버"," ","굿"],["쿠","팡","당","근","마"]
word = "카굿카놀토"

char_list = list()
char_loc = [[] for _ in range(len(word))]
distRes = []
answer = []
for i in range(len(word)):
    char_list.append(word[i])
    for j in range(len(keyboard)):
        for k in range(len(keyboard[j])):
            if (keyboard[j][k] == word[i]):
                char_loc[i].extend(tuple([j+k]))
    if (len(char_loc[i])) == 0:
        char_loc[i].extend("X")

if len(set(char_list)) == 1:
    answer = list([0, 1])
    print(answer)
print(char_loc)

char_loc = [[1,2],[6], [4,8],[5],['X'],[4]]
print(char_loc)
t = 0
while (True):
    if t == len(char_loc) - 1:
        break

    if len(char_loc[t]) > 1:
        char_loc[t] = list([char_loc[t][0]])
        print(char_loc)
    if char_loc[t][0] == "X":
        t += 1
    else:
        if char_loc[t + 1][0] == "X":
            distRes.append(20)
            t += 1
        else:
            dist = []

            if (len(char_loc[t + 1]) == 1):
                res = abs(char_loc[t][0] - char_loc[t+1][0])
                distRes.append(res)
                t+=1
            elif (len(char_loc[t+1]) > 1):
                for s in range(len(char_loc[t+1])):
                    res = abs(char_loc[t][0] - char_loc[t + 1][s])
                    if(dist.count(res) != 0):
                        break
                    dist.append(res)
                print(dist)
                minDist = dist[0]
                for s in range(len(dist)):
                    if dist[s] < minDist:
                        minDist = dist[s]
                        char_loc[t+1] = list([char_loc[t+1][s]])
                distRes.append(minDist)
                t+=1



print(sum(distRes))
print(distRes)


answer.append(sum(distRes))
answer.append(len(distRes))
print(answer)
