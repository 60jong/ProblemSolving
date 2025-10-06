import sys

input = sys.stdin.readline

N = int(input())
loc = {}

for _ in range(N):
    x, a = map(int, input().split())
    loc[x] = a

loc_keys = sorted(loc.keys())

ld = 0
la = 0

rd = 0
ra = 0
for i in range(1, N):
    rd += (loc_keys[i] - loc_keys[0]) * loc[loc_keys[i]]
    ra += loc[loc_keys[i]]

dist = rd
min_x = loc_keys[0]
prev_x = loc_keys[0]

for i in range(1, N):
    x = loc_keys[i]
    d = x - prev_x
    
    la += loc[prev_x]
    ld += d * la
    
    rd -= d * ra
    ra -= loc[x]
    
    cd = ld + rd

    if cd < dist:
        dist = cd
        min_x = x
    prev_x = x

print(min_x)