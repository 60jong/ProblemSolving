array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer=[]

for c in commands:
    temp = array[c[0]-1:c[1]]
    temp.sort()
    answer.append(temp[c[2]-1])

print(answer)
