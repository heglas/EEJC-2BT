# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def media_valores(lista):
    total = 0
    contagem = 0
    for numero in lista:
        total += numero
        contagem += 1
    return total / contagem if contagem != 0 else 0

if __name__ == '__main__':
    numeros = [1,2,3,4,5]
    print(media_valores(numeros))
