# insert() remove() 남발 금지 | O(N)이기 때문
import string

a = [1,2,3,4,5,6,7,8,9]
remove_set = [3,5]
insert_set = [0,0]

result_r = [i for i in a if i not in remove_set]





new_id = "..ARDSG*#$%#$..^-."
print(new_id)

# step 1
new_id = new_id.lower()


# step 2
symbols = string.punctuation.replace(".","").replace("-","").replace("_","")

for c in new_id:
    if c in symbols:
        new_id = new_id.replace(c, "")


# step 3
while new_id.find("..") != -1 :
    new_id = new_id.replace("..", ".")


# step 4
new_id = new_id.strip(".")


# step 5
if len(new_id) == 0 :
    new_id = "a"

# step 6
if len(new_id) > 15 :
    new_id = new_id[0:15]
new_id = new_id.rstrip(".")

# step 7
if len(new_id) < 3 :
    while len(new_id) < 3 :
        new_id += new_id[-1]

