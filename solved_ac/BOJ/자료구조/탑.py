import sys

N = int(sys.stdin.readline().strip())

stack = []
result = [0]
line = [0]
line.extend(list(map(int,sys.stdin.readline().strip().split())))

for i in range(1, len(line)):
    print(result)
    if line[i] < line[i - 1]:
        result.append(i - 1)
    else:
        # 앞의 것이 향하는 index
        temp = result[i - 1]
        while True:
            if line[temp] == 0:
                result.append(temp)
                break
            elif line[temp] <= line[i]:
                temp = result[temp]
            else:
                result.append(temp)
                break
print(" ".join(map(str, result[1:])))
# for i, _l in enumerate(line):
#     l = int(_l)
#     if len(stack) == 0:
#         stack.append((l, i + 1))
#         result.append(0)
#     else:
#         while len(stack) > 0 and stack[-1][0] <= l:
#             stack.pop()
#         if len(stack) == 0:
#             result.append(0)
#         else:
#             result.append(stack[-1][1])
#         stack.append((l, i + 1))
#
# answer = ''
# for r in result:
#     answer += '{} '.format(r)
# print(answer.strip())