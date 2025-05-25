def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numeros = [i + 1 for i in range(5)]
print(numeros)

if numeros[0] < 3:
    print("menor que 3")
else:
    print("maior ou igual a 3")

fatoriais = [fatorial(i) for i in numeros]
print(fatoriais)