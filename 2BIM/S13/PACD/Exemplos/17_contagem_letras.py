texto = "exemplo de texto"
contagem = {letra: texto.count(letra) for letra in texto if letra != ' '}
print(contagem)