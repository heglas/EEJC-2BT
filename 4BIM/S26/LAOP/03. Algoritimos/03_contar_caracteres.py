# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def contar_caracteres(texto, caractere):
    contagem = 0
    for char in texto:
        if char == caractere:
            contagem += 1
    return contagem

if __name__ == '__main__':
    texto = "Exemplo de texto para contar caracteres"
    caractere = 'e'
    print(contar_caracteres(texto, caractere))
