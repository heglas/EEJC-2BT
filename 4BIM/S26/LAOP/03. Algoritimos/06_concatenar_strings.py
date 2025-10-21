# Extraído de: [DADOS]ANO1C3B4S27_C.pdf. fileciteturn2file0
def concatenar_strings(lista):
    resultado = ""
    for string in lista:
        resultado += string
    return resultado.strip()

if __name__ == '__main__':
    strings = ["Este", " ", "é", " ", "um", " ", "exemplo"]
    print(concatenar_strings(strings))
