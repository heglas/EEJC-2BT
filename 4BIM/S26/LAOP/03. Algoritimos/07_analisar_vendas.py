# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def analisar_vendas(vendas):
    contagem_vendas = {}
    receita_total = {}

    for produto, quantidade, preco in vendas:
        if produto in contagem_vendas:
            contagem_vendas[produto] += quantidade
            receita_total[produto] += quantidade * preco
        else:
            contagem_vendas[produto] = quantidade
            receita_total[produto] = quantidade * preco

    return contagem_vendas, receita_total

if __name__ == '__main__':
    vendas = [
        ('Produto A', 10, 5.0),
        ('Produto B', 5, 12.0),
        ('Produto A', 3, 5.0),
        ('Produto C', 8, 7.5),
        ('Produto B', 7, 12.0)
    ]
    contagem, receita = analisar_vendas(vendas)
    print(contagem)
    print(receita)
