# Extraído de: [DADOS]ANO1C2B4S26_C.pdf. fileciteturn1file1
# Exemplo: Merge entre DataFrames com chave comum
import pandas as pd

def main():
    clientes = pd.DataFrame({
        'IDcliente': [1, 2, 3],
        'nome': ['Joao', 'Maria', 'Pedro'],
        'idade': [30, 25, 22]
    })

    pedidos = pd.DataFrame({
        'IDcliente': [1, 1, 2, 3],
        'produto': ['Camisa', 'Tenis', 'Celular', 'Notebook'],
        'valor': [50, 120, 800, 2500]
    })

    df_merge = clientes.merge(pedidos, on='IDcliente', how='inner')
    print('=== Merge clientes x pedidos ===')
    print(df_merge)

if __name__ == '__main__':
    main()
