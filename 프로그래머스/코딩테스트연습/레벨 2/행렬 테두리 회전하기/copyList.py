listA = [[0] * 10 for _ in range(10)]
listB = []
for _ in range(100):
    listB = [item[:] for item in listA]

listA[0][0] = 1

print(listA)
print(listB)



listC = [[(15*j) + (i+1) for i in range(15)] for j in range(10)  ]
print(listC)

print(abs(1-2))