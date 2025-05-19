senha_correta = "1234"
senha_digitada = ""

# Simulação de entrada correta na 3ª tentativa
tentativas = ["1111", "2222", "1234"]
for tentativa in tentativas:
    senha_digitada = tentativa
    if senha_digitada == senha_correta:
        break
print("Acesso concedido" if senha_digitada == senha_correta else "Acesso negado")