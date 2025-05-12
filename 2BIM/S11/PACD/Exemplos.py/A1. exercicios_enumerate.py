# 1. Enumerar lista de cores
cores = ['vermelho', 'verde', 'azul', 'amarelo', 'roxo']
for indice, cor in enumerate(cores, start=1):
    print(f'Indice: {indice}, Cor: {cor}')

# 2. Enumerar lista de cores começando em 6
for indice, cor in enumerate(cores, start=6):
    print(f'Indice: {indice}, Cor: {cor}')

# 3. Enumerar caracteres de uma string
frase = "Adoro estudar!"
for indice, caractere in enumerate(frase):
    print(f'Indice: {indice}, Caractere: {caractere}')
