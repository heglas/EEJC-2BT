# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def contar_elementos(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    return contagem

if __name__ == '__main__':
    elementos = ['a', 'b', 'a', 'c', 'b', 'a']
    print(contar_elementos(elementos))
