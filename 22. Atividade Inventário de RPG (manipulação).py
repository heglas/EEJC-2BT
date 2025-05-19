inventario_jogador = {'armas': 3, 'poções': 5, 'armaduras': 2, 'moedas': 100, 'energia': [2, 1, 5]}

# a) Aumentar moedas para 500
inventario_jogador['moedas'] = 500

# b) Imprimir valor de armas
print(inventario_jogador['armas'])

# c) Apagar chave 'armaduras'
del inventario_jogador['armaduras']

# d) Inserir 'armaduras_poderosas': 10
inventario_jogador['armaduras_poderosas'] = 10

# e) Substituir energia 1 por 3
# energia está na posição 1 (índice 1)
inventario_jogador['energia'][1] = 3
