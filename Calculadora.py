op = input("entre com a operação: (SOMA, SUBTRAÇÃO, DIVISÃO ou MULTIPLICAÇÃO)")
if (op!="SOMA"and op!="SUBTRACAO" and op!="SUBTRAÇÃO" and op!="DIVISÃO" and op!="MULTIPLICAÇÃO"):
    print("ERRO: operação não reconhecida","\n")
else:
    opr1 = int(input("entre com o primeiro valor:"))
    opr2 = int(input("entre com o segundo valor:"))
    if(op=="SOMA"):
        result = opr1 + opr2
    elif(op=="SUBTRAÇÃO"):
        result = opr1 - opr2
    elif(op=="DIVISÃO"):
         result = opr1 / opr2
    elif(op=="MULTIPLICAÇÃO"):
        result = opr1 * opr2
    print (result,"\n")
