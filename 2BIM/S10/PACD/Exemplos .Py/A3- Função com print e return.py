def soma(a, b):
    resultado = a + b
    print("print do resultado dentro da função: ", resultado)  # apenas mostra na tela
    return resultado  # retorna um resultado/saída da função

resultado = soma(2, 3)
media = resultado / 2
print(f'A média é {media}')
# Saída:
# print do resultado dentro da função: 5
# A média é 2.5
