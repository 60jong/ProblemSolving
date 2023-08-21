# A, B, C = map(int, input().split())
#
# mod_store = []
# for i in range(1, B + 1):
#     stop = False
#     mod = A ** i % C
#     for j in range(len(mod_store)):
#         if mod_store[j] == mod:
#             repeats = len(mod_store) - j
#             offset = (B - i + 1) % repeats - 1
#             mod = mod_store[j:][offset]
#             stop = True
#             break
#     else:
#         mod_store.append(mod)
#     if stop:
#         break
# print(mod)

A, B, C = map(int, input().split())

def fpow(a, b, c):
    if b == 1:
        return a % c

    x = fpow(a, b // 2, c)
    if b & 1: # 홀수
        return x * x * a % c
    else:
        return x * x % c

print(fpow(A, B, C))
