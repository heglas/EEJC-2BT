# 1. Imprimir produtos com índice
def imprimir_produtos(produtos):
    for indice, produto in enumerate(produtos, start=1):
        print(f'Produto {indice}: {produto}')

produtos = ['Computador', 'Mouse', 'Teclado']
imprimir_produtos(produtos)

# 2. Calcular média de notas
def calcular_media(notas):
    return sum(notas) / len(notas)

notas_alunos = [8, 7, 5, 9, 6]
media = calcular_media(notas_alunos)
print(f'Média dos alunos: {media}')

# 3. Aumentar salários em 10%
def aumentar_salarios(salarios):
    return [salario * 1.1 for salario in salarios]

salarios = [3000, 5000, 7000]
salarios_aumentados = aumentar_salarios(salarios)
print(f'Salários aumentados: {salarios_aumentados}')

# 4. Imprimir alturas com índice
def imprimir_alturas(alturas):
    for indice, altura in enumerate(alturas, start=1):
        print(f'Aluno {indice}: {altura} cm')

alturas_alunos = [160, 175, 150, 180]
imprimir_alturas(alturas_alunos)
