# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
import cProfile

def analisar_dados(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

if __name__ == '__main__':
    numeros = list(range(100000))
    cProfile.run('analisar_dados(numeros)')
