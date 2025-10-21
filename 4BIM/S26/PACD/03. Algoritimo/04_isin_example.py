# Extraído de: [DADOS]ANO1C2B4S26_C.pdf. fileciteturn1file0
# Exemplo: Selecionando linhas com múltiplos valores possíveis usando .isin()
import pandas as pd

def main():
    df_funcionarios = pd.DataFrame({
        'nome': ['Carlos', 'Ana', 'Marcos', 'Fernanda'],
        'cargo': ['Gerente', 'Atendente', 'Vendedor', 'Diretora'],
        'salario': [5000, 2500, 3200, 7000]
    })
    cargos_desejados = ['Gerente', 'Diretora']
    df_filtrado = df_funcionarios[df_funcionarios['cargo'].isin(cargos_desejados)]
    print('=== Funcionarios com cargos desejados ===')
    print(df_filtrado)

if __name__ == '__main__':
    main()
