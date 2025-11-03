import pandas as pd

def frutas_value_counts():
    data = ['Maçã', 'Banana', 'Maçã', 'Laranja', 'Banana']
    df = pd.DataFrame({'Fruta': data})
    print(df['Fruta'].value_counts())

if __name__ == '__main__':
    frutas_value_counts()