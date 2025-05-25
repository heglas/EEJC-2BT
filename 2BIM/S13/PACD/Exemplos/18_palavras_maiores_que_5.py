frase = "Python é uma linguagem de programação incrível"
palavras_maiores = [palavra for palavra in frase.split() if len(palavra) > 5]
print(palavras_maiores)