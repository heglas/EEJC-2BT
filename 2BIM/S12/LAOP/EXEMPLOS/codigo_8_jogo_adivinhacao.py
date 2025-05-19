import random
numero_secreto = random.randint(1, 10)
tentativas = 0
palpites = [3, 7, 5, numero_secreto]  # Simulação de entrada

for tentativa in palpites:
    tentativas += 1
    if tentativa < numero_secreto:
        print(f"Tentativa {tentativas}: Muito baixo!")
    elif tentativa > numero_secreto:
        print(f"Tentativa {tentativas}: Muito alto!")
    else:
        print(f"Tentativa {tentativas}: Correto! Total de tentativas: {tentativas}")
        break