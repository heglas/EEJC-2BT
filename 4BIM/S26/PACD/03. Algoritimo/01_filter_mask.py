# Extraído de: [DADOS]ANO1C2B4S26_C.pdf. Fonte: PDF do usuário. fileciteturn1file0
# Exemplo: Filtrando linhas com base em valores de colunas (máscara booleana)
import pandas as pd

def main():
    data = {
        'Date': ['April-10', 'April-11', 'April-12', 'April-13', 'April-14', 'April-16'],
        'Sales': [200, 300, 400, 200, 300, 300],
        'Price': [3, 1, 2, 4, 3, 2]
    }
    df = pd.DataFrame(data)
    # Criando uma máscara booleana para Sales igual a 300
    dfmask = df['Sales'] == 300
    # Aplicando a máscara para filtrar o DataFrame
    df_filtrado = df[dfmask]
    print('=== df_filtrado (Sales == 300) ===')
    print(df_filtrado)

if __name__ == '__main__':
    main()
