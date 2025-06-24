citation=[8,10,10,15,17,22,24,28,32,42,47]
h = len(citation)

while h > 0:
    over = []
    for c in citation:
        if c >= h:
            over.append(c)
    if len(over) >= h:
        answer = h
        break
    else:
        h -= 1

print(h)

