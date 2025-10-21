# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def somar_elementos(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

if __name__ == '__main__':
    numeros = [1,2,3,4,5]
    print(somar_elementos(numeros))
