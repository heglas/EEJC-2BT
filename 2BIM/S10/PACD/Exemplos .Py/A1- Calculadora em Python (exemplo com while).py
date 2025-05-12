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
            resultado = numero1 + numero2
            print("Resultado: ", resultado)
        elif escolha == '2':
            resultado = numero1 - numero2
            print("Resultado: ", resultado)
        elif escolha == '3':
            resultado = numero1 * numero2
            print("Resultado: ", resultado)
        elif escolha == '4':
            if numero2 != 0:
                resultado = numero1 / numero2
                print("Resultado: ", resultado)
            else:
                print("Erro: Divisão por zero")
    else:
        print("Escolha inválida. Por favor, escolha uma operação válida.")