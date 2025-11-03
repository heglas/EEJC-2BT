import pandas as pd

def groupby_aggs_example():
    frutasdata = {
        'Fruta': ['Maçã', 'Banana', 'Laranja', 'Uva', 'Maçã', 'Abacaxi', 'Morango', 'Melancia', 'Kiwi', 'Pera'],
        'Mercado': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
        'Quantidade': [10, 15, 8, 12, 20, 14, 18, 25, 9, 11]
    }
    dffrutas = pd.DataFrame(frutasdata)
    print("Média por grupo:\n", dffrutas.groupby(['Fruta', 'Mercado'])['Quantidade'].mean())
    print("Mínimo por mercado:\n", dffrutas.groupby(['Mercado'])['Quantidade'].min())
    print("Máximo por mercado:\n", dffrutas.groupby(['Mercado'])['Quantidade'].max())

if __name__ == '__main__':
    groupby_aggs_example()