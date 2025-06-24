import re

equation = input()
nums = list(map(int,re.split(r'[+-]', equation)))
operators = ["+", "-"]
op = list()
for i in equation:
    if i in operators:
        op.append(i)

while '+' in op:
    for i, j in enumerate(op):
        if j == '+':
            index = i
            break
    nums[index] = nums[index] + nums[index + 1]
    del nums[index + 1]
    del op[index]

if len(nums) > 1:
    result = 2 * nums[0]
    for num in nums:
        result = result - num

    print(result)
else:
    print(nums[0])

