def calcular_total_transacoes_positivas(transacoes):
    transacoes_positivas = [valor for valor in transacoes if valor > 0]
    total_transacoes_positivas = sum(transacoes_positivas)
    quantidade_transacoes_positivas = len(transacoes_positivas)
    return total_transacoes_positivas, quantidade_transacoes_positivas

def calcular_total_transacoes_negativas(transacoes):
    transacoes_negativas = [valor for valor in transacoes if valor < 0]
    total_transacoes_negativas = sum(transacoes_negativas)
    return total_transacoes_negativas

transacoes = [100, -50, 200, -20, 150, -30, 180]
total_positivas, quantidade_positivas = calcular_total_transacoes_positivas(transacoes)
total_negativas = calcular_total_transacoes_negativas(transacoes)

print("Total das transações positivas:", total_positivas)
print("Quantidade de transações positivas:", quantidade_positivas)
print("Total das transações negativas:", total_negativas)