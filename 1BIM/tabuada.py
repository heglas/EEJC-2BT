a=1 ##inicialização do contador

m = input("insira o multiplicador:")

while(a<=10):
    resultado = a*int(m)
    print(str(m)+"X"+str(a)+"="+str(resultado))
    a+=1
    ##loop principal
4