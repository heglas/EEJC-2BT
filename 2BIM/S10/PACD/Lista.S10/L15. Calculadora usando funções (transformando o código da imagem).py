def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def calculadora():
    print("Essa é uma calculadora!")
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        escolha = input("Digite o número da operação desejada: ")
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até a próxima!")
            break
        if escolha in ['1', '2', '3', '4']:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            if escolha == '1':
                print("Resultado: ", somar(numero1, numero2))
            elif escolha == '2':
                print("Resultado: ", subtrair(numero1, numero2))
            elif escolha == '3':
                print("Resultado: ", multiplicar(numero1, numero2))
            elif escolha == '4':
                print("Resultado: ", dividir(numero1, numero2))
        else:
            print("Escolha inválida. Por favor, escolha uma operação válida.")

# Para rodar a calculadora, chame:
# calculadora()