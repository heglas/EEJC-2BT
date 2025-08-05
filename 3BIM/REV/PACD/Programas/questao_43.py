# Questão 43
# Classifica as temperaturas em categorias

temperaturas = [-5, 0, 10, 16, 25, 32]
'''
#A
for temp in temperaturas: 
    if temp <= 0: 
        print("PERIGO") 
    elif temp < 15: 
        print("FRIO") 
    elif temp <= 30: 
        print("AGRADÁVEL") 
    else: 
        print("CALOR") 
'''
#B
'''
for temp in temperaturas: 
    if temp < 0: 
        print("PERIGO") 
    elif temp <= 15: 
        print("FRIO") 
    elif temp < 30: 
        print("AGRADÁVEL") 
    else: 
        print("CALOR")
'''

#C
for temp in temperaturas:
    if temp <= 0:
        print("PERIGO")
    elif temp < 15:
        print("FRIO")
    elif temp <= 30:
        print("AGRADÁVEL")
    else:
        print("CALOR")


#D
'''
for temp in temperaturas: 
    if temp < 0: 
        print("PERIGO") 
    elif temp < 16: 
        print("FRIO") 
    elif temp <= 30: 
        print("AGRADÁVEL") 
    else: 
        print("CALOR")
'''

#E
'''for temp in temperaturas: 
    if temp <= 0: 
        print("PERIGO") 
    elif temp <= 15: 
        print("FRIO") 
    elif temp <= 30: 
        print("AGRADÁVEL") 
    else: 
        print("CALOR")
'''