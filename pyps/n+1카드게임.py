# import math
#
# # 에라토스테네스의 체
# num = 81
#
# nums = [i for i in range(2, num + 1)]
# checked = [False * len(nums)]
#
#

x = 10

def foo():
    x = 1

    def bar():
        nonlocal x
        x = 5
        print(x)
    bar()
    print(x)
foo()
print(x)