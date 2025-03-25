x=int(input("2 p/ verificação PRIMO"))
c=2
while(c<x):
     if(x%c):
         print("ñ divisivel por"+str(c))
     else:
         print("ñ é primo!")
     c+=1