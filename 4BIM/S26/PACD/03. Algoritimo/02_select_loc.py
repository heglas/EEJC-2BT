# Extraído de: [DADOS]ANO1C2B4S26_C.pdf. Fonte: PDF do usuário. fileciteturn1file0
# Exemplo: Selecionando linhas e colunas específicas usando .loc
import pandas as pd

def main():
    data = {
        'Date': ['April-10', 'April-11', 'April-12', 'April-13', 'April-14', 'April-16'],
        'Sales': [200, 300, 400, 200, 300, 300],
        'Price': [3, 1, 2, 4, 3, 2]
    }
    df = pd.DataFrame(data)
    # Selecionar apenas as colunas 'Date' e 'Sales' onde Sales = 300
    df_selecionado = df.loc[df['Sales'] == 300, ['Date', 'Sales']]
    print('=== df_selecionado (Date, Sales where Sales == 300) ===')
    print(df_selecionado)

if __name__ == '__main__':
    main()
