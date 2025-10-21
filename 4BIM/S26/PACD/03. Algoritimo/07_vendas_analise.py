# Exemplo prático extraído do PDF e reconstruído onde o texto estava truncado.
# Fonte: [DADOS]ANO1C2B4S26_C.pdf. Algumas listas no PDF estavam truncadas; ajustei para tornar o script executável. fileciteturn1file2
import pandas as pd

def main():
    vendas = pd.DataFrame({
        'Data': pd.date_range(start='2024-05-01', periods=10, freq='D'),
        'QuantidadeVendida': [48, 38, 24, 17, 30, 48, 28, 32, 20, 20],
        'Sabor': ['Baunilha', 'Creme', 'Creme', 'Creme', 'Baunilha', 'Baunilha', 'Baunilha', 'Morango', 'Creme', 'Baunilha']
    })

    vendas_novas = pd.DataFrame({
        'Data': pd.date_range(start='2024-05-11', periods=10, freq='D'),
        'QuantidadeVendida': [33, 45, 49, 33, 12, 31, 11, 33, 39, 47],
        'Sabor': ['Baunilha', 'Morango', 'Baunilha', 'Creme', 'Baunilha', 'Creme', 'Creme', 'Morango', 'Baunilha', 'Creme']
    })

    # Concatenando as tabelas de vendas
    vendas_completas = pd.concat([vendas, vendas_novas], ignore_index=True)

    precos = pd.DataFrame({
        'Sabor': ['Baunilha', 'Chocolate', 'Morango', 'Creme'],
        'Preco': [5.0, 6.0, 5.5, 4.5]
    })

    # Merge entre vendas e preços
    vendas_completas = vendas_completas.merge(precos, on='Sabor', how='left')

    # Filtrando receitas acima de 200 (quantidade * preco)
    vendas_completas['Receita'] = vendas_completas['QuantidadeVendida'] * vendas_completas['Preco']

    filtro_receita = vendas_completas[vendas_completas['Receita'] > 200]

    print('=== Vendas com Receita > 200 ===')
    print(filtro_receita)

if __name__ == '__main__':
    main()
