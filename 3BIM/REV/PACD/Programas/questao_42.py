# Questão 42
# Retorna o preço final aplicando o desconto

#A
#def calcular_preco(preco, desconto): 
#    preco_final = preco - (preco * desconto / 100)
#    print(preco_final)


#B
def calcular_preco(preco, desconto):
    preco_final = preco - (preco * desconto / 100)
    return preco_final

#C
#def calcular_preco(preco, desconto): 
#    preco = preco - (preco * desconto / 100)

#D
#def calcular_preco(preco, desconto): 
#    return print(preco - (preco * desconto / 100))

#E
#def calcular_preco(preco, desconto):
#return preco - preco * 100 / desconto



# Exemplo de uso
preco_original = 100
desconto_percentual = int(input("Digite o percentual de desconto: "))
print("Preço com desconto:", calcular_preco(preco_original, desconto_percentual))
