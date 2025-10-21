# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def produto_elementos(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto

if __name__ == '__main__':
    numeros = [1,2,3,4,5]
    print(produto_elementos(numeros))
