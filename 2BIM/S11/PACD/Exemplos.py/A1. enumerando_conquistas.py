# Enumerando conquistas em um jogo
conquistas = ['Primeira Vitória', 'Derrotou o Chefe Final', 'Coletou o Tesouro Secreto']
indice = 1
for conquista in conquistas:
    print(f'Conquista {indice}: {conquista}')
    indice += 1

# Função para imprimir conquistas com parâmetro padrão
def imprimir_conquistas(conquistas, start=1):
    indice = start
    for conquista in conquistas:
        print(f'Conquista {indice}: {conquista}')
        indice += 1

# Exemplos de uso
conquistas = ['Primeira Vitória', 'Derrotou o Chefe Final', 'Coletou o Tesouro Secreto']
imprimir_conquistas(conquistas)
imprimir_conquistas(conquistas, start=1)
imprimir_conquistas(conquistas, start=10)
# imprimir_conquistas(start=1) # Gera TypeError