# Baseado no trecho do PDF. Algumas linhas estavam truncadas no PDF; reconstruí a condição.
# Fonte: [DADOS]ANO1C2B4S26_C.pdf. fileciteturn1file0
import pandas as pd

def main():
    df_vendas = pd.DataFrame({
        'produto': ['Notebook', 'Celular', 'Camisa', 'Tenis'],
        'preco': [2500, 800, 50, 120],
        'data': ['2023-01-10', '2023-03-15', '2023-05-22', '2023-04-01']
    })
    # converter data para datetime para comparação correta
    df_vendas['data'] = pd.to_datetime(df_vendas['data'])
    # Selecionar produtos com 'preco' entre 50 e 100 e data maior que '2023-01-01'
    df_filtrado = df_vendas[(df_vendas['preco'] >= 50) & (df_vendas['preco'] <= 100) & (df_vendas['data'] > pd.to_datetime('2023-01-01'))]
    print('=== Produtos com preco entre 50 e 100 e data > 2023-01-01 ===')
    print(df_filtrado)

if __name__ == '__main__':
    main()
