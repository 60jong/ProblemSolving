import time
from random import randint

array = []
for _ in range(10000):
    array.append(randint(1,100))

array1 = array

start = time.time()
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[j] < min_index:
            min_index = j
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp

end = time.time()

print("선택 정렬 성능 측정 : ",end-start)

start = time.time()
array1.sort()
end= time.time()
print("선택 정렬 성능 측정 : ",end-start)