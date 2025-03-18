op=input("Entre com A para Soma, S para subtraçao, D para divisão e M para Multiplicação")
if (op!="A" and op!="S" and op!="D" and op!="M"):
    print("Erro: operaçao não reconhecida")
else:
    opr1 = int(input("entre com o primeiro valor:"))
    opr2=int(input("entre com o segundo valor:"))
    if(op=="SOMA"):
        result = opr1 + opr2
    elif(op=="SUBTRAÇÃO"):
        result = opr1 - opr2
    elif(op=="DIVISÃO"):
         result = opr1 / opr2
    elif(op=="MULTIPLICAÇÃO"):
        result = opr1 * opr2
    print (result,"\n")
