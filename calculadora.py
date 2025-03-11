op = input ("entre com a operacao desejada")
if ((op != "soma") and (op != "sub")and (op != "div") and (op != "mult")):
    print ("erro : operação ñ reconhecida","/n")
else:
    opr1 = ("entre c/ o 1º operador")
    opr2 = ("entre c/ o 2º operador")
if(op == "soma"):
    r = int(opr1) + int (opr2)
elif (op == "sub"):
    r = int (opr1) - int (opr2)
elif(op1 == "div"):
    r = int (opr1) / int (opr2)
elif(opr == "mult"):
    r = int (opr1) * int (opr2)
print ("mostre o resultado" + str (r))