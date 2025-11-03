import pandas as pd

def groupby_sum_example():
    frutasdata = {
        'Fruta': ['Maçã', 'Banana', 'Laranja', 'Uva', 'Maçã', 'Abacaxi', 'Morango', 'Melancia', 'Kiwi', 'Pera'],
        'Mercado': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
        'Quantidade': [10, 15, 8, 12, 20, 14, 18, 25, 9, 11]
    }
    dffrutas = pd.DataFrame(frutasdata)
    print("Soma por fruta:\n", dffrutas.groupby('Fruta')['Quantidade'].sum())
    print("Soma por mercado:\n", dffrutas.groupby('Mercado')['Quantidade'].sum())
    print("Soma por fruta e mercado:\n", dffrutas.groupby(['Fruta', 'Mercado'])['Quantidade'].sum())

if __name__ == '__main__':
    groupby_sum_example()