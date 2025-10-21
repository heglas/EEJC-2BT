# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def contar_palavras(texto):
    palavras = texto.split()
    contagem = len(palavras)
    return contagem

if __name__ == '__main__':
    texto = "Exemplo de texto para contar vogais e palavras"
    print(contar_palavras(texto))
