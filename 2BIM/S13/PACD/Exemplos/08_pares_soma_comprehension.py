pares_soma = [(x, y, x + y) for x in range(2) for y in range(2, 4) if (x + y) % 2 == 0]
print(pares_soma)