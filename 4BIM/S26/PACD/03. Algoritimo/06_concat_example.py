# Extraído de: [DADOS]ANO1C2B4S26_C.pdf. fileciteturn1file1
# Exemplo: Concatenação vertical e horizontal
import pandas as pd

def main():
    df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']})
    df2 = pd.DataFrame({'col1': [3, 4, 5], 'col2': ['C', 'D', 'E']})

    # Concatenação vertical (eixo 0) com reset de índice
    df_concat_axis0 = pd.concat([df1, df2], ignore_index=True, axis=0)
    print('=== Concat vertical (axis=0) ===')
    print(df_concat_axis0)

    # Concatenação horizontal (eixo 1)
    df_concat_axis1 = pd.concat([df1, df2], axis=1)
    print('=== Concat horizontal (axis=1) ===')
    print(df_concat_axis1)

if __name__ == '__main__':
    main()
