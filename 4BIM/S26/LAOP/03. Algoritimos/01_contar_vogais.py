# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contagem = 0
    for char in texto:
        if char in vogais:
            contagem += 1
    return contagem

if __name__ == '__main__':
    texto = "Exemplo de texto para contar vogais"
    print(contar_vogais(texto))
