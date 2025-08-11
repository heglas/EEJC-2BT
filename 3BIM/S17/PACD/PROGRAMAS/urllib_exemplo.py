from urllib import request

resposta = request.urlopen('https://www.example.com')
print(resposta.read().decode('utf-8'))
