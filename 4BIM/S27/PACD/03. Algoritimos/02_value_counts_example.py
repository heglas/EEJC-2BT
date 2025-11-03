import pandas as pd

def exemplo_value_counts():
    data = ['A', 'B', 'A', 'C', 'B', 'A']
    df = pd.DataFrame({'Categoria': data})
    print(df['Categoria'].value_counts())

if __name__ == '__main__':
    exemplo_value_counts()