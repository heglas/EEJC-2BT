import random

print("Bem-vindo ao Jogo Par ou Ímpar!")
while True:
    escolha = input("Escolha [P]ar ou [Í]mpar: ").strip().upper()
    numero_usuario = int(input("Escolha um número entre 1 e 10: "))
    numero_computador = random.randint(1, 10)
    soma = numero_usuario + numero_computador
    print(f"Você escolheu {numero_usuario} e o computador escolheu {numero_computador}.")
    if (escolha == "P" and soma % 2 == 0) or (escolha == "Í" and soma % 2 != 0):
        print(f"Você ganhou! A soma é {soma}")
    else:
        print(f"Você perdeu! A soma é {soma}")
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break
