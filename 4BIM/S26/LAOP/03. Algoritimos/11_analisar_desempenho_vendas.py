# Extraído e reconstruído a partir de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
# Havia uma linha truncada no PDF ao calcular a média de vendas por dia; reconstituí a lógica.
def analisar_desempenho_vendas(vendas):
    contagem_vendas = {}
    receita_total = {}
    soma_vendas_dia = {}
    dias_por_produto = {}

    for produto, quantidade, preco, dia in vendas:
        # Atualizar contagem total vendida por produto
        contagem_vendas[produto] = contagem_vendas.get(produto, 0) + quantidade
        # Atualizar receita
        receita_total[produto] = receita_total.get(produto, 0) + quantidade * preco
        # Atualizar soma de vendas por dia (acumula quantidade)
        soma_vendas_dia[produto] = soma_vendas_dia.get(produto, 0) + quantidade
        # Atualizar conjunto de dias nos quais houve vendas
        dias_por_produto.setdefault(produto, set()).add(dia)

    # Calcular média de vendas diárias por produto
    media_vendas_dia = {}
    for produto in contagem_vendas:
        dias = len(dias_por_produto.get(produto, set()))
        media_vendas_dia[produto] = soma_vendas_dia.get(produto, 0) / dias if dias > 0 else 0

    return contagem_vendas, receita_total, media_vendas_dia

if __name__ == '__main__':
    vendas_exemplo = [
        ('Produto A', 10, 5.0, 1),
        ('Produto B', 5, 12.0, 1),
        ('Produto A', 3, 5.0, 2),
        ('Produto C', 8, 7.5, 2),
        ('Produto B', 7, 12.0, 3)
    ]

    contagem, receita, media = analisar_desempenho_vendas(vendas_exemplo)
    print(contagem)
    print(receita)
    print(media)
