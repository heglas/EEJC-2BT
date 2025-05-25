pares_soma = []
for x in range(2):
    for y in range(2, 4):
        if (x + y) % 2 == 0:
            pares_soma.append((x, y, x + y))
print(pares_soma)