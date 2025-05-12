# Exemplo 1: enumerate em listas
frutas = ['maçã', 'banana', 'laranja']
for indice, valor in enumerate(frutas):
    print(f'Indice: {indice}, Valor: {valor}')

# Exemplo 2: enumerate em string
frase = "Python é incrível!"
for indice, letra in enumerate(frase, start=1):
    print(f'Indice: {indice}, Letra: {letra}')

# Exemplo 3: enumerate em tupla
pontos_cardeais = ('Norte', 'Sul', 'Leste', 'Oeste')
for indice, ponto_cardeal in enumerate(pontos_cardeais, start=1):
    print(f'Indice: {indice}, Ponto Cardeal: {ponto_cardeal}')

# Exemplo 4: enumerate em dicionário
pessoas = {'João': 25, 'Maria': 30, 'Pedro': 28}
for indice, (nome, idade) in enumerate(pessoas.items(), start=1):
    print(f'Indice: {indice}, Nome: {nome}, Idade: {idade} anos')
