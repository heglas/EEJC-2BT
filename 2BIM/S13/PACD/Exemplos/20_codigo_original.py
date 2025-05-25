def fatorial(n): 
    if n==0 or n==1:
        return 1
    else:
        return n*fatorial(n-1)

numeros=[]
for i in range(5): 
    numeros.append(i+1)
print(numeros)

if numeros[0]<3:
    print("menor que 3")
else:
    print("maior ou igual a 3")

fatoriais = []
for i in numeros:
    fatoriais.append(fatorial(i))
print(fatoriais)