frutas = {
    'maçã': 2.5,
    'banana': 1.0,
    'uva': 3.0,
    'morango': 4.5,
    'laranja': 2.0,
    'abacaxi': 5.0,
    'kiwi': 3.5,
    'melancia': 6.0,
    'pêssego': 4.0,
    'manga': 3.8
}

# 5. Valor do abacaxi
print(frutas['abacaxi'])

# 6. Valor do melão (usando get para evitar erro)
print(frutas.get('melão', 'Não encontrado'))

# 7. Atualizar preço do kiwi para 4
frutas['kiwi'] = 4.0

# 8. Remover manga
del frutas['manga']

# 9. Adicionar goiaba
frutas['goiaba'] = 2.8
